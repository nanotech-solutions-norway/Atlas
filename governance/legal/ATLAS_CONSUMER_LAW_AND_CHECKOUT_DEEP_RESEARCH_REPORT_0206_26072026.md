# Atlas AI Consumer Law and Checkout Deep Research Report — 02:06, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Jurisdiction:** Norway; EU/EEA where relevant  
**Commercial contract:** `0.5.1`  
**Research status:** `RESEARCH_COMPLETED_DRAFT_PACK_CREATED`  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Consumer checkout:** `NO_GO`  
**Public release:** `NO_GO`

> This report is controlled legal research and implementation planning. It is not a legal opinion, does not evidence professional approval and must not be represented as proof of compliance.

---

## 1. Executive legal conclusion

### 1.1 Applicable framework

The principal Norwegian statutes applicable to an Atlas AI consumer subscription are:

1. **Angrerettloven** for pre-contract information, electronic ordering, payment-obligation acknowledgement, durable-medium confirmation, withdrawal, early commencement and proportional payment.
2. **Digitalytelsesloven** for delivery, conformity, updates, changes, price changes, binding periods, ordinary cancellation, statutory remedies, refunds and customer-created content.
3. **Ehandelsloven** for supplier identity, electronic contracting information, error-correction mechanisms, contract-term availability and electronic order confirmation.
4. **Markedsføringsloven** for unfair or misleading practices, material omissions, pricing and protection of children.
5. **Vergemålsloven** for the contractual capacity of minors.
6. **Personopplysningsloven/GDPR** for account, consent, profiling, child-data, export and deletion controls.

The EU Consumer Rights Directive and Digital Content and Digital Services Directive are relevant interpretative sources, but the implementation must be built against the Norwegian statutes in force on the launch date.

### 1.2 Recommended legal classification

**Research interpretation — `PENDING_LEGAL_REVIEW`:** Student Basic, Student Plus, Everyday Basic and Family are most defensibly classified as **continuing digital services**. The defining supply is ongoing access to an Atlas-managed AI service that lets the customer create, process, store, access and interact with digital data. Individual AI outputs may constitute digital content, but they do not change the principal subscription into a one-off supply of digital content.

Consequences:

- The 14-day withdrawal period normally begins when the subscription contract is concluded.
- Activating access does **not** by itself remove the withdrawal right.
- If the consumer expressly requests commencement during the withdrawal period, Atlas may have a basis for proportional payment for service delivered before withdrawal, provided all statutory information and consent requirements are satisfied.
- Loss of the withdrawal right for a service requires full performance and the required prior request/acknowledgement. A continuing subscription is not fully performed merely because access is activated.
- Atlas should not use a one-off digital-content waiver as the default withdrawal model for subscriptions.

### 1.3 Checkout model

The recommended checkout architecture is:

1. A final-order screen that prominently displays the selected plan, essential characteristics, total price including MVA, billing interval, duration, minimum commitment, renewal and cancellation treatment.
2. A final button labelled unambiguously with the payment obligation.
3. A separate, unchecked early-commencement request.
4. A clear explanation that withdrawal during the first 14 days may result in proportional payment for service already supplied.
5. A separate terms acceptance record; privacy and marketing consent must not be bundled into the purchase or early-commencement request.
6. Immediate durable-medium confirmation containing the complete contract record and withdrawal form.

Recommended final button:

- Bokmål: **`Bestill abonnement med forpliktelse til å betale`**
- English: **`Order subscription with obligation to pay`**

The shorter statutory wording **`Bestilling med forpliktelse til å betale`** may also be used. Generic labels such as `Fortsett`, `Bekreft`, `Start`, `Aktiver`, `Opprett konto` or `Fullfør` are not approved for the final paid-order action.

### 1.4 Cancellation and binding periods

- A continuing digital service must have a simple cancellation method using the same or another suitable communication channel.
- For a monthly prepaid plan, cancellation should normally take effect at the next billing date, with access continuing through the paid period.
- A binding period may not exceed six months unless special circumstances justify up to twelve months and the consumer receives an economic benefit proportionate to the binding period.
- A six-month reminder must be actively sent. Merely displaying information in a customer portal is insufficient.
- The annual 10% discount cannot be treated as a validated basis for a twelve-month binding period until Norwegian counsel confirms that the statutory conditions are satisfied.
- The student semester option must also be reviewed if it creates a binding period rather than a cancellable prepaid term.

### 1.5 Family and minors

Recommended launch rule:

- The payer and contract holder must be at least 18 years old.
- Family members are named authorised users, not separate contracting parties.
- A minor must not independently purchase a subscription or top-up.
- Any child account requires guardian authority, age controls, privacy-safe defaults and a technically enforceable relationship to the adult payer.
- Marketing must not directly exhort children to purchase or persuade adults to purchase.

Because Wix Members Area is not installed and Atlas-specific age, guardian, household and subordinate-account controls are not implemented, **Family remains blocked**.

### 1.6 Top-ups and premium boosts

**Research interpretation — `PENDING_LEGAL_REVIEW` and `PENDING_ACCOUNTING_AND_TAX_REVIEW`:** Standard units and premium boosts should be structured as fixed, non-transferable additional entitlements within the existing Atlas digital service, not as generic stored value or cash-equivalent credit.

Required controls:

- exact quantity, price including MVA, expiry and non-rollover treatment shown before purchase;
- no negative balance or silent chargeable overage;
- purchase button that states the item and price;
- separate order and entitlement records;
- no consumption before the early-start choice is captured, unless counsel approves an alternative treatment;
- refund and MVA treatment based on actual unused/used entitlement and the approved tax classification.

### 1.7 Service changes and model substitution

Atlas may reserve a controlled right to replace providers or AI models only where the terms identify an objective reason, the change is necessary or proportionate, no extra charge is imposed and the service remains conforming. A materially adverse change requires clear durable-medium notice and a statutory termination route. Mandatory conformity and remedy rights cannot be excluded.

### 1.8 Decisive release recommendation

**Recommendation: `NO_GO`.**

The research mandate has been executed and implementation-ready drafts have been prepared. Norwegian consumer checkout must remain disabled because:

- the contracting entity and MVA invoice identity are unresolved;
- offer classifications are not approved by Norwegian counsel;
- the annual/semester and top-up models require legal review;
- no public terms are legally approved;
- no compliant checkout or durable-medium implementation exists;
- age, guardian and Family controls do not exist;
- Wix tax configuration, consent logging, refund handling and reconciliation are not validated;
- no accountant/tax-adviser sign-off exists;
- no Norwegian lawyer sign-off or written release approval exists.

---

## 2. Law and obligation register

| ID | Authority | Obligation | Atlas requirement | Evidence required | Status |
|---|---|---|---|---|---|
| CL-001 | Angrerettloven § 8 | Give complete pre-contract information clearly and comprehensibly | Bokmål/English disclosure pack; supplier, characteristics, price, term, withdrawal, complaint and compatibility information | Approved copy and rendered-page evidence | `RESEARCH_COMPLETE_IMPLEMENTATION_BLOCKED` |
| CL-002 | Angrerettloven §§ 14–15 | Information becomes part of the contract; limited-space exceptions are narrow | Version-controlled disclosure record; no hidden material term | Terms/disclosure snapshot | `RESEARCH_COMPLETE_IMPLEMENTATION_BLOCKED` |
| CL-003 | Angrerettloven § 16 | Immediately before order, prominently show main characteristics, total price, duration/minimum commitment and termination; button must acknowledge payment | Final order summary and compliant button | Desktop/mobile screenshots and event log | `BLOCKED` |
| CL-004 | Angrerettloven § 18 | Confirm contract on a durable medium before service performance begins | Immediate email/PDF or immutable stored confirmation | Delivered email, immutable snapshot and delivery log | `BLOCKED` |
| CL-005 | Angrerettloven § 19 | Early commencement of a paid service requires an express request and acknowledgement | Separate unchecked checkbox; timestamp and exact text version | Consent event and readback | `BLOCKED` |
| CL-006 | Angrerettloven §§ 20–22 | Provide 14-day withdrawal right and correctly apply exceptions | Subscription classified as continuing digital service; no automatic loss at activation | Lawyer-approved classification and tests | `PENDING_LEGAL_REVIEW` |
| CL-007 | Angrerettloven § 24 | Refund within 14 days using same payment method and no fee | Refund workflow and deadline monitoring | Payment/refund event evidence | `BLOCKED` |
| CL-008 | Angrerettloven § 24 a | Restrict post-termination use of consumer-created non-personal content and support retrieval where required | Content export/deletion policy and technical flow | Export/delete tests | `BLOCKED` |
| CL-009 | Angrerettloven § 26 | Proportional payment requires correct information and express early-start request; payment may be barred if requirements are absent | Daily/time/usage-based approved calculation and zero-charge exception | Calculation tests and lawyer approval | `PENDING_LEGAL_REVIEW` |
| CL-010 | Digitalytelsesloven §§ 4–10 | Deliver without undue delay; conform to agreement and objective requirements; provide necessary updates | Service specification, compatibility, availability and update commitments | Service catalogue and runtime tests | `BLOCKED` |
| CL-011 | Digitalytelsesloven §§ 12–25 | Delay/defect remedies, repair/replacement, price reduction, termination and damages | Statutory remedy matrix and support escalation | Case simulations | `RESEARCH_COMPLETE_IMPLEMENTATION_BLOCKED` |
| CL-012 | Digitalytelsesloven § 28 | Price increases require contractual basis, reasonable notice and cancellation right where applicable; no increase in binding period | Versioned price-change notice and termination route | Notice and cancellation test | `BLOCKED` |
| CL-013 | Digitalytelsesloven § 33 | Simple cancellation; binding limits; six-month reminders | Self-service cancellation; active reminder; no obstructive flow | End-to-end tests | `BLOCKED` |
| CL-014 | Digitalytelsesloven §§ 41–42 | Modifications require contractual basis, no extra charge and clear information; adverse changes trigger durable notice/termination | Provider/model substitution policy and change-notice flow | Change simulation | `BLOCKED` |
| CL-015 | Digitalytelsesloven §§ 45–47 | Refund after termination/price reduction; same payment method; content restrictions and retrieval | Refund, export and deletion automation | Evidence bundle | `BLOCKED` |
| CL-016 | Ehandelsloven §§ 8–12 | Supplier identity, electronic-contract steps, error correction, contract storage/language and order confirmation | Supplier footer, checkout explanation, editable order, electronic receipt | UI and email evidence | `BLOCKED` |
| CL-017 | Markedsføringsloven §§ 6–8 | No unfair, misleading or materially incomplete marketing | Claims/evidence controls and price/allowance parity | Content audit | `PARTIAL` |
| CL-018 | Markedsføringsloven §§ 19–21 | Enhanced protection of children; no direct purchase exhortation | Age-targeted copy review and marketing exclusion | Campaign audit | `BLOCKED` |
| CL-019 | Vergemålsloven §§ 8–9 | Under-18s generally lack independent legal capacity except where specifically provided | Adult contract holder and guardian authority | Age/guardian tests | `BLOCKED` |
| CL-020 | GDPR art. 5, 6, 8, 12–22 and Norwegian age rule | Lawful basis, transparency, child consent controls where consent is used, minimisation, access/export/deletion | Privacy design separate from purchase consent | DPIA/ROPA and privacy tests | `PENDING_PRIVACY_REVIEW` |
| CL-021 | Law 19 June 2026 no. 34, future Angrerettloven § 20 a | Electronic withdrawal function enacted but not in force as of this report | Future-proof `Angre avtalen` function; do not label current statutory requirement until commencement | Commencement check and activation test | `FUTURE_REQUIREMENT_NOT_IN_FORCE` |

---

## 3. Offer-by-offer rights and classification matrix

| Offer | Working classification | Withdrawal | Early commencement | Ordinary cancellation | Key unresolved issue | State |
|---|---|---|---|---|---|---|
| Student Basic | Continuing digital service | 14 days from contract | Separate request; proportional-payment model | Monthly next billing date | Student eligibility and age evidence | `PENDING_LEGAL_REVIEW` |
| Student Plus | Continuing digital service | 14 days from contract | Separate request; proportional-payment model | Monthly next billing date | Student eligibility and age evidence | `PENDING_LEGAL_REVIEW` |
| Everyday Basic | Continuing digital service | 14 days from contract | Separate request; proportional-payment model | Monthly next billing date | Final service specification | `PENDING_LEGAL_REVIEW` |
| Family | Continuing digital service with adult payer and named users | Adult contract holder exercises withdrawal | Separate request by adult payer | Adult payer cancels; subordinate users lose access at effective date | Age, guardian, household and member controls | `BLOCKED_FAMILY_CONTROLS` |
| Annual option | Same service; prepaid or binding term depends final contract design | 14 days from contract | Same as subscription | Must reflect approved prepayment/binding model | 12-month binding justification and refund method | `BLOCKED_PENDING_LEGAL_MODEL` |
| Student semester option | Same service; fixed/prepaid or binding term depends final design | 14 days from contract | Same as subscription | Must reflect approved term model | Six-month benefit and cancellation treatment | `BLOCKED_PENDING_LEGAL_MODEL` |
| Standard top-up | Additional fixed entitlement within digital service | Right and refund treatment require counsel confirmation | Separate top-up early-use request or delayed usability | Not independently recurring | Service vs digital-content character; proportional use | `PENDING_LEGAL_REVIEW` |
| Premium boosts | Additional fixed entitlement within digital service | Same issue as top-ups | Separate early-use treatment | Not independently recurring | Usage valuation and expiry | `PENDING_LEGAL_REVIEW` |
| Promotional credits | Gratuitous contractual benefit | No paid withdrawal amount, but transparency applies | N/A | Expiry per disclosed policy | Non-discrimination and marketing clarity | `PENDING_REVIEW` |
| Rollover units | Contractual carry-forward benefit | Follows base subscription | N/A | Expire after disclosed one-month window | Clear calculation and no misleading balance | `PENDING_REVIEW` |

### 3.1 Required offer-page disclosures

Each consumer offer page must state, in Bokmål and English:

- plan name;
- price including MVA;
- billing frequency;
- named-user limit;
- standard-unit and premium-boost allowance;
- rollover rule;
- top-up prices and non-automatic nature;
- absence of silent chargeable overage;
- renewal and cancellation treatment;
- minimum commitment, if any;
- early-start choice;
- withdrawal route;
- compatibility/interoperability and material technical requirements;
- principal model/provider dependency and change treatment;
- support and complaint route;
- contract and policy versions.

---

## 4. Approved research model for withdrawal and commencement

### 4.1 Default service model

1. Contract concluded when Atlas accepts the paid order and sends confirmation.
2. Fourteen-day withdrawal period begins at conclusion.
3. Consumer may choose delayed activation until the period expires, or expressly request immediate commencement.
4. Immediate commencement must not be preselected or inferred from purchase.
5. Withdrawal remains available unless the legally applicable full-performance exception is satisfied.
6. If the consumer requested early commencement and withdraws, Atlas calculates only the legally permitted proportional amount.
7. If Atlas failed to give required information or obtain the request, no proportional charge is made.

### 4.2 Proportional-payment calculation — draft

**Preferred calculation for a continuously available monthly service:**

`Permitted amount = gross price for current billing period × elapsed service time / total service time in billing period`

Usage should be used as corroborating evidence, not as a punitive or automatically higher charge, unless counsel approves a different value methodology. The amount must never exceed the normal price for the relevant period and must be reduced where service was unavailable or non-conforming.

For annual or semester prepayment, the denominator and permitted amount must be approved before launch. Top-up consumption requires a separate approved methodology.

### 4.3 Evidence fields

- customer ID and verified email;
- payer age/eligibility state;
- offer ID and version;
- price, currency and MVA basis;
- billing interval and commitment model;
- terms, withdrawal notice and privacy versions;
- final-order summary hash/snapshot;
- payment-button text and locale;
- terms acceptance timestamp;
- early-start checkbox state, exact text and timestamp;
- IP/network and device metadata only to the extent lawful and necessary;
- payment authorisation/order ID;
- activation timestamp;
- first-use and entitlement events;
- durable-medium delivery timestamp and delivery result;
- cancellation/withdrawal request timestamp and channel;
- refund/credit-note IDs and completion timestamp.

---

## 5. Cancellation, renewal, annual, semester and pause conclusions

### 5.1 Monthly subscriptions

- recurring until cancelled;
- cancellation available in the customer account and via support;
- no retention maze, hidden button or mandatory phone call;
- effective at next payment date unless immediate termination is required by law or agreed as a discretionary benefit;
- confirmation sent immediately on a durable medium;
- next billing date and effective access-end date shown before confirmation.

### 5.2 Annual subscription

The approved 10% annual discount is a commercial baseline, not a validated legal binding-period conclusion. Two candidate designs require legal review:

1. **Binding annual term:** only if special circumstances and a proportionate economic benefit satisfy Digitalytelsesloven § 33.
2. **Annual prepayment without binding:** customer may cancel future renewal and may have an avbestilling/refund treatment for the unused period, subject to approved contract and statutory rules.

No annual consumer checkout may be implemented until one model is selected and approved.

### 5.3 Student semester option

A semester plan must define exact dates or duration, price, renewal/non-renewal, cancellation and the economic benefit. Automatic conversion to a different plan is prohibited unless clearly agreed. The design remains blocked pending legal review.

### 5.4 Student summer pause

The summer pause is a discretionary customer benefit. Terms must state:

- eligibility;
- maximum frequency and duration;
- request deadline;
- billing and access effect;
- allowance/rollover effect;
- restart date;
- no removal of statutory rights.

The pause must never make cancellation more difficult.

### 5.5 Six-month reminder

For continuing services, Atlas must actively send the legally required reminder at least every six months. The reminder should include plan, price, billing interval, next payment, cancellation link and support route. A portal-only notice is insufficient.

---

## 6. Statutory remedy and refund framework

| Trigger | Consumer right | Atlas action | Deadline/control | MVA dependency |
|---|---|---|---|---|
| Withdrawal within 14 days; no early start | Full refund | End access, refund same method, issue required accounting correction | Within 14 days | Credit-note/VAT correction model |
| Withdrawal after valid early start | Refund less approved proportional amount | Calculate, explain and refund balance | Within 14 days | Partial credit note |
| Invalid/missing early-start request or information | No proportional charge | Full refund | Within 14 days | Full correction |
| Delay | Performance; in qualifying cases termination/damages | Restore delivery or terminate | Without undue delay | Credit/refund as applicable |
| Defect/non-conformity | Repair/replacement; price reduction; termination; damages | Incident triage and statutory remedy | Statutory promptness | Price-reduction or termination correction |
| Material adverse service change | Termination right where statutory conditions apply | Durable notice and cost-free exit | Notice before change; exercise window | Prorated credit if required |
| Ordinary cancellation | Stop future renewal | Preserve access to effective date unless immediate model applies | Immediate confirmation | No correction for fully delivered paid period unless required |
| Duplicate/incorrect charge | Full correction | Refund and correct ledger | Immediate operational priority | Credit note and tax correction |
| Goodwill refund | Contractual discretion; no reduction of statutory rights | Approval workflow | Internal SLA | Accountant determines documentation |
| Chargeback | Payment-provider process; rights remain | Freeze evidence, avoid double refund | Provider timetable | Reconcile provider adjustment |

Refunds, cancellations, withdrawals, price reductions and terminations must have separate reason codes. Support must not use the word `refund` as a substitute for identifying the legal basis.

---

## 7. Family, student, minor and guardian controls

### 7.1 Minimum launch controls

- contract holder and payer: 18+;
- student status: evidence rule, verification frequency and expiry;
- Family owner: adult payer;
- named members: unique account, no credential sharing;
- household definition in terms;
- invitation acceptance and removal flow;
- guardian authority for minor members;
- no independent payment instrument for minors;
- no purchase or top-up button for subordinate minor accounts;
- privacy-safe defaults and no behavioural advertising to children;
- data access/export/deletion route for adult payer and user, respecting individual privacy rights;
- abuse/safety escalation.

### 7.2 Launch recommendation

- Student plans may launch only to verified customers aged 18+ in the first consumer release unless a separate minor design is legally and technically approved.
- Family may initially be restricted to adult named household users. Adding minors is a later gated feature.

These are implementation recommendations, not a change to the approved commercial price structure.

---

## 8. Wix implementation conclusion

Wix Pricing Plans can represent recurring and one-time plans and supports member cancellation immediately or at the next payment date. However, the Atlas legal model cannot be delivered by native Pricing Plans configuration alone.

Required architecture:

- **Native Wix:** plan/order shell, price preview, payment processing where supported, member order list and cancellation request.
- **Wix + Velo:** custom final-order summary, compliant button control, separate early-start capture, localisation, entitlement gating, six-month reminders and confirmation orchestration.
- **External backend:** immutable consent/version evidence, entitlement/metering ledger, durable contract snapshot, refund decision record, export/deletion workflow, jurisdiction/tax rules and financial reconciliation.
- **Manual controlled process:** legal escalation, exceptional refunds, minor/guardian exception handling, complaints and professional sign-off.

Current Wix evidence:

- site remains Draft;
- Wix Pricing Plans installed;
- operative plan count read back as `0`;
- Atlas Pricing Contract records read back as `13`;
- all 13 records retain `professionalSignoffRequired=true`, `publicAllowed=false` and `purchaseAllowed=false`;
- the four consumer offers retain `checkoutLegalStatus=NO_GO`;
- Family retains a separate Family-control block.

No public plan or checkout was created during this workstream.

---

## 9. Pending legal-review register

| ID | Decision required | Owner | Release effect | Classification |
|---|---|---|---|---|
| PLR-001 | Confirm continuing digital-service classification for all four subscriptions | Norwegian consumer lawyer | Checkout blocker | `PENDING_LEGAL_REVIEW` |
| PLR-002 | Approve early-commencement and proportional-payment model | Norwegian consumer lawyer | Checkout blocker | `PENDING_LEGAL_REVIEW` |
| PLR-003 | Approve top-up/boost withdrawal, expiry and partial-use treatment | Lawyer + tax adviser | Top-up blocker | `PENDING_LEGAL_REVIEW` |
| PLR-004 | Approve annual 10% model and any 12-month binding period | Norwegian consumer lawyer | Annual blocker | `PENDING_LEGAL_REVIEW` |
| PLR-005 | Approve semester term and summer pause | Norwegian consumer lawyer | Semester blocker | `PENDING_LEGAL_REVIEW` |
| PLR-006 | Approve Family household, adult payer, minor and guardian model | Lawyer + privacy adviser | Family blocker | `PENDING_LEGAL_REVIEW` |
| PLR-007 | Confirm proportional-payment formula and outage adjustment | Norwegian consumer lawyer | Withdrawal blocker | `PENDING_LEGAL_REVIEW` |
| PLR-008 | Approve terms, notices, forms, emails and Bokmål/English parity | Norwegian consumer lawyer | Publication blocker | `PENDING_LEGAL_REVIEW` |
| PLR-009 | Confirm complaint body and mandatory complaint wording | Norwegian consumer lawyer | Terms blocker | `PENDING_LEGAL_REVIEW` |
| PLR-010 | Monitor commencement of future Angrerettloven § 20 a | Legal owner | Future compliance | `PENDING_REVIEW` |
| PLR-011 | Approve privacy roles, child-data controls and export/deletion model | Privacy adviser/DPO | Account blocker | `PENDING_PRIVACY_REVIEW` |
| PLR-012 | Verify payment-provider refund, renewal and evidence capabilities | Product/payment owner | Checkout blocker | `PENDING_PROVIDER_VALIDATION` |

---

## 10. Source bibliography

Only sources relied upon are listed.

### Norwegian legislation and preparatory works

1. Lovdata, **Lov om opplysningsplikt og angrerett ved fjernsalg og salg utenom faste forretningslokaler (angrerettloven)**, current consolidated text, particularly §§ 8, 14–16, 18–27.
2. Lovdata, **Lov om levering av digitale ytelser til forbrukere (digitalytelsesloven)**, current consolidated text, particularly §§ 4–10, 12–28, 33, 41–47.
3. Lovdata, **Lov om visse sider av elektronisk handel og andre informasjonssamfunnstjenester (ehandelsloven)**, particularly §§ 8–12.
4. Lovdata, **Lov om kontroll med markedsføring og avtalevilkår mv. (markedsføringsloven)**, particularly §§ 6–8 and 19–21.
5. Lovdata, **Lov om vergemål (vergemålsloven)**, particularly §§ 8–9 and 12.
6. Lovdata, **Lov 19 June 2026 no. 34**, enacted future electronic withdrawal-function provisions; commencement not in force as of this report.
7. Norwegian Government, preparatory works to the Digital Services Act and amendments to the Right of Withdrawal Act, used for distinction between digital service/digital content, binding periods, reminders, proportional payment and durable-medium requirements.

### Authorities and guidance

8. Forbrukertilsynet, guidance on fair digital terms, clear language, children and consumer journeys.
9. Datatilsynet, guidance on children, consent age, guardian verification, data portability and separation of privacy consent from contract acceptance.
10. Wix official API documentation, Pricing Plans Plans V3 and Orders APIs, including query plans, price preview, member cancellation and order management.

### EU sources

11. EUR-Lex, Directive 2011/83/EU on consumer rights.
12. EUR-Lex, Directive (EU) 2019/770 on contracts for the supply of digital content and digital services.

---

## 11. Exact evidence required to change `NO_GO`

1. Signed contracting entity and invoice profile.
2. Norwegian legal opinion approving offer classifications.
3. Lawyer-approved Bokmål and English terms and disclosures.
4. Approved early-start and proportional-payment model.
5. Approved annual, semester, pause, Family and top-up models.
6. Accountant/tax-adviser sign-off for launch scope.
7. Approved payment provider and refund operating model.
8. Implemented account/member/age/guardian controls for the offers released.
9. Implemented checkout with compliant final-order information and payment button.
10. Immutable consent, terms-version and order-snapshot evidence.
11. Durable-medium confirmation with withdrawal form.
12. Self-service cancellation and six-month reminder.
13. Statutory remedy, refund, export and deletion workflows.
14. Bokmål/English parity and accessibility tests.
15. MVA, invoice, credit-note and accounting reconciliation tests.
16. Written product-owner release approval after all mandatory gates pass.

Until all launch-scope items pass, `publicAllowed=false`, `purchaseAllowed=false`, `checkoutLegalStatus=NO_GO` and the overall Atlas release state remain unchanged.