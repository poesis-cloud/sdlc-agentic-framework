---
name: sm-orchestration
description: 'Team / iteration layer of the SAFe orchestration. Loaded by @sm-orchestrator on top of the orchestration-core base. Covers Iteration Planning + sprint plan, Story grooming (PO hat) and the ★ Story Gate (backlog → ready Definition-of-Ready validation), the pair-programming micro-cycle (HUDDLE -> DRIVE -> CRITIQUE -> ACCEPT/REJECT -> SWAP), the Team Kanban, WIP limits, Daily Sync / Iteration Review / Retro, QA acceptance, and ★ PR Gate packet preparation. Use for everything at or below the iteration line.'
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

## What the sm-orchestrator governs (iteration-layer police)

The SM **polices** the iteration layer: it controls the agents' input/output artifacts, enforces conformance to its **owned templates** + SAFe practice, and owns the **flow** (★ Story / PR gates, Team Kanban, WIP). It does **not** author or own the backlog.

- **Iteration Planning** — `<P>sprint-N/plan.md`; assign Driver/Navigator per Story.
- **Stories (PO-owned)** — dispatch `SE: Product Manager` (PO hat), who **authors** `<P>sprint-N/stories/S-NNN.md`; sm polices the **★ Story Gate** (DoR, `backlog -> ready`), template + SAFe conformance, renders the **Team Kanban** (`<P>kanban/team-sprint-N.md`), owns the in-iteration transitions, and enforces **WIP limits**. sm owns the iteration-tier templates (sprint-plan, story, qa-signoff, daily, retro, progress, gate-decisions, kanban-team).
- **Pair-programming micro-cycle** — coach HUDDLE -> DRIVE -> CRITIQUE -> ACCEPT/REJECT -> SWAP (see Pair Programming below).
- **Events** — Daily Sync (`<P>sprint-N/daily-N.md`), Iteration Review, Retro (`<P>sprint-N/retro.md`); update `<P>sprint-N/progress.md`.
- **QA + ★ PR Gate packet** — dispatch `ai-team-qa`; drive Story -> `awaiting-pr`; hand the packet to the Central Supervisor (`@rte-orchestrator` merges).
- **Story cost — once, at `in-qa -> awaiting-pr`** — fetch dev + QA dispatch tokens from session logs (matched by `S-NNN`; no intermediary ledger); write `cost:` once ([cost-accounting](../orchestration-core/references/cost-accounting-protocol.md)).
- **Pain points — continuous** — append iteration friction to `portfolio/_improvement-log.md` (input block, `status: open`; no inline fix).
- **Impediments** — remove iteration-level; escalate program-level to `@rte-orchestrator`.

Dispatched by `@rte-orchestrator` at PI/Iteration Planning, or directly by the Central Supervisor; hands the Story to the Central Supervisor at the **★ PR Gate** and back to `@rte-orchestrator` for merge. **Facilitates; never decides scope; never writes production code.**

## Iteration flow — Story handling matrix

The iteration workflow **is the Story FSM**: `backlog → ready → in-progress → in-review → in-qa → awaiting-pr → done` (flag `blocked`). sm is the **event loop** and the **only writer of Story `status:`**. One matrix folds the flow, sub-orchestrations, and gates (kinds **D / Ceremony / Practice / Gate**). The pair micro-cycle and verification are **CI practices** (multi-agent sub-orchestrations), not solo work.

| Event (Story reaches…) | Kind | Sub-orchestration | Gate | → sm commits |
|---|---|---|---|---|
| Feature `committed` (← `@rte`) | Ceremony | **Iteration Planning** (sm + `SE:PM`·PO derives → Stories + pairs + `plan.md`) | — | `∅→backlog` |
| `backlog` not DoR-ready | Ceremony·CE | **Story Backlog Refinement** (`SE:PM`·PO grooms) | — | — *(stays `backlog`)* |
| unknown / spike surfaced | Ceremony·CE | **Story Backlog Refinement** → seeds an **Enabler Story (spike)** | — | `∅→backlog` (`type: enabler`) |
| `backlog` *(DoR holds — checklist below)* | **Gate** | — | **★ Story Gate** (sm-run DoR) | accept→`ready` (assign Driver+Navigator; first `ready` ⇒ **notify `@rte`**, Feature `→in-progress`) · reject→stay `backlog` |
| `ready` + pair free | Practice·CI | **Pair micro-cycle** — Driver · DRIVE (+ tests) | — | `ready→in-progress` |
| one unit committed | Practice·CI | **Pair micro-cycle** — Navigator · CRITIQUE | — | `in-progress→in-review` |
| CRITIQUE accept (WIP `in-qa`≤2) | D | — | — | `in-review→in-qa` |
| CRITIQUE reject | D | — | — | `in-review→in-progress` (log a SWAP) |
| DoD ok · `SE:Security` verdict | Practice·CI | **Verification & Sign-off** (`ai-team-qa` + `SE:Security`) → `qa-signoff` | — | `in-qa→awaiting-pr`; commit Story `cost:` once; publish board |
| DoD fail | D | — | — | `in-qa→in-progress` (bug report) |
| `awaiting-pr` *(board-published · QA + Security attached)* | **Gate** | — | **★ PR Gate** (CS) | *(rte merges `awaiting-pr→done`; roll-up to Feature)* |
| any Story transition / `→blocked` | Ceremony | **Daily Sync** (blockers + WIP → `daily-DD.md` + `progress.md`) | — | `→blocked`/unblock |
| `→awaiting-pr` / `done` | Ceremony | **Iteration Review** (increment → CS + stakeholders) | — | — *(feedback ⇒ backlog items)* |
| `→done` | Ceremony | **Retrospective** (→ `retro.md`; triage sprint pain points) | — | — *(escalate program-scope → Inspect & Adapt)* |

**★ Story Gate — Definition of Ready (all must hold):**

| DoR check | Must hold |
|---|---|
| ID + title + parent Feature | present |
| Acceptance criteria | unambiguous and testable (no "should/may") |
| Parent Feature is `committed` or `in-progress` | verified in Feature frontmatter |
| No unresolved upstream Story blockers | confirmed |
| Repos in scope identified | from `product.yaml > repos[]` |
| Driver/Navigator pair assigned | SM assigns before `ready` |

The **pair micro-cycle** (HUDDLE → DRIVE → CRITIQUE → ACCEPT/REJECT → SWAP) and **Verification & Sign-off** are the iteration's **CI practices** — multi-agent sub-orchestrations, detailed in **Pair Programming** below. All sub-orchestrations are listed in the handling matrix above; sm **facilitates** and authors only **flow/meta** artifacts (plan, daily, progress, retro), Story authoring stays with `SE:PM`·PO, and the ★ gates stay with the Central Supervisor.

## Team Kanban ownership

The sm-orchestrator renders `<P>kanban/team-sprint-N.md` from Story frontmatter after every Story status flip. It owns `ready`, `blocked` (iteration), and coaches the `in-progress`/`in-review` pair transitions (Owner = Driver / Navigator respectively). `ai-team-qa` owns `in-qa`; the Central Supervisor owns the ★ PR Gate; rte-orchestrator owns the `awaiting-pr -> done` merge. See orchestration-core for the full table.

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

See [anti-patterns.md](../orchestration-core/references/anti-patterns.md).
