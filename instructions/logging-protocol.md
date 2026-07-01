# Logging Protocol

The journal model that makes every orchestration run **observable and replayable**: the harness appends
**one entry per command** to a single per-run journal, and the journal is the **audit + trace, never the
branching input** — sequencing recomputes from artifacts. Harness reference:
[def/harness/README.md](../def/harness/README.md) (`## Logging`).

## One journal, one entry per command

There is **one** journal schema for the whole framework —
[journal.schema.json](../harness/schemas/journal.schema.json) — an **envelope** discriminated by `command`
(`oneOf`) over per-command payload schemas (`../harness/schemas/journal/*.payload.schema.json`). Every
command (hook or orchestration) appends exactly one entry. **Logging is intrinsic to every command** —
there is no separate "log" command.

- **envelope** (every entry, one schema): `{command, trigger, run, session, orchestration, step, unit, actor, ts, status}`.
- **payload** (typed per command): a hook command's payload **is its report**; an orchestration command's
  payload **is its action** (`dispatch` / `halt` / `done`). `check-step`'s payload carries the evaluated
  conditions (formerly `log.base.schema.json`, now `journal/check-step.payload.schema.json`).

## Journal location

One JSONL file per run (append-only, one JSON object per line):

```
portfolio/logs/<run>.jsonl
```

Per-session host hook streams land alongside at `portfolio/logs/hooks/<session>.jsonl` and fold into the
run journal by dispatch correlation. JSONL order is the authoritative command ordering; `ts` is advisory.
Grouping entries by `step` reconstructs each step; the ordered `orchestrate`→`dispatch` entries are the
run's step sequence, so the whole journal replays the run end-to-end.

## The run is harness-driven (no per-step hand-logging)

You never hand-author journal lines or hand-sequence steps. The harness drives, via
`python3 -m harness <command>`:

- **orchestration commands** (agent-called drive loop):
  - `orchestrate --workflow <id> --unit <id> --run <run>` — computes the next action from the unit's
    **artifacts** + the workflow and appends one `orchestrate` entry (`action` = `dispatch` | `halt` |
    `done`). Relay a `dispatch` (model verbatim), surface a `halt` (`gate` / `blocked` / `unroutable`), end
    on `done`.
  - `check-step --orchestration <id> --step <id> --unit-id <id> [--session <id>]` — evaluates a step's
    pre/postconditions and appends a `check-step` entry.
  - `check-artifact --path <artifact>` — validates a written artifact against its schema / state and appends
    a `check-artifact` entry.
- **hook commands** (host-fired at lifecycle boundaries): `hook --event <e> --env <env>` — each appends a
  `hook` entry (its report). Bound by `../harness/adapters/<host>/hooks/map.yaml`.

## Conditions (what `check-step` evaluates)

Each entry in a step's flat `conditions` list is checked by `expression`:

- **structural refs** — `type: after` (the predecessor step's output artifact exists), `type: input` /
  `output` (an artifact ref resolves + exists; an unresolvable logical ref is `skipped`);
- **judgments** — every pre/postcondition is `cel` (a CEL predicate over the read-only fact set — `status`,
  `unit`, `child_features`, `child_stories`, `product`, `unit_id`, `open_items_clear`, + the derived facts;
  an author-attested judgment rides `cel` as `unit.attestations.<id>`);
- **invariants** — `instruction` (the harness resolves the obligation file structurally; the agent follows
  it).

`check-step` covers **both** the step's preconditions (at entry) and postconditions (at exit); the
pre/post split is conceptual — one CLI command evaluates both.

## Check-only determinism (the journal is not the gate)

The journal is the **audit + trace, not the branching input**. The next `orchestrate` recomputes the step
cursor from the unit's **artifacts** + the workflow — every step produces or updates exactly one artifact —
so sequencing **never** depends on trusting a prior journal entry (Design Invariant 13). CEL is
side-effect-free; the harness never writes artifacts.

## Fail-closed rule (on artifacts, not on log lines)

Effect-determinism is grounded in **artifacts**, not journal coverage: every step produces or updates
exactly one artifact — a new artifact, a kanban status update, a gate decision, or a review/verdict. An
orchestrator MUST NOT treat a step complete while its artifact is missing or fails `check-artifact`. A
`halt` action is **not** a completed return — the only valid outcomes are: keep driving the workflow,
surface the halt to the human (★ gates), record a blocker, or record workflow friction in
the PI Inspect & Adapt ledger (`pi-M/inspect-adapt.md` §3b). The journal records what happened; the **artifacts decide what is true**.
