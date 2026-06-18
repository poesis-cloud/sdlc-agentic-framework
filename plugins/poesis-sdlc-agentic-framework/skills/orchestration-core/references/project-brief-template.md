# PROJECT_BRIEF.md Template

Copy this template to your project root and fill in every section. **Do not abbreviate sections 12-14** — they are critical for cross-chat context survival.

---

```markdown
# PROJECT_BRIEF.md — [Project Name]

> Last updated: [date] | PI [M] | Sprint [N] | Status: [In Progress / Complete]

## 1. Project Overview

[3-4 sentences describing what the project is, who it's for, and the core goal.]

## 2. Concept / Product Description

[Detailed description of the product — user flows, key features, narrative if applicable.]

## 3. Tech Stack

- **Frontend:** [framework, language, key libraries]
- **Backend:** [runtime, framework, database]
- **Hosting:** [platform, CDN, storage]
- **Testing:** [test framework, E2E tool]
- **CI/CD:** [pipeline tool]

## 4. Architecture

```
┌─────────────────────────────────────────┐
│              Frontend                    │
│  [Main Component] → [Sub Components]    │
└──────────────┬──────────────────────────┘
               │ HTTPS
┌──────────────▼──────────────────────────┐
│              Backend API                 │
│  [Endpoints and their purpose]          │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│              Storage / Database          │
│  [Tables, collections, env vars]        │
└─────────────────────────────────────────┘
```

## 5. Key Files Map

| Area | Path | Contents |
|------|------|----------|
| Entry point | `src/main.tsx` | App bootstrap |
| API | `api/src/` | Server-side logic |
| Config | `api/src/config/` | Server-only configuration |
| Tests | `tests/` | E2E and API tests |
| Portfolio | `docs/portfolio/` | Epics |
| Features | `docs/features/` | Features (F-NN-<slug>.md) |
| Architecture | `docs/architecture/` | ADRs |
| PI | `docs/pi-M/` | PI objectives, Inspect & Adapt |
| Sprint docs | `docs/sprint-N/` | Plan, progress, done, stories, retro |
| QA sign-off | `docs/qa/` | Sprint sign-off docs |

## 6. Team Roles

| Role | Agent | Owns |
|------|-------|------|
| RTE / Orchestrator | `@rte-orchestrator` | Drives the SAFe flow, derives Stories, assigns pairs, runs acceptance, merges PRs after approval. Never writes production code. |
| Product Management | `SE: Product Manager` | Features (`docs/features/F-NN-<slug>.md`), Program Backlog, WSJF ranking |
| Architecture | `SE: Architect` | ADRs (`docs/architecture/adr-NNN-*.md`, `status: proposed` until human approves) |
| Generic Dev | default Copilot agent | Code for Stories that don't need a specialist (dispatched by RTE) |
| Security | `SE: Security` | Auth, crypto, secrets, threat-model-driven code |
| Platform / CI | `SE: DevOps/CI` | CI/CD, Helm, deployment, env config |
| Docs | `SE: Tech Writer` | Story-attached docs, ADR prose, release notes |
| UX | `SE: UX Designer` | UX journeys, Figma specs |
| RAI / Accessibility | `SE: Responsible AI` | Accessibility Enablers, bias review |
| Business Owner / Approver | **You** (human) | Submits + approves Epics at the ★ Epic Gate; approves ADRs / PRs / System Demo at the ★ ADR / ★ PR / ★ Feature gates |

## 7. Sprint Status

| PI | Sprint | Name | Status | Scope |
|----|--------|------|--------|-------|
| 1 | 0 | Architecture runway | ✅ Done | Tech stack, project structure, initial ADRs |
| 1 | 1 | Core Features | 🔨 In Progress | [scope description] |

## 8. Current State (rewrite every sprint)

**What works:**
- [List of working features]

**What doesn't work yet:**
- [Known issues]

**What's next:**
- [Next sprint goals]

## 9. Security Rules

1. Secrets live in environment variables only — never in code or git.
2. [Auth approach]
3. [Additional security rules]

## 10. How to Run Locally

```bash
npm install
cd api && npm install
cp api/local.settings.json.example api/local.settings.json
npm run dev:all
```

## 11. How to Deploy

[Pipeline description, env var locations, deployment steps]

## 12. Cross-Chat Handoff Protocol

When the RTE chat overflows or restarts, the human says **`@rte-orchestrator — recover state.`** RTE then:

1. Reads `PROJECT_BRIEF.md`.
2. Reads `docs/portfolio/`, `docs/features/`, `docs/architecture/` (latest ADRs), `docs/pi-*/` (current PI), `docs/sprint-N/` (current sprint).
3. Runs `gh pr list` and `gh issue list`.
4. Reports current PI, current Sprint, in-flight Stories, open ADRs awaiting the ★ ADR Gate, open PRs awaiting the ★ PR Gate, next action.
5. Waits for human confirmation before dispatching.

Every sprint, before the RTE chat closes:
1. RTE writes `docs/sprint-N/done.md`.
2. RTE updates this brief — Section 7 (mark sprint done) + Section 8 (rewrite current state).
3. RTE commits with a descriptive `sprint-N: <summary>` message and the Copilot trailer.

The repo is the shared blackboard — keep it accurate.

## 13. Bug & Fix Tracking

Bugs are tracked as GitHub Issues on the repo. Single source of truth.

**For RTE (acceptance duty):** When acceptance against a Story DoD fails, file an Issue with labels (`bug`, `severity:blocker/major/minor`). Include: Story ID, component, steps, expected vs actual. Write `docs/qa/sprint-N-signoff.md` with test count, pass rate, blocker list. RTE will not open the PR for the ★ PR Gate with open blockers.

**For Dev pairs:** Check open Issues before starting a Story. Fix referenced Issues in pair commits using GitHub closing keywords: `fix: description (Fixes #42)`. For reference-only, use `Refs #42`.

**For infrastructure:** label `infra`. Routed to a pair with `SE: DevOps/CI` as Driver or Navigator.

**For feature ideas:** add to `docs/portfolio/ideas-backlog.md`. RTE batches them into the next Epic intake.

## 14. Repo & Branch Strategy

Single git repo. One branch per sprint (`feature/sprint-N`). One RTE chat per Epic.

**Branch lifecycle:**
1. RTE creates `feature/sprint-N` from `main` at Iteration Planning.
2. All Story commits land on `feature/sprint-N` with pair attribution + Copilot trailer.
3. RTE runs acceptance, opens PR.
4. ★ PR Gate — human approves PR.
5. RTE merges (regular merge — **never squash, never rebase**).
6. RTE deletes the branch.

**Rules:**
- Never push directly to `main`.
- Never squash merge (loses individual fix commits).
- Never rebase a feature branch (loses commits and breaks pair history).
- Force push is forbidden — fix forward or revert.
- Every commit ends with `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`. Pair commits also carry `(pair: <Driver>/<Navigator>)` in the subject.
```
