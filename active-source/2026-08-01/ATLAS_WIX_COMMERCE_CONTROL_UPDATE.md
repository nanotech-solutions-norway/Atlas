# Atlas AI Wix Commerce Control Update — 12:18, 01.08.2026

**Classification:** owner-authorised controlled implementation; verified facts `AUTO_APPROVED`; provider-policy reconciliation `PENDING_REVIEW`  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`

## Current controlled state

- Wix Payments configuration is owner-confirmed for the Norway-registered Atlas-AI site.
- Three approved monthly Pricing Plans now exist as private, non-buyable administrative test objects:
  - Student Basic — NOK 129;
  - Student Plus — NOK 169;
  - Everyday Basic — NOK 159.
- Members Area is installed and has private age-band, contracting-model and student-eligibility status fields.
- The private `AtlasPricingContract` binds all three Wix plan IDs and preserves public/purchase locks.
- Velo backend wildcard permissions are owner-only.
- The checkout policy is implemented as a fail-closed code foundation and cannot approve purchase while the canonical locks remain false.
- GitHub Actions validation passed before the Velo configuration was merged.

## Controlling boundaries

This update authorises planning, hidden-object configuration, private member metadata, fail-closed code and validation only.

It does not authorise:

- public plan visibility;
- public checkout;
- real-money production charging;
- production entitlement;
- Family, annual, semester, top-up or foreign-B2C offers;
- public write endpoints;
- frontend provider credentials;
- Managed Secure activation;
- Wix publication.

## Provider contradiction

The owner-confirmed Wix Payments configuration is newer implementation evidence than the earlier provider-availability working assumption in MVA memorandum v0.8.0. Do not silently rewrite the memorandum; prepare a future versioned reconciliation. Provider connection alone does not prove payment, refund, settlement, tax, accounting or release acceptance.

## Next executable workstream

Complete non-production payment, refund, durable-confirmation, cancellation, invoice, credit-note, MVA/Conta, entitlement, usage-cap and member-eligibility acceptance evidence while preserving all release locks.
