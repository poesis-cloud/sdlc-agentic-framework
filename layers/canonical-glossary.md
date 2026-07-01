# Canonical Orchestration Terminology

This file is the **single, canonical source** for the SAFe-agentic-framework orchestration
vocabulary. When any framework artifact (skill, workflow, schema, log, harness, instruction,
memory) refers to these concepts it MUST use the canonical term below and no synonym. Older
synonyms are listed only to support the in-flight rename; new content must not introduce them.

## Terms

| Canonical term | Definition | Replaces (do not use) |
|---|---|---|
| **orchestration** | A unit that **delivers artifacts** by following a *workflow* step by step, emitting one *log* per step, and running the *harness* at each step. Two ranks: *root orchestration* and *suborchestration*. | "orchestrator skill", "orchestration layer" |
| **root orchestration** | One of the three layer orchestrations — `lpm`, `art`, `scrum`. Drives a unit FSM (Epic / Feature / Story); each *structurant step* either commits a transition directly, delegates to a *suborchestration*, or stages a ★ gate. `orchestrator` is **not** an orchestration — it is the shared library (harness, base log schema, this glossary). | "orchestrator", "the layer", "router skill" |
| **suborchestration** | A facilitated, multi-participant orchestration nested under `<root-orchestration>/workflows/<name>/`. Loaded by its parent root orchestration via **explicit path** (not auto-discovery). The SAFe sub-kind (ceremony vs practice) survives only as the `kind:` field inside the workflow — it is no longer a noun, folder, or naming distinction. | "ceremony", "practice", "sub-orchestration", "handler (skill)" |
| **role** | An authoring hat (BO / PM / PO / EA / SA) loaded *inside* a suborchestration by a dispatched agent. Roles live under their layer's actors folder (`layers/<portfolio\|program\|team>/actors/<name>/`). A role is **not** an orchestration. | "author skill", "author hat skill" |
| **workflow** | The single `workflow.yaml` (one `workflow:` root node) in an orchestration folder that declares the **structurant steps** constituting that orchestration. Every orchestration (root and sub) has exactly one. | "orchestration contract", "contract.yaml", "sidecar", "handler_contract", "the contract sidecar" |
| **structurant step** (**step**) | One entry in a workflow's `steps:`. Fields: `id`, `kind` (the step's nature: facilitate/author/delegate/gate/…), `actor` (role or orchestrator), plus one flat **conditions** list — the same shape the *log* records — of `{kind, type, expression, value, id}` records covering both structural refs (`after`/`input`/`output`) and judgments (`cel`/`instruction`) (see *condition*). Each step appends one *log* line (the single generic log type), discriminated by its `step` field. | "handler", "matrix row", "exchange row" |
| **condition** | One entry in a step's flat `conditions` list with four orthogonal attributes plus an id. **kind** ∈ precondition / postcondition / invariant (WHEN it holds). **type** ∈ authority / content / clarification / challenge / consistency / transition / state (judgment categories) or `after` / `input` / `output` (structural dependencies). **expression** ∈ `cel` / `instruction` / `ref` (the FORM of `value`). **value** is the body — a CEL predicate, an instruction URI, or a ref. Coherence is enforced: **every condition carries an `id`**; structural types use `expression: ref` (`after`/`input` are preconditions, `output` a postcondition); a precondition/postcondition judgment uses `expression: cel`; an invariant uses `expression: instruction`. `cel` evaluates over the read-only fact set (`status`, `unit`, `child_features`, `child_stories`, `product`, `unit_id`, `open_items_clear`, + derived facts `depends_on_met` / `gate_packet_ok` / `inventory_complete` / `all_children_done` / `child_qa_signoffs_present` / `blocked_route_ok` / `wsjf_correct` / `cost_rollup_correct`), a judgment the author attests riding `cel` as `unit.attestations.<id>`; `instruction` resolves a `.instructions.md` obligation file structurally (the agent follows it). | "control/data condition", "phase", "present()", "harness.py function", "ctx.defer" |
| **log** | The structured record a step appends. **One generic log type for the whole framework — one JSON schema total** (`harness/schemas/log.base.schema.json`); there are no per-step log schemas. A log line is discriminated by its `step` field (which must match a `steps[].id` in the emitting workflow) and records its step's declared condition evaluations. Log instances are appended (one JSON object per line, JSONL) under `portfolio/logs/<orchestration>/<product-or-portfolio>/<unit-id>/<step-id>.jsonl`, and validated by the harness `step-check`. | "trace", "trace event", "orchestration-trace", "per-step log schema" |
| **artifact** | A deliverable an orchestration produces. Worked **internally as JSON** (validated against its *artifact schema* after every edit) and rendered to **Markdown by its author as the orchestration's last step**. The JSON instance `<unit>.artifact.json` is the **source of truth**; `<unit>.md` is its render. Each orchestration owns the templates + schemas of the artifacts it produces, under `<orchestration>/artifacts/`. | "doc", "backlog file" |
| **artifact schema** | The JSON Schema for an artifact. Its object tree **mirrors the artifact template's hierarchical section structure**: the head title/section is the root object; each child `##`/`###`/… section is a nested subobject, recursively. Native-JSON artifacts carry this as a real `sections` object the schema validates directly (harness `check-artifact`); Markdown-only artifacts are still checked via the harness-injected `__section_tree` field pending migration. | "flat section schema" |
| **artifact template** | The human-facing Markdown shape of an artifact, `<artifact>.artifact-template.md`, paired 1:1 with `<artifact>.artifact.schema.json`. Section nesting in the template is authoritative for the schema's object tree. | — |
| **harness** | The deterministic checker the orchestration runs **during** the orchestration — at each step, not only at return. Per step it (1) validates the step's *log* line against the single generic log schema, in the workflow-declared step order (`step-check`); and (2) validates every edited *artifact* against its schema after each edit — native-JSON artifacts directly via `check-artifact`. Source: `harness/orchestration-harness.py` (the CLI entry inside the `harness/` package). | "return guard" (now one mode of the harness) |

## Folder layout (canonical)

```
<framework-root>/                     # the single movable framework folder (harness/ + layers/ at its root)
  workflows.lock                      # pinned sha256 of every workflow.yaml (the constitution)
  harness/                            # the self-contained deterministic engine (entry + build + package + schemas)
    orchestration-harness.py          # harness CLI entry (run from harness/, or as harness/orchestration-harness.py)
    Makefile  requirements.txt        # make verify / test / check-catalog ; pip deps
    README.md                         # harness reference (was references/orchestration-harness.md)
    schemas/{workflow.schema.json, log.base.schema.json, orchestration-harness-finding.schema.json,
             artifact/<artifact>.artifact.schema.json}   # one flat artifact-schema registry, harness-governed
  instructions/{cost-accounting-protocol.md, logging-protocol.md, anti-patterns.md}   # techno-agnostic protocols
  sync/github/{github-projects-board-spec.md, github-sync-protocol.md,
               github-sync-config-template.yaml.md}  # host adapter (swap a sibling sync/<host>/ for gitlab, ...)
  docs/{cel-migration-plan.md, cel-rung-classification.md}   # design notes
  layers/                             # the three SAFe layers + shared library
    orchestrator.skill.md                   # shared library skill (NOT an orchestration)
    canonical-glossary.md  brainstorm-format.md
    artifacts/                              # cross-cutting artifact templates (project-brief, ledger)
    portfolio/                              # portfolio layer
      actors/                               # personas (bench roles + orchestrator persona)
        value-management-officier/          # orchestrator persona: <name>.agent.md + <name>.skill.md + artifacts/
        business-owner/  enterprise-architect/       # roles (portfolio): <name>.agent.md + <name>.skill.md + artifacts/
      lpm/            # root orchestration (portfolio)
        workflow.yaml                       # root workflow (structurant steps)
        instructions/
        workflows/
          epic-lean-business-case/          # suborchestration
            epic-lean-business-case.skill.md
            workflow.yaml
            artifacts/<artifact>.artifact-template.md   # template colocated; schema lives in harness/schemas/artifact/
          <other suborchestrations>/
    program/                                # program layer
      actors/
        release-train-engineer/             # orchestrator persona
        product-manager/  system-architect/          # roles (program)
        product-manager-author/                      # skill-only role (no agent)
      art/  (same shape as the portfolio root orchestration above)
    team/                                   # team layer
      actors/
        scrum-master/                       # orchestrator persona
        product-owner/  developer/  operator/  quality-engineer/
        security-expert/  tech-writer/  ux-designer/  # roles + bench (team)
      scrum/  (same shape as the portfolio root orchestration above)
```

## Loading & discovery note

Suborchestrations are nested and therefore **not** in VS Code auto-discovery (no `/slash`, no
automatic model-invocation). This is intentional: the framework already loads them by **explicit
path** (`load <root>/workflows/<name>` — read the `<name>.skill.md` + `workflow.yaml`).
Root orchestrations live under their layer folder (`layers/<portfolio|program|team>/<root>/`) and
personas (bench roles + orchestrator persona) under `layers/<portfolio|program|team>/actors/<name>/`;
in the colocated layout (the framework root is its own skills root) they too are loaded by
**explicit path** from the framework agents, not VS Code auto-discovery.
