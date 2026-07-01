---
description: 'the Feature — including its status: — is authored by its owner (@product-manager for business, @system-architect for enabler); @release-train-engineer governs the transition via the transition guard and the program kanban; ADRs, decision inventory, runway/NFR registers stay @system-architect-owned'
---

# Invariant: feature_owner_owns_status_architecture_stays_sa_owned

The Feature — including its `status:` — is authored by its owner (@product-manager for business, @system-architect for enabler). @release-train-engineer governs the status transition through the transition guard (`check-artifact --to`) and the @release-train-engineer-owned program kanban; it does not write the Feature. ADRs, the architecture decision inventory, and the runway/NFR registers stay @system-architect-owned — the RTE collates only flow-owned outputs.
