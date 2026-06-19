# Workflow Improvement Ledger Template — `portfolio/_improvement-log.md`

Poesis-level **singleton**, cross-product. The single source of truth for improving the
*orchestration workflow itself*. Merges two stages into one append-only ledger so a unit of
friction and its fix never drift apart:

- **Input** — a workflow **pain point** (raw friction) captured continuously by the orchestrators
  the moment it is hit, never at retro time.
- **Output** — the **improvement** (a meta-artifact change: skill / agent / instruction / prompt /
  orchestrator template) that resolves it, decided at **Retro** or **Inspect & Adapt**.

A pain point is an *input*, **not yet** an improvement. Resolutions are workspace-level
meta-artifacts — **never** product Features.

```markdown
---
scope: poesis-orchestration
purpose: |
  Append-only ledger for improving the orchestration workflow itself.
  Each entry runs the full lifecycle: pain point (input) -> triage at
  Retro / Inspect & Adapt -> improvement (output, a meta-artifact change).
  Resolutions are workspace-level meta-artifacts (skill / agent / instruction /
  prompt / orchestrator template) — never product Features.
captured_by: [vmo-orchestrator, rte-orchestrator, sm-orchestrator]
reviewed_at: [sprint-retro, inspect-adapt]
maintained_by: RTE
---

# Poesis workflow improvement ledger (pain point -> improvement)

> Append-only. Never delete — flip `status`, or supersede with a new entry that back-refs the old.
> Capture the symptom the moment friction is hit; do **not** solve inline.
> Fill the output block only at/after Retro (sm, sprint-scope) / Inspect & Adapt (rte, PI-scope) / Strategic Portfolio Review (vmo, portfolio-scope).

## PP-YYYYMMDD-NN — <one-line symptom>
Input (captured continuously):
- surfaced-by: vmo-orchestrator | rte-orchestrator | sm-orchestrator | Central Supervisor | <subagent>
- origin: <portfolio | product>/<sprint-N | pi-M> (or cross-product)
- layer: portfolio | program | iteration
- symptom: what friction was hit (no solution here)
- candidate-target: skill | agent | instruction | prompt | template | (unknown)
- status: open | triaged | resolved | wont-fix | superseded
Output (filled at/after Retro / Inspect & Adapt):
- root-cause: why it happened
- improvement: the meta-artifact change that resolves it
- target: <path to the skill/agent/instruction/prompt/template changed>
- resolved: <date + commit / back-ref>
```

## Lifecycle — articulated with Retro and Inspect & Adapt

1. **Capture (continuous).** Any orchestrator appends a pain point (input block only,
   `status: open`) the moment it hits workflow friction. `@vmo-orchestrator` captures
   portfolio-scope friction; `@rte-orchestrator` captures program/ART-scope friction;
   `@sm-orchestrator` captures iteration-scope friction. Never solve inline — the symptom only.
2. **Review (Retro / I&A / Portfolio Review).** Open pain points are pulled in as *input*:
   - **Sprint Retro** (sm, sprint-scope, §2b of [retro-template.md](./retro-template.md)) —
     resolve iteration-local ones; feed program/ART-scope ones up.
   - **Inspect & Adapt** (rte, PI-scope, §3b of [inspect-adapt-template.md](./inspect-adapt-template.md)) —
     root-cause and triage each into a workflow improvement, a product Feature, or `wont-fix`; feed portfolio-scope ones up.
   - **Strategic Portfolio Review** (vmo, portfolio-scope) — root-cause and triage portfolio-scope
     entries into a workflow improvement, a product Epic, or `wont-fix`.
3. **Resolve (output).** A **workflow** improvement is a concrete meta-artifact change — fill the
   output block, implement the change, set `status: resolved` with a back-ref. Delivery-level root
   causes become product **Features** instead (tracked in their product's backlog, not here).

This ledger is the standing **input** to every Inspect & Adapt (I&A §3b) and Sprint Retro
(retro §2b); those rituals are where its open entries become resolved improvements. Keep the
input and output blocks **distinct within an entry** — capturing a symptom must never wait on, or
be conflated with, deciding its fix.
