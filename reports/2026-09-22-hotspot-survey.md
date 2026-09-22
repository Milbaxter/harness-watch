# Hotspot survey: where the open-source harness ecosystem is being built (2026-09-22)

A wide search for the places, projects and people doing the actual invention and tinkering on agent harnesses, run on 2026-09-22 as input to the docs in this repo. Written as a diff against the repo's own map at the time, so the corrections are explicit. Everything here is a snapshot; star counts and dates are as observed that day.

## Method

- **GitHub**: topic searches (`agent-harness`, `harness-engineering`, `loop-engineering`, `dsh-plugin`) sorted by stars; free-text search for repos created after 2026-08-01 with `harness` in name/description and >150 stars; README reads of the hubs that surfaced.
- **Web**: origin of the term; Discord/community indexes; the Meta-Harness, HarnessTax, AHE and SoL-Pi papers; UHP and Harness Protocol specs; Hermes and OpenClaw scale; Terminal-Bench harness policy; the Claude Code source-map situation; Chinese, Korean and Japanese language searches.
- **Hacker News**: threads on the major 2026 harness posts and papers.
- Deliberately excluded: anything only reachable via login (Discord contents, X timelines). Those are named as venues but not summarised.

## Headline

The repo's landscape doc described a small, fragmented field ("nowhere in particular", registries with tens of stars). That was accurate for Q1 2026. Since 2026-08 the field has:

1. three runtimes above 100k stars in which harness components are swappable plugins,
2. a research sub-field on *automatically* designing harnesses, with its own critique paper,
3. two competing interoperability standards,
4. lab-shipped open harnesses (DeepSeek, Z.ai),
5. regional communities with in-person meetups, and
6. a third-party fixed-model comparison of Claude Code vs Codex CLI vs pi, published six days before this survey, which falsified a core claim in `providers.md`.

## 1. The gravity wells

| Hub | Observed size | Why it is a harness hotspot | Where iteration happens |
|---|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) | 232k stars; created 2026-08-13 | "Everything is a plugin" on [Cordis](https://github.com/cordiverse/cordis). Model adapters, tools, memory, sandbox, scheduler, UI and the agent loop itself are plugins swappable from config. Ships a minimal profile (one shell + one edit tool) explicitly for model benchmarking, a PTC profile, and a "creative" profile that composes new presets from in-memory plugins. `headless`, `sdk`, `acp` profiles; Python SDK. Developer preview. | GitHub Discussions, Discord, `dsh-plugin` topic (15.7k repos in six weeks, heavily spammed), [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) (16.5k), [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook), bilingual awesome-lists |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ~390k stars; GitHub calls it the fastest-growing repo in its history | Personal-assistant gateway where "models and agent harnesses (Claude, Codex, local models) are plugins you can swap". OpenClaw Foundation (501(c)(3)). [ClawHub](https://github.com/openclaw/clawhub): ~69k skills plus whole-agent Claw packages. | Discord, ClawHub, [GitHub Blog maintainer interview](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/) |
| [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent) | ~240k stars | Self-improving harness: creates skills from experience, revises them in use. Skills hub indexes ~90k skills across 11 registries with trust tiers and `.well-known/skills` discovery. | Discord, skills hub, awesome-hermes-agent, hermesatlas.com |
| [earendil-works/pi](https://github.com/earendil-works/pi) | 108k stars | **Renamed from `badlogic/pi-mono`; npm scope now `@earendil-works/*`.** Four-tool minimal harness. Control arm in HarnessTax; substrate for NVIDIA's SoL-Pi; base for gentle-shell, RSI-Harness, SpecPi. | Issues/RFCs, pi.dev packages, Mastodon/X |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | 29.6k | Self-describes as "the batteries-included agent harness". Shows mainstream framework vendors adopted the vocabulary. | GitHub |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 5.9k; created 2026-09-20 | Z.ai's open coding-agent harness, two days old at survey time. Lab-shipped open harnesses are now a pattern (DeepSeek, Z.ai, [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) 35k). | GitHub |

## 2. Research: automated harness evolution is a sub-field

None of this was in the repo's paper list. It is the thread closest to the owner's own `dsh-evoloop` / `excalibur-harness-loop` / `dsh-intelligence-lab` experiments.

- [Meta-Harness](https://arxiv.org/abs/2603.28052) (Stanford IRIS; Yoonho Lee, Chelsea Finn, Omar Khattab et al.; [code](https://github.com/stanford-iris-lab/meta-harness), 1.6k). Outer-loop search over harness code; agentic proposer reads source, scores and full traces of prior candidates via a filesystem. Beats hand-built baselines on Terminal-Bench 2. Spin-offs: SuperagenticAI/metaharness, Harness Forge, Harvey's "Don't Train the Model, Evolve the Harness".
- [Agentic Harness Engineering (AHE)](https://arxiv.org/abs/2604.25850) (Fudan / PKU / Qiji Zhifeng; NexAU). Observability-driven evolution from a bash-only seed: 69.7% to 77.0% pass@1 on TB2 in ten iterations (~32 h), beating Codex CLI (71.9%). Gains from tools, middleware, long-term memory; prompt-only evolution regresses. NexAU-AHE tops the TB 2.0 board with GPT-5.5.
- [SoL-Pi](https://arxiv.org/abs/2609.20519) ([NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi), 2.8k, 2026-09-02). NVIDIA ran auto-research loops, kept four efficiency mechanisms, shipped them as an opt-in pi extension, and offers to benchmark community PRs on a reporting cycle.
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227). Under matched feedback and inference budgets, evolution does not consistently beat simple test-time scaling, and evolved harnesses generalise poorly to held-out tasks. Any evolution claim needs a held-out split and a test-time-scaling control arm.
- [HarnessTax](https://harnesstax.github.io/) (UC Berkeley Sky Lab + Arena.ai; Melissa Pan, Wei-Lin Chiang, Ion Stoica, Matei Zaharia; **2026-09-16**). 21 model x harness pairs across Claude Code, Codex CLI and pi on SWE-bench Lite and TB 2.0. Harness moved success +/-2 to 5 pp but cost up to 5x; pi on the Pareto frontier with four tools; a foreign harness beat the vendor's own in 9 of 12 comparisons. **Falsifies the repo's claim that no third party runs Claude Code vs Codex vs pi on the same model.**
- Adjacent RSI thread: [TokenRhythm/NeoHorse](https://github.com/TokenRhythm/NeoHorse) (same group as Claw-SWE-Bench), [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi), [Q00/ouroboros](https://github.com/Q00/ouroboros) (6k, budgeted evolution across 14 runtimes), [CosmosMind-ai/RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness).

Also relevant to leaderboards: vals.ai re-runs TB 2.1 under a unified Terminus-2 harness; [LHTB](https://huggingface.co/datasets/IntelligenceLab/LHTB-leaderboard) records the harness per row and segregates custom-harness runs out of the ranking; Terminal-Bench 3.0 is referenced in model launch notes.

## 3. Standards and interop (absent from the repo)

- [Unified Harness Protocol (UHP)](https://unifiedharnessprotocol.org/): draft `2026-08-11`, 11 chapters, 75-check conformance suite. Reference implementation [HarnessRouter](https://github.com/HarnessRouter/harnessrouter) (2k, 2026-08-09) drives Claude Code, Codex, Hermes, pi, dsh, OpenCode, Qwen Code, Cline, Gemini CLI, oh-my-pi through one Responses-compatible API. Adapter support there is not native adoption upstream.
- [Harness Protocol](https://harnessprotocol.io/) (`harness.yaml`): portable configuration compiling to eight targets. Different problem from UHP; both use the word.
- [agentskills.io](https://agentskills.io) `SKILL.md`: adopted across Hermes, OpenClaw, pi, Claude Code, Codex. The one portability layer that has effectively won.
- txcript (Skillsync): translates whole sessions between agents; explicitly does not carry system prompts or tools, which is a clean operational definition of "the harness".

## 4. Experiment platforms

- [QoderAI/better-harness](https://github.com/QoderAI/better-harness) (2.3k, 2026-07-21): harnesses as code, controlled experiments, evidence inspection. Closest product to this repo's `RESULTS.md` template.
- [FailproofAI](https://github.com/FailproofAI/failproofai) (5k): observability and policy enforcement across harnesses.
- [loopx](https://github.com/loopx-project/loopx) (5.9k), [LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) (Alibaba AMAP, 1.6k): long-horizon control planes over Codex / Claude Code.
- cliwatch.com: model+harness pairs evaluated against your own CLI.

## 5. Claude Code is readable

`cli.js.map` shipped on npm with `sourcesContent`, exposing ~4,756 TypeScript files. Anatomy projects: [whanyu1212/claude-code-anatomy](https://github.com/whanyu1212/claude-code-anatomy), [HaiDong-Once/claude-code-map](https://github.com/HaiDong-Once/claude-code-map), [fattail4477/claw-decode](https://github.com/fattail4477/claw-decode), the "Claude Code from Source" book, and [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) (515 prompts across 284 versions, updated within minutes of each release). The repo's "closed CLI" framing needed a footnote.

## 6. Curation hubs larger than those listed

- [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) 4.4k; [walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) 4.1k
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) 15.7k; 12 lessons, 6 projects, 14 languages
- [RyanAlberts/best-of-Agent-Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses): 100+ harnesses, rescored weekly, exposed as MCP and `llms.txt`
- [revfactory/harness](https://github.com/revfactory/harness) 9k, [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) 11.3k, [maxritter/pilot-shell](https://github.com/maxritter/pilot-shell) 2k, [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent) 1.3k, [obra/superpowers](https://github.com/obra/superpowers) (the most-installed cross-runtime skill pack)
- Sibling vocabulary: **loop engineering** (Addy Osmani / Boris Cherny lineage) is a 476-repo topic that co-occurs with `harness-engineering` on most serious repos.

## 7. Regional communities

- **China**: the DSH/Cordis ecosystem is the largest single concentration of harness tinkering observed. Volcengine ([OpenViking](https://github.com/volcengine/OpenViking) 38k), Tencent ([WeKnora](https://github.com/Tencent/WeKnora)), Alibaba (QwenPaw 35k, AMAP), MemTensor, dream-num all ship DSH plugins. Key developer: shigma (Cordis). Chinese-first docs.
- **Korea**: Harness Engineering Korea 26Q2 Meetup (~150 attendees, via LangChain Korea); PyTorchKR threads by 9bow; a cluster of high-star Korean authors (revfactory, first-fluke, Q00).
- **Japan**: Zenn hosts the critical writing (e.g. karamage, "why I don't want to say I do harness engineering"); ENSAPIA "Harness-thon" hackathon, Jul 2026.

## 8. Origin of the term

Mitchell Hashimoto named "harness engineering" in "My AI Adoption Journey" (2026-02-05). Ryan Lopopolo's OpenAI field report (2026-02-11; ~1M lines, 0 hand-written, 1,500 automated PRs) popularised it. Can Bölük's "We improved 15 LLMs at coding in one afternoon. Only the harness changed." (2026-02-12) supplied the first widely shared empirical demonstration. Birgitta Böckeler (martinfowler.com), Addy Osmani, Viv Trivedy ("Anatomy of an Agent Harness", harness-as-a-service) and Anthropic's engineering posts (Nov 2025, Mar 2026) systematised it. Dex Horthy (HumanLayer) tracks the pattern; Fareed Khan's Claude Code architecture breakdown is the most-cited diagram.

## 9. High-signal individuals

- **Origin / theory**: Mitchell Hashimoto, Ryan Lopopolo (also maintains a 12-thesis "Harness Engineering" playbook repo), Birgitta Böckeler, Addy Osmani, Viv Trivedy, Dex Horthy, Boris Cherny, Prithvi Rajasekaran.
- **Runtime builders**: Mario Zechner (pi), Can Bölük (oh-my-pi), Peter Steinberger (OpenClaw, pi-skills), Armin Ronacher (pi contributor), Jesse Vincent (superpowers), shigma (Cordis / DSH), Vincent Koc (OpenClaw Foundation), Ian Johnson (tacoda.dev), ruvnet (ruflo, metaharness).
- **Researchers**: Yoonho Lee, Chelsea Finn, Omar Khattab (Meta-Harness); Melissa Pan, Wei-Lin Chiang, Ion Stoica, Matei Zaharia (HarnessTax); the NexAU/AHE group; Kilian Lieret, John Yang (SWE-agent); Mike Merrill, Alex Shaw (Terminal-Bench, Harbor); the LHTB team.

## 10. Where discussion happens, revised

1. GitHub issues/PRs/Discussions on pi, oh-my-pi, deepseek-harness, OpenHands, mini-swe-agent, meta-harness, harness-engineering-guide.
2. X / Mastodon (Zechner posts mainly on Mastodon).
3. Discords: DeepSeek Harness, OpenClaw, Hermes, oh-my-pi, OpenCode, Goose. Slacks: OpenHands, SWE-bench.
4. Hacker News threads on each paper (HarnessTax, Empirical Study, OpenAI post, "Harnesses Explained"); practitioners post disagreeing private numbers there.
5. arXiv cs.SE / cs.AI.
6. Hugging Face datasets and sessions.
7. Regional: DSH docs and Discord; LangChain Korea / PyTorchKR; Zenn.

General "AI agent community" Discords (Latent Space, Anthropic developer Discord, Rasa's Agent Engineering Community, AI Builder Club) discuss harnesses, but at a lower density than the project-specific venues above.

## 11. Signal versus noise

- Topic tagging is gamed. `harness-engineering` is on ragflow (91k), a macOS proxy app and a Xiaohongshu scraper; `dsh-plugin` is on PicGo and reactive-resume. Filter topic searches by description keyword.
- Star counts on 2026 repos are inflated by the OpenClaw/DSH wave. Use commit velocity, issue-close rate, and whether trajectories or ablations are published.
- GitHub redirects renamed repos silently; watch canonical names, not URLs.

## Corrections applied to this repo as a result

| File | Change |
|---|---|
| `sources.yml` | `badlogic/pi-mono` -> `earendil-works/pi`; +31 repos; topics `loop-engineering`, `dsh-plugin`, `cordis`; anchors 2603.28052, 2604.25850, 2607.12227, 2608.25512, 2609.20519; HarnessTax; vals.ai and LHTB boards; new Discords; regional and HN sources; description-ANDed topic searches |
| `docs/providers.md` | Replaced the "no third party runs Claude Code vs Codex vs pi" claim with HarnessTax; added vals.ai, LHTB, SoL-Pi PR benchmarking, better-harness, evolution systems' inner loops |
| `docs/landscape.md` | Layer 0 standards; DSH, OpenClaw, Hermes promoted; evolution paper cluster; Claude Code footnote; regional communities; people; signal-vs-noise |
| `docs/benchmarking.md` | Held-out split and matched-budget test-time-scaling control for evolved harnesses; HarnessTax and Rethinking in the noise-floor table; HarnessRouter, better-harness, dsh-minimal and pi as tooling and control arms |
| `docs/monitoring.md` | Renamed repos; noise filters; HN and regional surfaces; rename detection |
| `README.md` | Both headline answers updated |

## Left unverified

- Exact URLs of two Anthropic engineering posts ("Effective harnesses for long-running agents", "Harness design for long-running application development"); cited by title.
- Discord membership counts and channel activity for any of the named servers.
- Whether HarnessTax will be refreshed; the authors are the Arena team, which makes a live board plausible but not announced.
- NEAR AI's benchmark repo was still not publicly reachable.

## Suggested follow-ups

1. Extend `templates/HARNESS_CARD.md` with proposer model, iteration count and campaign token spend for evolved harnesses.
2. Run the `sources.yml` digest once and diff against this report in a month; the DSH plugin count and the ZCode trajectory are the two numbers most likely to have moved.
3. If gap 1 in `providers.md` is to be filled, HarnessRouter plus Claw-SWE-Bench Lite plus a 50-task TB subset is now the cheapest credible build.
