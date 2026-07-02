#!/usr/bin/env python3
"""Workflow migration script: Convert old condition model to new model.

Conservative migration strategy (backward compatible):
1. type: after, expression: ref, value: <step_id>
   → type: after, step_id: <step_id>  (MIGRATE)
2. kind: invariant, type: authority
   → Remove entirely (RBAC-only)  (MIGRATE)
3. Everything else → Keep as-is during migration  (NO CHANGE)

This conservative approach ensures all conditions remain valid during
the gradual migration to the new model.

Run: python3 migrate_workflows.py
"""

import sys
from pathlib import Path
import yaml

def migrate_condition(cond: dict) -> dict | None:
    """Migrate a single condition. Return None to remove it."""
    kind = cond.get("kind", "")
    ctype = cond.get("type", "")
    expression = cond.get("expression", "")
    value = cond.get("value", "")
    cid = cond.get("id", "")

    # Rule 1: type: after, expression: ref → type: after, step_id
    if ctype == "after" and expression == "ref" and value:
        return {
            "id": cid,
            "kind": kind,
            "type": "after",
            "step_id": value,
        }

    # Rule 2: kind: invariant, type: authority → remove (RBAC-only)
    if kind == "invariant" and ctype == "authority":
        return None

    # Rule 3: kind: invariant, type: clarification → remove (guidance, not checks)
    if kind == "invariant" and ctype == "clarification":
        return None

    # Everything else: keep as-is for backward compatibility
    return cond


def migrate_workflow(wf_path: Path) -> tuple[bool, str]:
    """Migrate a single workflow file. Returns (success, message)."""
    try:
        with open(wf_path) as f:
            data = yaml.safe_load(f)
        
        if not data or "workflow" not in data:
            return False, f"no workflow key in {wf_path}"

        workflow = data["workflow"]
        if "steps" not in workflow:
            return True, f"no steps in {wf_path} (skipped)"

        original_count = 0
        migrated_count = 0
        removed_count = 0
        instructions_added = 0

        for step in workflow["steps"]:
            if "conditions" not in step:
                continue
            
            old_conditions = step["conditions"]
            original_count += len(old_conditions)
            
            # Collect instructions from clarification invariants
            step_instructions = step.get("instructions", [])
            if isinstance(step_instructions, str):
                step_instructions = [step_instructions]
            else:
                step_instructions = list(step_instructions) if step_instructions else []
            
            new_conditions = []
            for cond in old_conditions:
                migrated = migrate_condition(cond)
                if migrated is not None:
                    new_conditions.append(migrated)
                    migrated_count += 1
                else:
                    # If it's a removed clarification invariant, extract the instruction file
                    if cond.get("kind") == "invariant" and cond.get("type") == "clarification":
                        instr_file = cond.get("value")
                        if instr_file and instr_file not in step_instructions:
                            step_instructions.append(instr_file)
                            instructions_added += 1
                    removed_count += 1

            step["conditions"] = new_conditions
            if step_instructions:
                step["instructions"] = step_instructions

        # Write back
        with open(wf_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        msg = f"{wf_path.name}: {original_count} conds → {migrated_count} kept + {removed_count} removed"
        if instructions_added:
            msg += f" (+{instructions_added} to step.instructions)"
        return True, msg

    except Exception as e:
        return False, f"{wf_path.name}: ERROR: {e}"


def main() -> int:
    framework_root = Path("/home/clem/repositories/poesis/safe-agentic-framework")
    workflow_files = sorted(framework_root.glob("**/workflow.yaml"))

    print(f"Migrating {len(workflow_files)} workflow files (conservative strategy)...")
    successes = 0
    failures = 0

    for wf_path in workflow_files:
        ok, msg = migrate_workflow(wf_path)
        if ok:
            print(f"  ✓ {msg}")
            successes += 1
        else:
            print(f"  ✗ {msg}")
            failures += 1

    print(f"\nResult: {successes} success, {failures} failures")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

