# Atlas AI Non-Public Release Registry, Test Infrastructure and Hidden Plan Workflow

**Version:** `0.6.1-DRAFT`  
**Prepared:** 26.07.2026  
**Plan sponsor:** Ruben A. Meyer  
**Sponsor role:** CEO / daglig leder and chair of the board, NanoTech Solutions Norway AS  
**Contracting entity:** NanoTech Solutions Norway AS, org. no. `925 367 869 MVA`  
**Atlas status:** Internal department/business line; not a separate legal entity  
**Release:** `NO_GO`

> Planning and operator-control document only. It authorises no public plan, real-money charge, production entitlement, provider credential, public write endpoint or release.

## 1. Operator prompt convention

- `PREFILLED_VERIFIED`: verified company or canonical fact.
- `PENDING_OWNER_INPUT`: Ruben A. Meyer or a named owner must decide/sign.
- `PENDING_PROFESSIONAL_REVIEW`: lawyer or accountant/tax adviser must decide.
- `PENDING_IMPLEMENTATION_EVIDENCE`: release operator must add exact run IDs, screenshots, API readback and test results.
- `HOLD/NO_GO`: no subsequent phase may proceed beyond its authorised non-public scope.

## 2. Plan sponsor and governance

| Field | Value/input |
|---|---|
| Plan sponsor | Ruben A. Meyer |
| Sponsor role | CEO / daglig leder and chair of the board |
| Company | NanoTech Solutions Norway AS |
| Organisation/MVA identifier | `925 367 869` / `NO925367869MVA` |
| Project | Atlas AI, internal department/business line |
| Student minimum age | 16 |
| Current release | `NO_GO` |
| Architecture/security owner | `[[PENDING_OWNER_INPUT — name and approval reference]]` |
| Legal owner | `[[PENDING_OWNER_INPUT — signed counsel memorandum reference]]` |
| Finance/payment owner | `[[PENDING_OWNER_INPUT — signed tax/accounting memorandum reference]]` |
| Release operator | `[[PENDING_OWNER_INPUT — person implementing and collecting evidence]]` |
| Test-data owner | `[[PENDING_OWNER_INPUT — retention/deletion owner]]` |

## 3. Entry criteria

No controlled hidden-plan work may begin until:

1. a signed legal memorandum covers Student minimum age 16, users aged 16–17 and exact legal-copy versions;
2. a signed MVA/accounting memorandum provides exact Wix/payment/accounting configuration;
3. Ruben A. Meyer signs the owner launch-scope decision;
4. architecture/security, legal, finance/payment and release owners approve the controlled test environment;
5. all excluded capabilities have explicit fail-closed deny rules;
6. the exact release candidate is created with all approval booleans false.

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNERS: APPROVE, HOLD OR REJECT ENTRY]]`

## 4. Phase 1 — Immutable non-public release registry

### Actions

- create a private immutable release-candidate ID;
- bind NanoTech Solutions Norway AS legal identity and Atlas internal-business-line relationship;
- bind offer IDs, Student age 16+, supported jurisdiction/customer types, prices and allowances;
- bind legal-copy hashes and legal, tax, privacy, security and accessibility approval references;
- bind Wix app/configuration, payment, entitlement/runtime and test-run versions;
- default `publicAllowed=false`, `purchaseAllowed=false` and `releaseApproved=false`;
- require named approver and timestamp for every state transition.

### Evidence prompt

`[[PENDING_IMPLEMENTATION_EVIDENCE — RELEASE OPERATOR: release-record export, access-control result, immutable ID, version/hash references and approver.]]`

### Phase decision

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNER: PASS, HOLD OR REJECT PHASE 1.]]`

## 5. Phase 2 — Controlled test infrastructure

### Actions

- create a non-discoverable, allowlisted Wix test route;
- use sandbox/test payment only and test offers distinct from commercial offers;
- use no production provider credentials or production entitlements;
- create private CMS indexes for release candidates, offer versions, legal-copy versions and sanitized evidence;
- keep authoritative consent, payment, entitlement, usage, refund and accounting ledgers outside Wix where required;
- implement stable fail-closed reason codes and negative-path tests;
- define test-data retention, deletion and incident handling.

### Evidence prompt

`[[PENDING_IMPLEMENTATION_EVIDENCE — RELEASE OPERATOR: route controls, allowlist, sandbox proof, CMS schema/readback, retention rule and negative-test run IDs.]]`

### Phase decision

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNER: PASS, HOLD OR REJECT PHASE 2.]]`

## 6. Phase 3 — Professional configuration decisions

### Legal translation

- exact Bokmål/English payment-obligation text and immediately visible information;
- contract-formation event and durable confirmation;
- age 16–17 payer/guardian/identity/privacy controls;
- early/delayed commencement and proportional-payment formula;
- cancellation, withdrawal, refund and complaint workflow;
- exact approved legal-copy versions/hashes.

### Tax/accounting translation

- exact gross price/MVA configuration;
- settlement entity and payment-provider configuration;
- invoice/receipt and credit-note formats;
- tax point, periodisation and account/MVA codes;
- foreign provider reverse charge;
- order/payment/refund, entitlement, accounting and MVA reconciliation.

Any configuration that lacks professional evidence or conflicts with platform limits must be rejected.

### Evidence prompt

`[[PENDING_IMPLEMENTATION_EVIDENCE — RELEASE OPERATOR: configuration-to-memorandum traceability matrix and named professional/owner acceptance.]]`

### Phase decision

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNER: PASS, HOLD OR REJECT PHASE 3.]]`

## 7. Phase 4 — Hidden Wix test plans

### Actions

- create only the approved monthly Student Basic, Student Plus and Everyday Basic test plans;
- keep plan visibility hidden/private and prevent public discovery or purchase;
- record Wix plan ID, revision, MVA-inclusive price, recurrence, benefits, cancellation rules and linked offer version;
- validate Members Area and My Subscriptions cancellation access;
- do not create Family, annual, semester, top-up or foreign-market plans;
- capture API readback and dashboard screenshots.

### Evidence prompt

`[[PENDING_IMPLEMENTATION_EVIDENCE — RELEASE OPERATOR: hidden-plan IDs, revisions, screenshots, API readback, Members Area test and public-denial result.]]`

### Phase decision

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNER: PASS, HOLD OR REJECT PHASE 4.]]`

## 8. Phase 5 — Acceptance testing

Required scenarios include:

- eligible adult purchase;
- counsel-approved Student user aged 16–17;
- under-16 denial;
- missing payer/guardian/eligibility control denial;
- unsupported jurisdiction denial;
- missing legal/tax/owner approval denial;
- legal-copy/version mismatch denial;
- payment success/failure and duplicate-event idempotency;
- durable-confirmation failure blocks activation;
- hard caps, no overage, no negative balance and concurrency-safe reset;
- cancellation, withdrawal, full/partial refund, credit note and accounting reconciliation;
- Bokmål/English parity, keyboard, screen-reader, focus, errors and responsive layout;
- provider outage, rollback, monitoring and incident response.

### Evidence prompt

`[[PENDING_IMPLEMENTATION_EVIDENCE — RELEASE OPERATOR: complete acceptance run, failures/repairs, final rerun, evidence bundle and named approvers.]]`

### Phase decision

`[[PENDING_OWNER_INPUT — RUBEN/NAMED OWNER: PASS, HOLD OR REJECT PHASE 5.]]`

## 9. Exit criteria

| Deliverable | Required evidence | State |
|---|---|---|
| Release registry | immutable record and access-control test | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Hidden Wix plans | plan/API readback and screenshots | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Payment configuration | sandbox transactions and refunds | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Legal controls | copy hashes, consent and durable confirmation | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Tax/accounting | invoices, credit notes and reconciliation | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Entitlement/usage | ledger, cap/reset and idempotency | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Accessibility/language | Bokmål/English and accessibility report | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Security/privacy | access, secret, retention, recovery and incident evidence | `[[PENDING_IMPLEMENTATION_EVIDENCE]]` |
| Owner release | signed exact release-candidate decision | `[[PENDING_OWNER_INPUT]]` |

## 10. Prohibited actions before final GO

- no public Pricing Plan visibility or public purchase route;
- no real-money charge or production payment credential;
- no production AI-provider credential or automatic customer provisioning;
- no public write endpoint or frontend secret;
- no Family, under-16, annual, semester, top-up, foreign B2C or Managed Secure activation;
- no release-boolean change without the exact signed owner decision and complete evidence.

## 11. Management authorisation of the plan

| Field | Value/input |
|---|---|
| Authorising company | NanoTech Solutions Norway AS |
| Authorising signatory | Ruben A. Meyer |
| Role | CEO / daglig leder and chair of the board |
| Authorisation scope | Controlled preparation only; no execution beyond the stated entry gates. |
| Signature | `[[PENDING_OWNER_INPUT — RUBEN A. MEYER SIGNATURE]]` |
| Date | `[[PENDING_OWNER_INPUT]]` |

Signing this plan does not change `NO_GO` or authorise public checkout.
