# Atlas Workspace — Business, Security and Implementation Update

**Timestamp:** 18:54, 05.08.2026 Europe/Oslo  
**Project:** Atlas Website / Atlas AI  
**Classification:** `PENDING_REVIEW` unless an individual item is explicitly marked otherwise  
**Release state:** `NO_GO` — unchanged  
**Source report:** `Atlas Workspace: Secure AI Execution Interface (20:00, 05.08.2026)`  

## 1. Purpose

This controlled addendum integrates the Atlas Workspace research report into the current Atlas business, website, commercial, security and implementation baseline without treating research recommendations as approved architecture or implementation evidence.

## 2. Existing approved boundaries preserved

The following existing controls remain governing:

- Atlas-managed B2C API plans require hard usage caps and may not use retail-seat resale or pass-through.
- Wix remains the public website, CMS, plan, order, account and member-entry surface.
- Provider credentials, provider routing, authoritative entitlements, usage reservations, usage ledger, hard caps, reconciliation, protected state and audit controls remain external to Wix and client-side code.
- Customer-owned licence lanes, including approved Microsoft Copilot and Google Workspace Gemini configurations, execute in the customer/provider application rather than through an Atlas-managed provider credential.
- Managed Secure remains qualification and architecture-review only until its separate identity, storage, logging, revocation, backup, incident and acceptance evidence is approved.
- No frontend provider tokens, public write endpoint or unapproved production availability is permitted.

## 3. Proposed Workspace product model

**Proposed decision — `PENDING_REVIEW`:** Customers using Atlas-managed API-metered plans execute their AI tasks through an authenticated Atlas-owned Workspace. Wix remains the commercial, account and member-entry surface. The Workspace communicates only with the protected Atlas runtime; it does not call model providers directly from the browser.

The proposed minimum Workspace scope is:

1. authenticated user and organisation access;
2. Atlas-branded chat and controlled workflow interfaces;
3. permitted file upload with type, size, malware and policy checks;
4. project and conversation history under explicit retention controls;
5. result review, copy and approved export functions;
6. visible allowance, reservation, consumption and remaining-cap status;
7. fail-closed warnings and hard stops at entitlement or usage limits;
8. support and deletion-request entry points;
9. provider abstraction without exposing Atlas provider credentials;
10. accessible responsive UX aligned with the Atlas v4 website language and design system.

## 4. Recommended implementation boundary

**Security-first recommendation — `PENDING_REVIEW`:** Implement the Workspace as a separately deployed protected web application, preferably on a dedicated Atlas subdomain such as `app.atlas-ai.no`, integrated with Wix for purchase, membership/account entry and entitlement initiation.

### Wix responsibilities

- public pages, navigation, SEO and trust content;
- product and pricing presentation;
- checkout and order/member status where legally and technically approved;
- onboarding entry and links into the Workspace;
- non-authoritative usage summaries where safely synchronized;
- support and account-management entry points.

### Atlas Workspace responsibilities

- authenticated execution UI;
- workflow selection and task interaction;
- permitted upload, history, output review and export;
- usage and allowance presentation based on authoritative runtime state;
- safe error, limit, retention and deletion experiences.

### Secure Atlas runtime responsibilities

- CIAM/session validation and role/tenant authorization;
- entitlement resolution and fail-closed access decisions;
- request validation, policy enforcement and rate limiting;
- provider abstraction, routing and fallback policy;
- secrets vaulting and key rotation;
- usage reservation, metering, hard caps and reconciliation;
- tenant-isolated storage and encrypted file processing;
- append-only security, consent, usage and administrative audit records;
- deletion, revocation, incident and emergency provider kill-switch controls.

## 5. Security requirements

Security is the primary implementation criterion. The Workspace must not progress to pilot until evidence demonstrates:

- no provider or infrastructure secret is present in Wix, browser bundles, URLs, logs, screenshots or public documentation;
- strong CIAM with MFA for privileged roles, short-lived sessions, secure cookies and revocation;
- explicit tenant and object-level authorization on every protected operation;
- encrypted transit and storage with managed key control;
- server-side request validation, content policy controls, rate limits and abuse controls;
- upload quarantine, malware scanning, type verification, size limits and safe parsing;
- reservation-based metering and atomic hard-cap enforcement before provider execution;
- immutable or append-only audit evidence for security-relevant actions;
- retention schedules, user deletion workflows and backup-deletion handling;
- dependency, secret, infrastructure and container scanning in CI/CD;
- threat model, DPIA screening, incident runbook and external penetration testing;
- tested rollback, provider-disable and account-revocation procedures.

Special-category, confidential or regulated data remains prohibited unless a separately approved Managed Secure workflow and contract-bound control set exists.

## 6. Commercial and entitlement implications

No price or public plan is changed by this addendum. The Workspace requires future approval of:

- plan-to-entitlement mappings;
- normalized usage-unit definitions and customer-facing allowance wording;
- reservation, settlement, refund and failed-request treatment;
- boost/top-up rules and consumer-law presentation;
- provider-cost ceilings and margin alarms;
- cancellation, refund and account-deletion reconciliation across Wix, runtime and accounting;
- support access and administrative override controls.

The authoritative usage ledger and cap decision must remain in the secure runtime. Wix may display synchronized summaries but must not become the source of truth.

## 7. Website and UX integration

The existing Atlas website should introduce the Workspace only after architecture approval and UX validation. Required future website changes include:

- a secure sign-in/open-workspace entry;
- clear separation between Atlas-managed Workspace plans and customer-owned licence lanes;
- accurate allowance, data-use, provider and retention explanations;
- updated Trust, Privacy, Terms, Pricing, Onboarding and FAQ content;
- no claim that the Workspace, SSO, storage, provider routing or Managed Secure controls are live before validated evidence exists.

## 8. Documentation and implementation gaps

The following controlled artifacts are required before development and release approval:

1. Workspace product requirements document;
2. UX flows, information architecture and accessibility specification;
3. system context, container and data-flow diagrams;
4. formal Workspace architecture decision record;
5. CIAM and session architecture decision;
6. threat model and security control matrix;
7. provider-routing and provider-failure specification;
8. entitlement, reservation, metering and reconciliation specification;
9. upload and file-processing security specification;
10. data classification, retention, deletion and backup policy;
11. GDPR role assessment, processor register and DPIA screening/full DPIA as applicable;
12. observability, audit and incident-response specification;
13. test strategy, acceptance matrix, pilot controls and rollback plan;
14. support and privileged-administration procedures.

## 9. Controlled contradiction record

The source report presents a Wix Members/Velo-hosted MVP as one possible first phase. This is not adopted as governing architecture because it can be read more broadly than approved decision `ATL-DEC-20260725-014`. Any Wix-hosted interface may be considered only if it remains a thin, non-authoritative client and all protected execution, secrets, entitlements, metering, tenant state and audit functions remain external. The separately deployed Workspace is the preferred security-first option pending explicit approval.

## 10. Implementation sequence

1. **Decision and design:** approve Workspace boundary, CIAM, hosting, data classes and MVP scope.
2. **Security foundation:** threat model, DPIA screening, secrets, tenant authorization, ledger and upload controls.
3. **Non-public prototype:** synthetic/test data only; no public purchase or production provider credentials.
4. **Integrated staging:** Wix handoff, identity, entitlements, routing, metering, audit and deletion tests.
5. **Closed pilot:** named users, limited workflows, monitored caps and documented support/incident procedures.
6. **Release review:** independent security assessment, acceptance evidence and explicit written approval.

## 11. Current status

| Area | Status |
|---|---|
| Research report received | Complete |
| Source classification | Evidence/advisory; not architecture approval |
| Preferred architecture | `PENDING_REVIEW` |
| Workspace PRD and UX specification | Not created |
| Secure runtime implementation | Not implemented or validated |
| CIAM decision | Open |
| Threat model and DPIA | Open |
| Entitlement and usage runtime | Not implemented or validated |
| Pilot approval | `NO_GO` |
| Public release | `NO_GO` |

This file is an additive controlled update. It does not silently supersede approved Atlas decisions or activate any public, purchase or production capability.
