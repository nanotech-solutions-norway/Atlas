# Atlas Wix Page Content Validation — 22:24, 13.07.2026

**Status:** VALIDATED_EVIDENCE_RECORD  
**Classification:** AUTO_APPROVED validation rule; PENDING_REVIEW route and production changes  
**Site:** Atlas-AI — `1448ccad-68f0-43ea-8f0e-c9d8c0366082`

## 1. Purpose

Control and validate which Atlas pages can currently be treated as created in Wix based on live Wix data, current GitHub route records, Gamma draft purpose, Google Drive source authority, and Atlas project history.

## 2. Critical validation boundary

The Wix connector confirms the site, Wix Studio editor and preview URLs, CMS collections, content records, form asset, and Pricing Plans state. It does **not** expose a supported API that enumerates the Wix Studio visual page tree or verifies that a page is rendered and bound correctly.

Therefore:

- A CMS record is **not** proof that a Wix Studio page is physically created.
- A Gamma draft is **not** proof that a Wix page is implemented.
- A project-history statement is evidence, not independent editor verification.
- The correct high-confidence label is: **project-reported current Wix page; CMS content validated; Studio page/rendering unverified**.

## 3. High-confidence current/legacy Wix page set

The following eight pages are supported by three converging evidence types:

1. Atlas project history identifies the page as part of the current Wix build.
2. Atlas AI 3.1 contains a matching update-only Gamma v1/v2 pair rather than a missing-page full draft.
3. `AtlasPagePlan` contains a substantive record with page purpose, CTA, route/slug and implementation status.

| Current/legacy route | Content evidence | Validated classification |
|---|---|---|
| `/` — Home | `AtlasPagePlan` plus three audience records and package/offer support | High-confidence current Wix page; Studio binding/rendering unverified |
| `/solutions/` | Page-plan record plus populated audience, offer and package collections | High-confidence current Wix page; Studio layout binding unverified |
| `/packages/` | Page-plan record plus 14 substantive package records | High-confidence current legacy page; merge into `/solutions/` only after destination QA |
| `/governance/` | Page-plan record plus Trust, legal and validation-governance records | High-confidence current legacy page; merge/redirect to `/trust/` only after destination QA |
| `/process/` | Page-plan record plus seven detailed phase records | High-confidence current page candidate; final canonical treatment remains PENDING_REVIEW |
| `/intake/` | Page-plan record, five onboarding routes and low-risk Wix form asset | High-confidence current legacy page/asset; form routing and onboarding binding remain incomplete |
| `/managed-secure-mode/` | Page-plan record plus Managed Secure package, trust gate, Azure lane and legal/security records | High-confidence current legacy page candidate; future-state language only; canonical route unverified |
| `/contact/` | Page-plan record with purpose/CTA and explicit remaining form-routing work | High-confidence current Wix page; final form and notification routing remain incomplete |

## 4. Pages not independently validated as created in Wix Studio

The following have substantive CMS content and/or Gamma drafts but no available editor-level evidence that a canonical Wix Studio page is physically created and bound:

- `/solutions/business-ai/`
- `/solutions/students/`
- `/solutions/consumers/`
- `/pricing/`
- `/platform-lanes/` and provider subpages
- `/trust/` and trust subpages
- `/onboarding/` and onboarding subpages
- `/resources/` and resource subpages
- `/about/`
- `/legal/` and legal subpages
- `/account/`
- English `/en/` mirrors

Classification: **CMS/Gamma ready; Wix Studio page verification or implementation required**.

## 5. Live Wix evidence

- Atlas-AI site status: Draft.
- Editor type: Wix Studio; Velo enabled; Premium/custom domain.
- Wix returned a primary premium root URL: `https://www.atlas-ai.no/`.
- Wix returned valid Studio editor and preview URLs.
- `AtlasPagePlan`: 8 substantive records.
- Supporting content:
  - 3 customer segments
  - 14 packages
  - 7 pricing records
  - 6 platform lanes
  - 5 trust topics
  - 5 onboarding routes
  - 4 resources
  - 7 legal records
  - 7 phase records
- `PaidPlans/Plans`: 0 records.
- Wix form asset `Atlas Standard Qualification - Low Risk` exists; no submissions/data items were returned.
- Student and consumer pricing CMS records remain outdated placeholders and do not reflect Student Basic, Student Plus, Everyday Basic and Family.

## 6. GitHub and route-state validation

The current `sitemap.xml` still lists legacy GitHub Pages routes including `/business/`, `/students/` and `/consumers/`. PR #1 proposes the canonical routes:

- `/solutions/business-ai/`
- `/solutions/students/`
- `/solutions/consumers/`

PR #1 remains open and unmerged. No production redirect or sitemap migration is authorized by this validation record.

## 7. Corrective rule

Never mark a Wix visual page as independently verified unless the editor page tree or rendered route has been directly inspected. Use separate fields or labels for:

1. Project-reported current page
2. CMS content validated
3. Studio page verified
4. Page binding/rendering verified
5. Operational flow validated
6. Published-production state validated

## 8. Required next validation

1. Open the Wix Studio page panel and export or record the complete page list, names and slugs.
2. Preview every page and verify that content is rendered, bound and responsive.
3. Record screenshots for desktop and mobile.
4. Verify forms, notifications, internal links, metadata and language variants.
5. Compare the resulting editor page tree to this evidence record.
6. Only then mark pages `STUDIO_PAGE_VERIFIED` or `PUBLISHED_PRODUCTION_VERIFIED`.

## 9. Action status

- Wix content was read only; no page, route, CMS record or publication state was changed.
- Gamma content was read only; no draft was changed.
- GitHub route recommendations remain PENDING_REVIEW.
- Updated DOCX report produced separately.
