# Architectural Runway Register Template — `portfolio/<slug>/architecture/runway.md`

The product's **Architectural Runway** register (SAFe) — the runway capabilities, references, and
enabler work that build technical foundation ahead of business Features. Seeded by the
**Architectural Vision** and extended by the **Architectural Runway Extension** practice
(`architectural-runway-extension`). Each runway item may have:

- an **architecture reference** from the standard artifact set (ADR, architecture decision
  inventory, NFR register, or other owned template-backed artifact) that defines or constrains the
  runway item, and
- one or more **enabler Features** (`type: enabler`) that realize that runway item through the
  normal Feature FSM + gates.

This register tracks both the reference artifact and the backlog realization so PI Planning can
budget enabler capacity without confusing architecture documentation with enabler backlog units. It
is architecture-scoped and belongs under the product's `architecture/` folder, not beside the
backlog folders.

```markdown
---
product: <slug>
revised: YYYY-MM-DD
---

# <Product> — Architectural Runway

| Runway item | Architecture reference | Realized by enabler Features | enabler_type | Consumed by (Features) | Readiness |
|---|---|---|---|---|---|
| <capability> | ADR-N; `decision-inventory-F-N-*.md`; `nfrs.md` | F-N (`type: enabler`) | architectural | F-AA, F-BB | building |

enabler_type: exploration · architectural · infrastructure · compliance.
Readiness: building · ready · depleting.

## Runway health
- Ready ahead of demand: ...
- Gaps (seed enabler Features → `architectural-runway-extension`): ...
- Depleting (needs extension): ...
```
