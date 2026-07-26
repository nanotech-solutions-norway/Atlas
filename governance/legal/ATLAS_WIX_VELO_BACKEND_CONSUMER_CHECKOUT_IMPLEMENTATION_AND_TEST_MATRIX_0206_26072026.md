# Atlas AI Wix, Velo and Backend Consumer Checkout Implementation and Test Matrix — 02:06, 26.07.2026

**Site:** Atlas-AI  
**Wix site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Editor:** Wix Studio  
**Contract version:** `0.5.1`  
**Implementation state:** `NOT_IMPLEMENTED`  
**Validation state:** `DESIGN_COMPLETE_TESTS_NOT_RUN`  
**Release:** `NO_GO`

> This matrix allocates technical responsibility. It does not authorize plan creation, payment activation or public release.

---

## 1. Current verified Wix state

- Site state: Draft.
- Wix Pricing Plans: installed.
- Wix Pricing Plans readback: `0` operative plans.
- Wix Members Area: not installed.
- Velo: enabled.
- Private collection `AtlasPricingContract`: `13` records at version `0.5.1`.
- Four consumer offers remain `checkoutLegalStatus=NO_GO`.
- Every offer remains `professionalSignoffRequired=true`, `publicAllowed=false` and `purchaseAllowed=false`.
- Family remains separately blocked by identity, age, guardian and household controls.

---

## 2. Responsibility vocabulary

| Class | Meaning |
|---|---|
| `NATIVE_WIX` | Can be represented by a supported Wix business object or member/order feature, subject to configuration and testing. |
| `WIX_PLUS_VELO` | Requires custom Wix Studio UI and/or Velo frontend/backend logic. |
| `EXTERNAL_BACKEND` | Requires controlled non-frontend storage, rules, metering, evidence or reconciliation outside Wix. |
| `MANUAL_ADMIN_PROCESS` | Requires a controlled human decision or exception workflow. |
| `UNSUPPORTED_OR_ALTERNATIVE` | Native route is insufficient or must be replaced by an approved architecture. |

---

## 3. Legal-requirement implementation matrix

| ID | Requirement | Primary class | Wix component | External/control component | Owner | Current state |
|---|---|---|---|---|---|---|
| IMP-001 | Versioned plan/price catalogue | `NATIVE_WIX` + `EXTERNAL_BACKEND` | Private CMS; later Pricing Plans | Canonical offer contract and release flags | Product | `PARTIAL_CMS_ONLY` |
| IMP-002 | Complete pricing-page disclosures | `WIX_PLUS_VELO` | Wix Studio pages/CMS datasets | Canonical disclosure version | Web/legal | `NOT_IMPLEMENTED` |
| IMP-003 | Final order summary immediately before purchase | `WIX_PLUS_VELO` | Custom checkout review component | Immutable snapshot service | Product/legal | `BLOCKED` |
| IMP-004 | Payment-obligation button | `WIX_PLUS_VELO` | Custom final action/wrapper | UI event evidence | Product/legal | `BLOCKED` |
| IMP-005 | Terms acceptance | `WIX_PLUS_VELO` | Unticked checkbox | Consent event store | Legal/product | `BLOCKED` |
| IMP-006 | Early-start choice | `WIX_PLUS_VELO` | Explicit early/delayed activation choice | Immutable consent event | Legal/product | `BLOCKED` |
| IMP-007 | Payment and recurring authorisation | `NATIVE_WIX` | Pricing Plans/payment provider | Payment reconciliation | Finance/product | `NOT_CONFIGURED` |
| IMP-008 | Price/tax preview | `NATIVE_WIX` + `WIX_PLUS_VELO` | Wix price preview; site tax config | Jurisdiction decision service | Tax/product | `BLOCKED` |
| IMP-009 | Contract formation event | `WIX_PLUS_VELO` | Order/payment events | Canonical order snapshot | Product | `BLOCKED` |
| IMP-010 | Durable-medium confirmation | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Wix Automation/email orchestration | Immutable terms/PDF snapshot and delivery log | Legal/ops | `BLOCKED` |
| IMP-011 | Delayed activation option | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Account/order state UI | Entitlement scheduler | Product | `BLOCKED` |
| IMP-012 | Immediate activation | `EXTERNAL_BACKEND` | Velo call after all checks | Entitlement control plane | Product/security | `BLOCKED` |
| IMP-013 | Usage ledger and hard caps | `EXTERNAL_BACKEND` | Account display only | Append-only usage/entitlement ledger | Platform | `NOT_IMPLEMENTED` |
| IMP-014 | Rollover | `EXTERNAL_BACKEND` | Account display | Monthly allowance processor | Platform/finance | `NOT_IMPLEMENTED` |
| IMP-015 | Top-up purchase | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Separate checkout action | Fixed entitlement and tax logic | Product/tax | `BLOCKED` |
| IMP-016 | Member identity | `NATIVE_WIX` + `EXTERNAL_BACKEND` | Members Area | Identity assurance and provider account binding | Security/product | `BLOCKED_APP_ABSENT` |
| IMP-017 | Student verification | `WIX_PLUS_VELO` + `MANUAL_ADMIN_PROCESS` | Secure low-risk verification UI | Verification status/expiry | Ops/privacy | `BLOCKED` |
| IMP-018 | Family payer/member model | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Member portal | Household graph, guardian and subordinate roles | Legal/security | `BLOCKED` |
| IMP-019 | Minor purchase prevention | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Age gate and hidden purchase actions | Verified adult-payer rule | Legal/security | `BLOCKED` |
| IMP-020 | Member cancellation | `NATIVE_WIX` + `WIX_PLUS_VELO` | Pricing Plans member cancellation | Entitlement/accounting orchestration | Product/ops | `BLOCKED_NO_ORDERS` |
| IMP-021 | Email cancellation fallback | `WIX_PLUS_VELO` + `MANUAL_ADMIN_PROCESS` | Form/support route | Case management | Ops | `BLOCKED` |
| IMP-022 | Digital withdrawal route | `WIX_PLUS_VELO` | Portal/form | Withdrawal case and deadline engine | Legal/ops | `BLOCKED` |
| IMP-023 | Six-month reminder | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Automation/email | Reminder scheduler and evidence | Ops/legal | `BLOCKED` |
| IMP-024 | Refund initiation | `NATIVE_WIX` + `MANUAL_ADMIN_PROCESS` | Payment/order admin | Legal reason and approval engine | Finance/ops | `BLOCKED` |
| IMP-025 | Refund completion evidence | `EXTERNAL_BACKEND` | Provider status display | Payment event/reconciliation | Finance | `BLOCKED` |
| IMP-026 | Credit note/MVA correction | `EXTERNAL_BACKEND` + `MANUAL_ADMIN_PROCESS` | Wix invoice reference where suitable | Accounting system and posting rule | Finance/tax | `BLOCKED` |
| IMP-027 | Statutory remedy case | `WIX_PLUS_VELO` + `MANUAL_ADMIN_PROCESS` | Support intake | Incident/remedy decision system | Support/legal | `BLOCKED` |
| IMP-028 | Service-change notice | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Email/account notice | Notice version and delivery evidence | Product/legal | `BLOCKED` |
| IMP-029 | Price-change notice | `WIX_PLUS_VELO` + `EXTERNAL_BACKEND` | Email/account notice | Contract eligibility and cancellation window | Product/finance | `BLOCKED` |
| IMP-030 | Customer-content export | `EXTERNAL_BACKEND` | Request/status UI | Export package and secure download | Privacy/platform | `BLOCKED` |
| IMP-031 | Deletion/retention | `EXTERNAL_BACKEND` + `MANUAL_ADMIN_PROCESS` | Request/status UI | Approved lifecycle engine | Privacy/platform | `BLOCKED` |
| IMP-032 | Bokmål/English parity | `WIX_PLUS_VELO` | Wix Multilingual | Canonical translation diff | Legal/web | `NOT_RUN` |
| IMP-033 | Accessibility | `WIX_PLUS_VELO` | Wix Studio components | Automated/manual WCAG tests | Web/QA | `NOT_RUN` |
| IMP-034 | Audit log | `EXTERNAL_BACKEND` | Admin view only | Tamper-evident event records | Security | `BLOCKED` |
| IMP-035 | End-to-end finance reconciliation | `EXTERNAL_BACKEND` | Wix order/refund export | Accounting/MVA/OSS reconciliation | Finance | `NOT_RUN` |

---

## 4. Required data objects

### 4.1 Wix private CMS

#### `AtlasPricingContract`

Existing controlled offer records. Retain:

- `offerId`;
- `version`;
- prices/allowances;
- commercial status;
- `mvaStatus`;
- `consumerLawStatus`;
- `consumerLawResearchStatus`;
- `checkoutLegalStatus`;
- `professionalSignoffRequired`;
- `publicAllowed`;
- `purchaseAllowed`.

CMS must not become the sole entitlement, consent or financial ledger.

#### Proposed `AtlasLegalCopyVersion`

- `documentType`;
- `locale`;
- `version`;
- `effectiveFrom`;
- `contentHash`;
- `canonicalGitHubRef`;
- `professionalApprovalRef`;
- `publicationStatus`;
- `supersedesVersion`.

No record may become public/effective without approval evidence.

### 4.2 External controlled objects

- `CustomerIdentity`.
- `HouseholdRelationship`.
- `StudentEligibility`.
- `OfferContractVersion`.
- `CheckoutDisclosureSnapshot`.
- `ConsentEvent`.
- `OrderContractSnapshot`.
- `DurableMediumDelivery`.
- `EntitlementAccount`.
- `EntitlementTransaction`.
- `UsageTransaction`.
- `WithdrawalCase`.
- `CancellationCase`.
- `RemedyCase`.
- `RefundDecision`.
- `PaymentRefundEvent`.
- `AccountingCorrection`.
- `DataExportDeletionCase`.
- `ReconciliationRun`.

No secret, provider key or confidential customer content may be stored in Wix frontend code or ordinary public CMS collections.

---

## 5. Event sequence — successful monthly subscription

1. Load approved offer and legal-copy versions.
2. Validate `publicAllowed` and `purchaseAllowed`; both must be true only after a written release decision.
3. Validate supported jurisdiction, customer type and age/eligibility.
4. Render plan details and final summary.
5. Capture terms acceptance.
6. Capture early or delayed commencement choice.
7. Create immutable disclosure/consent snapshot.
8. Request price/tax preview.
9. Display final gross price and recurring billing.
10. Execute payment-obligation action.
11. Receive payment/order result.
12. Create order contract snapshot.
13. Generate and deliver durable-medium confirmation.
14. For early start: create entitlement only after consent and confirmation controls pass.
15. For delayed start: schedule entitlement after withdrawal period.
16. Start usage ledger.
17. Schedule six-month reminder and billing/reconciliation jobs.
18. Reconcile order, payment, entitlement and accounting.

Any failed mandatory step must halt activation and create an operations case.

---

## 6. Acceptance-test suite

### 6.1 Governance and release tests

| Test | Expected result | Evidence |
|---|---|---|
| GOV-001 Query current Pricing Plans before approval | Count remains `0` | API response |
| GOV-002 Read consumer CMS locks | All four: public/purchase false, checkout NO-GO | API response |
| GOV-003 Attempt activation with release false | Hard block | Backend test log |
| GOV-004 Attempt public plan creation by ordinary workflow | Denied by release guard | Audit event |
| GOV-005 Verify no frontend/provider secrets | PASS | Static/config scan |

### 6.2 Pre-contract and button tests

| Test | Expected result |
|---|---|
| CHK-001 Essential information visible immediately before button | PASS desktop/tablet/mobile |
| CHK-002 Price includes MVA and billing interval | PASS |
| CHK-003 Duration, renewal and cancellation visible | PASS |
| CHK-004 Button uses approved payment wording | PASS |
| CHK-005 Replace button with `Fortsett` | Test must FAIL and block release |
| CHK-006 Hidden price behind accordion only | Test must FAIL |
| CHK-007 Terms link unavailable | Purchase blocked |
| CHK-008 Order summary differs from selected plan | Purchase blocked and incident logged |

### 6.3 Consent and commencement tests

| Test | Expected result |
|---|---|
| CON-001 Terms checkbox default | Unticked |
| CON-002 Early-start choice default | Neither option selected |
| CON-003 Marketing checkbox default | Unticked and optional |
| CON-004 Submit without terms acceptance | Blocked |
| CON-005 Submit without early/delayed choice | Blocked |
| CON-006 Early start selected | Exact text/version/timestamp stored |
| CON-007 Delayed start selected | Entitlement scheduled after period |
| CON-008 Consent store unavailable | Payment/activation blocked |
| CON-009 Consent text changed after rendering | Purchase blocked; snapshot mismatch |

### 6.4 Durable-medium tests

| Test | Expected result |
|---|---|
| DUR-001 Confirmation generated before activation | PASS |
| DUR-002 Complete terms and withdrawal form attached/embedded | PASS |
| DUR-003 Mutable links only | FAIL |
| DUR-004 Email delivery fails | Retry and operations alert; no uncontrolled activation |
| DUR-005 Account download matches email snapshot | Hash/version match |
| DUR-006 Bokmål order gets Bokmål pack | PASS |
| DUR-007 English order gets equivalent English pack | PASS |

### 6.5 Withdrawal tests

| Test | Expected result |
|---|---|
| WDR-001 Withdraw before activation | Full refund and no proportional charge |
| WDR-002 Withdraw after valid early start | Approved proportional calculation |
| WDR-003 Missing early-start evidence | Full refund; no deduction |
| WDR-004 Missing statutory information | Full refund and legal incident |
| WDR-005 Digital withdrawal button | Immediate acknowledgement/case ID |
| WDR-006 Email withdrawal without account access | Accepted and timestamped |
| WDR-007 Reason field left blank | Withdrawal still processed |
| WDR-008 Refund deadline monitor | Alert before statutory deadline |

### 6.6 Cancellation and reminder tests

| Test | Expected result |
|---|---|
| CAN-001 Member cancels recurring monthly order | Future renewal stops; confirmation sent |
| CAN-002 Email cancellation | Same legal outcome |
| CAN-003 Account locked | Fallback cancellation remains available |
| CAN-004 Cancellation adds mandatory retention call | FAIL |
| CAN-005 Cancel at next payment date | Access end matches payment date |
| CAN-006 Immediate cancellation where selected/supported | Entitlement and refund rules applied |
| CAN-007 Six-month reminder delivered | Active email/message evidence |
| CAN-008 Portal-only reminder | FAIL |

### 6.7 Remedy/refund tests

| Test | Expected result |
|---|---|
| REF-001 Duplicate charge | Full duplicate refund and correction |
| REF-002 Payment provider approves but refund remains pending | Case stays open |
| REF-003 Internal refund complete without provider confirmation | FAIL |
| REF-004 Refund and chargeback overlap | Prevent double reimbursement |
| REF-005 Defect price reduction | Approved calculation and credit note |
| REF-006 Full statutory termination | Entitlement, payment and data actions agree |
| REF-007 Refund without reason code | FAIL |

### 6.8 Top-up tests

| Test | Expected result |
|---|---|
| TOP-001 Top-up button states quantity and price | PASS |
| TOP-002 Automatic top-up | FAIL; feature prohibited |
| TOP-003 Minor/subordinate account attempts purchase | Blocked |
| TOP-004 Entitlement created before payment confirmation | FAIL |
| TOP-005 Partly used refund before approved model | Manual block/escalation |
| TOP-006 Base subscription cancellation | Approved unused-entitlement treatment applied |

### 6.9 Student, Family and minor tests

| Test | Expected result |
|---|---|
| FAM-001 Purchaser under 18 | Blocked |
| FAM-002 Student status absent/expired | Student plan blocked or controlled transition |
| FAM-003 Family exceeds four named users | Blocked |
| FAM-004 Shared credentials detected | Security workflow, not silent deletion |
| FAM-005 Minor top-up purchase | Blocked |
| FAM-006 Guardian authority absent | Child access blocked |
| FAM-007 Member removed | Notice/export opportunity and scheduled access end |
| FAM-008 Household evidence request | Proportionate and privacy reviewed |

### 6.10 Tax and finance tests

| Test | Expected result |
|---|---|
| TAX-001 Norway B2C approved launch scope | 25% only after professional sign-off |
| TAX-002 Foreign B2B without status evidence | Checkout/quote finalisation blocked |
| TAX-003 EU B2C without OSS/registration route | Checkout blocked |
| TAX-004 Conflicting customer-location evidence | Manual review/block |
| TAX-005 Withdrawal full refund | Correct credit note/MVA adjustment |
| TAX-006 Partial refund | Correct proportional accounting/tax correction |
| TAX-007 Top-up tax point | Uses approved classification only |
| TAX-008 Order/payment/entitlement/accounting totals | Exact reconciliation or exception case |

### 6.11 Localisation and accessibility tests

- complete Bokmål/English semantic parity;
- keyboard-only checkout and cancellation;
- visible focus;
- accessible checkbox labels and error messages;
- screen-reader announcement of price, renewal and errors;
- no colour-only status;
- mobile reflow without hidden statutory information;
- plain-language review;
- legal links and attachments accessible;
- text resizing and contrast checks;
- no pre-ticked control.

---

## 7. Evidence bundle per test run

- environment and release version;
- offer/legal-copy version;
- screenshots/video where appropriate;
- API requests/responses with secrets redacted;
- consent and event records;
- payment-provider sandbox references;
- emails/attachments and delivery status;
- entitlement/usage transactions;
- refund/credit-note records;
- accessibility outputs;
- defects and remediation;
- tester, timestamp and approval state.

Screenshots and logs must not expose keys, tokens, confidential customer data or unrestricted internal endpoints.

---

## 8. Release-decision rule

Research and design completion may change `consumerLawResearchStatus` to `RESEARCH_COMPLETED_DRAFT_PACK_CREATED`. It must not change:

- `consumerLawStatus=PENDING_LEGAL_REVIEW`;
- `checkoutLegalStatus=NO_GO`;
- `professionalSignoffRequired=true`;
- `publicAllowed=false`;
- `purchaseAllowed=false`;
- overall release `NO_GO`.

A later release change requires exact launch-scope test evidence, professional sign-off and explicit written project-owner approval.