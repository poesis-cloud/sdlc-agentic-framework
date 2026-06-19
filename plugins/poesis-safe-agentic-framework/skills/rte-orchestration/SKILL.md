---
name: rte-orchestration
description: 'Program / ART layer of the SAFe orchestration. Loaded by @rte-orchestrator on top of the orchestration-core base. Covers receiving an approved Epic from @vmo-orchestrator, Feature derivation + refinement, architecture runway (the Architecture Gate), PI Planning, dispatching @sm-orchestrator for iteration execution, System Demo (the Demo Gate), ART Sync, PI Inspect & Adapt, the Program Kanban, cross-Feature risk, and ART health / state recovery. Use for everything between the portfolio line and the iteration line. Portfolio concerns (Strategic Themes, Epics, the Epic Gate, Portfolio Kanban, ART registration) belong to @vmo-orchestrator.'
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

The RTE **polices** the program layer: it controls the agents' input/output artifacts, enforces conformance to its **owned templates** + SAFe practice, and owns the **flow** (gates, Program Kanban, per-unit ceremony handlers). It does **not** author or own the backlog.

- **Features (PM-owned)** — dispatch `SE: Product Manager` (PM hat), who **authors + refines** `<P>features/F-NN-*.md` (`parent_epic: E-NN`); rte polices template + SAFe conformance and renders the **Program Kanban** (`<P>kanban/program.md`). rte owns the program-tier templates (feature, adr, pi-objectives, risks, inspect-adapt, kanban-program).
- **Architecture runway** — **ART Sync** (Architect participates) while ADRs are in flight; facilitate the **★ Architecture Gate**.
- **PI Planning** — `<P>pi-M/pi-objectives.md`; flip Features `ready -> committed`; **dispatch `@sm-orchestrator`** for all iteration execution (sprint planning, story execution, pair programming, ★ PR Gate prep).
- **System Demo** — facilitate the **★ Demo Gate**; write `<P>pi-M/inspect-adapt.md`; merge approved PRs (**★ PR Gate**, `awaiting-pr -> done`).
- **ART health** — gate compliance, artifact-trace integrity (Story -> Feature -> Epic), invariant enforcement, cross-Feature/-product risk (`<P>pi-M/risks.md`); remove program-level impediments, escalate portfolio ones to `@vmo-orchestrator`.
- **Feature cost — once, at the ★ Demo Gate** — fetch overhead from ecosystem logs + Σ child Story `tokens_rolled`; write `cost:` once; refresh kanban; **notify `@vmo-orchestrator`** for the Epic-level commit ([cost-accounting](../orchestration-core/references/cost-accounting-protocol.md)). Story cost is `@sm-orchestrator`'s at `awaiting-pr`.
- **Pain points — continuous** — append program/ART friction to `portfolio/_improvement-log.md` (input block, `status: open`; no inline fix).

Dispatched by `@vmo-orchestrator` for an approved Epic, or directly by the Central Supervisor; dispatches the bench + `@sm-orchestrator`. **Never writes production code**; is **not** the Central Supervisor, Architect, PM/PO, or QA.

## The Flow — Feature handling matrix

The program/ART workflow **is the Feature FSM**: `funnel → refined → arch-pending → ready → committed → in-progress → done` (flag `blocked`). rte is the **event loop** and the **only writer of Feature `status:`**. One matrix folds the flow, sub-orchestrations, and gates (kinds **D / Ceremony / Practice / Gate**). Each Feature carries `type: business | enabler`. Halt only at the ★ gates (Feature / Architecture / Demo / PR) you own. **Step 0:** if the product is unregistered, **escalate to `@vmo`**.

| Event (Feature reaches…) | Kind | Sub-orchestration | Gate | → rte commits |
|---|---|---|---|---|
| Epic `portfolio-backlog`+ (← `@vmo`) | Ceremony·CE | **Feature Backlog Refinement** (`SE:PM`·PM authors; Architect / dev / QA / UX / Security) → AC + WSJF + `structurant` | — | `∅→funnel` → `funnel→refined`; **notify `@vmo`** (Epic→`implementing`) |
| `refined` *(refined)* | **Gate** | — | **★ Feature Gate** (rte-run; escalate if structurant/contested) | accept→`arch-pending` (structurant) / `ready` · reject→`funnel` (re-refine) |
| `arch-pending` *(produce)* | Practice·CE | **Architectural Runway Extension** (`SE:Architect`·SA + Security + DevOps + dev) → ADR@`proposed` | — | *(ADR committed; stays `arch-pending`)* |
| runway / NFR / compliance gap | Practice·CE | **Architectural Runway Extension** → seeds an **Enabler Feature** | — | `∅→funnel` (`type: enabler`) |
| `arch-pending` *(ADR decided · challenge done · board-published)* | **Gate** | — | **★ Architecture Gate** (CS) | accept→`ready` · reject→ADR `rejected`, Feature→`refined` |
| `ready` **and** `depends_on` met | Ceremony | **PI Planning** (→ `pi-objectives.md` + `risks.md`) | — | `ready→committed`; **dispatch `@sm`** |
| first child Story `ready` (roll-up ← `@sm`) | D | — | — | `committed→in-progress` |
| child Stories **all `done`** | Ceremony | **System Demo** (stages the increment for the CS) | **★ Demo Gate** (CS) | accept→`in-progress→done`; commit Feature `cost:` once; **notify `@vmo`** |
| Story `awaiting-pr` (rte-owned merge) | **Gate** | — | **★ PR Gate** (CS) | Story `awaiting-pr→done` (**rte merges**); roll-up to Feature |
| any Feature transition / `→blocked` / ADR in flight | Ceremony | **ART Sync** (deps + risk + runway → `risks.md` + kanban) | — | `→blocked`/unblock |
| `done` *(synthesise at an Epic's completion)* | Ceremony | **Inspect & Adapt** (→ `inspect-adapt.md`) | — | triage program pain points; enabler gaps ⇒ seed Feature `∅→funnel` |

rte **facilitates** and authors only **flow/meta** artifacts (pi-objectives, risks, inspect-adapt, kanban); Features / ADRs stay delegated; the human ★ gates (Architecture / Demo / PR) stay with the Central Supervisor.

## Product registration (escalate to VMO)

Product / ART registration is owned by **`@vmo-orchestrator`** — it is the only writer of `portfolio/_registry.yaml` and `portfolio/portfolio.yaml > arts[]`. When a target product is not registered, **escalate to `@vmo-orchestrator`** (ART / Product Init lives in the vmo-orchestration skill) and resume once the product manifest exists. Do not create `portfolio/` or mutate the registry from the program layer.

## Program Kanban ownership

The rte-orchestrator renders `<P>kanban/program.md` from Feature frontmatter after every Feature status flip. It owns the `ready`, `committed`, and `blocked` (program) transitions and the `awaiting-pr -> done` merge; PM owns `funnel`/`refined`; `SE: Architect` owns `arch-pending`; the Central Supervisor owns the ★ Architecture / Demo gate transitions. The **Portfolio Kanban** (`portfolio/kanban/portfolio.md`, Epic frontmatter) is owned by `@vmo-orchestrator`; rte-orchestrator only **notifies** it of Epic-affecting events (first child Feature in `funnel` -> `implementing`; last child Feature `done` -> outcome acceptance). See orchestration-core for the full tables.

## PM vs PO when dispatching `SE: Product Manager`

`SE: Product Manager` holds both hats — **name the hat in the prompt prefix**. PM (program layer): owns the Program Backlog (Features), input = an approved Epic (`portfolio-backlog`+) or a standalone-Feature mandate, output = `features/F-NN-*.md` (AC, WSJF, `parent_epic`). Prefix `Acting as PM, …`. The PO hat (team layer) is driven from the sm-orchestration skill.

## State Recovery (program / ART view)

When the Central Supervisor (or `@vmo-orchestrator`) says "recover state":
1. Read `PROJECT_BRIEF.md` and `portfolio/_registry.yaml`. Identify the product(s) in scope (ask which, or "all").
2. Read the relevant Epics read-only from `portfolio/epics/` (statuses, which are `implementing`); for each product read `product.yaml`, then `features/`, `architecture/`, `pi-*/`, `sprint-N/`. Portfolio recovery (Epic lifecycle, Portfolio Kanban) is owned by `@vmo-orchestrator`.
3. Re-render `<P>kanban/program.md` and `<P>kanban/team-sprint-N.md` from frontmatter.
4. For each repo in `product.yaml > repos[]`, run `gh pr list` and `gh issue list`.
5. Report per product: current PI/Sprint, in-flight Stories, open ADRs (★ Architecture Gate), Stories in `in-qa`/`awaiting-pr`, open PRs (★ PR Gate), Features awaiting the ★ Demo Gate, next action.
6. Wait for Central Supervisor confirmation before dispatching.
