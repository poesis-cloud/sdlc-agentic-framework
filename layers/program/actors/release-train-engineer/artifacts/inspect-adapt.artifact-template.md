# Inspect & Adapt Template — `portfolio/<slug>/pi-M/inspect-adapt.md`

Authored by RTE. This artifact is also the **living per-PI workflow-improvement ledger**: §3b is appended **continuously** through the PI (the moment workflow friction is observed), and §1–§2, §4–§5 are finalized at the Inspect & Adapt event after the System Demo (★ Demo Gate cycle).

```markdown
---
pi: M
product: <product-slug>
date: YYYY-MM-DD
attendees:
  - central-supervisor
  - RTE
  - SE-Product-Manager
  - @developer
  - @quality-engineer
---

# PI-M Inspect & Adapt — <product>

## 1. PI System Demo summary
- Features demoed (with link to ★ Demo Gate outcome).
- Central Supervisor acceptance per Feature: accepted | conditionally accepted | rejected.

## 2. Quantitative metrics
| Metric | Planned | Actual | Delta |
|---|---|---|---|
| Features committed → done | | | |
| Stories committed → done | | | |
| Predictability (actual/planned BV %) | | | |
| ★ PR Gate cycle time (avg days) | | | |
| ★ Architecture Gate cycle time (avg days) | | | |
| Defect escape rate (post-QA bugs) | | | |

## 3. Retrospective (problem-solving)
Top 3 systemic issues surfaced in sprint retros; root-cause analysis; actions.

## 3b. Workflow pain points (living ledger — continuous capture)
This section is the **per-PI workflow-improvement ledger**: workflow friction (a clunky/ambiguous step, a missing or wrong template field, a kanban/transition rule that fought you, a routing/dispatch gap, a redundant or contradictory instruction, a missing tool/capability) is appended here **the moment it is observed** — never fixed inline mid-flow, never deferred to memory — plus items fed up from sprint retros (retro §2b). Each is an *input* (raw friction, not a solution), triaged in §4. Append-only: never delete an entry — flip its `status`. `@release-train-engineer` captures program/ART friction here; portfolio-scope items feed to Strategic Portfolio Review, iteration-scope items rise from the sprint retros.
| Pain point | Origin | Layer | Symptom | Status |
|---|---|---|---|---|
| PP-YYYYMMDD-NN | <product>/<sprint\|pi> (or cross-product) | portfolio\|program\|iteration | what friction was hit (no solution here) | open |

## 4. Improvement backlog items (triage + resolution)
Triage each §3/§3b pain point into exactly one target and record its resolution **here** (this is the ledger's output block — there is no separate file):

**Workflow improvements** (resolve a pain point) — a change to a **skill / agent / instruction / prompt / orchestrator template**. Fill the row's root-cause + improvement + target, implement the change, and mark `status: resolved`. **Not** product Features.
| Pain point | Root cause | Improvement (meta-artifact change) | Target file | Owner | Status |
|---|---|---|---|---|---|
| PP-... | ... | ... | `layers/…` / `instructions/…` / `harness/…` | RTE | open |

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
