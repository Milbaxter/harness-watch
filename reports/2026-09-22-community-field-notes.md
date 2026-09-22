# Field notes: where to participate in harness evolution

Observed 22 September 2026. Purpose: find a productive entry point for an AI-assisted experimenter and scout interested in broad agent capability. Start with the [participation guide](../docs/participate.md).

Method: read public project documentation, GitHub issue reports, PR metadata, reviews and follow-up comments. The [status snapshot](2026-09-22-community-evidence.json) records seven PRs and their commit IDs. No external experiment was reproduced here, and no private chat contents were inspected. Numbers below belong to the named reporters, not to harness-watch. Rankings are editorial judgments.

## Five developments that matter

| Development | Evidence and status | Why it matters to a newcomer |
|---|---|---|
| GEPA's incomplete-candidate failure produced a merged compatibility-aware fix | [#390](https://github.com/gepa-ai/gepa/issues/390) → [#462](https://github.com/gepa-ai/gepa/pull/462), merged Sep 21; [#465](https://github.com/gepa-ai/gepa/pull/465) credits the superseded contributors | A careful reproduction can improve the shared search machinery without inventing a new harness |
| Hermes has substantial proposed expansion beyond skill evolution | [#162](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162), open and unmerged at head `dee3c8833aaaaf2eec2f1d2c5a788f7082d7b115` | There is visible design/review work to learn from; proposal scope and passing tests do not establish broad intelligence gains |
| SoL-Pi connects auto-research to maintained extensions and contributor benchmarking | [Research account](https://nvlabs.github.io/SoL-Pi/), [contribution policy](https://github.com/NVlabs/SoL-Pi/blob/main/CONTRIBUTING.md), live [reducer PR #27](https://github.com/NVlabs/SoL-Pi/pull/27) | Follow both the search method and the small corrective changes needed after an idea ships |
| DSH has an active exchange for plugins and unresolved memory/context questions | [Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions): September 22 posts include plugins, memory proposals and compaction failures | A useful scouting route into Chinese and English implementations; forum activity alone does not validate their benefits |
| Meta-Harness's community applications go beyond terminal tasks | [Community Projects](https://github.com/stanford-iris-lab/meta-harness#community-projects) links legal, disease-related and long-video applications | Follow the linked experimenters for broader domains. A README listing is discovery evidence, not independent validation of the applications |

## History 1 — GEPA: when a promising candidate is malformed

**Idea.** Reflection on execution traces should produce better instructions. But the output must first be a usable candidate.

**Evidence.** [Lee-byeonggwan's report](https://github.com/gepa-ai/gepa/issues/390) describes a Qwen3-8B reproduction on 30 AIME problems with five runs: baseline 24.0%, optimized test score 31.33%. The reporter found that 13 of 23 candidates were incomplete reasoning text. Those are reported results under that setup, not a universal GEPA effect.

**Revision and adoption.** [overgoy's #435](https://github.com/gepa-ai/gepa/pull/435) and [sethkimmel3's #460](https://github.com/gepa-ai/gepa/pull/460) were closed without merging. [LakshyAAAgrawal's #462](https://github.com/gepa-ai/gepa/pull/462) superseded them and merged Sep 21. Its policy uses positive truncation evidence while preserving valid legacy unfenced output. The author reports 726 passing tests and five skipped tests, including mutation checks. [#465](https://github.com/gepa-ai/gepa/pull/465) subsequently merged a credit commit for the earlier contributors. Release inclusion was not checked.

**Limitation.** A custom model returning plain strings may omit the metadata needed to identify truncation. A parser fix also does not demonstrate a new task-performance gain.

**Next question.** Which failure and termination metadata must survive trace transformations so later optimization can distinguish a bad idea from an incomplete response?

**People.** Lee-byeonggwan supplied the reproduction; overgoy and sethkimmel3 proposed fixes; LakshyAAAgrawal authored the merged replacement. This is a concrete route from experiment to shared improvement.

## History 2 — Hermes: proposed capability meets evaluation and review

**Idea.** Extend the self-evolution pipeline to tool descriptions, prompt sections, code and a continuous improvement loop. The [main README](https://github.com/NousResearch/hermes-agent-self-evolution) still identifies only skill evolution as implemented; [#162](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162) proposes the wider system.

**Evidence and revision.** On Aug 15, independent contributor enzo-adami reported a passing isolated suite, then [corrected that conclusion](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5303937493) after finding statistical and serialization gaps. The author [responded with fixes and counterexamples](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5304452354), explaining why an unestimable bootstrap interval need not erase other statistical evidence.

Later, contributor kvnloo [identified a subprocess isolation gap](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5460676153). The author added an enforced boundary; the reviewer then [confirmed the original protections and found a virtualenv portability failure](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5465993915). The author's [latest relevant response](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5483891013) reports three new regressions and 1,724 passing tests in fork CI at `dee3c88`.

**Adoption and limitation.** The PR is still open. Historical review findings above were subsequently addressed according to author responses; do not repeat them as confirmed current bugs. Fork-CI claims and reviewer probes are useful evidence, but this notebook did not rerun them or establish an end-to-end capability improvement. Even the separate compatibility PR [#142](https://github.com/NousResearch/hermes-agent-self-evolution/pull/142) is closed without merging; its reported lifts are not evidence that main contains its fixes.

**Next question.** Is there a public, current-head, end-to-end run showing better task outcomes on an untouched holdout, with all failed candidates and total search costs included?

**People.** MaxFreedomPollard is the proposal author; enzo-adami and kvnloo supplied independent contributor feedback. Their reviews are not treated as maintainer acceptance.

## History 3 — SoL-Pi: auto-research findings still need iterative engineering

**Idea.** Reduce wasted work while preserving capability. NVIDIA's [research account](https://nvlabs.github.io/SoL-Pi/) reports 152 proposed directions, four surviving mechanisms and a 51-task final held-out suite. This is the authors' account, not an independent reproduction. The [release](https://github.com/NVlabs/SoL-Pi) exposes opt-in mechanisms, including observation packing and evidence-preserving log reduction.

**Failure and revision.** [PR #27](https://github.com/NVlabs/SoL-Pi/pull/27) reports that an optional regex group let non-diagnostic Cargo commands enter the reducer. The proposed repair grew into bounded shell-token parsing. A contributor [showed that empty quoted arguments still fooled it](https://github.com/NVlabs/SoL-Pi/pull/27#issuecomment-5691507124). The author [responded with token-presence handling and tests](https://github.com/NVlabs/SoL-Pi/pull/27#issuecomment-5692878220), reporting 144 passing tests at that revision.

**Adoption and limitation.** The PR remains open. The test counts and reproductions are contributor reports; no new cost or capability measurement was established here. A [maintenance-team clarification](https://github.com/NVlabs/SoL-Pi/pull/27#issuecomment-5730645509) explicitly distinguishes independent contributor reviews from team decisions. Do not infer merge authority from a confident review.

**Next question.** After eligibility and evidence handling change, does the extension still save resources while preserving task outcomes and useful diagnostic evidence?

**People.** kaluli123123 authored the fix; gaoanze888 supplied independent feedback; Owen718 posted the maintenance clarification.

## Three questions worth bringing to the communities

1. **Evidence retention:** when tool outputs become receipts or handles, what must an optimizer receive to preserve its ability to diagnose failures? GEPA's truncation episode and SoL-Pi's archived observations make this a concrete cross-project question. No integration or improvement is claimed.
2. **Skill discovery:** can an individually improved skill become harder to select among competing skills? Hermes [issue #186](https://github.com/NousResearch/hermes-agent-self-evolution/issues/186) raises this evaluation gap. Review current code and follow-up discussion before proposing work.
3. **Transfer and search cost:** how much of an apparent evolution gain survives different task families, fresh trials and a matched-budget baseline? The [Meta-Harness community applications](https://github.com/stanford-iris-lab/meta-harness#community-projects) provide candidates to inspect, not an answer by themselves.

The first is the proposed contribution: a small cross-community evidence-retention comparison. A [discussion draft](../drafts/trace-evidence-discussion.md) and [pilot design](../experiments/trace-evidence-pilot.md) are ready for review.

## Five people to follow through their work

These choices reflect observed contributions, not a claim about overall reputation or responsiveness. GitHub following has not been enabled.

| Person | Evidence to start with | What to learn |
|---|---|---|
| [Lee-byeonggwan](https://github.com/Lee-byeonggwan) | [GEPA #390](https://github.com/gepa-ai/gepa/issues/390) | Reporting an unexpected failure inside a reproduction, including setup differences |
| [overgoy](https://github.com/overgoy) | [Design question before a fix](https://github.com/gepa-ai/gepa/issues/390#issuecomment-5302569992), then [#435](https://github.com/gepa-ai/gepa/pull/435) | Asking about the behavioral contract before contributing an AI-assisted change |
| [Lakshya Agrawal](https://github.com/LakshyAAAgrawal) | [GEPA #462](https://github.com/gepa-ai/gepa/pull/462), [credit #465](https://github.com/gepa-ai/gepa/pull/465) | Combining contributions while retaining compatibility and credit |
| [MaxFreedomPollard](https://github.com/MaxFreedomPollard) | [Hermes #162](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162) | Responding to review with changed implementations and bounded evidence |
| [enzo-adami](https://github.com/enzo-adami) | [Correction after an earlier approval](https://github.com/NousResearch/hermes-agent-self-evolution/pull/162#issuecomment-5303937493) | Revising conclusions when passing tests miss an important property |

## What this changes in harness-watch

Add GEPA, DSPy and the dedicated Hermes evolution project to the watchlist. Keep the wider ecosystem map, but use individual experiment histories for participation. Start with GEPA and Nous; use pi/SoL-Pi, DSH and Meta-Harness to discover ideas to compare. Two weeks of actual community participation and the future experiment remain pending.
