# Lean Business Case Template — `portfolio/epics/E-N-lbc.md`

The Epic's **Lean Business Case** (SAFe). Authored in the **Epic Lean Business Case** practice
(`epic-lean-business-case`) — `@business-owner` drafts; `@enterprise-architect`,
`@security-expert` challenge. It is the evidence the Central Supervisor (BO hat)
weighs at the **★ Epic Gate**, and the unit **Participatory Budgeting** funds. Portfolio-scoped;
companion to its Epic `E-N`.

```markdown
---
id: E-1-lbc
epic: E-1
status: draft            # draft | challenged | gate-ready
funding_state: proposed  # proposed | funded | not-funded   (set by Participatory Budgeting)
---

# E-1 — Lean Business Case

## Problem & opportunity
The systemic problem, who has it, why now.

## Solution hypothesis (MVP)
The smallest Feature set that tests the hypothesis (`mvp_features` on the Epic).

## WSJF
| Cost of Delay (UBV + TC + RR) | Job Size | WSJF |
|---|---|---|
| ... | ... | ... |

## Leading & lagging indicators
- Leading: ...
- Lagging: ...

## Cost / effort estimate
Rough order of magnitude; informs Participatory Budgeting.

## Enabler / runway dependency
Architectural-runway items this Epic consumes or requires (→ `architectural-vision`).

## Pivot / persevere / stop criteria
What evidence would change the decision (assessed at Strategic Portfolio Review / Inspect & Adapt).

## Challenge findings
EA / Security adversarial notes, folded in before the ★ Epic Gate.
```
