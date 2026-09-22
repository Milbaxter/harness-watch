# The landscape

For the current prioritized map, concrete design PRs, and activity caveats, read the **[22 September hotspot audit](hotspots-2026-09-22.md)**. Older numerical benchmark claims below were not all revalidated by that audit.

The word "harness" is used for three different things. The people working on each layer mostly do not read each other. Knowing which layer you care about tells you where to look.

```
┌──────────────────────────────────────────────────────────────┐
│ Layer 3: Curation & research                                 │
│   awesome-lists, guides, arXiv papers, benchmark projects    │
├──────────────────────────────────────────────────────────────┤
│ Layer 2: Config layer on top of a runtime                    │
│   AGENTS.md / CLAUDE.md, skills, hooks, plugins, MCP configs │
│   (this is what most people mean by "my harness")            │
├──────────────────────────────────────────────────────────────┤
│ Layer 1: Runtimes (the agent loop itself)                    │
│   pi, OpenHands, mini-swe-agent, OpenCode, Goose, ...        │
└──────────────────────────────────────────────────────────────┘
```

## Layer 1: Open runtimes

These are the projects where the loop, tools, context policy and stop conditions are themselves open and being changed by individuals.

| Project | Why it matters | Where the iteration happens |
|---|---|---|
| [pi-mono](https://github.com/earendil-works/pi) (Mario Zechner) | Deliberately minimal, self-extensible harness. Community ships extensions/skills/prompts/themes as [pi packages](https://pi.dev/docs/latest/packages) via npm or git. Author publishes his raw work sessions to Hugging Face (`badlogicgames/pi-mono`), one of very few people sharing trajectories rather than configs. | GitHub issues/PRs, RFCs in-repo, [pi.dev package registry](https://pi.dev/packages?type=extension), X |
| [oh-my-pi](https://github.com/can1357/oh-my-pi) (Can Boluk) | Fork of pi, coding-first, moves faster: LSP integration, subagents, pluggable memory backends, browser relay. ~80k weekly npm downloads for `@oh-my-pi/pi-coding-agent` as of 2026-08. Inherits `.claude`, `.cursor`, `.codex` etc. configs on first run. | GitHub, Discord (linked from README), community extension repos (e.g. `omp-discord`) |
| [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) / [SWE-agent](https://github.com/SWE-agent/SWE-agent) (Princeton / Stanford) | ~100-line bash-only baseline scoring >74% on SWE-bench Verified. The harness everyone ablates against; also the harness behind the SWE-bench "bash only" leaderboard (fixed harness, vary model). | GitHub, papers, SWE-bench Slack |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Production-grade, Docker-sandboxed, best-documented internal design (context condensation, prompt-injection mitigation, `openhands-sdk`). | GitHub, Slack, docs |
| [OpenCode](https://github.com/anomalyco/opencode) | Popular TUI agent, provider-agnostic, large plugin surface. | GitHub, Discord |
| [Goose](https://github.com/aaif-goose/goose) (Block) | Extensible desktop/CLI agent with MCP-first tooling. | GitHub, Discord |
| "Claw" family: OpenClaw, NanoBot (HKUDS), Hermes (Nous Research), ZeroClaw, NullClaw, Moltis | General-purpose personal-assistant runtimes (not coding-first). Relevant because the first fixed-model harness benchmarks target exactly this family. | GitHub |

## Layer 2: Config and workflow layers

Claude Code and Cursor expose user-configurable behavior. [Codex CLI](https://github.com/openai/codex) is itself open source, and also supports user-supplied configuration. This layer is enormous and shallow: thousands of repos, almost no shared evaluation.

| Hub | What it is |
|---|---|
| [awesome-claude-code](https://github.com/sadsfae/awesome-claude-code) | De facto index of skills, hooks, slash commands, orchestrators, `CLAUDE.md` examples. Also links the extracted Claude Code system prompts (Piebald AI), which is the closest thing to reading the closed harness's source. |
| [awesome-claude-plugins](https://github.com/Chat2AnyLLM/awesome-claude-plugins) | Metadata catalog of Claude Code plugin marketplaces: ~190 marketplaces, ~2,500 plugins as of 2026-06. |
| [awesome-claude-code-workflows](https://github.com/sergeykrin9/awesome-claude-code-workflows) | Methodologies, memory systems, `CLAUDE.md`/`HANDOFF.md` templates. |
| [claudelicious](https://github.com/BioInfo/claudelicious) | One operator's complete wired-together setup with the reasoning behind each piece. A model for how to publish a harness rather than a snippet. |
| [harness-lab](https://github.com/hgflima/harness-lab), [madebywild/agent-harness](https://github.com/madebywild/agent-harness), [ar27111994/agent-harness](https://github.com/ar27111994/agent-harness), [orkestr](https://github.com/eooo-io/orkestr) | Attempts at portable registries / package managers for harness assets across Claude Code, Codex, Cursor, pi, OpenCode, Copilot. All small (tens of stars) as of 2026-09. Nobody has won this. |
| Cursor rules / Codex `AGENTS.md` collections | Same pattern, smaller. Search GitHub for `path:.cursor/rules` or `filename:AGENTS.md`. |

## Layer 3: Curation and research

| Resource | Notes |
|---|---|
| [Turi-Labs/awesome-harness](https://github.com/Turi-Labs/awesome-harness) | Curated, includes eval and infra-noise references. |
| [Lijunjie2/awesome-agent-harness](https://github.com/Lijunjie2/awesome-agent-harness) | Implementation-first, 120+ entries, EN/ZH. |
| [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | Overlapping list, includes meta-harnesses (Omnigent). |
| [nexu-io/harness-engineering-guide](https://github.com/nexu-io/harness-engineering-guide) ([harness-guide.com](https://harness-guide.com)) | Structured guide (loop, tools, memory, guardrails, eval infra) with GitHub Discussions enabled. Discussion activity and central-forum status were not verified; the repository last-push date observed on September 22 was April 19. |
| Anthropic engineering blog | [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) and related posts are primary sources for eval methodology. |
| [thedeepfeed.ai: Measuring the agent harness](https://www.thedeepfeed.ai/posts/2026-06-22-how-much-is-the-harness-worth-measuring-agent-scaffolds/) | Best single synthesis of the 2026 harness-effect papers. |

### Key 2026 papers

| Paper | Finding |
|---|---|
| [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) | 3 models x 3 harnesses on SWE-bench Verified: harness variance 7.8x model variance; 6 of 9 model rankings reverse across harnesses. Proposes the "Harness Card". |
| [The Scaffold Effect](https://arxiv.org/abs/2607.22585) | Goose / OpenCode / OpenHands-SDK on Terminal-Bench Pro: pass rates within 2-8 pp, tokens per solved task differ up to 40x, failure fingerprints are harness-specific and model-independent. |
| [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804) | Component ablations (planning, action space, context management) across 176 settings. Effects depend on model strength and context budget. |
| [Harness-Bench](https://arxiv.org/abs/2605.27922) | 6 harnesses x 8 models x 106 tasks, full factorial. 23.8-point spread between best and worst harness on the same model pool. |
| [Claw-SWE-Bench](https://arxiv.org/abs/2606.12344) | Same model, adapter design alone moves SWE-bench Pass@1 from 19.1% to 73.4%. Model choice: 29.4 pp; harness choice: 27.4 pp. |
| [Holistic Agent Leaderboard (HAL)](https://arxiv.org/abs/2510.11977), ICLR 2026 | 21,730 rollouts; task-specific scaffolds beat generalist ones in 20/24 comparisons; cost must be reported alongside accuracy. |
| [Terminal-Bench](https://www.tbench.ai) paper | Acknowledges each leaderboard entry used "the agent scaffold chosen to maximize performance". |

## Where discussion actually happens

There is no single venue. In rough order of signal density:

1. GitHub issues, PRs and Discussions on pi-mono, oh-my-pi, OpenHands, mini-swe-agent, harness-engineering-guide.
2. X. Search `harness engineering`, `agent harness`, `scaffold effect`; follow the authors of the projects and papers above.
3. Project Discords/Slacks (oh-my-pi, OpenCode, Goose, OpenHands, SWE-bench).
4. arXiv cs.SE / cs.AI, filtered on `harness` and `scaffold`.
5. Hugging Face: datasets and published sessions (Terminal-Bench, Claw-SWE-Bench, pi sessions).

See [`monitoring.md`](monitoring.md) for how to watch these on a cadence.
