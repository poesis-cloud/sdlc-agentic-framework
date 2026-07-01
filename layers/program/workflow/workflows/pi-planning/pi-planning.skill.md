---
name: pi-planning
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The PI Planning playbook loaded by `@release-train-engineer` per Feature (when `ready` and its `depends_on` are met). USE FOR: turning `ready` Features into committed PI objectives; capacity allocation; cross-Feature dependency mapping; ROAM risk; the confidence vote; dispatching `@scrum-master`. It returns the PI objectives; `@release-train-engineer` commits Feature `ready→committed`. DO NOT USE FOR: deciding the ★ Architecture / Demo gates (Central Supervisor); authoring Features (use `product-manager-author`); the PI retro (use `inspect-and-adapt`). Loaded by `@release-train-engineer` before facilitating.'
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

# SAFe Ceremony — PI Planning

The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the per-actor confirmations + challenges + ROAM / confidence-commit obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@release-train-engineer` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[RTE orchestration core](../../../actors/release-train-engineer/release-train-engineer.skill.md)**. Features stay `product-manager`-authored; **only `@release-train-engineer` writes `status:`** — committing Feature `ready→committed` on a passing confidence vote and dispatching `@scrum-master`. The facilitator may raise (never silently lower) a Feature's risk/complexity here.
Objectives committed + dependencies mapped + risks ROAMed + confidence ≥ threshold + `@scrum-master` running.