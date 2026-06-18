# GitHub Projects board spec — SAFe/ART surface for Poesis

The **normative definition** of how the orchestration-core artifact model (Epic `E-NN` → Feature
`F-NN` → Story `S-NNN` — Epics portfolio-scoped under `portfolio/`, Features/Stories
product-scoped under `portfolio/<slug>/`) is mirrored onto GitHub Projects v2. This spec is the
single source of truth for board topology, issue model, field schema, status mappings, and board
views. The bidirectional sync toolchain (`portfolio/_sync/`) and its protocol
([github-sync-protocol.md](./github-sync-protocol.md)) implement exactly this spec.

> This **replaces** the legacy `def/features/` PlantUML feature-model sync and the
> `product-manager` skill's GitHub flow. Those are set aside; do not extend them.

## 1. Principles

- **Filesystem is the source of truth for content.** The committed markdown artifacts under
  `portfolio/<slug>/` author the *what*. GitHub Projects is the *human-facing board surface*
  for moving work and for items born on GitHub.
- **One ART per product, one portfolio above them.** Each product in `portfolio/_registry.yaml`
  is its own ART with exactly **one GitHub Project** (Program board + Team board) and **one
  planning repo**. Above them, a single cross-product **Portfolio Project** holds Epics.
- **Gates are never automated.** The board may *display* gate-pending columns; crossing a gate
  (Epic / ADR / PR / Feature) always requires Central Supervisor approval in chat. Sync never approves a
  gate (see §8).
- **Non-destructive.** Sync never deletes or closes items as a side effect. Removal is manual.

## 2. Topology (one Project + one planning repo per product, plus one Portfolio Project)

Org: **`poesis-cloud`**. Legacy Project #2 ("Poesis Product Features") is **archived**, not reused.

| Scope | Project title | Planning repo (`poesis-cloud/…`) | Sync config |
|---|---|---|---|
| `_portfolio` (Epics) | `Poesis — Portfolio` | `poesis-portfolio-planning` | `portfolio/github-sync.yaml` |
| `itip-web` | `Poesis — ITIP Web` | `itip-web-planning` | `portfolio/itip-web/github-sync.yaml` |
| `itip-blackboard-sourcer` | `Poesis — ITIP Blackboard Sourcer` | `itip-blackboard-sourcer-planning` | `portfolio/itip-blackboard-sourcer/github-sync.yaml` |
| `sie-blackboard` | `Poesis — SIE Blackboard` | `sie-blackboard-planning` | `portfolio/sie-blackboard/github-sync.yaml` |
| `sie-definition` | `Poesis — SIE Definition` | `sie-definition-planning` | `portfolio/sie-definition/github-sync.yaml` |

- The **planning repo** holds only Epic/Feature/Story **Issues** — it is *not* a code repo and is
  **never** added to `product.yaml > repos[]` (Story commits must not touch it).
- On provision, the resolved Project URL is written back to `product.yaml > github_project` (or
  `portfolio.yaml > github_project` for the Portfolio Project).

## 3. Org Issue Types (shared, org-level — provision once, **assigned to every issue**)

Configured once at org level (`poesis-cloud` → Settings → Issue Types), reused by every
planning repo. The sync **assigns the matching type to every issue** it creates/updates (via the
`updateIssueIssueType` GraphQL mutation), so the issue itself is classified — not only the
Project item.

| Issue Type | Maps to | Used for |
|---|---|---|
| `Epic` | Portfolio-layer Epic `E-NN` | one Issue per `portfolio/epics/E-*.md` |
| `Feature` | Program-layer Feature `F-NN` | one Issue per `portfolio/<slug>/features/F-*.md` |
| `Story` | Team-layer Story `S-NNN` | one Issue per `portfolio/<slug>/sprint-*/stories/S-*.md` |

`Feature` ships as a GitHub default type; `Epic` and `Story` are created by `provision` if absent
(`createIssueType`). Parentage is expressed natively via **sub-issues**: a Story Issue is a
sub-issue of its Feature Issue, and a Feature Issue is a sub-issue of its Epic Issue (when
`parent_epic` is set). Because Features and Epics live in **different planning repos**, the
Feature→Epic sub-issue link is cross-repo (supported by GitHub sub-issues). `ADR` Issue Types
remain **out of scope** (ADRs stay local-only, gated in chat).

## 3b. Status labels (`<type>:<status>` — synchronized onto every issue)

The Project status fields (§5) live *inside* a Project and are split by type, so they are not
visible on the issue itself or in cross-type issue lists/search. To make status **visible and
synchronized on the issue**, the sync maintains one lifecycle label per issue, namespaced by type:

| Type | Label namespace | Examples |
|---|---|---|
| Epic | `epic:<portfolio-column>` | `epic:funnel`, `epic:analyzing`, `epic:portfolio-backlog`, `epic:implementing`, `epic:done` |
| Feature | `feature:<program-column>` | `feature:funnel`, `feature:refined`, `feature:adr-pending`, `feature:ready`, `feature:committed`, `feature:in-progress`, `feature:done` |
| Story | `story:<team-column>` | `story:backlog`, `story:ready`, `story:in-progress`, `story:in-review`, `story:in-qa`, `story:awaiting-pr`, `story:done` |

Rules:
- The label set is **exactly** the kanban columns (§5), prefixed by the lowercase type. `provision`
  creates them in each planning repo (color-coded per type); the column lists stay authoritative
  in SKILL.md.
- On every push, the sync sets the single correct `<type>:<column>` label and removes any stale
  `<type>:*` status label. The orthogonal **`blocked`** flag is a separate `blocked` label applied
  alongside (never replacing) the status label — matching the rendered-kanban "Blocked
  (orthogonal)" semantics.
- These labels are the unified, cross-type status axis (one issue-list view shows every item's
  status regardless of type or Project). The Project status fields remain the board-grouping
  source; the labels mirror them onto the issues.

## 4. Project field schema (per Project)

The built-in `Status` field carries a **coarse `Todo` / `In Progress` / `Done` roll-up** of the
fine-grained lifecycle, so the Project's *default* board view (which always groups by built-in
`Status`) stays meaningful and synchronized. The authoritative, fine-grained status lives in the
type-specific single-select fields (`Portfolio Status` / `Program Status` / `Team Status`) so each
curated board groups by its own column set without overlap, and is mirrored onto issues as labels
(§3b). The coarse map (applied by the sync on push) is:

| Fine column (any of Portfolio/Program/Team) | built-in `Status` |
|---|---|
| `funnel`, `portfolio-backlog`, `backlog`, `refined`, `ready` | `Todo` |
| every mid-flight column (`reviewing`, `analyzing`, `implementing`, `adr-pending`, `committed`, `in-progress`, `in-review`, `in-qa`, `awaiting-pr`) | `In Progress` |
| `done` | `Done` |

**Generic SAFe fields** — those shared across Epic/Feature/Story — are namespaced with a `SAFe `
prefix; type-specific fields (status + structural links) stay unprefixed. GitHub Project field
names **cannot contain `:`**, so the namespace is a space (`SAFe Local ID`), never a colon.

| Field | Type | Options / format | Applies to | Source (frontmatter) |
|---|---|---|---|---|
| `Status` | single-select | `Todo`, `In Progress`, `Done` (built-in) | all (coarse roll-up) | derived from `status` |
| `Portfolio Status` | single-select | the Portfolio columns (§5) | Epic *(Portfolio Project)* | `status` |
| `Program Status` | single-select | the Program columns (§5) | Feature *(product Project)* | `status` |
| `Team Status` | single-select | the Team columns (§5) | Story *(product Project)* | `status` |
| `SAFe Type` | single-select | `Epic`, `Feature`, `Story` | all (generic) | derived from `id` prefix |
| `SAFe Local ID` | text | `E-NN` / `F-NN` / `S-NNN` | all (generic) | `id` — **identity anchor** |
| `SAFe Product` | text | product slug (Epics: comma-sep `products[]`) | all (generic) | `product` / `products` |
| `SAFe PI` | number | integer | generic (Feature, Story) | `pi` |
| `SAFe WSJF` | number | `wsjf.score` | generic (Epic, Feature) | `wsjf.score` |
| `SAFe Risk` | single-select | `low`, `medium`, `critical` | all (generic) | `risk` (optional) |
| `SAFe Complexity` | single-select | `simple`, `involved`, `complex` | all (generic) | `complexity` (optional) |
| `SAFe Gate` | single-select | `none`, `gate-epic`, `gate-adr`, `gate-pr`, `gate-feature` | all (generic) | derived from `status` (§8) |
| `Parent Epic` | text | `E-NN` | Feature *(type-specific)* | `parent_epic` |
| `Parent Feature` | text | `F-NN` | Story *(type-specific)* | `parent_feature` |
| `Strategic Theme` | text | theme id/name | Epic *(type-specific)* | `strategic_theme` |
| `Epic Type` | single-select | `business`, `enabler` | Epic *(type-specific)* | `type` |
| `Sprint` | number | integer | Story *(type-specific)* | `sprint` |
| `Estimate` | number | story points | Story *(type-specific)* | `estimate_points` |
| `Structurant` | single-select | `yes`, `no` | Feature *(type-specific)* | `structurant` |
| `Local Path` | text | repo-relative path | all *(sync bookkeeping)* | file path |

Each Project carries only the fields relevant to the items it holds: the **Portfolio Project**
uses `Portfolio Status` + Epic fields; each **product Project** uses `Program Status` /
`Team Status` + Feature/Story fields. The generic `SAFe *` fields appear on every Project.
Optional frontmatter (`risk`, `complexity`) absent on older artifacts is synced as empty and never
invented by the tool.


## 5. Status fields ↔ kanban columns

The `Portfolio Status`, `Program Status` and `Team Status` option sets are **exactly** the kanban
columns defined in orchestration-core — this spec does not redefine them or their meaning.
Authoritative sources:

- **Portfolio columns + Owner/Gate per column** — orchestration-core SKILL.md *§ Portfolio
  Kanban — Epics* table, and [epic-template.md](./epic-template.md) "Transition rules".
- **Program columns + Owner/Gate per column** — orchestration-core SKILL.md *§ Program Kanban —
  Features* table.
- **Team columns + Owner/Gate per column** — orchestration-core SKILL.md *§ Team Kanban —
  Stories* table.
- **Per-column transition triggers** — [feature-template.md](./feature-template.md) and
  [story-template.md](./story-template.md) "Transition rules" tables.

Binding rules specific to the board surface:

- The single-select options MUST equal those column lists verbatim, in order. They are restated
  for the tool only in each product's `github-sync.yaml > status_options` (the machine copy);
  if that list and the SKILL.md tables ever diverge, the **SKILL.md tables win** and the config
  is corrected.
- `blocked` is **not** an option — it is the orthogonal `blocked` label (§7), matching the
  rendered-kanban "Blocked (orthogonal)" semantics.

## 6. Board views (per Project)

| View | Layout | Column field | Filter | Sort |
|---|---|---|---|---|
| **Portfolio Board** *(Portfolio Project)* | board | `Portfolio Status` | `SAFe Type = Epic` | `SAFe WSJF` desc |
| **Program Board** | board | `Program Status` | `SAFe Type = Feature` | `SAFe WSJF` desc |
| **Team Board** | board | `Team Status` | `SAFe Type = Story` | `SAFe Local ID` asc |
| **Feature Table** | table | — | `SAFe Type = Feature` | `SAFe WSJF` desc |
| **PI Roadmap** *(optional)* | roadmap | — | — | `SAFe PI` asc |

The Team Board may be narrowed to the active sprint with an extra `Sprint = N` filter (a
per-sprint saved view), mirroring `kanban/team-sprint-N.md`.

The Project's auto-created **default board view** groups by the built-in `Status` field, i.e. the
coarse `Todo` / `In Progress` / `Done` roll-up (§4) — a useful at-a-glance lane even before the
curated views above are configured. The curated views group by the fine-grained
`Portfolio` / `Program` / `Team Status` fields.

## 7. Issue conventions

- **Title:** `E-NN — <title>` / `F-NN — <title>` / `S-NNN — <title>`. The id prefix is the
  human-readable identity anchor; the authoritative match is the `SAFe Local ID` field + state file.
- **Body:** generated from the markdown — Description + Acceptance criteria (Epic: hypothesis +
  outcome), plus a footer `<!-- poesis-sync: <local-id> | <path> -->` marker. The body is a
  *projection*; the markdown remains authoritative for content.
- **Sub-issue link:** each Story Issue is a sub-issue of its `parent_feature` Issue; each Feature
  Issue is a sub-issue of its `parent_epic` Issue when set (cross-repo, since Epics live in
  `poesis-portfolio-planning`).
- **`blocked`:** carried as the `blocked` label, not a column.

## 8. Gate handling (coherence with orchestration-core invariants)

A status transition that **crosses a gate boundary** is never auto-applied by sync in either
direction. Which columns are gate-bearing is defined by the **Gate** column of the kanban tables
in orchestration-core SKILL.md (and the Epic / ADR / Story / PR / Feature rows of its *Gates (summary)* table) — this
spec does not re-decide it. The `SAFe Gate` project field marks only the genuinely *awaiting-gate*
columns for the board (`analyzing → gate-epic`, `adr-pending → gate-adr`,
`awaiting-pr → gate-pr`); a `portfolio-backlog` / `done` item has already passed its gate, so
its `SAFe Gate` is `none`. The `→ portfolio-backlog` and `→ done` crossings are still gate-protected
by the sync independently of the display field (protocol §4).

Rules:
- **Local → remote:** sync may move a card *into* a gate-pending column (e.g. `awaiting-pr`,
  `analyzing`). It never moves a card *across* the gate (e.g. `→ portfolio-backlog`, `→ done`) —
  that only happens after the chat-side gate, then the local flip, then the next push.
- **Remote → local:** if a human drags a card *across* a gate boundary on the board (e.g.
  `analyzing → portfolio-backlog`, `awaiting-pr → done`, or `→ done`), `pull` treats it as a
  **request**: it is reported and recorded in `gate-decisions.md` (product) or
  `.sync-gate-requests.md` (portfolio), **not** written to local as approved. The Central
  Supervisor still approves the gate in chat; the orchestrator then performs the owner-only flip.

This preserves *No Gate skipping* and *Owner-only transitions* from orchestration-core.

## 9. Identity model

| Anchor | Where | Role |
|---|---|---|
| `id` (`E-NN`/`F-NN`/`S-NNN`) | markdown frontmatter | canonical key |
| `SAFe Local ID` field | Project item | remote mirror of the key |
| title prefix | Issue title | human-readable fallback match |
| `github:` block | markdown frontmatter | back-reference (issue #, node id, item id) |
| `items[]` map | `.sync-state.json` (product or `_portfolio`) | authoritative cross-reference + last-synced state |

Match order on sync: state file → `SAFe Local ID` field → title prefix → else **born-remote**
(materialize a new local artifact, §5 of the protocol).

## 9b. Issue-form templates (remote authoring, mirrors the references)

Each planning repo carries GitHub **issue forms** under `.github/ISSUE_TEMPLATE/` so a human can
author a conformant Epic/Feature/Story directly on GitHub (supporting the "defined remotely →
synced locally" path). The forms mirror the reference templates and pre-apply the type + initial
status label:

| Form file | Repo(s) | Mirrors | Pre-applies |
|---|---|---|---|
| `epic.yml` | `poesis-portfolio-planning` | [epic-template.md](./epic-template.md) | type `Epic`, label `epic:funnel`, title `E-NN — ` |
| `feature.yml` | `<slug>-planning` | [feature-template.md](./feature-template.md) | type `Feature`, label `feature:funnel`, title `F-NN — ` |
| `story.yml` | `<slug>-planning` | [story-template.md](./story-template.md) | type `Story`, label `story:backlog`, title `S-NNN — ` |

The form **body** captures the reference's key sections (hypothesis/description, acceptance
criteria, parent link, WSJF, risk/complexity). A remotely-authored issue is picked up by `pull`
as a born-remote item and materialized into a local stub for completion (protocol §5); the form
is an authoring aid, not a second source of truth. Forms are written via the GitHub contents API
(no local clone of the planning repos) and **converge on every push**: a drifted form is updated
in place so the remote always matches the canonical template.

## 10. Provisioning (idempotent)

`provision <slug|portfolio>` ensures, in order:
1. Org Issue Types `Epic`, `Feature`, `Story` exist (create `Epic`/`Story` if absent).
2. Planning repo (`<slug>-planning` or `poesis-portfolio-planning`) exists (private, issues
   enabled, no code).
3. The `<type>:<status>` lifecycle labels (§3b) + the `blocked` label exist in the planning repo.
4. The `.github/ISSUE_TEMPLATE/` issue forms (§9b) exist in the planning repo.
5. Project (`Poesis — <Name>` or `Poesis — Portfolio`) exists; capture its number + node id.
6. Custom fields (§4, generic ones `SAFe *`) for that Project's scope exist with the exact
  option sets (§5). Legacy pre-`SAFe` field names from older Projects are reconciled by the
  separate `migrate-fields` command: each is **renamed** in place to its `SAFe ` name, or
  **deleted** when the canonical `SAFe ` field already exists — so duplicate fields can never
  accumulate.
7. Board views (§6) exist.
8. `product.yaml > github_project` (or `portfolio.yaml > github_project`) and the `.sync-state.json`
   are updated.

All steps are idempotent (create-if-absent / rename-if-old / delete-stale-duplicate) and support
`--dry-run`. See the protocol for the command surface and run order.
