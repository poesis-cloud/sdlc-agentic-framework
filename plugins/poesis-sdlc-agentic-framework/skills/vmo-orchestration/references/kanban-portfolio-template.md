# Portfolio Kanban (rendered) — `portfolio/kanban/portfolio.md`

**Rendered view.** Never hand-edit. RTE regenerates from Epic frontmatter across
`portfolio/epics/*.md` after every Epic status flip. This is the portfolio-level
analogue of the per-product Program Kanban.

```markdown
---
scope: portfolio
rendered_at: YYYY-MM-DDTHH:MM:SSZ
source: portfolio/epics/
---

# Poesis Portfolio Kanban

| funnel | reviewing | analyzing | portfolio-backlog | implementing | done |
|---|---|---|---|---|---|
| E-05 ... | E-04 | E-03 → Epic Gate | E-02 (WSJF 9) | E-01 (3/5 Features done) | E-00 ✓ Epic Gate [134.1k tk] |

## Blocked (orthogonal)
| Epic | Reason | Owner |
|---|---|---|
| E-06 | waiting on enterprise-architecture spike | RTE |

## WIP limits
- `analyzing`: <portfolio capacity> (current: K)
- `implementing`: 3 (current: K)

## Gate watch
- **★ Epic Gate pending** (Epics awaiting Business-Owner approval): E-03

## Strategic-theme rollup
| Theme | Epics in flight |
|---|---|
| ST-1 | E-02, E-03 |

## Cost rollup (tokens)
| Epic | tokens_rolled | source |
|---|---|---|
| E-00 | 134.1k | mixed |
| E-01 | 88.0k | estimated |

| Theme | tokens_rolled (Σ Epics) |
|---|---|
| ST-1 | 222.1k |
```

## Render rule

For each Epic file in `portfolio/epics/`, place its id in the column matching its
`status:`. Annotate each with its `cost.tokens_rolled` (e.g. `E-00 [134.1k tk]`) and render the Cost
rollup section (per Epic and per Strategic Theme) from each Epic's `cost:` block (see
[cost-accounting-protocol.md](./cost-accounting-protocol.md)). Sort within a column by `wsjf.score`
descending. Refresh the `rendered_at` timestamp. Do not invent content not present in frontmatter.
