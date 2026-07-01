---
name: verification
user-invocable: false
description: '**SAFe PRACTICE SKILL.** The Verification & Sign-off practice (Continuous Integration / Built-In Quality) loaded by `@scrum-master` per Story (when a Story is `in-qa`). USE FOR: `@quality-engineer` verifying the Story against its Definition of Done + `@security-expert` rendering the trust-boundary verdict, producing the `qa-signoff`. DO NOT USE FOR: the ★ PR Gate (Central Supervisor); coding (use `pair-programming`); the iteration demo (use `iteration-review`). Loaded by `@scrum-master` before facilitating; returns the sign-off — the sm commits `in-qa→awaiting-pr` (or `→in-progress` on fail).'
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

# SAFe Practice — Verification & Sign-off (Built-In Quality)

A **practice** (Continuous Integration) that produces the QA sign-off. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the DoD acceptance + Security verdict + INST audit + sign-off obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@scrum-master` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[scrum-master orchestration core](../../../actors/scrum-master/scrum-master.skill.md)**. The sign-off uses the **qa-signoff** template; no Story reaches `awaiting-pr` without it (observability Stories include the instrumentation-coverage audit, INST-R7/R8 green); **only `@scrum-master` writes `status:`** (`in-qa→awaiting-pr` on pass / `in-qa→in-progress` on fail).
