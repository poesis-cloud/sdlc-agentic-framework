---
name: iteration-planning
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The Iteration Planning playbook loaded by `@scrum-master` per Feature (when it reaches `committed`). USE FOR: writing `sprint-N/plan.md`; seeding Stories from committed Features; running the ★ Story Gate (Definition of Ready) for `backlog→ready`; assigning Driver/Navigator pairs; verifying `risk`/`complexity`. It seeds Stories and runs the ★ Story Gate (DoR); `@scrum-master` commits Story `∅→backlog` and `backlog→ready`. DO NOT USE FOR: the ★ PR Gate (Central Supervisor); authoring Stories yourself (use `product-owner` for business Stories and `system-architect` for enabler Stories); the retro (use `retrospective`). Loaded by `@scrum-master` before facilitating.'
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

# SAFe Ceremony — Iteration Planning

The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the per-actor authoring + challenges + the sm-run ★ Story Gate (DoR) obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@scrum-master` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[scrum-master orchestration core](../../../actors/scrum-master/scrum-master.skill.md)**. Business Stories are authored via `product-owner`, enabler Stories via `system-architect`; **the ★ Story Gate (DoR) is sm-run here** (never the ★ PR Gate); **only `@scrum-master` writes `status:`** — on the first Story reaching `ready` it notifies `@release-train-engineer` to flip the parent Feature `committed→in-progress`.
Plan written + Stories DoR-gated + pairs assigned + `@release-train-engineer` notified on first `ready`; relation discipline stays minimal and actionable.