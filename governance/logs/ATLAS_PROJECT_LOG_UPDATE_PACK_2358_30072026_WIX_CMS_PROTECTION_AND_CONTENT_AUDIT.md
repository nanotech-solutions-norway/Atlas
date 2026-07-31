# ATLAS PROJECT LOG UPDATE PACK — Wix CMS Protection and Content Audit — 23:58, 30.07.2026

## Timestamp

23:58, 30.07.2026 Europe/Oslo

## Session / task

Protect recommended Atlas Wix CMS records; resolve the stale Process page issue; retrieve current Wix Studio page/entity and design-time text evidence; compare current text with approved/canonical Atlas strategy, governance, Trust, Gamma and Figma sources; produce a validated page-by-page remediation ranking; and preserve all release controls.

## Issue or mistake observed

1. Seven internal authoring/governance collections allowed anonymous reads despite containing evidence, legal notes, owners, validation states, implementation actions or publication controls.
2. `AtlasPagePlan` retained a stale Process record although no current Process page exists and FAQ is the approved Resources child.
3. Current Wix drafts contain literal Gamma asset placeholders.
4. Internal QA labels, implementation instructions and review markers are visible in visitor-facing page text.
5. Home and Managed Secure contain unsupported or premature certification, compliance, residency, runtime and control claims.
6. Business copy implies operational uploads, processing, module activation and integrations not evidenced as current runtime capabilities.
7. Student Basic/Plus and Family entitlement content conflict with later project decisions.
8. Contact and FAQ have newer Gamma/Figma source material, but current Wix implementation remains static, duplicated or mixed with implementation notes.
9. English terminology and hybrid phrases reduce clarity in the Norwegian site.

## Root cause

- Initial CMS schemas predated the approved private-authoring/public-rendering control pattern.
- Page-plan records were not reconciled after current FAQ and page-entity implementation.
- Gamma/Figma implementation briefs were copied into Wix as page content without fully separating visitor copy from implementation instructions.
- June/early-July commercial concepts remained in Wix after later strategy, legal, security and release-governance updates.
- The Wix Studio canvas, CMS, GitHub code and approved Drive sources were updated at different times without an exact copy-manifest reconciliation.

## Corrective rule

- Internal authoring, legal, claims, release, validation, page-plan and editorial metadata must be CMS-editor-only.
- Public pages may bind only to sanitized public rendering collections.
- A page-role record must be reconciled to authenticated current Wix and repository evidence; obsolete roles must be explicitly superseded, not silently retained.
- Visitor-facing pages must not expose QA markers, internal implementation requirements, placeholder asset tokens or unapproved claims.
- Operational capabilities may be described only after exact implementation and acceptance evidence exists.
- Use `Atlas AI` as the brand and clear Norwegian `KI` terminology in body copy.
- Public copy changes remain PENDING_REVIEW until exact page, locale, claim and evidence are approved.

## Evidence / source

- Authenticated Wix context and translation/editor-content index for site `1448ccad-68f0-43ea-8f0e-c9d8c0366082`.
- Wix CMS schemas, items and permission readbacks.
- Private engineering repository `nanotech-solutions-norway/atlas_wix` and current page-entity manifest.
- Canonical governance repository `nanotech-solutions-norway/Atlas`.
- Google Drive report `Atlas AI Web Design and Website Strategy 09:54, 29.07.2026 - English Translation`.
- Google Drive `Atlas AI Trust Center, Security and Privacy Copy Pack — 23:55, 27.07.2026`.
- Gamma `FAQ v1.1` and `Generell kontakt v1.1`.
- Figma Slides Contact file `6UODS1tY13e5kO2UnpyGKr` and FAQ file `By3uvqtSoHpP7ioqasm4OO`.
- Official Språkrådet and Digdir klarspråk guidance reviewed for Norwegian terminology and user-facing digital text.

## Action taken

### Wix CMS

Changed the following collections to `CMS_EDITOR` for read, insert, update and remove:

- `AtlasClaimsRegistry`
- `AtlasLegalDocs`
- `AtlasTrustTopics`
- `AtlasReleaseGates`
- `AtlasValidationGates`
- `AtlasPagePlan`
- `AtlasLocaleStrings`

Validated the existing FAQ boundary:

- `AtlasFAQs`: private CMS-editor authoring.
- `AtlasFAQsPublic`: anonymous read, CMS-editor write.

### Process page-plan defect

- Verified that no current Process page exists in Wix or `atlas_wix`.
- Re-categorized the stale `AtlasPagePlan` Process record as FAQ under Resources.
- Preserved the existing record ID and history.
- Set the implementation control to bind only `AtlasFAQsPublic` and validate locales, links, schema, accessibility and sensitive-data routing.

### Content audit

- Retrieved current unpublished Norwegian Wix Studio text for all page roles and performed targeted deep checks of Home, Services, Business, Students, Individuals, Managed Secure, Pricing, Trust, Legal, FAQ and Contact.
- Compared current Contact and FAQ against current Gamma and corrected Figma sources.
- Compared Trust and Managed Secure against the current controlled Trust copy pack.
- Produced a fifteen-page remediation ranking and Norwegian terminology corrections.
- Did not apply public page copy changes because final public wording, claims and commercial presentation remain PENDING_REVIEW.

### GitHub

- Created controlled branch `agent/wix-cms-protection-content-audit-20260730`.
- Added the validation report and this project log update pack.
- A draft pull request is to be opened for review.

### Google Drive

- Private validation and project-log mirrors are to be stored in the controlled July 2026 Wix audit and governance folders.

## Validation performed

| Check | Result |
|---|---|
| Seven collection permission changes | PASS_READBACK |
| Private FAQ authoring collection | PASS |
| Public FAQ rendering collection | PASS |
| Separate Process page | NOT_PRESENT |
| Process record correction | PASS_READBACK |
| Current 15 public-role candidates | PASS_ENTITY_COVERAGE |
| Wix page copy readback | PASS_UNPUBLISHED_EDITOR_CONTENT |
| Contact Gamma/Figma comparison | PASS_SOURCE_COMPARISON |
| FAQ Gamma/Figma comparison | PASS_SOURCE_COMPARISON |
| Trust copy comparison | PASS_SOURCE_COMPARISON |
| Placeholder removal | FAIL_REMEDIATION_REQUIRED |
| Internal QA marker removal | FAIL_REMEDIATION_REQUIRED |
| Public claim alignment | FAIL_REMEDIATION_REQUIRED |
| Student plan alignment | FAIL_LEGACY_TWO_PLAN_STRUCTURE |
| Family alignment | FAIL_LEGACY_ENTITLEMENT_CONCEPT |
| Norwegian terminology | PARTIAL_REMEDIATION_REQUIRED |
| Public release | NO_GO |

## Decisions and classifications

### AUTO_APPROVED

- Exact CMS permission hardening and verified readback.
- Private/public FAQ permission boundary verification.
- Stale Process-to-FAQ page-plan correction.
- Verified page/entity and content findings.
- Identification of public-layer placeholders, QA leakage and obsolete plan structures.
- Clear-language terminology improvements.
- No-release-effect validation.

### PENDING_REVIEW

- Final public page copy.
- Final public claims and supporting evidence.
- Pricing and plan presentation.
- Legal, privacy and security publication wording.
- Final navigation labels and routes.
- Any public, purchase, payment, production or release change.

## Unresolved items

1. Approve the remediation order and exact public copy manifests.
2. Remove unsupported Home and Managed Secure claims.
3. Replace visitor-facing implementation notes and placeholders.
4. Reconcile Student Basic/Plus to one approved student lane and foreground age 16+.
5. Remove or reclassify Family as a consumer entitlement.
6. Implement FAQ public CMS binding and verify no private working records are exposed.
7. Convert Legal/Trust public status lists to sanitized public projections.
8. Correct the Wix About page label in Studio and resynchronize.
9. Resolve the 73% versus 87% metric conflict by removing both or approving one with evidence.
10. Validate final rendered desktop/tablet/mobile, Bokmål/English parity, accessibility, forms, links, SEO and structured data.
11. Complete all release and acceptance gates.

## Preserved controls

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- Wix remains Draft.
- No Wix publication.
- No payment, checkout or Pricing Plan activation.
- No public write endpoint.
- No frontend provider token.
- No credentials, secrets, customer data or confidential commercial material exposed.
- Release remains `NO_GO`.

## Classification

`AUTO_APPROVED` for verified CMS hardening, exact defect correction, evidence-backed findings and non-sensitive workflow improvements.

`PENDING_REVIEW` for public copy, claims, commercial/legal/security content and all release-affecting decisions.
