# ATLAS PROJECT LOG UPDATE PACK — 19:19, 20.07.2026

## Session / task

Create a deterministic replacement map identifying which validated Figma section replaces, consolidates or supplements each current Wix section in the Atlas-AI Draft site.

## Issue observed

The project had validated Figma replacement decks and a Wix content audit, but lacked a single implementation map at section level. Without this map, Wix implementation could duplicate sections, retain stale claims or replace valid sections unnecessarily.

## Root cause

Earlier reports described replacement coverage by page and ranked the content, but did not consistently map every Figma slide to exact Wix section names and actions such as replace, merge-replace, insert, split-replace, keep or retire.

## Corrective rule

Every Wix implementation pass must use a slide-to-section replacement register before editing. The register must identify:

- exact Figma file and slide order;
- current Wix page/slug and section name;
- replacement action;
- placement order;
- sections/cards to retire;
- native Wix components that must remain functional rather than become static Figma images;
- route, safety and publication constraints.

## Evidence / sources

- Current `AtlasPagePlan` Wix CMS readback for all eight page shells.
- `WIX_EXISTING_PAGE_CONTENT_AUDIT_AND_RANKING_0206_19072026.md`.
- `WIX_GAMMA_REPLACEMENT_SECTIONS_SIMULATION_AND_RANKING_1013_19072026.md`.
- `ATLAS_FIGMA_FULL_SECTION_REANALYSIS_HEADING_SPACING_CONTENT_REVALIDATION_0142_20072026.md`.
- Seven current validated Figma replacement decks.

## Action taken

- Created `governance/specifications/ATLAS_FIGMA_TO_WIX_SECTION_REPLACEMENT_MAP_1919_20072026.md`.
- Mapped all 30 Figma replacement slides to the current Wix section architecture.
- Identified one-to-one replacements, consolidation points, new insertions, split replacements and sections/cards to retire.
- Confirmed that Solutions requires only two targeted replacements.
- Confirmed that Process requires one new customer-facing section plus one roadmap replacement.
- Confirmed that Intake has no replacement from the seven-section pack and must use Onboarding v3.
- Confirmed that the Contact native Wix form must remain functional and must not be replaced by static Figma content.
- Preserved Managed Secure architecture-review-only and low-risk public-form safety boundaries.
- Saved a matching Google Drive document in the Atlas Website project-source folder.

## Unresolved items

- Execute the replacements in Wix Studio.
- Reconfigure and validate the native Contact/Intake form.
- Validate responsive layouts, routes, CTA targets, accessibility, SEO, structured data and multilingual parity.
- Approve any `/packages`→`/pricing` and `/managed-secure-mode`→`/managed-secure` route changes.
- Complete legal, privacy, commercial, provider and release gates.

## Classification

**AUTO_APPROVED:** verified replacement mapping, sequencing, consolidation, duplicate-retirement and native-component rules.

**PENDING_REVIEW:** commercial pricing, provider eligibility, route renames, legal/privacy/security claims, public availability and release decisions.

## Final status

- Replacement map: COMPLETE.
- Figma source validation: 30/30 PASS.
- Wix mutation: NONE.
- Phase 1 public deployment: NO-GO.
