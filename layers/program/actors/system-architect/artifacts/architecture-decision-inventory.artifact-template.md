# Architecture Decision Inventory Template — `portfolio/<slug>/architecture/decision-inventory-F-N-<slug>.md`

Per-Feature architecture reference artifact for any `structurant: true` Feature.

```markdown
---
product: <product-slug>
feature: F-12
feature_title: <Feature title>
status: in-progress          # in-progress | gate-ready | accepted |
                             # superseded
revised: YYYY-MM-DD
linked_adrs: []              # ADR ids currently referenced by this inventory
linked_enablers: []          # enabler Feature ids seeded from this inventory
---

# Architecture Decision Inventory — F-12

## Gate summary

- Coverage status: incomplete | gate-ready
- Why not yet gate-ready: <short reason, or `n/a`>
- Architecture Gate target: current pass | next pass | staged

## Decision units

<!-- markdownlint-disable MD013 -->
| Decision unit | Status | Coverage | ADRs | Enabler follow-up | Notes |
| --- | --- | --- | --- | --- | --- |
| <Decision unit> | open | missing | — | F-21 | <what is still unresolved> |
| <Decision unit> | proposed | partial | ADR-1 | — | <what remains before accept> |
| <Decision unit> | decided | covered | ADR-2 | F-22 | <accepted and any downstream work> |
| <Decision unit> | waived | covered | — | — | <why the gate accepts no ADR here> |
<!-- markdownlint-restore MD013 -->

Status: open | proposed | decided | waived.
Coverage: missing | partial | covered.

## Gate notes

- Open questions for the next architecture pass or for the ★ Architecture Gate.
- Explicit waivers or deferrals that the gate must see.
```

The inventory is the gate-facing index of decision units for one structurant
Feature. Every required decision unit must appear here, each linked ADR must
govern exactly one unit, and open rows block the ★ Architecture Gate unless
they are explicitly waived.
