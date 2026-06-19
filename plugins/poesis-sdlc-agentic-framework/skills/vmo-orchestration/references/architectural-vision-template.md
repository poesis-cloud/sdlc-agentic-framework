# Architectural Vision Template — `portfolio/architectural-vision.md` (singleton)

The cross-product **Architectural Vision** (SAFe) — the future-state architecture, the NFR
backbone, and the architectural-runway direction. Authored by `SE: Architect`·EA in the
**Architectural Vision** practice (`safe-architectural-vision`); the portfolio's
intentional-architecture anchor. Feeds Epic runway (`reviewing→analyzing`) and every product's
NFR register + runway register. Portfolio-scoped singleton.

```markdown
---
id: architectural-vision
owner: central-supervisor   # EA hat
revised: YYYY-MM-DD
---

# Architectural Vision

## Future-state architecture
Target architecture across the portfolio's products; key components and boundaries.

## Architectural principles (intentional architecture)
The standing decisions + constraints (security, data, integration, observability, set-based options).

## NFR backbone
Cross-product nonfunctional requirements (→ each product's `nfrs.md`).

## Runway direction & enabler Epics
The runway the portfolio must build ahead of demand; seeds **enabler Epics** (`type: enabler`,
`enabler_type: architectural | infrastructure | compliance`).

## Target ARTs / products
Which products realise which parts of the Vision.
```
