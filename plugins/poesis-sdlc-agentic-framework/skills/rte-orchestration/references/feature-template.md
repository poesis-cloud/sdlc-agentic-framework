# Feature Template — `portfolio/<slug>/features/F-NN-<slug>.md`

Authored by `SE: Product Manager` (PM hat). A Feature optionally rolls up to a portfolio **Epic**
(`parent_epic: E-NN`); there is **no PRD tier** — the defining intent lives in the Epic (or, for
standalone engineering/operability Features, in the Feature itself). Lives at
`portfolio/<slug>/features/`.

```markdown
---
id: F-12
title: <Feature title>
status: funnel           # funnel | refined | arch-pending | ready | committed | in-progress | done | blocked
type: business           # business | enabler
enabler_type: null       # exploration | architectural | infrastructure | compliance (when type=enabler)
parent_epic: E-01        # portfolio Epic id, or null for a standalone Feature
epic_rationale: "<why this Feature serves the Epic, or 'standalone: <reason>'>"
wsjf:
  user_business_value: 0
  time_criticality: 0
  risk_reduction: 0
  job_size: 0
  score: 0               # (UBV + TC + RR) / JS
structurant: false       # true ⇒ requires an ADR ⇒ arch-pending
risk: medium             # low | medium | critical; set by PM before leaving funnel
complexity: involved     # simple | involved | complex; set by PM before leaving funnel
adrs: []                 # ADR ids referenced; empty if structurant=false
pi: M                    # set on transition to `committed`
owner: SE-Product-Manager
created: YYYY-MM-DD
cost:                    # token cost accounting — see cost-accounting-protocol.md
  tokens_in: 0           # self: NET-NEW prompt tokens = Σ(inputTokens − cachedTokens) of THIS Feature's overhead dispatches
  tokens_out: 0          # self: Σ outputTokens of those dispatches
  tokens_cached: 0       # self: Σ cachedTokens (re-sent context; not in tokens_self — for billed-cost reconstruction)
  tokens_self: 0         # tokens_in + tokens_out — the Feature's own net cost ("point")
  tokens_rolled: 0       # tokens_self + Σ child Story.tokens_rolled — Feature end-to-end cost
  dispatches: 0          # number of subagent dispatches counted into tokens_self (not llm_request turns)
  source: estimated      # measured | estimated | mixed
  committed: null        # YYYY-MM-DD the one-time snapshot was written (terminal status; immutable after)
github:                  # filled by portfolio/_sync (GitHub Projects board sync); null when authoring
  issue_number: null
  issue_node_id: null
  project_item_id: null
---

# F-12 — <title>

## Description
What is this Feature, in one paragraph.

## Acceptance criteria
- Given/When/Then or measurable bullets.
- If `parent_epic` is set, must trace to the Epic's hypothesis / in-scope items.

## Benefit hypothesis
Why this Feature delivers value (a slice of the parent Epic's outcome hypothesis, or the
Feature's own rationale when standalone).

## NFRs (Feature-level)
Performance, security, accessibility, observability — or explicit "N/A".

## Routing classification
- Risk: low | medium | critical — consequence of being wrong.
- Complexity: simple | involved | complex — cognitive/structural difficulty.
- Rationale: why these values are correct for this Feature.

## Dependencies
Other Features, ADRs, external systems. Cross-product coordination is expressed via the shared
parent Epic (one Feature per product), never a single cross-product Feature.

## Story breakdown (filled in step 6 by PO)
- S-101 …
- S-102 …
```

## Status lifecycle (Program Kanban columns)

```text
funnel → refined → arch-pending → ready → committed → in-progress → done
                 ↑ ★ Feature Gate  ↑ ★ Architecture Gate              ↑ ★ Demo Gate
                        (skip arch-pending if structurant=false)
```

Orthogonal flag: `blocked`.

## Transition rules

| From | To | Trigger / actor |
| --- | --- | --- |
| (none) | `funnel` | PM derives from an Epic (`parent_epic`) or files a standalone Feature |
| `funnel` | `refined` | Feature Backlog Refinement (PM completes AC + WSJF + `structurant`) |
| `refined` | `arch-pending` | **★ Feature Gate** accept + `structurant: true` |
| `refined` | `ready` | **★ Feature Gate** accept + `structurant: false` |
| `refined` | `funnel` | **★ Feature Gate** reject (re-refine) |
| `arch-pending` | `ready` | **★ Architecture Gate** ADR `accepted` |
| `arch-pending` | `refined` | ADR `rejected` (PM revises) |
| `ready` | `committed` | RTE at PI Planning |
| `committed` | `in-progress` | First child Story passes the **★ Story Gate** → enters Team Kanban `ready` |
| `in-progress` | `done` | **★ Demo Gate** Central Supervisor accepts at System Demo |
| any | `blocked` | SM/RTE flag (orthogonal) |
