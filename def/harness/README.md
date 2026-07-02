# Deterministic Harness

The harness is the deterministic execution core of the SAFe agentic framework. It owns the workflow graph, step sequencing, gate staging, authorization checks, model routing, context injection, and run logging. Agents stay limited to the irreducible work: generating content, judging within a step, conversing with the human, and actuating host tools.

This document is the canonical harness description. It replaces the older split between the root harness README and the environment-hooks README.

## Functional role

The harness is check-only and artifact-driven.

- It computes what happens next from workflow definitions plus current artifacts.
- It validates step preconditions, postconditions, and written artifacts.
- It mediates all host hook events so the host adapter never becomes a second source of truth.
- It records one journal entry per harness command, making each orchestration run observable and replayable.

The harness never authors business artifacts itself. Status transitions, gate decisions, and authored deliverables are all produced by dispatched agents and then checked by the harness. The one deliberate exception is enforcement: the postcondition hook may **revert** an invalid write (restore the last-good version or delete the new file) to preserve the Portfolio Validity Invariant (C6) — it never authors content.

## Invariants

The harness enforces the following invariants.

### C0 - Portfolio state definition

Portfolio state is the union of:

- Persisted portfolio artifacts (business, governance, and orchestration deliverables under portfolio state paths).
- Harness logs (run journals and hook streams) persisted under the portfolio logs paths.

Both are first-class state for deterministic checks and replay.

### C1 - Portfolio-state scope

All preconditions and postconditions are evaluated strictly against persisted portfolio state.

### C2 - Harness assertion boundary

Condition checks executed by the harness only assert portfolio state. The harness does not assert private agent memory or transient, non-persisted host context.

### C3 - Agent sourcing freedom

The actor agent may source from portfolio data, external systems, tools, or web context. Harness pass or fail is based only on persisted portfolio state.

### C5 - Schema-bound persisted artifacts

Every persisted artifact used in condition evaluation must be cataloged and schema-bound. The selector model has one selector type: selecting persisted portfolio artifacts.

Where a condition depends on log evidence, that evidence is read from persisted harness logs (part of portfolio state) and asserted as state; logs are not business artifacts.

### C6 - Portfolio validity

The portfolio contains exclusively schema-valid artifacts and valid state, at all times.

- Maintained at the write boundary. The postcondition hook validates each agent write against its artifact schema and, if invalid, reverts it (restore the last-committed version if the path is tracked, else delete the new file) and denies with the schema findings so the agent retries. This revert is the harness's single deliberate write.
- Relied on by every reader. The artifact repository is valid-by-construction: `discover()` raises rather than yield a schema-invalid artifact, so no domain code (state selection, step checks, orchestration) ever operates on an invalid artifact. The validators that must enumerate invalids (`check-artifact`, the hook) read the raw universe (`scan_raw`) instead.
- Enables safe asynchronous / remote portfolio sync. A synced replica is trustably valid; reconciliation only has to preserve validity, not re-derive it.

## Two trigger planes, one command system

Every harness behavior is exposed as a harness command. The same command system is entered from two places.

- Hook-triggered commands: the host calls the harness on lifecycle events such as `sessionStart`, `preToolUse`, `postToolUse`, and `sessionEnd`.
- Agent-triggered commands: the orchestrator agent calls the harness drive loop with `orchestrate`, plus targeted checks such as `check-step` and `check-artifact`.

There is no separate hook logic outside the harness. The adapters only forward host events and render the harness decision back into the host format.

## Core commands

| Command | Trigger | Purpose | Output |
|---|---|---|---|
| `orchestrate <workflow-id>` | orchestrator agent | Resolve the next workflow action from artifacts and workflow state | `dispatch`, `halt`, or `done` |
| `check-step` | orchestrator or hook flow | Evaluate a step's preconditions and postconditions | typed report |
| `check-artifact` | post-write validation | Validate the written artifact against schema and state rules | typed report |
| `hook --event <name> --env <env>` | host adapter | Normalize a host lifecycle event and route it through the deterministic checks | typed report / host decision |

## Hook adapter layout

The dispatch script is shared and generic across every host; only the per-host registration and
tool binding live under each adapter's own subfolder. See `harness/adapters/README.md` for the full
adapter contract (adding a new host, etc.).

```text
harness/
  adapters/
    dispatch.sh       # shared, generic dispatcher: stdin JSON -> harness hook command (every adapter calls this)
    github-copilot/
      hooks/
        map.yaml      # YAML source rendered to .copilot/hooks.json
      tools/
        map.yaml      # host tool names, write verbs, payload keys
  acl/
    map.yaml          # env-agnostic authorization grants
  llm/
    map.yaml          # env-agnostic model tiers, capability scores, routing knobs
```

`dispatch.sh` is intentionally thin and env-agnostic: it takes the event name and the environment
id as its two arguments and forwards the raw event payload to `harness.py hook --event <name> --env
<env>`, exiting with the harness result. Each adapter's `hooks/map.yaml` supplies its own
environment id as the second argument.

## Event normalization

Host events are normalized to workflow concepts before any policy is applied.

| Host event | Normalized phase | Harness responsibility |
|---|---|---|
| `sessionStart` | `session-open` | inject deterministic context, verify step entry conditions |
| `userPromptSubmit` | `observe` | record observation only |
| `preToolUse` | `precondition` | authorize writes and validate dispatch route |
| `postToolUse` | `postcondition` | validate the produced artifact |
| `stop` / `sessionEnd` | `session-close` | review step exit conditions and session outcome |

This keeps the harness env-agnostic: only the adapter maps host-specific event names and tool payloads.

## Runtime model

One session corresponds to one structurant step. At session open, the harness correlates the session to the most recent open dispatch for the actor and injects the step-local context.

- Skills are injected per step, not globally per workflow.
- Instruction files are injected from the step's declared invariants.
- Model choice is resolved by the harness and only relayed by the agent into `runSubagent`.
- Authorization remains plain artifact-level RBAC over `<action>_<resource>` privileges.

## Logging

The run journal is append-only and command-granular.

- Per-run journal: `portfolio/logs/<run>.jsonl`
- Per-session hook stream: `portfolio/logs/hooks/<session>.jsonl`

Each harness command appends exactly one entry with a shared envelope and a typed payload. The journal is the audit and replay trace, but not the branching input. Sequencing is always recomputed from workflow definitions plus current artifacts.

## Installation

Render the GitHub Copilot hook registration into the repository `.copilot` folder:

```bash
make -C harness install-copilot-hooks
```

That command renders `harness/adapters/github-copilot/hooks/map.yaml` into `.copilot/hooks.json`.

## Validation surface

Use the harness make targets for deterministic validation.

```bash
make -C harness verify
make -C harness check-catalog
make -C harness full
```

`verify` runs the constitution tests. Runtime artifact validation remains in the CLI and hook path rather than the static verification suite.
