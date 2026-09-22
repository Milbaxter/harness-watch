# Who is running the harness benchmark?

Short answer, as of 2026-09: yes, but not continuously. The first third-party, fixed-model comparison of the coding CLIs people actually use (Claude Code, Codex CLI, pi) was published on 2026-09-16 (HarnessTax). Two groups run fixed-model, vary-harness leaderboards for general-purpose "claw" runtimes. One vendor re-runs Terminal-Bench under a unified harness. NVIDIA benchmarks pi extensions on request. Nobody yet runs a continuously refreshed board across all the coding harnesses (Claude Code, Codex CLI, Cursor, pi, OpenCode, OpenHands, dsh, ZCode) on the same models.

## Fixed-model, vary-harness (what you want)

| Project | Who | What it measures | Status |
|---|---|---|---|
| [HarnessTax](https://harnesstax.github.io/) | UC Berkeley Sky Lab + Arena.ai (Melissa Z. Pan, Shuo Yang, Negar Arabzadeh, Wei-Lin Chiang, Ion Stoica, Matei Zaharia) | 21 model x harness pairs: 7 models (Claude Fable 5, Opus 4.8, Sonnet 4.6, Haiku 4.5, GPT-5.6 Sol, GPT-5.6 Luna, Kimi K3) across Claude Code, Codex CLI and pi, on 30-task random subsets of SWE-bench Lite and Terminal-Bench 2.0, 3 trials each, 100-turn cap, default harness settings at high reasoning, official evaluators, bootstrap CIs. | Published 2026-09-16 with interactive figures and the full grid. **Result:** harness shifts success only about +/-2 pp (SWE-bench Lite) and +/-5 pp (TB 2.0), but per-task cost up to 5x. pi sits on the Pareto frontier with four tools and a system prompt >10x smaller than Claude Code's. In 9 of 12 vendor comparisons a foreign harness beat the vendor's own. One-off so far; the authors are the Arena team, so a live board is plausible. |
| [Harness-Bench](https://www.harness-bench.ai) ([paper](https://arxiv.org/abs/2605.27922), [code](https://github.com/Qihoo360/harness-bench)) | Peking University / Qiyuan Tech (Qihoo 360) | 106 sandboxed offline tasks in 8 workflow domains; 6 configurable harnesses (OpenClaw, ZeroClaw, Hermes, Moltis, NullClaw, NanoBot) x 8 model backends, full factorial, 5,088 trajectories. Scores completion, process quality, security, tokens, turns. | Live leaderboard with model / harness / pair views. Not coding-CLI focused. |
| [Claw-SWE-Bench](https://github.com/TokenRhythm/claw-swe-bench) ([leaderboard](https://claw-swe-bench.github.io/), [paper](https://arxiv.org/abs/2606.12344), [data](https://huggingface.co/datasets/TokenRhythm/Claw-SWE-Bench)) | TokenRhythm (repo formerly under `opensquilla`) | 350 SWE-bench Multilingual + Verified-Mini instances (80-task Lite subset) with a harness-neutral adapter contract. Supported claws: openclaw, hermes, nanobot, zeroclaw, GenericAgent. Adding a harness is one `BaseClawAdapter` file plus a registry entry. | Leaderboard and reference implementation public. Coding-task focused, but the supported harnesses are claw-style runtimes. |
| NVIDIA [SoL-Pi](https://github.com/NVlabs/SoL-Pi) contributor benchmarking | NVIDIA | Accepts pi-compatible extension PRs that improve token efficiency, benchmarks them, and "publishes results on a regular reporting cycle". | Announced 2026-09 with the repo. Scope is pi extensions only, but it is a lab offering to run your harness change through their eval. |
| NEAR AI benchmarks | NEAR AI | Reposted Claw-SWE-Bench Lite runs (2026-06) with trajectories. | Vendor-run, sporadic. |
| [reacher-z/HarnessBench](https://github.com/reacher-z/HarnessBench) | Community | Everyday online tasks; fixes one model, sweeps six harnesses. | Work in progress as of 2026-09. |
| [nyosegawa/harness-bench](https://github.com/nyosegawa/harness-bench) | Individual | Real-repository debugging tasks; targets Codex, Claude Code, Cursor Agent, Antigravity CLI. | Framework published; results not yet. |

## Automated harness-evolution systems (they run the benchmark as an inner loop)

These are not services, but each one is a working fixed-model, vary-harness pipeline with public code, and their papers contain the largest same-model harness grids available.

| System | Grid | Notes |
|---|---|---|
| [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness) (Stanford IRIS) | Dozens of generated harness candidates per run, fixed model, Terminal-Bench 2 and text-classification reference experiments. | Proposer is Claude Code by default; wrapper is swappable. Optimised TB2 harness released as a separate artifact repo. |
| [AHE / NexAU](https://arxiv.org/abs/2604.25850) (Fudan / PKU / Qiji Zhifeng) | Bash-only seed evolved over 10 iterations on all 89 TB2 tasks, k=2, ~32 h; compared against OpenCode, Terminus-2, Codex, ACE, TF-GRPO on the same model. | Cross-model transfer table on five alternate bases is the closest thing to a published model x harness matrix for a *coding* harness. E2B sandboxes; configs released. |
| [SoL-Pi](https://github.com/NVlabs/SoL-Pi) (NVIDIA) | Auto-research loops over pi; four surviving mechanisms shipped. | Paper: arXiv 2609.20519. |
| [Rethinking the Evaluation of Harness Evolution](https://arxiv.org/abs/2607.12227) | Re-evaluates the above class on TB 2.1 with GPT-5.4 and Opus 4.6 against matched-budget test-time scaling and held-out tasks. | Finds no consistent advantage and limited generalisation. Read before trusting any evolution result, including your own. |

## One-off controlled studies (not services)

| Study | Scope |
|---|---|
| [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) | 3 models x 3 harnesses, 100 SWE-bench Verified tasks, 2 runs each. Harness variance 7.8x model variance. |
| [The Scaffold Effect](https://arxiv.org/abs/2607.22585) ([data](https://github.com/namanvats/scaffold-effects)) | Qwen 3.6 Plus and MiniMax M2.5 across Goose, OpenCode, OpenHands-SDK on 50 Terminal-Bench Pro tasks. |
| [An Empirical Study of Harness Design](https://arxiv.org/abs/2609.20804) | Component-level ablations within one harness across 4 models, SWE-bench Verified and Terminal-Bench 2.1, 176 settings. |
| [HAL](https://hal.cs.princeton.edu) (ICLR 2026) | 21,730 rollouts, 9 models x 9 benchmarks; task-specific vs generalist scaffolds; cost reported. Leaderboard paused for new models. |
| Can Bölük, "We improved 15 LLMs at coding in one afternoon. Only the harness changed." (blog.can.ac, 2026-02-12) | 15 models, one harness change (oh-my-pi). Not peer reviewed, but the post that made the field visible. |

## Model-focused leaderboards that disclose the harness (useful, but not the same thing)

| Leaderboard | Harness handling |
|---|---|
| [Terminal-Bench](https://www.tbench.ai/leaderboard) (Laude Institute / Stanford, Harbor) | Every entry names its harness and version (e.g. Claude Code 2.1.123, Codex 0.125.0, Terminus 2) and publishes trajectories; the same model appears under several harnesses so you can read off same-model spread. Entries are chosen to maximise each model's score; community submissions for 2.1 are closed at time of writing; Terminal-Bench 3.0 is being referenced in model launch notes. |
| vals.ai Terminal-Bench 2.1 | Re-runs models under a **unified Terminus-2 harness**, pass@1. Fixed harness, vary model. Use as the cross-check against the official board. |
| Artificial Analysis | Direct model tests with labelled effort tiers; its own harness. Third number that disagrees with the two above for structural reasons, not error. |
| [LHTB](https://huggingface.co/datasets/IntelligenceLab/LHTB-leaderboard) (Long-Horizon Terminal-Bench) | Records the harness per row; runs on a non-Terminus harness go under `1.0-custom-harness/` and are excluded from the ranking. The disclosure pattern other boards should copy. |
| SWE-bench "bash only" (mini-swe-agent) | Harness fixed, model varies. Cleanest model comparison available. |
| SWE-bench Verified / Pro, main boards | Harness disclosed inconsistently; vendor-run harnesses. Treat as model-harness systems. |
| Anthropic / OpenAI / Google model cards | Own harness, own settings. Not comparable across vendors. |

## Tooling that makes running it yourself cheaper than it was

| Tool | Why it matters here |
|---|---|
| [HarnessRouter](https://github.com/HarnessRouter/harnessrouter) / UHP | One API in front of Claude Code, Codex, Hermes, pi, dsh, OpenCode, Qwen Code, Cline, Gemini CLI, oh-my-pi. Removes most of the per-harness glue that made the "8 harnesses x 3 models" board expensive to build. |
| [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | Harnesses as code, controlled experiments, evidence inspection, outcome comparison. |
| DeepSeek Harness `sdk-minimal` / minimal profile | A lab-shipped one-shell-tool-one-edit-tool baseline, explicitly for benchmarking. A second control arm alongside mini-swe-agent. |
| [Harbor](https://www.harborframework.com), [Claw-SWE-Bench](https://github.com/TokenRhythm/claw-swe-bench), [HAL harness](https://github.com/princeton-pli/hal-harness) (archived 2026-07) | Runners; see [`benchmarking.md`](benchmarking.md). |

## What is still missing

1. **A continuously refreshed fixed-model board for coding harnesses.** HarnessTax proved it can be done on 30 tasks x 3 trials for 21 pairs. Nobody has committed to refreshing it monthly or extending it to Cursor, OpenCode, OpenHands, dsh, ZCode, oh-my-pi and mini-swe-agent. UHP/HarnessRouter removes the integration cost; the remaining blockers are money and the closed CLIs' hidden settings.
2. **Config-layer evaluation.** Nobody measures whether a given `CLAUDE.md`, skill pack or hook set helps. The Harness Card and the protocol in [`benchmarking.md`](benchmarking.md) apply directly; treat a config bundle as a harness variant and run the A/B.
3. **Standard disclosure.** The Harness Card ([2605.23950](https://arxiv.org/abs/2605.23950)) is still the only proposal. LHTB's custom-harness segregation and Terminal-Bench's per-entry version pins are partial adoptions. Vendors have no incentive; independent evaluators can demand it.
4. **Honest evaluation of evolved harnesses.** Per [2607.12227](https://arxiv.org/abs/2607.12227), evolution results need a held-out task split and a matched-budget test-time-scaling control. None of the evolution papers' public leaderboards enforce this yet.

If you want to fill gap 1, the cheapest credible version is: pick one open model (removes vendor drift), Claw-SWE-Bench Lite (80 tasks) plus a 50-task Terminal-Bench subset, k=5, six or seven harnesses behind HarnessRouter, publish trajectories and Harness Cards, repeat quarterly. That is a few thousand dollars per refresh and, given that HarnessTax got picked up by mainstream tech press within a day, would be widely cited.
