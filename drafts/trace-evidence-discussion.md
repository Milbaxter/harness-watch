# Draft: what evidence should survive context compression for agent evolution?

Status: **prepared for review; not posted**. Suggested venue: an existing relevant [GEPA Discussion](https://github.com/gepa-ai/gepa/discussions), or a new discussion only after checking for duplicates and available categories. This is an evaluation suggestion, not a bug report. It is not intended for pi's issue tracker.

## Draft message

I'm mapping open-source harness experiments in [harness-watch](https://github.com/Milbaxter/harness-watch), with a particular interest in what agents need to retain in order to learn from failed attempts.

Two projects seem worth comparing:

- [GEPA #390](https://github.com/gepa-ai/gepa/issues/390) exposed incomplete reflection outputs entering the candidate pool. The merged [#462](https://github.com/gepa-ai/gepa/pull/462) uses termination evidence to reject known-incomplete proposals while preserving compatible parsing behavior.
- [SoL-Pi](https://github.com/NVlabs/SoL-Pi) reduces repeated observations and long logs while keeping archived source material available.

These address different stages—proposal generation versus the evidence supplied to an agent. My question is whether a compact trace can preserve the information an optimizer needs to diagnose a failure, especially when the decisive clue was omitted from the visible summary.

A small initial comparison could use public, frozen failure cases: full trace, compact receipt with source retrieval, and receipt alone. Score the diagnosis and cited evidence against a human-checked answer; count retrieval and summarization costs too. That would test a prerequisite for harness evolution, not establish an end-to-end evolution gain.

Does an existing adapter or evaluation already test this? In particular, are there cases showing which command outcomes, timestamps, truncation signals or source references must survive compression? A pointer to a failure example or relevant experiment would help avoid duplicating work.

I haven't run this comparison. This note was prepared with AI assistance from linked public sources.

## Before sharing

- Recheck #462 and the current SoL-Pi documentation; this draft was researched on September 22, 2026.
- Search existing GEPA discussions for trace compression, evidence retrieval and observation packing; adapt to the community's local rules.
- Edit into the author's own voice and retain the disclosure and statement that no experiment has been run.
- Share once in the relevant venue. Connect another community only when there is useful evidence or a response to carry over.

Background: [field report](../reports/2026-09-22-community-field-notes.md). Proposed follow-up: [trace-evidence pilot](../experiments/trace-evidence-pilot.md).
