---
name: system-demo
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The System Demo playbook loaded by `@release-train-engineer`. This ceremony **stages the ★ Demo Gate**: it presents the integrated increment for the Central Supervisor, who decides. USE FOR: staging the System Demo of an `in-progress` Feature; on accept `@release-train-engineer` flips Feature `in-progress→done`, commits the Feature `cost:` once, notifies `@value-management-officier`, and writes the I&A input. DO NOT USE FOR: making the accept decision yourself (the Central Supervisor decides); the PI retro (use `inspect-and-adapt`). Loaded by `@release-train-engineer` before staging.'
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

# SAFe Ceremony — System Demo (the ★ Demo Gate)

Stages the **★ Demo Gate**. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the per-actor verdicts + gate-staging obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@release-train-engineer` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[RTE orchestration core](../../../actors/release-train-engineer/release-train-engineer.skill.md)**. The facilitator **stages, never decides** — it demos the *integrated* increment against the Feature's acceptance criteria (not slideware); **the Central Supervisor decides** accept/rework; on accept **only `@release-train-engineer` writes `status:`** (`in-progress→done`), commits the immutable `cost:` block once, and notifies `@value-management-officier` for the Epic outcome.