# Atlas AI Phase-by-Phase Implementation Guide — 11:35, 11.07.2026

> **Control status:** Recommended consolidated working baseline. Commercial pricing, provider-delivery rights, legal interpretation, public availability, production routing and site identity remain approval-gated where identified as PENDING_REVIEW.

> **Execution boundary:** No Wix publication, Gamma editing, Azure deployment, subscription activation or production change was performed.

## Program rule

A phase is complete only when its exit criteria are evidenced, tested against the relevant release profile and signed by the designated owner. The existence of pages, code or configuration is not evidence of operational readiness.

## Integrated dependency sequence

| Phase | Objective | Main output | Blocking dependency |
|---|---|---|---|
| 0 | Architecture, source authority and route lock | Approved operating model, route map, claims and data boundaries | None |
| 0.5 | Product and commercial object contract | Versioned plan/package records and CMS/runtime schema | Phase 0 |
| 1 | Public commercial shell and early access | Canonical bilingual website with checkout disabled | Phase 0 and 0.5 |
| 2 | Account, portal and structured handoff | Identity, role, plan, intake and customer-status layer | Phase 0.5 |
| 3 | Entitlement, usage and routing control plane | Provider routing, ledger, caps, reset and reconciliation | Phase 2 |
| 4 | Pilot and Managed Secure MVP | One evidenced pilot and one qualified secure journey | Phase 3 where runtime applies |
| 5 | Productization and optimization | Repeatable content, delivery, analytics and support operations | Stable Phase 1-4 workflows |
| 6 | Security, privacy, incident and final acceptance | Cross-cutting hardening and release approval | Runs throughout; closes last |

## Phase 0 — Architecture, governance and canonical route lock

### Implementation actions

1. Create a source register with version, date, authority and approval status.
2. Approve the governed solution-layer positioning.
3. Verify canonical Wix site identity and deployment destination.
4. Approve canonical audience routes and the legacy redirect matrix.
5. Lock the Wix/GitHub/Azure/Gamma role separation.
6. Define public-form data classes and secure escalation triggers.
7. Create claims, decision, error, validation and session-close registers.
8. Preserve Atlas safety locks and repository secret boundaries.

### Exit criteria

- No unresolved contradiction in route, positioning or system-of-record responsibilities.
- Current source hierarchy is documented.
- Pricing/provider/availability items are visibly PENDING_REVIEW.
- No public or frontend surface is designated as a secure system of record.

## Phase 0.5 — Product, pricing and CMS/runtime contract

### Required objects

- Business package records
- Student Basic
- Student Plus
- Everyday Basic
- Family
- Managed Secure quote-only record
- provider capability classes
- routing policy versions
- terms and disclosure references

### Minimum fields

| Group | Required fields |
|---|---|
| Identity | `plan_id`, `version`, `segment`, `status`, `effective_date` |
| Commercial | gross price, net price, MVA treatment, billing period, cancellation/refund rule |
| Entitlement | capability classes, allowance unit, premium-use unit, named-user limit, shared-pool rule |
| Control | hard cap, warnings, reset, rollover, overage, downgrade, suspension |
| Governance | terms version, provider disclosure, claim references, owner, approval status |
| Runtime | routing policy, meter unit, fallback, outage behavior, ledger mapping |

### Exit criteria

- The public plan matrix, checkout object, terms and runtime configuration reconcile exactly.
- Delayed or unapproved plans cannot be purchased.
- No plan promises “unlimited” use or a permanent model version.
- Provider commercial rights and delivery mechanism are documented.

## Phase 1 — Public commercial shell and early access

### Build scope

- Home
- Solutions
- Business
- Students
- Consumers
- Managed Secure
- Pricing
- Trust
- Platform Lanes
- Onboarding
- Resources
- About
- Contact
- Legal

### Execution controls

- Bokmål root and English `/en/` parity.
- Canonical self-references and reciprocal hreflang.
- All CTAs point to approved routes.
- Public forms include no-confidential-upload notice.
- Checkout disabled.
- Managed Secure status limited to qualification/architecture review.
- Claims linked to approved evidence.
- Mobile, keyboard and screen-reader journeys validated to WCAG 2.2 AA target.

### Exit criteria

- Early-access gate PASS.
- No obsolete route remains in navigation, CMS, Gamma or metadata.
- No paid or secure-delivery promise is implied.
- Content, pricing proposal, provider disclosure and legal summaries are version-aligned.

## Phase 2 — Identity, portal and structured handoff

### Components

- Verified account identity and session lifecycle
- Account owner/member roles
- Plan state and entitlement request
- Family invitations/removal
- Low-risk intake classification
- Customer status portal
- Cancellation and data-request links
- Secure-escalation trigger without public file upload

### Blocking tests

- Duplicate identity
- session revocation
- unauthorized plan view
- family member limit
- wrong-plan provisioning
- stale billing state
- secure-required request blocked from ordinary intake

## Phase 3 — Entitlement, usage, routing and reconciliation

### Required control plane

1. Idempotent billing-event ingestion.
2. Exactly-once entitlement state transition.
3. Normalized usage ledger.
4. Provider event reconciliation.
5. Hard caps under concurrency.
6. Monthly reset with timezone and retry rules.
7. Premium-use unit decrement.
8. Cost alerts and suspension thresholds.
9. Provider outage and fallback policy.
10. Immutable audit references without customer prompt content.

### Exit criteria

- No entitlement bypass.
- Ledger balance reconciles to provider/accounting events within defined tolerance.
- Hard caps cannot be bypassed by parallel requests.
- No silent chargeable overage.
- The customer portal and internal ledger show consistent status.

## Phase 4 — Pilot validation and Managed Secure MVP

### Subscription pilot

- Small invited cohort
- support burden measurement
- cost per active user
- p50/p95 usage
- provider mix
- refund/cancellation outcomes
- abuse and cap events
- cohort conversion and retention

### Managed Secure minimum viable journey

- qualified architecture review
- authenticated invitation
- private storage
- malware/quarantine treatment where files are accepted
- least-privilege access
- audit logging
- retention and deletion
- revocation
- backup/restore test
- incident workflow

### Exit criteria

No scale decision until economics and support fit the approved envelope. No secure claim until the tested journey matches public wording.

## Phase 5 — Productization, automation and optimization

- Governed CMS publishing workflow
- bilingual drift checks
- automated schema/link/claim/secret checks
- analytics event taxonomy
- pricing and provider review calendar
- support knowledge base
- release tags and rollback records
- quarterly claim and vendor review
- package finder and lane comparison only after manual flows stabilize

## Phase 6 — Security, privacy, incident and final acceptance

### Cross-cutting controls

- MFA/passkeys and least privilege
- branch protection and secret scanning
- no frontend tokens
- data inventory and retention
- provider disclosure
- DPIA/legitimate-interest/legal review triggers
- incident classification, containment, communication and recovery
- accessibility and performance
- vulnerability/dependency review
- backup/restore
- production smoke test and rollback

### Final exit criteria

- No open P0/P1 defect.
- No exposed secret or customer-sensitive evidence.
- Current legal/terms/provider documents approved.
- Relevant launch profile gates pass.
- Rollback and incident owners acknowledge readiness.
- Production release has explicit written approval.

## Recommended cadence

| Period | Primary work |
|---|---|
| Days 1-5 | Phase 0 and site-identity resolution |
| Days 6-10 | Phase 0.5 product/CMS contract |
| Days 11-20 | Phase 1 staging and early-access validation |
| Weeks 4-8 | Phase 2-3 subscription control plane |
| Weeks 8-12 | Controlled pilot and economics |
| After pilot | Paid launch decision and selective Managed Secure activation |

## Evidence structure

Use sanitized evidence under versioned release folders: source register, route tests, content export, legal versions, screenshots, machine-readable authorization tests, billing/ledger test results, security scans, accessibility tests, monitoring and sign-off.

## Source basis

This guide supersedes the separate June Phase 0-6 website-strategy files as the active execution plan while retaining them as historical evidence.
