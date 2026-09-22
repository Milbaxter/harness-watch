# Harness comparison: <A> vs <B>

One-paragraph claim first, then the tables. If the paired CI includes zero, the claim says so.

## Claim

<A> vs <B>, model <M> at effort <E>, on <task set> (commit <X>), k=<k>, budget <B>, sandbox <S> at <N>x resources.
A: pass <p>% [<lo>, <hi>], <t> tokens/solve, $<c>/solve.
B: pass <p>% [<lo>, <hi>], <t> tokens/solve, $<c>/solve.
Paired difference (A - B): <d> pp [<lo>, <hi>].
Dominant failure modes: A <tag>, B <tag>.
Trajectories: <url>. Harness Cards: <url A>, <url B>.

## Setup

| | A | B |
|---|---|---|
| Harness Card | link | link |
| Model, effort | | |
| Runner + version | | |
| Task set + commit | | |
| k | | |
| Budget (turns / tokens / wall-clock) | | |
| Sandbox resources | | |
| Run dates | | |
| Command | | |

## Accuracy

| Metric | A | B | A - B (95% CI, paired bootstrap over tasks) |
|---|---|---|---|
| Pass@1 (mean over k) | | | |
| Pass@k | | | |
| Pass@1 at 50% budget | | | |
| Pass@1 at 25% budget | | | |
| Tasks solved by A only / B only / both / neither | | | |

## Efficiency

| Metric | A | B |
|---|---|---|
| Tokens per solved task (median, p90) | | |
| Input / output / cached tokens per task | | |
| $ per solved task at <rate card, date> | | |
| Wall-clock per solved task (median, p90) | | |
| Turns per task (median) | | |
| No-op / idle turns per task | | |

## Failure fingerprint

Counts over all failed trials.

| Tag | A | B |
|---|---|---|
| MAX_TURNS | | |
| IDLE_LOOP | | |
| WRONG_VERIFY | | |
| BAD_EDIT | | |
| CONTEXT_OVERFLOW | | |
| REASONING | | |
| INFRA | | |
| TIMEOUT | | |
| REFUSAL | | |

Two or three representative failed trajectories per dominant tag, with one sentence each on what went wrong.

## Control arm (recommended)

Same table for a deliberately minimal harness on the same model: mini-swe-agent, pi with its default four tools, DeepSeek Harness `sdk-minimal`, or the benchmark's neutral reference agent. If neither A nor B beats it on the primary metric, say so.

## Evolved-harness controls (required if A or B was evolved or benchmark-tuned)

| | Development split | Held-out split |
|---|---|---|
| Evolved harness | | **headline number goes here** |
| Seed harness, single shot | | |
| Seed harness, matched inference budget (best-of-n / retries at task time, same total tokens as the evolution campaign) | | |

State the campaign cost (iterations, candidates, total tokens) and link the Provenance section of the Harness Card. If the evolved harness does not beat the matched-budget seed on the held-out split, the honest claim is "found a benchmark-specific configuration", not "better harness".

## Second model (recommended)

Repeat the accuracy and efficiency tables with a second model of different strength. Note any ranking inversions.

## Threats to validity

- Provider drift between arms (dates above)
- Settings the harness would not expose
- Verifier weakness on specific tasks
- Anything else you noticed
