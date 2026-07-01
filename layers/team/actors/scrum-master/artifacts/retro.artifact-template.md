# Sprint Retro Template — `portfolio/<slug>/sprint-N/retro.md`

Authored by SM at the end of every iteration.

```markdown
---
sprint: N
product: <product-slug>
date: YYYY-MM-DD
facilitator: SM (RTE-self)
attendees:
  - central-supervisor
  - SE-Product-Manager
  - @developer
  - @quality-engineer
---

# Sprint N Retro — <product>

## 1. What worked
- ...

## 2. What didn't
- ...

## 2b. Workflow pain points (sprint-scope capture)
Iteration-scope workflow friction captured this sprint (append-only, `status: open`; no inline fix). Resolve iteration-local items now; feed program/ART-scope items up to the PI's Inspect & Adapt ledger (`pi-M/inspect-adapt.md` §3b). These are *inputs* to triage, not solutions.
| Pain point | Symptom | Candidate target (skill/agent/instruction/prompt/template) | Disposition |
|---|---|---|---|
| PP-YYYYMMDD-NN | ... | ... | resolve now / feed-up to I&A / wont-fix |

## 3. Root causes (5 Whys for the top 2 items)
- Issue 1 → why → why → why → why → why → root cause
- Issue 2 → ...

## 4. Action items
| Action | Owner | Due |
|---|---|---|
| ... | SM / RTE / @specialist | Sprint N+1 |

## 5. Metrics snapshot
| Metric | Value |
|---|---|
| Stories committed | |
| Stories done | |
| Stories carried over | |
| Avg story cycle time (days) | |
| Bugs found post-QA | |

## 6. Feed-up to I&A
Items to surface at the PI-level Inspect & Adapt. Include any program/ART-scope pain points from §2b not resolvable within the iteration.
```

## Lifecycle

One file per sprint. Action items flow to next sprint's plan; systemic items flow to `pi-M/inspect-adapt.md`.
