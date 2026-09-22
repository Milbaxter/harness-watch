# Monitoring: how to stay on top of it

Start with the **[current hotspot map](hotspots-2026-09-22.md)** and its [evidence snapshot](../data/hotspots-2026-09-22.json). The expanded `sources.yml` adds priority and verification-date fields for new entries.

The problem is not lack of information, it is that the signal is spread over five surfaces with different update rates. The approach below is a fixed cadence per surface plus a small set of saved queries. Budget: about 30 minutes a week once set up.

## Principles

- **Watch queries, not lists.** Awesome-lists lag by weeks. Saved searches on GitHub, npm and arXiv catch new projects the day they get a README.
- **Watch behaviour, not stars.** A repo shipping raw trajectories, ablation results, or a Harness Card is worth more than a 5k-star prompt collection.
- **Separate the layers.** Runtime changes (Layer 1) are rare and important. Config-layer churn (Layer 2) is constant and mostly noise. Papers and benchmarks (Layer 3) arrive in bursts.
- **Keep a changelog.** A single `CHANGELOG.md` or notes file where you record what changed and why you care. After three months it becomes your own map.

## Cadence

| Surface | Cadence | Time |
|---|---|---|
| GitHub: releases and pinned issues on core runtimes | Weekly | 10 min |
| GitHub: saved code/repo searches for new projects | Weekly | 5 min |
| npm / PyPI: new packages by keyword | Weekly | 2 min |
| arXiv: saved queries | Weekly | 5 min |
| Hugging Face: datasets and leaderboards | Bi-weekly | 3 min |
| X / Discord | Daily skim, 5 min, or never. Choose. | 5 min |
| Benchmark leaderboards (tbench.ai, harness-bench.ai, claw-swe-bench.github.io) | Monthly | 5 min |
| Awesome-lists (diff since last visit) | Monthly | 5 min |

## Surface 1: GitHub

### Watch these repos (selective releases, discussions, and design PRs)

Core runtimes: `earendil-works/pi`, `can1357/oh-my-pi`, `SWE-agent/mini-swe-agent`, `OpenHands/OpenHands`, `anomalyco/opencode`, `aaif-goose/goose`.

Benchmarks and eval infra: `harbor-framework/harbor`, `harbor-framework/terminal-bench-2-1` (and successors), `Qihoo360/harness-bench`, `opensquilla/claw-swe-bench`, `princeton-pli/hal-harness`, `reacher-z/HarnessBench`, `nyosegawa/harness-bench`.

Curation: `nexu-io/harness-engineering-guide` (Discussions), `Turi-Labs/awesome-harness`, `Lijunjie2/awesome-agent-harness`, `sadsfae/awesome-claude-code`, `Chat2AnyLLM/awesome-claude-plugins`.

Use Releases and Discussions for a low-volume feed. For invention, additionally inspect selected design PRs and independent packages: release-only monitoring misses work before it ships. Avoid subscribing to every issue or PR; filter by the mechanism you care about.

### Saved repository searches

Sort by recently updated, filter `pushed:>YYYY-MM-DD` to the last week.

```
topic:harness-engineering
topic:agent-harness
topic:pi-package
"agent harness" in:description,readme stars:>20
"harness" "coding agent" in:readme created:>2026-01-01
"harness card" in:readme
"fixed model" harness benchmark in:readme
```

### Saved code searches (find people publishing configs)

```
path:.claude/skills filename:SKILL.md
filename:AGENTS.md "harness"
path:.pi/ extension:ts
path:.cursor/rules
"BaseInstalledAgent" language:Python          # people wrapping their harness for Harbor
"BaseClawAdapter" language:Python             # people wrapping their harness for Claw-SWE-Bench
```

### Topics pages

Bookmark `github.com/topics/harness-engineering`, `/topics/agent-harness`, `/topics/pi-package`, `/topics/claude-code-plugin`. Sort by recently updated.

## Surface 2: Package registries

- npm: search `keywords:pi-package`, `keywords:harness-engineering`, `keywords:agent-harness`, `keywords:claude-code-plugin`. Sort by date.
- PyPI: `harness`, `swe-agent`, `harbor` keyword searches; also watch `mini-swe-agent`, `openhands-sdk`, `harbor` release feeds (`https://pypi.org/rss/project/<name>/releases.xml`).
- Package downloads can supplement activity evidence but are not unique users or a reliable innovation ranking. Historical download counts in older notes should be refreshed before reuse.

## Surface 3: arXiv

Saved queries (cs.SE, cs.AI, cs.CL). Use the arXiv advanced search or an RSS-to-email service.

```
abs:"agent harness"
abs:"harness" AND abs:"coding agent"
abs:"scaffold" AND (abs:"SWE-bench" OR abs:"Terminal-Bench")
abs:"harness card"
abs:"fixed model" AND abs:"harness"
```

Also follow citations of the anchor papers listed in [`landscape.md`](landscape.md) via Semantic Scholar alerts. New harness-benchmark papers almost always cite at least one of: HAL (2510.11977), Stop Comparing (2605.23950), Harness-Bench (2605.27922), Claw-SWE-Bench (2606.12344), Scaffold Effect (2607.22585).

## Surface 4: Hugging Face

- Datasets: `harborframework/*`, `TokenRhythm/Claw-SWE-Bench`, anything tagged `terminal-bench`, `swe-bench`, `agent-trajectories`.
- Published sessions: `badlogicgames/pi-mono` (pi work sessions). Search datasets for `pi-share-hf` to find others doing the same.
- Leaderboard spaces: search Spaces for `harness`, `terminal-bench`, `swe-bench`.

## Surface 5: People and chat

X is where most harness design arguments happen first and where papers get announced. Curate a list of 30 to 50 accounts: maintainers of the Layer 1 runtimes, authors of the papers above, the Terminal-Bench / Harbor / SWE-bench teams, and Anthropic / OpenAI developer-relations people who post about Claude Code and Codex internals. Read the list, not the timeline.

Discords/Slacks worth joining if you are actively building: oh-my-pi, OpenCode, Goose, OpenHands, SWE-bench. Mute everything except announcements and the dev channel.

## Surface 6: Leaderboards

Check monthly, and look for *new harness rows*, not new model rows:

- [tbench.ai](https://www.tbench.ai/leaderboard) (Terminal-Bench): entries list the agent harness; filter one model across harnesses to see spread. Community submissions may be closed at any given time.
- [harness-bench.ai](https://www.harness-bench.ai/leaderboard.html): fixed protocol, model x harness pair view.
- [claw-swe-bench.github.io](https://claw-swe-bench.github.io/): SWE-bench with the harness as the controlled variable.
- Vendor boards that repost harness benchmarks (NEAR AI posted Claw-SWE-Bench Lite runs with trajectories in 2026-06; the repo was not publicly reachable at time of writing). Treat as secondary sources.
- [HAL](https://hal.cs.princeton.edu): paused for new models as of 2026, still the reference for cost-aware reporting.
- SWE-bench "bash only" leaderboard: fixed harness (mini-swe-agent), vary model. The inverse of what you want, but the cleanest model comparison available.

## Automating it

You can do all of the above by hand in 30 minutes a week. If you want a digest:

1. Put the repos, queries and feeds in [`sources.yml`](../sources.yml) (already seeded).
2. A weekly GitHub Action or cron job pulls: new releases for watched repos (GitHub REST `releases/latest`), new repos matching each saved search (GitHub search API, `pushed:>` last 7 days), new arXiv results (arXiv API query, `submittedDate` window), npm search by keyword (`registry.npmjs.org/-/v1/search?text=keywords:pi-package`).
3. Diff against last week's snapshot, write a Markdown digest, open it as an issue or send it to yourself.

This repo deliberately ships the list and the method rather than the script; the script is 100 lines of whatever language you already have a scheduler for, and it goes stale slower if you own it.

## What to record when something new shows up

For each new harness or benchmark, write down:

- Layer (runtime / config / eval).
- Does it publish trajectories? Costs? A Harness Card or equivalent disclosure?
- Which model(s) and benchmark(s) were the claims made on, and was the model held fixed?
- Is it wrappable for Harbor / Claw-SWE-Bench / HAL harness? If not, you cannot compare it to anything.

If the answers are no, no, unclear, no, it is a prompt collection. Note it and move on.
