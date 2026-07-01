---
description: 'the Epic — including its status: — is authored by its owner (@business-owner for business, @enterprise-architect for enabler); @value-management-officier governs the transition via the transition guard and the portfolio kanban it owns, not by writing the Epic'
---

# Invariant: epic_owner_owns_status

The Epic — including its `status:` — is authored by its owner (@business-owner for business, @enterprise-architect for enabler). @value-management-officier governs the status transition through the transition guard (`check-artifact --to`) and records it in the @value-management-officier-owned portfolio kanban; it does not write the Epic itself.
