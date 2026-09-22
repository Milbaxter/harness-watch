# Mechanism scan: what open harnesses actually implement, and what of it is measurable (2026-09-22)

This is not another map of *where* harness work happens. [`reports/2026-09-22-hotspot-survey.md`](2026-09-22-hotspot-survey.md) and [`docs/landscape.md`](../docs/landscape.md) already name the projects, the standards, and the communities. This note asks a different question:

**If you want to know whether one harness is better than another, which knobs differ in the source, which of those knobs have a measured effect, and which pairs can a public runner actually drive on the same day?**

Read on 2026-09-22 from repository docs and source, not from star counts or READMEs of awesome-lists. A cell is omitted or marked **not found** when the file was not in the set that was opened. Package versions below are the `version` field in the tree that was fetched, not a claim about the latest GitHub release. No benchmark was re-run.

## What is comparable this week

[Harbor](https://github.com/harbor-framework/harbor) is the runner that already wraps the coding CLIs. Its installed-agent adapters, read from `src/harbor/agents/installed/`, are Claude Code, Codex, Gemini CLI, Goose, Hermes, mini-swe-agent, OpenCode, OpenHands, OpenHands SDK, and pi. The public [ATIF doc](https://harborframework.com/docs) still lists a shorter set (Terminus-2, OpenHands, mini-swe-agent, Gemini CLI, Claude Code, Codex, Muse). The code is ahead of that page. Harbor writes an [Agent Trajectory Interchange Format](https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md) trajectory with token and `total_cost_usd` fields.

Terminal-Bench's current dataset README ([harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench)) is Terminal-Bench 4.0 on the Harbor Hub, and the documented run is `harbor run -d terminal-bench/terminal-bench@latest -k 5`. That is the trial count this repo's protocol already asks for.

Everything else is a different experiment:

| Runner | What it can vary | What it cannot |
|---|---|---|
| Harbor | The ten installed agents above, on Terminal-Bench, into ATIF | ZCode, DeepSeek Harness, deepagents, Prime Agent (no adapter in the tree that was read) |
| [Claw-SWE-Bench](https://github.com/TokenRhythm/claw-swe-bench) (`opensquilla/claw-swe-bench` redirects here) | `openclaw`, `hermes`, `nanobot`, `zeroclaw`, `generic`, same prompt, runner-side `git diff` | Coding CLIs. Adding one is a `BaseClawAdapter` |
| [HarnessRouter](https://github.com/HarnessRouter/harnessrouter) | One Responses-shaped API. The in-sandbox runner comment lists backends `claude`, `codex`, `hermes`, `dsh` (`pi -p --mode json` is the pi backend), and normalises events to Claude Code `stream-json` | It is a driver, not a leaderboard. A turn is one CLI shot inside a sandbox |
| [HAL harness](https://github.com/princeton-pli/hal-harness) | Historical: SWE-bench Verified, USACO, tau-bench, CORE-bench, Weave cost | README says the repo is **archived** and the leaderboard is no longer updated through it |
| [HarnessBench (Qihoo360)](https://github.com/Qihoo360/harness-bench) | Adapters named in the README: `openclaw`, `picoclaw`, `nanobot`, `fairyclaw`, `demo`. Oracle plus a token total | Not the coding CLIs |
| [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | Reads sessions from Claude Code, Codex, Cursor, Copilot, Pi, and others and writes a workflow report | Not an experiment runner. The README is a host-session auditor ("improve the loop around them"), not a harness-vs-harness board |
| [SoL-Pi](https://github.com/NVlabs/SoL-Pi) | Four opt-in efficiency mechanisms on an unmodified pi | pi only |

[txcript](https://github.com/skillsynchq/txcript) (Apache-2.0) converts a live session among Claude Code, Codex, and OpenCode so a conversation can continue. It does not produce an eval trajectory. Harbor's ATIF export is the format that does.

## How the open harnesses differ

Versions in the tree fetched that day: pi `@earendil-works/pi-coding-agent` 0.87.0 (MIT), oh-my-pi `@oh-my-pi/pi-coding-agent` 18.2.8, DeepSeek Harness root `0.1.7-alpha.1` (MIT), ZCode package `3.14.0` (Apache-2.0), deepagents `0.7.17` (MIT). Codex CLI, Goose, and Gemini CLI are Apache-2.0. OpenCode, OpenHands SDK, Hermes Agent, and Prime Agent are MIT. Prime Agent's LICENSE still carries Mario Zechner's copyright alongside Prime Intellect's; the README describes a different product from pi.

### Loop, stop, retry

| Harness | What the source says |
|---|---|
| pi | A turn ends when the model stops calling tools. Auto-compaction runs when `contextTokens > contextWindow - reserveTokens` (default reserve 16,384; keep-recent default 20k), checked after tool results and before the next assistant turn. One compact-and-retry is allowed on context overflow or a length stop. **No max-turn counter was found** in the agent-loop sources that were opened. [compaction](https://github.com/earendil-works/pi/blob/main/docs/compaction.md) |
| oh-my-pi | Retry and compaction are separate. `TurnRecovery` retries `stopReason === "error"` except context overflow, which goes to compaction. [non-compaction retry](https://github.com/can1357/oh-my-pi/blob/master/docs/non-compaction-retry-policy.md) |
| DeepSeek Harness | `ReactLoopAgent`: call model, run tools, repeat. `maxParallelToolCalls` bounds the parallel pool. A listener may answer `agent/request-error` with `{ kind: 'retry' }`; an unhandled failure ends the turn. **No task-level turn budget in the agent-loop README.** [dsh-agent-loop](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/agent-loop/README.md) |
| ZCode | The CLI `AGENTS.md` states the design on purpose: do **not** hard-stop on tool-call count. Stop conditions are context compaction, user cancel, permission denial, tool timeout, output truncation, and provider retry caps. Sessions live in `~/.zcode/cli/db/db.sqlite` |
| mini-swe-agent | v2 default is a native `bash` tool, not a fenced command. `mini.yaml` sets `step_limit: 0` (no step cap) and `cost_limit: 3`. Exit is an exception that is written into the trajectory. [v2 migration](https://github.com/SWE-agent/mini-swe-agent/blob/main/docs/v2_migration.md) |
| Hermes | `IterationBudget`, default **500** turns via `agent.max_turns`. Subagents get their own budget, default 50 (`delegation.max_iterations`). Three consecutive reasoning-only Codex Responses continuations fail over. [agent loop](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop) |
| OpenHands SDK | `StuckDetector` watches four patterns: repeated action/observation, repeated action errors, monologue, and alternating pairs (`openhands/sdk/conversation/stuck_detector.py`). `LLMSummarizingCondenser` rolls the event view, default `max_size` 240 |
| Gemini CLI | `loopDetectionService.ts`: tool-call loop threshold 5, content loop threshold 10, then an LLM loop check (history 20, confidence 0.9). Headless mode returns one JSON object or a JSONL event stream, including usage |
| Goose | Compaction fires as a fraction of the context limit (`ops_compaction.rs`). Permission modes are `auto`, `smart_approve`, `approve`, and `chat` |
| Codex CLI | Mid-turn and pre-turn compaction are different code paths (`core/src/compact.rs`); pre/post compact hooks exist. Sandbox backends in tree: macOS seatbelt, Linux landlock, bubblewrap (`codex-rs` sandboxing crate) |
| Prime Agent | README only. Persistent Python REPL; `rlm.spawn` for child agents; `/refine` may edit durable harness state and must not rewrite the base system prompt. Explicitly **not** a security sandbox |
| deepagents | Library. Summarization, message-eviction, and overflow-clip middleware. `AGENTS.md` from `~/.deepagents/` and `./.deepagents/` is injected as `<agent_memory>`. Filesystem tools include `ls`, `read_file`, `glob`, `grep` (read class) |

### The edit tool is the least standardised knob, and the one with the largest published effect

| Harness | Edit contract | Read-before-edit |
|---|---|---|
| pi | `edit` takes `edits[]` of `{oldText, newText}`. Each `oldText` must be unique and is matched against the **original** file, not after earlier edits in the same call | Not found as a hard gate |
| oh-my-pi | Default mode is **hashline**: the model must copy a 4-hex snapshot tag from the latest `read` / `grep` / successful `edit` (`[path#1A2B]`). Other modes: `apply_patch`, `patch`, `replace` | The tag *is* the read receipt |
| DeepSeek Harness | Base profile: `read`, `write`, `edit`. `str_replace_editor` is opt-in (`tool-str-replace-editor`) | Not stated for the default editor |
| ZCode | Edit handler maintains read-before-edit state (`read-file-state.ts`); a stale read does not match | Yes, in the handler comment and the state machine |
| OpenHands SDK | One `file_editor` tool: `view`, `create`, `str_replace`, `insert`, `undo_edit` | `view` is a separate command on the same tool |
| mini-swe-agent | No edit tool. The model runs `bash` | n/a |
| Codex CLI | `apply_patch` handler is a first-class tool spec | Not confirmed in the spec header that was opened |
| deepagents | Patch middleware exists (`patch_tool_calls.py`); the exact wire schema was not copied out | Not confirmed |

Can Bölük's [hashline post](https://blog.can.ac/2026/02/12/the-harness-problem/) (2026-02-12) changed **only** the edit format and reported about +15 points versus a diff/`apply_patch` format across 16 model rows, and a 6.7% → 68.3% jump for one weak editor. oh-my-pi now ships that format as the default. pi still ships exact `oldText`. pi is a Harbor installed agent; oh-my-pi is not, so the second arm is a custom Harbor agent (or a pi run with `edit.mode` left as exact replace, which is a weaker comparison). That pair is still the cleanest public A/B this scan found, and neither of the earlier surveys named the edit-format split.

Claw-SWE-Bench's own diagnostic points the same direction from the other side: asking the model to *emit a unified diff* scored 19.1% with 69.1% apply failures; letting it edit through native tools and taking `git diff` on the runner scored 73.4% ([2606.12344](https://arxiv.org/abs/2606.12344) §5.1). The paper says this is a diagnostic, not a component ablation. It is still the difference between "the harness collects the patch" and "the model has to be a diff printer".

### Context, memory, delegation, permissions

pi compacts by LLM summary and keeps file operations in the summary ([compaction doc](https://github.com/earendil-works/pi/blob/main/docs/compaction.md)). It has **no built-in sandbox** and says so: project trust only gates whether `.pi/` settings and extensions load; `AGENTS.md` / `CLAUDE.md` load either way ([security](https://github.com/earendil-works/pi/blob/main/docs/security.md)). Sessions are a JSONL tree at `~/.pi/agent/sessions/` (format v3). There is no built-in todo tool; the README says todos confuse models and tells you to use a `TODO.md`. The footer reports tokens, cache, and dollar cost. Headless: `-p`, `--mode json`, `--mode rpc`.

oh-my-pi adds, on top of that shape: snapcompact (history stored as dense bitmaps), mechanical elision (`shake`), provider-native streaming compaction, a `todo` tool with `init/start/done/drop/block`, a `task` tool that batches subagents and can isolate them, and five memory backends defaulting to **off** (`local`, `hindsight`, `mnemopi`, `sharpshooter`). Approval modes are `always-ask`, `write`, and `yolo`, and **`yolo` is the default**. Context-file discovery reads `.omp/`, Claude, Gemini, and other agents' instruction files ([context files](https://github.com/can1357/oh-my-pi/blob/master/docs/context-files.md)).

DeepSeek Harness's base profile mounts file edit, a platform shell (bash, or PowerShell on Windows), web search, public HTTP fetch, subagents, and task/goal tracking. Writes go through a sandboxed filesystem; on macOS/Linux the shell row is `bash-sandbox`, on Windows an ACL restricted-token runner. Web fetch is not per-call approved, but the provider rejects non-public hosts. Headless is `dsh --profile headless --json`. The `sdk-minimal` bundle exists so a benchmark can mount a smaller composition; `BENCHMARK.md` points at the Python SDK `jsonrpc-agent`. Dollar cost was **not found**; the token meter that was opened is context pressure, not a rate card.

ZCode's hook contract (from `NOTICE.md`) is `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PostToolUseFailure`, `Stop`. `AGENTS.md` asks the CLI to record token and cost from the first version. A todo handler and a plan-mode handler are in the tool tree.

Hermes persists sessions in SQLite (`state.db`) and, separately, can export ShareGPT JSONL trajectories (`trajectory_samples.jsonl` / `failed_trajectories.jsonl`). Micro-compaction is its own doc. That split matters: the SQLite file is the product log; the JSONL is the training export. They are not the same schema as Harbor ATIF.

## What the 2026 papers say those knobs do

Effects below were read from the papers on 2026-09-22. They are not replications.

| Knob, as it exists in a runtime above | Best evidence | Direction |
|---|---|---|
| Edit format (hashline / native tool-edit vs asking for a diff) | [Bölük](https://blog.can.ac/2026/02/12/the-harness-problem/); Claw-SWE-Bench §5.1 | Largest single swing in this set (+15 pts average in the blog; 19.1% → 73.4% in the diagnostic). Not ablated in the peer-reviewed harness-design study |
| Typed tools vs bash-only | [2609.20804](https://arxiv.org/abs/2609.20804) Fig 7 | Depends on the model. A 30B model gained +15.0 pp (SWE-bench) / +10.1 pp (Terminal-Bench) from typed tools; 66% of its bash-only Terminal-Bench runs died by emitting a tool that does not exist. A 550B model was *better and cheaper* on bash-only (+3.6 / +5.6 pp, cost −53% / −30%). mini-swe-agent is the bash-only arm; pi's four tools and OpenHands' editor are the typed arm |
| Explicit plan tool, injected every turn | same paper, Fig 6 | Helps a weak model (+11.6 pp SWE, but +293% turns) and *saves cost* on a strong one (about −30% with no accuracy gain). oh-my-pi and ZCode ship a todo/plan tool; pi's README refuses a built-in one |
| Compaction / elision | same paper, §3.2; [SoL-Pi](https://arxiv.org/abs/2609.20519) | The gain over "die on overflow" collapses as the window grows: 35.7 pp at 32k → 2.7 pp at 128k on SWE-bench. Staged elision-then-summary was the cheap variant. Recall of elided text was a no-op (−0.36 pp; most settings never called it) |
| SoL-Pi's four mechanisms on pi | [2609.20519](https://arxiv.org/abs/2609.20519) Tables 2 and 4; [README](https://github.com/NVlabs/SoL-Pi) | All four off unless `sol-pi.json` opts in. Stack: about −49% tokens and 94% of pi's score on their 51-task set. ObservationPack alone *raised* the score on one backend. Action fusion (edit plus the follow-up command in one call) was the best single add on the other |
| Long-term memory file vs prompt-only edits | [AHE, 2604.25850](https://arxiv.org/abs/2604.25850) Table 3 | Memory-only +5.6 pp, tool-only +3.3, finish-hook +2.2, **prompt-only −2.3**. Prompt-only edits are the most consistently negative lever across AHE, Meta-Harness's rejected candidates, and the [evolution critique](https://arxiv.org/abs/2607.12227) |
| Verification gate before "done" | AHE middleware; Meta-Harness appendix; Scaffold Effect | Helps a little and causes loops. Meta-Harness's double-confirm checklist produced 15–40 step spirals; removing it also got worse. OpenHands' fingerprint is `VERIFY` / `MAX_TURNS`; Goose's is `REASON` and it stops ([2607.22585](https://arxiv.org/abs/2607.22585)) |
| Same model, three coding harnesses, cost not accuracy | [HarnessTax](https://harnesstax.github.io/) (2026-09-16) | Claude Code's initial context was >10× pi's. Success moved a few points; cost moved up to ~5×. pi (`read`, `write`, `edit`, `bash`) sat on the cost frontier. No component ablation |
| Harness evolution vs just sampling more | [2607.12227](https://arxiv.org/abs/2607.12227) | Under a matched feedback budget, evolving the harness scored *below* parallel sampling, and the held-out gain was about +0.6 pp. Any auto-tune claim needs a disjoint test split and that control |
| Container CPU/RAM headroom | [Anthropic infra noise](https://www.anthropic.com/engineering/infrastructure-noise) | 1× limits: 5.8% infra errors and −6 pp vs uncapped on Terminal-Bench 2.0. Same order as several "harness improvements" |

Two Anthropic engineering posts that this repo previously cited by title only, now with URLs: [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) and [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-03-24). Both are qualitative. The second one says context resets mattered for Sonnet 4.5 and were dropped for Opus 4.5, and that a planner was kept because the generator under-scoped without it. That matches the paper result that planning is a model-strength interaction, not a universal good.

Knobs that are common in the runtimes above and still have **no controlled result** in this set: permission modes, hook vetoes, prompt-cache warming, subagent delegation as an isolated factor, and progress files.

## Three comparisons that would teach something new

1. **pi vs oh-my-pi, same model, Terminal-Bench `@latest`, k=5.** The intended difference is the edit contract (exact `oldText` vs hashline) plus oh-my-pi's todo tool and `yolo` approvals. Harbor already launches pi. oh-my-pi needs a thin installed-agent wrapper first; until that exists, do not pretend `-a oh-my-pi` works. Publish both Harness Cards. If oh-my-pi wins on a weak model and ties on a strong one, that reproduces Bölük and the planning result at once. Pin `edit.mode` so a later default change does not silently rewrite the arm.
2. **mini-swe-agent vs pi vs OpenHands SDK, two models (one cheap, one frontier).** The empirical study says the ranking of bash-only vs typed tools flips with model size. A single-model "bash is enough" claim does not survive that paper.
3. **pi vs pi with SoL-Pi's ObservationPack only, then the full stack.** The paper's add-one table says the stack is not uniformly better than the best single mechanism. All four flags default off, so the control arm is unmodified pi.

Do not treat a win on the same tasks that an evolution loop searched as a harness improvement. The critique paper's held-out delta was ~0.

## Corrections that change a watchlist entry

These are mechanism-level, not a new catalog. GitHub still redirects the old names, so a digest that stores the old path looks healthy and reports the wrong repo.

| Was | Is, as fetched 2026-09-22 |
|---|---|
| `badlogic/pi-mono` | `earendil-works/pi` |
| `sst/opencode` | `anomalyco/opencode` |
| `block/goose` | `aaif-goose/goose` |
| `opensquilla/claw-swe-bench` | `TokenRhythm/claw-swe-bench` |
| Terminal-Bench 2.1 as the current dataset | `terminal-bench/terminal-bench@latest` (4.0 README); `-k 5` is the documented oracle run |
| HAL as a live cost-aware board | Repository archived; board no longer updated through that harness |
| better-harness as an experiment runner | Session auditor over several hosts' native transcripts |

`data/mechanisms-2026-09-22.yml` is the same matrix in a form a Harness Card can be pre-filled from. Fields that were not opened are absent, not guessed.
