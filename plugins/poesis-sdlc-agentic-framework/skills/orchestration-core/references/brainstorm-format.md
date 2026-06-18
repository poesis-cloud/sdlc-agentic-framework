# Brainstorm Format

Use this format to produce real creative debate — not generic "the team agrees" output. The key is dispatching to **distinct SE:\* specialists** so each voice has its own training and tool palette, instead of asking one chat to roleplay personas.

In the single-orchestrator model, **`@rte-orchestrator` runs the brainstorm by dispatching each phase to the right specialists as subagents** and stitching their committed artifacts into the final summary.

## RTE prompt template

```
@rte-orchestrator — Run a brainstorm on [PROJECT NAME / TOPIC].

Phase 1 — Free Ideation:
Dispatch each of the following specialists in a separate subagent call.
Each writes 2-3 raw ideas from their lens to its own committed file.
  - SE: Product Manager  → docs/brainstorm/01-pm-ideas.md
                            (lens: business value, benefit hypothesis, WSJF)
  - SE: UX Designer      → docs/brainstorm/01-ux-ideas.md
                            (lens: user journey, accessibility, delight)
  - SE: Architect        → docs/brainstorm/01-arch-ideas.md
                            (lens: structural fit, NFRs, architectural runway)
  - SE: Security         → docs/brainstorm/01-sec-ideas.md
                            (lens: threat model, data classification, trust boundaries)
  - SE: DevOps/CI        → docs/brainstorm/01-devops-ideas.md
                            (lens: deployability, observability, CI cost)
  - SE: Responsible AI   → docs/brainstorm/01-rai-ideas.md
                            (lens: bias, accessibility compliance, inclusivity)

Phase 2 — Discussion & Refinement:
RTE collates the 6 idea files into docs/brainstorm/02-discussion.md.
Then dispatches each specialist again, asking them to critique the
other lenses' top ideas and surface at least 2 genuine disagreements.
Each specialist appends their critique to docs/brainstorm/02-discussion.md.

Phase 3 — Final Concepts:
RTE synthesizes 3-5 polished concepts into separate files:
  docs/brainstorm/03-concept-[A/B/C...].md
Each concept includes: name, description, pros, cons, NFR impact,
estimated effort, lens-by-lens scorecard.

Phase 4 — Vote & Summary:
RTE dispatches each specialist for an explicit vote with justification.
  docs/brainstorm/04-team-vote.md  (one row per specialist)
RTE writes the final pick and rationale.
  docs/brainstorm/05-summary.md

Halt at Phase 3 for human review if a concept touches an
existing ADR — the Architect must draft an ADR addendum
(status: proposed) before the vote.
```

## Tips

- **Dispatch separate specialists** — one chat roleplaying six personas produces bland consensus; six distinct subagent calls produce real diversity.
- **One committed artifact per voice per phase** — subagent calls don't share a context window. The filesystem is the shared blackboard.
- **Require disagreements** — "at least 2 genuine disagreements" prevents groupthink.
- **Customize the bench** — drop specialists that don't apply (e.g. no UX for a backend-only tool); add domain-specific specialists by extending the SE:\* bench.

## Mini-Brainstorm (quick version)

For smaller decisions where a 4-phase brainstorm is overkill:

```
@rte-orchestrator — Run a 2-phase mini-brainstorm on [TOPIC].
  Phase 1: dispatch [SE: X], [SE: Y], [SE: Z] for one idea each
           into docs/[topic]-ideas.md (3 sections).
  Phase 2: collate + recommend in docs/[topic]-design.md.
```

## Pre-sprint consilium

Before starting a sprint, validate the plan:

```
@rte-orchestrator — Run a consilium on docs/sprint-N/plan.md.
Dispatch each relevant specialist to review from their lens:
  - SE: Product Manager: do the Stories trace to a ranked Feature?
  - SE: Architect: are all dependent ADRs accepted (★ ADR Gate clean)?
  - SE: Security: any Story crossing a trust boundary without
                  SE: Security on the pair?
  - SE: DevOps/CI: any Story that needs a CI / Helm change not scoped
                   as an Enabler?
  - SE: Tech Writer: docs Enabler missing for any externally-visible change?

Each writes findings to docs/sprint-N/consilium.md.
RTE flags blockers and proposes plan amendments before Iteration Planning closes.
```
