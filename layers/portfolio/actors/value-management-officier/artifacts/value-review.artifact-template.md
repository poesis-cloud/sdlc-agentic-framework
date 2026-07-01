# Value Review Template — `portfolio/<slug>/.../reviews/<subject>-value-review.md`

Authored by `@business-owner`. The business-value verdict on a subject (an Epic, Feature, or budget allocation) — WSJF justification, strategic-theme fit, and lean-budget guardrail adherence. One review per subject per attempt; a `fail` records blocking `open_items`.

```markdown
---
id: <subject>-value-review
subject: <artifact-id-or-path under review>
reviewer: '@business-owner'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# Value Review — <subject>

## Subject under review
Link / id. Restate the value hypothesis, the WSJF inputs, and the strategic-theme fit under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — value justified; strategic-theme fit and guardrails clear.
*(or)* **CONCERNS** — non-blocking concerns recorded as `open_items`.
*(or)* **FAIL** — blocking value/fit defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One review per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-value-review-2.md`.
