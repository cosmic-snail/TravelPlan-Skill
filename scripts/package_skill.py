#!/usr/bin/env python3
"""Build a deterministic skill.zip for plan-travel-guide."""

from __future__ import annotations

import argparse
import stat
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "plan-travel-guide"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def zip_info(name: str, is_dir: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
    if is_dir:
        info.external_attr = (stat.S_IFDIR | 0o755) << 16
    else:
        info.external_attr = (stat.S_IFREG | 0o644) << 16
    return info


def add_file(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    archive.writestr(zip_info(arcname), source.read_bytes())


def build(output_path: Path) -> None:
    required = [
        SKILL_DIR / "SKILL.md",
        SKILL_DIR / "agents" / "openai.yaml",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        missing_list = ", ".join(str(path.relative_to(ROOT)) for path in missing)
        raise FileNotFoundError(f"missing required skill files: {missing_list}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(zip_info("plan-travel-guide/", is_dir=True), b"")
        archive.writestr(zip_info("plan-travel-guide/agents/", is_dir=True), b"")
        add_file(archive, SKILL_DIR / "agents" / "openai.yaml", "plan-travel-guide/agents/openai.yaml")
        add_file(archive, SKILL_DIR / "SKILL.md", "plan-travel-guide/SKILL.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output",
        nargs="?",
        default=ROOT / "outputs" / "skill.zip",
        type=Path,
        help="output zip path, defaults to outputs/skill.zip",
    )
    args = parser.parse_args()

    try:
        build(args.output)
    except Exception as exc:
        print(f"Packaging failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
