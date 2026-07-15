# ATLAS PROJECT LOG UPDATE PACK — 10:12, 15.07.2026

## Timestamp
10:12, 15.07.2026 Europe/Oslo

## Session / task
Verify whether the recreated Atlas AI Figma Slides decks already have two Gamma source drafts, provide direct links and update the controlled source registers.

## Issue or mistake observed
The Figma-to-Gamma relationship was stored in slide metadata and source maps, but there was no single human-readable register containing the direct v1 and v2 Gamma URLs for every recreated Figma presentation.

## Root cause
The previous validation focused on card-level source IDs and Figma geometry. Direct Gamma editor links were distributed across connector outputs and were not consolidated in one governed register.

## Corrective rule
For every primary Atlas Figma deck, maintain one controlled record containing:
1. Figma URL;
2. Gamma v1 URL and ID;
3. Gamma v2 URL and ID;
4. supporting Gamma sources where applicable;
5. source-disposition note;
6. approval limitations.

Do not regenerate existing Gamma drafts merely to obtain a consistent naming scheme. Avoid duplicate files.

## Evidence / source
- Gamma workspace search confirmed v1 and v2 drafts for Business, Students, Consumers, Prices, Platform Lanes, Trust, Onboarding, Resources, About and Legal.
- Gamma folder search confirmed the Atlas AI 3.1 folder exists.
- The Students Figma deck was re-read and contains `atlas/sourceMap` and `atlas/referenceValidation` metadata linking it to Student v1, Student v2, Student Intake v2 and Responsible AI Study Guide v2.
- The approved 72-slide validation report confirms source maps on all nine new decks.

## Action taken
- Confirmed that all nine recreated Figma decks already have two primary Gamma drafts.
- Did not create duplicate Gamma files.
- Added `governance/registers/ATLAS_GAMMA_TO_FIGMA_DRAFT_LINK_REGISTER_1009_15072026.md` to GitHub.
- Created and populated the native Google Doc `Atlas Gamma-to-Figma Draft Link Register — 10:09, 15.07.2026`.
- Moved the Google Doc into the canonical `Atlas AI Project` Drive folder.

## Google Drive evidence
- Document ID: `1CNpY4WwRoV__4Lew3-3GcCD3yHf2Ig1mWUjKpknexg8`
- URL: https://docs.google.com/document/d/1CNpY4WwRoV__4Lew3-3GcCD3yHf2Ig1mWUjKpknexg8/edit?usp=drivesdk
- Parent folder: `1VUOFbzGcAXWjzQLDcPfXfbxhsVjMHUJ3`

## Unresolved items
- The Gamma connector does not expose a move action or per-file folder membership in the returned Gamma records. Exact current folder placement of the existing drafts was therefore not changed or asserted.
- Commercial, legal, provider, runtime and public-release gates remain unchanged.

## Classification

### AUTO_APPROVED
- Exact source-link verification.
- Human-readable Gamma-to-Figma link register.
- Duplicate-avoidance rule.
- GitHub and Google Drive record creation.

### PENDING_REVIEW
- Any future renaming, deletion or relocation of existing Gamma files.
- Commercial, legal, provider, security/runtime and production-publication decisions.
