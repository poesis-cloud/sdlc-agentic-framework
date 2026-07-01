# Enabler Epic Template — `portfolio/epics/E-N-<slug>.md`

Portfolio-scoped backlog contract for **enabler Epics**. Use this template when `type: enabler`.
An enabler Epic is a first-class portfolio backlog unit, not an architecture note: it exists to
fund and govern runway work that enables downstream product Features and program execution.

```markdown
---
id: E-1
title: <Enabler Epic title>
status: funnel            # funnel | reviewing | analyzing | portfolio-backlog | implementing | done | blocked
type: enabler
enabler_type: architectural   # architectural | infrastructure | compliance
strategic_theme: <theme-id or name>
business_owner: central-supervisor
enterprise_architect: central-supervisor
products: []
work_item_relations:
  depends_on: []         # hard prerequisite Epics that must land before this enabler is actionable
  enables: []            # downstream Epic/Feature ids this enabler unblocks
  related_to: []         # non-gating semantic or strategic adjacency
  supersedes: []         # Epic ids intentionally replaced by this enabler Epic
wsjf:
  user_business_value: 0
  time_criticality: 0
  risk_reduction: 0
  job_size: 0
  score: 0
mvp_features: []
risk: medium
complexity: complex
created: YYYY-MM-DD
approved: null
open_items: []           # clarification + challenge ledger — see orchestrator "Open-item ledger".
                         # Each entry: { id, kind, raised_by, owner, blocking, status, … }; kind: clarification | challenge.
                         # status: open | resolved | withdrawn. A blocking+open entry HALTS the ★ Epic Gate.
cost:
  tokens_in: 0
  tokens_out: 0
  tokens_cached: 0
  tokens_self: 0
  tokens_rolled: 0
  dispatches: 0
  source: estimated
  committed: null
github:
  issue_number: null
  issue_node_id: null
  project_item_id: null
---

# E-1 — <title>

## Enablement statement
### Syntax
Use exactly one hypothesis block in this canonical form:
> To enable <products / ARTs / capabilities> to <deliver or operate something>, the <Epic name>
> provides <architectural runway / infrastructure / compliance foundation>. We will know we are
> ready when <dependent Features / ART capabilities> can proceed with reduced risk or removed
> constraints, evidenced by <leading indicators>.

## Runway outcome & leading indicators
### Syntax
- `Leading indicator: <early measurable signal>`
- `Lagging indicator: <later outcome signal>`
- Add more bullets only when each is materially distinct.

- Leading indicator: ...
- Lagging indicator: ...

## In scope / out of scope
- In: ...
- Out (non-goals): ...

## Enablement rationale
Why this runway investment matters now, and what delivery or operability risk it removes.

## Enabler properties
- Consuming products / Features: ...
- Unblocked capabilities / constraints removed: ...
- Validation evidence expected before closure: ...

### Syntax
- `Consuming products / Features: <product slug and/or work-item ids>`
- `Unblocked capabilities / constraints removed: <single sentence>`
- `Validation evidence expected before closure: <test, report, review, or artifact>`

## Enterprise-Architect runway (EA hat)
Cross-product architectural implications, NFR backbone, shared enablers, and which
products must build runway.

## Affected products & Feature seeds
### Syntax
Use one row per product seed in this form:

| Product | Feature seed (becomes F-N in that product) | Notes |
|---|---|---|
| <slug> | <one-line enabler Feature intent> | ... |

## MVP & pivot/persevere
The smallest enabler Feature set (`mvp_features`) that makes the blocked delivery path viable.

### Syntax
- `MVP feature set: <Feature id list or named seed list>`
- `Ready when: <evidence that the blocker is removed>`
- `Rework when: <evidence that the runway is still insufficient>`

## Dependencies / constraints
Other Epics, external systems, regulations.

## Work-item relations

Use only relation types that materially shape sequencing or runway intent.

- `depends_on` — hard prerequisite relation. Use when this enabler Epic cannot remove its target
  constraint before another Epic produces a prerequisite decision or capability.
- `enables` — primary relation for enabler Epics. Use to name the downstream Epics or Features whose
  path becomes viable because this enabler lands.
- `related_to` — non-gating adjacency. Use for shared runway area or conceptual coupling that should
  remain visible but must not drive scheduling.
- `supersedes` — replacement relation. Use when this enabler Epic intentionally retires or absorbs an
  earlier runway Epic.

Best-practice rules:

- Prefer `enables` over vague prose when the value of the enabler is specifically to unblock named
  downstream work.
- Use `depends_on` sparingly; enablers should remove blockers, not accumulate them without cause.
- Do not encode architecture references (ADR ids, runway files, NFR registers) as work-item links;
  keep this contract limited to backlog units.

## Open items
The human-readable companion to the `open_items:` frontmatter ledger (the [open-item
ledger](../../value-management-officier/value-management-officier.skill.md#open-item-ledger)) — this enabler Epic's **clarifications**
(proactive unknowns surfaced by the CE Discovery turn) and **challenges** (reactive findings from
peer review), formalized identically and routed to the owning hat. Every **blocking** item must be
resolved before the ★ Epic Gate; non-blocking items are resolved or explicitly deferred with a
recorded default. The ledger is kept after resolution as an audit + agent-memory trail.

### Syntax
One bullet per item, mirroring a frontmatter entry:
- `I<n> [clarification|challenge] [blocking|non-blocking] (raised_by: <hat>, owner: <EA|Security|DevOps|human>): <question or finding>` — default if unanswered: `<assumption>`; status: `open|resolved|withdrawn`.

- I1 [clarification] [non-blocking] (raised_by: <hat>, owner: ...): ... — default if unanswered: ...; status: open
```
