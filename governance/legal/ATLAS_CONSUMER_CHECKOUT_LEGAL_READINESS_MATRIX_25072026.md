# Atlas AI Consumer Checkout Legal Readiness Matrix — 03:14, 26.07.2026

**Scope:** Norwegian consumer subscriptions and top-ups  
**Original report:** `20:37, 25.07.2026` — DOCX and Markdown ingested with checksums and source reconciliation  
**Independent controlled research report:** `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`  
**Current-source validation:** `../validation/ATLAS_EXTERNAL_SOURCE_VALIDATION_UPDATE_0308_26072026.md`  
**Professional decision pack:** `../review/ATLAS_PROFESSIONAL_LEGAL_TAX_DECISION_PACK_0308_26072026.md`  
**Research state:** `RESEARCH_COMPLETED_ORIGINAL_AND_INDEPENDENT_PACKS_CONTROLLED`  
**Professional-review preparation:** `READY_FOR_SUBMISSION`  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Implementation:** `NON_PUBLIC_FOUNDATION_STARTED / CUSTOMER_FLOW_NOT_IMPLEMENTED`  
**Checkout state:** `NO_GO`

> Original-artifact ingestion closes the report-availability blocker only. Research completion, source validation, contract-schema creation and artifact integrity checks do not constitute professional approval, customer-flow implementation, acceptance validation or release approval.

| Gate | Requirement | Current evidence | Result | Required next evidence |
|---|---|---|---|---|
| LEG-001 | Offer-by-offer classification | Original and independent reports plus current-source review support a continuing-digital-service working view; top-ups/components remain separately unresolved | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed Norwegian offer/component classification |
| LEG-002 | Complete pre-contract information | Full Bokmål/English terms and disclosure drafts exist | `PARTIAL / DRAFT_COMPLETE` | Counsel approval and rendered-page mapping |
| LEG-003 | Information immediately before order | Final-summary specification, negative-path vectors and tests exist; no customer checkout | `NON_PUBLIC_DESIGN_COMPLETE / NOT_IMPLEMENTED` | Wix desktop/tablet/mobile rendered evidence |
| LEG-004 | Unambiguous payment-obligation control | Statutory requirement revalidated; original and independent reports agree on explicit button wording; prohibited-label tests exist | `PASS_REQUIREMENT / IMPLEMENTATION_PENDING` | Counsel approval and exact functional test |
| LEG-005 | Early service commencement | §§ 18–19 revalidated; separate unticked early/delayed-start design and consent schema exist | `PASS_REQUIREMENT / PENDING_LEGAL_REVIEW` | Counsel approval, implementation and event readback |
| LEG-006 | Service versus digital-content withdrawal treatment | Subscription distinction documented and supported by CJEU C-234/25; top-up and discrete-component treatment remains unresolved | `PARTIAL / PENDING_LEGAL_REVIEW` | Signed classification and exception analysis |
| LEG-007 | Durable-medium confirmation | Requirement revalidated; complete template, snapshot fields and delivery controls exist | `PASS_REQUIREMENT / NOT_IMPLEMENTED` | Immutable snapshot, email/PDF and delivery tests |
| LEG-008 | Withdrawal notice and form | Complete Bokmål/English draft notice and model form exist | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and operational route |
| LEG-009 | Proportional payment | § 26 conditions revalidated; competing conservative calculation proposals and zero-charge rules documented | `PASS_REQUIREMENT / FORMULA_PENDING_LEGAL_REVIEW` | Approved formula and case/refund tests |
| LEG-010 | Simple cancellation and account-access fallback | § 33 and Wix asynchronous cancellation mechanics revalidated; portal/email workflow designed; Members Area absent | `BLOCKED` | Implemented portal, fallback, state machine and end-to-end tests |
| LEG-011 | Recurring billing, annual/semester and pause terms | Monthly model drafted; binding-period restrictions revalidated; annual and semester blocked | `PARTIAL / PENDING_LEGAL_REVIEW` | Approved term/prepayment/binding model and reminder tests |
| LEG-012 | Refund and remedy matrix | Reason-coded statutory-remedy matrix, cancellation/refund state schema and SOPs exist | `PARTIAL / IMPLEMENTATION_PENDING` | Legal/finance approval and payment/accounting tests |
| LEG-013 | Top-up and boost classification | Fixed-entitlement recommendation, disclosure, ledger controls and deny-by-default test exist | `BLOCKED / PENDING_LEGAL_AND_TAX_REVIEW` | Signed classification, tax point and refund model |
| LEG-014 | Family, age, guardian and household controls | Minor-capacity and child-consent requirements revalidated; adult-payer/no-minor-purchase design exists; controls absent | `BLOCKED` | Legal/privacy approval and identity/guardian tests |
| LEG-015 | Price and service changes | Draft clauses and durable-notice requirements exist | `PARTIAL / PENDING_LEGAL_REVIEW` | Counsel approval and change-flow tests |
| LEG-016 | Consumer-content export/deletion | Required workflow, evidence objects and test cases defined | `BLOCKED` | Approved lifecycle and operational evidence |
| LEG-017 | Wix capability mapping | Detailed native Wix, Wix+Velo, external-backend and manual matrix exists; member-only purchase, asynchronous cancellation, published-site test and site-level tax boundaries revalidated | `PASS_DESIGN / IMPLEMENTATION_BLOCKED` | Implemented components and acceptance evidence |
| LEG-018 | Bokmål/English parity | Full bilingual draft and version-pair failure test exist | `PARTIAL / NOT_REVIEWED` | Legal and linguistic parity review |
| LEG-019 | Accessibility | Current private-sector baseline revalidated as WCAG 2.0 A/AA with stated exceptions; detailed journey tests exist; no live flow | `PASS_REQUIREMENT / NOT_RUN` | Legal confirmation, implemented UI and documented automated/manual evidence |
| LEG-020 | Legal and release approval | Professional decision pack is ready; no approval exists | `NO_GO` | Named counsel approval and written release decision |
| LEG-021 | Research artifact ingestion and exact review | Original 20:37 DOCX/Markdown ingested; SHA-256, 29/29 heading parity, content-equivalence and primary-source reconciliation completed; independent 02:06 pack remains controlled | `PASS_EVIDENCE_INGESTION / LEGAL_PENDING` | Counsel reviews exact controlled files; normalize citations where relied upon |
| LEG-022 | 2026 amendment effective-date check | New § 20 a is enacted; no official commencement decision was identified in the 26.07.2026 validation run | `ENACTED_NOT_VERIFIED_IN_FORCE` | Recheck official commencement before build completion and launch |
| LEG-023 | Professional review decision coverage | LEG-DEC-001–016 and TAX-DEC-001–010 decision questions prepared | `PASS_PREPARATION / APPROVAL_ABSENT` | Signed, dated, version-specific professional memoranda |
| LEG-024 | Fail-closed foundation | Checkout-gate, consent-event and cancellation/refund state schemas plus negative-path vectors created | `PASS_CONTRACT_DESIGN / RUNTIME_NOT_IMPLEMENTED` | Schema validation in CI and controlled service implementation |
| LEG-025 | Controlled member-order test environment | Official Wix guidance indicates member-facing plan APIs require a published site and do not fully operate in preview | `PENDING_REVIEW` | Approved non-public published test architecture and safeguards |
| LEG-026 | Citation portability | Raw reports preserve conversation-local citation tokens; persistent official-source reconciliation covers load-bearing requirements | `FAIL_FULL_ARCHIVAL_PORTABILITY / MITIGATED_CORE_REQUIREMENTS` | Use stable identifiers in all future controlled reports and reconstruct additional citations only when relied upon |

## Controlled research and implementation outputs

1. `ATLAS_CONSUMER_LAW_REPORT_REVIEW_0208_26072026.md`.
2. `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`.
3. `ATLAS_CONSUMER_TERMS_BOKMAL_AND_ENGLISH_DRAFT_0206_26072026.md`.
4. `ATLAS_CHECKOUT_DISCLOSURE_WITHDRAWAL_CANCELLATION_REFUND_OPERATIONS_PACK_0206_26072026.md`.
5. `ATLAS_WIX_VELO_BACKEND_CONSUMER_CHECKOUT_IMPLEMENTATION_AND_TEST_MATRIX_0206_26072026.md`.
6. `../tax/ATLAS_MVA_IMPLEMENTATION_AND_PROFESSIONAL_REVIEW_PACK_0206_26072026.md`.
7. `../validation/ATLAS_EXTERNAL_SOURCE_VALIDATION_UPDATE_0308_26072026.md`.
8. `../review/ATLAS_PROFESSIONAL_LEGAL_TAX_DECISION_PACK_0308_26072026.md`.
9. `../implementation/ATLAS_FAIL_CLOSED_CONSUMER_CHECKOUT_IMPLEMENTATION_BACKLOG_0308_26072026.md`.
10. `../implementation/contracts/atlas-consumer-checkout-gate.schema.json`.
11. `../implementation/contracts/atlas-consent-event.schema.json`.
12. `../implementation/contracts/atlas-cancellation-refund-state.schema.json`.
13. `../implementation/test-vectors/consumer-checkout-negative-paths.v0.1.json`.
14. `ATLAS_ORIGINAL_CONSUMER_LAW_REPORT_VALIDATION_AND_RECONCILIATION_0314_26072026.md`.
15. `ATLAS_CONSUMER_LAW_PERSISTENT_SOURCE_RECONCILIATION_0314_26072026.md`.
16. `../../evidence/research/2026-07-25/ATLAS_CONSUMER_LAW_CHECKOUT_REPORT_2037_25072026_RAW.md.gz.b64`.
17. `../../evidence/research/2026-07-25/ATLAS_RESEARCH_ARTIFACT_INTEGRITY_MANIFEST_0314_26072026.json`.

## Verified implementation evidence

- Wix Pricing Plans count remains `0` from the last authoritative readback.
- Student Basic, Student Plus, Everyday Basic and Family record completed research/draft status only.
- `checkoutLegalStatus=NO_GO`, `professionalSignoffRequired=true`, `publicAllowed=false` and `purchaseAllowed=false` remain unchanged.
- Family remains separately blocked by identity, age, guardian and household controls.
- No public plan, checkout, payment activation, entitlement or production claim was created.
- The schemas and test vectors are static non-public contracts only.

## Control outcome

Original-artifact ingestion, current-source validation, professional-review preparation and fail-closed contract design are complete. Professional approval, contracting-entity completion, Wix/Velo/backend customer-flow implementation, payment and tax configuration, identity/Family controls, durable-medium delivery, entitlement metering, refund/accounting reconciliation, bilingual parity, accessibility and end-to-end acceptance testing remain incomplete. Consumer checkout and overall public release remain `NO_GO`.
