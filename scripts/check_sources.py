#!/usr/bin/env python3
"""Keep sources.yml and the docs honest.

Checks, in order:

1. sources.yml parses and matches the schema described in its header
   (required keys, allowed layers, allowed watch kinds, no duplicate repos).
2. Every github_repos entry resolves through the GitHub API to the *same*
   full_name. GitHub silently redirects renamed repos, so a watchlist can look
   healthy while pointing at a stale name (badlogic/pi-mono -> earendil-works/pi,
   sst/opencode -> anomalyco/opencode). Renames, 404s and archived repos fail.
   Repos with no push in --stale-days are reported as warnings.
3. Relative links inside docs/, templates/ and README.md point at files that exist.
4. GitHub repo links in the docs (https://github.com/owner/name) that also appear
   in sources.yml are cross-checked so the docs and the watchlist agree.

Usage:
    python3 scripts/check_sources.py            # full run
    python3 scripts/check_sources.py --no-network
    GITHUB_TOKEN=... python3 scripts/check_sources.py --stale-days 120

Exit code is 1 on any error, 0 otherwise. Warnings never fail the run unless
--strict is given. Only dependency: PyYAML.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yml"
DOC_DIRS = [ROOT / "docs", ROOT / "templates", ROOT / "reports"]
DOC_FILES = [ROOT / "README.md", ROOT / "CHANGELOG.md"]

ALLOWED_LAYERS = {"standard", "runtime", "config", "curation", "eval", "infra", "research"}
ALLOWED_WATCH = {"releases", "discussions", "pulls", "commits"}
REQUIRED_TOP_LEVEL = {
    "github_repos": list,
    "github_topics": list,
    "github_repo_searches": list,
    "github_code_searches": list,
    "arxiv_queries": list,
    "arxiv_anchor_papers": list,
    "leaderboards": list,
}
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
GITHUB_LINK_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)(?:[/#?)\s]|$)")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def dump(self, strict: bool) -> int:
        for w in self.warnings:
            print(f"WARN  {w}")
        for e in self.errors:
            print(f"ERROR {e}")
        n_err, n_warn = len(self.errors), len(self.warnings)
        print(f"\n{n_err} error(s), {n_warn} warning(s)")
        if n_err or (strict and n_warn):
            return 1
        return 0


# --------------------------------------------------------------------------- schema


def load_sources(report: Report) -> dict | None:
    try:
        data = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        report.error(f"sources.yml does not parse: {exc}")
        return None
    if not isinstance(data, dict):
        report.error("sources.yml top level must be a mapping")
        return None
    for key, typ in REQUIRED_TOP_LEVEL.items():
        if key not in data:
            report.error(f"sources.yml is missing top-level key `{key}`")
        elif not isinstance(data[key], typ):
            report.error(f"sources.yml `{key}` must be a {typ.__name__}")
    return data


def check_repo_entries(data: dict, report: Report) -> list[dict]:
    entries = data.get("github_repos") or []
    seen: dict[str, int] = {}
    valid: list[dict] = []
    for i, entry in enumerate(entries):
        where = f"github_repos[{i}]"
        if not isinstance(entry, dict):
            report.error(f"{where}: entry must be a mapping")
            continue
        repo = entry.get("repo")
        if not isinstance(repo, str) or not REPO_RE.match(repo):
            report.error(f"{where}: `repo` must look like owner/name, got {repo!r}")
            continue
        where = f"github_repos[{repo}]"
        key = repo.lower()
        if key in seen:
            report.error(f"{where}: duplicate of entry {seen[key]}")
        seen[key] = i
        layer = entry.get("layer")
        if layer not in ALLOWED_LAYERS:
            report.error(f"{where}: layer {layer!r} not in {sorted(ALLOWED_LAYERS)}")
        watch = entry.get("watch")
        if not isinstance(watch, list) or not watch:
            report.error(f"{where}: `watch` must be a non-empty list")
        else:
            bad = [w for w in watch if w not in ALLOWED_WATCH]
            if bad:
                report.error(f"{where}: unknown watch kind(s) {bad}; allowed {sorted(ALLOWED_WATCH)}")
        extra = set(entry) - {"repo", "layer", "watch", "note"}
        if extra:
            report.warn(f"{where}: unexpected key(s) {sorted(extra)}")
        valid.append(entry)
    return valid


# --------------------------------------------------------------------------- github


class GitHub:
    def __init__(self, token: str | None, sleep: float) -> None:
        self.token = token
        self.sleep = sleep
        self.remaining: int | None = None

    def get(self, path: str) -> tuple[int, dict | None]:
        req = urllib.request.Request(
            f"https://api.github.com{path}",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "harness-watch-check-sources",
                **({"Authorization": f"Bearer {self.token}"} if self.token else {}),
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                self.remaining = _int_header(resp.headers.get("X-RateLimit-Remaining"))
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            self.remaining = _int_header(exc.headers.get("X-RateLimit-Remaining"))
            body = None
            try:
                body = json.loads(exc.read().decode("utf-8"))
            except Exception:
                pass
            return exc.code, body
        finally:
            if self.sleep:
                time.sleep(self.sleep)


def _int_header(value: str | None) -> int | None:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def check_repos_live(entries: list[dict], report: Report, gh: GitHub, stale_days: int) -> None:
    now = dt.datetime.now(dt.timezone.utc)
    for entry in entries:
        repo = entry["repo"]
        status, body = gh.get(f"/repos/{repo}")
        if status == 403 and body and "rate limit" in json.dumps(body).lower():
            report.error(
                f"GitHub API rate limit hit at {repo}; set GITHUB_TOKEN or re-run later "
                f"({gh.remaining} requests remaining)"
            )
            return
        if status == 404:
            report.error(f"{repo}: not found on GitHub (deleted, private, or a typo)")
            continue
        if status != 200 or not body:
            report.error(f"{repo}: unexpected GitHub response {status}")
            continue
        canonical = body.get("full_name", "")
        if canonical.lower() != repo.lower():
            report.error(f"{repo}: renamed, canonical name is now {canonical}; update sources.yml and the docs")
        elif canonical != repo:
            report.warn(f"{repo}: casing differs from canonical {canonical}")
        if body.get("archived"):
            report.error(f"{repo}: repository is archived; drop it or move it to a note")
        pushed = body.get("pushed_at")
        if pushed:
            age = (now - dt.datetime.fromisoformat(pushed.replace("Z", "+00:00"))).days
            if age > stale_days:
                report.warn(f"{repo}: no push in {age} days (last {pushed[:10]}); still worth watching?")


# --------------------------------------------------------------------------- docs


def iter_doc_files() -> list[Path]:
    files = [p for p in DOC_FILES if p.exists()]
    for d in DOC_DIRS:
        if d.exists():
            files.extend(sorted(d.rglob("*.md")))
    return files


def check_relative_links(report: Report) -> None:
    for path in iter_doc_files():
        text = path.read_text(encoding="utf-8")
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                rel = path.relative_to(ROOT)
                report.error(f"{rel}: broken relative link -> {match.group(1)}")


def check_doc_repo_links(entries: list[dict], report: Report) -> None:
    """Docs that link to a repo the watchlist knows under a different (old) name are stale."""
    known = {e["repo"].lower(): e["repo"] for e in entries}
    known_names = {}
    for full in known.values():
        known_names.setdefault(full.split("/")[1].lower(), set()).add(full.lower())
    for path in iter_doc_files():
        if path.parent.name == "reports":
            continue  # dated snapshots are allowed to age
        text = path.read_text(encoding="utf-8")
        for match in GITHUB_LINK_RE.finditer(text):
            linked = match.group(1)
            key = linked.lower()
            if key in known:
                continue
            same_name = known_names.get(key.split("/")[1], set()) - {key}
            if same_name:
                rel = path.relative_to(ROOT)
                report.warn(
                    f"{rel}: links github.com/{linked} but sources.yml lists "
                    f"{', '.join(sorted(known[k] for k in same_name))}; possible stale name"
                )


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-network", action="store_true", help="skip the GitHub API checks")
    parser.add_argument("--stale-days", type=int, default=180, help="warn when a repo has no push in N days")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--sleep", type=float, default=0.0, help="seconds to sleep between API calls")
    parser.add_argument("--only", metavar="SUBSTR", help="only hit the API for repos containing SUBSTR (debugging)")
    args = parser.parse_args()

    report = Report()
    data = load_sources(report)
    if data is None:
        return report.dump(args.strict)

    entries = check_repo_entries(data, report)
    check_relative_links(report)
    check_doc_repo_links(entries, report)

    if not args.no_network:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not token:
            report.warn("no GITHUB_TOKEN set; unauthenticated GitHub API allows 60 requests/hour")
        gh = GitHub(token, args.sleep)
        subset = [e for e in entries if not args.only or args.only.lower() in e["repo"].lower()]
        print(f"checking {len(subset)} repos against the GitHub API ...")
        check_repos_live(subset, report, gh, args.stale_days)

    return report.dump(args.strict)


if __name__ == "__main__":
    sys.exit(main())
