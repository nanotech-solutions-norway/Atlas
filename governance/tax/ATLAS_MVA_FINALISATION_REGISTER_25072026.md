# Atlas AI MVA Finalisation Register — 25.07.2026

**Project:** Atlas Website / Atlas AI  
**Prepared:** 20:33, 25.07.2026 Europe/Oslo  
**Commercial contract:** Phase 0.5 `v0.5.1`  
**Working domestic rate:** 25%  
**Final status:** `PENDING_ACCOUNTING_AND_TAX_REVIEW`  
**Release state:** `NO_GO`

## 1. Current validated working position

Official Norwegian Tax Administration guidance places software access and updates, hosting, online storage, automated remote teaching, IT services and consultancy within service categories normally subject to the standard 25% rate. This supports 25% as the working Norwegian rate for Atlas AI's domestic digital subscriptions, setup, consultancy and managed services.

This is not a final offer-by-offer or cross-border tax opinion. Each transaction must be classified by the actual supply, customer status, customer location, contractual bundle and billing/refund event.

## 2. Remaining finalisation requirements

| ID | Decision/evidence required | Scope | Current state | Required output | Approval owner |
|---|---|---|---|---|---|
| MVA-001 | Confirm the Atlas contracting legal entity, organisation number, MVA registration and invoice identity. | All offers | `PENDING` | Signed entity/invoice profile | Project owner + accountant |
| MVA-002 | Confirm 25% treatment for Norwegian B2C subscriptions, top-ups and premium boosts. | Student Basic, Student Plus, Everyday Basic, Family, top-ups | `WORKING_BASELINE` | Written offer-level tax opinion | Accountant/tax adviser |
| MVA-003 | Confirm 25% treatment for Norwegian B2B consultancy, setup, project and managed-service fees. | Business and managed offers | `WORKING_BASELINE` | Written offer-level tax opinion | Accountant/tax adviser |
| MVA-004 | Classify each offer as electronically supplied service, remotely deliverable service, consultancy, support, licence-related service or composite supply. | All offers | `PENDING` | Supply-classification register | Tax adviser |
| MVA-005 | Determine whether platform access, AI usage, onboarding, support, setup and provider costs are one principal supply or separate supplies. | Bundled offers | `PENDING` | Bundle/principal-supply memorandum | Tax adviser |
| MVA-006 | Confirm that Student plans do not qualify for education exemption merely because students are the target segment. | Student Basic and Plus | `PENDING` | Education-exemption analysis | Tax/legal adviser |
| MVA-007 | Define evidence and invoice treatment for foreign B2B customers and remotely deliverable exports. | EEA/EU/UK/non-EU B2B | `PENDING` | Customer-status/location and reverse-charge matrix | Tax adviser |
| MVA-008 | Determine destination-country VAT obligations for foreign B2C customers. | Non-Norwegian B2C | `PENDING` | Supported-country VAT matrix | Tax adviser |
| MVA-009 | Decide whether and where Atlas will register for non-Union OSS for EU consumer sales. | EU B2C | `PENDING` | OSS decision, registration owner and filing procedure | Project owner + tax adviser |
| MVA-010 | Define customer-location evidence and conflict resolution. | Cross-border B2C | `PENDING` | Evidence rules for billing address, payment method, IP/geolocation and exceptions | Tax/privacy adviser |
| MVA-011 | Classify standard top-ups and premium boosts: additional service, prepayment, single-purpose voucher, multi-purpose voucher or credit. | Top-ups/boosts | `PENDING` | Tax point and refund treatment | Tax adviser |
| MVA-012 | Confirm invoicing/tax-point treatment for monthly, annual and semester plans, including advance invoices up to one year where permitted. | Recurring plans | `PENDING` | Billing and periodisation rules | Accountant/tax adviser |
| MVA-013 | Determine treatment and timing for setup fees and milestone/project invoices. | B2B/managed | `PENDING` | Delivery milestone and invoice rule | Accountant |
| MVA-014 | Determine whether provider/API/cloud costs are Atlas's own cost, taxable recharge, separately supplied service or genuine disbursement as agent. | Provider costs | `PENDING` | Recharge/disbursement policy | Tax adviser |
| MVA-015 | Configure reverse-charge treatment for foreign API, software, hosting, cloud and consultancy purchases. | Provider/vendor AP | `PENDING` | Accounting codes and posting SOP | Accountant |
| MVA-016 | Define credit-note and VAT correction treatment for withdrawal, cancellation, duplicate billing, price reduction and refunds. | All consumer and business refunds | `PENDING` | Refund/credit-note matrix | Accountant/tax adviser |
| MVA-017 | Create exact Norwegian MVA, export, OSS and reverse-charge accounting codes and revenue accounts. | Accounting implementation | `PENDING` | Chart-of-accounts mapping | Accountant |
| MVA-018 | Approve invoice and credit-note wording for Norway, EU B2B reverse charge, EU B2C/OSS and other exports. | Billing documents | `PENDING` | Approved document examples | Accountant/legal adviser |
| MVA-019 | Map Wix offer, customer-country and customer-type fields to the correct tax result. | Wix checkout | `NOT_IMPLEMENTED` | Wix tax decision table and test evidence | Product owner + accountant |
| MVA-020 | Validate accounting reconciliation between Wix orders/refunds, invoicing, Norwegian MVA return and OSS return. | Finance control | `NOT_RUN` | End-to-end reconciliation test | Accountant/finance owner |

## 3. Offer-level working matrix

| Offer group | Norway B2C | Norway B2B | Foreign B2B | EU/EEA B2C | Current status |
|---|---|---|---|---|---|
| Consumer subscriptions | 25% working baseline; price displayed incl. MVA | N/A unless business purchase | Transaction-specific export/reverse-charge assessment | Destination-country VAT assessment and possible non-Union OSS | `PENDING_FINAL_REVIEW` |
| Top-ups and premium boosts | 25% working baseline; classification/tax point unresolved | Transaction-specific | Transaction-specific | Destination and voucher/prepayment analysis | `PENDING_FINAL_REVIEW` |
| Assessments, sprints and setup | 25% working baseline | 25% working baseline | Remotely deliverable/export rules and evidence | Rare B2C case requires destination analysis | `PENDING_FINAL_REVIEW` |
| Project packages | 25% working baseline | 25% working baseline | Export/reverse-charge and provider recharge analysis | Destination analysis | `PENDING_FINAL_REVIEW` |
| Managed Workflow Lite | 25% working baseline | 25% working baseline | Export/reverse-charge and service-location analysis | Destination analysis | `PENDING_FINAL_REVIEW` |
| Managed Secure | No self-service consumer sale | 25% working baseline for Norwegian customers | Contract and establishment-specific assessment | Not approved for consumer sale | `QUALIFICATION_ONLY` |

## 4. Minimum implementation evidence before checkout

1. Signed offer-by-offer tax position paper.
2. Approved Norway/EU/EEA/UK/non-EU customer matrix.
3. Approved non-Union OSS decision and filing owner.
4. Customer-status and location-evidence rules.
5. Wix tax configuration and test cases.
6. Approved invoice, credit-note and refund examples.
7. Imported-provider reverse-charge SOP.
8. Accounting code and reconciliation mapping.
9. End-to-end tests for purchase, renewal, cancellation, withdrawal, partial refund, full refund and chargeback.
10. Written accountant or tax-adviser sign-off.

## 5. Source basis

- Norwegian Tax Administration: standard 25% rate for software, hosting, automated online services, IT and consultancy categories.
- Norwegian Tax Administration: imported remotely deliverable services, including software, development, hosting, legal and consultancy, require transaction-specific reverse-charge assessment.
- Relevant Norwegian MVA Act provisions and the current MVA Handbook must be reviewed in the final signed position.

## 6. Control rule

The value `mvaRate=25%` may be used as a controlled planning and domestic-price-display assumption. It must not be represented as final tax treatment for every Atlas transaction. `publicAllowed`, `purchaseAllowed` and checkout remain false until MVA-001 through MVA-020 are resolved to the level applicable to the launch scope.
