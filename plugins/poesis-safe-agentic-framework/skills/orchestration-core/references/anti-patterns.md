# Anti-Patterns

Lessons learned from real multi-agent projects. Each anti-pattern was encountered at least once and caused real problems.

## Git & Branching

| Don't | Do Instead | Why |
|-------|------------|-----|
| Rebase feature branches | Regular merge | Rebase rewrites history, loses commits, and breaks pair attribution. When multiple specialists contribute to a branch, rebase causes cascading regressions. |
| Squash merge PRs | Regular merge | Squash hides individual commits and pair attributions, making it impossible to revert a single fix. |
| Push directly to main | Feature branch → PR → ★ PR Gate → merge | Direct pushes bypass the human approval gate and can't be reverted cleanly. |
| Force push (`--force`) | Fix forward or revert | Force push destroys remote history that subagent dispatches may have been pulled against. |
| Merge on green CI without human approval | Halt at the ★ PR Gate, wait for explicit approval | CI is not human approval. Green CI is a precondition, not a substitute, for the ★ PR Gate. |

## Roles

| Don't | Do Instead | Why |
|-------|------------|-----|
| RTE writes production code | RTE only orchestrates, derives Stories, runs acceptance, merges | When the orchestrator starts coding, it loses track of the SAFe flow. Code fixes in the RTE chat conflict with pair work and skip pair attribution. |
| One subagent does everything | Pair every Story (Driver + Navigator) with at least one CRITIQUE step | The CRITIQUE step catches the issues that single-agent code review misses. |
| Skip the architecture runway | ADR-first for any structurant Feature | A Story that ships against an unaddressed architectural concern creates retroactive ADRs nobody can approve cleanly. |
| Ask one chat to roleplay six personas | Dispatch six distinct SE:\* specialists as separate subagents | Roleplay produces bland consensus; separate dispatches produce real diversity because each specialist has its own training and tool palette. |

## Sprint Management

| Don't | Do Instead | Why |
|-------|------------|-----|
| Batch "fix everything" commits | One commit per unit with issue reference and pair attribution | Batch commits make it impossible to track what was fixed. If one fix causes a regression, you can't revert just that fix. |
| Keep bugs only in chat | File GitHub Issues | Chat context dies when the conversation ends. Issues persist across all chats and subagent dispatches — they are part of the shared blackboard. |
| Skip the done.md | Mandatory done.md + PROJECT_BRIEF update at sprint end | Without a handoff doc, the next RTE chat starts blind on `recover state`. It may overwrite work or duplicate effort. |
| Skip progress.md | Update progress.md after each Story | Without a progress tracker, context overflow recovery is impossible. The new RTE chat doesn't know which Stories are in flight. |
| Rush the AI with time pressure | "Take your time, do it right" | Time pressure makes the LLM skip edge cases, write fewer tests, and produce lower quality code. "No rush" produces better results. |

## Acceptance & Quality

| Don't | Do Instead | Why |
|-------|------------|-----|
| Merge before RTE acceptance | Acceptance → file blockers → fix → re-accept → open PR → ★ PR Gate | RTE folds in the QA-acceptance duty. Skipping it means ★ PR Gate reviewers waste cycles catching what RTE should have caught. |
| Let pairs self-accept their own Story | RTE runs acceptance against the Story DoD | Self-acceptance creates blind spots — the pair has training-bias from their own implementation. |
| Close issues without verification | Pair fixes → RTE verifies → close | Self-closing issues skips verification. The fix might not actually work. |

## Context & Communication

| Don't | Do Instead | Why |
|-------|------------|-----|
| Assume subagents share RTE's context | Commit artifacts before dispatching | Subagent calls do not share context with RTE. The filesystem is the shared blackboard. If a subagent needs a Feature or ADR as input, that file must be committed before dispatch. |
| Keep decisions in conversation | Write decisions to ADRs or sprint docs | Decisions made in chat are lost when the chat closes. Write to `docs/architecture/` or `docs/sprint-N/`. |
| Relay raw error logs between dispatches | Summarize and file as GitHub Issue | Raw logs waste tokens in the next dispatch. Summarize: Story, component, steps, expected, actual. |
