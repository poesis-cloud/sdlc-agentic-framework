# Quickstart — SDLC Agentic Framework

This guide takes you from a fresh install to your first successful orchestrated PR.
Target: **under 30 minutes**.

---

## Prerequisites

Before you start, you need:

1. **VS Code** (1.90 or later) with the **GitHub Copilot** extension installed and signed in.
2. **Git** (any recent version).
3. The following **external prerequisites** (distributed separately under their own licences):

| Prerequisite | Install |
|---|---|
| **SE:\* specialist bench agents** | Install via the [software-engineering-team plugin](https://github.com/github/awesome-copilot) or equivalent Copilot extension |
| **bmad-\* skills** | Clone [bmadcode/bmad-method](https://github.com/bmadcode/bmad-method) into `~/.vscode/agent-plugins/github.com/bmadcode/bmad-method` |
| **gds-\* skills** | Install from the upstream source per its documentation |

> These components are **not** bundled in this package and are **not** relicensed under Poesis Cloud's
> Apache-2.0. See [NOTICE](../NOTICE) and [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## Step 1 — Install

```bash
git clone https://github.com/poesis-cloud/sdlc-agentic-framework \
  ~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework
```

That's it. VS Code GitHub Copilot automatically scans `~/.vscode/agent-plugins/` for agents and
skills — no further configuration needed.

**To pin to a specific version:**

```bash
cd ~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework
git fetch --tags
git checkout v0.1.0
```

**To update to the latest:**

```bash
cd ~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework
git pull
```

---

## Step 2 — Verify agents are visible

1. Restart VS Code (or reload the window: `Ctrl+Shift+P` → "Developer: Reload Window").
2. Open GitHub Copilot Chat.
3. Type `@` — you should see the following agents listed:
   - `@rte-orchestrator` — Release Train Engineer (program/ART layer)
   - `@sm-orchestrator` — Scrum Master (team/iteration layer)
   - `@vmo-orchestrator` — Value Management Office (portfolio layer)

If agents do not appear, see [Troubleshooting](#troubleshooting).

---

## Step 3 — Run your first orchestration

The entry point for new work is `@vmo-orchestrator`. It receives your Epic (the high-level
intent), approves it at ★ Gate 0, and hands it to `@rte-orchestrator` for Feature breakdown.

**Minimal example — start a new Epic:**

Open Copilot Chat and type:

```
@vmo-orchestrator I want to start a new Epic:
"Build a REST API for user authentication (JWT, refresh tokens)"
```

The VMO will:
1. Help you shape the Epic hypothesis and WSJF scoring.
2. Approve it at ★ Gate 0.
3. Dispatch `@rte-orchestrator` to derive Features and plan the sprint.

**Continue to your first PR:**

```
@rte-orchestrator Continue. Derive Features from the Epic and dispatch the SM for Sprint 1.
```

The RTE will derive Features, run architecture triage (★ Gate 2 if needed), and dispatch
`@sm-orchestrator` for Story decomposition and pair programming execution.

---

## Step 4 — Validate success

You have completed the quickstart when:

- [ ] `@vmo-orchestrator`, `@rte-orchestrator`, `@sm-orchestrator` all appear in the agent list.
- [ ] A planning repo structure exists under `portfolio/<slug>/` in your workspace.
- [ ] At least one Story has been executed and a PR has been opened by the SM.

---

## Troubleshooting

**Agents do not appear in the Copilot Chat `@` list**

- Ensure the clone is at the exact path `~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework`.
  The `github.com/<org>/<repo>` path structure is required by the VS Code APM convention.
- Reload VS Code window (`Ctrl+Shift+P` → "Developer: Reload Window").
- Check that GitHub Copilot extension is up to date (v1.270 or later recommended).
- Verify `plugins/ai-team-orchestration/agents/` contains `*.agent.md` files.

**Skills fail to load (agent says "skill not found")**

- Confirm that the orchestration-core skill is present:
  `ls ~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework/plugins/ai-team-orchestration/skills/`
- Verify the `bmad-*` and `gds-*` external prerequisites are installed if the agent tries to load them.

**"SE:\* bench agents not found"**

- The SE:\* bench (`SE: Security`, `SE: Architect`, etc.) are external prerequisites.
  Install the `software-engineering-team` plugin or equivalent. See [Prerequisites](#prerequisites).

---

## What's next

- Read [CONTRIBUTING.md](../CONTRIBUTING.md) to understand how to contribute improvements.
- Check [GitHub Releases](https://github.com/poesis-cloud/sdlc-agentic-framework/releases) for version history.
- File issues at [github.com/poesis-cloud/sdlc-agentic-framework/issues](https://github.com/poesis-cloud/sdlc-agentic-framework/issues).
