# ATLAS PROJECT LOG UPDATE PACK — Figma FAQ and General Contact Reconstruction

**Timestamp:** 13:46, 28.07.2026 Europe/Oslo  
**Session/task:** Recreate `FAQ v1.1` and `Generell kontakt v1.1` as editable Figma Slides presentations  
**Project:** Atlas Website / Atlas AI  
**Repository:** `nanotech-solutions-norway/Atlas`  
**Classification:** `AUTO_APPROVED` for source reconciliation, design-generation instructions and non-public draft generation; `PENDING_REVIEW` for final option selection, visual approval, Wix implementation and release.

## Issue or mistake observed

The Gamma-to-PowerPoint/Figma copies preserved content but also preserved presentation defects and implementation-only wording:

- broken or missing cover imagery;
- mixed Norwegian/English workflow labels;
- an overloaded and visually broken FAQ onboarding diagram;
- duplicate disclaimers and dense document-style slides;
- contradiction between required contact fields (`Navn`, `E-post`) and a blanket prohibition on all personal information;
- unsupported wording implying no deletion right;
- planned routing, receipts and form behaviour presented too close to verified runtime facts;
- implied public availability in some contact wording.

The first Figma generation attempt used the wrong similarly named plan. Figma account readback showed three plans. The explicit user-selected target is `Ruben`, plan key `team::1663898462705127337`.

## Root cause

1. Gamma webpages were imported as presentation copies without a full presentation-specific editorial and layout pass.
2. Multiple Figma plans had similar names (`Ruben A. Meyer's team`, `Ruben's`, `Ruben`), creating a plan-selection ambiguity.
3. Draft, implementation and release states were not consistently separated in presentation copy.

## Corrective rule

1. Recreate imported Gamma copies as editable Figma Slides presentations rather than treating PPTX import as final design.
2. Resolve the exact Figma plan by authenticated `whoami` readback and explicit user selection before generation.
3. Preserve Atlas governance locks and distinguish design evidence from Wix implementation, runtime validation and release approval.
4. Rewrite form-safety copy to permit necessary contact details while prohibiting sensitive, confidential, regulated, customer-sensitive and unnecessary personal data.
5. Frame routing, receipts, success/error states and storage/sletion wording as implementation requirements until verified.
6. Use Norwegian Bokmål consistently and remove mixed-language helper text.

## Evidence/source

- Explicit user instruction dated 28.07.2026 selecting Figma team `Ruben`.
- Gamma drafts `FAQ v1.1` and `Generell kontakt v1.1` in `Atlas AI - Phase 1`.
- Attached source pairs:
  - `FAQ-v11.pdf`
  - `FAQ-v11.pptx`
  - `Generell-kontakt-v11.pdf`
  - `Generell-kontakt-v11.pptx`
- Canonical GitHub registers:
  - `governance/registers/canonical/ATLAS_DECISIONS_REGISTER.md`
  - `governance/registers/canonical/PROJECT_LEARNING_LOG.md`
  - `governance/registers/canonical/ATLAS_SOURCE_AUTHORITY_MAP.md`
- Relevant approved decisions:
  - FAQ is a required Phase 1 page role.
  - ordinary public forms are low-risk only;
  - Managed Secure remains qualification/architecture review only;
  - design status must remain separate from implementation, validation and release;
  - public and purchase activation remain locked.

## Action taken

1. Reconciled the Gamma content and attached PDF/PPTX presentations against current approved Atlas governance boundaries.
2. Prepared a nine-slide FAQ reconstruction brief with:
   - one public-facing hero;
   - topic navigation without fake search functionality;
   - four direct answers;
   - audience routing;
   - Atlas positioning;
   - platform/cost decision model;
   - data and Managed Secure qualification route;
   - corrected student/onboarding composition;
   - related-page route map and draft-status footer.
3. Prepared a seven-slide General Contact reconstruction brief with:
   - corrected hero imagery;
   - task-based contact routing;
   - low-risk acceptable-use guidance;
   - required/optional field structure;
   - implementation-state routing model;
   - corrected prohibited-data wording;
   - dedicated privacy/security/Managed Secure route map.
4. Submitted both editable Figma Slides generation jobs under plan `Ruben` (`team::1663898462705127337`).
5. Preserved the following locks in both design briefs:
   - `publicAllowed=false`
   - `purchaseAllowed=false`
   - `releaseApproved=false`
   - `NO_GO`

## Validation performed

- Figma `whoami` readback confirmed the authenticated user and exact selected plan key:
  - handle: `Ruben`
  - plan: `Ruben`
  - key: `team::1663898462705127337`
- Both Figma Slides generation widgets were returned successfully under the selected plan.
- Generation briefs explicitly prohibit:
  - public-availability claims;
  - provider-partnership implication;
  - operational Managed Secure claims;
  - guaranteed security, response, receipt or processing;
  - fake search functionality;
  - mixed-language workflow labels;
  - blanket prohibition on all personal data;
  - unsupported no-deletion-right wording.

## Unresolved items

1. Select the preferred generated Figma option for each deck in the Figma widgets.
2. Verify final Figma slide count, typography, contrast, overflow, spacing, image treatment and editable-layer quality after selection.
3. Confirm exact Figma file URLs and node IDs for controlled indexing.
4. Perform final comparative ranking against the established Atlas design discipline.
5. Transfer only approved design decisions to Wix Studio.
6. Validate Wix form schema, routing, consent/privacy copy, retention/deletion disclosures, accessibility and negative paths.
7. Preserve `NO_GO` until implementation, validation and release gates pass.

## Classification

- **AUTO_APPROVED:** exact plan selection, source reconciliation, correction of verified presentation defects, non-public Figma generation briefs, and preservation of existing safety/release locks.
- **PENDING_REVIEW:** preferred option selection, final visual approval, public copy approval, implementation claims, legal/privacy wording, Wix runtime evidence and release decision.
