# QA Sign-off Template — `portfolio/<slug>/sprint-N/qa/S-NNN-signoff.md`

Authored by `ai-team-qa` (Ivy). Mandatory artifact for any Story transition `in-qa → awaiting-pr`.

```markdown
---
story: S-101
product: <product-slug>
sprint: N
qa_engineer: ai-team-qa
verdict: pass                 # pass | fail
date: YYYY-MM-DD
test_artifacts:
  - <relative/path/to/test-run-log>
coverage:
  instruction_pct: 0          # JaCoCo or equivalent, where applicable
  line_pct: 0
---

# QA Sign-off — S-101

## Story under test
Link / id. Restate the AC verified.

## DoD verification
- [ ] Code merged to feature branch
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Coverage threshold met (>=95% where applicable)
- [ ] AC verified end-to-end
- [ ] PO confirmation recorded below
- [ ] No security regressions (if security-touching)
- [ ] Accessibility verified (if UI-touching)
- [ ] Docs updated (if applicable)

## PO confirmation
- Confirmed by: `SE: Product Manager` (PO hat)
- Date: YYYY-MM-DD
- Notes: ...

## Verdict
**PASS** — Story is ready for the ★ PR Gate.
*(or)*
**FAIL** — bugs filed below; Story returns to `in-progress`.

## Bugs filed (if FAIL)
| Bug id | Severity | Title | GitHub issue |
|---|---|---|---|
| B-01 | High | ... | #NNN |
```

## Lifecycle

One sign-off per Story per attempt. If FAIL, a new sign-off file `S-NNN-signoff-2.md` (and so on) is created on the next QA pass.
