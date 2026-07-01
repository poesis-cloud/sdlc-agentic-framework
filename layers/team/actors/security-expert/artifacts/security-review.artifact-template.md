# Security Review Template — `portfolio/<slug>/.../reviews/<subject>-security-review.md`

Authored by `@security-expert`. The security verdict on a subject (a Story, Feature, ADR, runway item, or PR). One review per subject per attempt; a `fail` records blocking `open_items` the owning step must clear.

```markdown
---
id: <subject>-security-review
subject: <artifact-id-or-path under review>
reviewer: '@security-expert'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# Security Review — <subject>

## Subject under review
Link / id. Restate the trust boundary, surface, or change under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — no blocking security concerns.
*(or)* **CONCERNS** — non-blocking issues recorded as `open_items`.
*(or)* **FAIL** — blocking security defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One sign-off per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-security-review-2.md`.
