# Atlas AI Non-Public Release Registry, Test Infrastructure and Hidden Plan Workflow

**Version:** `0.6.0-DRAFT`  
**Prepared:** 26.07.2026  
**Release:** `NO_GO`

> Planning only. No public plan, real payment, production entitlement or provider credential is authorized.

## Entry criteria

- signed legal memorandum covering Student minimum age 16 and exact legal-copy versions;
- signed MVA/accounting memorandum with exact Wix/payment/accounting configuration;
- signed owner launch-scope decision;
- architecture/security, legal, finance/payment and release-owner approval for the controlled test environment;
- explicit fail-closed deny rules for all excluded capabilities.

## Phase A — Immutable non-public release registry

- private immutable release-candidate ID;
- offer IDs, Student age 16+, jurisdictions, customer types, prices and allowances;
- legal-copy hashes and legal/tax/privacy/security/accessibility references;
- Wix app/configuration, payment, entitlement/runtime and test-run versions;
- `publicAllowed=false`, `purchaseAllowed=false`, `releaseApproved=false` by default;
- named approver and timestamp for every transition.

## Phase B — Test infrastructure

- non-discoverable allowlisted Wix test route;
- sandbox/test payment only;
- test offers distinct from commercial offers;
- no production provider credentials or entitlements;
- private CMS collections for release candidates, offer versions, legal-copy versions and sanitized evidence indexes;
- append-only consent, order-snapshot, entitlement, usage and cancellation/refund stores outside Wix where required;
- stable fail-closed reason codes and negative-path tests;
- explicit test-data retention/deletion.

## Phase C — Professional configuration decisions

- translate legal advice into exact copy, button text, consent controls, durable confirmation and refund rules;
- translate tax advice into price display, tax, invoice, credit-note and reconciliation configuration;
- bind every configuration to the professional decision and release candidate;
- reject any configuration that cannot be evidenced or conflicts with Wix limitations.

## Phase D — Hidden Wix test plans

- create only approved monthly test plans;
- hidden/private visibility and no public discovery or purchase;
- record Wix plan ID, revision, VAT-inclusive price, recurrence, benefits, cancellation rules and linked offer version;
- no Family, annual, semester, top-up or foreign-market plans;
- validate Members Area and My Subscriptions cancellation access;
- capture API readback and dashboard screenshots.

## Phase E — Acceptance testing

- eligible adult and counsel-approved 16–17 Student scenarios;
- under-16 denial and denial when payer/guardian controls are missing;
- unsupported jurisdiction, missing approval and version mismatch denial;
- payment success/failure, duplicate event and idempotency;
- durable-confirmation failure blocks activation;
- hard caps, no overage, no negative balance and concurrency-safe reset;
- cancellation, full withdrawal refund, partial early-start refund and accounting reconciliation;
- Bokmål/English, keyboard, screen-reader, focus, error and responsive tests;
- provider outage, rollback, monitoring and incident response.

## Prohibited until final GO

- public Pricing Plan visibility or purchase route;
- real-money charge;
- production provider credentials or customer provisioning;
- public write endpoint or frontend secret;
- Family/minor-below-16, annual, semester, top-up, foreign B2C or Managed Secure activation;
- changing release booleans without the final controlled release decision.
