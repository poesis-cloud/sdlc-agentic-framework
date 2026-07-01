---
name: architectural-runway-extension
user-invocable: false
description: '**SAFe PRACTICE SKILL.** The Architectural Runway Extension practice (Continuous Exploration / intentional architecture) loaded by `@release-train-engineer` per Feature (when a structurant Feature is `arch-pending`). USE FOR: `@system-architect` authoring one or more architecture decisions (**ADRs**) incrementally, with `@security-expert` (trust boundaries) + `@operator` (operability) + dev (feasibility) challenging; updating runway/NFR architecture references; seeding **enabler Features** (architectural / infrastructure / compliance); and iterating until the decision inventory is sufficient for the ★ Architecture Gate. DO NOT USE FOR: the ★ Architecture Gate decision (Central Supervisor); Feature AC + WSJF (use `feature-backlog-refinement`); the portfolio runway (use `architectural-vision`). Loaded by `@release-train-engineer` before facilitating; returns the architecture packet for the current pass — or a replay-required result when late enabler seeding invalidates prior Feature refinement; rte stages the gate only when the packet is complete.'
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

# SAFe Practice — Architectural Runway Extension (intentional architecture)

A **practice** (Continuous Exploration / intentional architecture) that extends the **architectural runway** for a structurant Feature. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the inventory + per-actor challenges + gate-staging + replay obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@release-train-engineer` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[RTE orchestration core](../../../actors/release-train-engineer/release-train-engineer.skill.md)**. ADRs are authored via `system-architect` (one ADR per decision unit — a structurant Feature may need several); **only `@release-train-engineer` writes `status:`** and **stages the ★ Architecture Gate** only when the decision inventory is sufficiently covered (it never decides). A late-seeded enabler Feature forces the parent Feature to replay **Feature Backlog Refinement** before the gate is restaged.
