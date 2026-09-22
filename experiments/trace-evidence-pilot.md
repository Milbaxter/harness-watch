# Future experiment: does compact evidence preserve failure diagnosis?

Status: **proposal only; not implemented, funded or run**. Current discovery-phase experiment spending is zero. This is a next-step candidate for the October 6 review, not an instruction to begin paid work.

## Hypothesis and relationship to the projects

A compact receipt with bounded access to the original trace may reduce total context use while preserving the ability to identify why an agent failed. The question connects [SoL-Pi's evidence-preserving mechanisms](https://github.com/NVlabs/SoL-Pi) with [GEPA's trace-driven optimization](https://github.com/gepa-ai/gepa).

The pilot tests failure diagnosis, a prerequisite for proposing useful improvements. It does not test recursive intelligence growth or establish that the two projects already interoperate. A compact-receipt prototype must be labeled as inspired by SoL-Pi, not benchmarked as SoL-Pi itself.

## Baseline, cases and comparison

- Assemble 20 small public or deliberately constructed failure cases across terminal debugging, multi-step information retrieval and skill/tool selection. Record provenance; use only material that can be redistributed, and label constructed cases.
- Keep the source trace, task question and human-checked root cause for each case. Pin all artifacts. Split ten development / ten holdout cases by source problem so variants of one incident cannot cross the split. Keep answer labels out of model-visible traces and receipt generation.
- Compare three conditions: **full trace** (baseline), **compact receipt plus source retrieval**, and **receipt only** (diagnostic ablation). Freeze the receipt format after development. Preserve source IDs, tool outcomes, event order and termination metadata; summarize content without using the answer labels.
- Use one fixed model/version with the same settings and task instructions in all conditions. Choose and price the available model before any paid execution; model selection is deliberately deferred to that later decision. Record an exact model ID, not a floating alias.
- Run three trials per case and condition: 180 diagnosis attempts total, 90 on the holdout. Expose one initial response plus at most one continuation to every condition. Source retrieval is available only in the receipt-plus-retrieval arm, with at most two archive excerpts totaling 4,000 input tokens; include these within the attempt's total budget. Give the other arms the same continuation opportunity without archive tools.
- Cap each diagnosis attempt at 8,000 total input tokens across calls and 1,000 total output tokens. Exclude oversized cases before freezing the split; record exclusions. Record budget exhaustion as failure, not missing data. Generate at most one receipt per case, capped at 8,000 input / 1,000 output tokens, then reuse it across the two receipt conditions and trials.

## Measures and acceptance

Score a diagnosis as correct only if it identifies the reference cause and cites supporting source evidence. A human reviews blinded outputs; no extra paid judge is required. Report paired outcomes, unsupported citations, retrieval failures, input/output tokens, wall time and all preparation costs. Keep failures in the denominator.

Report two cost views: total campaign cost including receipt creation, and per-attempt serving cost with the reuse assumption explicit. A first-use comparison charges the full receipt-generation cost to that case.

The pilot can justify a larger test if receipt-plus-retrieval reduces median total tokens by at least 20%, has at least as many correct holdout diagnoses as the baseline, and has no unsupported source citations. These are screening criteria, not proof of equivalence: ten held-out cases are too few to establish a small non-regression margin. Publish paired counts by case and mark an uncertain result inconclusive. Never tune on the holdout; a second iteration needs fresh holdout cases.

Checks before running: deterministic fixture/source lookup, hidden-label separation, missing-source handling, token/cost cap accounting across continuation calls, and complete accounting of failed attempts. If a receipt drops the only decisive clue, retrieval should recover it; the receipt-only arm exposes that failure mode.

## Estimated cost and stop condition

Maximum planned token envelope: 180 attempts × (8,000 input + 1,000 output), plus 20 receipts × the same limits = **1.6 million input and 0.2 million output tokens**. All continuation calls count inside those limits; do not double the envelope silently.

For budgeting illustration only, at assumed rates of €2 per million input tokens and €10 per million output tokens, that is **€5.20** before taxes or currency effects. These are arithmetic assumptions, not verified prices for any provider. Propose a **€10 hard campaign cap**, with no automatic top-up; stop before a call whose maximum charge would exceed the remaining cap. If actual selected-model pricing makes the envelope exceed €10, revise the design before running it.

Estimated human preparation/review: 3–5 hours; hosting: local files, no new service. Preparation in the current scouting phase costs €0 in experiment API calls. Actual model availability, pricing and funding must be resolved if this proposal is selected later.

## Publishable outcome

A case manifest, pinned receipt builder, baseline and candidate settings, all outputs and failure records, paired results and cost accounting. A negative or inconclusive result is useful. Only after this prerequisite is supported should a separate experiment ask whether compressed evidence improves GEPA's search or transfers to Hermes.

Use the existing [Harness Card](../templates/HARNESS_CARD.md) and [results template](../templates/RESULTS.md) for any later run. No results file should contain invented scores.
