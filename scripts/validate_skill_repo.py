#!/usr/bin/env python3
"""Validate the plan-travel-guide skill repository layout and package."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "plan-travel-guide"
SKILL_MD = SKILL_DIR / "SKILL.md"
AGENT_YAML = SKILL_DIR / "agents" / "openai.yaml"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"
COMMUNITY_GUIDE = ROOT / "docs" / "community-sharing.md"
VALIDATE_WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
PACKAGE_SCRIPT = ROOT / "scripts" / "package_skill.py"
PACKAGE_SHELL = ROOT / "scripts" / "package.sh"

EXPECTED_ZIP_ENTRIES = {
    "plan-travel-guide/",
    "plan-travel-guide/agents/",
    "plan-travel-guide/agents/openai.yaml",
    "plan-travel-guide/SKILL.md",
}

REQUIRED_SKILL_TERMS = [
    "Map/OTA/Ticketing Category Sweep",
    "Local Vocabulary Discovery",
    "Universal Keyword Bank",
    "destination-relevant equivalents",
    "Theme Reconnaissance",
    "Theme Profile",
    "Discovery Evidence Matrix",
    "TopK",
    "完整 POI 总表",
    "按天行程",
    "小红书",
    "抖音",
    "微博/新浪",
    "B站",
]

FORBIDDEN_GENERIC_SKILL_TERMS = [
    "A馆",
    "B馆",
    "C馆",
    "D馆",
    "E馆",
    "连廊",
    "负一层",
    "6楼",
    "MTR",
    "新玛特",
    "吾悦",
    "恒隆",
    "大悦城",
]

FORBIDDEN_README_EXAMPLE_TERMS = [
    "东京",
    "成都",
    "上海南京路",
    "香港旺角",
    "沈阳",
]

REQUIRED_README_TERMS = [
    "# Plan Travel Guide Skill",
    "安装",
    "使用",
    "$plan-travel-guide",
    "旅行目的地",
    "日期强烈建议提供",
    "地图/OTA/票务候选池扫描",
    "本地词汇发现",
    "通用关键词库",
    "最小来源组合",
    "等价平台",
    "主题画像",
    "发现证据矩阵",
    "完整 POI 总表",
    "按天行程",
    "打包",
    "skill.zip",
    "验证",
    "维护",
    "npx skills add cosmic-snail/TravelPlan-Skill",
    "skills.sh",
    "MIT",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_frontmatter(markdown: str) -> dict[str, str]:
    if not markdown.startswith("---\n"):
        return {}
    try:
        _, frontmatter, _ = markdown.split("---", 2)
    except ValueError:
        return {}

    parsed: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip().strip('"')
    return parsed


def validate_repo() -> list[str]:
    errors: list[str] = []

    for path in [
        SKILL_MD,
        AGENT_YAML,
        README,
        LICENSE,
        COMMUNITY_GUIDE,
        VALIDATE_WORKFLOW,
        PACKAGE_SCRIPT,
        PACKAGE_SHELL,
    ]:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    skill = read_text(SKILL_MD)
    if skill:
        frontmatter = parse_frontmatter(skill)
        if frontmatter.get("name") != "plan-travel-guide":
            errors.append("SKILL.md frontmatter name must be plan-travel-guide")
        description = frontmatter.get("description", "")
        if not description.startswith("Use when "):
            errors.append("SKILL.md description must start with 'Use when '")
        if len(description) > 500:
            errors.append("SKILL.md description should stay under 500 characters")
        for term in REQUIRED_SKILL_TERMS:
            if term not in skill:
                errors.append(f"SKILL.md missing required term: {term}")
        for term in FORBIDDEN_GENERIC_SKILL_TERMS:
            if term in skill:
                errors.append(f"SKILL.md contains over-specific generic-search example: {term}")

    agent = read_text(AGENT_YAML)
    if agent:
        for term in [
            'display_name: "Plan Travel Guide"',
            "short_description:",
            "default_prompt:",
        ]:
            if term not in agent:
                errors.append(f"agents/openai.yaml missing required term: {term}")

    readme = read_text(README)
    if readme:
        for term in REQUIRED_README_TERMS:
            if term not in readme:
                errors.append(f"README.md missing required term: {term}")
        for term in FORBIDDEN_README_EXAMPLE_TERMS:
            if term in readme:
                errors.append(f"README.md contains over-specific example: {term}")

    license_text = read_text(LICENSE)
    if license_text:
        for term in [
            "MIT License",
            "Copyright (c) 2026 cosmic-snail",
            "Permission is hereby granted",
        ]:
            if term not in license_text:
                errors.append(f"LICENSE missing required term: {term}")

    workflow = read_text(VALIDATE_WORKFLOW)
    if workflow:
        for term in [
            "python3 scripts/validate_skill_repo.py",
            "./scripts/package.sh",
            "unzip -t outputs/skill.zip",
        ]:
            if term not in workflow:
                errors.append(f"validate workflow missing required command: {term}")

    return errors


def validate_zip(zip_path: Path) -> list[str]:
    errors: list[str] = []
    if not zip_path.exists():
        return [f"missing zip package: {zip_path}"]

    try:
        with zipfile.ZipFile(zip_path) as archive:
            names = set(archive.namelist())
            if names != EXPECTED_ZIP_ENTRIES:
                extras = sorted(names - EXPECTED_ZIP_ENTRIES)
                missing = sorted(EXPECTED_ZIP_ENTRIES - names)
                if extras:
                    errors.append(f"zip has unexpected entries: {extras}")
                if missing:
                    errors.append(f"zip missing entries: {missing}")

            skill_bytes = archive.read("plan-travel-guide/SKILL.md")
            local_bytes = SKILL_MD.read_bytes()
            if skill_bytes != local_bytes:
                errors.append("zip SKILL.md differs from repository SKILL.md")

            agent_bytes = archive.read("plan-travel-guide/agents/openai.yaml")
            local_agent_bytes = AGENT_YAML.read_bytes()
            if agent_bytes != local_agent_bytes:
                errors.append("zip agents/openai.yaml differs from repository agents/openai.yaml")
    except KeyError as exc:
        errors.append(f"zip is missing expected file: {exc}")
    except zipfile.BadZipFile:
        errors.append(f"bad zip package: {zip_path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", dest="zip_path", type=Path, help="also validate a skill.zip file")
    args = parser.parse_args()

    errors = validate_repo()
    if args.zip_path:
        errors.extend(validate_zip(args.zip_path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
