# Atlas AI Accountant / Tax-Adviser Memorandum

**Version:** `0.6.1-DRAFT`  
**Prepared:** 26.07.2026  
**Contracting company:** NanoTech Solutions Norway AS  
**Organisation number:** `925 367 869`  
**Norwegian MVA identifier:** `NO925367869MVA`  
**Management authorisation:** Ruben A. Meyer, CEO / daglig leder and chair of the board  
**Release:** `NO_GO`

> Ruben A. Meyer may authorise and sign management representations and the review request. The accountant or tax adviser must separately sign the professional tax/accounting conclusions. This document is not professional approval until that attestation is completed.

## 1. Operator prompt convention

- `PREFILLED_VERIFIED`: verified from an authoritative public register or official source.
- `APPROVED_OWNER_FACT`: explicitly confirmed by Ruben A. Meyer.
- `PENDING_OWNER_INPUT`: Ruben A. Meyer must complete or sign.
- `PENDING_PROFESSIONAL_INPUT`: accountant/tax adviser or named finance operator must complete.
- `PENDING_PROFESSIONAL_REVIEW`: professional decision and signature required.
- `PENDING_IMPLEMENTATION_EVIDENCE`: configuration or transaction evidence required.

## 2. Verified company and project facts

| Field | Prefilled value | State |
|---|---|---|
| Legal contracting entity | NanoTech Solutions Norway AS | `PREFILLED_VERIFIED` |
| Organisation number | `925 367 869` | `PREFILLED_VERIFIED` |
| MVA identifier | `NO925367869MVA` | `PREFILLED_VERIFIED` |
| MVA registration | Registered in the Norwegian Value Added Tax Register from 1 July 2020 | `PREFILLED_VERIFIED` |
| Registered address | Vestsideveien 279, 3648 Passebekk, Kongsberg, Norway | `PREFILLED_VERIFIED` |
| Organisation form | Aksjeselskap (AS) | `PREFILLED_VERIFIED` |
| Industry code | 71.129 Annen teknisk konsulentvirksomhet | `PREFILLED_VERIFIED` |
| Management/signature | Ruben André Meyer is CEO/daglig leder and chair; CEO or chair may sign individually | `PREFILLED_VERIFIED` |
| Atlas AI status | Internal department/business line of NanoTech Solutions Norway AS; not a separate legal entity | `APPROVED_OWNER_FACT` |
| Commercial contract | `0.5.1` | `APPROVED` |

## 3. Prefilled MVA/accounting working position

| Topic | Prefilled position | State |
|---|---|---|
| Contracting and invoice entity | NanoTech Solutions Norway AS | `PREFILLED_VERIFIED / PROFESSIONAL_CONFIRMATION_REQUIRED` |
| Invoice seller identifier | NanoTech Solutions Norway AS, org. no. `925 367 869 MVA` | `PREFILLED_WORKING_POSITION` |
| Domestic standard MVA rate | 25% | `OFFICIAL_RATE / OFFER_SIGNOFF_PENDING` |
| Norway B2C monthly digital subscriptions | 25% working baseline, gross price presentation | `PENDING_PROFESSIONAL_REVIEW` |
| Student-plan exemption | No education exemption is assumed merely because students are the target market | `PENDING_PROFESSIONAL_CONFIRMATION` |
| Norway B2B IT/consultancy/setup | 25% working baseline | `PENDING_OFFER_CLASSIFICATION` |
| Foreign provider/API/cloud/SaaS purchases | Vendor-by-vendor reverse-charge assessment required, normally using the applicable standard rate where taxable | `PENDING_PROFESSIONAL_REVIEW` |
| Foreign B2C | Blocked | `NO_OSS_OR_LOCAL_REGISTRATION_APPROVED` |
| Top-ups, annual and semester products | Blocked | `CLASSIFICATION_AND_TAX_POINT_PENDING` |
| Refunds and credit notes | Full and partial corrections must be approved and reconciled | `PENDING_PROFESSIONAL_REVIEW` |

The 25% rate is a controlled domestic planning baseline. It is not final treatment for every offer, customer, jurisdiction or billing/refund event.

## 4. Management representations and authorisation

| Field | Value/state |
|---|---|
| Authorising company | NanoTech Solutions Norway AS |
| Authorising person | Ruben A. Meyer |
| Role | CEO / daglig leder and chair of the board |
| Organisation number | `925 367 869` |
| MVA identifier | `NO925367869MVA` |
| Atlas AI organisational position | Internal department/business line of NanoTech Solutions Norway AS |
| Accounting system | `[[PENDING_PROFESSIONAL_INPUT — identify the production accounting system and legal accounting entity. Historical ledger/trial-balance evidence does not prove the current configuration.]]` |
| Bank/payment settlement entity | `[[PENDING_PROFESSIONAL_INPUT — enter bank-account owner, merchant entity and payment-provider settlement entity.]]` |
| MVA reporting owner | `[[PENDING_PROFESSIONAL_INPUT — identify preparer, reviewer, submitter and required Altinn authority.]]` |
| Accounting evidence cut-off | `[[PENDING_PROFESSIONAL_INPUT — latest reconciled period and source documents reviewed.]]` |
| Record-retention owner | `[[PENDING_PROFESSIONAL_INPUT — finance/privacy owner and retention schedule.]]` |

## 5. Professional decision schedule

| ID | Decision required | Professional response | Evidence/configuration reference |
|---|---|---|---|
| TAX-01 | Confirm NanoTech Solutions Norway AS as contracting, invoicing, credit-note and settlement entity; identify any exception. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-02 | Confirm 25% treatment and gross-price presentation for monthly Norway B2C Student Basic, Student Plus and Everyday Basic. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-03 | Confirm that student target status does not create an education exemption for the actual automated/digital supply. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-04 | Classify principal and ancillary components, setup, support, allowances and AI usage for every offer. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-05 | Determine tax point, periodisation and revenue recognition for monthly subscriptions and later approved products. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-06 | Approve full withdrawal, partial early-start, duplicate charge, statutory price reduction, chargeback and refund corrections. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-07 | Assign exact chart-of-accounts and MVA codes for revenue, output MVA, imported services, deferred revenue, refunds, clearing, chargebacks and future OSS. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-08 | Approve invoice, receipt and credit-note examples and required seller-identity format. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-09 | Configure foreign-provider reverse charge, deduction treatment, documentation and retention vendor by vendor. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |
| TAX-10 | Approve Wix/order/payment/refund, entitlement, invoice/credit note, accounting and MVA-return reconciliation, including exception owner and frequency. | `[[PENDING_PROFESSIONAL_REVIEW]]` | `[[PENDING_REFERENCE]]` |

## 6. Required approved examples

The professional reviewer must provide or approve examples for:

- Norwegian B2C monthly subscription receipt/invoice;
- full withdrawal refund and credit note;
- partial early-start refund and credit note;
- duplicate charge and chargeback correction;
- Norwegian B2B setup/project invoice if later included;
- foreign provider purchase and reverse-charge posting;
- Wix order/payment/refund to entitlement, accounting and MVA-return reconciliation.

## 7. Known invoice-control baseline

- seller identity should use NanoTech Solutions Norway AS;
- Norwegian sales documentation should show the organisation number followed by `MVA` when applicable;
- domestic consumer prices should be presented gross, including applicable MVA;
- service period, order/offer version and refund/credit-note linkage should be retained;
- foreign B2B, EU B2C/OSS, top-up and binding-period wording remains blocked until approved.

## 8. Management authorisation and factual representation

| Field | Value |
|---|---|
| Company | NanoTech Solutions Norway AS |
| Authorising signatory | Ruben A. Meyer |
| Role | CEO / daglig leder and chair of the board |
| Statement | I authorise this review request and confirm the management-supplied company and Atlas organisational facts to the best of my knowledge. |
| Signature | `[[PENDING_OWNER_INPUT — RUBEN A. MEYER SIGNATURE]]` |
| Date | `[[PENDING_OWNER_INPUT — DATE]]` |

This signature authorises the review and confirms management facts. It is not the accountant's or tax adviser's professional opinion.

## 9. Accountant/tax-adviser professional attestation

| Field | Required input |
|---|---|
| Reviewer | `[[PENDING_PROFESSIONAL_INPUT — NAME]]` |
| Firm/qualifications | `[[PENDING_PROFESSIONAL_INPUT]]` |
| Review date | `[[PENDING_PROFESSIONAL_INPUT]]` |
| Tax-law/guidance cut-off | `[[PENDING_PROFESSIONAL_INPUT — DATE AND SOURCES]]` |
| Covered release/doc versions | `[[PENDING_PROFESSIONAL_INPUT — EXACT REFERENCES]]` |
| Overall decision | `[[PENDING_PROFESSIONAL_DECISION — APPROVED / CONDITIONAL / NOT APPROVED]]` |
| Conditions and unresolved risks | `[[PENDING_PROFESSIONAL_INPUT]]` |
| Professional signature | `[[PENDING_PROFESSIONAL_SIGNATURE]]` |

The full professional memorandum should be stored privately in controlled Drive. GitHub should contain a sanitized approval record and exact covered-version references.
