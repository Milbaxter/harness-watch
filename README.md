# harness-watch

How to stay on top of the open-source **agent harness** ecosystem, and how to tell whether one harness is actually better than another.

> A *harness* is everything around the model: the agent loop, tool set, context/memory management, permission model, retry/stop logic, sandbox, and the prompt/config layer (`AGENTS.md`, skills, hooks, plugins). In 2026 the harness accounts for as much score variance on agentic coding benchmarks as the model does, and nobody has a shared vocabulary or venue for it yet. This repo is a map and a method, not a catalog.

## Contents

| Doc | What it answers |
|---|---|
| [`docs/landscape.md`](docs/landscape.md) | Where the ecosystem actually lives (runtimes, config layer, curation, research). |
| [`docs/monitoring.md`](docs/monitoring.md) | How to scan GitHub, npm, arXiv, Hugging Face, Discords and X on a fixed cadence without drowning. |
| [`docs/benchmarking.md`](docs/benchmarking.md) | How to compare *your* harness against *Joe's* in a way that survives scrutiny. |
| [`docs/providers.md`](docs/providers.md) | Who is running fixed-model harness benchmarks today, and what is still missing. |
| [`sources.yml`](sources.yml) | Machine-readable watchlist: repos, feeds, queries, accounts. |
| [`templates/HARNESS_CARD.md`](templates/HARNESS_CARD.md) | Disclosure template you should publish alongside any score. |
| [`templates/RESULTS.md`](templates/RESULTS.md) | Results template for a harness-vs-harness comparison. |

## The two questions this repo exists to answer

**1. Where is everyone?**
Nowhere in particular. The ecosystem is split into three layers that do not share a name or a forum: (a) open runtimes such as pi, OpenHands, mini-swe-agent, OpenCode, Goose; (b) the config layer on top of closed CLIs (Claude Code, Codex, Cursor) shared as skills, hooks, plugins and `CLAUDE.md` files across hundreds of personal repos and ~190 plugin marketplaces; (c) curation and research, in awesome-lists, one guide with active GitHub Discussions, and a burst of 2026 arXiv papers. Real iteration happens in issues and PRs, not in a community. [`docs/landscape.md`](docs/landscape.md) maps it; [`docs/monitoring.md`](docs/monitoring.md) tells you how to watch it.

**2. How do I know my harness is better than yours?**
Hold the model, task set, budget and sandbox resources fixed; vary only the harness; run 5 or more trials per task; report pass rate with paired confidence intervals *and* tokens, latency, and failure fingerprint; publish a Harness Card. Public leaderboards do not do this. [`docs/benchmarking.md`](docs/benchmarking.md) gives the protocol and the exact tooling (Harbor, Claw-SWE-Bench, HAL harness).

**Is anyone running that benchmark as a service?**
Partially, and only since mid-2026. Harness-Bench (Peking University / Qiyuan Tech, 6 harnesses x 8 models, 106 tasks) and Claw-SWE-Bench (350 SWE-bench tasks with a harness-neutral adapter) are the first true fixed-model, vary-harness benchmarks with public leaderboards. Both target general-purpose "claw" style runtimes, not the coding CLIs most people actually use. No third party currently runs Claude Code vs Codex vs pi vs OpenCode on the same model at scale. Details and gaps in [`docs/providers.md`](docs/providers.md).

## Status

Snapshot as of 2026-09. The landscape moves monthly; PRs that fix stale links or add sources are welcome. Everything here is opinionated and unaffiliated with any of the projects mentioned.

## License

MIT. See [`LICENSE`](LICENSE).
