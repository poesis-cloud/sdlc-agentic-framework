# Inspect & Adapt Template — `portfolio/<slug>/pi-M/inspect-adapt.md`

Authored by RTE at the end of the PI, after the System Demo (★ Feature Gate cycle).

```markdown
---
pi: M
product: <product-slug>
date: YYYY-MM-DD
attendees:
  - central-supervisor
  - RTE
  - SE-Product-Manager
  - ai-team-dev
  - ai-team-qa
---

# PI-M Inspect & Adapt — <product>

## 1. PI System Demo summary
- Features demoed (with link to ★ Feature Gate outcome).
- Central Supervisor acceptance per Feature: accepted | conditionally accepted | rejected.

## 2. Quantitative metrics
| Metric | Planned | Actual | Delta |
|---|---|---|---|
| Features committed → done | | | |
| Stories committed → done | | | |
| Predictability (actual/planned BV %) | | | |
| ★ PR Gate cycle time (avg days) | | | |
| ★ ADR Gate cycle time (avg days) | | | |
| Defect escape rate (post-QA bugs) | | | |

## 3. Retrospective (problem-solving)
Top 3 systemic issues surfaced in sprint retros; root-cause analysis; actions.

## 3b. Workflow pain points (input from the ledger)
Open PI-scope entries pulled from `portfolio/_improvement-log.md`, plus items fed up from sprint retros (§6). These are *inputs* to triage in §4 — raw friction, not solutions.
| Pain point | Origin | Symptom | Root cause |
|---|---|---|---|
| PP-YYYYMMDD-NN | <product>/<sprint\|pi> | ... | ... |

## 4. Improvement backlog items
Triage each §3/§3b item into exactly one target:

**Workflow improvements** (resolve a pain point) — a change to a **skill / agent / instruction / prompt / orchestrator template**. Recorded by filling the pain point's output block in `portfolio/_improvement-log.md` and implementing the change; the entry is marked `resolved`. **Not** product Features.
| Pain point | Improvement (meta-artifact change) | Target file | Owner | Status |
|---|---|---|---|---|
| PP-... | ... | `.github/skills|agents|instructions|prompts/...` | RTE | open |

**Product improvements** — new Features filed against this product (or other products) to address delivery-level root causes.

| Action | Owner | Target PI |
|---|---|---|
| ... | ... | M+1 |

## 5. PI+1 priming
- Carry-over Features (committed but not done).
- Top 3 candidates for the next PI funnel.
```

## Lifecycle

Closes the PI. After approval by Central Supervisor, the PI folder is archival; new work goes into `pi-(M+1)/`.
