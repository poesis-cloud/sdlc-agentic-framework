---
name: strategic-portfolio-review
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The Strategic Portfolio Review playbook loaded by `@value-management-officier` per unit (on an Epic enter/exit). USE FOR: re-ranking the portfolio backlog by WSJF; revising Strategic Themes; pivot/persevere/stop recommendations on in-flight Epics; triaging portfolio-scope pain points from the workflow-improvement ledger. DO NOT USE FOR: deciding the ★ Epic Gate or accepting outcomes (Central Supervisor); shaping an individual Epic (use `business-owner`); program ceremonies (use `inspect-and-adapt`). Loaded by `@value-management-officier` before facilitating.'
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

# SAFe Ceremony — Strategic Portfolio Review

The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the participant challenges + facilitation obligations as judgment conditions; the structural `after`/`input`/`output` wiring), consumed by `@value-management-officier` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[VMO orchestration core](../../../actors/value-management-officier/value-management-officier.skill.md)**. The WSJF re-rank + Strategic-Theme revisions are authored via `business-owner`; **the Central Supervisor decides** pivot/persevere/stop and **only `@value-management-officier` writes `status:`**. A workflow-improvement is a meta-artifact change, never a product Epic.