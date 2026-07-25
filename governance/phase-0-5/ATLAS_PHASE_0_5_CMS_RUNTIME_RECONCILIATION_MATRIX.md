# Atlas AI Phase 0.5 CMS/Runtime Reconciliation Matrix

**Project:** Atlas Website / Atlas AI  
**Created:** 12:10, 25.07.2026 Europe/Oslo  
**Classification:** Mixed — `AUTO_APPROVED` controls and verified structure; commercial, legal, provider and production values remain `PENDING_REVIEW`.  
**Release state:** `NO_GO`  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Target branch:** `agent/phase-0-5-contract-20260725`  
**Repository path:** `governance/phase-0-5/`  

> No file in this pack authorizes public sale, checkout activation, provider provisioning, paid entitlement, production routing or Managed Secure activation.

## Current-state evidence

- Wix CMS contains package and offer records, but they are release-locked.
- All G00–G22 release gates require evidence.
- No operative Wix Pricing Plans were evidenced in the current audit.
- No production entitlement, usage ledger or approved provider route exists.

| Plan/package identity | GitHub contract | Wix CMS | Checkout | Terms | Runtime | Current result | Blocking gates |
|---|---|---|---|---|---|---|---|
| business-executive-decision-support @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| business-commercial-growth @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| business-finance-operations @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| business-research-multi-engine @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| business-workspace-team-adoption @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| student-basic @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| student-plus @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| everyday-basic @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| family @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |
| managed-secure @ 0.5.0-draft | DEFINED | REQUIRES_ID_AND_VERSION_RECONCILIATION | ABSENT_OR_DISABLED | UNAPPROVED | rp-0.5-blocked-v1 | BLOCKED | G02/G03/G05/G06/G09/G21 |

## Exact reconciliation test

A plan may become purchasable only when `plan_id`, version, segment, price, MVA, billing period, named-user/shared-pool rules, allowance, premium-use definition, hard-cap/reset/overage rules, terms version, provider-disclosure version, routing-policy version, checkout IDs, entitlement mapping, ledger mapping, approval status and effective date match exactly. Any missing, stale or inconsistent value keeps `purchaseAllowed=false`.
