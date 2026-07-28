# Atlas AI Phase 1 FAQ CMS Hardening Addendum — 13:11, 28.07.2026

**Project:** Atlas Website / Atlas AI  
**Wix site:** `Atlas-AI`  
**Site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Classification:** Implementation and verified fail-closed controls `AUTO_APPROVED`; final public copy, claims, legal/privacy approval, Studio implementation, accessibility and release remain `PENDING_REVIEW` / `NO_GO`.

## 1. Governing scope

FAQ remains the fifteenth Phase 1 public page role under Resources:

- Bokmål: `/resources/faq/`
- English: `/en/resources/faq/`

This addendum supplements the current Phase-by-Phase Implementation Guide and Wix/Gamma Copy and Route Pack. It does not publish the site or relax any activation control.

## 2. Controlled CMS architecture

### 2.1 Private working collection

`AtlasFAQs` is the editorial and governance collection.

Permissions:

- item read: `CMS_EDITOR`
- item insert: `CMS_EDITOR`
- item update: `CMS_EDITOR`
- item remove: `CMS_EDITOR`

The working collection may contain drafts, review metadata, rejected or archived material and records not approved for public rendering. It must never be connected directly to the public FAQ page.

### 2.2 Public rendering collection

`AtlasFAQsPublic` is the only collection permitted for the public FAQ page.

Permissions:

- item read: `ANYONE`
- item insert: `CMS_EDITOR`
- item update: `CMS_EDITOR`
- item remove: `CMS_EDITOR`

The public collection must contain only exact, approved promotion copies. It remains empty until the relevant content, claim, legal/privacy, bilingual, accessibility and release gates pass.

### 2.3 Promotion rule

A working FAQ record may be promoted only when all of the following are true:

1. a stable `faqKey` exists;
2. the reciprocal Bokmål/English record exists and has the same substantive meaning;
3. `phase=PHASE_1` and `pagePlacement=resources_faq`;
4. the record has an approved content version;
5. content, claim and applicable legal/privacy/provider/commercial reviews pass;
6. the exact promoted record is approved for public rendering;
7. the target page, locale routing, accessibility and release candidate pass validation.

Promotion must copy the exact approved record to `AtlasFAQsPublic`; it must not change the private working record into a publicly readable draft.

## 3. Required working-record controls

The private collection now includes:

- `faqKey`
- `contentVersion`
- `reviewOwner`
- `approvedAt`
- `reviewDue`
- `claimReviewStatus`
- `recordStatus`
- `translationPairStatus`
- `publicSyncStatus`
- the existing locale, phase, placement, review, claim-reference and fail-closed publication fields.

`publicAllowed=false`, `schemaEligible=false` and `publicSyncStatus=NOT_SYNCED_PUBLIC` remain the default until exact approval and promotion.

## 4. Phase 1 customer FAQ inventory

The working collection contains fourteen reciprocal customer topics, each represented in Bokmål and English:

1. What Atlas AI is.
2. Who Atlas AI is for, including the minimum-age and controlled 16–17 activation boundary.
3. How AI platforms are selected.
4. Whether AI licences and API costs are included.
5. How usage allowances, hard caps and no automatic chargeable overage work.
6. The prohibition on confidential or sensitive material in ordinary public forms.
7. Managed Secure as qualification and architecture review only.
8. The prohibition on blanket GDPR-compliance or certification claims.
9. Provider- and configuration-dependent processing and storage locations.
10. Provider- and configuration-dependent model-training/data-use settings.
11. AI-output limitations and the need for qualified human review.
12. Student academic-integrity boundaries.
13. Consumer emotional-dependence, emergency and high-stakes-use boundaries.
14. Controlled low-risk onboarding and contact.

Current verified inventory:

- 28 active working records;
- 14 Bokmål/English pairs;
- one archived internal editorial record;
- zero public records.

## 5. Archived editorial record

The former customer-facing question about how pages should be structured for answer engines is retained only as internal editorial history:

- `phase=INTERNAL_EDITORIAL`
- `pagePlacement=internal_only`
- `recordStatus=ARCHIVED_INTERNAL_EDITORIAL`
- `publicAllowed=false`
- `schemaEligible=false`
- `publicSyncStatus=BLOCKED_INTERNAL_ONLY`

Internal SEO/AEO production instructions must not be presented as customer FAQ content.

## 6. Structured-data rule

The FAQ metadata baseline uses `WebPage` and `BreadcrumbList`. FAQ entries remain `schemaEligible=false` until implementation-time review.

No Atlas record may promise:

- FAQ rich results;
- guaranteed rankings;
- generative-search inclusion;
- permanent provider/search features.

Any later structured data must exactly match visible approved content and current provider eligibility rules.

## 7. Wix Studio binding contract

The accessible accordion/repeater on both locale routes must bind to `AtlasFAQsPublic`, not `AtlasFAQs`.

Required page validation includes:

- public-collection-only binding;
- correct locale;
- Phase 1 and page-placement filtering where applicable;
- approved sort order;
- no archived/internal record rendering;
- keyboard operation and visible focus;
- screen-reader labels and expanded/collapsed state;
- contrast and reflow;
- desktop, tablet and mobile layouts;
- canonical and reciprocal hreflang;
- internal links and metadata parity;
- performance checks;
- exact release-candidate approval.

## 8. Release state

The following remain unchanged:

- `publicAllowed=false`
- `purchaseAllowed=false`
- `releaseApproved=false`
- Wix site remains Draft / `NO_GO`
- `AtlasFAQsPublic` contains zero records
- no checkout, real payment, production entitlement, provider credential, confidential intake or public Managed Secure availability is enabled.

## 9. Remaining Phase 1 work

1. Review and approve the final FAQ v2.0 copy derived from the strongest Gamma alternative.
2. Complete claim, legal/privacy, provider, commercial, student and consumer-safety reviews.
3. Approve the exact reciprocal Bokmål/English pairs.
4. Transfer and validate the selected design in Figma.
5. Create and bind the Wix Studio pages to `AtlasFAQsPublic`.
6. Run accessibility, responsive, SEO, canonical, hreflang, performance and route acceptance tests.
7. Promote only the exact approved records.
8. Issue an explicit Phase 1 release decision.
