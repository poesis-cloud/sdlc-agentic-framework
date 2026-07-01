---
description: 'the Story — including its status: — is authored by its owner (@product-owner for business, @system-architect for enabler); @scrum-master governs the transition via the transition guard and the team kanban; @quality-engineer and @security-expert record verdicts only'
---

# Invariant: story_owner_owns_status_qa_security_verdicts_only

The Story — including its `status:` — is authored by its owner (@product-owner for business, @system-architect for enabler). @scrum-master governs the status transition through the transition guard (`check-artifact --to`) and the @scrum-master-owned team kanban. @quality-engineer and @security-expert record their verdicts in their own review artifacts only — they do not write the Story.
