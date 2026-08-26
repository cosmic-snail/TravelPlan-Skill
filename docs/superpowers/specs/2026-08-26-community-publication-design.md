# TravelPlan Skill Community Publication Design

## Goal

Publish `plan-travel-guide` as a discoverable, installable community Skill while preserving its existing research behavior and evidence boundaries.

## Scope

The publication includes:

1. Repository readiness for public reuse.
2. A validated GitHub Release containing `skill.zip`.
3. Discovery through skills.sh.
4. A curated-list submission to Awesome Codex Skills.
5. Reusable Chinese and English community descriptions.

The Skill's travel-planning instructions and output contract will not be redesigned as part of this work.

## Repository Changes

- Add an MIT License using copyright year 2026 and owner name `cosmic-snail`.
- Add repository badges for validation, skills.sh, and MIT licensing.
- Add the Skills CLI installation command for `plan-travel-guide` while retaining the existing source-copy and ZIP methods.
- Add concise community-discovery documentation with accurate capabilities, limitations, submission fields, and shareable Chinese and English text.
- Add a GitHub Actions workflow that runs the repository validator and deterministic packaging check on pushes and pull requests.
- Set the GitHub repository description and travel, codex, agent-skills, itinerary, and travel-planning topics.

## Release Design

- Use the repository's existing `scripts/package.sh` and `scripts/package_skill.py` workflow.
- Verify the generated archive with the repository validator and ZIP integrity check.
- Create release `v1.0.0` with an asset named exactly `skill.zip`.
- Include the archive SHA-256 digest in the release notes.
- Do not commit generated `outputs/` or temporary validation files.

## Community Publication

### skills.sh

Run the public Skills CLI installation command against the GitHub repository with the explicit `plan-travel-guide` selection. This verifies discovery and sends the CLI's documented anonymous install telemetry, which is used by skills.sh for indexing and ranking. Confirm the resulting skills.sh page or API record before claiming publication.

### Awesome Codex Skills

Submit one GitHub issue using the repository's current Chinese-skill or general-skill template, whichever best matches the required fields. The submission will identify the Skill as a source-led themed travel planner and disclose that live web research is required for dates, opening hours, tickets, events, and route feasibility.

### Other Communities

Prepare reusable posts for OpenAI Developer Community and other moderated channels, but do not publish through personal social accounts without a separate authenticated preview and explicit authorization for that channel.

## Quality And Safety

- Do not claim a skills.sh or curated-list publication until the remote page or issue exists.
- Do not claim tickets, opening hours, POIs, or routes are guaranteed current.
- Do not present social-platform popularity as verification.
- Do not add credentials, private browsing data, generated archives, or local paths to the repository.
- Preserve the existing public repository history and use non-destructive changes on `main`.

## Verification

Before completion:

1. Run `python3 scripts/validate_skill_repo.py`.
2. Run `./scripts/package.sh` and test the generated ZIP.
3. Validate `plan-travel-guide/` with the bundled Codex Skill validator when available.
4. Confirm a clean Git diff and successful GitHub Actions run.
5. Download the release asset and compare its SHA-256 digest.
6. Confirm the skills.sh record and Awesome Codex Skills issue URL.

