# Atlas AI Phase 1 FAQ CMS Update — 23:11, 27.07.2026

**Project:** Atlas Website / Atlas AI  
**Wix site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Classification:** Phase 1 scope decision `APPROVED`; CMS preparation and validation `AUTO_APPROVED`; publication and release remain `NO_GO`

## 1. Owner instruction

FAQ is included in Phase 1 as a required public page role under Resources.

Canonical routes:

- Bokmål: `/resources/faq/`
- English: `/en/resources/faq/`

This raises the Phase 1 canonical public page-role count from 14 to 15.

## 2. Wix CMS assessment

Wix CMS is suitable for the Atlas FAQ because it supports:

- structured question, short-answer and expanded-answer records;
- categories and related package/platform metadata;
- controlled ordering and filtering;
- Bokmål/English locale separation;
- claim and review traceability;
- fail-closed publication controls;
- accessible accordion/repeater rendering;
- visible-content/FAQPage structured-data parity.

The native `AtlasFAQs` collection already existed and contained eight English seed entries.

## 3. Wix actions completed

1. Read back the current CMS collection schema and all existing FAQ items.
2. Added explicit fields:
   - `locale`
   - `publicAllowed`
   - `reviewStatus`
   - `phase`
   - `pagePlacement`
3. Classified the eight legacy English entries as Phase 1 review-required records and set `publicAllowed=false`.
4. Added eight Bokmål Phase 1 draft entries covering:
   - Atlas AI definition;
   - intended audiences;
   - platform selection;
   - confidential-file prohibition;
   - Managed Secure boundary;
   - licence/API-cost treatment;
   - responsible student use;
   - onboarding/contact route.
5. Added `AtlasDiscoveryMetadata` record `faq` for `/resources/faq/` and `/en/resources/faq/`.
6. Updated Resources metadata to include the FAQ route.
7. Preserved `publicAllowed=false` for all FAQ entries and page metadata.

Current FAQ CMS count: **16 records** — eight English legacy seeds and eight Bokmål drafts.

## 4. Validation result

- CMS data model: `PASS`
- Locale and governance controls: `PASS`
- Phase 1 scope record: `PASS`
- Public rendering: `NOT_IMPLEMENTED`
- Studio page/route binding: `PENDING`
- Bokmål/English parity: `PENDING`
- Claim/legal/privacy/provider review: `PENDING`
- Responsive/accessibility/structured-data testing: `NOT_RUN`
- Release state: `NO_GO`

## 5. Required Studio implementation

The Wix Studio workstream must:

1. Create or verify the FAQ pages for both routes.
2. Place FAQ under Resources in navigation.
3. Bind an accessible accordion or repeater to `AtlasFAQs`.
4. Filter by current locale, `phase=PHASE_1`, `pagePlacement=resources_faq` and `publicAllowed=true`.
5. Prevent draft, wrong-language or unreviewed records from rendering.
6. Validate keyboard operation, focus visibility, reflow, accordion state and responsive layouts.
7. Apply FAQPage structured data only where the same reviewed FAQ content is visibly rendered.
8. Complete page-level acceptance before changing any public or release flag.

## 6. Preserved controls

No page was published and no release gate was changed.

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- checkout remains disabled
- real payments remain disabled
- production entitlements remain disabled
- Managed Secure remains qualification/architecture-review only

## 7. Records updated

- `governance/registers/canonical/ATLAS_DECISIONS_REGISTER.md`
- `governance/registers/canonical/ATLAS_VALIDATION_REGISTER.md`
- `governance/validation/ATLAS_WEBSITE_PUBLICATION_READINESS_AND_PHASE_STATUS_2233_27072026.md`
- Wix `AtlasFAQs`
- Wix `AtlasDiscoveryMetadata`

## 8. Result

FAQ is now an approved Phase 1 requirement with a suitable, governed and fail-closed Wix CMS foundation. The remaining work is Wix Studio page creation/binding, bilingual content approval, accessibility and structured-data testing, and final release acceptance. Public release remains `NO_GO`.
