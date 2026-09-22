# harness-watch

How to stay on top of the open-source **agent harness** ecosystem, and how to tell whether one harness is actually better than another.

> A *harness* is everything around the model: the agent loop, tool set, context/memory management, permission model, retry/stop logic, sandbox, and the prompt/config layer (`AGENTS.md`, skills, hooks, plugins). In 2026 the harness accounts for as much score variance on agentic coding benchmarks as the model does, and far more of the cost variance. This repo is a map and a method, not a catalog.

## Contents

| Doc | What it answers |
|---|---|
| **[`docs/participate.md`](docs/participate.md)** | **Start here to take part:** five communities, contribution norms, a two-week reading path and a completion checklist. |
| [`reports/2026-09-22-community-field-notes.md`](reports/2026-09-22-community-field-notes.md) | Five developments, three experiment histories, five people and three open questions, with proposed versus merged work distinguished. |
| [`drafts/trace-evidence-discussion.md`](drafts/trace-evidence-discussion.md) | A contribution draft connecting GEPA and SoL-Pi; prepared for review, not posted. |
| [`experiments/trace-evidence-pilot.md`](experiments/trace-evidence-pilot.md) | A future evidence-retention experiment with baseline, cases, limits and estimated cost; not run. |
| [`docs/landscape.md`](docs/landscape.md) | Where the ecosystem actually lives (standards, runtimes, config layer, curation, research, regional communities, people). |
| [`docs/monitoring.md`](docs/monitoring.md) | How to scan GitHub, npm, arXiv, HN, Hugging Face, Discords and X on a fixed cadence without drowning. |
| [`docs/benchmarking.md`](docs/benchmarking.md) | How to compare *your* harness against *Joe's* in a way that survives scrutiny, including if yours was auto-evolved. |
| [`docs/providers.md`](docs/providers.md) | Who is running fixed-model harness benchmarks today, and what is still missing. |
| [`sources.yml`](sources.yml) | Machine-readable watchlist: repos, feeds, queries, accounts. |
| [`templates/HARNESS_CARD.md`](templates/HARNESS_CARD.md) | Disclosure template you should publish alongside any score. |
| [`templates/RESULTS.md`](templates/RESULTS.md) | Results template for a harness-vs-harness comparison. |
| [`reports/`](reports/) | Dated research: [landscape survey](reports/2026-09-22-hotspot-survey.md), [participation field notes](reports/2026-09-22-community-field-notes.md), and [PR status evidence](reports/2026-09-22-community-evidence.json), all September 22. |

## The two questions this repo exists to answer

**1. Where is everyone?**
In 2026-09, in four places that do not talk to each other much. (a) Three runtimes above 100k stars where harness components are swappable plugins: DeepSeek Harness (`dsh`, on Cordis), OpenClaw, and Hermes Agent, plus the coding-first minimalists (pi and its forks, mini-swe-agent) and lab-shipped harnesses (ZCode). (b) The config layer on top of Claude Code, Codex and Cursor, shared as skills, hooks and plugins across thousands of repos, with `SKILL.md` as the one portable unit. (c) A research sub-field on *automatically* designing harnesses (Meta-Harness, AHE, SoL-Pi) and on measuring the harness effect (HarnessTax, Scaffold Effect, Harness-Bench). (d) Two young interop standards, UHP and Harness Protocol, trying to make (a) and (b) interchangeable. Real iteration happens in issues, PRs and Discords, and a large share of it is in Chinese. [`docs/landscape.md`](docs/landscape.md) maps it; [`docs/monitoring.md`](docs/monitoring.md) tells you how to watch it.

**2. How do I know my harness is better than yours?**
Hold the model, task set, budget and sandbox resources fixed; vary only the harness; run 5 or more trials per task; report pass rate with paired confidence intervals *and* tokens, latency, and failure fingerprint; publish a Harness Card. If your harness was evolved or tuned against a benchmark, report on a held-out split and against a matched-budget test-time-scaling control. Public leaderboards do not do this. [`docs/benchmarking.md`](docs/benchmarking.md) gives the protocol and the exact tooling (Harbor, Claw-SWE-Bench, HAL harness, HarnessRouter, better-harness).

**Is anyone running that benchmark as a service?**
Partially. HarnessTax (UC Berkeley Sky Lab + Arena.ai, 2026-09-16) is the first third-party fixed-model comparison of the coding CLIs people actually use (Claude Code, Codex CLI, pi): harness moved success by only a few points but cost by up to 5x. Harness-Bench and Claw-SWE-Bench run fixed-model boards for "claw" runtimes. vals.ai re-runs Terminal-Bench under a unified harness. NVIDIA benchmarks pi extensions on request. Nobody yet refreshes a coding-harness board monthly. Details and gaps in [`docs/providers.md`](docs/providers.md).

## Status

Snapshot as of 2026-09-22. The landscape moves monthly; PRs that fix stale links or add sources are welcome. Everything here is opinionated and unaffiliated with any of the projects mentioned.

## License

MIT. See [`LICENSE`](LICENSE).
