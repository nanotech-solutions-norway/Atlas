# Atlas AI Professional Legal and Tax Decision Pack — 03:08, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Commercial contract:** `0.5.1`  
**Prepared for:** Norwegian consumer-law counsel and accountant/tax adviser  
**Current release:** `NO_GO`  
**Document state:** `READY_FOR_PROFESSIONAL_SUBMISSION`  
**Approval state:** `NO_PROFESSIONAL_APPROVAL_RECORDED`

> This pack is a structured request for decisions. It does not supply or simulate professional approval. Every professional answer must identify scope, assumptions, effective date, reviewer and supporting authority.

---

## 1. Canonical review set

Reviewers must use the exact GitHub `main` versions of:

1. `governance/legal/ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md`.
2. `governance/legal/ATLAS_CONSUMER_TERMS_BOKMAL_AND_ENGLISH_DRAFT_0206_26072026.md`.
3. `governance/legal/ATLAS_CHECKOUT_DISCLOSURE_WITHDRAWAL_CANCELLATION_REFUND_OPERATIONS_PACK_0206_26072026.md`.
4. `governance/legal/ATLAS_WIX_VELO_BACKEND_CONSUMER_CHECKOUT_IMPLEMENTATION_AND_TEST_MATRIX_0206_26072026.md`.
5. `governance/tax/ATLAS_MVA_FINALISATION_REGISTER_25072026.md`.
6. `governance/tax/ATLAS_MVA_IMPLEMENTATION_AND_PROFESSIONAL_REVIEW_PACK_0206_26072026.md`.
7. `governance/validation/ATLAS_EXTERNAL_SOURCE_VALIDATION_UPDATE_0308_26072026.md`.
8. Approved commercial price book version `0.5.1`.
9. Current source-authority, decisions and validation registers.

Drive documents are review mirrors. GitHub Markdown is canonical.

---

## 2. Proposed lowest-risk initial consumer scope

### Controlled recommendation — `PENDING_REVIEW`

For professional review and implementation sequencing, the lowest-risk initial Atlas consumer scope is:

- Norway-resident consumers only;
- monthly Student Basic, Student Plus and Everyday Basic only;
- adult contract holder and payer, minimum age 18;
- no Family plan at initial launch;
- no child or subordinate accounts;
- no annual plan;
- no semester plan;
- no paid top-ups or premium-boost purchases;
- no foreign B2C checkout;
- no free trial;
- no automatic overage;
- delayed activation after the withdrawal period as the default option, with early activation available only if the approved consent and proportional-payment model is implemented;
- hard usage caps and no negative balance;
- cancellation effective at the next payment date unless the consumer selects or law requires another outcome.

This recommendation reduces the number of unresolved legal, tax, identity and refund paths. It is not approved until the project owner and professional reviewers record written acceptance.

---

## 3. Consumer-law decision schedule

The legal reviewer should complete every row with one of:

- `APPROVED_AS_DRAFTED`;
- `APPROVED_WITH_CHANGES`;
- `REJECTED`;
- `OUTSIDE_SCOPE`;
- `FURTHER_FACTS_REQUIRED`.

### LEG-DEC-001 — Principal supply classification

**Question:** Are Student Basic, Student Plus and Everyday Basic correctly classified as continuing digital services for Norwegian withdrawal and digital-service law?

**Required answer:**

- governing legal classification;
- whether AI outputs or other components change the principal classification;
- any separately classified component;
- effect on withdrawal, delivery and remedies.

**Current project position:** `PENDING_LEGAL_REVIEW`.

### LEG-DEC-002 — Contract formation point

**Question:** At what exact event should the Atlas consumer contract be considered concluded: payment authorisation, Wix order creation, successful payment, Atlas acceptance or durable confirmation?

**Required answer:**

- exact formation event;
- effect on the 14-day withdrawal period;
- required failure/rejection handling;
- required wording in checkout and confirmation.

### LEG-DEC-003 — Payment-obligation button

**Question:** Approve or amend the exact Bokmål and English final button wording and the essential information that must remain immediately visible.

**Draft wording:**

- Bokmål: `Bestill abonnement med forpliktelse til å betale`.
- English: `Order subscription with obligation to pay`.

**Required answer:** Exact final wording, placement and permitted variants.

### LEG-DEC-004 — Early commencement and delayed activation

**Question:** Approve or amend the separate early-start and delayed-start choice.

**Required answer:**

- exact Bokmål/English text;
- whether a separate acknowledgement of loss after full performance is required for the subscription model;
- whether activation may occur before durable confirmation;
- permitted evidence format;
- treatment where the consumer makes no selection.

### LEG-DEC-005 — Proportional-payment calculation

**Question:** What calculation is lawful and reasonable where a consumer withdraws after valid early commencement?

**Required answer:**

- time-based, usage-based or hybrid formula;
- treatment of included standard units and premium boosts;
- maximum amount;
- market-value check;
- zero-charge conditions;
- examples for withdrawal on days 1, 7 and 14 with different usage levels;
- required consumer disclosure.

### LEG-DEC-006 — Withdrawal notice and form

**Question:** Approve the complete Bokmål and English withdrawal notice, statutory form and electronic/email routes.

**Required answer:**

- contracting party and address fields;
- valid email/contact channel;
- acknowledgement deadline;
- mandatory form content;
- treatment of missing reason;
- treatment where account access is unavailable.

### LEG-DEC-007 — Electronic withdrawal function

**Question:** Confirm the current effective-date status of Law 19.06.2026 no. 34 and advise whether Atlas should implement the future § 20 a function before legal commencement.

**Required answer:**

- law-in-force status on review date;
- required pre-contract disclosure;
- exact button labels;
- continuous availability requirement;
- receipt content and durable-medium design;
- implementation deadline or trigger.

### LEG-DEC-008 — Cancellation and reminders

**Question:** Approve the cancellation model for monthly plans and the six-month continuation reminder.

**Required answer:**

- next-payment-date effect;
- immediate cancellation cases;
- acceptable portal and email routes;
- response/confirmation requirements;
- reminder timing and content;
- failure consequence;
- treatment of failed payments and dormant accounts.

### LEG-DEC-009 — Annual and semester plans

**Question:** Determine whether the 10% annual option and student semester option may be offered as prepaid cancellable terms or binding periods.

**Required answer:**

- lawful term structure;
- total price and benefit disclosure;
- maximum binding period;
- early cancellation/normal compensation;
- renewal and reminder rules;
- withdrawal/refund calculation;
- whether the proposed 10% annual discount is proportionate.

**Current state:** `BLOCKED`.

### LEG-DEC-010 — Top-ups and premium boosts

**Question:** Classify each paid add-on and determine its withdrawal/early-use/refund treatment.

**Required answer:**

- service entitlement, digital content, voucher, prepayment or other category;
- when delivery begins;
- whether separate early-use consent is required;
- unused/part-used refund rule;
- expiry and base-subscription cancellation effect;
- treatment of promotional and rollover units.

**Current state:** `BLOCKED`.

### LEG-DEC-011 — Student eligibility

**Question:** Approve eligibility evidence, review frequency, failed-verification treatment and transition from Student to Everyday plans.

**Required answer:**

- accepted evidence;
- minimum data collection;
- retention period;
- renewal/reverification frequency;
- grace period and notice;
- price-change or plan-transition rules.

### LEG-DEC-012 — Family and minors

**Question:** Approve or reject the adult-payer/named-household-user model and define whether minor access may be supported.

**Required answer:**

- contract holder and payer requirements;
- household definition;
- age and guardian verification;
- child-data lawful basis and privacy defaults;
- subordinate-account rights;
- removal, export and deletion;
- marketing limitations;
- whether Family must remain adult-only.

**Current state:** `BLOCKED_FAMILY_CONTROLS`.

### LEG-DEC-013 — Service, provider and model changes

**Question:** Approve the provider/model substitution, functionality-change and price-change clauses.

**Required answer:**

- objective permitted reasons;
- conformity threshold;
- notice form and lead time;
- cancellation/termination rights;
- changes requiring new consent or contract;
- treatment during binding terms.

### LEG-DEC-014 — Remedies and complaint handling

**Question:** Approve the statutory remedy matrix, support escalation and complaint/ADR wording.

**Required answer:**

- delivery and conformity standards;
- cure/replacement sequence;
- price reduction and termination calculation;
- damages wording;
- response deadlines;
- correct Norwegian complaint and ADR body/contact information.

### LEG-DEC-015 — Customer content after termination

**Question:** Approve the export, retrieval, deletion and lawful-retention design for customer-created content and personal data.

**Required answer:**

- content categories;
- export format and period;
- exceptions;
- deletion/retention schedule;
- account access after termination;
- security and identity verification.

### LEG-DEC-016 — Accessibility and language parity

**Question:** Confirm the applicable private-sector legal accessibility baseline and whether Atlas should adopt WCAG 2.1 AA as a stronger internal standard.

**Required answer:**

- legal minimum;
- applicable exceptions;
- evidence/documentation standard;
- checkout-specific requirements;
- status of Bokmål/English legal parity.

---

## 4. MVA/accounting decision schedule

The accountant/tax adviser should complete all applicable `MVA-001` through `MVA-020` entries and provide exact configuration outputs.

### TAX-DEC-001 — Contracting and invoice entity

Provide:

- legal entity name;
- organisation number;
- MVA registration status and effective date;
- registered address;
- invoice identity;
- accounting system/entity;
- bank/payment settlement entity.

No placeholder may be replaced before this is confirmed.

### TAX-DEC-002 — Offer and bundle classification

For every consumer and business offer, identify:

- actual supply type;
- principal and ancillary components;
- whether setup/support/usage/add-ons are one or separate supplies;
- Norwegian rate;
- place-of-supply rule;
- tax point;
- revenue recognition/periodisation method.

### TAX-DEC-003 — Norwegian consumer subscriptions

Confirm:

- 25% treatment;
- gross price presentation;
- invoice/receipt requirement;
- monthly renewal tax point;
- early-start withdrawal credit-note treatment;
- full and partial refund correction.

### TAX-DEC-004 — Student, annual and semester options

Confirm:

- no education exemption merely because students are the target market;
- advance payment and periodisation;
- treatment of cancellation in a fixed or binding period;
- credit-note and revenue adjustment.

### TAX-DEC-005 — Top-ups, boosts and credits

Classify and provide:

- voucher/prepayment/service-entitlement analysis;
- tax point;
- unused and partly used refund treatment;
- promotional and free-credit treatment;
- expiry and breakage treatment;
- accounting accounts.

### TAX-DEC-006 — Foreign B2B

Provide:

- customer-status evidence;
- establishment/location evidence;
- invoice wording;
- reverse-charge/export treatment;
- failed-evidence rule;
- document retention.

### TAX-DEC-007 — EU B2C and non-Union OSS

Provide:

- supported countries;
- Member State of identification;
- registration owner and status;
- VAT-rate source and update frequency;
- two-item location-evidence rule and conflict handling;
- invoice/receipt requirements;
- quarterly filing/payment owner;
- ten-year record retention;
- treatment of 2027 OSS/ViDA changes.

### TAX-DEC-008 — Foreign provider purchases

Provide vendor-by-vendor treatment for:

- AI/API providers;
- cloud/hosting;
- software licences;
- payment processing;
- analytics and support tools;
- legal, accounting and consultancy services.

Define reverse-charge accounts, deduction treatment and evidence.

### TAX-DEC-009 — Accounting-code map

Provide exact:

- revenue accounts by offer group;
- output MVA codes;
- export/reverse-charge codes;
- imported-service codes;
- deferred revenue/prepayment accounts;
- refund/credit-note accounts;
- payment clearing accounts;
- chargeback accounts;
- OSS liability/payment accounts.

### TAX-DEC-010 — Document and reconciliation approval

Approve examples for:

- Norwegian B2C monthly subscription;
- Norwegian B2B project/setup;
- foreign B2B service;
- EU B2C OSS service;
- full withdrawal refund;
- partial early-start refund;
- statutory price reduction;
- duplicate charge;
- chargeback;
- top-up refund if later approved.

Define Wix-order/payment/refund, entitlement, invoice/credit-note, Norwegian MVA return and OSS reconciliation.

---

## 5. Project-owner launch-scope decisions

After professional advice, the project owner must explicitly approve or reject:

| Decision | Options | Current state |
|---|---|---|
| Initial geography | Norway only / selected foreign markets | `PENDING_REVIEW` |
| Initial consumer plans | Monthly Student/Everyday only / broader | `PENDING_REVIEW` |
| Family | Exclude / adult-only / minors with controls | `BLOCKED` |
| Annual | Exclude / prepaid / binding | `BLOCKED` |
| Semester | Exclude / prepaid / binding | `BLOCKED` |
| Top-ups | Exclude / fixed entitlement / other | `BLOCKED` |
| Early commencement | Delayed only / consumer choice | `PENDING_LEGAL_REVIEW` |
| Accessibility target | Legal minimum / WCAG 2.1 AA internal target | `PENDING_REVIEW` |
| Electronic withdrawal function | Build now / activate at commencement / later | `PENDING_REVIEW` |
| Test environment | Approved non-public published test route / alternative | `PENDING_REVIEW` |

No default option is deemed approved by this pack.

---

## 6. Required professional deliverables

### Lawyer deliverable

A signed, dated memorandum containing:

- reviewer identity and qualifications;
- scope and exclusions;
- law/effective date;
- decision for LEG-DEC-001 through LEG-DEC-016;
- marked-up Bokmål and English terms/copy;
- final withdrawal form and complaint details;
- unresolved risks;
- conditions for implementation and release;
- explicit statement that approval covers the exact identified versions.

### Accountant/tax-adviser deliverable

A signed, dated memorandum containing:

- reviewer identity and qualifications;
- entity and MVA profile;
- decision for TAX-DEC-001 through TAX-DEC-010 and MVA-001 through MVA-020;
- offer/jurisdiction matrix;
- chart-of-accounts and tax-code map;
- invoice and credit-note examples;
- OSS and reverse-charge operating procedures;
- reconciliation design;
- unresolved risks;
- explicit statement that approval covers the exact identified versions.

---

## 7. Intake and governance procedure

1. Store professional deliverables privately in the controlled Drive legal/tax folder.
2. Store a sanitized approval record in GitHub; do not commit confidential advice, personal data or commercial account information without explicit approval.
3. Record document title, reviewer, review date, covered versions and decision status.
4. Classify each decision independently.
5. Do not convert a conditional or limited opinion into general approval.
6. Update consumer terms and MVA packs on a branch.
7. Perform Bokmål/English parity and source review.
8. Implement only approved scope.
9. Run the complete acceptance suite.
10. Require explicit written project-owner release approval.

---

## 8. Current outcome

This professional decision pack is complete and ready for submission. The underlying professional decisions are absent.

- Legal approval: `ABSENT`.
- Tax/accounting approval: `ABSENT`.
- Approved initial launch scope: `ABSENT`.
- Consumer checkout: `NO_GO`.
- Public release: `NO_GO`.