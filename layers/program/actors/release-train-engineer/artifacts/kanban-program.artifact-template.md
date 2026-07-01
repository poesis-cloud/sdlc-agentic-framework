# Program Kanban (rendered) — `portfolio/<slug>/kanban/program.md`

**Rendered view.** Never hand-edit. RTE regenerates from Feature frontmatter across `portfolio/<slug>/features/*.md` after every status flip.

```markdown
---
product: <product-slug>
rendered_at: YYYY-MM-DDTHH:MM:SSZ
source: portfolio/<slug>/features/
---

# Program Kanban — <product>

| funnel | refined | arch-pending | ready | committed | in-progress | done |
|---|---|---|---|---|---|---|
| F-20 ... | F-12 (WSJF 8) | F-15 → ADR-3 | F-11 | F-10 (PI-M) | F-9 (3/5 stories done) | F-8 ✓ Demo Gate [72.7k tk] |

## Blocked (orthogonal)
| Feature | Reason | Owner |
|---|---|---|
| F-13 | waiting on `sie-definition` F-4 | RTE |

## WIP limits
- `committed`: <PI capacity> (current: K)
- `in-progress`: 3 (current: K)

## Gate watch
- **★ Architecture Gate pending** (ADRs awaiting Central Supervisor): ADR-3 for F-15
- **★ Demo Gate pending** (Features awaiting demo): F-9

## Cost rollup (tokens)
| Feature | tokens_rolled | source |
|---|---|---|
| F-8 | 72.7k | mixed |
| F-9 | 41.2k | estimated |
```

## Render rule

For each Feature file in `portfolio/<slug>/features/`, place its id in the column matching its `status:`. Annotate each with its `cost.tokens_rolled` (e.g. `F-8 [72.7k tk]`) and render the Cost rollup section (top Features by `tokens_rolled`) from each Feature's `cost:` block (see [feature-cost-snapshot invariant instructions](../../../workflow/workflows/system-demo/instructions/feature-cost-snapshot-measured-once-from-logs.instructions.md)). Sort within a column by `wsjf.score` descending. Refresh the `rendered_at` timestamp. Do not invent content not present in frontmatter.
