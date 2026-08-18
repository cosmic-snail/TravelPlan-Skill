#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="${1:-"$ROOT/outputs/skill.zip"}"

python3 "$ROOT/scripts/package_skill.py" "$OUTPUT"
python3 "$ROOT/scripts/validate_skill_repo.py" --zip "$OUTPUT"
