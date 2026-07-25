# Atlas AI Wix Phase Responsibility Matrix — 25.07.2026

**Site:** Atlas-AI — `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**State:** Draft / `NO_GO`  
**Editor:** Wix Studio; Velo enabled  
**Current app evidence:** Forms, Forms & Payments, Invoices, Multilingual, Pricing Plans and SEO installed; Members Area not installed.  
**Current Pricing Plans count:** 0.

## Responsibility map

| Phase | Wix execution / implementation | External or canonical execution | Current Wix evidence | Status |
|---|---|---|---|---|
| 0 | Site identity, Studio routes/pages, CMS reference records, public-form boundary, multilingual configuration and release locks | GitHub source authority, decisions, claims, route and architecture governance | Site and CMS exist; Studio page evidence partial | `PARTIAL` |
| 0.5 | Private pricing-contract CMS, package/offer display fields, Pricing Plans objects, plan visibility, recurring/annual billing object, checkout/order UI, cancellation/pause interface and tax configuration | Provider rights, API accounts, routing policy, normalized usage ledger, hard caps, boost settlement and provider reconciliation | 14 packages, 7 historical offers, 0 Pricing Plans | `PARTIAL / BLOCKED` |
| 1 | Fourteen public page roles, navigation, responsive Studio implementation, bilingual copy, forms, CMS bindings, SEO metadata, consent and accessibility implementation | Canonical copy/claims and release evidence in GitHub/Drive | 13 visible pages previously evidenced; Contact gap; release locks active | `PARTIAL` |
| 2 | Members Area registration/login, member lifecycle, account/profile, Pricing Plans order display, ordinary intake, cancellation/data-request links and portal UI | Atlas RBAC authority, Family invitation/limit logic, secure escalation and entitlement authority | Members Area not installed | `NOT_IMPLEMENTED` |
| 3 | Billing/order events as an input, member plan/status display, gated portal surfaces and customer-facing balance/status readout | Idempotent ingestion, exactly-once entitlement transition, usage ledger, caps, reset, routing, cost alerts and audit | No plans or orders; no ledger evidence | `NOT_IMPLEMENTED` |
| 4 | Qualification and architecture-review forms, invite/portal front end and public status/claims | Private storage, malware/quarantine, least privilege, logging, retention, revocation, restore and incident controls | Low-risk qualification only | `PLANNED` |
| 5 | CMS publishing workflow, resources/help content, Wix Analytics, forms/automations and multilingual content operations | CI drift checks, schema/link/claim/secret validation, release tags, rollback evidence and provider review | CMS base exists | `PARTIAL / PLANNED` |
| 6 | Cookie/consent implementation, privacy notices, accessibility/performance remediation, account configuration and production smoke surface | MFA/passkeys where required, secrets, vulnerability review, data inventory, incident tabletop, backup/restore and final release sign-off | Draft legal/trust content; no final acceptance | `NO_GO` |

## Wix-specific conclusions

1. Wix Pricing Plans is suitable for commercial plan definitions, visibility, recurring/annual billing and order lifecycle.
2. Wix Members Area is required before Wix can own account/profile and member plan views; it is currently absent.
3. Wix CMS is suitable for the locked product/price contract and public content, but it is schemaless and cannot replace canonical contract validation.
4. Site-level tax must be configured and independently checked.
5. Wix is not the authoritative cross-provider cost/usage ledger.
6. Hard caps, premium boosts and provider reconciliation require a controlled backend.
7. Managed Secure is not a Wix-only implementation.
