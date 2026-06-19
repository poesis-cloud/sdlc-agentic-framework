# GitHub Projects sync protocol — bidirectional semantics

How `portfolio/_sync/sync.py` reconciles local `portfolio/<slug>/` artifacts with the per-product
GitHub Project defined by the [board spec](./github-projects-board-spec.md). Read the board spec
first — this document covers only the *runtime behaviour* of sync.

## 1. Command surface

All commands take `<slug>` or `--all`, and support `--dry-run` (mutating commands default to a
plan unless `--apply` is given). Run from the workspace root.

| Command | Side | Mutates | Purpose |
|---|---|---|---|
| `init <slug>` | local | local config | generate `portfolio/<slug>/github-sync.yaml` from registry + template |
| `export <slug>` | local | none (writes `.sync-export.json`) | parse markdown → normalized item list |
| `status <slug>` | both | none | diff local ↔ state ↔ remote; `--offline` skips remote |
| `provision <slug>` | remote | org/repo/project | ensure Issue Types, planning repo, Project, fields, views (board spec §10) |
| `migrate-fields <slug>` | remote | project fields | rename legacy pre-`SAFe` fields to `SAFe ` names, or delete the legacy duplicate when the canonical `SAFe ` field already exists (one-time reconcile) |
| `push <slug>` | remote | issues/items | create/update Issues + Project items + fields from local |
| `pull <slug>` | local+remote | local md + state | apply non-gate board moves to local; materialize born-remote items |

Standard run order: `init` → `provision` → `export` → `push` → (humans work the board) →
`pull`. `status` is safe any time.

## 2. Identity & matching

Match each local item to a remote item in this order (board spec §9):

1. `items[<id>]` in `portfolio/<slug>/.sync-state.json` (authoritative).
2. `SAFe Local ID` project field equal to the local `id`.
3. Issue title prefix `F-NN`/`S-NNN`.
4. No match → the item is **born-remote** (see §5) or **born-local** (see §6) depending on
   which side it exists on.

The state file is rewritten atomically after every mutating command.

## 3. Direction authority (non-gate)

| Concern | Authority | Resolution |
|---|---|---|
| Content (title, body, WSJF, risk, complexity, pi, sprint, parent, structurant, estimate) | **local** | `push` overwrites the remote projection from markdown |
| Status (Program/Team), non-gate columns | **remote** *(config `authority.status`)* | `pull` writes the board column back to frontmatter `status` |
| `blocked` flag | **local** | `push` sets/clears the `blocked` label from local frontmatter |

A conflict is when *both* sides changed since `last_synced_*` in state. Default resolution:
content → local wins; status → remote wins. Conflicts are always **reported** by `status` and
`push`/`pull` output; gate-adjacent conflicts are appended to `sprint-N/gate-decisions.md`.

## 4. Gate-crossing transitions (never auto-applied)

A transition is **gate-crossing** if it enters or leaves a gate column listed in
`gate_columns` (`arch-pending`, `awaiting-pr`) **or** targets `done` (board spec §8). `done` is
not itself a `gate_columns` entry — the `→ done` crossing is detected independently so a `done`
item never displays as awaiting a gate.

- **Local → remote:** sync may move a card *into* a gate-pending column; it never advances a
  card *past* a gate. `done` is pushed only after the local flip that the orchestrator performs
  *after* the chat-side gate.
- **Remote → local:** a human board move *across* a gate boundary is captured as a **request**,
  not applied. `pull` records it in `sprint-N/gate-decisions.md` with options
  `accept | rework | defer` and leaves local `status` unchanged. The Central Supervisor approves
  in chat; the owner then flips local; the next `push` reconciles the board.

This keeps sync compatible with the orchestration-core invariants *No Gate skipping* and
*Owner-only transitions*.

## 5. Born-remote items (materialize locally)

When `pull` finds a Project item / Issue with no local match:

1. Assign the next free `id` for its type (`F-` = max existing Feature + 1; `S-` likewise).
2. Write a new markdown artifact from the Feature/Story template into the correct product path
   (`features/` or `sprint-<N>/stories/` using the `Sprint` field, default current sprint).
3. Populate frontmatter from remote fields; set `status` from the board column (unless
   gate-crossing → leave at the column's pre-gate value and log to gate-decisions).
4. Record the mapping in state and write the `github:` back-reference block.
5. Report every materialized item; never overwrite an existing local file.

## 6. Born-local items (create remotely)

When `push` finds a local artifact with no remote match:

1. Create an Issue in the planning repo with the proper Issue Type, title, and body projection.
2. Add it to the Project; set all fields (board spec §4) from frontmatter.
3. For Stories, link as a sub-issue of the parent Feature's Issue (creating the Feature first
   if needed by ordering Features before Stories in the push pass).
4. Write back the `github:` block and the state entry.

## 7. Non-destructive guarantee

Sync never deletes or closes Issues, never archives Project items, and never deletes local
files. A removed local artifact is reported as **orphaned-remote** by `status` for manual
disposition; a closed remote Issue is reported as **orphaned-local**. `authority.destructive`
stays `false`.

## 8. Failure & safety

- Every remote call goes through `gh api graphql`; a non-zero `gh` exit aborts the command with
  the captured error (no partial state written for that item).
- `provision`/`push`/`pull` are idempotent and re-runnable; a re-run after a partial failure
  reconciles from state.
- Requires `gh auth status` logged-in with scopes `read:project`, `project`, and `repo`
  (planning-repo issues). Refresh: `gh auth refresh -h github.com -s read:project,project,repo`.

## 9. CI (optional)

A scheduled GitHub Action may run `status --all` (read-only) to detect drift and `pull --all
--apply` to land board moves, opening a PR with the resulting frontmatter changes. `provision`
and `push` stay manual/design-time. CI never crosses a gate (§4).

## 10. Git planning repo sync (`git-sync.py`)

Each product folder (`portfolio/<slug>/`) and the portfolio root (`portfolio/`) are **independent
git repositories** mirrored to the corresponding remote on GitHub (`poesis-cloud`). The
`portfolio/_sync/git-sync.py` script provides a single bidirectional git routine:

```
python3 portfolio/_sync/git-sync.py status --all        # read-only drift check
python3 portfolio/_sync/git-sync.py pull   --all --apply  # fetch + merge all repos
python3 portfolio/_sync/git-sync.py push   --all --apply  # commit + push all repos
python3 portfolio/_sync/git-sync.py sync   --all --apply  # pull then push all repos
```

All commands accept a single `<slug>` (or `portfolio`) instead of `--all`. Push auto-generates
a commit message if `--message` is not supplied.

**Remote mapping:**

| Local folder | Remote repo |
|---|---|
| `portfolio/` | `poesis-cloud/poesis-portfolio-planning` |
| `portfolio/<slug>/` | `poesis-cloud/<slug>-planning` |

(Slug overrides: `sdlc-agentic-framework` → `agentic-sdlc-framework-planning`.)

**Routine cadence** — run `git-sync.py sync --all --apply` after every batch of artifact edits
and before closing a turn that modified SAFe artifacts. The GitHub Projects board sync
(`sync.py push/pull`) is orthogonal and runs separately.
