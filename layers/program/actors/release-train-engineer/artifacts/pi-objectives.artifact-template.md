# PI Objectives Template — `portfolio/<slug>/pi-M/pi-objectives.md`

Authored by RTE at PI Planning. One file per product per PI.

```markdown
---
pi: M
product: <product-slug>
start_date: YYYY-MM-DD
end_date: YYYY-MM-DD
capacity_points: 0
committed_features: []          # ids of Features flipped ready → committed
stretch_features: []            # optional, not counted in capacity
---

# PI-M Objectives — <product>

## PI theme
One sentence framing what this PI delivers.

## Committed Features (with business value 1–10, set by Central Supervisor)

| Feature | Title | Planned BV | Actual BV (filled at I&A) |
|---|---|---|---|
| F-12 | ... | 8 | — |

## Stretch Features
| Feature | Title | Planned BV |
|---|---|---|
| F-15 | ... | 5 |

## Cross-product dependencies
List Features in other products that this PI depends on (`<other-slug>/F-N`).

## Milestones
- M+0 weeks: ...
- M+N weeks (IP): Inspect & Adapt
```

## Lifecycle

Created at PI Planning; updated at each Iteration boundary; closed at Inspect & Adapt with actual BV filled in.
