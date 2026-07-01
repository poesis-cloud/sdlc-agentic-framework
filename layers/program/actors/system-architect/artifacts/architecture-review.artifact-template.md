# Architecture Review Template — `portfolio/<slug>/.../reviews/<subject>-architecture-review.md`

Authored by `@system-architect` (or `@enterprise-architect` at the portfolio layer). A pure architecture verdict on a subject that does **not** itself produce an ADR (an ADR-producing review records its decision in the ADR / architecture-decision-inventory instead). One review per subject per attempt; a `fail` records blocking `open_items`.

```markdown
---
id: <subject>-architecture-review
subject: <artifact-id-or-path under review>
reviewer: '@system-architect'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# Architecture Review — <subject>

## Subject under review
Link / id. Restate the design, NFR, or runway item under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — design clears the architecture runway.
*(or)* **CONCERNS** — non-blocking issues recorded as `open_items`.
*(or)* **FAIL** — blocking design defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One review per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-architecture-review-2.md`.
