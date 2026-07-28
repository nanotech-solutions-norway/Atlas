# ATLAS PROJECT LOG UPDATE PACK — PHASE 1 FAQ CMS HARDENING — 13:11, 28.07.2026

## Timestamp

13:11, 28.07.2026 Europe/Oslo

## Session/task

Implement the recommended Phase 1 FAQ CMS corrections in Wix, record the architecture and validation in canonical GitHub, and synchronize the controlled Google Drive evidence and mirrors.

## Issue or mistake observed

1. The existing `AtlasFAQs` collection was readable by `ANYONE` while it contained draft, legacy and internal editorial records.
2. A page-level `publicAllowed` filter was being treated as the primary protection for draft records even though it did not change collection-level read permission.
3. The English and Bokmål records did not form complete reciprocal pairs.
4. Required Phase 1 trust topics were missing, including usage limits, GDPR claim qualification, processing location, provider training-use configuration and AI-output limitations.
5. An internal AEO/editorial question was stored as a customer FAQ.
6. The discovery record still referenced FAQ structured data as a default rather than an implementation-time controlled choice.

## Root cause

- The FAQ collection was originally created as a combined working and rendering source.
- CMS preparation preceded the latest security/privacy integration and final bilingual content inventory.
- Editorial, customer-content, approval and public-promotion states were not separated.
- Page filtering and collection access permissions were conflated.

## Corrective rule

1. Keep editorial and review content in private `AtlasFAQs` with editor-only access.
2. Render public FAQ content only from `AtlasFAQsPublic`, which is anonymous read-only and editor-write-controlled.
3. Promote exact approved records rather than exposing or repurposing working drafts.
4. Require stable `faqKey`, reciprocal locale pair, content version, review owner, claim-review status, approval state and promotion state.
5. Archive internal production guidance outside the public FAQ inventory.
6. Keep structured-data eligibility false by default and do not promise search-display outcomes.
7. Read back both collection permissions, working-record counts and public-record counts after every FAQ promotion or release preparation.

## Evidence/source

- Explicit current owner instruction, 28.07.2026.
- Canonical decision `ATL-DEC-20260727-032`.
- Active Phase 1 security/privacy implementation and copy baselines dated 27.07.2026.
- Live authenticated Wix collection schema, data permissions, data items and discovery metadata.
- Existing Gamma FAQ v1.0/v1.1 draft validation record.
- Wix CMS collection-management and data-permission documentation.

## Action taken

### Wix schema and access

- Added `faqKey`, `contentVersion`, `reviewOwner`, `approvedAt`, `reviewDue`, `claimReviewStatus`, `recordStatus`, `translationPairStatus` and `publicSyncStatus` to `AtlasFAQs`.
- Changed `AtlasFAQs` permissions to editor-only for read, insert, update and remove.
- Created `AtlasFAQsPublic` as the public rendering collection.
- Set `AtlasFAQsPublic` to anonymous read and CMS-editor-only writes.
- Kept `AtlasFAQsPublic` empty.

### Wix content

- Normalized the existing English and Bokmål records to content version `FAQ-PHASE1-v0.9.0-20260728`.
- Added missing reciprocal records.
- Established fourteen reciprocal customer FAQ topics and twenty-eight active working records.
- Added controlled age, usage-cap, privacy, provider, responsible-AI, student and consumer-safety boundaries.
- Removed provider-specific secure-runtime assumptions from customer-facing wording.
- Set every active record to `publicAllowed=false`, `schemaEligible=false`, `claimReviewStatus=PENDING` and `publicSyncStatus=NOT_SYNCED_PUBLIC`.
- Archived the internal AEO question with `publicSyncStatus=BLOCKED_INTERNAL_ONLY`.

### Wix discovery metadata

- Required Studio binding to `AtlasFAQsPublic`, not `AtlasFAQs`.
- Changed the default schema baseline to `WebPage` and `BreadcrumbList`.
- Preserved `NOINDEX` until content, route, bilingual, accessibility and release gates pass.
- Preserved page-level `publicAllowed=false`.

### GitHub

- Created `active-source/2026-07-28/ATLAS_PHASE_1_FAQ_CMS_HARDENING_ADDENDUM_1311_28072026.md`.
- Created this project log update pack.
- Updated the canonical decision and validation registers.

### Google Drive

- Updated the controlled FAQ CMS and publication-readiness records.
- Updated the applicable canonical mirrors.
- Created a dated six-register snapshot and verified the expected children.

## Validation performed

| Check | Result |
|---|---|
| `AtlasFAQs` read permission | PASS — `CMS_EDITOR` |
| `AtlasFAQs` write permissions | PASS — `CMS_EDITOR` |
| `AtlasFAQsPublic` read permission | PASS — `ANYONE` |
| `AtlasFAQsPublic` write permissions | PASS — `CMS_EDITOR` |
| Active working records | PASS — 28 |
| Reciprocal topic pairs | PASS — 14 Bokmål/English pairs |
| Archived internal editorial records | PASS — 1 |
| Public FAQ records | PASS_LOCK — 0 |
| Active-record `publicAllowed` | PASS_LOCK — false |
| Active-record `schemaEligible` | PASS_LOCK — false |
| Discovery page public flag | PASS_LOCK — false |
| Public checkout or production effect | NONE / NO_GO |

## Unresolved items

1. Final public-copy selection and owner approval.
2. Claims, privacy/legal, provider, commercial, student and consumer-safety review.
3. Figma implementation and geometry/interaction validation.
4. Wix Studio page creation and binding on both locale routes.
5. Accessibility, responsive, canonical, hreflang, metadata, internal-link and performance testing.
6. Exact record promotion to `AtlasFAQsPublic`.
7. Fresh current Wix Studio page-tree evidence.
8. Explicit Phase 1 release approval.

## Classification

- Verified schema, access separation, content normalization, reciprocal working inventory, archived editorial record, discovery metadata and readback: `AUTO_APPROVED`.
- The private/public collection architecture and Studio binding rule under the explicit owner instruction: `APPROVED`.
- Final public copy, claim/legal/privacy approvals, structured-data choice, Studio implementation and release: `PENDING_REVIEW` / `NO_GO`.

## Release controls after task

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- `AtlasFAQsPublic` item count: `0`
- checkout disabled
- real payments disabled
- production entitlements disabled
- public Managed Secure availability disabled
