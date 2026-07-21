# Atlas AI Wix CMS, Discovery and Navigation Update — 00:47, 22.07.2026

## Status

- Wix site: Atlas-AI
- Site ID: `1448ccad-68f0-43ea-8f0e-c9d8c0366082`
- Wix state: Draft
- Public deployment: NO-GO
- Wix publication performed: No
- Figma mutation performed: No

## Canonical source boundary

This update applies the current July 2026 Atlas page, route, claims and release-governance sources. Figma PASS establishes a design/content handoff only; it does not establish Wix implementation or production readiness.

## CMS actions completed

1. Expanded `AtlasPagePlan` from 8 to 15 current page concepts.
2. Renamed legacy roles:
   - Packages → Pricing
   - Governance → Trust
   - Intake → Onboarding
   - Managed Secure Mode → Managed Secure
3. Created `AtlasDiscoveryMetadata` and seeded 15 bilingual records with:
   - Bokmål and English routes
   - menu parent and ordering
   - SEO titles and descriptions
   - visible AEO answer blocks
   - GEO entity names, entity types and topics
   - intended schema types and internal links
   - page-experience checks
   - canonical Figma/source references
   - explicit release locks
4. Created `AtlasReleaseGates` with G00–G22; all 23 gates are `NOT_PASSED — EVIDENCE_REQUIRED`.
5. Marked the former 9 validation-gate records as superseded, preserving them as historical evidence.
6. Corrected stale platform-plane records:
   - Wix remains Draft.
   - `nanotech-solutions-norway/Atlas` is the active governance repository.
   - Gamma and Figma are source/design references, not the public CMS.
   - Azure is not operational.
   - Domeneshop backend/SQL references remain implementation evidence, not approved public production claims.
7. Corrected Phase 0.5 and Phase 1 roadmap records and added Phase 6.
8. Removed five verified duplicate claim records and refreshed all 17 remaining unique claim review dates to 22.07.2026 without changing approval status.
9. Added `publicAllowed` release locks to `AtlasOffers` and `AtlasPackages`:
   - 7/7 legacy offers locked from public rendering.
   - 14/14 package records locked from public rendering.
10. Verified Wix SEO User Config:
    - `shouldFlattenUrlHierarchy=false`
    - `shouldUsePartialRouteMatch=false`
    - hierarchical URLs are preserved and missing pages return SEO-friendly 404 responses.

## Approved menu hierarchy contract

- Root/logo: Home
- Solutions
  - Business AI
  - Students
  - Consumers
  - Platform Lanes
- Managed Secure — top-level contract but hidden/non-public until G20, G21 and explicit release approval
- Pricing
- Trust
  - Legal
- Resources
  - Process
- About
- Contact
  - Onboarding

Bokmål is the root-language contract and English uses reciprocal `/en/` routes.

## Discovery interpretation

The approved Atlas sources define SEO, AEO and GEO. No approved Atlas source defines “PEO”. This implementation treats PEO only as Page Experience Optimization and records release checks for LCP, INP, CLS, WCAG 2.2 AA target conformance, keyboard access, focus visibility, contrast, reflow, reduced motion and minimum target size. No speculative PEO schema or public claim was introduced.

## Connector boundary

### Completed through the Wix connector

- CMS collection creation and schema extension
- CMS item insertion, patching, deletion and validation
- route/menu contracts stored as governed CMS data
- SEO/AEO/GEO/page-experience source metadata stored in CMS
- release locks and G00–G22 gate migration
- claims deduplication and status correction
- site-level SEO URL and 404 configuration validation

### Requires Wix Studio/manual implementation

- Create/rename actual Wix Studio pages and apply the physical menu hierarchy
- Change actual page URLs and configure redirects
- Insert and bind validated Figma sections; remove superseded rendered content
- Apply per-page title, description, canonical, hreflang, Open Graph and structured data
- Validate sitemap and robots behavior against the actual published routes
- Complete Bokmål/English visible-content parity
- Configure and test forms, consent, retention, notifications, errors and backend routing
- Validate desktop, tablet and mobile layouts
- Validate accessibility, performance, CTAs, links, SEO and schema
- Approve legal/privacy text, pricing, provider delivery, audience rules and Managed Secure controls
- Record explicit release approval, smoke test and rollback evidence

## Validation result

- `AtlasPagePlan`: 15 records — PASS
- `AtlasDiscoveryMetadata`: 15 records, all `publicAllowed=false` — PASS
- `AtlasReleaseGates`: 23 records, all evidence-required — PASS
- `AtlasClaimsRegistry`: 17 unique reviewed records — PASS
- `AtlasOffers`: 7 legacy records release-locked — PASS
- `AtlasPackages`: 14 records release-locked — PASS
- SEO URL hierarchy and 404 configuration — PASS
- Wix page implementation and public release — NOT VALIDATED / NO-GO

## Classification

- AUTO_APPROVED: verified CMS inventory, duplicate removal, stale-status corrections, menu-parent contracts, metadata preparation, release locks and non-claim-changing quality-control rules.
- PENDING_REVIEW: page/route publication, pricing, provider rights and costs, legal/privacy terms, student/consumer/Family conditions, Managed Secure availability, production implementation and public release.
