# ATLAS PROJECT LOG UPDATE PACK — 00:47, 22.07.2026

## Session / task

Atlas-AI Wix CMS modernization, route/menu-parent correction, SEO/AEO/GEO and page-experience contract creation, claims cleanup and release-gate migration.

## Issue or mistake observed

1. The CMS contained only eight older page-plan records and omitted seven current Phase 1 page concepts.
2. Legacy names and roles remained active: Packages, Governance, Intake and Managed Secure Mode.
3. The physical target hierarchy was not represented consistently in CMS.
4. Phase 1 and platform records incorrectly stated or implied that Wix was published.
5. The old nine-gate system remained active although the current release model is G00–G22.
6. The claims register contained 22 records but only 17 unique claim topics.
7. Legacy offer and package records contained unapproved prices, SLA language and superseded equal-card product structures without an explicit public-rendering lock.
8. No unified bilingual SEO/AEO/GEO and page-experience metadata contract existed for all current page concepts.
9. No approved Atlas source defines “PEO”; treating it as a separate discovery framework would have introduced an unsupported concept.

## Root cause

The Wix CMS reflected earlier June planning and seed data, while later July Figma reconstructions, route decisions, claims controls and launch-gate specifications had not been written back into the CMS.

## Corrective rule

- Maintain one current page inventory and menu-parent contract in Wix CMS.
- Use `AtlasDiscoveryMetadata` as the governed source for bilingual routes, metadata, visible answer blocks, entity topics, internal links and page-experience checks.
- Keep every page and product release-locked until applicable G00–G22 evidence and explicit approval exist.
- Use outcome-led solution areas and delivery levels; do not render legacy offer names or all package records as equal public products.
- Treat PEO only as Page Experience Optimization unless an approved Atlas definition is added.
- Figma PASS is a design/content handoff, not Wix release evidence.

## Evidence / source

- Current Wix CMS readback and successful write/readback validation, 22.07.2026.
- Atlas AI Figma-to-Wix Section Replacement Map, 20.07.2026.
- Atlas AI Complete Final Presentation and Slide Ranking, 18.07.2026.
- Atlas AI Integrated SEO/AEO/GEO Implementation Blueprint, 11.07.2026.
- Atlas AI Launch Gates and Acceptance Criteria, 11.07.2026.
- Direct Figma readback of Platform lanes v3.

## Action taken

- Expanded `AtlasPagePlan` to 15 records and corrected names, slugs, roles and navigation groups.
- Created and seeded 15 `AtlasDiscoveryMetadata` records.
- Created and seeded 23 `AtlasReleaseGates` records, G00–G22.
- Marked nine older gate records as superseded.
- Corrected platform-plane and phase records; added Phase 6.
- Removed five duplicate claims; validated 17 unique claims and refreshed review dates.
- Added release locks to all 7 legacy offers and all 14 package records.
- Validated hierarchical URL and true-404 SEO settings.
- Wrote the validation record to GitHub.
- Did not publish or mutate Figma designs.

## Unresolved items

- Actual Wix Studio page creation/renaming, menu nesting and route changes.
- Redirects and physical navigation validation.
- Figma-to-Wix section insertion and CMS dataset binding.
- Per-page meta tags, canonical, hreflang, Open Graph and structured-data implementation.
- Sitemap/robots verification after final routes exist.
- Full Bokmål/English visible-content parity.
- Forms, consent, retention, notifications, error handling and backend routing.
- Responsive, accessibility, performance and link/CTA QA.
- Pricing, provider, legal/privacy, audience and Managed Secure approvals.
- Explicit release, smoke test and rollback evidence.

## Classification

AUTO_APPROVED:
- verified inventory and readback;
- duplicate claim removal;
- stale Draft/published status correction;
- menu-parent contracts;
- release locks;
- G00–G22 migration;
- SEO/AEO/GEO metadata preparation;
- Page Experience Optimization checks;
- non-claim-changing workflow and quality rules.

PENDING_REVIEW:
- physical route changes and publication;
- public pricing and SLAs;
- provider eligibility, costs and delivery rights;
- legal/privacy interpretation and documents;
- student, consumer, Family and age treatment;
- Managed Secure operational availability;
- production implementation and release decision.
