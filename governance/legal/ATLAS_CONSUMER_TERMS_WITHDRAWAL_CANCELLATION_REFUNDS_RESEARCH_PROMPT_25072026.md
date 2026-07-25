# DEEP RESEARCH PROMPT

## Atlas AI Consumer Terms, Withdrawal, Cancellation, Refunds, Digital-Service Commencement and Checkout Compliance

### Mode

- **MODE:** Deep Research
- **AS-OF DATE:** 25 July 2026
- **TIME ZONE:** Europe/Oslo
- **PRIMARY JURISDICTION:** Norway
- **SECONDARY JURISDICTIONS:** EU/EEA where relevant to Norwegian cross-border consumer sales
- **REPORT LANGUAGE:** English
- **IMPLEMENTATION LANGUAGES:** Norwegian Bokmål and English
- **OUTPUT STANDARD:** Decision-grade, source-cited, implementation-ready and suitable for legal review
- **PROJECT:** Atlas Website / Atlas AI
- **CURRENT RELEASE STATUS:** `NO_GO`

---

## 1. Research mandate

Prepare a comprehensive legal, commercial and technical implementation report covering the complete consumer-contract lifecycle for Atlas AI.

Determine how Atlas AI should lawfully structure, present, record and administer:

1. Consumer terms and conditions.
2. Pre-contract information.
3. Electronic checkout.
4. Express acknowledgement of the payment obligation.
5. Immediate commencement of a digital service.
6. Statutory withdrawal rights.
7. Loss or limitation of withdrawal rights.
8. Cancellation and ordinary termination.
9. Refunds, partial refunds and statutory remedies.
10. Automatic renewal and recurring billing.
11. Annual, semester and monthly subscriptions.
12. Subscription pauses.
13. Top-ups, premium boosts and rollover.
14. Changes to prices, allowances, provider access and service functionality.
15. Confirmation of the agreement on a durable medium.
16. Consumer data retrieval, deletion and service-access termination.
17. Complaint, correction, price-reduction and contract-termination procedures.
18. Evidence that the complete process complies with Norwegian consumer law.

Do not assume that an Atlas AI subscription is automatically “digital content” or automatically loses its withdrawal right when access is activated. Determine the legally correct classification and procedure for every relevant component.

---

## 2. Atlas AI commercial baseline

### Consumer subscriptions

| Offer | Price including Norwegian MVA | Users | Monthly allowance |
|---|---:|---:|---|
| Student Basic | NOK 129 | 1 named user | 300 standard units and 6 premium boosts |
| Student Plus | NOK 169 | 1 named user | 500 standard units and 12 premium boosts |
| Everyday Basic | NOK 159 | 1 named user | 400 standard units and 8 premium boosts |
| Family | NOK 399 | Up to 4 named household users | 1,000 shared standard units and 20 premium boosts |

### Approved commercial controls

- Atlas-managed API delivery.
- No resale or sharing of provider retail accounts.
- No unlimited-use promise.
- Hard usage caps.
- No negative usage balance.
- No silent chargeable overage.
- Standard top-up: NOK 39 including MVA for 250 units.
- Premium top-up: NOK 59 including MVA for five boosts.
- Family standard top-up: NOK 79 including MVA for 500 units.
- Family premium top-up: NOK 99 including MVA for ten boosts.
- Annual subscription discount: 10%.
- Student semester option.
- One permitted student summer pause.
- Maximum 25% of unused standard allowance may roll over for one month.
- Premium boosts do not roll over.
- Family is limited to named household users.

These commercial decisions are approved for controlled project implementation but are not publicly activated.

---

## 3. Current technical and release state

Apply these implementation facts:

- The website is being built in Wix Studio.
- Wix Pricing Plans is installed, but there are currently no active Pricing Plans.
- Wix Members Area is not installed.
- A private admin-only `AtlasPricingContract` CMS collection contains 13 versioned offer records.
- Current contract version: `0.5.1`.
- Every offer has `publicAllowed=false`.
- Every offer has `purchaseAllowed=false`.
- Checkout is disabled.
- Top-ups are not technically enabled.
- Provider routing is not in production.
- The entitlement and usage ledger is not implemented.
- Managed Secure remains qualification and architecture-review only.
- No conclusion in the research may authorize public activation.

---

## 4. Source hierarchy

Use primary and authoritative sources wherever available, in this order:

1. Current consolidated Norwegian legislation in Lovdata.
2. Norwegian preparatory works, regulations and government publications.
3. Forbrukertilsynet guidance, enforcement decisions and official templates.
4. Norwegian Consumer Council material where authoritative and directly relevant.
5. Norwegian Tax Administration material for price and MVA presentation.
6. EEA-incorporated EU directives and official European Commission guidance.
7. Relevant EFTA Court, CJEU and Norwegian court decisions.
8. Official Wix documentation for implementation capability only.
9. Secondary legal commentary only when primary sources do not resolve a material issue.

For every material conclusion:

- cite the exact source;
- identify the statutory section or official guidance passage;
- state the effective date;
- distinguish current law from enacted but not-yet-effective changes;
- identify uncertainty, conflicting interpretation or required professional judgement;
- state when Norwegian legal counsel is required.

Verify whether any Norwegian amendments enacted during 2026 were in force on 25 July 2026 before applying them.

---

## 5. Mandatory legal sources to analyse

At minimum, analyse the current versions of:

- Angrerettloven, including sections 8, 14–19, 21–27 and provisions governing digital content and digital services.
- Digitalytelsesloven, including delivery, conformity, remedies, updates, modification of continuing services and consumer-created content.
- Ehandelsloven.
- Markedsføringsloven and relevant regulations on price information, recurring agreements and unfair commercial practices.
- Avtaleloven and mandatory consumer-contract principles.
- Relevant personal-data rules where cancellation, withdrawal, data return, deletion and audit logging intersect with GDPR obligations.
- Relevant payment-services and card/recurring-payment rules where applicable.

The research must specifically confirm the current effect of the following Angrerettloven requirements:

- Before an electronic order that creates a payment obligation, the consumer must receive the required information clearly and prominently immediately before ordering.
- The consumer must expressly acknowledge that the order creates an obligation to pay.
- A button or equivalent function must use “bestilling med forpliktelse til å betale” or equivalent unambiguous wording.
- Failure to satisfy the payment-button requirement may mean the consumer is not bound.
- A paid service starting during the withdrawal period requires an express request for early commencement.
- The consumer must acknowledge when the withdrawal right will be lost after full performance of a service.
- Separate conditions apply to digital content not supplied on a physical medium.
- Confirmation of the contract and recorded acknowledgements must be provided on a durable medium.

---

## 6. Legal-classification analysis

Determine separately for each Atlas consumer offer and component whether it is:

- digital content;
- a digital service;
- an electronically supplied service;
- an ordinary service delivered remotely;
- a continuing service agreement;
- a combined agreement containing digital and non-digital components;
- or another legally relevant category.

Analyse the role of:

- automated AI access;
- provider APIs;
- account and portal access;
- standard usage units;
- premium boosts;
- top-ups;
- rollover;
- human onboarding;
- support;
- study-support guidance;
- optional human assistance;
- model/provider substitution;
- generated output;
- stored user prompts, files and content;
- security and feature updates.

Explain which statutory rules apply to each component and whether a combined agreement requires separate disclosures, consent or remedy treatment.

---

## 7. Pre-contract information

Create a complete requirement matrix for information that must be supplied before the consumer is bound.

Include at least:

- supplier identity, organisation number and MVA status;
- geographic address and communication channels;
- principal service characteristics;
- intended use and material limitations;
- functionality, compatibility and interoperability;
- supported devices, browsers and account requirements;
- internet and third-party provider dependency;
- provider-change and model-change limitations;
- monthly or annual price including MVA;
- billing interval and renewal;
- total price or calculation method;
- usage allowance and hard-cap behaviour;
- premium-boost allocation;
- top-up prices and expiry;
- rollover rules;
- duration and minimum commitment;
- cancellation and pause procedure;
- withdrawal rights and exceptions;
- immediate commencement treatment;
- delivery/activation time;
- complaint and remedy rights;
- statutory conformity and update obligations;
- service-change rights;
- customer-content export, retention and deletion;
- accepted payment methods;
- geographic and eligibility restrictions;
- student, age and Family eligibility;
- customer support;
- complaint and dispute-resolution channels.

Identify exactly what must appear:

1. On the pricing page.
2. On each plan page.
3. During registration.
4. In the checkout summary.
5. Immediately above the final payment button.
6. In linked terms.
7. In a withdrawal notice.
8. In post-purchase confirmation on a durable medium.

---

## 8. Payment-obligation checkout requirement

Analyse the Norwegian requirement that the consumer must expressly acknowledge the payment obligation.

Determine:

- the exact statutory test;
- the information required immediately before ordering;
- whether information can be behind links, expandable panels or separate pages;
- visibility, typography, prominence and proximity requirements;
- whether default selections are permissible;
- acceptable and unacceptable button labels;
- recommended Bokmål and English wording for:
  - monthly subscription;
  - annual subscription;
  - semester plan;
  - standard top-up;
  - premium boost;
  - free trial converting to paid;
  - zero-price onboarding followed by paid access;
- consequences of non-compliance.

Provide at least five compliant and five non-compliant button examples, with reasons. The final recommendation must be suitable for direct Wix implementation.

---

## 9. Immediate digital-service commencement

Determine the lawful procedure where Atlas activates access before the withdrawal period expires.

Distinguish:

1. A service beginning during the withdrawal period.
2. A service fully performed during the withdrawal period.
3. Digital content not supplied on a physical medium.
4. A continuing digital service.
5. A mixed agreement containing onboarding and recurring access.

Determine whether Atlas must obtain:

- an express request for early commencement;
- express prior consent;
- acknowledgement of proportional-payment liability;
- acknowledgement that withdrawal is lost following full service performance;
- acknowledgement that withdrawal is lost when qualifying digital-content delivery begins;
- separate consent for different components.

Assess whether one checkbox can cover several acknowledgements or whether separate unchecked checkboxes are required. Provide recommended Bokmål and English wording. Do not use pre-ticked boxes.

Specify evidence to preserve:

- exact checkbox/button text and version;
- date/time;
- account and order ID;
- offer ID and contract version;
- session/IP evidence where lawful and proportionate;
- terms and withdrawal-notice versions;
- recorded acknowledgements;
- activation timestamp;
- confirmation-email content.

---

## 10. Withdrawal rights

Prepare an offer-by-offer matrix for Student Basic, Student Plus, Everyday Basic, Family and each top-up.

Determine:

- whether the normal withdrawal period applies;
- when it starts;
- required information and withdrawal form;
- extension where information is missing;
- impact of immediate commencement;
- proportional payment for supplied service;
- conditions for complete loss of the right;
- treatment of unused and partly used top-ups;
- annual and semester subscriptions;
- trial periods;
- Family invitations and shared usage;
- associated agreements and add-ons;
- customer-created content and service access after withdrawal.

Distinguish withdrawal from cancellation, ordinary termination, termination for breach, rescission for non-conformity and discretionary goodwill refunds.

---

## 11. Cancellation and ordinary termination

Analyse:

- effective date of monthly cancellation;
- whether prorating is required or discretionary;
- binding-period requirements and any economic-benefit condition;
- annual and semester cancellation;
- student summer pause;
- cancellation channel and ease-of-use requirements;
- account-dashboard cancellation;
- email cancellation;
- cancellation where account access is unavailable;
- durable-medium confirmation;
- legally required reminders for continuing agreements;
- price-change and material service-change cancellation rights;
- provider/model discontinuation;
- non-payment suspension and termination;
- Family payer versus member rights;
- access and data treatment after cancellation.

Provide a recommended end-to-end cancellation workflow.

---

## 12. Refunds and statutory remedies

Create a refund and remedy matrix covering:

- statutory withdrawal;
- cancellation before delivery;
- ordinary cancellation;
- complete non-delivery;
- delayed activation;
- non-conformity or material defect;
- intermittent outage;
- failure to provide required updates;
- loss of promised functionality;
- provider discontinuation;
- material model downgrade;
- incorrect cap enforcement;
- duplicate billing;
- unauthorized renewal;
- unused and partly used top-ups;
- unused premium boosts;
- annual-plan cancellation;
- price reduction;
- rescission;
- goodwill refund;
- chargeback;
- payment failure.

Determine:

- full versus proportional refund;
- permitted retained amounts;
- price reduction and rescission thresholds;
- refund deadlines;
- required refund method;
- fee deductions;
- late-refund exposure;
- continued access during disputes;
- treatment of customer-created content;
- credit-note and MVA correction dependencies.

Provide:

1. Consumer-facing refund policy.
2. Internal refund-decision matrix.
3. Support-agent SOP.
4. Automatic, manual and escalated approval limits.
5. Evidence requirements.

---

## 13. Digital-service conformity and changes

Analyse obligations relating to:

- delivery and activation;
- conformity with advertised and agreed characteristics;
- compatibility and interoperability;
- security/functionality updates;
- customer support;
- burden of proof;
- availability and outages;
- provider dependency;
- price changes;
- allowance changes;
- rollover changes;
- provider/model replacement;
- feature discontinuation;
- safety, security, legal or provider-policy changes.

Determine what Atlas may lawfully reserve in its terms without excluding mandatory rights. Draft a durable-medium service-change notice.

---

## 14. Top-ups, boosts and rollover

Classify:

- standard top-ups;
- premium-boost top-ups;
- Family top-ups;
- promotional credits;
- rollover units;
- expired units;
- complimentary credits.

Analyse delivery, withdrawal, expiry, partial use, refunds, transferability, Family sharing, termination, provider discontinuation, suspension and required pre-purchase disclosure. Provide separate checkout and acknowledgement wording for top-ups.

---

## 15. Minors, students and Family

Research:

- age thresholds for contracting and payment;
- guardian consent and authority;
- verification;
- marketing to minors;
- academic-integrity disclosure;
- Family account ownership;
- household definition;
- named-user restriction;
- inviting/removing members;
- child-account privacy;
- payer versus user cancellation/withdrawal;
- data export/deletion for subordinate accounts.

Do not recommend activation until required age, guardian and household controls are technically enforceable.

---

## 16. Durable-medium confirmation

Design the mandatory post-order confirmation, including:

- supplier identity;
- order and customer details;
- offer and contract version;
- price including MVA;
- billing interval and renewal;
- allowances and top-ups;
- commencement date;
- next billing date;
- cancellation method;
- withdrawal notice and form;
- early-commencement request;
- recorded acknowledgements;
- circumstances causing loss of withdrawal rights;
- terms/privacy versions;
- complaint/support details;
- data export/deletion information.

Draft complete Bokmål and English confirmation-email copy.

---

## 17. Wix implementation analysis

Map each legal obligation to:

- Wix Studio pricing/plan pages;
- Wix Pricing Plans;
- Wix checkout;
- Wix Members Area;
- Wix Forms;
- CMS collections;
- Velo backend;
- Wix Automations;
- order and member APIs;
- cancellation/pause interface;
- consent and terms-version logging;
- email confirmation;
- refund processing;
- customer portal;
- accessibility;
- Bokmål/English localisation;
- external backend where Wix is insufficient.

Classify every requirement as:

- `NATIVE_WIX`;
- `WIX_PLUS_VELO`;
- `EXTERNAL_BACKEND`;
- `MANUAL_ADMIN_PROCESS`;
- `UNSUPPORTED_OR_REQUIRES_ALTERNATIVE`.

Identify Wix limitations that prevent legal compliance. Do not create public Wix plans or activate checkout as part of this research.

---

## 18. Required deliverables

### A. Executive legal conclusion

State applicable laws, legal classification, recommended withdrawal/cancellation/refund and immediate-commencement models, payment-button model, principal risks and whether Norwegian consumer checkout is ready.

### B. Law and obligation register

Fields: obligation ID, source, section, effective date, obligation, affected offer, consumer-facing requirement, technical requirement, evidence, owner and validation status.

### C. Offer-by-offer rights matrix

Cover all four consumer subscriptions and every top-up/boost.

### D. Consumer terms

Complete Bokmål and English drafts that distinguish statutory rights from discretionary policies and do not exclude mandatory rights.

### E. Checkout copy pack

Bokmål and English pricing disclosures, order summary, payment button, early-commencement request, withdrawal acknowledgement, recurring-payment acknowledgement, Family eligibility, top-up purchase and error states.

### F. Withdrawal pack

Withdrawal notice, statutory form implementation, internal SOP, proportional-payment calculation and evidence checklist.

### G. Cancellation pack

Policy, user flow, confirmation, annual/semester handling, pause rules, Family handling and support escalation.

### H. Refund pack

Consumer policy, statutory-remedy matrix, internal SOP, decision tree, approval limits and templates.

### I. Digital-service commencement pack

Exact consent wording, fields, event logs and acceptance tests.

### J. Wix compliance matrix

Requirement-to-component mapping and implementation owner.

### K. Validation test suite

Include compliant/non-compliant button tests, missing-information tests, unchecked-consent tests, activation tests, withdrawal, proportional refund, cancellation, Family, top-up, durable-medium, bilingual, accessibility and audit-log tests.

### L. Pending-review register

Separate Norwegian lawyer, accountant/tax adviser, provider, payment provider, Wix and project-owner decisions.

### M. Source bibliography

List only sources actually relied upon, with issuer, date, jurisdiction and relevance.

---

## 19. Quality and safety controls

- Do not declare legal compliance because draft terms exist.
- Do not treat a checkbox as valid consent without analysing wording, placement and evidence.
- Do not assume activation automatically removes withdrawal rights.
- Do not confuse withdrawal, cancellation, termination, rescission, price reduction and refund.
- Do not substitute US concepts for Norwegian law.
- Do not apply future legislation before its effective date.
- Preserve `publicAllowed=false` and `purchaseAllowed=false`.
- Preserve the Managed Secure and all Atlas safety locks.
- Label unresolved legal interpretations `PENDING_LEGAL_REVIEW`.
- Use `PASS`, `PARTIAL`, `BLOCKED` and `NO_GO` consistently.

The report must end with a decisive recommendation on whether Norwegian consumer checkout may be activated and an exact evidence list required before the state can change to `GO`.
