---
name: retrospective
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The Iteration Retrospective playbook loaded by `@scrum-master` per Story (on `done`). USE FOR: running the team retro; root-causing sprint-scope pain points from the workflow-improvement ledger; writing `sprint-N/retro.md` (with the Central Supervisor input section); escalating program-scope items to Inspect & Adapt. DO NOT USE FOR: the PI retro (use `inspect-and-adapt`); the increment demo (use `iteration-review`). Loaded by `@scrum-master` before facilitating.'
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

# SAFe Ceremony — Iteration Retrospective

The **sprint-scope** review point of the workflow-improvement ledger. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the observation + root-cause + triage obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@scrum-master` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[scrum-master orchestration core](../../../actors/scrum-master/scrum-master.skill.md)**. The Central Supervisor fills a mandatory input section; an iteration-local improvement is a meta-artifact change while program-scope items escalate **up** to Inspect & Adapt; **only `@scrum-master` writes `status:`**.