---
name: feature-backlog-refinement
user-invocable: false
description: 'SAFe ART ceremony — Feature Backlog Refinement (suborchestration of @release-train-engineer). Normative spec (trigger, participants, steps, conditions, facilitation intent) is workflow.yaml.'
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

# SAFe Ceremony — Feature Backlog Refinement

The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — the step sequence and every step's `conditions` (the trigger as the first step's preconditions; the discovery lenses + facilitation obligations as judgment conditions; the structural `after`/`input`/`output` wiring), consumed by both `@release-train-engineer` and the deterministic harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[RTE orchestration core](../../../actors/release-train-engineer/release-train-engineer.skill.md)**. Authoring bodies load *inside* the steps: business Features via `product-manager-author`, enabler Features via `system-architect`.
