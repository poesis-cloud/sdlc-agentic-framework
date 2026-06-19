# Product manifest template — `portfolio/<slug>/product.yaml`

```yaml
# portfolio/<slug>/product.yaml
slug: <slug>                          # kebab-case; matches folder name
name: <Human readable name>
description: <one-line>
business_line: commercial             # theory | commercial | infra
status: active                        # active | paused | sunset | exploration
owner: central-supervisor                       # always 'central-supervisor' in single-user mode
created: YYYY-MM-DD

# Repos attached to this product (workspace-relative paths).
# Only these repos may receive commits from Stories of this product.
repos:
  - <relative/path/to/repo>

# Cross-product relationships (referenced by `depends_on:` in Feature/Story frontmatter).
upstream: []                          # products this one consumes
downstream: []                        # products that consume this one

# Optional pointers.
project_brief: <path/to/PROJECT_BRIEF.md or null>
github_project: <url or null>
```

## Status lifecycle

`exploration → active → paused → sunset` (one-way after sunset).

## Init checklist (RTE runs this in Product Init step 0)

- [ ] Slug is kebab-case and unique in `portfolio/_registry.yaml`.
- [ ] All paths in `repos[]` exist in the workspace.
- [ ] `business_line` is one of `theory | commercial | infra`.
- [ ] Subfolders created with `.gitkeep`: `prd/`, `features/`, `architecture/`, `kanban/`.
- [ ] Entry appended to `portfolio/_registry.yaml`.
