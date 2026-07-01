# UX Review Template — `portfolio/<slug>/.../reviews/<subject>-ux-review.md`

Authored by `@ux-designer`. The UX/accessibility verdict on a subject (a Feature, Story, or user-facing flow) — user journeys, interaction affordances, and WCAG 2.1 AA accessibility. One review per subject per attempt; a `fail` records blocking `open_items`.

```markdown
---
id: <subject>-ux-review
subject: <artifact-id-or-path under review>
reviewer: '@ux-designer'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# UX Review — <subject>

## Subject under review
Link / id. Restate the user journey, screen, or interaction under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — UX and accessibility clear.
*(or)* **CONCERNS** — non-blocking issues recorded as `open_items`.
*(or)* **FAIL** — blocking UX/accessibility defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One review per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-ux-review-2.md`.
