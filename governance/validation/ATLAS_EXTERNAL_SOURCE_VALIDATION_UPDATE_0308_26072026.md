# Atlas AI External Source Validation Update — 03:08, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Repository:** `nanotech-solutions-norway/Atlas`  
**Scope:** Unresolved consumer-law, MVA, identity, cancellation, tax, minor and accessibility processes  
**Release state:** `NO_GO`  
**Classification boundary:** Verified source facts and workflow corrections are `AUTO_APPROVED`; Atlas-specific legal, tax, launch-scope and implementation choices remain `PENDING_REVIEW`, `PENDING_LEGAL_REVIEW` or `PENDING_ACCOUNTING_AND_TAX_REVIEW`.

> This file records current official-source validation. It is evidence, not professional legal or tax approval and not authority to create Wix Pricing Plans, enable checkout, accept payment or activate production access.

---

## 1. Validation method

The current canonical GitHub state after merge commit `70ec3e09cd630784e737acdc579d9cac2097c87e` was reconciled against current official sources available on 26.07.2026.

Sources were limited to:

- Lovdata and Norwegian legislative preparatory works;
- Norwegian Tax Administration;
- Datatilsynet;
- official EU VAT/OSS guidance;
- official Wix developer and support documentation.

External sources remain evidence under `ATLAS_SOURCE_AUTHORITY_MAP.md`. They do not independently approve Atlas-specific terms, tax positions, architecture or release.

---

## 2. Legal and consumer-process validation

### SRC-LEGAL-001 — Electronic payment-obligation acknowledgement

**Verified requirement:** Angrerettloven § 16 requires the prescribed material information to be clear and prominent immediately before an electronic paid order. The consumer must expressly acknowledge that the order entails an obligation to pay. If a button or equivalent function is used, it must be labelled `bestilling med forpliktelse til å betale` or equivalently unambiguous wording. Failure means the consumer is not bound.

**Atlas impact:**

- The current recommended final button remains supportable as a research draft.
- Generic labels such as `Fortsett`, `Bekreft`, `Start`, `Aktiver` or `Fullfør` remain prohibited for the final paid action.
- Final wording and rendered placement remain `PENDING_LEGAL_REVIEW` and `NOT_IMPLEMENTED`.

**Source:** Lovdata, Angrerettloven § 16: https://lovdata.no/nav/lov/2014-06-20-27/%C2%A719

**Result:** `PASS_REQUIREMENT / IMPLEMENTATION_BLOCKED`.

### SRC-LEGAL-002 — Durable-medium confirmation and early commencement

**Verified requirement:** Angrerettloven §§ 18–19 require contract confirmation on a durable medium before service delivery begins and an express consumer request where a paid service starts during the withdrawal period. The consumer must also acknowledge that the withdrawal right is lost only after the trader has fully performed all obligations.

**Atlas impact:**

- Activation alone cannot be used as a blanket withdrawal-right waiver for a continuing subscription.
- Early-start and delayed-start choices must remain unselected by default.
- Durable-medium confirmation must be generated and delivered before entitlement activation.
- Exact wording and proportional-payment method remain `PENDING_LEGAL_REVIEW`.

**Source:** Lovdata, Angrerettloven §§ 18–19: https://lovdata.no/nav/lov/2014-06-20-27/%C2%A719

**Result:** `PASS_REQUIREMENT / IMPLEMENTATION_BLOCKED`.

### SRC-LEGAL-003 — Proportional payment after withdrawal

**Verified requirement:** Under Angrerettloven § 26, proportional payment for service supplied before withdrawal is available only where the consumer expressly requested early commencement and the required information was provided. The payment obligation falls away where the statutory information or express request is missing.

**Atlas impact:**

- Any calculation must be lawyer-approved and reproducible.
- Missing consent or disclosure evidence must force a full-refund path.
- Usage alone must not automatically determine the charge without an approved formula and market-value reasonableness check.

**Source:** Lovdata, Angrerettloven § 26: https://lovdata.no/nav/lov/2014-06-20-27/%C2%A727

**Result:** `PASS_REQUIREMENT / CALCULATION_PENDING_LEGAL_REVIEW`.

### SRC-LEGAL-004 — Cancellation, binding periods and six-month reminders

**Verified requirement:** Digitalytelsesloven § 33 confirms that monthly advance-paid continuing agreements normally end from the next payment period; cancellation must be simple and available through the contracting communication method or another suitable method used by the supplier. Binding periods above six months require special circumstances and may never exceed twelve months. Any binding period requires a proportionate economic benefit. Active reminders must be sent at least every six months.

**Atlas impact:**

- Monthly cancellation at the next payment date remains the lowest-risk working model.
- Annual and semester plans remain blocked until legal review of term, benefit, cancellation, normal compensation and refund treatment.
- Portal-only reminders are insufficient; delivery evidence is required.

**Source:** Lovdata, Digitalytelsesloven § 33: https://lovdata.no/nav/lov/2022-06-17-56/kap7

**Result:** `PASS_REQUIREMENT / ANNUAL_AND_SEMESTER_BLOCKED`.

### SRC-LEGAL-005 — Future electronic withdrawal function

**Verified status:** Law 19 June 2026 no. 34 contains a new Angrerettloven § 20 a requiring an electronic withdrawal function labelled `angre avtalen` or equivalent and an immediate durable-medium receipt. The enactment provides that commencement occurs when the King determines and permits different provisions to commence at different times. No current official commencement decision for § 20 a was identified in this validation run.

**Atlas impact:**

- Do not classify § 20 a as current law in force on 26.07.2026.
- Retain it as a forward implementation requirement and recheck immediately before build completion and launch.
- Building a compatible withdrawal function now is recommended but remains a project implementation choice pending approval.

**Sources:**

- Lovdata, Law 19.06.2026 no. 34: https://lovdata.no/dokument/NL/lov/2026-06-19-34
- Prop. 38 LS (2025–2026), implementation and commencement table: https://www.regjeringen.no/no/dokumenter/prop.-38-ls-20252026/id3152649/

**Result:** `ENACTED_NOT_VERIFIED_IN_FORCE / PRE_LAUNCH_RECHECK_REQUIRED`.

---

## 3. Identity, minors and privacy validation

### SRC-ID-001 — Minor contractual capacity

**Verified requirement:** A person under 18 is a minor and generally cannot independently perform legal acts or control funds unless specifically authorised by law.

**Atlas impact:**

- The consumer contract holder and payer must remain at least 18 years old unless Norwegian counsel approves a narrower lawful exception.
- Minor independent subscription and top-up purchases remain blocked.

**Source:** Lovdata, Vergemålsloven §§ 8–9: https://lovdata.no/nav/lov/2010-03-26-9/kap3/%C2%A714

**Result:** `PASS_REQUIREMENT / MINOR_PURCHASE_BLOCK_PRESERVED`.

### SRC-ID-002 — Child-data consent and age assurance

**Verified requirement:** Where consent is the processing basis for an information-society service directed at children, Norwegian parental consent is required below age 13 and reasonable verification measures are required. Datatilsynet also states that consent must be voluntary, specific, informed, unambiguous, active, documented, easy to withdraw and separate from contract acceptance or terms.

**Atlas impact:**

- Contract acceptance, early-service commencement, privacy acknowledgement, optional marketing consent and cookie consent must remain separate interactions.
- Family child access remains blocked until age, guardian, relationship and privacy-safe defaults are technically enforceable.
- The legal basis for necessary account and service processing must be documented separately from optional consent.

**Sources:**

- Datatilsynet, legal bases and consent, updated 17.03.2026: https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/om-behandlingsgrunnlag/samtykke/
- Datatilsynet, children and digital services: https://www.datatilsynet.no/personvern-pa-ulike-omrader/kundehandtering-handel-og-medlemskap/digitale-tjenester-og-forbrukeres-personopplysninger/barn-og-unge-forbrukere/

**Result:** `PASS_REQUIREMENT / FAMILY_AND_MINOR_CONTROLS_BLOCKED`.

---

## 4. MVA and cross-border validation

### SRC-TAX-001 — Domestic digital and remote-service rate

**Verified working evidence:** Norwegian Tax Administration guidance lists software access and updates, hosting, online storage and related electronically delivered services at the ordinary 25% rate. The guidance is general and each supply must still be classified concretely.

**Atlas impact:**

- 25% remains a controlled Norwegian domestic working baseline.
- It is not final treatment for every offer, bundle, customer, top-up, refund or jurisdiction.

**Source:** Norwegian Tax Administration, rates for remotely deliverable services: https://www.skatteetaten.no/satser/merverdiavgiftssatser-for-fjernleverbare-tjenester-kjopt-fra-utlandet/

**Result:** `PASS_WORKING_BASELINE / PROFESSIONAL_SIGNOFF_REQUIRED`.

### SRC-TAX-002 — Imported software, cloud and professional services

**Verified requirement:** Norwegian businesses buying remotely deliverable services from foreign suppliers may have to calculate and report Norwegian MVA under reverse-charge rules. Official examples include software, licences, website/software development, hosting, legal, accounting and consultancy services. Registered recipients have no de minimis threshold for inclusion in the ordinary MVA return.

**Atlas impact:**

- Provider/API/cloud/software purchases require a vendor-by-vendor reverse-charge posting rule.
- Payment-provider and provider invoices must be retained and reconciled to accounting entries.
- MVA-015 remains professionally unresolved but its necessity is validated.

**Sources:**

- Norwegian Tax Administration, services purchased from abroad: https://www.skatteetaten.no/bedrift-og-organisasjon/avgifter/mva/utland/tjenester/
- MVA Handbook § 11-3: https://www.skatteetaten.no/rettskilder/type/handboker/merverdiavgiftshandboken/gjeldende/M-11/M-11-3/

**Result:** `PASS_REQUIREMENT / ACCOUNTING_CONFIGURATION_BLOCKED`.

### SRC-TAX-003 — EU B2C services and non-Union OSS

**Verified requirement:** A business established outside the EU with no EU fixed establishment may use the non-Union OSS scheme for services supplied to EU consumers. It may select one EU Member State of identification. Customer-country VAT must be charged, one OSS return/payment is filed through the selected state, and OSS records are retained for up to ten years.

**Current-source change:** The European Commission published revised OSS explanatory notes and guidelines on 24.07.2026, including changes that enter into force from 01.01.2027. The current Atlas launch design must therefore record an OSS rule version and a pre-launch/regulatory-change revalidation trigger.

**Atlas impact:**

- Foreign EU B2C checkout remains blocked until a Member State of identification, registration owner, country-rate source, location evidence and filing/reconciliation process are approved.
- The EU EUR 10,000 simplification described for businesses established in one EU Member State must not be assumed to apply to a Norwegian supplier using the non-Union scheme.
- MVA-008 through MVA-010 remain open.

**Sources:**

- European Commission, OSS registration: https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/register-oss_en
- Your Europe, EU VAT OSS, checked 13.05.2026: https://europa.eu/youreurope/business/finance-and-tax/vat/one-stop-shop/index_en.htm
- European Commission, revised OSS guides published 24.07.2026: https://vat-one-stop-shop.ec.europa.eu/guides_en

**Result:** `PASS_REQUIREMENT / EU_B2C_CHECKOUT_BLOCKED`.

---

## 5. Wix platform validation

### SRC-WIX-001 — Member identity prerequisite

**Verified platform fact:** Wix Pricing Plan purchases are currently limited to members; an order includes a `memberId`, and a buyer cannot purchase a plan without one.

**Atlas impact:**

- The absence of Wix Members Area remains an operative blocker.
- `IMP-016` and the Phase 2 identity prerequisite remain correctly classified as blocked.

**Source:** Wix Pricing Plans Order Object: https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/orders/order-object

**Result:** `PASS_PLATFORM_FACT / MEMBERS_AREA_BLOCKED`.

### SRC-WIX-002 — Cancellation processing is asynchronous

**Verified platform fact:** Recurring orders may be cancelled immediately or at the next payment date. A member cancellation request may enter `PENDING_CANCELLATION`, and payment/refund operations may continue before the order becomes `CANCELED`.

**Atlas impact:**

- A cancellation request receipt cannot be treated as final cancellation or refund completion.
- Case state must remain open until order, payment, entitlement and accounting statuses reconcile.
- Email cancellation fallback remains required because account access cannot be the only legal route.

**Sources:**

- Wix Request Cancellation: https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/orders/request-cancellation
- Wix Cancel Order: https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/orders/cancel-order

**Result:** `PASS_PLATFORM_FACT / ORCHESTRATION_REQUIRED`.

### SRC-WIX-003 — Published-site test limitation

**Verified platform fact:** Member-facing Pricing Plans APIs require a published site and do not work fully in preview mode.

**Atlas impact:**

- Live member/API acceptance tests cannot be represented as completed while the site remains Draft.
- A controlled non-public test or staging publication strategy must be approved before member-order tests.
- This does not authorize public purchase or production availability.

**Source:** Wix current-member order/cancellation documentation: https://dev.wix.com/docs/sdk/frontend-modules/pricing-plans/orders/request-current-member-order-cancellation

**Result:** `PASS_PLATFORM_LIMITATION / TEST_ENVIRONMENT_DECISION_PENDING`.

### SRC-WIX-004 — Wix tax configuration boundary

**Verified platform fact:** Pricing Plans tax application is defined at site level and is not accessible through the Pricing Plans Orders API. Wix users must configure tax collection manually.

**Atlas impact:**

- GitHub/Wix CMS metadata cannot by itself guarantee the charged tax result.
- MVA-019 requires dashboard configuration evidence and transaction tests.
- Cross-border B2C requires a jurisdiction decision layer or a separately approved Wix-supported configuration; it cannot be inferred from API fields alone.

**Source:** Wix Pricing Plans Orders introduction: https://dev.wix.com/docs/sdk/backend-modules/pricing-plans/orders/introduction

**Result:** `PASS_PLATFORM_FACT / TAX_CONFIGURATION_BLOCKED`.

---

## 6. Accessibility validation

### SRC-ACC-001 — Norwegian private-sector minimum

**Verified requirement:** The Norwegian IKT accessibility regulation applies to main web solutions supporting a business's ordinary functions. For private businesses, § 4 currently requires WCAG 2.0 level A and AA, with listed exceptions for success criteria 1.2.3, 1.2.4 and 1.2.5, or an equivalent standard. The business must be able to document compliance.

**Atlas impact:**

- The statutory private-sector baseline must be recorded as WCAG 2.0 A/AA with the stated exceptions.
- WCAG 2.1 AA may be retained as a stronger internal quality target, but it must not be misrepresented as the exact current private-sector statutory text without a separate legal basis.
- Checkout, cancellation, consent and withdrawal flows require documented keyboard, focus, label, error, contrast, reflow and screen-reader testing.

**Source:** Lovdata, IKT accessibility regulation §§ 2, 4 and 5: https://lovdata.no/nav/forskrift/2013-06-21-732

**Result:** `PASS_REQUIREMENT / IMPLEMENTATION_AND_DOCUMENTATION_NOT_RUN`.

---

## 7. Updated validation conclusions

| Area | Previously unresolved | Current validation result | Remaining gate |
|---|---|---|---|
| Payment-obligation button | Exact legal requirement | Requirement confirmed | Counsel approval and rendered test |
| Early commencement | Service/content distinction and evidence | Requirement confirmed; activation alone insufficient | Counsel-approved model and event store |
| Proportional payment | Formula and conditions | Conditions confirmed | Formula and case simulations |
| Monthly cancellation | Platform/legal process | Legal and Wix mechanics confirmed | Portal, email fallback and reconciliation |
| Annual/semester | Binding/prepayment design | Binding restrictions confirmed | Counsel and accountant decision |
| Electronic withdrawal function | Effective date | Enacted; commencement not verified | Recheck and approved implementation decision |
| Minor/Family | Contract/privacy controls | Adult-payer and parental-control need confirmed | Identity/guardian/privacy architecture |
| Reverse charge | Foreign provider purchases | Requirement confirmed | Account codes and posted examples |
| EU B2C/OSS | Registration and filing route | Non-Union OSS route confirmed; revised 24.07.2026 guides identified | Member State, registration, rates, evidence and filing owner |
| Wix identity | Members Area necessity | Purchase requires member identity | Install/configure/test in controlled environment |
| Wix cancellation | Completion model | Asynchronous state confirmed | State machine and reconciliation |
| Wix tax | API/configuration boundary | Site-level manual configuration confirmed | Dashboard evidence and transaction tests |
| Accessibility | Exact private-sector baseline | WCAG 2.0 A/AA with exceptions confirmed | Implement, test and document |

---

## 8. Control outcome

The external validation materially improves the professional review and implementation specification but does not close any gate requiring:

- Norwegian lawyer approval;
- accountant or tax-adviser approval;
- contracting entity data;
- Wix/payment configuration;
- identity, entitlement, consent or evidence implementation;
- executed acceptance tests;
- explicit written release approval.

Consumer checkout, public Pricing Plans, purchase activation and public release remain `NO_GO`.