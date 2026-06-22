# NFR Register Template — `portfolio/<slug>/nfrs.md`

The product **Nonfunctional Requirements** register (SAFe NFRs / quality attributes). Seeded from
the **Architectural Vision** NFR backbone (`architectural-vision`), maintained by
`SE: Architect` + `SE: Security`. NFRs are **constraints** on Features / Stories, **verified** at
Verification & Sign-off and the System Demo. Compliance NFRs may spawn **enabler** work.

```markdown
---
product: <slug>
revised: YYYY-MM-DD
---

# <Product> — NFR Register

| NFR | Category | Constraint (measurable) | Applies to | Verified by | Enabler? |
|---|---|---|---|---|---|
| NFR-01 | security | all endpoints authn/z; secrets in vault | all | Verification + Security | — |
| NFR-02 | performance | p95 < 200ms | F-NN | QA perf check | — |
| NFR-03 | compliance | GDPR data-retention | product | compliance enabler | E-NN / F-NN |

Categories: security · performance · reliability · scalability · usability · maintainability ·
observability · compliance.
```
