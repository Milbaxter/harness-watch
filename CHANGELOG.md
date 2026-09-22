# Changelog

What changed in the map, and why it matters. Newest first. Dated snapshots of the research behind each entry live in [`reports/`](reports/).

## 2026-09-22 (b): corrections, watchlist hygiene, evolved-harness disclosure

- **Canonical names.** `sst/opencode` is now `anomalyco/opencode`; `block/goose` is now `aaif-goose/goose`; `opensquilla/claw-swe-bench` is now `TokenRhythm/claw-swe-bench`. All three redirected silently, so the previous refresh missed them. Added `scripts/check_sources.py` and a weekly GitHub Action so this class of error fails CI instead of surviving in the watchlist; the first run of that script is what found the third rename.
- **`princeton-pli/hal-harness` was archived on 2026-07-01.** Removed from the watchlist; `benchmarking.md` now says to copy its cost accounting rather than build on it. `sadsfae/awesome-claude-code` has not been pushed to since March; noted, kept.
- **`nexu-io/harness-engineering-guide` demoted** from "active Discussions, closest thing to a forum" to "reference". No pushes since 2026-04-19.
- **Codex CLI is open source** (`openai/codex`, Rust). Layer 2 wording corrected; the repo added to the watchlist as the one vendor coding harness you can read end to end.
- **Added** to Layer 1 / control planes: Prime Agent + verifiers, oh-my-openagent (with its source-available licence flagged), OpenHands SDK, Gas City / Beads. To Layer 2: gsd-core, and a "personal harnesses on open runtimes" group (agent-stuff, pi-autoresearch, pi2dsh, pi-tool-duration). To research: GEPA, airbnb/agent-harness-optimizer, Adaptive Auto-Harness. To standards: the ACP and agentskills spec repos.
- **Monitoring**: new "saved pull-request searches" block. Releases show what shipped; the design question is in the PR body weeks earlier.
- **Templates**: Harness Card gains a *Provenance* section (seed, proposer model, dev/held-out splits, campaign tokens, matched-budget control); RESULTS.md gains an evolved-harness control table. These are the fields [2607.12227](https://arxiv.org/abs/2607.12227) says every evolution claim needs.
- Dropped two near-empty Claude Code anatomy repos (0 and 5 stars, last pushed April) that were carrying a claim Piebald's prompt tracker supports on its own.

## 2026-09-22 (a): landscape refresh for the post-August ecosystem

Merged from [#2](https://github.com/Milbaxter/harness-watch/pull/2). Survey in [`reports/2026-09-22-hotspot-survey.md`](reports/2026-09-22-hotspot-survey.md).

- **HarnessTax** (UC Berkeley Sky Lab + Arena.ai, 2026-09-16) falsified the claim that no third party runs Claude Code vs Codex CLI vs pi on the same model. 21 pairs; harness moves success +/-2 to 5 pp, cost up to 5x; pi on the Pareto frontier; vendor harness lost 9 of 12 comparisons.
- **Three runtimes above 100k stars** where harness components are plugins: DeepSeek Harness (`dsh`, on Cordis), OpenClaw, Hermes Agent. Promoted from one table cell to their own section.
- **Layer 0 added**: UHP / HarnessRouter (drive a harness), Harness Protocol (`harness.yaml`), agentskills.io `SKILL.md`, ACP, txcript.
- **Automated harness design** is a sub-field: Meta-Harness, AHE / NexAU, SoL-Pi, and the critique paper *Rethinking the Evaluation of Harness Evolution*. `benchmarking.md` gains rules for evolved harnesses (held-out split, matched-budget test-time-scaling control).
- `badlogic/pi-mono` is `earendil-works/pi`; npm scope `@earendil-works/*`.
- Regional communities (CN / KR / JP), a people list, signal-vs-noise notes on gamed topic tags and inflated stars.
- `sources.yml`: 30 -> 61 repos, new `standards`, `non_arxiv_studies`, `npm_packages`, `hacker_news_searches`, `regional`, `x_accounts_seed` sections.

## 2026-09 (initial)

README, `landscape.md`, `monitoring.md`, `benchmarking.md`, `providers.md`, `sources.yml`, Harness Card and RESULTS templates. Q1-2026-shaped map: pi, OpenHands, mini-swe-agent, OpenCode, Goose as runtimes; Harness-Bench and Claw-SWE-Bench as the only fixed-model boards.
