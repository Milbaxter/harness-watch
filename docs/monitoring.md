# Monitoring: how to stay on top of it

For a focused route into participation, use [Start here: watch, understand, contribute](participate.md). It starts with GEPA and Nous, follows three concrete experiment histories and keeps community memberships, posts and paid experiments explicit. The [September 22 field report](../reports/2026-09-22-community-field-notes.md) adds the dedicated Hermes evolution project and GEPA/DSPy to this repo's original map.

The problem is not lack of information, it is that the signal is spread over six surfaces with different update rates, and since 2026-08 the volume on two of them (GitHub topics, Discord) has gone up by an order of magnitude. The approach below is a fixed cadence per surface plus a small set of saved queries, with explicit noise filters. Budget: about 30 minutes a week once set up.

## Principles

- **Watch queries, not lists.** Awesome-lists lag by weeks. Saved searches on GitHub, npm and arXiv catch new projects the day they get a README.
- **Watch behaviour, not stars.** A repo shipping raw trajectories, ablation results, or a Harness Card is worth more than a 5k-star prompt collection. Star counts on 2026 repos are inflated by the OpenClaw and DeepSeek Harness waves.
- **Filter topics by description.** The `harness-engineering`, `agent-harness` and `dsh-plugin` topics are applied to unrelated projects for discoverability (a RAG engine, an image uploader, a resume builder). Never rank by topic alone.
- **Separate the layers.** Standards (Layer 0) change rarely and matter a lot. Runtime changes (Layer 1) are rare and important. Config-layer churn (Layer 2) is constant and mostly noise. Papers and benchmarks (Layer 3) arrive in bursts.
- **Follow renames.** GitHub redirects renamed repos silently (`badlogic/pi-mono` is now `earendil-works/pi`). Resolve the canonical `full_name` from the API each week and alert on changes.
- **Keep a changelog.** A single `CHANGELOG.md` or notes file where you record what changed and why you care. After three months it becomes your own map.

## Cadence

| Surface | Cadence | Time |
|---|---|---|
| GitHub: releases and pinned issues on core runtimes and standards | Weekly | 10 min |
| GitHub: saved code/repo searches for new projects | Weekly | 5 min |
| npm / PyPI: new packages by keyword | Weekly | 2 min |
| arXiv: saved queries | Weekly | 5 min |
| Hacker News: new paper threads | Weekly | 3 min |
| Hugging Face: datasets and leaderboards | Bi-weekly | 3 min |
| X / Discord | Daily skim, 5 min, or never. Choose. | 5 min |
| Benchmark leaderboards | Monthly | 5 min |
| Awesome-lists (diff since last visit) | Monthly | 5 min |
| Regional sources (CN/KR/JP) | Monthly | 5 min |

## Surface 1: GitHub

### Watch these repos (Releases + Discussions only, not all activity)

Standards: `HarnessRouter/harnessrouter`, `harnessprotocol/harness-protocol`.

Core runtimes: `deepseek-ai/deepseek-harness`, `earendil-works/pi`, `can1357/oh-my-pi`, `openclaw/openclaw`, `NousResearch/hermes-agent`, `zai-org/ZCode`, `SWE-agent/mini-swe-agent`, `OpenHands/OpenHands`, `sst/opencode`, `block/goose`.

Automated harness design: `stanford-iris-lab/meta-harness`, `NVlabs/SoL-Pi`, `NousResearch/hermes-agent-self-evolution`, `gepa-ai/gepa`, `stanfordnlp/dspy`.

Benchmarks and eval infra: `harbor-framework/harbor`, `harbor-framework/terminal-bench-2-1` (and successors), `QoderAI/better-harness`, `Qihoo360/harness-bench`, `opensquilla/claw-swe-bench`, `princeton-pli/hal-harness`, `zli12321/LHTB`.

Curation: `ai-boost/awesome-harness-engineering`, `RyanAlberts/best-of-Agent-Harnesses`, `nexu-io/harness-engineering-guide` (Discussions), `Piebald-AI/claude-code-system-prompts` (commits; one per Claude Code release).

For broad monitoring, use GitHub's per-repo "Custom" watch for Releases and Discussions where available. For participation, also follow a few selected experimental issues and PRs: this is where failures, revisions and acceptance become visible. Avoid all-activity subscriptions. For `deepseek-harness` and `openclaw`, Discussions alone can be high-volume; select relevant categories and threads.

### Saved repository searches

Sort by recently updated, filter `pushed:>YYYY-MM-DD` to the last week. Always AND a description keyword with the topic.

```
topic:harness-engineering harness in:description
topic:agent-harness harness in:description
topic:loop-engineering agent in:description
topic:dsh-plugin harness in:description
topic:pi-package
"agent harness" in:description,readme stars:>20
"harness" "coding agent" in:readme created:>2026-06-01
"harness card" in:readme
"harness evolution" OR "meta-harness" OR "auto-research" harness in:readme
"unified harness protocol" OR uhp harness in:readme
```

A useful weekly view: `harness agent in:name,description created:>{7 days ago} stars:>50`. In 2026-09 that returns a few dozen repos a week; a third are DSH plugins, a handful are new runtimes or research code.

### Saved code searches (find people publishing configs and adapters)

```
path:.claude/skills filename:SKILL.md
filename:AGENTS.md "harness"
path:.pi/ extension:ts
path:.cursor/rules
filename:harness.yaml "$schema" harnessprotocol   # Harness Protocol adopters
filename:cordis.yml dsh                            # DeepSeek Harness plugin compositions
"BaseInstalledAgent" language:Python               # people wrapping their harness for Harbor
"BaseClawAdapter" language:Python                  # people wrapping their harness for Claw-SWE-Bench
```

### Topics pages

Bookmark `github.com/topics/harness-engineering`, `/topics/agent-harness`, `/topics/loop-engineering`, `/topics/dsh-plugin`, `/topics/pi-package`, `/topics/claude-code-plugin`. Sort by recently updated, and read the description column, not the star column.

## Surface 2: Package registries

- npm: search `keywords:pi-package`, `keywords:harness-engineering`, `keywords:agent-harness`, `keywords:loop-engineering`, `keywords:dsh-plugin`, `keywords:claude-code-plugin`. Sort by date.
- npm weekly downloads for `@earendil-works/pi-coding-agent`, `@oh-my-pi/pi-coding-agent`, `@deepseek-ai/dsh`: the best health signal for CLI harnesses. Track the ratio between them month over month.
- PyPI: `harness`, `swe-agent`, `harbor` keyword searches; also watch `mini-swe-agent`, `openhands-sdk`, `harbor` release feeds (`https://pypi.org/rss/project/<name>/releases.xml`).

## Surface 3: arXiv

Saved queries (cs.SE, cs.AI, cs.CL). Use the arXiv advanced search or an RSS-to-email service.

```
abs:"agent harness"
abs:"harness" AND abs:"coding agent"
abs:"scaffold" AND (abs:"SWE-bench" OR abs:"Terminal-Bench")
abs:"harness card"
abs:"fixed model" AND abs:"harness"
abs:"harness evolution" OR abs:"meta-harness" OR abs:"harness optimization"
```

Also follow citations of the anchor papers listed in [`landscape.md`](landscape.md) via Semantic Scholar alerts. New harness papers almost always cite at least one of: HAL (2510.11977), Meta-Harness (2603.28052), AHE (2604.25850), Stop Comparing (2605.23950), Harness-Bench (2605.27922), Claw-SWE-Bench (2606.12344), Rethinking Harness Evolution (2607.12227), Scaffold Effect (2607.22585), SoL-Pi (2609.20519), Empirical Study (2609.20804). HarnessTax is not on arXiv at time of writing; watch harnesstax.github.io directly.

## Surface 4: Hacker News

Every significant harness paper or post gets a thread within a day, and the threads are where practitioners with private benchmarks post disagreeing numbers. Search hn.algolia.com weekly for `harness coding agent`, `harness engineering`, and the title of any paper that appeared in Surface 3. Read the top two comment chains, not the whole thread.

## Surface 5: Hugging Face

- Datasets: `harborframework/*`, `TokenRhythm/Claw-SWE-Bench`, `IntelligenceLab/Long-Horizon-Terminal-Bench`, anything tagged `terminal-bench`, `swe-bench`, `agent-trajectories`.
- Published sessions: `badlogicgames/pi-mono` (pi work sessions). Search datasets for `pi-share-hf` to find others doing the same.
- Leaderboard spaces and datasets: search for `harness`, `terminal-bench`, `swe-bench`, `LHTB`.

## Surface 6: People and chat

X is where most harness design arguments happen first and where papers get announced. Curate a list of 30 to 50 accounts from the "People" section of [`landscape.md`](landscape.md): maintainers of the Layer 1 runtimes, authors of the papers above, the Terminal-Bench / Harbor / SWE-bench teams, `@PiebaldAI` for Claude Code prompt diffs, and Anthropic / OpenAI developer-relations people who post about Claude Code and Codex internals. Read the list, not the timeline. Mario Zechner posts primarily on Mastodon.

Discords worth joining if you are actively building, in order of harness-design signal: DeepSeek Harness (plugin architecture discussions, Chinese and English), oh-my-pi, OpenCode, Goose, Hermes, OpenClaw (very high volume; announcements only). Slacks: OpenHands, SWE-bench. Mute everything except announcements and the dev channel.

## Surface 7: Regional sources

- **China**: the DeepSeek Harness docs site and Discord; `dsh-handbook`; the bilingual DSH awesome-lists. Most DSH plugin READMEs are Chinese-first; machine translation is adequate for triage.
- **Korea**: PyTorchKR discussion board (search 하네스); LangChain Korea meetup announcements (Harness Engineering Korea). Korean-authored repos (`revfactory/harness`, `first-fluke/oh-my-agent`, `Q00/ouroboros`) tend to ship verification-gate patterns first.
- **Japan**: Zenn (search ハーネスエンジニアリング) for critical and methodological writing; occasional "harness-thon" hackathon reports.

## Surface 8: Leaderboards

Check monthly, and look for *new harness rows*, not new model rows:

- [tbench.ai](https://www.tbench.ai/leaderboard) (Terminal-Bench): entries list the agent harness and version; filter one model across harnesses to see spread. Community submissions may be closed at any given time. Watch for the Terminal-Bench 3.0 board.
- vals.ai Terminal-Bench 2.1: unified Terminus-2 harness, vary model. Cross-check against the official board.
- [harnesstax.github.io](https://harnesstax.github.io/): fixed model, vary harness across Claude Code / Codex CLI / pi. One-off as of 2026-09; check for refreshes.
- [harness-bench.ai](https://www.harness-bench.ai/leaderboard.html): fixed protocol, model x harness pair view.
- [claw-swe-bench.github.io](https://claw-swe-bench.github.io/): SWE-bench with the harness as the controlled variable.
- [LHTB](https://zli12321.github.io/LHTB/leaderboard.html): harness column per row; custom-harness runs segregated.
- [HAL](https://hal.cs.princeton.edu): paused for new models as of 2026, still the reference for cost-aware reporting.
- SWE-bench "bash only" leaderboard: fixed harness (mini-swe-agent), vary model.
- NVIDIA SoL-Pi contributor results: published on the repo's reporting cycle.

## Automating it

You can do all of the above by hand in 30 minutes a week. If you want a digest:

1. Put the repos, queries and feeds in [`sources.yml`](../sources.yml) (already seeded).
2. A weekly GitHub Action or cron job pulls: new releases for watched repos (GitHub REST `releases/latest`), the canonical `full_name` for each watched repo (alert on rename), new repos matching each saved search (GitHub search API, `pushed:>` last 7 days, post-filtered on description keywords), new arXiv results (arXiv API query, `submittedDate` window), npm search by keyword and weekly downloads for the pinned packages, HN Algolia search for the week.
3. Diff against last week's snapshot, write a Markdown digest, open it as an issue or send it to yourself.

This repo deliberately ships the list and the method rather than the script; the script is 100 lines of whatever language you already have a scheduler for, and it goes stale slower if you own it.

## What to record when something new shows up

For each new harness or benchmark, write down:

- Layer (standard / runtime / config / eval / research).
- Does it publish trajectories? Costs? A Harness Card or equivalent disclosure?
- Which model(s) and benchmark(s) were the claims made on, and was the model held fixed?
- If it was evolved or auto-tuned: on which split, and against what control?
- Is it wrappable for Harbor / Claw-SWE-Bench / HAL harness / HarnessRouter? If not, you cannot compare it to anything.

If the answers are no, no, unclear, n/a, no, it is a prompt collection. Note it and move on.
