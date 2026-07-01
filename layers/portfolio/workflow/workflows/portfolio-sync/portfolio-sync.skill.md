---
name: portfolio-sync
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The Portfolio Sync playbook loaded by `@value-management-officier` per unit (after an Epic transition or a `blocked`). USE FOR: monitoring cross-ART Epic progress; surfacing + escalating portfolio-level risk; removing portfolio impediments (Epic `blocked`/unblock); re-rendering the Portfolio Kanban. DO NOT USE FOR: re-ranking the backlog or pivots (use `strategic-portfolio-review`); the ★ Epic Gate (Central Supervisor); program risk (use `art-sync`). Loaded by `@value-management-officier` before facilitating.'
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

# SAFe Ceremony — Portfolio Sync

A **reconcile** ceremony (no authoring, no gate). The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the reconcile obligations as judgment conditions; the structural `after`/`input`/`output` wiring), consumed by `@value-management-officier` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[VMO orchestration core](../../../actors/value-management-officier/value-management-officier.skill.md)**. The facilitator rolls up cross-ART child-Feature progress, updates the portfolio risk register, and flips `→blocked`/unblock only — it authors no backlog artifact and flips no ★ gate; **only `@value-management-officier` writes `status:`**.