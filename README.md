# Poesis SAFe Agentic Framework

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-scaffold-lightgrey)](.)

> **SAFe-shaped agentic framework for GitHub Copilot / VS Code and portable agent hosts** —
> multi-agent orchestration (portfolio/program/iteration orchestrators), a framework-owned
> specialist bench, skills, deterministic model routing, and a portable orchestration harness.
> Open-source developer tooling from [Poesis Cloud](https://poesis.cloud).

---

> **Note — v0.1:** This repository root **is** the framework. Agents, skills, harness, and the
> [`plugin.json`](plugin.json) manifest are its direct children — install the repository root as the
> GitHub Copilot customization plugin.

---

## Overview

The Poesis SAFe Agentic Framework brings SAFe-shaped multi-agent orchestration into
agent execution environments that support custom agents and skills. It includes:

- **Orchestrators**: `@value-management-officier`, `@release-train-engineer`, `@scrum-master`
- **Specialist bench**: framework-owned author, architecture, development, QA, security, operator, docs, and UX agents
- **Skills**: SAFe ceremony, practice, authoring, and orchestration playbooks loaded on demand
- **Model routing**: deterministic LLM tier + capability-score routing — no random model selection
- **Portable harness**: deterministic artifact, gate-packet, and runtime-trace checks independent of VS Code hooks

## Layout

The framework is declared by [`plugin.json`](plugin.json) at the repository root and is self-contained:

- [`layers/`](layers/) — the three SAFe layers (`portfolio/`, `program/`, `team/`), each with its
  orchestration root and an `actors/` bench of colocated `<name>.agent.md` + `<name>.skill.md` + `artifacts/`
- [`harness/`](harness/) — the portable, deterministic orchestration engine (sequencing, CEL conditions, FSM, gates, model routing, run journal)
- [`sync/github/`](sync/github/) — the host binding (GitHub Projects board spec + sync protocol; swap a sibling `sync/<host>/` for another host)
- [`hooks/`](hooks/) — git lifecycle gate that runs the harness constitution check

## Deterministic Harness

The framework's deterministic checks live in [`harness/`](harness/) and run through the stable
entrypoint [`harness/harness.py`](harness/harness.py). They are
host-neutral: a CI job, shell wrapper, VS Code hook, or another agent runtime can call the same CLI.

Four commands (the global options `--portfolio-root`, `--strict`, `--json` come **before** the command):

```bash
# STATE — validate Epic/Feature/Story artifacts (FSM, linkage, schema, gates, derived fields)
python3 harness/harness.py --portfolio-root /path/to/portfolio \
  check-artifact --unit-id sie-observability-foundation

# DRIVE — resolve the next orchestration action (dispatch | halt | done)
python3 harness/harness.py \
  orchestrate --workflow value-management-officier --unit sie-observability-foundation

# CONDITIONS — evaluate one step's conditions and append the session ledger line
python3 harness/harness.py \
  check-step --orchestration value-management-officier --step capture-epic \
  --unit-id sie-observability-foundation --session abc123

# HOOK — funnel a host lifecycle event (JSON on stdin) through the harness
cat event.json | python3 harness/harness.py hook --event preToolUse
```

The harness never writes artifacts — it reports the value/edge; the orchestrator commits. The framework
constitution (workflow contracts + artifact catalog) is verified separately by the pytest suite:
`make -C harness verify`.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions are accepted under Apache-2.0.
This project uses the [Developer Certificate of Origin (DCO)](https://developercertificate.org/).

---

## License

Apache License, Version 2.0. See [LICENSE](LICENSE).

Copyright 2026 Poesis Cloud and contributors.
