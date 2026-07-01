---
name: epic-lean-business-case
user-invocable: false
description: '**SAFe PRACTICE SKILL.** The Epic Lean Business Case practice (Continuous Exploration) loaded by `@value-management-officier` per Epic (when an Epic must be captured `∅→funnel`, shaped `funnel→reviewing`, or replayed after a late enabler invalidates prior shaping). USE FOR: collaboratively developing an Epic''s Lean Business Case — hypothesis, WSJF, leading indicators, MVP scope — with `@business-owner` authoring and EA / Responsible AI / Security challenging; capturing the Epic from a Strategic Theme. DO NOT USE FOR: the ★ Epic Gate decision (Central Supervisor); the architecture runway (use `architectural-vision`); Features (use `feature-backlog-refinement`). Loaded by `@value-management-officier` before facilitating; returns the shaped Epic — the VMO commits the status.'
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

# SAFe Practice — Epic Lean Business Case (Continuous Exploration)

The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the three Portfolio-tier Discovery lenses + facilitation obligations as judgment conditions; the structural `after`/`input`/`output` wiring), consumed by `@value-management-officier` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here. The native-JSON artifact uses [lean-business-case.artifact.schema.json](../../../../../harness/schemas/artifact/lean-business-case.artifact.schema.json) (validated directly by `check-artifact`).

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[VMO orchestration core](../../../actors/value-management-officier/value-management-officier.skill.md)**. CDP stage **Continuous Exploration**; the Epic is authored via `business-owner` and **only `@value-management-officier` writes `status:`** (`∅→funnel` / `funnel→reviewing`).
