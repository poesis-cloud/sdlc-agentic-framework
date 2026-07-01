---
description: 'the Story — including its status: — is authored by its owner (@product-owner for business, @system-architect for enabler); @scrum-master governs the transition via the transition guard and the team kanban it owns, not by writing the Story'
---

# Invariant: story_owner_owns_status

The Story — including its `status:` — is authored by its owner (@product-owner for business, @system-architect for enabler). @scrum-master governs the status transition through the transition guard (`check-artifact --to`) and records it in the @scrum-master-owned team kanban; it does not write the Story itself.
