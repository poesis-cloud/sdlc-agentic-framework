# Deterministic Harness

The harness is the deterministic execution core of the SAFe agentic framework. It owns the workflow graph, step sequencing, gate staging, authorization checks, model routing, context injection, and run logging. Agents stay limited to the irreducible work: generating content, judging within a step, conversing with the human, and actuating host tools.

This document is the canonical harness description. It replaces the older split between the root harness README and the environment-hooks README.

## Functional role

The harness is check-only and artifact-driven.

- It computes what happens next from workflow definitions plus current artifacts.
- It validates step preconditions, postconditions, and written artifacts.
- It mediates all host hook events so the host adapter never becomes a second source of truth.
- It records one journal entry per harness command, making each orchestration run observable and replayable.

The harness never writes business artifacts itself. Status transitions, gate decisions, and authored deliverables are all produced by dispatched agents and then checked by the harness.

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
