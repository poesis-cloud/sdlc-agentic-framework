# Architectural Runway Register Template — `portfolio/<slug>/runway.md`

The product's **Architectural Runway** register (SAFe) — the enabler work that builds technical
foundation ahead of business Features. Seeded by the **Architectural Vision** and extended by the
**Architectural Runway Extension** practice (`architectural-runway-extension`). Each runway
item is an **enabler** (`type: enabler`) flowing through the normal Feature FSM + gates; this
register tracks readiness so PI Planning can budget enabler capacity. Product-scoped.

```markdown
---
product: <slug>
revised: YYYY-MM-DD
---

# <Product> — Architectural Runway

| Runway item | Enabler | enabler_type | Consumed by (Features) | Readiness |
|---|---|---|---|---|
| <capability> | F-NN (`type: enabler`) | architectural | F-AA, F-BB | building |

enabler_type: exploration · architectural · infrastructure · compliance.
Readiness: building · ready · depleting.

## Runway health
- Ready ahead of demand: ...
- Gaps (seed enabler Features → `architectural-runway-extension`): ...
- Depleting (needs extension): ...
```
