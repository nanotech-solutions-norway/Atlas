# Atlas AI Fail-Closed Consumer Checkout Implementation Backlog — 03:08, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Contract version:** `0.5.1`  
**Implementation mode:** `NON_PUBLIC_FOUNDATION_ONLY`  
**Release:** `NO_GO`  
**Checkout:** `NO_GO`

> This backlog authorizes only non-public design, schema, mock, test and evidence work. It does not authorize Wix Pricing Plan creation, live payment configuration, public checkout, provider provisioning, customer activation or production release.

---

## 1. Governing implementation rules

1. Every customer-facing action must fail closed when an approval, version, jurisdiction, identity, consent, tax, payment, durable-medium or entitlement dependency is missing.
2. `publicAllowed=false` or `purchaseAllowed=false` must always block plan discovery and ordering.
3. `checkoutLegalStatus` other than an approved release value must block order creation.
4. `professionalSignoffRequired=true` without approved legal and tax references must block order creation.
5. Wix/CMS is not the sole consent, entitlement, financial or audit ledger.
6. No provider key, payment secret or privileged endpoint may appear in frontend code, CMS, logs, screenshots or public documentation.
7. No confidential customer material may be accepted through ordinary public Wix forms.
8. Every implemented control requires a negative-path test.
9. Research/draft status must never be mapped to purchase/public approval.
10. Overall release remains `NO_GO` until explicit written project-owner approval.

---

## 2. Workstream sequence

### WS-01 — Professional decision intake

**Objective:** Obtain version-specific legal and tax decisions.

**Inputs:**

- `ATLAS_PROFESSIONAL_LEGAL_TAX_DECISION_PACK_0308_26072026.md`;
- exact legal and MVA canonical files;
- approved price book `0.5.1`.

**Outputs:**

- sanitized legal approval record;
- sanitized tax/accounting approval record;
- approved launch-scope decision;
- marked-up legal copy;
- offer/jurisdiction/tax matrix;
- accounting and document examples.

**State:** `READY_FOR_EXTERNAL_REVIEW`.

**Blocking:** Does not block the schema/test foundation below; blocks any live checkout configuration.

### WS-02 — Version and release registry

**Objective:** Create one immutable release-contract record per candidate launch scope.

**Required fields:**

- release candidate ID;
- commercial contract version;
- offer IDs;
- supported jurisdictions;
- supported customer types;
- legal-copy versions and hashes;
- legal approval reference;
- tax approval reference;
- privacy/security/accessibility approval references;
- payment-provider configuration version;
- entitlement/runtime version;
- acceptance-test run ID;
- `publicAllowed`;
- `purchaseAllowed`;
- `releaseApproved`;
- approver and decision timestamp.

**Acceptance:** All approval booleans default false and cannot be inferred from document existence.

**State:** `SPECIFICATION_READY`.

### WS-03 — Checkout release-gate service

**Objective:** Evaluate whether an offer may be rendered, ordered, paid and activated.

**Required decisions:**

1. `DISCOVER` — may the offer be displayed publicly?
2. `QUOTE` — may price/tax be previewed?
3. `ORDER` — may a paid order be created?
4. `ACTIVATE` — may entitlement start?
5. `RENEW` — may recurring payment and entitlement continue?
6. `TOP_UP` — may an add-on be purchased?
7. `REFUND` — may an approved refund workflow execute?

**Fail-closed rule:** Any missing or unknown dependency returns `DENY` with a stable reason code.

**Minimum reason codes:**

- `RELEASE_NOT_APPROVED`;
- `PUBLIC_NOT_ALLOWED`;
- `PURCHASE_NOT_ALLOWED`;
- `LEGAL_APPROVAL_MISSING`;
- `TAX_APPROVAL_MISSING`;
- `UNSUPPORTED_JURISDICTION`;
- `IDENTITY_REQUIRED`;
- `AGE_OR_GUARDIAN_BLOCK`;
- `STUDENT_ELIGIBILITY_MISSING`;
- `FAMILY_CONTROLS_MISSING`;
- `LEGAL_COPY_VERSION_MISSING`;
- `CONSENT_STORE_UNAVAILABLE`;
- `TAX_PREVIEW_UNAVAILABLE`;
- `PAYMENT_CONFIGURATION_UNAVAILABLE`;
- `DURABLE_MEDIUM_UNAVAILABLE`;
- `ENTITLEMENT_CONTROL_UNAVAILABLE`;
- `RECONCILIATION_UNAVAILABLE`;
- `TOP_UP_NOT_APPROVED`;
- `ANNUAL_OR_SEMESTER_NOT_APPROVED`.

**State:** `CONTRACT_SCHEMA_CREATED / SERVICE_NOT_IMPLEMENTED`.

### WS-04 — Legal-copy version registry

**Objective:** Bind rendered customer copy to exact approved content.

**Data objects:**

- document type;
- locale;
- semantic version;
- content hash;
- canonical GitHub reference;
- approval reference;
- effective-from and supersession state;
- publication state.

**Controls:**

- Bokmål and English must be paired;
- no orphan translation may become effective;
- draft copy cannot be published;
- checkout must store the exact rendered copy hash.

**State:** `DESIGN_COMPLETE / CMS_AND_BACKEND_NOT_IMPLEMENTED`.

### WS-05 — Consent and commencement event store

**Objective:** Store exact affirmative actions required for contract and early/delayed commencement.

**Separate events:**

- terms acceptance;
- recurring-payment acknowledgement;
- early-start request or delayed-start selection;
- proportional-payment acknowledgement where approved;
- optional marketing consent;
- cookie/tracking consent where applicable.

**Controls:**

- no preselected values;
- exact text/version/hash;
- locale;
- timestamp;
- authenticated identity;
- session/order correlation;
- withdrawal/revocation event where applicable;
- write-once event history.

**State:** `CONTRACT_SCHEMA_CREATED / STORE_NOT_IMPLEMENTED`.

### WS-06 — Order and durable-medium snapshot

**Objective:** Create an immutable contract snapshot and deliver it before activation.

**Snapshot must contain:**

- parties;
- selected offer and allowances;
- total price including MVA;
- billing interval and next payment;
- duration, renewal and cancellation;
- legal-copy hashes;
- withdrawal notice and form;
- early/delayed commencement choice;
- order/payment identifiers;
- creation timestamp;
- document hash;
- delivery attempts and result.

**Fail-closed rule:** Entitlement cannot activate until a valid snapshot exists and durable delivery has reached the approved state.

**State:** `DESIGN_COMPLETE / GENERATOR_NOT_IMPLEMENTED`.

### WS-07 — Member identity and eligibility

**Objective:** Establish member identity without creating unsupported child/Family flows.

**Initial recommended scope:**

- adult account holder only;
- no Family/minor subordinate accounts;
- student eligibility as a separate expiring status;
- no confidential-document upload through an ordinary public form.

**Controls:**

- member ID bound to internal customer identity;
- age/contract-holder gate;
- student verification status and expiry;
- account recovery and cancellation fallback;
- role and access revocation;
- duplicate identity handling.

**State:** `BLOCKED_MEMBERS_AREA_ABSENT / DESIGN_READY`.

### WS-08 — Entitlement and usage ledger

**Objective:** Enforce allowances and hard caps externally to Wix.

**Required transaction types:**

- monthly allowance grant;
- usage debit;
- rejected usage due to cap;
- approved rollover grant/expiry;
- approved top-up grant/usage/expiry;
- refund reversal;
- cancellation/withdrawal suspension;
- manual correction with reason and approval.

**Controls:**

- append-only transactions;
- idempotency keys;
- no negative balance;
- no silent chargeable overage;
- exact reconciliation to order and plan version;
- Family/shared balance disabled until approved.

**State:** `NOT_IMPLEMENTED`.

### WS-09 — Cancellation and withdrawal state machine

**Objective:** Separate request receipt, legal decision, Wix cancellation, entitlement end, refund and accounting completion.

**Minimum states:**

- `REQUEST_RECEIVED`;
- `IDENTITY_VERIFIED`;
- `LEGAL_REVIEW_REQUIRED`;
- `APPROVED_NO_REFUND`;
- `APPROVED_FULL_REFUND`;
- `APPROVED_PARTIAL_REFUND`;
- `WIX_CANCELLATION_PENDING`;
- `WIX_CANCELED`;
- `PAYMENT_REFUND_PENDING`;
- `PAYMENT_REFUNDED`;
- `ENTITLEMENT_UPDATED`;
- `ACCOUNTING_CORRECTION_PENDING`;
- `RECONCILED`;
- `CLOSED`;
- `EXCEPTION`.

**Closure rule:** `CLOSED` is allowed only after the order, payment, entitlement and accounting outcomes agree.

**State:** `CONTRACT_SCHEMA_CREATED / ORCHESTRATION_NOT_IMPLEMENTED`.

### WS-10 — MVA decision and reconciliation service

**Objective:** Resolve tax only from approved transaction rules.

**Inputs:**

- supplier legal entity;
- offer/supply classification;
- customer type;
- customer establishment/location evidence;
- supported-country record;
- approved MVA/OSS rule version;
- billing/refund event.

**Fail-closed cases:**

- unknown customer type;
- missing foreign B2B evidence;
- conflicting B2C location evidence;
- EU B2C without approved OSS/local registration;
- top-up without approved classification;
- unavailable rate source;
- Wix/site configuration mismatch.

**State:** `BLOCKED_PROFESSIONAL_CONFIGURATION`.

### WS-11 — Accessibility and bilingual validation harness

**Objective:** Prove the complete consumer journey is usable and semantically equivalent.

**Legal baseline:** Norwegian private-sector WCAG 2.0 A/AA with applicable exceptions, subject to legal confirmation.

**Recommended internal target:** WCAG 2.1 AA, `PENDING_REVIEW`.

**Required tests:**

- keyboard only;
- visible focus;
- programmatic labels/instructions;
- accessible error summary and field errors;
- screen-reader reading order;
- price, renewal and payment-obligation announcement;
- checkbox/radio state;
- contrast and non-colour status;
- text resize and mobile reflow;
- accessible legal documents;
- Bokmål/English semantic diff;
- no hidden statutory information at any breakpoint.

**State:** `TEST_PLAN_READY / UI_NOT_IMPLEMENTED`.

### WS-12 — Controlled published test environment

**Objective:** Enable member-order API testing without public commercial availability.

**Required approval before creation:**

- architecture/security owner;
- legal owner;
- payment/finance owner;
- release owner.

**Required safeguards:**

- no discoverable public purchase route;
- sandbox/test payment only;
- allowlisted testers;
- test offers distinct from approved commercial offers;
- no provider production credentials;
- no production entitlement;
- explicit test-data retention and deletion;
- complete audit evidence.

**State:** `PENDING_REVIEW`.

---

## 3. Immediate completed foundation in this workstream

The following non-public artifacts are created with this backlog:

- `contracts/atlas-consumer-checkout-gate.schema.json`;
- `contracts/atlas-consent-event.schema.json`;
- `contracts/atlas-cancellation-refund-state.schema.json`;
- `test-vectors/consumer-checkout-negative-paths.v0.1.json`.

These artifacts define fail-closed interfaces only. They do not create an operational endpoint or public capability.

---

## 4. Definition of ready for controlled build

A work item is ready for build only when:

- source requirement is verified;
- owner is assigned;
- approval dependency is explicit;
- data classification is known;
- secrets and customer-data boundaries are defined;
- negative-path tests exist;
- release flags remain false;
- evidence destination is defined.

---

## 5. Definition of done

A work item is not done because code or configuration exists. Done requires:

- implemented in the correct environment;
- unit/contract/negative-path tests passed;
- security/privacy/accessibility review completed where applicable;
- evidence stored with secrets redacted;
- canonical register updated;
- Drive mirror updated where required;
- no contradictory stale state;
- owner approval recorded.

---

## 6. Current implementation decision

- Professional decision intake: `READY`.
- Fail-closed contracts/test vectors: `CREATED`.
- Runtime implementation: `NOT_STARTED`.
- Wix Members Area: `NOT_INSTALLED`.
- Wix Pricing Plans: `COUNT_0`.
- Live payment: `NOT_CONFIGURED`.
- Consumer checkout: `NO_GO`.
- Public release: `NO_GO`.