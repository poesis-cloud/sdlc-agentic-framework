# Portfolio Init Template — `portfolio/`

The portfolio is the **meta-governance** tier above the ARTs (one ART per product). It is a
poesis-wide singleton, created once. The **Business Owner** + **Enterprise Architect** hats
(both you) own it; the RTE renders and maintains it.

## Folder tree (singleton)

```
portfolio/
  portfolio.yaml          # manifest (this template)
  strategic-themes.md     # strategic-themes.artifact-template.md
  epics/                  # E-N-<slug>.md (epic.artifact-template.md)
  kanban/
    portfolio.md          # rendered (kanban-portfolio.artifact-template.md); never hand-edited
  github-sync.yaml        # Portfolio Project sync config (github-sync-config-template)
  .gitkeep in empty dirs
```

## Manifest — `portfolio/portfolio.yaml`

```yaml
# portfolio/portfolio.yaml
scope: portfolio
name: Poesis Portfolio
business_owner: central-supervisor       # BO hat (Go/No-Go, value authority)
enterprise_architect: central-supervisor # EA hat (cross-product runway, NFR backbone)
created: YYYY-MM-DD

# Canonical global portfolio configuration and product registry.
# `products:` is authoritative; `arts:` may be retained as a derived compatibility list.
products:
  - slug: itip-web
    path: portfolio/itip-web
    topology: submodule
  - slug: itip-blackboard-sourcer
    path: portfolio/itip-blackboard-sourcer
    topology: submodule
  - slug: sie-blackboard
    path: portfolio/sie-blackboard
    topology: submodule
  - slug: sie-definition
    path: portfolio/sie-definition
    topology: submodule

# Epics may span any subset of these via their `products:` list.
arts:
  - itip-web
  - itip-blackboard-sourcer
  - sie-blackboard
  - sie-definition

github_project: null      # filled by `provision portfolio` (Portfolio Project URL)
```

## Init checklist (RTE runs this once)

- [ ] Create `portfolio/` tree with `.gitkeep` in `epics/`, `kanban/`.
- [ ] Write `portfolio.yaml` with `products[]` as the authoritative registry and `arts[]` as the compatibility list where older tooling still expects it.
- [ ] Seed `strategic-themes.md` from `strategy/POESIS-STRATEGY.md` + business lines.
- [ ] Generate `github-sync.yaml` (portfolio variant) and `provision` the Portfolio Project.

## Relationship to products

- The portfolio does **not** own product code or product Features — it owns **Epics**.
- An Epic's child Features stay product-scoped (`parent_epic: E-N` in the Feature frontmatter).
- Cross-product coordination is expressed at the Epic level only; the "no cross-product Feature"
  rule is unchanged (one Feature per product, each linked to the shared Epic).
