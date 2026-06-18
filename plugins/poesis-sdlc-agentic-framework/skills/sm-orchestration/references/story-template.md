# Story Template — `portfolio/<slug>/sprint-N/stories/S-NNN.md`

Authored by `SE: Product Manager` (PO hat) from a `committed` Feature. Trace runs
Story → Feature → Epic (there is no PRD tier). Lives at `portfolio/<slug>/sprint-N/stories/`.

```markdown
---
id: S-101
title: <Story title>
status: backlog          # backlog | ready | in-progress | in-review | in-qa | awaiting-pr | done | blocked
parent_feature: F-12
sprint: N
pi: M
adrs: []                 # ADR ids the Story depends on
driver: ai-team-dev      # assigned at Iteration Planning
navigator: ai-team-dev   # assigned at Iteration Planning
pair_swaps: []           # log of HUDDLE→SWAP cycles
estimate_points: 0
risk: medium             # low | medium | critical; set by PO before leaving backlog
complexity: involved     # simple | involved | complex; set by PO before leaving backlog
owner: SE-Product-Manager
created: YYYY-MM-DD
cost:                    # token cost accounting — see cost-accounting-protocol.md
  tokens_in: 0           # NET-NEW prompt tokens = Σ(inputTokens − cachedTokens) of this Story's dispatches (dev D/N, QA, PO grooming)
  tokens_out: 0          # Σ outputTokens of those dispatches
  tokens_cached: 0       # Σ cachedTokens (re-sent context; not in tokens_self — for billed-cost reconstruction)
  tokens_self: 0         # tokens_in + tokens_out — the Story's net cost (a Story is a leaf)
  tokens_rolled: 0       # == tokens_self for a Story (no children)
  dispatches: 0          # number of subagent dispatches counted into tokens_self (not llm_request turns)
  source: estimated      # measured | estimated | mixed
  committed: null        # YYYY-MM-DD the one-time snapshot was written (terminal status; immutable after)
github:                  # filled by portfolio/_sync (GitHub Projects board sync); null when authoring
  issue_number: null
  issue_node_id: null
  project_item_id: null
---

# S-101 — <title>

## User-facing intent
As a <persona>, I want <thin slice>, so that <benefit>.

## Definition of Ready (DoR)
- [ ] AC complete and testable
- [ ] Dependencies resolved (deps Features `ready`+, ADRs `accepted`)
- [ ] Pair assignable (Driver + Navigator named)
- [ ] Estimate set

## Acceptance criteria (Given/When/Then)
- ...

## Routing classification
- Risk: low | medium | critical — consequence of being wrong.
- Complexity: simple | involved | complex — cognitive/structural difficulty.
- Rationale: why these values are correct for this Story.

## Definition of Done (DoD)
- [ ] Code merged behind Central Supervisor approval (★ PR Gate)
- [ ] Tests pass (unit + integration)
- [ ] Coverage maintained
- [ ] `ai-team-qa` sign-off file exists: `docs/sprint-N/qa/S-101-signoff.md`
- [ ] PO confirms AC met
- [ ] Docs updated where applicable

## Notes / decisions during pair work
(appended by pair during DRIVE/CRITIQUE)
```

## Status lifecycle (Team Kanban columns)

```text
backlog → ready → in-progress → in-review → in-qa → awaiting-pr → done
                                                            ↑ ★ PR Gate
```

Orthogonal flag: `blocked`.

## Transition rules

| From | To | Trigger / actor |
| --- | --- | --- |
| (none) | `backlog` | PO decomposes from committed Feature |
| `backlog` | `ready` | PO confirms DoR satisfied |
| `ready` | `in-progress` | SM dispatches pair (DRIVE starts) |
| `in-progress` | `in-review` | Driver hands to Navigator (CRITIQUE) |
| `in-review` | `in-progress` | REJECT — back to DRIVE (log a swap) |
| `in-review` | `in-qa` | ACCEPT — pair commits, hands to QA |
| `in-qa` | `in-progress` | QA fails — bug report attached |
| `in-qa` | `awaiting-pr` | QA passes + PO confirms AC + PR opened |
| `awaiting-pr` | `done` | **★ PR Gate** Central Supervisor approves, RTE merges |
| any | `blocked` | SM flag (orthogonal) |
