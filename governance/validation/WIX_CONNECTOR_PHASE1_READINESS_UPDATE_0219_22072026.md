# Atlas AI Wix Connector Phase 1 Readiness Update — 02:19, 22.07.2026

## Executive status

- Wix site: Atlas-AI
- Site ID: `1448ccad-68f0-43ea-8f0e-c9d8c0366082`
- Wix state: Draft
- Phase 1 public deployment: NO-GO
- Publication performed: No
- Physical Wix Studio page-tree mutation performed: No; the available connector does not expose a supported page-tree/menu API.

## Connector actions completed

### Package rendering control

`AtlasPackages` now contains explicit `renderRole` and `sourcePage` fields.

- 4 `DELIVERY_LEVEL_SOURCE` records → Pricing
- 5 `OUTCOME_AREA_SOURCE` records → Business AI
- 4 `AUDIENCE_SUPPORT_SOURCE` records → Students or Consumers
- 1 `ARCHITECTURE_REVIEW_ONLY` record → Managed Secure

All 14 remain `publicAllowed=false`.

### Locale and navigation readiness

- Corrected Home positioning in Bokmål and English.
- Replaced the obsolete “Explore packages” CTA with “Explore solutions”.
- Strengthened the low-risk public-form warning in both languages.
- Corrected Managed Secure language to architecture-review-only and non-operational.
- Added 30 bilingual navigation labels covering all 15 current Phase 1 page concepts.

### Resource controls

`AtlasResources` now contains:

- `publicAllowed`
- `assetExists`
- `evidenceStatus`

All four current resource records are classified as planned resource concepts:

- `assetExists=false`
- `publicAllowed=false`

The Managed Secure resource title and metadata were corrected so it does not imply an operational secure service.

### Qualification form

The existing form was updated in place:

- Form ID: `fc36d58a-fd2f-4183-baa9-310e087abf40`
- Name: `Atlas Phase 1 Qualification — Low Risk`
- Revision: 2
- Existing automation ID preserved: `65c5d999-879c-4b6c-b422-bb824c12246f`
- Advanced spam protection preserved.
- No file-upload field exists.

Current required form fields:

1. First name
2. Email
3. Audience
4. High-level need with prohibited-data warning
5. Expected user scope
6. Current work environment
7. Highest expected data class
8. Preferred next step
9. Explicit low-risk acknowledgement

Company/organization remains optional. The confirmation message now reiterates the no-file/no-sensitive-data boundary and separate architecture-review path.

No submission-content read was performed. The submission-count endpoint returned no count evidence, so operational form use remains unvalidated.

### Robots and GEO controls

- `robots.txt` remains Wix default and includes `https://www.atlas-ai.no/sitemap.xml`.
- No robots mutation was made before final route and indexing implementation.
- The publicly visible `llms.txt` was found to contain unsupported claims including blanket GDPR compliance, Norwegian data storage, full traceability, local integrations, rapid operational readiness and dedicated support.
- `llms.txt` was changed from `hidden=false` to `hidden=true`.
- A replacement must not be exposed until the actual public pages, claims and release state are approved.

## Phase 1 page inventory

The verified Wix audit identified eight existing content-bearing page concepts:

- Home
- Solutions
- Packages
- Governance
- Process
- Intake
- Managed Secure Mode
- Contact

The current Phase 1 contract contains 15 distinct page concepts.

### Missing distinct pages to create — 7

1. Business AI
2. Students
3. Consumers
4. Platform Lanes
5. Legal
6. Resources
7. About

### Existing pages requiring rename, move or rebuild — 5

1. Packages → Pricing
2. Governance → Trust
3. Intake → Onboarding; move under Contact
4. Managed Secure Mode → Managed Secure; keep hidden and non-indexed
5. Process → move under Resources; use `/resources/process/`

### Existing pages requiring content implementation and QA — 3

1. Home
2. Solutions
3. Contact

`AtlasPagePlan` now contains `phase1Required`, `wixPageState` and `implementationAction` for all 15 records.

## Correct Phase 1 hierarchy

- Home — root/logo
- Solutions
  - Business AI
  - Students
  - Consumers
  - Platform Lanes
- Managed Secure — top-level contract, hidden/non-public
- Pricing
- Trust
  - Legal
- Resources
  - Process
- About
- Contact
  - Onboarding

## Remaining manual Wix Studio work

- Create the seven missing pages.
- Rename, move and rebuild the five legacy page concepts.
- Insert and bind validated Figma sections.
- Configure actual menu nesting and mobile navigation.
- Apply routes and redirects.
- Apply per-page metadata, canonical URLs, hreflang, Open Graph and structured data.
- Bind and visually validate the updated form.
- Approve and test consent, retention, notifications, error states and backend routing.
- Validate Bokmål/English parity, accessibility, responsive behavior, performance, links and CTAs.
- Complete G00–G22 evidence and record explicit release approval.

## Validation result

- Package role classification: 14/14 PASS
- Navigation labels added: 30/30 PASS
- Resource locks: 4/4 PASS
- Qualification form schema: revision 2 PASS at schema level
- Form operation and notifications: NOT VALIDATED
- Robots state: default/readback PASS
- Unsupported `llms.txt`: hidden PASS
- Page-plan checklist: 15/15 PASS
- Physical Wix Studio implementation: NOT VALIDATED
- Phase 1 release: NO-GO

## Classification

AUTO_APPROVED:

- controlled package-role classification;
- bilingual navigation labels and approved safety copy;
- resource existence/publication locks;
- low-risk form field contract and no-upload boundary;
- hiding unsupported public `llms.txt` claims;
- page-gap classification and implementation checklist;
- non-claim-changing readback and quality controls.

PENDING_REVIEW:

- physical page creation, movement, routes, redirects and publication;
- form consent, retention, notifications and backend processing;
- pricing, MVA, provider eligibility, usage and SLA commitments;
- legal and privacy documents;
- student, consumer, Family and age treatment;
- Managed Secure operational availability;
- production implementation and release decision.
