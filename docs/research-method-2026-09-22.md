# Hotspot research: method and discovery log

Checked 2026-09-22. Scope: public places where builders change agent loops, tool interfaces, context, memory, skills, orchestration, or evaluation/optimization machinery.

## Discovery routes

Representative literal queries used during this search:

| Route | Queries / entry points |
|---|---|
| Existing project | GitHub `user:milbaxter harness`; read harness-watch README, landscape, monitoring, sources, and file tree. |
| Runtime/plugin breadth | `open source agent harness ecosystem tinkering pi opencode hermes September 2026`; `agent harness pi extensions oh my pi opencode oh my opencode GitHub`; `agent harness self improvement hermes openclaw nanoclaw GitHub` |
| Orchestration/workflow | `coding agents orchestration gastown beads ralph loop superpowers get shit done GitHub`; official READMEs and linked successor repositories. |
| Automated improvement | `agent harness optimization auto harness evolutionary DSPy GEPA GitHub`; `"agent harness" "Meta-Harness"`; `"Meta-Harness" "github" "2603.28052"`; `"agent harness" "autoresearch" github` |
| Composable infrastructure | `"harness" "deepagents" "community"`; `"agent harness" "Prime Intellect"` |
| Individual builders | `"pi" "extensions" "mitsuhiko"`; `"pi" "extensions" "autoresearch" github` |
| Regional/ecosystem breadth | `DeepSeek harness dsh github plugins official`; official DeepSeek English/Chinese project pages, dsh-plugin topic and community directory leads. |
| Package-level invention | Pi package catalog sorted by recent; followed source links for pi2dsh, SpecPi, and pi-tool-duration. |
| Broader discussion venues | `harness engineering community meetup discord builders`; found public event pages and official project chat invites. Did not use event listings to rank development activity. |
| Disambiguation | `"harness" "Muse" github agent` returned multiple different meanings; excluded a firm Muse classification rather than conflate them. |

Search engines returned duplicate forks, third-party mirrors, SEO pages, and irrelevant results. Those were discovery leads only. Primary GitHub endpoints, official READMEs, papers, and package pages were used for the substantive map. One batch of date-filtered web queries produced largely irrelevant matches and did not support any conclusion.

## Verification

1. GitHub REST `GET /repos/{owner}/{repo}` for canonical name, default branch, archive flag, license metadata, push time, and public counts.
2. Follow repository moves through the GitHub connector's repository lookup; record old and canonical names separately.
3. Read selected first-party READMEs for actual extension surfaces, limitations, community entry points, and release/migration status.
4. Sample `GET /repos/{owner}/{repo}/pulls?state=all&sort=updated&direction=desc&per_page=8` for ten priority repositories.
5. Read six individual PR bodies to distinguish actual proposals from vague activity signals. Link and label them in the report.
6. Preserve the normalized evidence in `data/hotspots-2026-09-22.json` so the map can be revised without relying on this conversation.

The snapshot contains **52 successful repository metadata checks**, three recorded redirects, and one unresolved `vercel-labs/ai-sdk` metadata lookup. That unresolved lookup is not scored or treated as a negative finding. A later DSH PR-list fetch did not yield parseable content; it is not included in the 80-PR sample.

## What the ranking means

Qualitative priorities combine: relevance to editable harness behavior; concrete implementation artifacts; recent public development; and usefulness as a place to inspect or try an idea. Stars and forks are contextual fields only. No numerical score is presented because these data do not support a reliable quantitative ranking.

The 80 PRs are a bounded convenience sample, not all work from a fixed time window. They contain routine maintenance, automated releases, and occasional irrelevant submissions. They are not a contributor census or evidence that high PR volume equals innovation. Six cited design threads provide more specific evidence; five were still open at observation.

## Boundaries

- Public-source research only: no access to private Discord/Slack channels, no inference of their membership or message rates.
- README feature descriptions are author claims, not independent performance validation.
- Repository push time can reflect any branch; it is not equivalent to a release date or a substantive default-branch change.
- GitHub license metadata can be absent or `NOASSERTION`; do not infer permissive licensing from public source visibility. OmO's license text was read directly and flagged as source-available.
- Historical paper claims and benchmark numbers already in harness-watch were not comprehensively re-audited.
- No geography ranking: software ecosystems are observable here, geographic concentrations of inventors were not established.
- No recurring automation, notifications, subscriptions, third-party installations, or outreach were created.

## Useful next searches

These are proposed saved searches, not claimed completed measurements. Adjust dates for the next scan:

```text
topic:pi-package pushed:>2026-09-15
topic:dsh-plugin pushed:>2026-09-15
"agent harness" in:description,readme pushed:>2026-09-15
repo:PrimeIntellect-ai/prime-agent is:pr updated:>2026-09-15
repo:can1357/oh-my-pi is:pr cache
repo:langchain-ai/deepagents is:pr harness
repo:gepa-ai/gepa is:pr reflection
```

For reproducible comparisons, start from this repository's benchmarking protocol, but reserve a final untouched test set and separate model updates from harness changes.
