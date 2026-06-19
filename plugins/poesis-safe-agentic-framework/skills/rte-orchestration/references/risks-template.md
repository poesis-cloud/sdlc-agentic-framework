# PI Risks Template — `portfolio/<slug>/pi-M/risks.md`

RTE-owned register of program-level risks for the PI. Append-only entries.

```markdown
---
pi: M
product: <product-slug>
updated: YYYY-MM-DD
---

# PI-M Risks — <product>

## Risk register (ROAM)

| ID | Description | Impact | Likelihood | Status | Owner | Notes |
|---|---|---|---|---|---|---|
| R-01 | ... | H/M/L | H/M/L | Resolved / Owned / Accepted / Mitigated | <role> | link to mitigation |

## New entries

### R-01 — <short title>
- Detected: YYYY-MM-DD
- Source: <Feature id / sprint / external>
- Description: ...
- Mitigation plan: ...
- ROAM decision: Resolved | Owned | Accepted | Mitigated
- Decided by: Central Supervisor / RTE
- Decision date: YYYY-MM-DD
```

## Lifecycle

Append a new R-NN block whenever a risk is identified. Update the table only when ROAM status changes. Closed at Inspect & Adapt.
