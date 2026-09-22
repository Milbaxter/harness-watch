# The landscape

The word "harness" is used for four different things. The people working on each layer mostly do not read each other. Knowing which layer you care about tells you where to look.

```
┌──────────────────────────────────────────────────────────────┐
│ Layer 3: Curation & research                                 │
│   awesome-lists, guides, arXiv papers, benchmark projects,   │
│   automated harness-evolution systems                        │
├──────────────────────────────────────────────────────────────┤
│ Layer 2: Config layer on top of a runtime                    │
│   AGENTS.md / CLAUDE.md, skills, hooks, plugins, MCP configs │
│   (this is what most people mean by "my harness")            │
├──────────────────────────────────────────────────────────────┤
│ Layer 1: Runtimes (the agent loop itself)                    │
│   pi, DeepSeek Harness, OpenClaw, Hermes, OpenHands,         │
│   mini-swe-agent, OpenCode, Goose, ZCode, ...                │
├──────────────────────────────────────────────────────────────┤
│ Layer 0: Interop standards                                   │
│   UHP (drive a harness), Harness Protocol (configure one),   │
│   agentskills.io SKILL.md, ACP, MCP                          │
└──────────────────────────────────────────────────────────────┘
```

A note on scale. In Q1 2026 this ecosystem was a handful of repos with tens of stars. Since 2026-08 it has three runtimes above 100k stars, lab-shipped open harnesses, two competing interop standards, and a research sub-field on *automated* harness design. The sections below reflect the 2026-09 state; the numbers will be wrong within a month, the shape less so.

## Layer 0: Interop standards

These did not exist when most of the awesome-lists were written. They matter because they are the layer that lets you run the same task against N harnesses programmatically, which is the whole game in [`benchmarking.md`](benchmarking.md).

| Standard | What it standardises | Status |
|---|---|---|
| [Unified Harness Protocol (UHP)](https://unifiedharnessprotocol.org/) | *Driving* a complete harness over HTTP: discovery, tasks, streaming, sessions, files, artifacts, cancellation, errors. Not a model API, not MCP. | Draft `2026-08-11`, 11 chapters, 75-check conformance suite. Reference implementation [HarnessRouter](https://github.com/HarnessRouter/harnessrouter) (Apache-2.0, Aug 2026) exposes a Responses-compatible API over Claude Code, Codex, Hermes, pi, dsh, OpenCode, Qwen Code, Cline, Gemini CLI, oh-my-pi. Adapter support there is not native adoption by those projects. |
| [Harness Protocol](https://harnessprotocol.io/) | *Configuring* a harness: a vendor-neutral `harness.yaml` for instructions, skills, plugins, MCP servers, env, permissions, governance. Compiles to Claude Code, Cursor, Copilot, Codex, OpenCode, Windsurf, Gemini CLI, Junie. | Schema v1 current; exchange and registry layers planned. [harness-kit](https://github.com/harnessprotocol/harness-kit) is the CLI. |
| [agentskills.io](https://agentskills.io) `SKILL.md` | The skill file format. Adopted by Claude Code, Codex, Hermes, OpenClaw, pi, OpenCode and most Layer 2 registries. | De facto won. This is the portable unit for Layer 2 assets. |
| ACP (Agent Client Protocol) | Editor-to-agent protocol (Zed lineage). DeepSeek Harness ships an `acp` profile. | Adopted by several runtimes; relevant if you want to swap harnesses under one editor. |
| txcript (Skillsync) | Translates whole *sessions* (history, tool calls, results) between Claude Code, Codex, OpenCode, Cursor and others. Explicitly does not carry system prompts or tools, which is a useful operational definition of "the harness". | Open-source Rust core. |

## Layer 1: Open runtimes

These are the projects where the loop, tools, context policy and stop conditions are themselves open and being changed by individuals.

### The three gravity wells

| Project | Why it matters | Where the iteration happens |
|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) | Released 2026-08-13, >200k stars in six weeks. "Everything is a plugin": model adapters, tools, memory, sandbox, scheduler, UI *and the agent loop itself* are [Cordis](https://github.com/cordiverse/cordis) plugins (shigma's plugin framework; design paper arXiv 2608.25512), swappable from config without touching source. Ships a **minimal profile** (one shell tool + one file-edit tool, explicitly for model benchmarking), a PTC profile (model writes a TypeScript program to compose tool calls) and a **creative profile** that inspects the runtime and composes new presets from in-memory plugins. Also `headless`, `sdk`, `acp` profiles and a Python SDK. Developer preview; breaking changes promised. | [GitHub Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions), [Discord](https://discord.gg/Ycq5dCaS4), the `dsh-plugin` topic (>15k repos, heavily spammed), [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin), [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) (includes same-model multi-agent comparisons), [Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) (bilingual). Chinese-first. |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) (Peter Steinberger, OpenClaw Foundation) | ~390k stars; GitHub calls it the fastest-growing repository in its history. A personal-assistant gateway in which "models and agent harnesses (Claude, Codex, local models) are plugins you can swap without changing anything else". Not coding-first, but it is where the largest number of people are swapping harnesses under a fixed workload. [ClawHub](https://github.com/openclaw/clawhub) hosts ~69k skills plus code plugins and whole-agent "Claw packages". Now stewarded by a 501(c)(3). | Discord, ClawHub, GitHub. See the [GitHub Blog maintainer interview](https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/) for governance and security lessons. |
| [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent) | ~240k stars. Self-improving harness: creates skills from experience, revises them during use, searches its own past sessions. Skills hub indexes ~90k skills across 11 registries (ClawHub, skills.sh, LobeHub, browse.sh, vendor registries) with trust tiers and `.well-known/skills` discovery. | Discord, skills hub, [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent), hermesatlas.com |

### Coding-first runtimes

| Project | Why it matters | Where the iteration happens |
|---|---|---|
| [earendil-works/pi](https://github.com/earendil-works/pi) (Mario Zechner; formerly `badlogic/pi-mono`, npm scope now `@earendil-works/*`) | ~108k stars. Deliberately minimal (four tools: read, write, edit, bash), self-extensible, provider-agnostic. The control arm in HarnessTax (on the cost/accuracy Pareto frontier with a system prompt >10x smaller than Claude Code's), the substrate for NVIDIA's SoL-Pi, and the base for [gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness), [SpecPi](https://tannermidd.github.io/SpecPi/research/) and many personal harnesses. Author publishes raw work sessions to Hugging Face. | GitHub issues/PRs and in-repo RFCs, [pi.dev packages](https://pi.dev/packages?type=extension), Mastodon/X |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) (Can Bölük) | Fork of pi, coding-first, moves faster: LSP, subagents, pluggable memory, browser relay. Inherits `.claude`, `.cursor`, `.codex` configs on first run. Bölük's Feb 2026 post "We improved 15 LLMs at coding in one afternoon. Only the harness changed." is one of the founding artefacts of the field. | GitHub, Discord (linked from README) |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | Z.ai's open coding-agent harness, released 2026-09-20. Lab-shipped open harnesses are now a pattern (DeepSeek, Z.ai, [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)). Watch for GLM-specific harness design decisions. | GitHub |
| [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) / [SWE-agent](https://github.com/SWE-agent/SWE-agent) (Princeton / Stanford) | ~100-line bash-only baseline scoring >74% on SWE-bench Verified. The harness everyone ablates against; also the harness behind the SWE-bench "bash only" leaderboard. | GitHub, papers, SWE-bench Slack |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Production-grade, Docker-sandboxed, best-documented internal design (context condensation, prompt-injection mitigation, `openhands-sdk`). | GitHub, Slack, docs |
| [sst/opencode](https://github.com/sst/opencode) | Popular TUI agent, provider-agnostic, large plugin surface. | GitHub, Discord |
| [block/goose](https://github.com/block/goose) (Block) | Extensible desktop/CLI agent with MCP-first tooling. | GitHub, Discord |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | ~30k stars, tagline "the batteries-included agent harness". Included because it shows framework vendors have adopted the vocabulary; it is a library, not a CLI. | GitHub |
| [context-labs/whip](https://github.com/context-labs/whip) | Single-binary Go harness built for open-weight models. Representative of a small wave of Go/Rust rewrites ([thClaws](https://github.com/thClaws/thClaws), [goclaw](https://github.com/nextlevelbuilder/goclaw)). | GitHub |

### Control planes and meta-harnesses (run *other* harnesses)

| Project | What it does |
|---|---|
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | Long-horizon control plane across Codex, Claude Code and others. |
| [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) (Alibaba AMAP) | Fresh-context execution, durable verified state, independent auditing over Claude Code / Codex / OpenClaw. |
| [Q00/ouroboros](https://github.com/Q00/ouroboros) | Budgeted evolution loop with staged evaluation across 14 runtimes. |
| [ruvnet/metaharness](https://github.com/ruvnet/metaharness), [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Scaffold your own branded harness; swarm orchestration. High star counts, treat claims with the usual care. |
| [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | Observability and policy enforcement across harnesses. |

## Layer 2: Config layer on top of runtimes

Claude Code, Codex CLI and Cursor are closed products whose behaviour is heavily shaped by user-supplied files. This layer is enormous and shallow: thousands of repos, almost no shared evaluation.

**Footnote on "closed".** Claude Code's npm package shipped a `cli.js.map` with `sourcesContent`, exposing roughly 4,700 TypeScript files. Independent anatomy projects now document the full harness: [whanyu1212/claude-code-anatomy](https://github.com/whanyu1212/claude-code-anatomy), [HaiDong-Once/claude-code-map](https://github.com/HaiDong-Once/claude-code-map), [fattail4477/claw-decode](https://github.com/fattail4477/claw-decode), plus the long-running [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) (515 prompts tracked across 284 versions, updated within minutes of each release). Codex CLI is open source. Cursor remains closed. So the "closed CLI" harnesses are readable even if not modifiable, and the anatomy repos are now primary sources for harness design patterns.

| Hub | What it is |
|---|---|
| [sadsfae/awesome-claude-code](https://github.com/sadsfae/awesome-claude-code) | De facto index of skills, hooks, slash commands, orchestrators, `CLAUDE.md` examples. |
| [Chat2AnyLLM/awesome-claude-plugins](https://github.com/Chat2AnyLLM/awesome-claude-plugins) | Metadata catalog of Claude Code plugin marketplaces. |
| [sergeykrin9/awesome-claude-code-workflows](https://github.com/sergeykrin9/awesome-claude-code-workflows) | Methodologies, memory systems, `CLAUDE.md`/`HANDOFF.md` templates. |
| [obra/superpowers](https://github.com/obra/superpowers) (Jesse Vincent) | The most-installed skill pack across Claude Code, Hermes and OpenClaw. Worth reading as the canonical example of a Layer 2 harness that travels. |
| [BioInfo/claudelicious](https://github.com/BioInfo/claudelicious), [maxritter/pilot-shell](https://github.com/maxritter/pilot-shell), [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent), [revfactory/harness](https://github.com/revfactory/harness) | Complete wired-together setups with reasoning: spec-driven, TDD gates, stop-hook verification, independent judges. Models for how to publish a harness rather than a snippet. |
| [harnessprotocol/harness-kit](https://github.com/harnessprotocol/harness-kit), [hgflima/harness-lab](https://github.com/hgflima/harness-lab), [madebywild/agent-harness](https://github.com/madebywild/agent-harness), [eooo-io/orkestr](https://github.com/eooo-io/orkestr) | Portable registries / package managers for harness assets across CLIs. harness-kit has the spec behind it; nobody has won this yet. |
| Cursor rules / Codex `AGENTS.md` collections | Same pattern, smaller. Search GitHub for `path:.cursor/rules` or `filename:AGENTS.md`. |

**Sibling vocabulary: "loop engineering".** Popularised via Addy Osmani and Boris Cherny; [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) (~11k stars) is the hub. The `loop-engineering` GitHub topic co-occurs with `harness-engineering` on most serious repos. Watch both.

## Layer 3: Curation and research

### Curation

| Resource | Notes |
|---|---|
| [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | Largest awesome-list (~4.4k stars): tools, patterns, evals, memory, permissions, observability. |
| [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | ~15k stars. 12 lessons, 6 projects, 14 languages. The on-ramp most newcomers use. Sister list: [walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering). |
| [RyanAlberts/best-of-Agent-Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) | 100+ harnesses, rescored weekly, exposed as MCP server and `llms.txt`. The only *ranked* list. |
| [Turi-Labs/awesome-harness](https://github.com/Turi-Labs/awesome-harness), [Lijunjie2/awesome-agent-harness](https://github.com/Lijunjie2/awesome-agent-harness), [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | Overlapping lists; Lijunjie2 is EN/ZH. |
| [nexu-io/harness-engineering-guide](https://github.com/nexu-io/harness-engineering-guide) ([harness-guide.com](https://harness-guide.com)) | Structured guide with active GitHub Discussions. |
| Ryan Lopopolo's "Harness Engineering" repo | 12 theses, 3 adoption procedures and a source library, packaged as an `AGENTS.md`-routed context bundle. The author of the OpenAI field report, in long form. |
| [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi) | Research map of recursive self-improvement including harnesses; the adjacent field. |
| Anthropic engineering blog | [Effective harnesses for long-running agents](https://www.anthropic.com/engineering) (Nov 2025), [Harness design for long-running application development](https://www.anthropic.com/engineering) (Mar 2026), [Quantifying infrastructure noise](https://www.anthropic.com/engineering/infrastructure-noise). Primary sources. |
| [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/) (Ryan Lopopolo, 2026-02-11) | The field report that gave the discipline its name in public. ~1M lines, 0 hand-written, 1,500 automated PRs. |
| [thedeepfeed.ai: Measuring the agent harness](https://www.thedeepfeed.ai/posts/2026-06-22-how-much-is-the-harness-worth-measuring-agent-scaffolds/) | Best single synthesis of the 2026 harness-effect papers up to June. |

### Key 2026 papers: measuring the harness effect

| Paper | Finding |
|---|---|
| [HarnessTax](https://harnesstax.github.io/) (UC Berkeley Sky Lab + Arena.ai, 2026-09-16) | 21 model x harness pairs (7 models across Claude Code, Codex CLI, pi) on SWE-bench Lite and Terminal-Bench 2.0. Harness moves success only +/-2 pp (SWE) / +/-5 pp (TB) but cost up to **5x**. pi is on the Pareto frontier with four tools. In 9 of 12 vendor comparisons a *foreign* harness beat the vendor's own. **The first third-party fixed-model comparison of the coding CLIs people actually use.** |
| [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) | 3 models x 3 harnesses on SWE-bench Verified: harness variance 7.8x model variance; 6 of 9 model rankings reverse. Proposes the "Harness Card". |
| [The Scaffold Effect](https://arxiv.org/abs/2607.22585) | Goose / OpenCode / OpenHands-SDK on Terminal-Bench Pro: pass rates within 2-8 pp, tokens per solved task differ up to 40x, failure fingerprints are harness-specific. |
| [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804) | Component ablations (planning, action space, context management) across 176 settings. Effects depend on model strength and context budget. |
| [Harness-Bench](https://arxiv.org/abs/2605.27922) | 6 harnesses x 8 models x 106 tasks, full factorial. 23.8-point spread between best and worst harness. |
| [Claw-SWE-Bench](https://arxiv.org/abs/2606.12344) | Same model, adapter design alone moves SWE-bench Pass@1 from 19.1% to 73.4%. |
| [Holistic Agent Leaderboard (HAL)](https://arxiv.org/abs/2510.11977), ICLR 2026 | 21,730 rollouts; task-specific scaffolds beat generalist ones in 20/24 comparisons; cost must be reported. |
| [Terminal-Bench](https://arxiv.org/abs/2601.11868) paper | Each leaderboard entry used "the agent scaffold chosen to maximize performance". |

### Key 2026 papers: *automating* harness design

This is now a distinct sub-field and the most active research hotspot. All of these hold the model fixed and search over the harness.

| Paper / system | Finding |
|---|---|
| [Meta-Harness](https://arxiv.org/abs/2603.28052) (Stanford IRIS: Yoonho Lee, Chelsea Finn, Omar Khattab et al.; [code](https://github.com/stanford-iris-lab/meta-harness)) | Outer-loop search over harness *code* with an agentic proposer that reads the source, scores and full traces of all prior candidates via a filesystem. Discovered harnesses beat hand-engineered baselines on Terminal-Bench 2. Spin-offs: SuperagenticAI/metaharness, Harness Forge, Harvey's "Don't Train the Model, Evolve the Harness". |
| [Agentic Harness Engineering (AHE)](https://arxiv.org/abs/2604.25850) (Fudan / PKU / Qiji Zhifeng; NexAU) | Observability-driven evolution from a bash-only seed: 69.7% to 77.0% pass@1 on TB2 in ten iterations (~32 h), beating Codex CLI (71.9%). Gains come from tools, middleware and long-term memory; **prompt-only evolution regresses**. Frozen harness transfers to SWE-bench Verified and across model families. NexAU-AHE tops the TB 2.0 board. |
| [SoL-Pi](https://arxiv.org/abs/2609.20519) (NVIDIA; [code](https://github.com/NVlabs/SoL-Pi)) | Auto-research loops over pi discovered four efficiency mechanisms (action fusion, observation handles, evidence-preserving log reduction, online compaction). Shipped as an opt-in pi extension. NVIDIA offers to benchmark community PRs on a reporting cycle. |
| [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227) | The critique. Under matched feedback and inference budgets, automatic harness evolution does not consistently beat simple test-time scaling, and evolved harnesses generalise poorly to held-out tasks. Any evolution claim needs a held-out split and a test-time-scaling control arm. |
| ACE, TF-GRPO | Prompt/context-evolution baselines that AHE compares against; both underperform component-level evolution. |
| [TokenRhythm/NeoHorse](https://github.com/TokenRhythm/NeoHorse), [CosmosMind-ai/RSI-Harness](https://github.com/CosmosMind-ai/RSI-Harness) | Early recursive-self-improvement-via-harness projects (post-training with a routing harness; pi + versioned "genome" config). Watch, do not cite yet. |

### Experiment platforms

| Project | What it does |
|---|---|
| [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | "Define harnesses as code, run controlled experiments, inspect evidence, compare outcomes." Closest existing product to the protocol in [`benchmarking.md`](benchmarking.md). |
| [Harbor](https://www.harborframework.com), [Claw-SWE-Bench](https://github.com/opensquilla/claw-swe-bench), [HAL harness](https://github.com/princeton-pli/hal-harness) | Runners. See [`benchmarking.md`](benchmarking.md). |
| vals.ai Terminal-Bench 2.1 board | Re-runs models under a unified Terminus-2 harness. Fixed harness, vary model. |
| [LHTB](https://huggingface.co/datasets/IntelligenceLab/LHTB-leaderboard) (Long-Horizon Terminal-Bench) | Records the harness per entry and segregates non-Terminus runs into a `custom-harness` folder outside the ranking. The right disclosure pattern. |
| cliwatch.com | Evaluates model+harness pairs against *your* CLI's docs and behaviour. |

## Regional communities

The English-language map above misses where a large share of the tinkering actually happens.

| Region | What is there |
|---|---|
| China | The DSH/Cordis ecosystem is the single largest concentration of harness work anywhere as of 2026-09. Volcengine ([OpenViking](https://github.com/volcengine/OpenViking)), Tencent ([WeKnora](https://github.com/Tencent/WeKnora)), Alibaba (QwenPaw, AMAP), MemTensor, dream-num all ship DSH plugins. Bilingual awesome-lists and a Chinese-first handbook. Key developer: shigma (Cordis). |
| Korea | Harness Engineering Korea 26Q2 Meetup (~150 attendees, via LangChain Korea); active threads on PyTorchKR; a cluster of high-star Korean-authored repos (revfactory/harness, first-fluke/oh-my-agent, Q00/ouroboros). |
| Japan | Zenn is where the sceptical writing lives (e.g. "why I don't want to say I do harness engineering"); ENSAPIA's "Harness-thon" hackathon (Jul 2026) is an in-person venue. |

## People

A starting list for an X/Mastodon/Bluesky list. Maintainers and paper authors first; commentators second.

- **Origin and theory**: Mitchell Hashimoto (coined the term, 2026-02-05), Ryan Lopopolo (OpenAI field report; playbook repo), Birgitta Böckeler (martinfowler.com), Addy Osmani, Viv Trivedy ("Anatomy of an Agent Harness", harness-as-a-service framing), Dex Horthy (HumanLayer), Boris Cherny (Claude Code), Prithvi Rajasekaran (Anthropic harness-design post).
- **Runtime builders**: Mario Zechner (pi), Can Bölük (oh-my-pi), Peter Steinberger (OpenClaw, pi-skills), Armin Ronacher (pi contributor, prolific writer), Jesse Vincent (superpowers), shigma (Cordis / DSH), Vincent Koc (OpenClaw Foundation), Ian Johnson (tacoda.dev pi harness write-ups), the Nous Research Hermes team.
- **Researchers**: Yoonho Lee, Chelsea Finn, Omar Khattab (Meta-Harness); Melissa Pan, Wei-Lin Chiang, Ion Stoica, Matei Zaharia (HarnessTax); the NexAU / AHE group; Kilian Lieret and John Yang (SWE-agent, mini-swe-agent); Mike Merrill and Alex Shaw (Terminal-Bench, Harbor); the LHTB team.

## Where discussion actually happens

There is no single venue. In rough order of signal density:

1. GitHub issues, PRs and Discussions on pi, oh-my-pi, deepseek-harness, OpenHands, mini-swe-agent, harness-engineering-guide, meta-harness.
2. X / Mastodon. Search `harness engineering`, `agent harness`, `loop engineering`, `scaffold effect`, `harness tax`; follow the people above.
3. Project Discords: DeepSeek Harness, OpenClaw, Hermes, oh-my-pi, OpenCode, Goose; Slacks: OpenHands, SWE-bench.
4. Hacker News threads on each new paper (HarnessTax, Empirical Study, OpenAI post, "Harnesses Explained") are where practitioners argue methodology.
5. arXiv cs.SE / cs.AI, filtered on `harness`, `scaffold`, `harness evolution`.
6. Hugging Face: datasets and published sessions (Terminal-Bench, Claw-SWE-Bench, LHTB, pi sessions).
7. Regional: DSH Discord and Chinese docs; LangChain Korea / PyTorchKR; Zenn.

## Signal versus noise

- **Topic tagging is gamed.** `harness-engineering` is on a 91k-star RAG engine, a macOS proxy app and a Xiaohongshu scraper; `dsh-plugin` is on an image uploader and a resume builder. Never rank by topic alone; require the keyword in the description or README.
- **Star counts on 2026 repos are inflated** by the OpenClaw and DSH waves. Prefer commit velocity, issue-close rate and whether trajectories or ablations are published.
- **GitHub redirects renamed repos silently.** `badlogic/pi-mono` still resolves; a digest script will keep "working" while reporting the wrong canonical name.

See [`monitoring.md`](monitoring.md) for how to watch these on a cadence.
