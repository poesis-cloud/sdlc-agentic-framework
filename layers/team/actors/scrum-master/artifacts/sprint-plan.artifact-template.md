# Sprint Plan Template

## Plan File

Save as `docs/sprint-N/plan.md`:

```markdown
# Sprint N — [Name]

> Sprint Goal: [one sentence describing the deliverable]
> PI: M | Branch: feature/sprint-N
> Estimated effort: [time estimate]

## Prioritized Story List

| # | Story | Feature | ADRs | Driver | Navigator | Est | Description |
|---|-------|---------|------|--------|-----------|-----|-------------|
| S-1 | [story] | F-N | [adr ids] | default-dev | default-dev | 1h | [what to build] |
| S-2 | [story] | F-N | [adr ids] | default-dev | @security-expert | 2h | [trust-boundary work] |
| S-3 | [story] | F-N | [adr ids] | @ux-designer | default-dev | 1h | [UX-driven work] |

Pair convention: first-named = initial Driver, second-named = initial Navigator.
Roles swap each pair-programming micro-cycle (see the scrum-master skill § Pair Programming).

## Work Schedule

### Phase 1: [Name] (S-1 .. S-3)
- Dispatch pairs sequentially
- Checkpoint commit after phase

### Phase 2: [Name] (S-4 .. S-6)
- Dispatch pairs sequentially
- Checkpoint commit after phase

### Phase 3: Acceptance & Polish
- RTE runs acceptance against every Story DoD (QA duty)
- File blockers as GitHub Issues
- Open PR for the ★ PR Gate only when no blockers remain

## Success Criteria

- [ ] Every Story meets its DoD
- [ ] Every commit carries pair attribution + Copilot trailer
- [ ] All dependent ADRs are `accepted`
- [ ] CI green
- [ ] `docs/qa/sprint-N-signoff.md` written

## What's NOT in This Sprint

| Story / Feature | Reason |
|-----------------|--------|
| [deferred item] | [why — scope, ADR pending, dependency] |

## RTE Dispatch Prompt

> @release-train-engineer — Read PROJECT_BRIEF.md and docs/sprint-N/plan.md. Execute Sprint N.
>
> First: git pull origin main && git checkout -b feature/sprint-N
>
> For each Story, dispatch the named Driver/Navigator pair as subagents.
> Pairs run the pair-programming micro-cycle and commit on feature/sprint-N.
> Close GitHub Issues in commits: "fix: description (Fixes #NN)".
> Update docs/sprint-N/progress.md after each Story.
> When all Stories pass acceptance, push and open a PR.
> Wait for the ★ PR Gate (human approval) before merging.
> Follow Sections 12-14 of PROJECT_BRIEF.md.
```

## Progress Tracker

Create `docs/sprint-N/progress.md` at sprint start:

```markdown
# Sprint N — Progress Tracker

> If context overflows, start a new chat:
> "@release-train-engineer — recover state."

## Story Status

| # | Story | Driver | Navigator | Status | Notes |
|---|-------|--------|-----------|--------|-------|
| S-1 | [story] | default-dev | default-dev | ⬜ Not started | |
| S-2 | [story] | default-dev | @security-expert | 🔨 In progress | |
| S-3 | [story] | @ux-designer | default-dev | ✅ Accepted | |
| S-4 | [story] | default-dev | default-dev | ❌ Blocked | [reason] |

## Bugs Found

| # | Story | Description | Severity | Status | Fix |
|---|-------|-------------|----------|--------|-----|
| #NN | S-2 | [bug] | blocker/major/minor | open/fixed | [commit or PR] |

## Notes

[Free-form notes about decisions, ADR amendments needed, context for recovery]
```

## Done File

Write `docs/sprint-N/done.md` at sprint end:

```markdown
# Sprint N — Done

## What Was Built
- S-1 — [Story] (pair: default-dev / default-dev)
- S-2 — [Story] (pair: default-dev / @security-expert)

## What's NOT Done
- [Deferred Story — why]

## Files Changed/Created
- `src/components/NewComponent.tsx` — [purpose]
- `api/src/functions/newEndpoint.ts` — [purpose]

## Manual Setup Required
- [Any env vars, config, or manual steps needed]

## Known Issues
- [Issue — tracked as GitHub Issue #NN]

## ADRs Referenced
- ADR-N — [title] (status: accepted)
```

## QA Sign-off Template

Save as `docs/qa/sprint-N-signoff.md`:

```markdown
# QA Sprint N Sign-Off

Date: [date]
Facilitator: @release-train-engineer (QA-acceptance duty folded into RTE)

## Stories Accepted

| Story | DoD met? | Notes |
|-------|----------|-------|
| S-1 | ✅ | |
| S-2 | ✅ | |
| S-3 | ❌ | blocker #NN open |

## Test Results
- Tests run: X
- Tests passed: X
- Tests failed: 0

## Blockers
NONE   (or: list of GitHub Issues with severity:blocker)

## Issues Filed
- #NN — [description] (severity: minor)

## Result
✅ PASS — No blockers. Sprint N ready to open PR for the ★ PR Gate.
   (or: ❌ HOLD — blockers must clear before the ★ PR Gate)
```
