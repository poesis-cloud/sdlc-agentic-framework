#!/usr/bin/env python3
"""Render the GitHub Copilot bundle from host-agnostic source agents."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import yaml

SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", "dist", "target"}


def _ignore(_root: str, names: list[str]) -> set[str]:
    return {name for name in names if name in SKIP_DIRS}


def _inject_tools(agent_path: Path, tools: list[str]) -> None:
    lines = agent_path.read_text().splitlines(keepends=True)
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError(f"agent file lacks YAML frontmatter: {agent_path}")

    frontmatter_end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter_end = index
            break
    if frontmatter_end is None:
        raise ValueError(f"agent frontmatter is not closed: {agent_path}")

    rendered = f"tools: [{', '.join(tools)}]\n"
    for index in range(1, frontmatter_end):
        if lines[index].startswith("tools:"):
            lines[index] = rendered
            break
    else:
        lines.insert(frontmatter_end, rendered)

    agent_path.write_text("".join(lines))


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: render_bundle.py <source-root> <bundle-root>", file=sys.stderr)
        return 2

    source_root = Path(sys.argv[1]).resolve()
    bundle_root = Path(sys.argv[2]).resolve()
    build_root = source_root / "builds" / "github-copilot"
    manifest_path = build_root / "plugin.json"
    tools_map_path = build_root / "tools.map.yaml"

    if bundle_root.exists():
        shutil.rmtree(bundle_root)
    shutil.copytree(source_root, bundle_root, ignore=_ignore)

    manifest = json.loads(manifest_path.read_text())
    tools_map = yaml.safe_load(tools_map_path.read_text()) or {}
    agent_tools = tools_map.get("agents", {})

    missing = [rel for rel in manifest.get("agents", []) if rel not in agent_tools]
    extra = sorted(set(agent_tools) - set(manifest.get("agents", [])))
    if missing or extra:
        if missing:
            print("missing tools map entries:", file=sys.stderr)
            for rel in missing:
                print(f"  - {rel}", file=sys.stderr)
        if extra:
            print("tools map contains non-manifest agents:", file=sys.stderr)
            for rel in extra:
                print(f"  - {rel}", file=sys.stderr)
        return 1

    for rel in manifest.get("agents", []):
        _inject_tools(bundle_root / rel, list(agent_tools[rel]))

    (bundle_root / "plugin.json").write_text(manifest_path.read_text())
    print(f"rendered GitHub Copilot bundle: {bundle_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())