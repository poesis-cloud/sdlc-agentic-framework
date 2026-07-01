---
name: architectural-vision
user-invocable: false
description: '**SAFe PRACTICE SKILL.** The Architectural Vision practice (Continuous Exploration) loaded by `@value-management-officier` per Epic (when a `reviewing` Epic needs its runway + NFR backbone toward `analyzing`). USE FOR: `@enterprise-architect` authoring the Architectural Vision, the NFR backbone, and the architectural-runway register; seeding **enabler Epics** for runway gaps; setting Feature seeds + target ARTs; business-owner challenges scope/value. DO NOT USE FOR: the ★ Epic Gate (Central Supervisor); ART-level ADRs (use `architectural-runway-extension`); the Epic hypothesis (use `epic-lean-business-case`). Loaded by `@value-management-officier` before facilitating; returns the runway-augmented Epic or a replay-required result when late enabler seeding invalidates prior business shaping; the VMO commits.'
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

# SAFe Practice — Architectural Vision (Continuous Exploration)

A **practice** (Continuous Exploration) that establishes the cross-product **architectural runway** + **NFR** backbone. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the participant challenges + facilitation obligations as judgment conditions; the structural `after`/`input`/`output` wiring), consumed by `@value-management-officier` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[VMO orchestration core](../../../actors/value-management-officier/value-management-officier.skill.md)**. The runway + Vision are authored via `enterprise-architect`, and **only `@value-management-officier` writes `status:`** (`reviewing→analyzing`). On a runway gap the pass may seed enabler Epics (dedicated enabler template); if that invalidates the parent Epic's shaping it returns a **replay-required** outcome that routes the Epic back through **Epic Lean Business Case**.
