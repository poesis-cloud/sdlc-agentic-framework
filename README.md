# SDLC Agentic Framework

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-scaffold-lightgrey)](.)

> **SAFe-shaped SDLC agentic framework for VS Code / GitHub Copilot** — multi-agent
> orchestration (portfolio/program/iteration orchestrators), specialist bench, skills,
> and model routing. Open-source developer tooling from [Poesis Cloud](https://poesis.cloud).

---

> **Note — v0.1 scaffold:** This repository currently contains the legal envelope only.
> Framework content (skills, agents, instructions, model routing) is published in
> a future sprint. Watch this repo for updates.

---

## Overview

The SDLC Agentic Framework brings SAFe-shaped multi-agent orchestration directly
into your IDE via the VS Code Agent Plugin Manager (APM). It includes:

- **Orchestrators**: `@vmo-orchestrator`, `@rte-orchestrator`, `@sm-orchestrator`
- **Specialist bench**: `SE: Security`, `SE: Architect`, `SE: DevOps/CI`, `SE: Tech Writer`, and more
- **Skills**: domain-specific procedural playbooks loaded by agents on demand
- **Model routing**: deterministic LLM tier + capability-score routing — no random model selection

---

## Install

This framework uses the **VS Code Agent Plugin Manager (APM)** convention — a directory that
VS Code / GitHub Copilot scans automatically at startup. There is no `apm` CLI to install;
the install mechanism is a plain `git clone` into `~/.vscode/agent-plugins/`.

**1. Install this framework:**

```bash
git clone https://github.com/poesis-cloud/sdlc-agentic-framework \
  ~/.vscode/agent-plugins/github.com/poesis-cloud/sdlc-agentic-framework
```

**2. Install the required prerequisites** (same APM convention):

```bash
# SE:* specialist bench agents
git clone https://github.com/github/awesome-copilot \
  ~/.vscode/agent-plugins/github.com/github/awesome-copilot

# bmad-* skills
git clone https://github.com/bmadcode/bmad-method \
  ~/.vscode/agent-plugins/github.com/bmadcode/bmad-method
```

**3. Reload VS Code.** `@rte-orchestrator`, `@sm-orchestrator`, and `@vmo-orchestrator` appear
in your Copilot Chat agent list automatically.

**Pin to a release:** `git checkout v0.1.0` in the cloned directory.

**Update:** `git pull` in the cloned directory.

---

## Quickstart

See **[docs/quickstart.md](docs/quickstart.md)** for the full walkthrough
(target: first orchestrated PR in under 30 minutes).

**TL;DR:**

1. Install (above).
2. Open Copilot Chat → type `@vmo-orchestrator` to start a new Epic.
3. Follow the orchestration chain: VMO → RTE → SM → first PR.

---

## External prerequisites

The framework depends on the following external components, installable via the same APM
convention. They are distributed under their own upstream licenses and are **not** relicensed
under this project's Apache-2.0 (see [NOTICE](NOTICE)):

| Component | APM install path | Purpose |
|---|---|---|
| `SE:*` specialist bench | `github.com/github/awesome-copilot` | Security, Architect, DevOps/CI, Tech Writer, UX, RAI agents |
| `bmad-*` skills | `github.com/bmadcode/bmad-method` | BMad Method skill library |
| GitHub Copilot | VS Code extension (Microsoft) | IDE host — required for agent resolution |

The `prerequisites` block in `plugins/poesis-sdlc-agentic-framework/plugin.json` lists these
dependencies in machine-readable form for future APM tooling.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [NOTICE](NOTICE) for license details.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions are accepted under Apache-2.0.
This project uses the [Developer Certificate of Origin (DCO)](https://developercertificate.org/).

---

## License

Apache License, Version 2.0. See [LICENSE](LICENSE).

Copyright 2026 Poesis Cloud and contributors.
