# TravelPlan Skill Community Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish `plan-travel-guide` as a validated, licensed, discoverable community Skill with a GitHub Release, skills.sh listing, and Awesome Codex Skills submission.

**Architecture:** Keep `plan-travel-guide/` as the installable Skill and leave its behavior unchanged. Extend the repository validator to enforce distribution metadata, add repository-facing documentation and CI, then use existing deterministic packaging for the release and public community channels for discovery.

**Tech Stack:** Markdown, Python standard library, Bash, GitHub Actions, GitHub CLI, Skills CLI.

---

### Task 1: Enforce Community Readiness

**Files:**
- Modify: `scripts/validate_skill_repo.py`
- Test: `scripts/validate_skill_repo.py`

- [ ] **Step 1: Add failing repository requirements**

Add these paths beside the existing constants:

```python
LICENSE = ROOT / "LICENSE"
COMMUNITY_GUIDE = ROOT / "docs" / "community-sharing.md"
VALIDATE_WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
```

Include them in the required-file loop and require these README terms:

```python
"npx skills add cosmic-snail/TravelPlan-Skill",
"skills.sh",
"MIT",
```

Validate that `LICENSE` contains `MIT License`, `Copyright (c) 2026 cosmic-snail`, and `Permission is hereby granted`, and that the workflow contains both `python3 scripts/validate_skill_repo.py` and `./scripts/package.sh`.

- [ ] **Step 2: Run the validator and verify RED**

Run:

```bash
python3 scripts/validate_skill_repo.py
```

Expected: exit 1 with missing `LICENSE`, `docs/community-sharing.md`, `.github/workflows/validate.yml`, and README community terms.

- [ ] **Step 3: Keep the failing validator change for Task 2**

Do not weaken the checks. Review `git diff -- scripts/validate_skill_repo.py` and confirm every new requirement maps to the approved publication design.

### Task 2: Add Distribution Files And README Guidance

**Files:**
- Create: `LICENSE`
- Create: `.github/workflows/validate.yml`
- Create: `docs/community-sharing.md`
- Modify: `README.md`
- Test: `scripts/validate_skill_repo.py`

- [ ] **Step 1: Add the approved MIT License**

Create the standard MIT text beginning with:

```text
MIT License

Copyright (c) 2026 cosmic-snail
```

and ending with the standard warranty disclaimer.

- [ ] **Step 2: Add deterministic CI**

Create `.github/workflows/validate.yml`:

```yaml
name: Validate

on:
  push:
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python3 scripts/validate_skill_repo.py
      - run: ./scripts/package.sh
      - run: unzip -t outputs/skill.zip
```

- [ ] **Step 3: Add README badges and Skills CLI installation**

Place these badges below the title:

```markdown
[![Validate](https://github.com/cosmic-snail/TravelPlan-Skill/actions/workflows/validate.yml/badge.svg)](https://github.com/cosmic-snail/TravelPlan-Skill/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/cosmic-snail/TravelPlan-Skill)](https://skills.sh/cosmic-snail/TravelPlan-Skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
```

Add the preferred installation method before source-copy installation:

```bash
npx skills add cosmic-snail/TravelPlan-Skill \
  --skill plan-travel-guide \
  --agent codex \
  --global
```

State that the Skill requires current public web research and does not book or guarantee availability.

- [ ] **Step 4: Add reusable community descriptions**

Create `docs/community-sharing.md` with:

- Chinese and English summaries describing source-led themed travel discovery.
- The exact Skills CLI installation command.
- Awesome Codex Skills fields: `Plan Travel Guide`, repository URL, `Creative & Media`, `GitHub`, `Chinese-Native, Travel Planning, POI Research, Itinerary`, and accurate risk notes.
- A note that dates, hours, ticketing, events, and route feasibility need current verification.

- [ ] **Step 5: Run GREEN verification**

Run:

```bash
python3 scripts/validate_skill_repo.py
./scripts/package.sh
unzip -t outputs/skill.zip
```

Expected: validator passes, package validation passes, and ZIP reports no errors.

- [ ] **Step 6: Commit repository readiness**

```bash
git add LICENSE README.md .github/workflows/validate.yml docs/community-sharing.md scripts/validate_skill_repo.py
git commit -m "chore: prepare skill for community release"
```

### Task 3: Publish Repository Metadata

**Files:**
- Modify remotely: GitHub repository metadata

- [ ] **Step 1: Set description and topics**

Run:

```bash
gh repo edit cosmic-snail/TravelPlan-Skill \
  --description "Source-led themed travel planning Skill for Codex with current POI research and day-by-day itineraries" \
  --add-topic agent-skills \
  --add-topic codex \
  --add-topic itinerary \
  --add-topic travel \
  --add-topic travel-planning
```

- [ ] **Step 2: Push the approved changes**

```bash
git push origin main
```

- [ ] **Step 3: Confirm CI**

Run `gh run list --branch main --limit 5` and wait for the `Validate` workflow for the pushed commit to finish successfully.

### Task 4: Create The v1.0.0 Release

**Files:**
- Generate locally: `outputs/skill.zip`
- Publish remotely: GitHub release `v1.0.0`

- [ ] **Step 1: Build and hash the package**

```bash
./scripts/package.sh
shasum -a 256 outputs/skill.zip
```

Expected: validation passes and one SHA-256 digest is printed.

- [ ] **Step 2: Create the release**

Use `gh release create v1.0.0 outputs/skill.zip --target main` with title `Plan Travel Guide Skill v1.0.0`. Notes must summarize current POI discovery, themed planning, deterministic packaging, live-data limitations, and include the digest from Step 1.

- [ ] **Step 3: Verify the remote asset**

Download `skill.zip` into a new temporary directory, run `unzip -t`, compare SHA-256 with Step 1, and inspect `gh release view v1.0.0 --json url,assets,body`.

### Task 5: Trigger And Verify skills.sh Discovery

**Files:**
- External index: skills.sh

- [ ] **Step 1: Verify CLI discovery**

```bash
npx --yes skills add https://github.com/cosmic-snail/TravelPlan-Skill \
  --skill plan-travel-guide \
  --agent codex \
  --global \
  --yes
```

Expected: CLI reports `plan-travel-guide` installed successfully from the repository.

- [ ] **Step 2: Confirm the catalog record**

Check `https://skills.sh/cosmic-snail/TravelPlan-Skill/plan-travel-guide` and the skills.sh search API. If indexing is asynchronous, retry with bounded waits and report the listing as pending rather than published until the record exists.

### Task 6: Submit Awesome Codex Skills

**Files:**
- External issue: `flaqai/awesome_codex_skills`

- [ ] **Step 1: Create one Chinese Skill submission**

Use `gh issue create` with title `[Chinese Skill] Plan Travel Guide` and the current template fields:

- Skill Name: Plan Travel Guide
- GitHub Source URL: `https://github.com/cosmic-snail/TravelPlan-Skill/tree/main/plan-travel-guide`
- Directory Page URL: the verified skills.sh URL
- Category: Creative & Media
- Source Platform: GitHub
- Tags: Chinese-Native, Travel Planning, POI Research, Itinerary
- Popularity Evidence: first public release, deterministic validator and GitHub Actions; do not invent stars or installs
- Install Command: the exact Skills CLI command
- Risk Notes: requires live web access; social results are discovery signals; dates, hours, tickets, and routes require current verification
- Confirm all three required declarations

- [ ] **Step 2: Verify the issue**

Open the returned issue with `gh issue view` and confirm its title, labels, repository URL, install command, and risk notes.

### Task 7: Final Verification

**Files:**
- Verify: repository, installed Skill, release archive, community URLs

- [ ] **Step 1: Run fresh local verification**

```bash
python3 scripts/validate_skill_repo.py
./scripts/package.sh
git diff --check
git status --short --branch
```

Expected: all validation passes and the branch is clean and synchronized with `origin/main`.

- [ ] **Step 2: Verify remote state**

Confirm the GitHub Actions run succeeded, release asset digest matches locally, skills.sh page exists or is explicitly pending, and the Awesome Codex Skills issue is open.

