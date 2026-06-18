# Epic Template — `portfolio/epics/E-NN-<slug>.md`

The portfolio-level artifact. Authored by the **Business Owner** hat (you) with the
**Enterprise Architect** hat for the architectural runway, and refined with `SE: Product Manager`
(PM hat) / `SE: Architect` as drafters. An Epic is the **single legitimately cross-product**
artifact: it coordinates Features across one or more products. It is **portfolio-scoped**, so it
lives under `portfolio/`, never under a product slug.

There is **no PRD tier** in this methodology — the Epic carries the intent (problem, outcome
hypothesis, leading indicators) that a PRD used to hold, and it cascades to Features and Stories.

```markdown
---
id: E-01
title: <Epic title — a large outcome spanning products/capabilities>
status: funnel            # funnel | reviewing | analyzing | portfolio-backlog | implementing | done | blocked
type: business           # business | enabler  (enabler = architectural/runway epic)
strategic_theme: <theme-id or name>   # see strategic-themes-template.md
business_owner: central-supervisor    # the BO-hat approver (you)
enterprise_architect: central-supervisor  # the EA-hat owner of the runway (you)
products: []             # product slugs this Epic spans (>=1); cross-product is allowed HERE only
wsjf:
  user_business_value: 0
  time_criticality: 0
  risk_reduction: 0      # risk reduction / opportunity enablement
  job_size: 0
  score: 0               # (UBV + TC + RR) / JS
mvp_features: []         # Feature ids that constitute the MVP (the pivot/persevere test)
risk: medium             # low | medium | critical
complexity: complex      # simple | involved | complex
created: YYYY-MM-DD
approved: null           # set to YYYY-MM-DD on ★ Epic Gate (portfolio-backlog)
cost:                    # token cost accounting — see cost-accounting-protocol.md
  tokens_in: 0           # self: NET-NEW prompt tokens = Σ(inputTokens − cachedTokens) of THIS Epic's overhead dispatches
  tokens_out: 0          # self: Σ outputTokens of those dispatches
  tokens_cached: 0       # self: Σ cachedTokens (re-sent context; not in tokens_self — for billed-cost reconstruction)
  tokens_self: 0         # tokens_in + tokens_out — the Epic's own net cost ("point")
  tokens_rolled: 0       # tokens_self + Σ child Feature.tokens_rolled — Epic end-to-end cost
  dispatches: 0          # number of subagent dispatches counted into tokens_self (not llm_request turns)
  source: estimated      # measured | estimated | mixed
  committed: null        # YYYY-MM-DD the one-time snapshot was written (terminal status; immutable after)
github:                  # filled by portfolio/_sync (Portfolio Project); null when authoring
  issue_number: null
  issue_node_id: null
  project_item_id: null
---

# E-01 — <title>

## Epic hypothesis statement
> For <customers/personas> who <do something / have a need>, the <Epic name> is a
> <class of solution> that <delivers value>. Unlike <current alternative>, our solution
> <key differentiator>. We will know we are right when we observe <leading indicators>.

(This replaces the former PRD problem/outcome sections — it IS the defined intent.)

## Outcome hypothesis & leading indicators
- Leading indicator: ...
- Lagging indicator: ...

## In scope / out of scope
- In: ...
- Out (non-goals): ...

## Business outcomes
Why this Epic matters to the portfolio (value, not solution).

## Enterprise-Architect runway (EA hat)
Cross-product architectural implications, NFR backbone, shared enablers, and which
products must build runway. Enabler Epics live mostly here. May spawn product-level ADRs
(those remain product-scoped, authored by `SE: Architect`).

## Affected products & Feature seeds
| Product | Feature seed (becomes F-NN in that product) | Notes |
|---|---|---|
| <slug> | <one-line Feature intent> | ... |

Each seed becomes a product-scoped Feature (`parent_epic: E-01`). Cross-product work is
expressed as one Feature per product linked to this Epic — never a single cross-product Feature.

## MVP & pivot/persevere
The smallest Feature set (`mvp_features`) that validates the hypothesis. After the MVP,
the Business Owner decides pivot / persevere / stop at ★ Epic Gate review or Inspect & Adapt.

## Dependencies / constraints
Other Epics, external systems, regulations.

## Open questions
Resolved before ★ Epic Gate approval or explicitly deferred.
```

## Status lifecycle (Portfolio Kanban columns)

```text
funnel → reviewing → analyzing → portfolio-backlog → implementing → done
                                        ↑ ★ Epic Gate (Business-Owner approval)
```

Orthogonal flag: `blocked`.

## Transition rules

| From | To | Trigger / actor |
| --- | --- | --- |
| (none) | `funnel` | BO/EA captures a raw Epic idea |
| `funnel` | `reviewing` | RTE + PM give it an Epic hypothesis + rough WSJF |
| `reviewing` | `analyzing` | EA drafts the runway; products + Feature seeds identified |
| `analyzing` | `portfolio-backlog` | **★ Epic Gate** Business Owner approves the Epic hypothesis |
| `analyzing` | `funnel` | BO defers/declines (re-shape) |
| `portfolio-backlog` | `implementing` | First child Feature enters its product Program Kanban (`funnel`) |
| `implementing` | `done` | All child Features `done` + BO accepts the outcome (at System Demo / I&A) |
| any | `blocked` | RTE flag (orthogonal) |

## Identity / linkage

- An Epic's id `E-NN` is portfolio-unique (not per product).
- A Feature points up via `parent_epic: E-NN` (optional — a Feature may exist without an Epic).
- The Epic lists its products in `products[]`; child Features remain product-scoped.
