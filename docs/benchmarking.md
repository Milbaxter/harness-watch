# Benchmarking and verifying a harness

The question "is my harness better than Joe's?" is answerable. It is just not answered by any public leaderboard, because leaderboards vary the model and let each vendor pick the harness. This doc describes the protocol that does answer it, the tooling that exists for it, and the traps.

## What the 2026 literature established

Read these numbers before designing an experiment; they set your noise floor.

| Effect | Size | Source |
|---|---|---|
| Harness variance vs model variance, SWE-bench Verified, 3x3 factorial | 7.8x larger; 6 of 9 model rankings flip | [2605.23950](https://arxiv.org/abs/2605.23950) |
| Same model, different harness, Terminal-Bench Pro | 2-8 pp pass rate; up to **40x** tokens per solved task | [2607.22585](https://arxiv.org/abs/2607.22585) |
| Same model, adapter design only, SWE-bench | 19.1% to 73.4% Pass@1 | [2606.12344](https://arxiv.org/abs/2606.12344) |
| Container CPU/RAM limits only, Terminal-Bench 2.0 | up to 6 pp | [Anthropic](https://www.anthropic.com/engineering/infrastructure-noise) |
| Broken SWE-bench test cases | 24.4% of Verified gradings changed after fixing | UTBoost, ACL 2025 |
| Typical "meaningful" model upgrade reported in papers | 2-4 pp | [2605.23950](https://arxiv.org/abs/2605.23950) |

Implications: a 3-point pass-rate difference between two harnesses on 50 tasks with one trial each is noise. Cost and failure mode differences are usually larger and more reproducible than pass-rate differences.

## The protocol

### 1. Decide what "better" means before you run anything

Pick a primary metric and one or two secondary metrics. Reasonable choices:

- **Primary**: pass rate at a fixed token or dollar budget per task (pass@budget). This is what matters operationally and it is where harnesses differ most.
- **Secondary**: mean tokens per solved task; wall-clock per solved task; number of no-op / idle turns; infra-error rate.
- **Diagnostic**: failure fingerprint (see step 6).

Pass@1 with unlimited budget is the metric leaderboards use. It is the least informative one for harness comparison.

### 2. Lock everything except the harness

| Variable | Lock it to |
|---|---|
| Model | One exact model ID and one reasoning-effort setting. Ideally test two models (one strong, one cheap); harness effects invert between them. |
| Task set | Same task IDs, same version. Record the dataset commit hash. |
| Sandbox | Same image, same CPU/RAM/disk limits. Set limits to **3x or more** of the task's stated minimum; below that you are measuring the container, not the harness. |
| Budget | Same max turns, same max tokens or dollars, same wall-clock timeout. Make the budget binding for at least some tasks or you learn nothing about efficiency. |
| Prompt | Same task prompt text handed to each harness. Harness-internal system prompts are part of the harness and may differ. |
| Network | Same policy (offline is cleanest). |
| Temperature / seed | Fixed where the provider allows it; otherwise rely on repeats. |

Write all of this down in a [Harness Card](../templates/HARNESS_CARD.md) for each harness before running.

### 3. Run enough trials

- **k = 5 trials per task minimum.** Terminal-Bench requires this for submissions and it is the practical floor for stable estimates.
- **50 to 100 tasks** if you want to detect differences under 10 pp. Fewer tasks is fine for iterating on your own harness but not for claiming victory.
- Run harness A and harness B on the **same task instances in the same window**. Provider behaviour drifts week to week.

### 4. Use paired statistics

Compute per-task differences (A minus B) and bootstrap the mean difference across tasks. Report the 95% CI. If the interval includes zero, say so. Do not compare two aggregate pass rates with an unpaired test; tasks vary far more than harnesses do.

### 5. Report cost and latency alongside accuracy

For every run: input tokens, output tokens, cached tokens, dollar cost at a stated rate card and date, wall-clock, turns. Then report:

- tokens per solved task
- dollars per solved task
- pass rate at 50% and 25% of the full budget (cut the trajectory and check if it had already succeeded)

The Scaffold Effect result (40x token spread, 2-8 pp pass spread) is the norm, not the exception. A harness that is 1 pp worse at a tenth of the cost is the better harness for most users.

### 6. Classify failures

Read a sample of failed trajectories from each harness and tag them. A workable taxonomy:

| Tag | Meaning |
|---|---|
| `MAX_TURNS` | Hit turn budget while still making progress |
| `IDLE_LOOP` | Repeated no-op or identical tool calls |
| `WRONG_VERIFY` | Declared done without running or passing tests |
| `BAD_EDIT` | Edit tool failed or corrupted file |
| `CONTEXT_OVERFLOW` | Context limit hit, harness did not recover |
| `REASONING` | Model misunderstood task; harness gave it what it needed |
| `INFRA` | Container, network or provider error |
| `TIMEOUT` | Wall-clock exceeded |
| `REFUSAL` | Model declined |

Harness fingerprints are stable across models (Scaffold Effect: Goose fails on reasoning, OpenHands-SDK on verify/max-turns, OpenCode on idle loops). The fingerprint tells you *what to change*; the pass rate does not.

### 7. Publish trajectories

Upload raw trajectories (Harbor Hub, Hugging Face, or a tarball in the repo). Anyone claiming a harness result without trajectories is asking you to trust them. Include the exact command line.

## Tooling that exists today

### Harbor (Terminal-Bench runner)

[Harbor](https://www.harborframework.com) is the framework behind Terminal-Bench 2.x and later. It is the most complete general-purpose runner: sandbox providers (Docker, Daytona, others), `-k` trials, uploads, trajectory viewer.

To evaluate your own harness, subclass `BaseAgent` or `BaseInstalledAgent` (see Harbor's agents docs; the built-in Claude Code and Codex agents are the reference examples). Then:

```bash
uv tool install harbor            # or: pip install harbor
harbor run \
  -d terminal-bench/terminal-bench-2-1 \
  -a <your-agent> \
  -m <provider/model> \
  --ak reasoning_effort=<effort> \
  -e docker \
  -k 5 \
  -n <concurrency>
```

Run the same command with `-a <joes-agent>`. Check sandbox resource limits in the task configs and raise them uniformly if you are below 3x.

Terminal-Bench is terminal-task heavy (bio, security, systems), not repo-editing heavy. If your harness is a coding agent, pair it with a SWE-style set.

### Claw-SWE-Bench (SWE-bench with a harness-neutral adapter)

[opensquilla/claw-swe-bench](https://github.com/opensquilla/claw-swe-bench) makes arbitrary harnesses comparable on SWE-bench Verified / Multilingual by fixing the prompt, workspace contract, patch extraction and evaluator. Adding a harness is one `BaseClawAdapter` subclass plus a registry entry. Use the 80-task **Lite** subset for iteration and the 350-task full set for claims.

```bash
python3 run_infer.py \
    --claw <yours> \
    --dataset multilingual \
    --run_id <yours>-lite-1 \
    --instance_file config/<lite-instance-list>.txt \
    --model <provider/model> \
    --timeout 3600

python3 run_eval.py \
    --predictions artifacts/<yours>-lite-1/predictions.jsonl \
    --dataset_name SWE-bench/SWE-bench_Multilingual \
    --run_id <yours>-lite-1
```

The runner enforces the fairness properties for you: identical prompt, no network, future-commit stripping, runner-side `git diff` patch collection, per-instance containers with `--pids-limit 300 --memory 8g`. Results are posted at [claw-swe-bench.github.io](https://claw-swe-bench.github.io/).

### HAL harness

[princeton-pli/hal-harness](https://github.com/princeton-pli/hal-harness): framework-agnostic wrapper with Weave cost tracking across SWE-bench Verified Mini, USACO, tau-bench, CORE-bench and more. The leaderboard is paused for new models but the harness works and its cost accounting is the best of the three.

### mini-swe-agent as a control

Always include [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) as a third arm. It is ~100 lines, bash-only, and scores >74% on SWE-bench Verified with frontier models. If your harness does not beat it on your chosen metric with the same model, your harness is adding cost without adding capability. This is the single most useful sanity check available.

## Private task sets

Public benchmarks are optimised against by everyone, and the harness you care about is the one that works on *your* repos. Build a private set:

1. Take 30 to 50 real issues from your own history that have a reproducible failing test and a known fix.
2. Package each as a Harbor task (Dockerfile, instruction, hidden test script) or a Claw-SWE-Bench-style instance (`base_commit`, `FAIL_TO_PASS`, `PASS_TO_PASS`).
3. Verify: the oracle patch passes, the base commit fails, the hidden tests are not trivially satisfiable (UTBoost's finding is that a quarter of public "verified" tests were).
4. Never commit the task set to a public repo; it leaks into training data within months.

Fifty private tasks with k=5 is 250 trajectories per harness, roughly an afternoon and tens of dollars per harness on a mid-tier model. That is cheap relative to the cost of picking the wrong harness.

## Common traps

- **Comparing across weeks.** Provider-side model updates and rate limits change behaviour. Run arms back-to-back.
- **Letting harnesses pick their own model settings.** Codex and Claude Code silently choose reasoning effort and context strategies. Pin what you can and disclose what you cannot.
- **Uncapped budgets.** With no binding budget every harness converges on similar pass rates and you learn nothing.
- **Reading the pass rate only.** Report cost, latency and fingerprint or do not report.
- **Trusting weak verifiers.** If a task's hidden tests pass on a wrong patch, both harnesses look better and the comparison is noise.
- **Single-model conclusions.** Harness rankings invert between strong and weak models (planning helps weak models, costs strong ones; predefined tools help weak-bash models, bash-only is cheaper for strong ones). Test two.

## Minimal honest claim

"Harness A vs harness B, model M at effort E, on task set T (commit X), k=5, budget B, sandbox S at 3x resources. A: pass 61% [55, 67], 210k tokens/solve. B: pass 58% [52, 64], 1.4M tokens/solve. Paired difference +3 pp [-2, +8]. A's failures are mostly `WRONG_VERIFY`; B's are `IDLE_LOOP`. Trajectories: <link>. Harness Cards: <link>."

That sentence is more information than most leaderboards give you, and it takes one afternoon to produce. Use [`templates/RESULTS.md`](../templates/RESULTS.md).
