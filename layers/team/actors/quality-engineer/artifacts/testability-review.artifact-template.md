# Testability Review Template — `portfolio/<slug>/.../reviews/<subject>-testability-review.md`

Authored by `@quality-engineer`. The testability verdict on a subject (a Feature, Story, or enabler) — acceptance-criteria verifiability, test seams, observability, and edge-case coverage. One review per subject per attempt; a `fail` records blocking `open_items`.

```markdown
---
id: <subject>-testability-review
subject: <artifact-id-or-path under review>
reviewer: '@quality-engineer'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# Testability Review — <subject>

## Subject under review
Link / id. Restate the acceptance criteria, the verification approach, and the seams under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — testable as scoped; acceptance criteria verifiable.
*(or)* **CONCERNS** — non-blocking gaps recorded as `open_items`.
*(or)* **FAIL** — blocking testability defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One review per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-testability-review-2.md`.
