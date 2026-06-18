# ADR Template — `portfolio/<slug>/architecture/adr-NNN-<slug>.md`

Authored by `SE: Architect` for any Feature flagged `structurant: true`.

```markdown
---
id: ADR-001
title: <short decision title>
status: proposed              # proposed | accepted | rejected | superseded
product: <product-slug>
parent_feature: F-12
deciders:
  - central-supervisor                  # ★ ADR Gate decider
  - SE-Architect
consulted:
  - SE-Security
  - SE-DevOps-CI
created: YYYY-MM-DD
decided: null                 # set on ★ ADR Gate accept/reject
supersedes: null              # ADR id, if applicable
superseded_by: null
---

# ADR-001 — <title>

## Context
Forces at play. What is structurant about the parent Feature.

## Decision
The decision, stated in one paragraph in active voice.

## Options considered
1. **<Option A>** — pros / cons.
2. **<Option B>** — pros / cons.
3. **<Option C — chosen>** — pros / cons.

## Consequences
- Positive: ...
- Negative: ...
- Follow-up Features or ADRs to file.

## Implementation hooks
Repos and code areas impacted (must intersect parent product's `repos[]`).
```

## Status lifecycle

`proposed → ★ ADR Gate → accepted | rejected`. `accepted` may later flip to `superseded` by a newer ADR.

ADR Gate transition: parent Feature flips `adr-pending → ready` on `accepted`, or back to `refined` on `rejected`.
