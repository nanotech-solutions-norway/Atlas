# ATLAS PROJECT LOG UPDATE PACK — WIX NON-HOME CONTENT ALIGNMENT

Timestamp: 00:50, 31.07.2026 Europe/Oslo  
Session/task: Align non-home Wix content with current Atlas business plan and governance  
Project: Atlas Website / Atlas AI

## Issue or mistake observed

The Wix draft contained June-era commercial copy, unsupported operational/security claims, internal QA instructions, untranslated form text, obsolete Student Basic/Plus and Family structures, proposed prices, early-access labels, and mixed English/Norwegian terminology.

## Root cause

The visual pages were assembled from several historical Gamma, Figma, CMS, strategy and legal/trust source generations. Later approved business-model, safety, pricing, student-age, provider and release decisions had not been fully reconciled into the Wix design-time text layer.

## Corrective rule

- Use the current approved Atlas source hierarchy before changing Wix copy.
- Treat business/professional as the primary route and student/private as controlled secondary routes.
- Do not describe Managed Secure or other controls as available or operational without exact implementation evidence.
- Do not expose internal QA, review status or implementation instructions as visitor copy.
- Do not publish prices, access, entitlement or provider claims before approval.
- Use `AI` on non-home pages as explicitly instructed by the user; reserve the AI/KI explanation for the future Home-page workstream.
- Keep public forms low-risk, file-free and non-sensitive.

## Evidence/source

- Authenticated Wix Translation Content API read/write/readback
- Current Atlas business strategy, Trust copy, legal/privacy controls and source-authority records
- Existing Figma and Gamma Contact/FAQ source comparison
- Current `atlas_wix` repository and Atlas governance PR #37
- Official Språkrådet and Digdir plain-language guidance

## Action taken

- Updated all fourteen non-home public-role pages and the low-risk qualification form.
- Left Home, images and Gamma image-placeholder tokens unchanged.
- Removed obsolete pricing and plan labels.
- Replaced unsupported claims and internal instructions with conditional, visitor-facing copy.
- Standardized terminology and Norwegian translations.
- Confirmed every write remained unpublished.
- Added detailed validation evidence to the existing draft PR branch.

## Unresolved items

- Rendered responsive and accessibility validation
- Button/text overflow and hierarchy checks
- Route, link, dataset and form-behaviour tests
- English locale reconciliation
- Final public legal, trust, privacy, claims and pricing approval
- Separate Home-page content workstream
- Release acceptance and publication

## Classification

AUTO_APPROVED:
- Exact user terminology correction
- Removal of verified obsolete plan/pricing labels
- Verified low-risk form translation
- Removal of internal QA text
- Source-supported correction of unsupported claims
- Non-sensitive workflow and quality-control improvements

PENDING_REVIEW:
- Public legal/privacy/trust claims
- Commercial prices and entitlements
- Provider/API policy statements
- Production availability and release decisions

Release state: `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.
