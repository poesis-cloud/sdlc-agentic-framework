---
name: rte-orchestration
description: 'Program / ART layer of the SAFe orchestration. Loaded by @rte-orchestrator on top of the orchestration-core base. Covers receiving an approved Epic from @vmo-orchestrator, Feature derivation + refinement, architecture runway (the ADR Gate), PI Planning, dispatching @sm-orchestrator for iteration execution, System Demo (the Feature Gate), PI Inspect & Adapt, the Program Kanban, cross-Feature risk, and ART health / state recovery. Use for everything between the portfolio line and the iteration line. Portfolio concerns (Strategic Themes, Epics, the Epic Gate, Portfolio Kanban, ART registration) belong to @vmo-orchestrator.'
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

Layer-specific procedure for **`@rte-orchestrator`**. Always load [orchestration-core](../orchestration-core/SKILL.md) first — it carries the shared personas (incl. the Business-Owner / Enterprise-Architect hats), product + portfolio model, bench, routing, kanban mechanics, gates, invariants, and templates. This skill carries only what is **program/ART-layer specific**. The portfolio layer above you (Strategic Themes, Epics, the ★ Epic Gate, the Portfolio Kanban, ART registration) is owned by **`@vmo-orchestrator`** — see the [vmo-orchestration skill](../vmo-orchestration/SKILL.md).

## What the rte-orchestrator governs (program/ART-layer police)

The RTE **polices** the program layer: it controls the agents' input/output artifacts, enforces conformance to its **owned templates** + SAFe practice, and owns the **flow** (gates, Program Kanban, PI cadence). It does **not** author or own the backlog.

- **Features (PM-owned)** — dispatch `SE: Product Manager` (PM hat), who **authors + refines** `<P>features/F-NN-*.md` (`parent_epic: E-NN`); rte polices template + SAFe conformance and renders the **Program Kanban** (`<P>kanban/program.md`). rte owns the program-tier templates (feature, adr, pi-objectives, risks, inspect-adapt, kanban-program).
- **Architecture runway** — **ART Sync** (Architect participates) while ADRs are in flight; facilitate the **★ ADR Gate**.
- **PI Planning** — `<P>pi-M/pi-objectives.md`; flip Features `ready -> committed`; **dispatch `@sm-orchestrator`** for all iteration execution (sprint planning, story execution, pair programming, ★ PR Gate prep).
- **System Demo** — facilitate the **★ Feature Gate**; write `<P>pi-M/inspect-adapt.md`; merge approved PRs (**★ PR Gate**, `awaiting-pr -> done`).
- **ART health** — gate compliance, artifact-trace integrity (Story -> Feature -> Epic), invariant enforcement, cross-Feature/-product risk (`<P>pi-M/risks.md`); remove program-level impediments, escalate portfolio ones to `@vmo-orchestrator`.
- **Feature cost — once, at the ★ Feature Gate** — fetch overhead from ecosystem logs + Σ child Story `tokens_rolled`; write `cost:` once; refresh kanban; **notify `@vmo-orchestrator`** for the Epic-level commit ([cost-accounting](../orchestration-core/references/cost-accounting-protocol.md)). Story cost is `@sm-orchestrator`'s at `awaiting-pr`.
- **Pain points — continuous** — append program/ART friction to `portfolio/_improvement-log.md` (input block, `status: open`; no inline fix).

Dispatched by `@vmo-orchestrator` for an approved Epic, or directly by the Central Supervisor; dispatches the bench + `@sm-orchestrator`. **Never writes production code**; is **not** the Central Supervisor, Architect, PM/PO, or QA.

## The Flow (Step 0 + SAFe steps)

Portfolio paths are `portfolio/`; product paths are `<P>` = `portfolio/<slug>/`. Halt only at the ★ gates (ADR / PR / Feature) you own.

0. **Resolution / init.** Identify the product via `portfolio/_registry.yaml`. If unregistered, **escalate to `@vmo-orchestrator`** (it owns the registry + Portfolio Init / ART registration) — never create `portfolio/` or mutate the registry yourself.
1. **Receive the Epic** (`portfolio/epics/E-NN-<slug>.md`, `portfolio-backlog`) from `@vmo-orchestrator`. No PRD — the Epic carries the intent (Strategic Themes, intake, and the ★ Epic Gate already happened at the portfolio layer).
2. **Feature derivation (PM hat)** — dispatch `SE: Product Manager` → `<P>features/F-NN-*.md` (`funnel`), each `parent_epic: E-NN` (or `null` + rationale). **Notify `@vmo-orchestrator`** to flip the Epic `portfolio-backlog -> implementing` on the first child Feature.
3. **Feature refinement (PM hat)** — AC + WSJF → `refined`; architectural triage: structurant → `adr-pending`, else → `ready`.
4. **Architecture runway + ★ ADR Gate** — dispatch `SE: Architect` → `<P>architecture/adr-NNN-*.md` (`proposed`). **Challenge (mandatory):** `SE: Security` + `SE: DevOps/CI` adversarially review the ADR + Feature from their lens; fold material findings into the ADR (Options/Consequences) and surface unresolved ones in the gate packet. **Publish before the gate (mandatory):** `python3 portfolio/_sync/sync.py push <slug> --apply` + `github:` write-back so the Feature card (`adr-pending`) is reviewable on GitHub *during* the gate; then `python3 portfolio/_sync/git-sync.py push <slug> --apply`. No Feature reaches the gate without its board card. On accept → Feature `adr-pending -> ready`.
5. **PI / Iteration Planning** — write `<P>pi-M/pi-objectives.md`; flip selected Features `ready -> committed`; **dispatch `@sm-orchestrator`** to write `<P>sprint-N/plan.md` and run the iteration.
6. **Iteration layer (Stories → execution → acceptance)** — owned by `@sm-orchestrator` (PO-hat derivation, pair micro-cycle, QA). First Story `ready` flips its parent Feature `committed -> in-progress` (rte updates the rollup); the layer ends each Story at `awaiting-pr`. rte monitors program-level health only.
7. **★ PR Gate** — the iteration layer prepares the PR packet (QA sign-off + `SE: Security` pre-merge review attached); the Central Supervisor approves; **rte merges** (`awaiting-pr -> done` is rte-owned) and updates the parent-Feature rollup. (The Story `cost:` was already committed by `@sm-orchestrator` at `awaiting-pr`; the Feature `cost:` commits once at the ★ Feature Gate.)
8. **★ Feature Gate — System Demo + Retro + Inspect & Adapt.** rte stages the demo; Central Supervisor accepts → Feature `in-progress -> done`; **commit the Feature `cost:` once** (overhead from ecosystem logs + Σ child Story `tokens_rolled`) and refresh the kanban. On the Epic's last child Feature `done`, **notify `@vmo-orchestrator`** for Epic outcome acceptance + Epic cost. sm writes `<P>sprint-N/retro.md`; rte writes `<P>pi-M/inspect-adapt.md`; **pull open program/ART-scope pain points** from `portfolio/_improvement-log.md` and triage each into a **workflow** improvement (skill/agent/instruction/prompt/template change → fill output block, mark `resolved`) or a **product** Feature, or `wont-fix`. Workflow improvements never become product Features.

## Product registration (escalate to VMO)

Product / ART registration is owned by **`@vmo-orchestrator`** — it is the only writer of `portfolio/_registry.yaml` and `portfolio/portfolio.yaml > arts[]`. When a target product is not registered, **escalate to `@vmo-orchestrator`** (ART / Product Init lives in the vmo-orchestration skill) and resume once the product manifest exists. Do not create `portfolio/` or mutate the registry from the program layer.

## Program Kanban ownership

The rte-orchestrator renders `<P>kanban/program.md` from Feature frontmatter after every Feature status flip. It owns the `ready`, `committed`, and `blocked` (program) transitions and the `awaiting-pr -> done` merge; PM owns `funnel`/`refined`; `SE: Architect` owns `adr-pending`; the Central Supervisor owns the ★ ADR / Feature gate transitions. The **Portfolio Kanban** (`portfolio/kanban/portfolio.md`, Epic frontmatter) is owned by `@vmo-orchestrator`; rte-orchestrator only **notifies** it of Epic-affecting events (first child Feature in `funnel` -> `implementing`; last child Feature `done` -> outcome acceptance). See orchestration-core for the full tables.

## PM vs PO when dispatching `SE: Product Manager`

`SE: Product Manager` holds both hats — **name the hat in the prompt prefix**. PM (program layer): owns the Program Backlog (Features), input = an approved Epic (`portfolio-backlog`+) or a standalone-Feature mandate, output = `features/F-NN-*.md` (AC, WSJF, `parent_epic`). Prefix `Acting as PM, …`. The PO hat (team layer) is driven from the sm-orchestration skill.

## State Recovery (program / ART view)

When the Central Supervisor (or `@vmo-orchestrator`) says "recover state":
1. Read `PROJECT_BRIEF.md` and `portfolio/_registry.yaml`. Identify the product(s) in scope (ask which, or "all").
2. Read the relevant Epics read-only from `portfolio/epics/` (statuses, which are `implementing`); for each product read `product.yaml`, then `features/`, `architecture/`, `pi-*/`, `sprint-N/`. Portfolio recovery (Epic lifecycle, Portfolio Kanban) is owned by `@vmo-orchestrator`.
3. Re-render `<P>kanban/program.md` and `<P>kanban/team-sprint-N.md` from frontmatter.
4. For each repo in `product.yaml > repos[]`, run `gh pr list` and `gh issue list`.
5. Report per product: current PI/Sprint, in-flight Stories, open ADRs (★ ADR Gate), Stories in `in-qa`/`awaiting-pr`, open PRs (★ PR Gate), Features awaiting the ★ Feature Gate, next action.
6. Wait for Central Supervisor confirmation before dispatching.
