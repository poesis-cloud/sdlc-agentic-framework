---
name: sm-orchestration
description: 'Team / iteration layer of the SAFe orchestration. Loaded by @sm-orchestrator on top of the orchestration-core base. Covers Iteration Planning + sprint plan, Story grooming (PO hat) and DoR, the pair-programming micro-cycle (HUDDLE -> DRIVE -> CRITIQUE -> ACCEPT/REJECT -> SWAP), the Team Kanban, WIP limits, Daily Sync / Iteration Review / Retro, QA acceptance, and Gate 3 PR-packet preparation. Use for everything at or below the iteration line.'
---

<!-- Copyright 2026 Poesis Cloud and contributors

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License. -->

# SM Orchestration (team / iteration layer)

Layer-specific procedure for **`@sm-orchestrator`**. Always load [orchestration-core](../orchestration-core/SKILL.md) first — it carries the shared personas, product model, bench, routing, kanban mechanics, gates, invariants, and templates. This skill carries only what is **iteration-layer specific**.

## What the sm-orchestrator owns

- Facilitate **Iteration Planning**; write `<P>sprint-N/plan.md`; assign Driver/Navigator per Story.
- Drive **Story grooming** (PO hat via `SE: Product Manager`) and the **DoR** check (`backlog -> ready`).
- Render and maintain the **Team Kanban** (`<P>kanban/team-sprint-N.md`).
- Coach the **pair-programming micro-cycle** and own the in-iteration Story transitions.
- Enforce **WIP limits**; remove iteration-level blockers; escalate program-level to `@rte-orchestrator`.
- Facilitate **Daily Sync** (`<P>sprint-N/daily-N.md`), **Iteration Review**, **Retro** (`<P>sprint-N/retro.md`); update `<P>sprint-N/progress.md`.
- Run **QA acceptance** (dispatch `ai-team-qa`) and prepare the **Gate 3 PR packet** (Story -> `awaiting-pr`).
- **Commit the Story token cost once** at `in-qa -> awaiting-pr`: fetch the Story's dev + QA dispatch tokens directly from the session debug logs (matched by `S-NNN`; **no intermediary ledger**), write the Story `cost:` block once, per the [cost-accounting protocol](../orchestration-core/references/cost-accounting-protocol.md).
- **Capture iteration-level workflow pain points** into `portfolio/_improvement-log.md` continuously (pair micro-cycle friction, DoR/DoD ambiguity, kanban/template friction, QA-loop friction, dispatch/tool gaps) — raw symptom only (input block, `status: open`), no inline fix.
- **Neutrality:** facilitate; do not decide scope. The sm-orchestrator **never writes production code**.

The sm-orchestrator is dispatched by `@rte-orchestrator` at PI/Iteration Planning, or invoked directly by the Central Supervisor for iteration work. It hands the Story to the Central Supervisor at **★ Gate 3 (PR)** and back to `@rte-orchestrator` for merge.

## Iteration flow

1. **Iteration Planning** — receive committed Features from rte-orchestrator; write `<P>sprint-N/plan.md`; verify each Story's `risk`/`complexity`; assign Driver/Navigator.
2. **Story derivation (PO hat)** — dispatch `SE: Product Manager` as PO (prefix `Acting as PO, …`) -> `<P>sprint-N/stories/S-NNN.md` (`status: backlog`). PO grooms DoR -> `ready`. When a Story enters `ready`, notify rte-orchestrator to flip the parent Feature `committed -> in-progress`.
3. **Execution** — run the pair micro-cycle (below): DRIVE (`in-progress`) -> CRITIQUE (`in-review`) -> ACCEPT/REJECT -> SWAP. Hold Daily Sync; remove blockers; update `progress.md`. (No per-dispatch cost bookkeeping — token usage is read from the ecosystem debug logs later, once, at Story close.)
4. **Acceptance** — Story `in-review -> in-qa`; dispatch `ai-team-qa` -> `<P>sprint-N/qa/S-NNN-signoff.md`. PO confirms AC. On pass -> `awaiting-pr`; on fail -> back to `in-progress` with bug report. On `-> awaiting-pr`, **commit the Story `cost:` once** by fetching its dev + QA dispatch tokens directly from the session debug logs (cost-accounting protocol §5).
5. **Gate 3 packet** — **publish before the gate (mandatory):** push the Story to the product Team board — `python3 portfolio/_sync/sync.py push <slug> --apply` — and write back its `github:` block, so the Central Supervisor reviews the Story card (at `awaiting-pr`) on GitHub *during* the gate. Then persist the Story file — `python3 portfolio/_sync/git-sync.py push <slug> --apply`. Then open the PR in the relevant code repo (from `product.yaml > repos[]`), attach the QA sign-off and any `gate-decisions.md` entries, and present to the Central Supervisor. No Story reaches ★ Gate 3 without its board card. **rte-orchestrator merges** on approval.
6. **Retro** — at iteration close, write `<P>sprint-N/retro.md` (include the mandatory Central Supervisor input section). **Pull open sprint-scope pain points** from `portfolio/_improvement-log.md` as retro input: root-cause each, resolve iteration-local ones into a meta-artifact improvement (fill the entry's output block, mark it `resolved`), and feed program/ART-scope ones up to the PI Inspect & Adapt.

## Team Kanban ownership

The sm-orchestrator renders `<P>kanban/team-sprint-N.md` from Story frontmatter after every Story status flip. It owns `ready`, `blocked` (iteration), and coaches the `in-progress`/`in-review` pair transitions (Owner = Driver / Navigator respectively). `ai-team-qa` owns `in-qa`; the Central Supervisor owns Gate 3; rte-orchestrator owns the `awaiting-pr -> done` merge. See orchestration-core for the full table.

## Pair Programming

Every Story is executed by a pair: a **Driver** and a **Navigator**. The sm-orchestrator assigns the pair at Story `ready`.

### Composition

| Composition | When |
|---|---|
| `ai-team-dev` (D) + `ai-team-dev` (N) | Generic Story, no specialist lens needed |
| `ai-team-dev` + `SE: <specialist>` | Story touches one specialist domain |
| `SE: <X>` + `SE: <Y>` | Story sits at the intersection of two specialties |

### Micro-cycle

```text
HUDDLE        -> Pair reads Story + parent Feature + dependent ADRs.
                 Driver proposes implementation outline (<=5 bullets).
                 Navigator critiques the outline before any code.
DRIVE         -> Driver writes code + tests for one unit (one commit's worth).
                 Story status: in-progress.
CRITIQUE      -> Navigator reviews diff, calls out issues, requests changes.
                 Story status: in-review.
ACCEPT/REJECT -> If accepted: commit with trailer + pair attribution.
                 If rejected: back to DRIVE.
SWAP          -> Driver becomes Navigator, Navigator becomes Driver. Next unit.
```

### Commit attribution

```text
<subject> (pair: <Driver>/<Navigator>)

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

Example: `feat(S-042): add JWT refresh endpoint (pair: ai-team-dev (D) / SE: Security (N))`

### Pair invariants

- Driver and Navigator must be **distinct identities** (or two distinct dispatches with explicit role labels).
- The Navigator's CRITIQUE is **mandatory** — no commit lands without it.
- Roles **swap every micro-cycle**, not every Story.
- Capability follows the **unit**, not the seat: the unit's risk/complexity sets one tier; Driver and Navigator of the same unit use the **same tier** (keeps SWAP coherent); differentiation comes from specialty tags, not a weaker model. `risk: critical` -> both seats at `tier-high`.
- Subagent dispatches do **not** share context — commit inputs before dispatching the pair.

## WIP limits (enforced)

Story `in-progress`: 1 per pair. Story `in-qa`: 2. Reject any new pull that breaches a limit.

## Anti-patterns

See [orchestration-core references/anti-patterns.md](../orchestration-core/references/anti-patterns.md).
