#!/usr/bin/env python3
"""Verify cumulative checkpoint contents against the canonical repository."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
from pathlib import Path


def tracked(root: Path) -> dict[str, str]:
    output = subprocess.check_output(
        ["git", "-C", str(root), "ls-files", "-z"], text=False
    )
    result = {}
    for raw in output.split(b"\0"):
        if not raw:
            continue
        relative = raw.decode()
        result[relative] = hashlib.sha256((root / relative).read_bytes()).hexdigest()
    return result


def require_subset(stage: Path, canonical: Path, allowed_differences: set[str]) -> list[str]:
    stage_files = tracked(stage)
    canonical_files = tracked(canonical)
    errors = []
    for path, digest in stage_files.items():
        if path in allowed_differences:
            continue
        if path not in canonical_files:
            errors.append(f"{stage.name}: {path} is absent from the canonical repository")
        elif canonical_files[path] != digest:
            errors.append(f"{stage.name}: {path} differs from the canonical repository")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    parser.add_argument("checkpoint1", type=Path)
    parser.add_argument("checkpoint2", type=Path)
    parser.add_argument("checkpoint3", type=Path)
    args = parser.parse_args()

    canonical = args.canonical.resolve()
    errors = []
    stage_differences = {"README.md", "checkpoint.json", "RECOVERY_MATRIX.md"}
    errors.extend(require_subset(args.checkpoint1.resolve(), canonical, stage_differences))
    errors.extend(require_subset(args.checkpoint2.resolve(), canonical, stage_differences))

    canonical_files = tracked(canonical)
    checkpoint3_files = tracked(args.checkpoint3.resolve())
    if canonical_files != checkpoint3_files:
        for path in sorted(canonical_files.keys() ^ checkpoint3_files.keys()):
            errors.append(f"Checkpoint 3 path mismatch: {path}")
        for path in sorted(canonical_files.keys() & checkpoint3_files.keys()):
            if canonical_files[path] != checkpoint3_files[path]:
                errors.append(f"Checkpoint 3 content mismatch: {path}")

    if errors:
        print("CHECKPOINT SYNC: FAIL")
        print("\n".join(errors))
        return 1
    print("CHECKPOINT SYNC: PASS")
    print(f"Checkpoint 3 matches {len(canonical_files)} canonical tracked files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
