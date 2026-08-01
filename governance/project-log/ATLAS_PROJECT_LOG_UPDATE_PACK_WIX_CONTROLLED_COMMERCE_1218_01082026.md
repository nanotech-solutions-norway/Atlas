# ATLAS PROJECT LOG UPDATE PACK — Wix Controlled Commerce Foundation

**Timestamp:** 12:18, 01.08.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Task:** Configure Wix payments/member/checkout/package foundations under current Atlas controls  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`

## Issue or change observed

The site owner confirmed that Wix Payments is now configured for the Norway-registered Atlas-AI site. Existing controlled records still reflected an older provider-availability assessment and a pre-implementation state with zero Pricing Plans and incomplete member-control metadata.

The Velo engineering repository also retained permissive wildcard backend defaults that allowed anonymous and site-member invocation, even though no current web methods existed.

## Root cause

- The provider assessment was a point-in-time capability finding and had not been refreshed after owner-side Wix configuration.
- Non-public plan creation had previously been deferred until the consumer-law and MVA management policies were approved.
- Members Area installation had occurred after earlier records were written, but plan-specific age/payer/eligibility fields had not been created.
- The Wix-generated repository permission template used permissive defaults unsuitable for future Atlas backend methods.

## Corrective rule

- Treat the current explicit owner correction and authenticated Wix implementation as controlling for current site configuration.
- Do not infer public, purchase or release approval from provider configuration.
- Create only the three management-approved Norway-only monthly plans as `PRIVATE` and `buyable=false`.
- Store member eligibility controls as private status fields and prohibit ordinary identity-document upload.
- Default all future Velo web methods to owner-only unless a separately reviewed method-specific permission is approved.
- Require automated checks to fail when a plan becomes public/buyable or when any release lock changes without review.

## Evidence and sources

- current explicit owner instruction dated 01.08.2026;
- canonical Atlas decisions and safety locks;
- management consumer-law memorandum v0.7.0;
- management MVA/accounting memorandum v0.8.0;
- pricing contract v0.5.1;
- authenticated Wix API plan, CMS and member-field readback;
- `nanotech-solutions-norway/atlas_wix` PR #3 and successful GitHub Actions workflow run 5.

## Actions taken

1. Created three hidden, non-buyable monthly Wix Pricing Plans:
   - Student Basic — `46c6e99c-f86e-4893-b7c7-637a6f7ec539`;
   - Student Plus — `a7f2bdd1-d8f0-4402-96a2-0bef4d9701bd`;
   - Everyday Basic — `e6dc7dff-cb54-49c3-9064-5b9c2e5fa235`.
2. Created three private Members Area custom fields for age band, contracting model and student eligibility.
3. Extended the private pricing-contract schema with plan revision, visibility, buyability and validation fields.
4. Bound and validated the three Wix plan objects against the approved pricing records.
5. Preserved `publicAllowed=false` and `purchaseAllowed=false` on all controlled offer records.
6. Changed Velo wildcard backend permissions to owner-only.
7. Added fail-closed checkout policy and automated commerce validation.
8. Validated the engineering branch through GitHub Actions and merged PR #3 at `5e53cfe4b17a7a9bc6102b1cf01295ff20e2e9f3`.
9. Added the full controlled configuration and validation report to the canonical Atlas repository.

## Validation summary

- exactly 3 Wix Pricing Plans: `PASS`;
- all plans private and non-buyable: `PASS`;
- exact prices, allowances, currency and monthly recurrence: `PASS`;
- three private member fields: `PASS`;
- CMS plan bindings and locks: `PASS`;
- owner-only Velo defaults: `PASS`;
- repository commerce validation and lint: `PASS`;
- payment-provider connected-account API readback: `NOT_AVAILABLE`;
- sandbox payment/refund, settlement, invoice, MVA/Conta and entitlement reconciliation: `NOT_RUN`;
- public release: `NO_GO`.

## Contradiction handling

The older MVA memorandum working assessment stated that Wix Payments was unavailable for a Norway-based business. The owner now confirms actual site configuration. The configuration direction is updated accordingly, but the memorandum text is not silently rewritten in this task. A future versioned source reconciliation should update the provider section and distinguish provider availability, actual connection, transaction validation and release approval.

## Unresolved items

- payment-provider dashboard evidence and enabled-method readback;
- sandbox transaction, decline, refund and settlement evidence;
- exact checkout UI, consent and durable-confirmation implementation;
- cancellation and member-portal runtime testing;
- invoice, credit-note, Conta and MVA reconciliation;
- external entitlement and usage-cap services;
- age/payer/student-eligibility runtime enforcement;
- bilingual/accessibility/responsive/end-to-end acceptance;
- explicit release-candidate approval.

## Classification

- owner instruction to perform controlled non-public configuration: `APPROVED`;
- exact Wix/GitHub implementation and validation facts: `AUTO_APPROVED`;
- current provider-policy contradiction and memorandum amendment: `PENDING_REVIEW`;
- payment activation, real-money production charging and release: `PENDING_REVIEW / NO_GO`.
