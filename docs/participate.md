# Start here: watch, understand, contribute

For an AI-assisted experimenter, scout and connector interested in broad agent capability. Start with two weeks of discovery, **22 September–6 October 2026**, using existing access. There is no experiment spending in this phase.

The initial research is ready: read the [field report](../reports/2026-09-22-community-field-notes.md), then the [contribution draft](../drafts/trace-evidence-discussion.md). A [future experiment proposal](../experiments/trace-evidence-pilot.md) is prepared but has not been run.

## Your five places

This is an interest-based shortlist, not a claim that these are objectively the five best harnesses. Prefer visible experiments, useful review and reusable evidence over stars or message volume.

| Priority | Community and entry points | What to follow | First useful role |
|---|---|---|---|
| 1 | [Hermes self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution), [Nous Discord](https://discord.gg/NousResearch) | Learning skills from experience; the boundary between the shipped skill pipeline and proposed broader evolution | Map which claims have working evidence; help clarify evaluation gaps |
| 2 | [GEPA](https://github.com/gepa-ai/gepa), [Discussions](https://github.com/gepa-ai/gepa/discussions), [Discord](https://discord.gg/WXFSeVGdbW), [DSPy](https://github.com/stanfordnlp/dspy) | Trace-driven improvement across tasks, candidate selection, feedback quality | Bring comparable examples and investigate why apparently better candidates fail |
| 3 | [pi](https://github.com/earendil-works/pi), [SoL-Pi PRs](https://github.com/NVlabs/SoL-Pi/pulls), [pi RFCs](https://rfc.earendil.com/keyword/pi/) | Tool and context mechanisms; cost versus task success; experiments becoming extensions | Follow a small change through reproduction and review |
| 4 | [DeepSeek Harness Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions), [Discord](https://discord.gg/Ycq5dCaS4) | Ideas and Show Your Plugins: memory, tool composition and agent-loop changes | Translate and connect promising Chinese/English work to other communities |
| 5 | [Meta-Harness](https://github.com/stanford-iris-lab/meta-harness#community-projects) | Harness-code search and independent applications in its Community Projects list | Trace one adaptation to a new domain and identify transferable evaluation lessons |

**Two communities to return to initially: GEPA and Nous.** SoL-Pi is the secondary reading track. Reassess on 6 October using the criteria below.

Official invitations are verified from project documentation; membership and private channel activity have not been inspected. Joining is a personal-account step still to do. No GitHub subscriptions, follows, Discord memberships or posts were created by this notebook.

## Participation norms worth knowing

- **GEPA:** [contribution guide](https://github.com/gepa-ai/gepa/blob/main/CONTRIBUTING.md) requires tests, formatting checks and type checks for code changes. Begin with an existing discussion or a focused question; search for duplicates first.
- **Hermes:** its [runtime contribution guide](https://github.com/NousResearch/hermes-agent/blob/main/CONTRIBUTING.md) prioritizes fixes and asks contributors to search both code and existing PRs. Review an existing proposal when it already addresses the idea. This runtime guide is context, not proof that the separate self-evolution repository has identical rules.
- **pi:** [its guide](https://github.com/earendil-works/pi/blob/main/CONTRIBUTING.md) says new contributors' issues and PRs are auto-closed for maintainer triage, and a maintainer's `lgtm` is required before submitting a PR. It also asks for issues in your own voice, with AI use clearly identified if applicable. Start by reading and discussing; a standalone extension may be more appropriate than a core change.
- **SoL-Pi:** [its guide](https://github.com/NVlabs/SoL-Pi/blob/main/CONTRIBUTING.md) welcomes tested extensions using pi's public APIs and offers help benchmarking contributions. Include correctness and trade-offs alongside efficiency measurements. No turnaround or free compute allocation is promised.
- **DeepSeek Harness:** read the pinned welcome and plugin guidelines in [Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions). Keep translated quotations linked to their originals and label your interpretation.
- **Meta-Harness:** the [README](https://github.com/stanford-iris-lab/meta-harness) invites links to independent applications, while qualifying the reference release's testing. A documented reproduction or domain adaptation is a suitable eventual contribution.

## Two-week checklist

Each week uses three 15-minute visits and a 45-minute synthesis. These are manual sessions, not scheduled reminders.

| Date | Time | Action | Concrete output |
|---|---|---|---|
| Sep 22 | 15 min | Join GEPA and Nous through the official links; inspect their local rules and relevant channels | Two entry points and channel bookmarks; leave membership pending if login is unavailable |
| Sep 24 | 15 min | Read GEPA #390 → #435/#460 → #462/#465 | One understood report-to-merge history |
| Sep 26 | 15 min | Read Hermes #162, especially corrections and later author responses | Separate proposed capability, reported testing and adoption status |
| Sep 28 | 45 min | Read SoL-Pi #27; compare the three histories with the field report | Five notable developments, three questions and one cross-community connection |
| Sep 29 | 15 min | Skim DSH Ideas/Show Your Plugins and one Meta-Harness community application | One candidate worth following, or a recorded reason to pass |
| Oct 1 | 15 min | Follow up on the five people in the report by reading their relevant work | Keep or replace each person based on substantive evidence |
| Oct 3 | 15 min | Recheck thread status and search GEPA/Nous for the draft's topic | Update the draft; avoid a duplicate discussion |
| Oct 6 | 45 min | Select two communities and review the contribution and experiment proposals | A ready-to-share note and a go/no-go recommendation for a later experiment |

For each community record **yes / unclear / no**, with a link, for: published failures, interpretable measurements, accessible artifacts, substantive review, and a feasible newcomer contribution. Keep the two with the strongest evidence and best fit; do not infer openness from stars or number of comments. For now GEPA and Nous are provisional choices, not outcomes from two weeks of participation.

## Reusable scouting note

Copy this into a new dated report for each promising thread:

```text
Observed date and source URL:
Idea / hypothesis:
What changed, and on which commit:
Evidence (author report / independent report / personally reproduced):
Status (proposed / merged / released / independently reproduced):
Limitation or counterexample:
Next unanswered question:
People involved and their role (author / contributor / maintainer / bot):
Connection to another project's result:
Smallest useful contribution:
```

Subscribe to individual research threads if useful; avoid all-activity notifications on large runtimes. Use AI to translate, summarize and compare, then check the original evidence before attributing a claim. A closed PR is not necessarily merged, a merged PR is not necessarily released, and a reviewer is not necessarily a maintainer.

## Completion record

- [x] Ranked five-community entry map with official links and participation norms.
- [x] Prepared three sourced histories, five developments, three questions and five people to follow.
- [x] Prepared one contribution draft and one costed future experiment proposal.
- [ ] Personally join the two communities and assess private discussion quality.
- [ ] Complete the follow-up visits and choose the two ongoing communities on Oct 6.
- [ ] Review and choose whether to share the draft. It has not been posted.
- [ ] Decide separately whether to fund and run the future experiment.

The unchecked items require later participation or a separate execution decision. The initial notebook does not claim they have happened.
