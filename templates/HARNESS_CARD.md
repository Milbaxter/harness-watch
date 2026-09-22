# Harness Card: <harness name> <version / commit>

Publish one of these next to every score. Adapted from the disclosure proposal in [Stop Comparing LLM Agents Without Disclosing the Harness](https://arxiv.org/abs/2605.23950) and Terminal-Bench submission requirements. Fill in every row; write "not exposed" if the harness hides a setting, never leave it blank.

## Identity

| Field | Value |
|---|---|
| Harness name and version / commit | |
| Source (URL) | |
| Open source? | yes / no / partially (which parts) |
| Maintainer | |
| Date of this card | |

## Model interface

| Field | Value |
|---|---|
| Model ID(s) used | exact provider string |
| Reasoning effort / thinking budget | |
| Temperature / sampling | |
| Max output tokens | |
| Provider / gateway (direct API, OpenRouter, Bedrock, ...) | |
| Prompt caching enabled? | |

## Context construction

| Field | Value |
|---|---|
| System prompt | link or hash; "closed" if unknown |
| Project instruction files loaded (AGENTS.md, CLAUDE.md, .cursor/rules, ...) | list, with hashes |
| Skills / plugins / hooks active | list, with versions |
| Context window budget | |
| Context management strategy (none / truncation / rule-based elision / LLM summarisation / recoverable) | |
| Memory across sessions | none / file / vector / other |

## Tools and action space

| Field | Value |
|---|---|
| Tool list | |
| Edit mechanism (bash-only / str_replace / full-file write / LSP-assisted) | |
| MCP servers attached | |
| Subagents / delegation | yes / no; how many, what for |
| Parallel tool calls | |
| Web / network access during task | allowed / blocked |

## Control loop

| Field | Value |
|---|---|
| Planning step | none / explicit plan / plan-and-revise |
| Max turns | |
| Stop condition | model-declared / verifier-gated / budget |
| Retry / recovery policy | |
| Loop detection | |
| Approval / permission model during eval | fully autonomous / auto-approve list / other |

## Execution environment

| Field | Value |
|---|---|
| Sandbox (Docker / Daytona / local / other) | |
| CPU / RAM / disk limits and how enforced | |
| Multiple of task-stated minimum resources | e.g. 3x |
| Wall-clock timeout per task | |
| Network policy | |

## Evaluation run

| Field | Value |
|---|---|
| Benchmark and version / commit | |
| Task subset (list or file hash) | |
| Trials per task (k) | |
| Runner (Harbor / Claw-SWE-Bench / HAL / custom) and version | |
| Dates of runs | |
| Exact command line | |
| Trajectories | URL |
| Rate card used for cost, and date | |

## Known limitations of this card

Anything you could not pin or observe. Be specific.
