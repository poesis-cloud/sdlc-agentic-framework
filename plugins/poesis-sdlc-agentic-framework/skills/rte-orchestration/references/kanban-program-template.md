# Program Kanban (rendered) — `portfolio/<slug>/kanban/program.md`

**Rendered view.** Never hand-edit. RTE regenerates from Feature frontmatter across `portfolio/<slug>/features/*.md` after every status flip.

```markdown
---
product: <product-slug>
rendered_at: YYYY-MM-DDTHH:MM:SSZ
source: portfolio/<slug>/features/
---

# Program Kanban — <product>

| funnel | refined | adr-pending | ready | committed | in-progress | done |
|---|---|---|---|---|---|---|
| F-20 ... | F-12 (WSJF 8) | F-15 → ADR-003 | F-11 | F-10 (PI-M) | F-09 (3/5 stories done) | F-08 ✓ Feature Gate [72.7k tk] |

## Blocked (orthogonal)
| Feature | Reason | Owner |
|---|---|---|
| F-13 | waiting on `sie-definition` F-04 | RTE |

## WIP limits
- `committed`: <PI capacity> (current: K)
- `in-progress`: 3 (current: K)

## Gate watch
- **★ ADR Gate pending** (ADRs awaiting Central Supervisor): ADR-003 for F-15
- **★ Feature Gate pending** (Features awaiting demo): F-09

## Cost rollup (tokens)
| Feature | tokens_rolled | source |
|---|---|---|
| F-08 | 72.7k | mixed |
| F-09 | 41.2k | estimated |
```

## Render rule

For each Feature file in `portfolio/<slug>/features/`, place its id in the column matching its `status:`. Annotate each with its `cost.tokens_rolled` (e.g. `F-08 [72.7k tk]`) and render the Cost rollup section (top Features by `tokens_rolled`) from each Feature's `cost:` block (see [cost-accounting-protocol.md](./cost-accounting-protocol.md)). Sort within a column by `wsjf.score` descending. Refresh the `rendered_at` timestamp. Do not invent content not present in frontmatter.
