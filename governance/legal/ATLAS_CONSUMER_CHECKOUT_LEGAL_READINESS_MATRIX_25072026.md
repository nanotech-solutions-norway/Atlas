# Atlas AI Consumer Checkout Legal Readiness Matrix — 02:08, 26.07.2026

**Scope:** Norwegian consumer subscriptions and top-ups  
**Report referenced:** 20:37, 25.07.2026  
**Report artifact:** `NOT_FOUND_IN_CANONICAL_GITHUB_OR_CONTROLLED_DRIVE`  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Checkout state:** `NO_GO`

| Gate | Requirement | Current evidence | Result | Required next evidence |
|---|---|---|---|---|
| LEG-001 | Offer-by-offer classification | Primary-source working view supports continuing digital-service treatment; report artifact unavailable | `PARTIAL` | Ingest report and obtain signed Norwegian legal classification |
| LEG-002 | Complete pre-contract information | Statutory requirement verified; final bilingual copy absent | `PARTIAL` | Approved copy mapped to every customer surface |
| LEG-003 | Information immediately before order | No checkout | `NOT_RUN` | Wix rendered evidence and test |
| LEG-004 | Unambiguous payment-obligation control | Angrerettloven § 16 verified | `PASS_REQUIREMENT / IMPLEMENTATION_PENDING` | Approved wording and functional test |
| LEG-005 | Early service commencement | Angrerettloven § 19 verified; no consent design | `BLOCKED` | Approved unchecked interaction and audit fields |
| LEG-006 | Service versus digital-content withdrawal treatment | Statutory distinction verified; Atlas component classification unsigned | `BLOCKED` | Signed offer/component matrix |
| LEG-007 | Durable-medium confirmation | No implemented order flow | `NOT_IMPLEMENTED` | Confirmation template and delivery test |
| LEG-008 | Withdrawal notice and form | No controlled final bilingual pack | `BLOCKED` | Approved notice, form and support process |
| LEG-009 | Proportional payment | Statutory conditions identified; Atlas calculation absent | `BLOCKED` | Calculation rule and refund test |
| LEG-010 | Simple cancellation and account-access fallback | Digitalytelsesloven § 33 verified; Members Area absent | `BLOCKED` | Portal and email fallback tests |
| LEG-011 | Recurring billing, annual/semester and pause terms | Statutory rules verified; final terms absent | `PARTIAL` | Approved terms and reminder flow |
| LEG-012 | Refund and remedy matrix | High-level statutory framework only | `BLOCKED` | Consumer policy and internal SOP |
| LEG-013 | Top-up and boost classification | Working prepaid-entitlement view only | `BLOCKED` | Signed classification and separate checkout copy |
| LEG-014 | Family, age, guardian and household controls | Not implemented | `BLOCKED` | Legal rules and enforceable controls |
| LEG-015 | Price and service changes | Digitalytelsesloven §§ 28 and 41–42 verified | `PARTIAL` | Approved clause and durable-medium notice |
| LEG-016 | Consumer-content export/deletion | Duty identified; architecture incomplete | `BLOCKED` | Data lifecycle workflow |
| LEG-017 | Wix capability mapping | High-level gap map only | `PARTIAL` | Detailed Wix/Velo/backend matrix and tests |
| LEG-018 | Bokmål/English parity | Final pack absent | `NOT_RUN` | Parity review |
| LEG-019 | Accessibility | No live flow | `NOT_RUN` | Accessibility validation |
| LEG-020 | Legal and release approval | Absent | `NO_GO` | Counsel approval and written release decision |
| LEG-021 | Report ingestion and exact review | Title known; artifact unavailable | `BLOCKED` | Complete report, version, checksum and line-by-line review |
| LEG-022 | 2026 amendment effective-date check | Law 19.06.2026 no. 34 enters into force when the King determines | `PASS_AS_OF_25_07_2026` | Recheck before implementation and launch |

## Verified checkpoints

- Angrerettloven § 16 requires prominent prescribed information immediately before an electronic order and an unambiguous acknowledgement of the obligation to pay. Non-compliance can mean the consumer is not bound.
- Sections 19 and 22 distinguish early commencement of a service from delivery of non-physical digital content. Immediate account activation does not automatically eliminate withdrawal rights for a continuing service.
- Sections 21 and 26 govern the service withdrawal period and any proportionate payment after a valid early-start request.
- Digitalytelsesloven § 1 supports the working digital-service classification. Section 33 governs simple cancellation, binding periods and continuation reminders. Sections 28 and 41–42 govern price and material service changes.
- The 2026 electronic-withdrawal-function amendment was not applied as current law on 25.07.2026 because its commencement remained subject to a later decision.

## Control outcome

The statutory baseline is clearer, but the generated report, final consumer terms, implementation, evidence logs, acceptance tests and legal approval remain incomplete. All public and purchasing locks remain unchanged.