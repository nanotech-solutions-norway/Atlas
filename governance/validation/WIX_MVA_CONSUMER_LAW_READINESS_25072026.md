# Wix MVA and Consumer-Law Readiness Validation — 25.07.2026

**Site:** Atlas-AI — `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Collection:** `AtlasPricingContract`  
**Contract version:** `0.5.1`  
**Collection access:** Admin/CMS-editor only  
**Release state:** `NO_GO`

## Schema update

The following private readiness fields were added:

- `mvaWorkingRatePct`
- `mvaStatus`
- `mvaRegisterRef`
- `consumerLawStatus`
- `consumerLawResearchStatus`
- `consumerLawPromptRef`
- `checkoutLegalStatus`
- `professionalSignoffRequired`

## Record update

All 13 commercial offer records were patched without changing approved prices, allowances, delivery modes or activation classifications.

### Consumer subscriptions

Student Basic, Student Plus and Everyday Basic now record:

- `mvaWorkingRatePct=25`
- `mvaStatus=PENDING_ACCOUNTING_AND_TAX_REVIEW`
- `consumerLawStatus=PENDING_LEGAL_REVIEW`
- `consumerLawResearchStatus=MANDATE_CREATED_NOT_EXECUTED`
- `checkoutLegalStatus=NO_GO`
- `professionalSignoffRequired=true`

Family uses the same controls with an additional Family-control review state.

### Business offers

Business offers now record:

- domestic 25% working rate;
- final MVA treatment pending;
- B2B contract review pending;
- quote-controlled, no self-service checkout;
- professional sign-off required.

### Managed offers

- Managed Workflow Lite remains blocked by metering, tax and managed-service contract gates.
- Managed Secure Standard and Enterprise remain qualification-only with no checkout and pending tax/secure-contract approval.

## Readback result

| Check | Result |
|---|---|
| Total pricing-contract records | `PASS` — 13 |
| Contract version | `PASS` — all `0.5.1` |
| MVA working rate | `PASS` — 25 recorded as working baseline |
| Final MVA status | `PASS` — pending professional review |
| Consumer research status | `PASS` — mandate created/not executed for B2C |
| Consumer checkout status | `PASS` — `NO_GO` for B2C |
| Professional sign-off required | `PASS` — true for all records |
| `publicAllowed` | `PASS` — false for all 13 |
| `purchaseAllowed` | `PASS` — false for all 13 |
| Approved prices/allowances preserved | `PASS` |
| Wix Pricing Plans | `PASS_EXPECTED_LOCK` — count 0 |
| Checkout or production activation | `NOT_PERFORMED` |

## Classification

- `AUTO_APPROVED`: private schema/status update and verified preservation of locks.
- `PENDING_REVIEW`: final MVA treatment, legal conclusions, contract text, Wix checkout implementation and release approval.

## Next executable workstream

Execute the consumer-law deep research mandate and prepare the complete Bokmål/English legal implementation pack. In parallel, obtain accountant/tax-adviser approval for the launch-country and offer-level MVA matrix.
