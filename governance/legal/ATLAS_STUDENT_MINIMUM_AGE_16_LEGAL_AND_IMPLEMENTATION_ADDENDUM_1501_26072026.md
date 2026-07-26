# Atlas AI Student Minimum Age 16 — Legal and Implementation Addendum

**Prepared:** 15:01, 26.07.2026 Europe/Oslo  
**Commercial contract:** `0.5.1`  
**Status:** `APPROVED_PRODUCT_RULE / PENDING_LEGAL_IMPLEMENTATION`  
**Publication:** `PROHIBITED`  
**Checkout:** `NO_GO`

## 1. Governing correction

Student Basic and Student Plus have a minimum **user age of 16**.

This exact product-eligibility correction supersedes any active draft or planning language that:

- requires every Student user to be at least 18;
- excludes all users below 18 from Student plans; or
- treats Student user eligibility and authority to enter a recurring payment contract as the same question.

Historical source artifacts are not rewritten. This addendum governs active draft interpretation until counsel-approved replacement documents are merged.

## 2. Interim fail-closed contracting rule

The age-16 product rule does not establish that a person aged 16 or 17 may independently:

- conclude an open-ended recurring subscription;
- authorise recurring payment;
- act as the sole contracting party or invoice recipient;
- provide every legally required consent; or
- control withdrawal, cancellation, refund or complaint decisions where another person pays.

Until a signed, dated and version-specific Norwegian legal memorandum approves another exact model, Atlas must require a verified adult guardian or other adult contracting party and payer for a Student user aged 16–17.

## 3. Required legal decisions

Norwegian counsel must decide and provide exact approved Bokmål and English wording for:

1. whether a 16–17-year-old may be the named Student user;
2. whether and when that user may be a contracting party;
3. whether a guardian or other adult must be the contract holder and payer;
4. proportional, data-minimising age, identity, Student and guardian evidence;
5. recurring-payment authority and payment-method ownership;
6. division of notices and rights between user, contract holder and payer;
7. early commencement and withdrawal where user and payer differ;
8. cancellation, refund, complaint, chargeback and failed-payment handling;
9. privacy, retention, access, deletion and account recovery;
10. final terms, checkout, account, privacy and durable-confirmation copy.

## 4. Active draft replacement text

### Bokmål — section on eligibility

> Student Basic og Student Plus er beregnet for kvalifiserte brukere som er fylt 16 år. En bruker på 16 eller 17 år kan bare få en betalbar konto gjennom den kontrakts-, betalings- og vergeordningen som er godkjent for den aktuelle avtaleversjonen. Inntil en annen ordning er skriftlig godkjent av norsk juridisk rådgiver, skal en verifisert myndig verge eller annen myndig person være avtalepart og betaler. Studentstatus, alder og eventuell fullmakt skal kontrolleres med minst mulig personopplysninger og etter den godkjente personvern- og oppbevaringsregelen.

### English — eligibility section

> Student Basic and Student Plus are intended for eligible users aged 16 or older. A user aged 16 or 17 may receive a paid account only through the contracting, payment and guardian model approved for the applicable contract version. Until another model is approved in writing by Norwegian legal counsel, a verified adult guardian or other adult must be the contracting party and payer. Student status, age and any authority must be verified using the minimum personal data required under the approved privacy and retention rule.

These texts remain `PENDING_LEGAL_REVIEW` and may not be published.

## 5. Implementation controls

The release gate must deny ordering or activation where any applicable dependency is missing, including:

- user age below 16;
- unverified age or Student eligibility;
- user aged 16–17 without the approved adult/guardian contract-holder and payer route;
- missing contract-holder or payer identity;
- missing approved legal-copy version;
- missing consent or durable-medium evidence;
- missing privacy/retention configuration;
- missing legal or tax approval reference.

Required stable deny reasons include:

- `MINIMUM_AGE_NOT_MET`;
- `AGE_VERIFICATION_REQUIRED`;
- `STUDENT_ELIGIBILITY_MISSING`;
- `ADULT_CONTRACT_HOLDER_REQUIRED`;
- `GUARDIAN_OR_PAYER_AUTHORITY_MISSING`;
- `LEGAL_APPROVAL_MISSING`;
- `LEGAL_COPY_VERSION_MISSING`.

## 6. Wix status

As of this update:

- Members Area is installed and API-verified;
- Student minimum age 16 is recorded in `AtlasCustomerSegments` and `AtlasPricingContract`;
- the interim adult/guardian payer control is recorded;
- G04 and G22 are `PARTIAL`, not passed;
- Wix Pricing Plans count remains zero;
- `publicAllowed=false` and `purchaseAllowed=false` remain controlling.

## 7. Classification

- Minimum Student user age 16: `APPROVED`.
- Interim adult/guardian contract-holder and payer requirement: `AUTO_APPROVED` fail-closed control pending counsel.
- Independent contracting authority for users aged 16–17: `PENDING_LEGAL_REVIEW`.
- Public checkout and paid activation: `NO_GO`.
