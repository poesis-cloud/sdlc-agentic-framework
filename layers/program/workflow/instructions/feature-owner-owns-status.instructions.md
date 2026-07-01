---
description: 'the Feature — including its status: — is authored by its owner (@product-manager for business, @system-architect for enabler); @release-train-engineer governs the transition via the transition guard and the program kanban it owns, not by writing the Feature'
---

# Invariant: feature_owner_owns_status

The Feature — including its `status:` — is authored by its owner (@product-manager for business, @system-architect for enabler). @release-train-engineer governs the status transition through the transition guard (`check-artifact --to`) and records it in the @release-train-engineer-owned program kanban; it does not write the Feature itself.
