# Atlas AI MVA Finalisation Register — Updated 02:06, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Commercial contract:** Phase 0.5 `v0.5.1`  
**Working domestic rate:** 25%  
**Research/implementation package:** `CREATED`  
**Final status:** `PENDING_ACCOUNTING_AND_TAX_REVIEW`  
**Release state:** `NO_GO`

## 1. Current validated working position

Official Norwegian Tax Administration guidance supports 25% as the controlled working Norwegian rate for Atlas AI's domestic digital subscriptions, setup, consultancy and managed services. The working baseline is not a final offer-by-offer or cross-border tax opinion. Each transaction must be classified by actual supply, customer status, location, contractual bundle and billing/refund event.

The implementation and professional-review package now provides decision frameworks, draft matrices, invoice/credit-note requirements, a Wix tax decision table and a reconciliation test plan. It does not close any gate requiring signed advice, configured accounts or executed tests.

## 2. Finalisation requirements

| ID | Decision/evidence required | Current state after research package | Required professional output | Approval owner |
|---|---|---|---|---|
| MVA-001 | Contracting entity, organisation number, MVA registration and invoice identity | Entity template created; values unresolved | Signed entity/invoice profile | Project owner + accountant |
| MVA-002 | 25% treatment for Norwegian B2C subscriptions, top-ups and premium boosts | Working position documented; top-ups unresolved | Written offer-level tax opinion | Accountant/tax adviser |
| MVA-003 | 25% treatment for Norwegian B2B consultancy, setup, project and managed fees | Working position documented | Written offer-level tax opinion | Accountant/tax adviser |
| MVA-004 | Supply classification for every offer | Draft classification matrix created | Approved classification register | Tax adviser |
| MVA-005 | Principal supply or separate supplies | Decision framework and working recommendations created | Bundle memorandum | Tax adviser |
| MVA-006 | Student-plan education exemption | Research position: target segment alone does not establish exemption | Signed exemption analysis | Tax/legal adviser |
| MVA-007 | Foreign B2B status, location and invoice evidence | Evidence matrix and block rules created | Approved B2B/export matrix | Tax adviser |
| MVA-008 | Foreign B2C destination obligations | Launch-country matrix created; all foreign B2C blocked | Supported-country VAT matrix | Tax adviser |
| MVA-009 | Non-Union OSS decision | Decision framework created; no registration approval | OSS decision, owner and procedure | Project owner + tax adviser |
| MVA-010 | Consumer-location evidence and conflicts | Candidate evidence and conflict rules created | Approved tax/privacy rules | Tax/privacy adviser |
| MVA-011 | Top-up/boost classification | Fixed-service-entitlement recommendation created | Tax point and refund treatment | Tax adviser |
| MVA-012 | Monthly, annual and semester timing | Billing-event table created | Billing and periodisation rules | Accountant/tax adviser |
| MVA-013 | Setup fees and milestones | Delivery/invoice event framework created | Milestone/invoice rule | Accountant |
| MVA-014 | Provider/API/cloud costs | Own-cost/recharge/disbursement decision tree created | Recharge/disbursement policy | Tax adviser |
| MVA-015 | Reverse charge on foreign purchases | Monthly SOP and controls created | Exact codes and approved posting SOP | Accountant |
| MVA-016 | Credit-note/MVA corrections | Trigger and correction matrix created | Approved calculations/postings | Accountant/tax adviser |
| MVA-017 | Accounting and revenue codes | Functional mapping created without invented account numbers | Exact chart-of-accounts mapping | Accountant |
| MVA-018 | Invoice and credit-note wording | Required-field examples created | Approved document examples | Accountant/legal adviser |
| MVA-019 | Wix customer/offer/jurisdiction decision table | Design created; configuration absent | Configured logic and test evidence | Product owner + accountant |
| MVA-020 | Wix/payment/accounting/MVA/OSS reconciliation | Detailed test plan created; not executed | End-to-end signed test | Accountant/finance owner |

## 3. Offer-level working matrix

| Offer group | Norway B2C | Norway B2B | Foreign B2B | EU/EEA B2C | Current status |
|---|---|---|---|---|---|
| Consumer subscriptions | 25% working baseline; price displayed incl. MVA | N/A unless business purchase | Transaction-specific status/place assessment | Destination-country VAT and possible non-Union OSS | `PENDING_FINAL_REVIEW` |
| Top-ups and premium boosts | 25% working baseline; tax point unresolved | Transaction-specific | Transaction-specific | Destination and prepayment/voucher analysis | `PENDING_FINAL_REVIEW` |
| Assessments, sprints and setup | 25% working baseline | 25% working baseline | Export/place-of-supply evidence | Rare B2C destination analysis | `PENDING_FINAL_REVIEW` |
| Project packages | 25% working baseline | 25% working baseline | Export/reverse-charge and recharge analysis | Destination analysis | `PENDING_FINAL_REVIEW` |
| Managed Workflow Lite | 25% working baseline | 25% working baseline | Export/place and recurring-service analysis | Destination analysis | `PENDING_FINAL_REVIEW` |
| Managed Secure | No consumer self-service sale | 25% working baseline | Contract/establishment-specific | Not approved for consumer sale | `QUALIFICATION_ONLY` |

## 4. Controlled launch recommendation

- Initial self-service scope: Norway consumer only, after all applicable professional and implementation gates pass.
- Norway business: quote-controlled until signed tax and contract treatment exists.
- Foreign B2B: quote-controlled and blocked from final tax treatment without business/status/location evidence.
- EU/EEA and other foreign B2C: disabled until destination VAT and OSS/local registration decisions are approved.
- Top-ups/boosts: disabled until tax point, refund and accounting treatment is approved.

## 5. Controlled research output

`governance/tax/ATLAS_MVA_IMPLEMENTATION_AND_PROFESSIONAL_REVIEW_PACK_0206_26072026.md`

The pack contains:

1. offer and bundle classifications;
2. MVA-001–MVA-020 review outputs;
3. launch-country and customer-evidence matrices;
4. non-Union OSS decision framework;
5. top-up/boost analysis;
6. billing/tax-point and periodisation table;
7. imported-service reverse-charge SOP;
8. provider-cost/recharge decision tree;
9. functional accounting mapping;
10. invoice/credit-note examples;
11. Wix tax decision table;
12. reconciliation design and test scenarios.

## 6. Minimum evidence before checkout

1. Signed entity/invoice profile.
2. Signed offer-by-offer tax position.
3. Approved launch-country matrix.
4. Approved OSS decision where relevant.
5. Approved customer-status/location rules.
6. Exact accounting and MVA codes.
7. Approved invoice, credit-note and refund examples.
8. Implemented Wix/custom tax decision logic.
9. Imported-provider reverse-charge implementation.
10. Passed purchase, renewal, cancellation, withdrawal, partial/full refund, chargeback and reconciliation tests.
11. Written accountant/tax-adviser sign-off.

## 7. Control rule

The value `mvaRate=25%` may be used only as a controlled planning and domestic-price-display assumption. It must not be represented as final tax treatment for every Atlas transaction. `publicAllowed`, `purchaseAllowed` and checkout remain false until the MVA gates applicable to the approved launch scope are professionally resolved, implemented and tested.