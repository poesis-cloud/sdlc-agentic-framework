---
name: inspect-and-adapt
user-invocable: false
description: '**SAFe CEREMONY SKILL.** The Inspect & Adapt playbook loaded by `@release-train-engineer` per Feature (on `done`; synthesised at an Epic's completion). USE FOR: the PI quantitative measurement + the problem-solving workshop; root-causing program-scope pain points from the workflow-improvement ledger; seeding enabler Features for systemic gaps; writing `inspect-adapt.md`. DO NOT USE FOR: the ★ Demo Gate (use `system-demo`); portfolio re-ranking (use `strategic-portfolio-review`); the sprint retro (use `retrospective`). Loaded by `@release-train-engineer` before facilitating.'
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

# SAFe Ceremony — Inspect & Adapt

The **program-scope** review point of the workflow-improvement ledger. The **normative spec** is the machine-readable **[workflow.yaml](workflow.yaml)** — every step + its `conditions` (the trigger as the first step's preconditions; the aggregation + root-cause + triage obligations as conditions; the structural `after`/`input`/`output` wiring), consumed by `@release-train-engineer` and the harness (`check-step` / `check-artifact`). Load and follow it; do not restate it here.

Shared model (the open-item ledger, ★ gates, the bench, invariants, artifact templates) lives in **[RTE orchestration core](../../../actors/release-train-engineer/release-train-engineer.skill.md)**. A workflow-improvement is a meta-artifact change (never a product Feature); a product gap may become an enabler Feature (`∅→funnel`). **Only `@release-train-engineer` writes `status:`**.
PI measured + retros aggregated + top problems root-caused + improvements recorded.