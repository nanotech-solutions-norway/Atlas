# Atlas Canonical Route Correction Recommendations — 11:00, 11.07.2026

**Status:** PENDING_REVIEW  
**Classification:** Public route, SEO, analytics, and production-availability change  
**Repository:** `nanotech-solutions-norway/Atlas`  
**Scope:** Recommendation and controlled implementation blueprint only. This record does not authorize production redirects or public route removal.

## 1. Purpose

Resolve route drift between the GitHub static mirror, Wix planning architecture, and Gamma drafts while preserving the approved three-audience Atlas AI strategy:

1. Professional / Business
2. Students
3. Consumers / Families

The canonical commercial hierarchy should be audience routes below `/solutions/`, with one authoritative URL per audience and permanent redirects from all superseded routes.

## 2. Current contradiction

### GitHub/static mirror routes

- `/business/`
- `/students/`
- `/consumers/`

### Gamma/reference routes found in draft CTAs

- `/bedrift`
- `/studenter`
- `/privat`
- `/pakker`
- `/velg`

### Recommended canonical Wix/SEO hierarchy

- `/solutions/business-ai/`
- `/solutions/students/`
- `/solutions/consumers/`

The Wix/SEO hierarchy is recommended because it groups the three commercial audience paths under one stable Solutions entity, reduces navigation drift, supports breadcrumbs and structured data, and avoids duplicate audience pages.

## 3. Canonical route map

| Audience or function | Canonical route | Status |
|---|---|---|
| Professional / Business | `/solutions/business-ai/` | Recommended canonical |
| Students | `/solutions/students/` | Recommended canonical |
| Consumers / Families | `/solutions/consumers/` | Recommended canonical |
| Solutions overview | `/solutions/` | Existing canonical category |
| Pricing | `/pricing/` | Existing canonical |
| Managed Secure | `/managed-secure/` | Existing canonical |
| Trust | `/trust/` | Existing canonical |
| Onboarding | `/onboarding/` | Existing canonical |

English mirrors should use the same path structure under `/en/`, for example `/en/solutions/students/`.

## 4. Permanent redirect recommendations

| Superseded route | Permanent destination |
|---|---|
| `/business/` | `/solutions/business-ai/` |
| `/students/` | `/solutions/students/` |
| `/consumers/` | `/solutions/consumers/` |
| `/bedrift/` | `/solutions/business-ai/` |
| `/studenter/` | `/solutions/students/` |
| `/privat/` | `/solutions/consumers/` |
| `/pakker/` | `/solutions/` |
| `/velg/` | `/solutions/` |

Equivalent English legacy routes must redirect to the corresponding `/en/solutions/.../` destination rather than to the Bokmål route.

## 5. Implementation requirements

1. Create or validate all canonical destination pages before enabling redirects.
2. Use permanent server/platform redirects. Do not use client-side JavaScript redirects.
3. Preserve query parameters used for attribution unless they contain prohibited or sensitive values.
4. Avoid redirect chains and loops. Every legacy route must resolve directly to the final canonical route in one redirect.
5. Update all internal navigation, CTA links, footer links, Gamma references, CMS route fields, onboarding routes, and email templates to the canonical URLs.
6. Update canonical tags, hreflang links, BreadcrumbList structured data, Service schema, FAQ references, and Open Graph URLs.
7. Update the XML sitemap only after the destination pages and redirects are active. Remove superseded URLs from the sitemap.
8. Keep legacy routes operational as redirects for a minimum monitored transition period; do not return 404 for known historical routes.
9. Update analytics route names and conversion events so historical and new paths can be reconciled without double counting.
10. Record the route release in the implementation register with owner, timestamp, evidence, rollback plan, and approval status.

## 6. GitHub changes required after approval

- Replace `/business/`, `/students/`, and `/consumers/` entries in `sitemap.xml` with the canonical `/solutions/.../` routes and matching `/en/` routes.
- Move or recreate the static mirror pages under:
  - `solutions/business-ai/index.html`
  - `solutions/students/index.html`
  - `solutions/consumers/index.html`
- Retain lightweight redirect stubs or platform redirect rules for legacy GitHub Pages URLs where technically supported.
- Update all repository-internal links, canonical tags, alternate-language links, breadcrumbs, and metadata.
- Add an automated route validation test that fails on:
  - legacy route references in public content;
  - redirect chains;
  - canonical/hreflang mismatch;
  - sitemap entries that redirect;
  - broken internal links.

## 7. Wix changes required after approval

- Set the three audience pages to the canonical routes.
- Add permanent URL redirects in Wix URL Redirect Manager for all superseded routes.
- Confirm Wix Multilingual generates or permits the matching English hierarchy.
- Update CMS records in `AtlasPagePlan`, `AtlasCustomerSegments`, `AtlasPackages`, `AtlasPricingPlans`, and `AtlasOnboardingRoutes` where route or slug fields reference legacy URLs.
- Rebind buttons and dynamic-page links after slug changes.
- Verify the pricing and onboarding flows retain the correct audience context after redirect.

## 8. Gamma correction requirements

Gamma is reference input, not the operational CMS. All draft CTA URLs must nevertheless be corrected before further Wix transfer:

- Replace `/bedrift` with `/solutions/business-ai/`.
- Replace `/studenter` with `/solutions/students/`.
- Replace `/privat` with `/solutions/consumers/`.
- Replace `/pakker` and `/velg` with `/solutions/` unless a future approved package finder receives a separate canonical route.

## 9. Validation and acceptance criteria

The route correction is acceptable only when all conditions below pass:

- Each canonical route returns HTTP 200 and renders the intended audience page.
- Each legacy route returns one permanent redirect to the correct canonical route.
- No redirect loop or multi-hop chain is present.
- Canonical tags are self-referential on destination pages.
- Bokmål and English hreflang pairs are reciprocal and resolve to HTTP 200 pages.
- Sitemap contains only canonical, indexable HTTP 200 URLs.
- Internal navigation and CTA scans contain no legacy audience routes.
- Breadcrumbs and structured data use the canonical paths.
- Wix forms and onboarding retain the correct audience/plan parameter after redirect.
- Analytics records one landing route and does not double count the redirect and destination as separate page conversions.
- Search Console inspection shows no blocking canonical or redirect error.
- Mobile and desktop navigation tests pass.
- A rollback procedure has been tested in staging or documented with exact steps.

## 10. Release order

1. Approve this recommendation and route ownership.
2. Create/validate canonical pages in Wix staging and GitHub static mirror.
3. Update CMS links, content links, Gamma CTAs, metadata, and structured data.
4. Implement redirects in staging.
5. Run automated and manual validation.
6. Deploy canonical pages and redirects together.
7. Update sitemap and submit it after production verification.
8. Monitor 404s, redirect errors, indexing, and conversion attribution for at least 30 days.
9. Close the route migration only after evidence is stored in GitHub.

## 11. Rollback rule

If a destination page fails, audience context is lost, checkout/onboarding breaks, or indexing errors materially increase, disable the affected redirect and restore the last known working route configuration. Do not delete legacy content until the monitored transition is complete.

## 12. Decision status

This document records the recommended canonical route correction. Because it affects public URLs, SEO, analytics, and production availability, implementation remains **PENDING_REVIEW** until explicitly approved and validated.