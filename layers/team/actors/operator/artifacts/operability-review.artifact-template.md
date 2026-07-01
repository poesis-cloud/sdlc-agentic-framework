# Operability Review Template — `portfolio/<slug>/.../reviews/<subject>-operability-review.md`

Authored by `@operator`. The operability verdict on a subject (a Feature, runway item, deployment topology, or release) — CI/CD, Helm, environment config, observability, and runtime concerns. One review per subject per attempt; a `fail` records blocking `open_items`.

```markdown
---
id: <subject>-operability-review
subject: <artifact-id-or-path under review>
reviewer: '@operator'
verdict: pass            # pass | concerns | fail
created: YYYY-MM-DD
findings: []
open_items: []
---

# Operability Review — <subject>

## Subject under review
Link / id. Restate the deployment, pipeline, or runtime surface under review.

## Findings
| id | severity | finding | recommendation |
|---|---|---|---|
| F-01 | high | ... | ... |

## Verdict
**PASS** — operationally ready.
*(or)* **CONCERNS** — non-blocking issues recorded as `open_items`.
*(or)* **FAIL** — blocking operability defect; subject returns to its owner.

## Recommendations
Remediation guidance, owner, and target.
```

## Lifecycle
One review per subject per attempt. A `fail` lists blocking `open_items`; the next attempt produces `<subject>-operability-review-2.md`.
