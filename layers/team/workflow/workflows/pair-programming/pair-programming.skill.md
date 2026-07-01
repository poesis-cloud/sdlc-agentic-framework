---
name: pair-programming
user-invocable: false
description: '**SAFe PRACTICE SKILL.** The Pair-Programming micro-cycle (Continuous Integration) loaded by `@scrum-master` per Story (across `ready → in-progress → in-review → in-qa`). USE FOR: the HUDDLE → DRIVE → CRITIQUE → ACCEPT/REJECT → SWAP loop on a single Story — Driver codes (`@developer`), Navigator reviews (mandatory CRITIQUE), `@security-expert` on trust boundaries; producing committed code + reviews + tests. DO NOT USE FOR: the ★ PR Gate (Central Supervisor); QA sign-off (use `verification`); Story authoring (use `product-owner`). Loaded by `@scrum-master` before facilitating; returns the integrated unit — the sm commits each edge.'
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

# SAFe Practice — Pair-Programming micro-cycle (Continuous Integration)

A multi-agent micro-cycle (Continuous Integration), Driver ⇄ Navigator — **not** solo work. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the HUDDLE → DRIVE → CRITIQUE → SWAP turns + the Scrum-Master-mediated swap as conditions; the structural `after`/`input`/`output` wiring), consumed by `@scrum-master` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[scrum-master orchestration core](../../../actors/scrum-master/scrum-master.skill.md)**. The mandatory Navigator CRITIQUE precedes `in-qa`; one commit per unit (trailer + pair attribution); the orchestrator writes no code and **only `@scrum-master` writes `status:`** — committing each execution edge (`ready→in-progress`, `in-progress→in-review`, `in-review→in-qa` on accept / `→in-progress` on reject).
