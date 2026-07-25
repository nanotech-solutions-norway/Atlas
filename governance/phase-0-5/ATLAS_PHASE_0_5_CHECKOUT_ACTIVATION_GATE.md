# Atlas AI Phase 0.5 Checkout Activation Gate

**Project:** Atlas Website / Atlas AI  
**Created:** 12:10, 25.07.2026 Europe/Oslo  
**Classification:** Mixed — `AUTO_APPROVED` controls and verified structure; commercial, legal, provider and production values remain `PENDING_REVIEW`.  
**Release state:** `NO_GO`  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Target branch:** `agent/phase-0-5-contract-20260725`  
**Repository path:** `governance/phase-0-5/`  

> No file in this pack authorizes public sale, checkout activation, provider provisioning, paid entitlement, production routing or Managed Secure activation.

## Default lock

```yaml
checkoutEnabled: false
purchaseAllowed: false
publicAllowed: false
topupsEnabled: false
```

## Blocking conditions

Checkout remains disabled when a plan is unapproved; lacks an effective date; has unapproved price/MVA/cancellation/refund treatment; lacks provider rights and delivery mode; has unapproved terms or provider disclosure; uses a non-production routing policy; lacks entitlement/ledger mappings; has not passed hard-cap/reset/concurrency tests; conflicts across CMS/checkout/terms/runtime; has any blocking G02/G03/G05/G06/G07/G08/G09/G21/G22 gate; or lacks explicit written activation approval.

## Current result

`NO_GO` — no plan may be purchased. Business and Managed Secure remain quote/qualification routes only.
