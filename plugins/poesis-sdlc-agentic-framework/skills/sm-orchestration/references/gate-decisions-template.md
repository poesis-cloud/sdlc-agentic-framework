# Gate Decision Backlog Template — `portfolio/<slug>/sprint-N/gate-decisions.md`

Append-only ledger authored by RTE/SM. Captures assumptions or decisions taken by agents that may require Central Supervisor disposition at a gate.

```markdown
---
product: <product-slug>
sprint: N
updated: YYYY-MM-DD
---

# Sprint N Gate Decision Backlog — <product>

## Open decisions
| ID | Story/Feature | Source artifact | Decision needed | Options | Recommended | Owner | Status |
|---|---|---|---|---|---|---|---|
| GD-001 | S-100 | PR #123 | Accept PR scope variance | accept / rework / defer | accept | Central Supervisor | open |

## Resolved decisions
| ID | Resolved at gate | Disposition | Notes |
|---|---|---|---|
| GD-000 | ★ ADR Gate | accept | Covered by ADR-004 approval |

## Usage rules
- Add a row as soon as an agent takes a decision that could require Central Supervisor confirmation.
- Do not delete rows; move resolved rows to the resolved table.
- Every gate packet must list unresolved entries from this file.
- If disposition is `rework`, open the re-iteration path immediately and link the resulting artifact/PR.
```
