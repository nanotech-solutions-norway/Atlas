# Atlas AI Wix Controlled Commerce Configuration and Validation — 12:18, 01.08.2026

## Control status

- **Project:** Atlas Website / Atlas AI
- **Wix site:** Atlas-AI
- **Site ID:** `1448ccad-68f0-43ea-8f0e-c9d8c0366082`
- **Wix engineering repository:** `nanotech-solutions-norway/atlas_wix`
- **Engineering merge:** PR #3 / commit `5e53cfe4b17a7a9bc6102b1cf01295ff20e2e9f3`
- **Configuration classification:** owner-authorised controlled implementation; verified implementation facts `AUTO_APPROVED`
- **Release state:** `NO_GO`
- **Locks:** `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`

## Authority applied

The implementation was constrained by:

1. the current explicit owner instruction to configure the listed Wix functions;
2. the canonical Atlas source hierarchy and safety locks;
3. pricing contract v0.5.1;
4. management-approved consumer-law memorandum v0.7.0;
5. source-reconciled MVA/accounting memorandum v0.8.0;
6. current authenticated Wix implementation evidence;
7. official Wix API method documentation.

No report recommendation, provider configuration, or Wix object was treated as public-release approval.

## Live Wix changes

### Hidden Pricing Plans

| Offer | Wix plan ID | Gross price | Allowance | Visibility | Buyable | Billing |
|---|---|---:|---|---|---|---|
| Student Basic | `46c6e99c-f86e-4893-b7c7-637a6f7ec539` | NOK 129 | 300 units / 6 boosts / 1 user | PRIVATE | false | monthly until cancelled |
| Student Plus | `a7f2bdd1-d8f0-4402-96a2-0bef4d9701bd` | NOK 169 | 500 units / 12 boosts / 1 user | PRIVATE | false | monthly until cancelled |
| Everyday Basic | `e6dc7dff-cb54-49c3-9064-5b9c2e5fa235` | NOK 159 | 400 units / 8 boosts / 1 user | PRIVATE | false | monthly until cancelled |

All three plans:

- use NOK;
- have revision `1`;
- are active only as hidden administrative test objects;
- have no free trial;
- allow buyer cancellation;
- limit purchase to one per member if later enabled;
- state hard caps and no automatic paid overage.

No Family, annual, semester, top-up, free-trial, foreign-B2C, business self-service, or Managed Secure plan was created.

### Members Area controls

The live Members Area remains installed. Three private custom fields were created:

| Field | ID | Key | Privacy |
|---|---|---|---|
| Atlas Age Band | `0ca7fe0e-7dbd-4675-8cff-66338ec015fa` | `custom.atlas-age-band-jfcczdrvhwewqgzlwosz` | PRIVATE |
| Atlas Contracting Model | `dc63bccb-b3f4-4d73-8cae-2936422b66d9` | `custom.atlas-contracting-model-xyimrvmhnld` | PRIVATE |
| Atlas Student Eligibility Status | `032bbe4b-3914-41ce-833b-c46311ff93ea` | `custom.atlas-student-eligibility-st-fbgjxo` | PRIVATE |

These fields record status values only. Identity-document upload through ordinary public forms remains prohibited.

### Pricing-contract evidence

The private `AtlasPricingContract` schema was extended with:

- `wixPlanRevision`;
- `wixPlanVisibility`;
- `wixPlanBuyable`;
- `wixPlanValidationStatus`.

The Student Basic, Student Plus and Everyday Basic records were bound to the new Wix plan IDs. Their exact plan status, management-policy status and remaining runtime acceptance requirements were recorded. `publicAllowed` and `purchaseAllowed` remained false on every record.

## Velo and GitHub controls

PR #3 in `atlas_wix` was validated by GitHub Actions and squash-merged.

Implemented controls:

- wildcard Velo web-method defaults changed to owner-only;
- site-member and anonymous wildcard invocation disabled;
- no public HTTP function or public write endpoint added;
- no payment credential, merchant identifier, bank detail, API key or provider token stored;
- fail-closed checkout policy module added;
- machine-readable commerce-control configuration added;
- automated plan, member, payment, checkout and release-lock validation added;
- CI updated to run repository, commerce and lint validation.

Even a fully formed internal checkout request is denied by the policy while any canonical release lock is false.

## Wix Payments correction and evidence boundary

The owner states that Wix Payments is configured for the Norway-registered Atlas-AI site. This is a direct correction to the older v0.8.0 working provider assessment that treated Wix Payments as unavailable for the site.

Controlling treatment:

- the current owner statement is recorded as `OWNER_CONFIRMED_CONFIGURED`;
- the obsolete provider-availability statement must not be used to reverse the current configuration;
- the current connector does not expose a reliable connected-provider/account readback for this site;
- no credentials or account identifiers were requested or stored;
- provider configuration does not prove transaction, refund, settlement, accounting or release acceptance.

The provider-policy contradiction is therefore closed for current configuration direction but remains `PENDING_REVIEW` for external provider-policy documentation and future memorandum revision.

## Checkout policy foundation

The controlled configuration preserves:

- Norway-only scope;
- monthly Student Basic, Student Plus and Everyday Basic only;
- Student minimum age 16;
- adult contracting payer for a named user aged 16–17;
- private age-band, contracting-model and student-eligibility statuses;
- total price including 25% MVA;
- monthly renewal and hard-cap disclosure;
- Bokmål and English payment-obligation wording;
- default activation after 14 calendar days;
- separate unselected request for immediate activation;
- durable confirmation before activation;
- full refund for a valid withdrawal within 14 days;
- no proportional-payment deduction for the initial scope;
- clear cancellation route and fallback contact route.

The actual checkout UI, consent capture, payment, entitlement and durable-confirmation sequence remains disabled and untested.

## Validation results

| Validation target | Result |
|---|---|
| Wix plan count | `PASS` — exactly 3 |
| Plan identity and revision | `PASS` |
| Gross prices | `PASS` — 129 / 169 / 159 NOK |
| Allowances | `PASS` |
| Currency and monthly billing | `PASS` |
| Visibility | `PASS` — all PRIVATE |
| Buyability | `PASS` — all false |
| Free trials | `PASS` — none |
| Cancellation capability | `PASS` — enabled |
| Member custom fields | `PASS` — 3 present and PRIVATE |
| Pricing-contract bindings | `PASS` |
| Public/purchase flags | `PASS` — false |
| Velo default permissions | `PASS` — owner-only |
| Automated GitHub validation | `PASS` — workflow run 5 |
| Payment-provider API readback | `NOT_AVAILABLE` |
| Sandbox payment/refund | `NOT_RUN` |
| Invoice/MVA/Conta reconciliation | `NOT_RUN` |
| Entitlement and usage ledger | `NOT_IMPLEMENTED` |
| Public checkout/release | `NO_GO` |

## Required next evidence

1. Dashboard evidence of the connected payment provider and enabled methods.
2. Non-production success, decline, cancellation and refund tests.
3. Durable confirmation, invoice, credit-note and settlement evidence.
4. Conta/MVA posting and gross-to-net reconciliation.
5. Member account, My Subscriptions and cancellation runtime tests.
6. Age-16–17 adult-payer and student-eligibility fail-closed tests.
7. External entitlement, usage-cap and reconciliation implementation.
8. Bokmål/English, accessibility, mobile and desktop acceptance.
9. Explicit signed release-candidate approval.

## Release effect

None.

```text
publicAllowed=false
purchaseAllowed=false
releaseApproved=false
NO_GO
```
