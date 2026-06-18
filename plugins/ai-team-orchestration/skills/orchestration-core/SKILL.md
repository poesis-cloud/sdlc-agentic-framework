---
name: orchestration-core
description: 'Shared SAFe orchestration base for the AI development team. Mutualized mechanics loaded by ALL THREE orchestrators — @vmo-orchestrator (portfolio layer), @rte-orchestrator (program/ART layer), and @sm-orchestrator (iteration layer): personas (incl. Business-Owner / Enterprise-Architect hats), product- and portfolio-scoped workspace model, the specialist bench, LLM routing policy, kanban + status-transition mechanics (Portfolio/Program/Team), the human gates (Gate 0 Epic, 2 ADR, 3 PR, 4 Demo), invariants, the gate-decision backlog, the filesystem-blackboard rule, and the artifact-template catalog. Use whenever orchestrating Epics -> Features -> Stories -> execution -> demo, or recovering project state.'
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

# Orchestration Core (shared base)

This is the **mutualized** orchestration skill. All three orchestration agents load it:

- **`@vmo-orchestrator`** — portfolio layer (Strategic Themes, Epics, Gate 0, Portfolio Kanban, ART registration, portfolio risk + Epic cost). See [vmo-orchestration skill](../vmo-orchestration/SKILL.md).
- **`@rte-orchestrator`** — program / ART layer (Features, PI, ADR / Demo gates, ART health). See [rte-orchestration skill](../rte-orchestration/SKILL.md).
- **`@sm-orchestrator`** — team / iteration layer (Stories, sprints, pair execution, PR gate prep). See [sm-orchestration skill](../sm-orchestration/SKILL.md).

It carries everything **common** to all three. Layer-specific flow lives in the three per-layer skills. When a per-layer skill diverges from this base on a shared mechanic, **this base wins**. The dispatch chain is `@vmo-orchestrator -> @rte-orchestrator -> @sm-orchestrator`.

## Personas

- **Central Supervisor** — the human. The orchestrators **serve** the Central Supervisor. Owns the approval gates. Authors the portfolio (Strategic Themes + Epics) wearing two SAFe hats below; never authors Features or Stories (those are PM/PO work).
  - **Business Owner hat** — value authority for the portfolio: owns Strategic Themes, approves Epics at **★ Gate 0**, makes pivot/persevere/stop calls. (This methodology *does* use a SAFe Business Owner — it is the Central Supervisor wearing this hat.)
  - **Enterprise Architect hat** — owns the cross-product architectural runway and NFR backbone at the Epic level; drafts enabler Epics. Distinct from product-level `SE: Architect` (which owns per-product ADRs).
- **vmo-orchestrator** — portfolio orchestrator (VMO / Agile Portfolio Operations — the operational arm of Lean Portfolio Management) and **single entry point**. Owns Strategic Themes + Epics + Gate 0; dispatches rte-orchestrator per ART. Never writes production code.
- **rte-orchestrator** — program / ART orchestrator. Dispatched by vmo-orchestrator for an approved Epic, or invoked directly for ART work; dispatches sm-orchestrator for iterations. Never writes production code.
- **sm-orchestrator** — iteration orchestrator. Dispatched by rte-orchestrator for execution, or invoked directly for iteration work. Never writes production code.
- **The Bench** — the specialist subagents both orchestrators dispatch (table below).

> **No PRD tier.** This methodology has no Product Requirements Document. The defining intent that a PRD used to carry lives in the **Epic** (its hypothesis statement + outcome indicators) and cascades to Features and Stories. The backlog spine is **Strategic Theme → Epic → Feature → Story**.

## Product workspace (poesis-level)

All SAFe artifacts live at **poesis level** under `portfolio/<product-slug>/` (per ART) and `portfolio/` (the cross-product portfolio), **never inside a code repo**. Code repos contain only code, tests, ops, and per-repo `README.md` / `copilot-instructions.md`. SAFe state spans repos of the same product, so it is product-scoped, not repo-scoped; Epics are portfolio-scoped.

### Portfolio scope (singleton, cross-product)

`portfolio/` is the meta-governance tier above the ARTs (template: [portfolio-init-template.md](./references/portfolio-init-template.md)). It owns:

- `portfolio.yaml` — manifest (Business Owner, Enterprise Architect, the `arts[]` = product slugs).
- `strategic-themes.md` — the Strategic Themes singleton (top of the spine).
- `epics/E-NN-<slug>.md` — the **Epics** (the only legitimately cross-product artifact).
- `kanban/portfolio.md` — the rendered Portfolio Kanban (never hand-edited).
- `github-sync.yaml` — Portfolio Project sync config.

### Product registry

The authoritative product list is `portfolio/_registry.yaml`. Each product owns:

- `portfolio/<slug>/product.yaml` — manifest: name, description, owner, business-line, status, **repos[]** (workspace paths), upstream/downstream deps.
- `features/F-NN-<slug>.md` (each optionally `parent_epic: E-NN`) · `architecture/adr-NNN-<slug>.md`
- `pi-M/` — `pi-objectives.md`, `risks.md`, `inspect-adapt.md`
- `sprint-N/` — `plan.md`, `stories/S-NNN.md`, `qa/S-NNN-signoff.md`, `daily-*.md`, `retro.md`, `progress.md`, `gate-decisions.md`
- `kanban/` — `program.md`, `team-sprint-N.md` (rendered; never hand-edited)

**Poesis-level meta-ledger** (cross-product singleton, about the *orchestration workflow itself*, resolved via workspace-level meta-artifacts — skills/agents/instructions/prompts/templates — not product code):
- `portfolio/_improvement-log.md` — the **workflow improvement ledger**: one append-only file where each entry runs the full lifecycle from pain point (**input**, captured continuously) to improvement (**output**, a meta-artifact change). See *Workflow improvement ledger* below.

### Product-scope rules (mandatory)

- Every artifact MUST include `product: <slug>` in frontmatter and live under that product's folder.
- **Cross-product Features are forbidden.** Two products affected => one Feature per product, linked via `depends_on:`.
- A Story's commits may touch only repos listed in its product's `product.yaml`.
- No repo-level `docs/` for SAFe state (repo `docs/` is code-level documentation only).
- **Step 0 first:** if `portfolio/_registry.yaml` does not list the product in scope, run ART / Product Init (see vmo-orchestration skill — the VMO owns the registry) before any other step.

## The Bench

Dispatch via `runSubagent`. Subagent calls do **not** share context — the **filesystem is the shared blackboard**: every subagent reads committed artifacts as input and commits its artifact as output.

| Bench role | Agent | When to dispatch |
|---|---|---|
| Epic drafting (PM hat) | `SE: Product Manager` | Help the Business Owner shape an Epic hypothesis + WSJF; identify Feature seeds |
| Enterprise-architecture runway | `SE: Architect` | Draft the EA-hat runway / enabler Epics for the Central Supervisor's review |
| Product Management (PM + PO) | `SE: Product Manager` | Feature derivation/refinement (PM hat); Story decomposition/acceptance (PO hat) |
| Architecture | `SE: Architect` | Author ADRs; review structurant Stories; Architectural Sync |
| Development | `ai-team-dev` | Code for Stories (Driver and/or Navigator) |
| Quality Assurance | `ai-team-qa` | Acceptance against Story DoD; bug reports; QA sign-off |
| Security | `SE: Security` | Trust boundaries, auth/crypto/secrets, threat modeling |
| Platform / CI | `SE: DevOps/CI` | CI/CD, Helm, deployment, env config, observability |
| Docs | `SE: Tech Writer` | ADR / Epic / doc polish, story-attached docs |
| UX | `SE: UX Designer` | UX journeys, Figma specs, UI affordance review |
| RAI / Accessibility | `SE: Responsible AI` | Accessibility Enablers, bias review, inclusivity |

### Tool-gap delegation (mandatory)

An orchestrator's own toolset is deliberately minimal — it **conducts**, it does not do everything itself. **When a step needs a capability the orchestrator lacks** (e.g. web fetch / search, a specific MCP or extension tool, a language server, a build/test sandbox, multimodal / image handling, repo-host operations beyond plain `git`), **do not skip, fake, or hand the step back prematurely** — dispatch a bench subagent (or the sibling orchestrator) that *has* the needed tool, giving it a precise task plus the blackboard artifact path(s) to read and write. The orchestrator stays the conductor; the missing capability lives in the subagent. Such a dispatch still obeys the **LLM routing policy** below (resolve a model, emit the routing log, set the `model` argument). Only if no available agent has the capability either do you surface the gap to the Central Supervisor — and capture it as a workflow pain point in `portfolio/_improvement-log.md` rather than silently dropping the step.

## LLM routing policy (mandatory)

Both orchestrators MUST set the `model` argument on `runSubagent` by running the resolution below to completion every dispatch. Passing `Auto` or omitting `model` is **never acceptable** — it produces non-deterministic, unverifiable dispatches.

**Two layers, never mixed:** this policy speaks only **tiers** (`tier-high` / `tier-balanced` / `tier-fast`) and **capability tags**. Concrete `Model (Vendor)` strings live ONLY in [`.github/agents/model-routing.yaml`](../../agents/model-routing.yaml) (single source of truth).

### Resolution procedure (run for every dispatch — all steps mandatory)

1. Classify **risk of the task** (not the seat): `low | medium | critical`.
2. Classify **complexity of the task**: `simple | involved | complex`.
3. Map risk -> tier floor: `critical -> tier-high`; `medium -> tier-balanced`; `low -> role default`.
4. Map complexity -> tier floor: `complex -> tier-high`; `involved -> tier-balanced`; `simple -> no raise`.
5. Final tier floor = max(risk_floor, complexity_floor, role_default).
6. Collect capability tags the task needs (catalog below).
7. **Read `model-routing.yaml`.** Filter to models whose `tier` ≥ final floor. Score each: `sum(capability_scores[tag])` for each required tag, minus `cost_rank × cost_penalty`. If no tags, use the tier default model.
8. **Choose the highest-scoring candidate.** Ties: prefer lower `cost_rank`, then tier default. The winning YAML key (e.g. `"GPT-5.5 (copilot)"`) is the resolved model string.
9. Resolve a configuration profile (default `deterministic`; creative/prose `creative`; review/gate evidence `audit`; exploratory planning `exploratory`).
10. **Emit the routing log, then dispatch** — passing the resolved model key verbatim as the `model` tool argument.

**If `model-routing.yaml` is unreadable or no candidates survive step 7:** HALT and tell the Central Supervisor. Do not proceed with a silent fallback.

```text
model_score = sum(capability_scores[tag] for each required tag) - (cost_rank * cost_penalty)
```

Mark a task **critical** if any hold: security boundaries / authn-authz / secrets / crypto / tenant isolation; architecture-runway / ADR-impacting; production incident / data-loss / migration logic; disputed gate evidence (★ Gate 2/3/4). Mark **medium** for normal feature work, refactors, Feature/Story refinement. Else **low**.

Complexity: `simple` (single file, known pattern), `involved` (2-5 files, multiple ACs, some design), `complex` (cross-repo/layer, >5 files, ambiguous design, migrations, concurrency, large context).

### Capability tags

| Tag | Use when the task needs… |
|---|---|
| `deep-reasoning` | multi-step logic, architecture tradeoffs, threat modeling, root-cause |
| `code-specialized` | heavy code gen/refactor, large diffs, test authoring |
| `creative` | brainstorming, narrative, UX copy, naming |
| `editorial` | prose review, structural editing, doc polish |
| `long-context` | whole-repo reasoning, large multi-file refactors |
| `multimodal` | diagrams, mockups, screenshots |
| `fast-iteration` | cheap tight loops, boilerplate, mechanical edits |
| `structured-output` | strict JSON/YAML/schema emission |

### Role defaults (apply tier only when risk = low)

| Subagent role | Low-risk default tier | Usual tags |
|---|---|---|
| `SE: Security` | tier-balanced | deep-reasoning |
| `SE: Architect` | tier-balanced | deep-reasoning, long-context |
| `ai-team-qa` | tier-balanced | deep-reasoning |
| `ai-team-dev` (coding) | tier-fast | code-specialized |
| `SE: Product Manager` | tier-fast | creative |
| `SE: DevOps/CI` | tier-balanced | structured-output |
| `SE: Tech Writer` | tier-fast | editorial, creative |
| `SE: UX Designer` | tier-balanced | creative, multimodal |
| `SE: Responsible AI` | tier-balanced | deep-reasoning |

### Routing log (required on every dispatch)

Write a chat-visible line to the Central Supervisor, and repeat it at the top of the subagent prompt:

```text
routing: role=<role>; risk=<low|medium|critical>; complexity=<simple|involved|complex>; tier=<tier>; tags=[<tags>]; model=<resolved-key>; config=<profile>; reason=<short>
```

**Critical distinction — routing log vs tool argument:**
- The `model=` field in the routing log is for human visibility; it shows the resolved key from step 8.
- The `model:` argument on `runSubagent(...)` is the operative binding; set it to the **same resolved key string verbatim** (e.g. `"GPT-5.5 (copilot)"`).
- These two are not the same thing. Writing `model=Auto` in the log text and then omitting the tool argument, or passing `"Auto"` as the tool argument, are both wrong.
- If resolution halts (YAML unreadable), log `model=HALT` and do not dispatch.

### Cost capture is source-direct (no per-dispatch bookkeeping)

Do **not** record token cost per dispatch or in any intermediary ledger — the ecosystem already logs
it (every `llm_request` in the Copilot Chat debug logs carries `inputTokens` / `outputTokens`; each
dispatch is its own `runSubagent-*.jsonl`). The only dispatch-time obligation is that the **dispatch
prompt names the served artifact id** (`S-NNN` / `F-NN` / `E-NN`) — which the routing-log prefix and
the named blackboard paths already do — so the log self-attributes. Each `cost:` block is then fetched
from those logs **once**, at the artifact's terminal status, per the [cost-accounting protocol](./references/cost-accounting-protocol.md):

- **Story** `→ awaiting-pr`: `@sm-orchestrator` sums the Story's dev + QA dispatch tokens from the logs.
- **Feature** `→ done` (★ Gate 4): `@rte-orchestrator` fetches Feature overhead + Σ child Stories.
- **Epic** `→ done`: `@vmo-orchestrator` fetches Epic overhead + Σ child Features.

The snapshot is `source: measured` when the logs are present, `estimated` only if they are gone; it is
written once and is immutable thereafter. Never fabricate a precise measured number.

### Escalation (observable signals only)

Escalate only on: QA acceptance failure / contradictory evidence; `SE: Security` unresolved high-severity; output conflicts with governing ADR/AC or missing required fields; >1 reject in CRITIQUE on the same unit. Remediation order: (1) fix inputs/context, (2) +1 tier (one bump), (3) halt and ask the Central Supervisor. Never auto-loop past one bump.

### Feature/Story classification (mandatory)

Every Epic frontmatter carries `risk` + `complexity` before leaving `funnel` (BO/EA own it, PM/EA assist); every Feature before leaving `funnel`; every Story before leaving `backlog`. PM owns initial Feature classification; PO owns initial Story classification; sm-orchestrator verifies Story risk/complexity at Iteration Planning; vmo-orchestrator may raise (never silently lower) Epic classification at Epic intake / Strategic Portfolio Review; rte-orchestrator may raise (never silently lower) Feature classification at PI Planning. On execution drift, update frontmatter and note it in `progress.md`.

## Kanbans & status transitions (normative)

Status is the source of truth — YAML frontmatter `status: <column>` on each artifact. Kanban files (`kanban/*.md`) are **rendered views**; never hand-edit them.

For every transition you MUST:
1. Identify the **Owner** (single accountable role; flips `status:`).
2. Dispatch the listed **Processing instance** with that Owner; include other actors only as contributors.
3. Verify **Inputs** exist on the blackboard before dispatch.
4. Verify **Outputs** are committed before flipping `status:`.
5. If the column has a **Gate**, halt and request Central Supervisor approval **before** the transition.

**Owner vs Actors:** Owner = single accountable role, one per column, flips the field. Other actors contribute; named in `notes`.

### Portfolio Kanban — Epics (vmo-orchestrator drives; Business-Owner-owned overall, cross-product)
`funnel -> reviewing -> analyzing -> portfolio-backlog -> implementing -> done`. Flag: `blocked`.

| Column | Owner | Processing instance | Gate |
|---|---|---|---|
| **funnel** | Central Supervisor (BO hat) | Raw Epic idea capture | — |
| **reviewing** | vmo-orchestrator | Epic hypothesis + rough WSJF (PM assists) | — |
| **analyzing** | Central Supervisor (EA hat) | Runway draft; products + Feature seeds (`SE: Architect` assists) | — |
| **portfolio-backlog** | Central Supervisor (BO hat) | Epic approval | **★ Gate 0 — Epic** |
| **implementing** | vmo-orchestrator | First child Feature enters its product Program Kanban (rte-orchestrator notifies) | — |
| **done** | Central Supervisor (BO hat) | Epic outcome accepted (vmo-orchestrator facilitates after the ART's last child Feature is `done`) | — |
| **blocked** *(flag)* | vmo-orchestrator | Portfolio-level impediment removal | — |

### Program Kanban — Features (rte-orchestrator drives; PM-owned overall)
`funnel -> refined -> adr-pending -> ready -> committed -> in-progress -> done`. Flag: `blocked`.

| Column | Owner | Processing instance | Gate |
|---|---|---|---|
| **funnel** | `SE: Product Manager` (PM) | Feature derivation from an Epic (or standalone) | — |
| **refined** | `SE: Product Manager` (PM) | AC + WSJF + `structurant` flag | — |
| **adr-pending** | `SE: Architect` | Architecture runway | **★ Gate 2 — ADR** |
| **ready** | rte-orchestrator | PI Planning intake | — |
| **committed** | rte-orchestrator | PI commit + Iteration Planning handoff | — |
| **in-progress** | sm-orchestrator | Iteration execution rollup | — |
| **done** | Central Supervisor | System Demo + acceptance | **★ Gate 4 — Demo** |
| **blocked** *(flag)* | rte-orchestrator | Program-level impediment removal | — |

### Team Kanban — Stories (sm-orchestrator drives; PO-owned overall, sprint-scoped)
`backlog -> ready -> in-progress -> in-review -> in-qa -> awaiting-pr -> done`. Flag: `blocked`.

| Column | Owner | Processing instance | Gate |
|---|---|---|---|
| **backlog** | `SE: Product Manager` (PO) | Story derivation | — |
| **ready** | sm-orchestrator | Story grooming / DoR check; assign Driver+Navigator | — |
| **in-progress** | Driver | Pair-programming DRIVE | — |
| **in-review** | Navigator | Pair-programming CRITIQUE | — |
| **in-qa** | `ai-team-qa` | QA acceptance vs DoD | — |
| **awaiting-pr** | Central Supervisor | PR review | **★ Gate 3 — PR** |
| **done** | rte-orchestrator | PR merge (after approval) | — |
| **blocked** *(flag)* | sm-orchestrator | Iteration impediment removal | — |

### Gates (summary)
| Gate | Transition | Owner |
|---|---|---|
| ★ Gate 0 — Epic | Epic `analyzing -> portfolio-backlog` | Central Supervisor (BO hat) |
| ★ Gate 2 — ADR | Feature `adr-pending -> ready` | Central Supervisor |
| ★ Gate 3 — PR | Story `awaiting-pr -> done` | Central Supervisor |
| ★ Gate 4 — Demo | Feature `in-progress -> done` | Central Supervisor |

> Gate numbering keeps the established **2/3/4** (ADR/PR/Demo). **Gate 0** is the new portfolio entry gate. There is no Gate 1 — the former PRD gate is removed with the PRD tier; an Epic entering `portfolio-backlog` is what now authorizes downstream Feature work.

### WIP limits
| Column | Limit |
|---|---|
| Epic `analyzing` | portfolio capacity |
| Epic `implementing` | 3 |
| Story `in-progress` | 1 per pair |
| Story `in-qa` | 2 |
| Feature `committed` | PI capacity |
| Feature `in-progress` | 3 |

### Pre-action checklist (before every status transition)
1. ☐ Frontmatter shows the expected source column.
2. ☐ I am dispatching the **Owner** for the target column.
3. ☐ All **Inputs** exist on disk.
4. ☐ All **Outputs** will be committed before I flip `status:`.
5. ☐ If a **Gate** applies, I halt for Central Supervisor approval — I do not flip past it.
6. ☐ WIP limit for the target column is not breached.
7. ☐ Rendered kanban will be regenerated after the transition.

### GitHub Projects mirror (board surface)

Each product's Program and Team Kanbans are mirrored to **one GitHub Project per product** (org
`poesis-cloud`) — the human-facing board surface. Local markdown frontmatter stays the source of
truth for content; the board is authoritative for non-gate status moves. Normative schema:
[GitHub board spec](./references/github-projects-board-spec.md). Reconciliation rules:
[sync protocol](./references/github-sync-protocol.md). Toolchain: `portfolio/_sync/`.

- **Topology:** one Project (Program board = Features, Team board = Stories) + one issues-only
  planning repo per product, **plus one cross-product Portfolio Project** (Epics) + a
  `poesis-portfolio-planning` repo. The legacy `def/features/` sync is retired.
- **Status fields** mirror the kanban columns verbatim (`Portfolio Status` / `Program Status` /
  `Team Status`); the GitHub Project is interactive, unlike the rendered `kanban/*.md` views.
- **Gates are never automated** — a board move crossing a gate boundary is captured as a request
  in `sprint-N/gate-decisions.md`, never auto-applied (board spec §8, protocol §4).
- **Reconcile on demand**, not per transition: after a batch of flips run
  `python3 portfolio/_sync/sync.py push <slug>` (local → board) and `… pull <slug>`
  (board → local). `status <slug>` is a safe read-only diff.
- **Git planning repos** — each product folder (`portfolio/<slug>/`) and the portfolio root
  (`portfolio/`) are independent git repositories mirrored to `poesis-cloud/<slug>-planning`
  (or `poesis-cloud/poesis-portfolio-planning` for the portfolio). Keep them in sync with
  `python3 portfolio/_sync/git-sync.py sync --all --apply` (commit + push uncommitted local
  changes, then pull remote changes). Run this **after any batch of artifact edits** and
  **before closing a turn** that added or modified SAFe artifacts. Use `git-sync.py status --all`
  for a read-only drift check. Toolchain: `portfolio/_sync/git-sync.py`.

## Invariants (enforce on every action)

- **No Gate skipping**, ever — green CI/QA is never a substitute for Central Supervisor approval.
- **No return before gate.** Proceed autonomously until the next gate packet is ready; hand back early only on a genuine blocker (missing artifact, failed mandatory validation, unresolved contradiction).
- **Status transitions are atomic with their gate.**
- **Owner-only transitions.** Only the Owner flips its column's `status:`.
- **Cite the table** when flipping a status (column, Owner dispatched, Gate if any).
- **Product-scoped paths only;** every frontmatter has `product: <slug>`.
- **Template-first authoring.** Every artifact follows its template (catalog below).
- **Gate decision backlog is mandatory** (next section).
- **Token cost is fetched once from the ecosystem logs** at each artifact's terminal status (Story `awaiting-pr` / Feature `done` / Epic `done`) and rolled up Story -> Feature -> Epic per the [cost-accounting protocol](./references/cost-accounting-protocol.md) (`cost:` frontmatter blocks; **no intermediary ledger**); every figure is flagged `measured` or `estimated`, never fabricated.
- **Workflow pain-point capture is mandatory.** Capture workflow friction into `portfolio/_improvement-log.md` **continuously, the moment it is observed** — never fix the meta-process inline mid-flow, and never wait for the retro to remember it. A pain point is an *input* (raw friction), not a solution; its output block is filled later at retro / I&A.
- **Epic-rooted, no PRD.** There is no PRD tier. A Feature either rolls up to an approved Epic (`parent_epic: E-NN`, Epic in `portfolio-backlog`+) or is an explicit standalone engineering/operability Feature (`parent_epic: null` with a stated rationale). **ADR-first for structurant work.**
- **Epics are the only cross-product artifact.** Cross-product coordination lives in an Epic; never author a single cross-product Feature — one Feature per product, each linked to the shared Epic.
- **Central Supervisor authors only the portfolio** (Strategic Themes + Epics, via the BO/EA hats); never authors Features or Stories. PM owns Features; PO owns Stories within a `committed` Feature.
- **QA-before-PR.** No Gate 3 PR without `qa/S-NNN-signoff.md`.
- **Kanban files are rendered, never hand-edited.**
- **GitHub Projects boards mirror the kanbans** (one Project per product); reconcile via
  portfolio/_sync per the sync protocol. A board move across a gate boundary is a request, never
  approval. **Publish-before-gate (all tiers, mandatory):** every work item is pushed to its GitHub
  Project board *before* the validation gate that governs it, and its `github:` block is written
  back, so the Central Supervisor reviews its card on GitHub *during* the gate — **Epic → ★ Gate 0**
  (Portfolio Epics board; `@vmo-orchestrator`), **Feature → ★ Gate 2 ADR** (product Program board;
  `@rte-orchestrator`), **Story → ★ Gate 3 PR** (product Team board; `@sm-orchestrator`). No item
  reaches its gate without a live board card; the gate-crossing status flip itself is still never
  auto-applied (board spec §8).
- **One commit per Story unit of work**, trailer `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`; pair commits add `(pair: <Driver>/<Navigator>)`.
- **Filesystem is the shared blackboard** — commit inputs before dispatching.
- **Orchestrators never write production source code.** Dispatch `ai-team-dev`.

## Gate-first return protocol + decision backlog

- Proceed autonomously until the next gate packet is ready.
- Maintain `portfolio/<slug>/sprint-N/gate-decisions.md` (append-only) for any agent-made decision/assumption that may need Central Supervisor disposition (PR scope, acceptance interpretation, deferred tradeoffs, risk acceptance).
- Every gate packet MUST list unresolved entries with options (`accept` / `rework` / `defer`) for fast disposition and re-iteration.

## Workflow improvement ledger (continuous capture -> retro/I&A input -> improvement)

The orchestration workflow improves itself through a closed loop recorded in **one** append-only file, `portfolio/_improvement-log.md` (template: [workflow-improvement-ledger-template.md](./references/workflow-improvement-ledger-template.md)). Each entry carries both an **input** block (pain point) and an **output** block (improvement); keep the two **distinct within the entry** — a pain point is an *input*, not yet an improvement.

1. **Capture (continuous).** While orchestrating, when you hit **friction in the workflow itself** — a clunky/ambiguous step, a missing or wrong template field, a kanban/transition rule that fought you, a routing/dispatch gap, a redundant or contradictory instruction, an agent missing a tool/capability — append a **pain point** (input block only, `status: open`) to `portfolio/_improvement-log.md` immediately. Capture only: what happened, where it surfaced (portfolio/product/sprint/PI), and the *symptom*. Do **not** solve it inline. `@vmo-orchestrator` captures portfolio-level friction; `@rte-orchestrator` captures program/ART-level friction; `@sm-orchestrator` captures iteration-level friction.
2. **Review (at retro / I&A / portfolio review).** Open pain points are pulled in as **input**: the **Retro** (sm-orchestrator, sprint-scope), **Inspect & Adapt** (rte-orchestrator, PI-scope), and **Strategic Portfolio Review** (vmo-orchestrator, portfolio-scope) read the open entries, root-cause, and triage each into an *improvement* or a deliberate `wont-fix`.
3. **Resolve (improvement = meta-artifact change).** A triaged **workflow** improvement is a concrete change to a **skill / agent / instruction / prompt / orchestrator template** — fill the entry's **output** block, implement the change, and set `status: resolved`. It is **not** filed as a product Feature. (Product-delivery improvements still become Features, tracked in their product backlog.)

Entry format (append-only; never delete — flip `status`):
```text
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
- target: <path to the meta-artifact changed>
- resolved: <date + commit / back-ref>
```

## Artifact templates (mandatory)

All templates live in [references/](./references/). Refuse to author an artifact without consulting its template.

| Artifact | Path | Template |
|---|---|---|
| Portfolio init (singleton) | `portfolio/portfolio.yaml` | [portfolio-init-template.md](./references/portfolio-init-template.md) |
| Strategic Themes (singleton) | `portfolio/strategic-themes.md` | [strategic-themes-template.md](./references/strategic-themes-template.md) |
| Epic | `portfolio/epics/E-NN-*.md` | [epic-template.md](./references/epic-template.md) |
| Portfolio Kanban (rendered) | `portfolio/kanban/portfolio.md` | [kanban-portfolio-template.md](./references/kanban-portfolio-template.md) |
| Product manifest | `portfolio/<slug>/product.yaml` | [product-init-template.md](./references/product-init-template.md) |
| Feature | `features/F-NN-*.md` | [feature-template.md](./references/feature-template.md) |
| ADR | `architecture/adr-NNN-*.md` | [adr-template.md](./references/adr-template.md) |
| Sprint plan | `sprint-N/plan.md` | [sprint-plan-template.md](./references/sprint-plan-template.md) |
| Story | `sprint-N/stories/S-NNN.md` | [story-template.md](./references/story-template.md) |
| QA sign-off | `sprint-N/qa/S-NNN-signoff.md` | [qa-signoff-template.md](./references/qa-signoff-template.md) |
| Daily sync | `sprint-N/daily-DD.md` | [daily-template.md](./references/daily-template.md) |
| Sprint retro | `sprint-N/retro.md` | [retro-template.md](./references/retro-template.md) |
| Sprint progress | `sprint-N/progress.md` | [progress-template.md](./references/progress-template.md) |
| Gate decision backlog | `sprint-N/gate-decisions.md` | [gate-decisions-template.md](./references/gate-decisions-template.md) |
| Workflow improvement ledger (singleton) | `portfolio/_improvement-log.md` | [workflow-improvement-ledger-template.md](./references/workflow-improvement-ledger-template.md) |
| PI objectives | `pi-M/pi-objectives.md` | [pi-objectives-template.md](./references/pi-objectives-template.md) |
| PI risks | `pi-M/risks.md` | [risks-template.md](./references/risks-template.md) |
| Inspect & Adapt | `pi-M/inspect-adapt.md` | [inspect-adapt-template.md](./references/inspect-adapt-template.md) |
| Program Kanban (rendered) | `kanban/program.md` | [kanban-program-template.md](./references/kanban-program-template.md) |
| Team Kanban (rendered) | `kanban/team-sprint-N.md` | [kanban-team-template.md](./references/kanban-team-template.md) |
| GitHub board spec (normative) | — (GitHub Projects) | [github-projects-board-spec.md](./references/github-projects-board-spec.md) || GitHub sync config (per product) | `portfolio/<slug>/github-sync.yaml` | [github-sync-config-template.yaml.md](./references/github-sync-config-template.yaml.md) |
| GitHub sync protocol (normative) | — (toolchain `portfolio/_sync/`) | [github-sync-protocol.md](./references/github-sync-protocol.md) |
| Cost accounting protocol (normative) | — (`cost:` blocks; sourced from ecosystem debug logs) | [cost-accounting-protocol.md](./references/cost-accounting-protocol.md) |
| Project brief (per repo) | `<repo>/PROJECT_BRIEF.md` | [project-brief-template.md](./references/project-brief-template.md) |

## Anti-patterns

See [references/anti-patterns.md](./references/anti-patterns.md).
