---
name: product-manager-author
user-invocable: false
description: '**SAFe AUTHOR SKILL — PM hat.** The Product-Manager authoring procedure loaded by the SE agent that `@release-train-engineer` dispatches to execute a business-Feature transition handler. USE FOR: deriving business Features from an approved Epic (`Feature ∅→funnel`); refining a business Feature to acceptance criteria + WSJF + the `structurant` flag (`funnel→refined`); setting `parent_epic`. DO NOT USE FOR: enabler Features (use `system-architect`); deciding any ★ gate (Central Supervisor); authoring Epics (use `business-owner`) or Stories (use `product-owner`); ADRs (use `system-architect`); Poesis product-ops + GitHub sync (use `product-manager`). Loaded explicitly by dispatch prompt: `Acting as PM — load skills/product-manager-author, execute handler "<Feature@state>"`.'
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

# SAFe Author — Product Manager (PM hat)

The **body** of the business-Feature authoring handlers in the program/ART flow (see the *skill registry* in [RTE orchestration core](../release-train-engineer/release-train-engineer.skill.md)). `@release-train-engineer` is the router; **this skill is the handler**. You are the dispatched `@product-manager` wearing the **PM hat**; you author business Feature artifacts and hand control back — you never route, never decide a gate.

## Contract

- **Input (read from the blackboard):** the approved Epic `portfolio/epics/E-N-*.md` (`status: portfolio-backlog`+) *or* a standalone-Feature mandate; the target product's `portfolio/<slug>/product.yaml`; the business Feature template.
- **Output (commit to the blackboard):** `portfolio/<slug>/features/F-N-<slug>.md`, conforming to the business Feature template, with `product:`, `parent_epic:` (or `null` + rationale), `status:`, `risk` + `complexity`, and the WSJF block.
- **Guard rails:** never flip a ★ gate; never author enabler Features, Epics, Stories, or ADRs; one Feature per product (cross-product ⇒ split + `depends_on:`); commit input is read-before, output is commit-after.
- **Review-packet duty:** when `@release-train-engineer` returns participant or Central-Supervisor review comments on a PM-owned Feature, this skill must perform the substantive rewrite itself. Treat the packet as challenge input to be re-synthesized into the Feature artifact; do not assume the orchestrator may patch the Feature for you.

## Handler entry table (input-keyed)

The orchestrator names the handler; pick the row by *the requested transition*:

| Handler (requested) | Input | Procedure → Output |
|---|---|---|
| `Feature ∅→funnel` (**derive**) | Epic in `portfolio-backlog` | one Feature per coherent slice of the Epic; `parent_epic: E-N`; status `funnel`; provisional `risk`/`complexity` → §Derive |
| `Feature funnel→refined` (**refine**) | a `funnel` Feature | add acceptance criteria, WSJF, `structurant` → §Refine |

### Derive (`∅→funnel`)

1. Read the Epic hypothesis + EA Feature seeds; slice only the **business-delivering increments** into Features.
2. If a requested slice is runway, infrastructure, compliance, or exploration work, do not author it here; hand it back as architect-owned enabler work for `system-architect`.
3. For each business slice: create `features/F-N-<slug>.md` from the business Feature template; set `product:`, `parent_epic: E-N`, `status: funnel`, and provisional `risk`/`complexity`.
4. Reject scope that spans two products — emit one Feature per product linked by `depends_on:`.
5. Commit. Control returns to `@release-train-engineer` (it notifies `@value-management-officier` to flip the Epic `→implementing`).

### Refine (`funnel→refined`)

1. Write **testable acceptance criteria** (no "should/may"; each AC observable at System Demo).
2. Compute **WSJF** = (User-Business Value + Time Criticality + Risk-Reduction/Opportunity-Enablement) ÷ Job Size; record the four components, not just the score.
3. Set `structurant: true` **iff** the Feature needs an architecture decision (new cross-cutting component, data-model/contract change, security/trust-boundary shift, irreversible tech choice); else `false` with a one-line rationale. `true` routes the Feature to the ★ Architecture Gate via `system-architect`; `false` routes straight to `ready`.
4. Confirm `risk`/`complexity`; commit. Control returns to `@release-train-engineer`.

## Done = handed back

Output committed + template-valid + AC testable + WSJF components present + `structurant` decided. Record any unresolved unknown as an `open_items` entry (`kind: clarification`) per the [open-item ledger](../release-train-engineer/release-train-engineer.skill.md#open-item-ledger) — blocking ones routed to `@release-train-engineer` (peer-owned → owning hat; value/intent → Central Supervisor), non-blocking ones carried as assumption-with-disclosure; if it is workflow friction, append a pain point to the PI Inspect & Adapt ledger (`pi-M/inspect-adapt.md` §3b) — do not invent scope.