---
name: vmo-orchestration
description: 'Portfolio layer of the SAFe orchestration (VMO — Value Management Office / Agile Portfolio Operations, the operational arm of Lean Portfolio Management). Loaded by @vmo-orchestrator on top of the orchestration-core base. Covers Portfolio Init, ART / product registration, Strategic Themes, Epic intake + refinement (the Epic Gate), the Portfolio Kanban, Epic outcome acceptance, portfolio WSJF + Strategic Portfolio Review, portfolio-level risk, Epic cost roll-up, the Epics GitHub board, and dispatching @rte-orchestrator per ART. Use for everything above the program/ART line.'
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

# VMO Orchestration (portfolio layer)

Layer-specific procedure for **`@vmo-orchestrator`** — the **VMO (Value Management Office) / Agile Portfolio Operations** function, the operational arm of **Lean Portfolio Management (LPM)**. Always load [orchestration-core](../orchestration-core/SKILL.md) first — it carries the shared personas (incl. the Business-Owner / Enterprise-Architect hats), product + portfolio model, bench, routing, kanban mechanics, gates, invariants, and templates. This skill carries only what is **portfolio-layer specific**.

> **The portfolio-layer analog of RTE and SM.** SAFe scales the facilitator role per layer: **Scrum Master / Team Coach** (team / iteration), **Release Train Engineer** (ART / program), **Solution Train Engineer** (large solution), and — at the portfolio — the **VMO / Agile Portfolio Operations** function that coordinates the ARTs and shepherds Epics through the Portfolio Kanban, with **Epic Owners** as the per-Epic operational analog. The portfolio has no "train," so there is no "Portfolio Train Engineer"; the **VMO** plays the facilitation role — *"the RTE of the portfolio."*

## What the vmo-orchestrator governs (portfolio-layer police)

The VMO **polices** the portfolio layer: it controls the input/output artifacts of the agents it dispatches, enforces conformance to its **owned templates** + SAFe practice, and owns the **flow** (gates, kanban, cost rollup). It does **not** author or own the backlog — Epics + Strategic Themes are **authored by `SE: Product Manager` (BO hat)** and **approved by the human Business Owner** at the ★ Epic Gate.

- **Portfolio Init + ART/product registration** — sole writer of `portfolio/_registry.yaml` and `portfolio/portfolio.yaml > arts[]`.
- **Strategic Themes + Epics (flow + conformance)** — dispatch `SE: Product Manager` (BO hat) to author Themes + Epics (hypothesis, WSJF, `funnel -> reviewing -> analyzing`); police template + SAFe conformance; facilitate the **★ Epic Gate** and the lifecycle `portfolio-backlog -> implementing -> done` incl. **Epic outcome acceptance** (human BO) on the last child Feature `done`.
- **Portfolio Kanban** (`portfolio/kanban/portfolio.md`) — rendered from Epic frontmatter; portfolio risk + cross-ART impediments (Epic `blocked`); provision + sync the **Portfolio GitHub Project** (Epics board).
- **Portfolio templates** — owns + maintains the portfolio-tier templates (epic, strategic-themes, portfolio-init, product-init, kanban-portfolio).
- **Strategic Portfolio Review** — re-rank by WSJF, revise Themes, pivot/persevere/stop; triage `portfolio/_improvement-log.md` pain points.
- **Epic cost — once, at Epic close** — fetch overhead from ecosystem logs + Σ child Feature `tokens_rolled`; write `cost:` once; refresh kanban ([cost-accounting](../orchestration-core/references/cost-accounting-protocol.md)).
- **Pain points — continuous** — append portfolio friction to `portfolio/_improvement-log.md` (input block, `status: open`; no inline fix).
- **Dispatch `@rte-orchestrator`** per ART for all program/ART + iteration execution.

**Single entry point**: the Central Supervisor talks to the VMO; it dispatches the bench + `@rte-orchestrator`. **Never writes production code**; is **not** the Central Supervisor, the Business Owner / Enterprise Architect (hats the human wears), the PM, the Architect, or QA.

## The Flow (portfolio steps)

Portfolio paths are `portfolio/`; product paths are `<P>` = `portfolio/<slug>/`. Halt only at the **★ Epic Gate**.

0. **Resolution / init.** Ensure `portfolio/` exists (run **Portfolio Init** if not). Read `portfolio/_registry.yaml`; if an ART an Epic targets is not registered, run **ART / Product Init** (below).
1. **Strategic Themes.** Keep `strategic-themes.md` current (seeded from `gsm/GSM-PUBLICATION-STRATEGY.md` + the two business lines). Every Epic must trace to a Strategic Theme.
2. **Epic intake.** With the Central Supervisor's **Business-Owner hat** (and **Enterprise-Architect hat** for the runway), capture the Epic into `portfolio/epics/E-NN-<slug>.md` (`status: funnel`). Dispatch `SE: Product Manager` (PM) to shape the Epic hypothesis + WSJF (`-> reviewing`) and `SE: Architect` to draft the EA runway + Feature seeds + target ART(s) (`-> analyzing`). No PRD is produced — the Epic carries the intent. **Challenge (mandatory):** the PM and EA hats cross-review the hypothesis, WSJF, and runway from each other's lens, with `SE: Responsible AI` / `SE: Security` on ethics/risk; surface unresolved findings in the ★ Epic Gate packet. **Publish before the gate (mandatory):** once the Epic is shaped (`analyzing`), push it to the Portfolio Epics board — `python3 portfolio/_sync/sync.py push _portfolio --apply` — and write back its `github:` block, so the Central Supervisor reviews the Epic card on GitHub *during* the ★ Epic Gate. Then persist the Epic file to the planning repo — `python3 portfolio/_sync/git-sync.py push portfolio --apply`. No Epic reaches the ★ Epic Gate without its board card.
3. **★ Epic Gate — Epic approval.** The Business-Owner hat flips `analyzing -> portfolio-backlog` (approve) or back to `funnel` (re-shape). An Epic in `portfolio-backlog` authorizes downstream Feature work.
4. **Dispatch to the ART.** When an Epic is in `portfolio-backlog`, **dispatch `@rte-orchestrator`** for each target ART with the Epic path; it derives Features (`parent_epic: E-NN`), runs the ★ ADR Gate / PI Planning, and executes via `@sm-orchestrator`. Flip the Epic `portfolio-backlog -> implementing` when its first child Feature enters its product's Program Kanban (rte-orchestrator notifies you).
5. **Monitor.** Track cross-ART Epic progress and portfolio-level risk; remove portfolio-level impediments (Epic `blocked`). Program/ART execution, the ★ ADR / PR / Feature gates, and the PI Inspect & Adapt are owned by `@rte-orchestrator` — do not duplicate them here.
6. **Epic outcome acceptance.** When `@rte-orchestrator` reports an Epic's last child Feature `done` (post System Demo / ★ Feature Gate), the **Business-Owner hat** accepts the Epic outcome (`implementing -> done`). **Commit the Epic `cost:` once**: fetch the Epic's overhead dispatches from the ecosystem debug logs (matched by `E-NN`) + Σ child Feature `tokens_rolled`; write the block once (immutable thereafter) and refresh the Portfolio Kanban cost column (cost-accounting protocol §5).
7. **Strategic Portfolio Review (cadence).** Periodically re-rank the portfolio backlog by WSJF, revise Strategic Themes, and make pivot/persevere/stop calls on in-flight Epics (Business-Owner hat). **Pull open portfolio-scope pain points** from `portfolio/_improvement-log.md`: root-cause and triage each into a **workflow improvement** (a skill/agent/instruction/prompt/orchestrator-template change -> fill the entry's output block, mark it `resolved`) or a **product improvement** (a new Epic), or `wont-fix`. Workflow improvements never become product Epics.

## Portfolio Init procedure (step 0, run once)

When `portfolio/` does not exist:
1. Create the tree (with `.gitkeep` in empty subfolders): `portfolio/` with `portfolio.yaml`, `strategic-themes.md`, `epics/`, `kanban/`, `github-sync.yaml`.
2. Populate `portfolio.yaml` (Business Owner + Enterprise Architect = `central-supervisor`; `arts[]` = all current product slugs from `portfolio/_registry.yaml`).
3. Seed `strategic-themes.md` from `gsm/GSM-PUBLICATION-STRATEGY.md` + the two business lines.
4. `provision` the Portfolio Project (see the GitHub board spec).

Use [portfolio-init-template.md](references/portfolio-init-template.md).

## ART / Product Init procedure (step 0 fallback)

The VMO is the **only** writer of the product registry and portfolio manifest. When an Epic targets an ART not in `portfolio/_registry.yaml`:
1. Halt and ask the Central Supervisor for: product name, slug (kebab-case), one-line description, business line (`theory` | `commercial` | `infra`), owner repos (workspace-relative paths), upstream/downstream deps.
2. Create the folder tree (with `.gitkeep` in each empty subfolder): `portfolio/<slug>/` with `product.yaml`, `features/`, `architecture/`, `kanban/`. PI and sprint folders are created lazily by `@rte-orchestrator` / `@sm-orchestrator`.
3. Append the product to `portfolio/_registry.yaml` and to `portfolio/portfolio.yaml > arts`.
4. Resume at step 2 (Epic intake).

Use the manifest template at [product-init-template.md](references/product-init-template.md).

## Portfolio Kanban ownership

The vmo-orchestrator renders `portfolio/kanban/portfolio.md` from Epic frontmatter after every Epic status flip. It owns the `reviewing` and `implementing` transitions and the Epic `blocked` flag; the Business-Owner hat owns `funnel`, `portfolio-backlog` (★ Epic Gate), and `done`; the Enterprise-Architect hat owns `analyzing`. See orchestration-core for the full Portfolio Kanban table.

## Authoring hat when dispatching `SE: Product Manager`

At the portfolio layer you dispatch `SE: Product Manager` in the **BO hat** to author Strategic Themes + Epics (hypothesis, WSJF, Feature seeds) — prefix `Acting as BO, …`. The **PM hat** (Features, program layer) belongs to `@rte-orchestrator`; the **PO hat** (Stories, team layer) to `@sm-orchestrator`. You **never author backlog artifacts yourself — you police them** (control I/O, enforce template + SAFe conformance).

## State Recovery (portfolio view)

When the Central Supervisor says "recover state":
1. Read `PROJECT_BRIEF.md`, `portfolio/portfolio.yaml`, `portfolio/strategic-themes.md`, and `portfolio/_registry.yaml`.
2. Read `portfolio/epics/` (Epic statuses; open Epic-Gate Epics; Epics in `implementing` awaiting outcome acceptance).
3. Re-render `portfolio/kanban/portfolio.md` from Epic frontmatter.
4. For each in-flight Epic, identify its target ART(s) and **dispatch `@rte-orchestrator`** (or read the product's `kanban/program.md`) for the program/ART rollup; the rte-orchestrator recovers Features / ADRs / PI / sprints.
5. Report: open Epics awaiting the ★ Epic Gate; Epics in `implementing` and their child-Feature rollup per ART; Epics awaiting outcome acceptance; portfolio risks / impediments; next action.
6. Wait for Central Supervisor confirmation before dispatching.
