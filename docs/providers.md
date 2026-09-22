# Who is running the harness benchmark?

Short answer: as of 2026-09, two groups run true fixed-model, vary-harness benchmarks with public leaderboards, both since mid-2026, both focused on general-purpose "claw" style runtimes. Nobody runs a continuously updated, third-party, fixed-model comparison of the coding harnesses most people actually use (Claude Code, Codex CLI, Cursor, pi, OpenCode, OpenHands). Several one-off studies have done it on small task sets.

## Fixed-model, vary-harness (what you want)

| Project | Who | What it measures | Status |
|---|---|---|---|
| [Harness-Bench](https://www.harness-bench.ai) ([paper](https://arxiv.org/abs/2605.27922), [code](https://github.com/Qihoo360/harness-bench)) | Peking University / Qiyuan Tech (Qihoo 360) | 106 sandboxed offline tasks in 8 workflow domains; 6 configurable harnesses (OpenClaw, ZeroClaw, Hermes, Moltis, NullClaw, NanoBot) x 8 model backends, full factorial, 5,088 trajectories. Codex reported separately as a model-bound reference. Scores completion, process quality, security, tokens, turns. | Live leaderboard with model / harness / pair views. Not coding-CLI focused. |
| [Claw-SWE-Bench](https://github.com/opensquilla/claw-swe-bench) ([leaderboard](https://claw-swe-bench.github.io/), [paper](https://arxiv.org/abs/2606.12344), [data](https://huggingface.co/datasets/TokenRhythm/Claw-SWE-Bench)) | opensquilla / TokenRhythm | 350 SWE-bench Multilingual + Verified-Mini instances (80-task Lite subset) with a harness-neutral adapter contract: fixed prompt, no network, future-commit stripping, runner-side patch collection, official evaluator. Supported claws: openclaw, hermes, nanobot, zeroclaw, GenericAgent. Adding a harness is one `BaseClawAdapter` file plus a registry entry. | Leaderboard and reference implementation public. Coding-task focused, but the supported harnesses are claw-style runtimes, not Claude Code / Codex / pi. |
| NEAR AI benchmarks | NEAR AI | Reposted Claw-SWE-Bench Lite runs (Hermes 36.2%, OpenClaw 35.0%, IronClaw-Reborn 25.0% on Qwen3.5-122B, 2026-06) with trajectories. | Vendor-run, sporadic; the GitHub repo was not publicly reachable as of 2026-09. |
| [reacher-z/HarnessBench](https://github.com/reacher-z/HarnessBench) | Community (sister of ClawBench) | Everyday online tasks (ordering, booking, job applications); fixes one model, sweeps six harnesses (openclaw, hermes, claw-code, browser-use, stagehand, coze-studio). | Work in progress; leaderboard placeholders as of 2026-09. |
| [nyosegawa/harness-bench](https://github.com/nyosegawa/harness-bench) | Individual | Real-repository debugging tasks with hidden core + regression tests; targets Codex, Claude Code, Cursor Agent, Antigravity CLI. Closest to a coding-CLI comparison. | Framework published; results not yet. |

## One-off controlled studies (not services)

| Study | Scope |
|---|---|
| [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) | 3 models x 3 harnesses (minimal / improved / full), 100 SWE-bench Verified tasks, 2 runs each. Harness variance 7.8x model variance. |
| [The Scaffold Effect](https://arxiv.org/abs/2607.22585) ([data](https://github.com/namanvats/scaffold-effects)) | Qwen 3.6 Plus and MiniMax M2.5 across Goose, OpenCode, OpenHands-SDK on 50 Terminal-Bench Pro tasks. Configs, logs and scripts released. |
| [An Empirical Study of Harness Design](https://arxiv.org/abs/2609.20804) | Component-level ablations within one harness across 4 models, SWE-bench Verified and Terminal-Bench 2.1, 176 settings. |
| [HAL](https://hal.cs.princeton.edu) (ICLR 2026) | 21,730 rollouts, 9 models x 9 benchmarks; compares task-specific vs generalist scaffolds and reports cost. Leaderboard paused for new models. |

## Model-focused leaderboards that disclose the harness (useful, but not the same thing)

| Leaderboard | Harness handling |
|---|---|
| [Terminal-Bench](https://www.tbench.ai/leaderboard) (Laude Institute / Stanford, Harbor) | Every entry names its harness and publishes trajectories; the same model often appears under several harnesses, so you can read off same-model spread (e.g. GPT-5.2: 62.9% under Codex CLI vs 54.0% under the neutral Terminus 2). But entries are chosen to maximise each model's score, and community submissions are periodically closed. |
| SWE-bench "bash only" (mini-swe-agent) | Harness fixed, model varies. The inverse experiment. Cleanest model comparison available. |
| SWE-bench Verified / Pro, main boards | Harness disclosed inconsistently; vendor-run harnesses. Treat as model-harness systems. |
| Anthropic / OpenAI / Google model cards | Own harness, own settings. Not comparable across vendors. |

## What is missing

1. **A fixed-model board for coding CLIs.** Claude Code, Codex CLI, Cursor Agent, pi / oh-my-pi, OpenCode, OpenHands, Goose, mini-swe-agent, all on the same two or three models, same budget, same sandbox, k=5, updated monthly. Harbor plus Claw-SWE-Bench already provide the runner and the adapter contract. The blockers are money (roughly 8 harnesses x 3 models x 100 tasks x 5 trials, on the order of tens of thousands of dollars per refresh) and the fact that the closed CLIs do not expose every setting.
2. **Config-layer evaluation.** Nobody measures whether a given `CLAUDE.md`, skill pack or hook set helps. The Harness Card and the protocol in [`benchmarking.md`](benchmarking.md) apply directly; the task is to treat a config bundle as a harness variant and run the A/B.
3. **Standard disclosure.** The Harness Card ([2605.23950](https://arxiv.org/abs/2605.23950)) is the only proposal. Vendors have no incentive to adopt it. Independent evaluators can demand it.

If you want to fill gap 1, the cheapest credible version is: pick one open model (removes vendor drift), Claw-SWE-Bench Lite (80 tasks) plus a 50-task Terminal-Bench subset, k=5, four or five harnesses, publish trajectories and Harness Cards, repeat quarterly. That is a few thousand dollars per refresh and would be the most-cited harness resource on the internet within a month.
