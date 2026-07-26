# Atlas AI Consumer Checkout Legal Readiness Matrix — 03:14, 26.07.2026

**Scope:** Norwegian consumer subscriptions and top-ups  
**Original report:** `20:37, 25.07.2026` — DOCX and Markdown now ingested with checksums  
**Independent controlled report:** `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`  
**Research state:** `RESEARCH_COMPLETED_ORIGINAL_AND_INDEPENDENT_PACKS_CONTROLLED`  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Implementation:** `NOT_IMPLEMENTED`  
**Checkout state:** `NO_GO`

> Original-artifact ingestion closes the evidence-availability blocker only. It does not approve the report’s Atlas-specific interpretations, consumer copy, MVA treatment, implementation or release.

| Gate | Requirement | Current evidence | Result | Required next evidence |
|---|---|---|---|---|
| LEG-001 | Offer-by-offer classification | Original and independent reports treat subscriptions as continuing digital services; top-ups/components remain separately unresolved | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed Norwegian offer/component classification |
| LEG-002 | Complete pre-contract information | Full Bokmål/English terms and disclosure drafts exist | `PARTIAL / DRAFT_COMPLETE` | Counsel approval and rendered-page mapping |
| LEG-003 | Information immediately before order | Final-summary specification and tests exist; no live checkout | `NOT_IMPLEMENTED` | Wix desktop/tablet/mobile rendered evidence |
| LEG-004 | Unambiguous payment-obligation control | Original and independent reports agree on explicit button wording; native Wix text remains constrained | `PARTIAL / IMPLEMENTATION_PENDING` | Counsel approval and exact functional test |
| LEG-005 | Early service commencement | Separate unticked early/delayed-start design and audit fields exist | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval, implementation and event readback |
| LEG-006 | Service versus digital-content withdrawal treatment | Subscription distinction supported by statutory analysis and CJEU C-234/25; Atlas application and top-ups remain unresolved | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed classification and exception analysis |
| LEG-007 | Durable-medium confirmation | Complete template, attachment requirements and delivery controls exist | `NOT_IMPLEMENTED` | Immutable snapshot, email/PDF and delivery tests |
| LEG-008 | Withdrawal notice and form | Complete Bokmål/English draft notice and model form exist | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and operational route |
| LEG-009 | Proportional payment | Competing conservative calculation proposals documented; no approved formula or ledger | `PARTIAL / PENDING_LEGAL_REVIEW` | Approved formula and refund tests |
| LEG-010 | Simple cancellation and account-access fallback | Portal/email workflow designed; Members Area absent | `BLOCKED` | Implemented portal, fallback and end-to-end tests |
| LEG-011 | Recurring billing, annual/semester and pause terms | Monthly model drafted; annual and semester expressly blocked; pause controls drafted | `PARTIAL / PENDING_LEGAL_REVIEW` | Approved term/prepayment/binding model and reminder tests |
| LEG-012 | Refund and remedy matrix | Reason-coded statutory-remedy matrix and internal SOPs exist | `PARTIAL / IMPLEMENTATION_PENDING` | Legal/finance approval and payment/accounting tests |
| LEG-013 | Top-up and boost classification | Fixed-entitlement recommendation, disclosure and ledger controls exist | `BLOCKED / PENDING_LEGAL_AND_TAX_REVIEW` | Signed classification, tax point and refund model |
| LEG-014 | Family, age, guardian and household controls | Adult-payer/no-minor-purchase design exists; enforceable controls absent | `BLOCKED` | Legal/privacy approval and identity/guardian tests |
| LEG-015 | Price and service changes | Draft clauses and durable-notice requirements exist | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and change-flow tests |
| LEG-016 | Consumer-content export/deletion | Required workflow, evidence objects and test cases defined | `BLOCKED` | Approved lifecycle and operational evidence |
| LEG-017 | Wix capability mapping | Detailed native Wix, Wix+Velo, external-backend and manual matrix exists; official Wix constraints rechecked | `PASS_DESIGN / IMPLEMENTATION_BLOCKED` | Implemented components and acceptance evidence |
| LEG-018 | Bokmål/English parity | Full bilingual draft exists | `PARTIAL / NOT_REVIEWED` | Legal and linguistic parity review |
| LEG-019 | Accessibility | Detailed checkout/cancellation test suite exists; no live flow | `NOT_RUN` | WCAG and manual assistive-technology evidence |
| LEG-020 | Legal and release approval | Absent | `NO_GO` | Named counsel approval and written release decision |
| LEG-021 | Research artifact ingestion and exact review | Original 20:37 DOCX/Markdown ingested; SHA-256, heading parity, content equivalence and primary-source reconciliation completed; independent 02:06 pack remains controlled | `PASS_EVIDENCE_INGESTION / LEGAL_PENDING` | Counsel reviews exact controlled files; normalize citations for archival portability |
| LEG-022 | 2026 amendment effective-date check | Law 19.06.2026 no. 34 confirmed not in force on 25.07.2026 | `PASS_AS_OF_25_07_2026` | Recheck official commencement before implementation and launch |
| LEG-023 | Citation portability | Raw reports preserve conversation-local citation tokens that do not resolve outside the originating research session; persistent official-source reconciliation now covers load-bearing requirements | `FAIL_FULL_ARCHIVAL_PORTABILITY / MITIGATED_CORE_REQUIREMENTS` | Use stable identifiers in all future reports and reconstruct additional citations only when a proposition is relied upon |

## Controlled research outputs

1. `ATLAS_CONSUMER_LAW_REPORT_REVIEW_0208_26072026.md`.
2. `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`.
3. `ATLAS_CONSUMER_TERMS_BOKMAL_AND_ENGLISH_DRAFT_0206_26072026.md`.
4. `ATLAS_CHECKOUT_DISCLOSURE_WITHDRAWAL_CANCELLATION_REFUND_OPERATIONS_PACK_0206_26072026.md`.
5. `ATLAS_WIX_VELO_BACKEND_CONSUMER_CHECKOUT_IMPLEMENTATION_AND_TEST_MATRIX_0206_26072026.md`.
6. `ATLAS_ORIGINAL_CONSUMER_LAW_REPORT_VALIDATION_AND_RECONCILIATION_0314_26072026.md`.
7. `../../evidence/research/2026-07-25/ATLAS_CONSUMER_LAW_CHECKOUT_REPORT_2037_25072026_RAW.md.gz.b64`.
8. `ATLAS_CONSUMER_LAW_PERSISTENT_SOURCE_RECONCILIATION_0314_26072026.md`.
9. `../../evidence/research/2026-07-25/ATLAS_RESEARCH_ARTIFACT_INTEGRITY_MANIFEST_0314_26072026.json`.
10. `../tax/ATLAS_MVA_IMPLEMENTATION_AND_PROFESSIONAL_REVIEW_PACK_0206_26072026.md`.

## Verified implementation evidence

- Wix Pricing Plans count remains `0`.
- Student Basic, Student Plus, Everyday Basic and Family record completed research/draft status only.
- `checkoutLegalStatus=NO_GO`, `professionalSignoffRequired=true`, `publicAllowed=false` and `purchaseAllowed=false` remain unchanged.
- Family remains separately blocked by identity, age, guardian and household controls.
- No public plan, checkout, payment activation or production claim was created.

## Control outcome

Artifact ingestion and static evidence validation are complete. Professional approval, Wix/Velo/backend implementation, payment and tax configuration, identity/Family controls, durable-medium delivery, refund/accounting reconciliation, bilingual parity, accessibility and acceptance testing remain incomplete. Consumer checkout and overall public release remain `NO_GO`.
