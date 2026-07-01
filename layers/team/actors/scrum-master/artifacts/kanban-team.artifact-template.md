# Team Kanban (rendered) — `portfolio/<slug>/kanban/team-sprint-N.md`

**Rendered view.** Never hand-edit. SM regenerates from Story frontmatter across `portfolio/<slug>/sprint-N/stories/*.md` after every status flip.

```markdown
---
product: <product-slug>
sprint: N
rendered_at: YYYY-MM-DDTHH:MM:SSZ
source: portfolio/<slug>/sprint-N/stories/
---

# Team Kanban — <product> — Sprint N

| backlog | ready | in-progress | in-review | in-qa | awaiting-pr | done |
|---|---|---|---|---|---|---|
| S-110 ... | S-105 (dev/dev) | S-103 (dev/SE-Sec) | S-102 (dev/dev) | S-101 | S-100 → PR #NNN | S-99 ✓ [23.7k tk] |

## Blocked (orthogonal)
| Story | Reason | Owner |
|---|---|---|
| S-104 | waiting on ADR-3 | RTE |

## WIP limits
- `in-progress`: 1 per pair (current: K / max P)
- `in-qa`: 2 (current: K)

## Gate watch
- **★ PR Gate pending** (Stories awaiting PR approval): S-100 (PR #NNN)

## Cost (tokens, self)
| Story | tokens_self | source |
|---|---|---|
| S-101 | 23.7k | measured |
```

## Render rule

For each Story file in `portfolio/<slug>/sprint-N/stories/`, place its id in the column matching its `status:`. Annotate with `(driver/navigator)` for `in-progress`/`in-review`, with PR link for `awaiting-pr`, and with its `cost.tokens_self` (e.g. `S-99 [23.7k tk]`). Render the Cost section from each Story's `cost:` block (see [story-cost-snapshot invariant instructions](../../../workflow/workflows/verification/instructions/story-cost-snapshot-measured-once-from-logs.instructions.md)). Sort within a column by `id` ascending. Refresh the `rendered_at` timestamp. Do not invent content not present in frontmatter.
