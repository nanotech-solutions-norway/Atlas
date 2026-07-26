# Atlas AI Consumer Checkout Legal Readiness Matrix — Updated 02:06, 26.07.2026

**Scope:** Norwegian consumer subscriptions and top-ups  
**Research mandate:** `EXECUTED_DRAFT_PACK_CREATED`  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Implementation:** `NOT_IMPLEMENTED`  
**Checkout state:** `NO_GO`

> Research completion does not constitute legal approval, implementation, validation or release approval.

| Gate | Requirement | Current evidence | Result | Required next evidence |
|---|---|---|---|---|
| LEG-001 | Offer-by-offer legal classification under Angrerettloven and Digitalytelsesloven | Continuing-digital-service research position and rights matrix created | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed Norwegian legal classification memorandum |
| LEG-002 | Complete pre-contract information under Angrerettloven § 8 and electronic-contract rules | Bokmål/English disclosure and terms drafts created | `PARTIAL / DRAFT_COMPLETE` | Counsel approval and mapped rendered pages |
| LEG-003 | Required information displayed clearly and prominently immediately before order | Final-summary specification and tests created; no live checkout | `NOT_IMPLEMENTED` | Wix layout, device screenshots and functional evidence |
| LEG-004 | Payment button unambiguously acknowledges obligation to pay | Approved-research wording set created | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and functional test of exact button |
| LEG-005 | Early commencement request for paid service during withdrawal period | Separate unticked-consent wording and data fields created | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval, implementation and readback evidence |
| LEG-006 | Correct distinction between service and digital-content withdrawal loss | Research concludes subscriptions are continuing digital services; top-ups remain unresolved | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed classification for subscriptions/components/top-ups |
| LEG-007 | Durable-medium confirmation before service performance | Complete Bokmål/English template and evidence design created | `NOT_IMPLEMENTED` | Immutable attachment/snapshot and delivery tests |
| LEG-008 | Withdrawal notice and statutory form | Bokmål/English notice and model form created | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and operational route |
| LEG-009 | Proportional-payment method for early-started service | Draft elapsed-service-time method and zero-charge exceptions created | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and refund calculation tests |
| LEG-010 | Cancellation method no harder than contracting and available without account lockout | Portal plus email fallback designed; Members Area absent | `BLOCKED` | Members Area/portal implementation and acceptance tests |
| LEG-011 | Recurring billing, renewal, annual/semester and pause terms | Monthly model drafted; annual and semester models explicitly blocked | `PARTIAL / PENDING_LEGAL_REVIEW` | Approved annual/semester/benefit/binding model and tests |
| LEG-012 | Refund and statutory-remedy matrix | Consumer matrix, reason codes and SOP created | `PARTIAL / PENDING_LEGAL_AND_FINANCE_REVIEW` | Counsel/accountant approval and sandbox tests |
| LEG-013 | Top-up/boost legal classification, expiry, withdrawal and refund | Fixed-entitlement recommendation and checkout controls created | `PARTIAL / PENDING_LEGAL_AND_TAX_REVIEW` | Signed classification and tax-point/refund model |
| LEG-014 | Family/minor/guardian/household controls | Adult-payer and no-minor-purchase design created | `BLOCKED` | Legal/privacy approval and enforceable identity controls |
| LEG-015 | Service-change, provider/model substitution and price-change rights | Draft terms and durable-notice requirements created | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and change-flow tests |
| LEG-016 | Customer-content export/deletion after withdrawal/termination | Required workflow and evidence objects defined | `BLOCKED` | Approved lifecycle and operational tests |
| LEG-017 | Wix capability and limitation mapping | Requirement-by-requirement Wix/Velo/backend matrix and tests created | `PASS_DESIGN / IMPLEMENTATION_BLOCKED` | Implemented components and test evidence |
| LEG-018 | Bokmål and English parity | Full bilingual draft pack created | `PARTIAL / NOT_REVIEWED` | Legal and linguistic parity review |
| LEG-019 | Accessibility of checkout, consent and legal information | Accessibility test suite defined; no live flow | `NOT_RUN` | WCAG/manual validation on implemented flow |
| LEG-020 | Legal sign-off and release approval | Absent | `NO_GO` | Named Norwegian counsel approval and written release decision |

## Controlled research outputs

1. `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`.
2. `ATLAS_CONSUMER_TERMS_BOKMAL_AND_ENGLISH_DRAFT_0206_26072026.md`.
3. `ATLAS_CHECKOUT_DISCLOSURE_WITHDRAWAL_CANCELLATION_REFUND_OPERATIONS_PACK_0206_26072026.md`.
4. `ATLAS_WIX_VELO_BACKEND_CONSUMER_CHECKOUT_IMPLEMENTATION_AND_TEST_MATRIX_0206_26072026.md`.

## Current official-source checkpoints

- The final paid-order step must make the payment obligation unambiguous and must be preceded immediately by the required prominent information.
- Durable-medium confirmation and a valid express request are required for the selected early-service-start model.
- A continuing digital-service subscription must not be treated as losing withdrawal rights merely because access is activated.
- Ordinary cancellation, withdrawal, statutory termination, price reduction and refund remain separate legal/operational routes.
- Annual/semester, top-up and Family/minor conclusions remain subject to Norwegian legal review.

## Control outcome

The research mandate is executed and implementation-ready drafts exist. No Norwegian lawyer has approved the legal conclusions or copy. No checkout, consent, durable-medium, cancellation, refund, identity, Family or accessibility implementation has passed. Consumer checkout, Wix Pricing Plans creation and paid activation remain prohibited.