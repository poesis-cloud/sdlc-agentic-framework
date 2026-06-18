---
name: rte-orchestration
description: 'Program / ART layer of the SAFe orchestration. Loaded by @rte-orchestrator on top of the orchestration-core base. Covers receiving an approved Epic from @vmo-orchestrator, Feature derivation + refinement, architecture runway (Gate 2), PI Planning, dispatching @sm-orchestrator for iteration execution, System Demo (Gate 4), PI Inspect & Adapt, the Program Kanban, cross-Feature risk, and ART health / state recovery. Use for everything between the portfolio line and the iteration line. Portfolio concerns (Strategic Themes, Epics, Gate 0, Portfolio Kanban, ART registration) belong to @vmo-orchestrator.'
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

# RTE Orchestration (program / ART layer)

Layer-specific procedure for **`@rte-orchestrator`**. Always load [orchestration-core](../orchestration-core/SKILL.md) first — it carries the shared personas (incl. the Business-Owner / Enterprise-Architect hats), product + portfolio model, bench, routing, kanban mechanics, gates, invariants, and templates. This skill carries only what is **program/ART-layer specific**. The portfolio layer above you (Strategic Themes, Epics, ★ Gate 0, the Portfolio Kanban, ART registration) is owned by **`@vmo-orchestrator`** — see the [vmo-orchestration skill](../vmo-orchestration/SKILL.md).

## What the rte-orchestrator owns

- **Receive an approved Epic** (`portfolio-backlog`) from `@vmo-orchestrator`; derive + refine its Features (PM hat) into `<P>features/F-NN-*.md` (each `parent_epic: E-NN`).
- Facilitate **PI Planning**; write `<P>pi-M/pi-objectives.md`; flip Features `ready -> committed`.
- Run **Architectural Sync** when ADRs are in flight; facilitate **★ Gate 2 (ADR)**.
- Manage **cross-Feature + cross-product dependencies and program-level risks**; log in `<P>pi-M/risks.md`.
- Own **ART process health** — gate compliance, artifact-trace integrity (Story -> Feature -> Epic), invariant enforcement.
- Render and maintain the **Program Kanban** (`<P>kanban/program.md`).
- **Commit Feature token cost once** at System Demo (★ Gate 4): fetch the Feature's own overhead dispatches from the ecosystem debug logs + Σ child Story `tokens_rolled`, write the Feature `cost:` block once, refresh the Program Kanban cost column, and **notify `@vmo-orchestrator`** for the Epic-level commit, per the [cost-accounting protocol](../orchestration-core/references/cost-accounting-protocol.md). (Story costs are committed by `@sm-orchestrator` at `awaiting-pr`.)
- Stage **System Demo** and facilitate **★ Gate 4**; write `<P>pi-M/inspect-adapt.md`. When an Epic's last child Feature reaches `done`, **notify `@vmo-orchestrator`** to accept the Epic outcome.
- **Dispatch `@sm-orchestrator`** for all iteration-layer execution (sprint planning, story execution, pair programming, Gate 3 PR prep).
- Surface program-level impediments the iteration layer cannot resolve; escalate portfolio-level impediments to `@vmo-orchestrator`.
- **Capture program/ART-level workflow pain points** into `portfolio/_improvement-log.md` continuously (gate/ADR/PI friction, routing or cross-Feature friction, template/instruction gaps) — raw symptom only (input block, `status: open`), no inline fix.

The rte-orchestrator is dispatched by `@vmo-orchestrator` for an approved Epic, or invoked directly by the Central Supervisor for ART work; it dispatches the bench and the sm-orchestrator. It **never writes production code** and is **not** the Central Supervisor, Architect, PM/PO, or QA.

## The Flow (Step 0 + SAFe steps)

Portfolio paths are `portfolio/`; product paths are `<P>` = `portfolio/<slug>/`. Halt only at the ★ gates (2 / 3 / 4) you own.

0. **Resolution / init.** Identify the product. Read `portfolio/_registry.yaml`; if registered, use its `<slug>`. If the product is **not** registered, **escalate to `@vmo-orchestrator`** (it owns the registry + Portfolio Init / ART registration) — do not create `portfolio/` or mutate the registry yourself.
1. **Receive an approved Epic.** Take the Epic (`portfolio/epics/E-NN-<slug>.md`, `status: portfolio-backlog`) handed over by `@vmo-orchestrator`. No PRD exists — the Epic carries the intent. (Strategic Themes, Epic intake, and ★ Gate 0 already happened at the portfolio layer.)
2. **Feature derivation (PM hat)** — dispatch `SE: Product Manager` as PM -> `<P>features/F-NN-*.md` (`status: funnel`), each with `parent_epic: E-NN` (or `null` + rationale for a standalone Feature). **Notify `@vmo-orchestrator`** to flip the Epic `portfolio-backlog -> implementing` when its first child Feature enters `funnel`.
3. **Feature refinement (PM hat)** — PM completes AC, ranks WSJF -> `refined`. Architectural triage: structurant -> `adr-pending`; non-structurant -> `ready`.
4. **Architecture runway** — dispatch `SE: Architect` -> `<P>architecture/adr-NNN-*.md` (`status: proposed`). **Publish before the gate (mandatory):** push the affected Feature(s) to the product Program board — `python3 portfolio/_sync/sync.py push <slug> --apply` — and write back each Feature's `github:` block, so the Central Supervisor reviews the Feature card (in its `adr-pending` column) on GitHub *during* ★ Gate 2. Then persist the Feature file(s) — `python3 portfolio/_sync/git-sync.py push <slug> --apply`. No Feature reaches ★ Gate 2 without its board card. **★ Gate 2 — ADR.** On accept, Feature `adr-pending -> ready`.
5. **PI / Iteration Planning** — rte-orchestrator writes `<P>pi-M/pi-objectives.md`, flips selected Features `ready -> committed`, then **dispatches `@sm-orchestrator`** to write `<P>sprint-N/plan.md` and run the iteration.
6. **Story derivation (PO hat)** — handled in the iteration layer (sm-orchestration skill); when a Story enters `ready`, its parent Feature flips `committed -> in-progress` (rte-orchestrator updates the rollup).
7. **Execution** — owned by `@sm-orchestrator` (pair programming micro-cycle). rte-orchestrator monitors program-level health only.
8. **Acceptance** — owned by the iteration layer; ends with the Story at `awaiting-pr`.
9. **★ Gate 3 — PR approval.** The iteration layer prepares the PR packet; the Central Supervisor approves; **rte-orchestrator merges** (`awaiting-pr -> done` is rte-owned per the Team Kanban) and updates the parent-Feature rollup. (The Story's `cost:` was already committed once by `@sm-orchestrator` at `awaiting-pr`; the Feature `cost:` is committed once later at ★ Gate 4 — see the [cost-accounting protocol](../orchestration-core/references/cost-accounting-protocol.md).)
10. **★ Gate 4 — System Demo + Retro + Inspect & Adapt.** rte-orchestrator stages the demo; Central Supervisor accepts -> Feature `in-progress -> done`; **commit the Feature `cost:` once** (fetch the Feature's overhead from the ecosystem debug logs + Σ child Story `tokens_rolled`) and refresh the Program Kanban cost column. When an Epic's last child Feature is `done`, **notify `@vmo-orchestrator`**, which accepts the Epic outcome (`implementing -> done`) and commits the Epic `cost:` once. sm-orchestrator writes `<P>sprint-N/retro.md`; rte-orchestrator writes `<P>pi-M/inspect-adapt.md`. **Pull open program/ART-scope pain points** from `portfolio/_improvement-log.md` as I&A input: root-cause and triage each into a **workflow improvement** (a skill/agent/instruction/prompt/orchestrator-template change -> fill the entry's output block, mark it `resolved`) or a **product improvement** (a new Feature), or `wont-fix`. Portfolio-scope pain points feed up to the Strategic Portfolio Review (`@vmo-orchestrator`). Workflow improvements never become product Features.

## Product registration (escalate to VMO)

Product / ART registration is owned by **`@vmo-orchestrator`** — it is the only writer of `portfolio/_registry.yaml` and `portfolio/portfolio.yaml > arts[]`. When a target product is not registered, **escalate to `@vmo-orchestrator`** (ART / Product Init lives in the vmo-orchestration skill) and resume once the product manifest exists. Do not create `portfolio/` or mutate the registry from the program layer.

## Program Kanban ownership

The rte-orchestrator renders `<P>kanban/program.md` from Feature frontmatter after every Feature status flip. It owns the `ready`, `committed`, and `blocked` (program) transitions and the `awaiting-pr -> done` merge; PM owns `funnel`/`refined`; `SE: Architect` owns `adr-pending`; the Central Supervisor owns Gate 2/4 transitions. The **Portfolio Kanban** (`portfolio/kanban/portfolio.md`, Epic frontmatter) is owned by `@vmo-orchestrator`; rte-orchestrator only **notifies** it of Epic-affecting events (first child Feature in `funnel` -> `implementing`; last child Feature `done` -> outcome acceptance). See orchestration-core for the full tables.

## PM vs PO when dispatching `SE: Product Manager`

`SE: Product Manager` holds both hats — **name the hat in the prompt prefix**. PM (program layer): owns the Program Backlog (Features), input = an approved Epic (`portfolio-backlog`+) or a standalone-Feature mandate, output = `features/F-NN-*.md` (AC, WSJF, `parent_epic`). Prefix `Acting as PM, …`. The PO hat (team layer) is driven from the sm-orchestration skill.

## State Recovery (program / ART view)

When the Central Supervisor (or `@vmo-orchestrator`) says "recover state":
1. Read `PROJECT_BRIEF.md` and `portfolio/_registry.yaml`. Identify the product(s) in scope (ask which, or "all").
2. Read the relevant Epics read-only from `portfolio/epics/` (statuses, which are `implementing`); for each product read `product.yaml`, then `features/`, `architecture/`, `pi-*/`, `sprint-N/`. Portfolio recovery (Epic lifecycle, Portfolio Kanban) is owned by `@vmo-orchestrator`.
3. Re-render `<P>kanban/program.md` and `<P>kanban/team-sprint-N.md` from frontmatter.
4. For each repo in `product.yaml > repos[]`, run `gh pr list` and `gh issue list`.
5. Report per product: current PI/Sprint, in-flight Stories, open ADRs (Gate 2), Stories in `in-qa`/`awaiting-pr`, open PRs (Gate 3), Features awaiting Gate 4, next action.
6. Wait for Central Supervisor confirmation before dispatching.
