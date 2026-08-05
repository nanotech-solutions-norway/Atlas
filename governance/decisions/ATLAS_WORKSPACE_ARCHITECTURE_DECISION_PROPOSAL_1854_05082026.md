# Atlas Workspace Architecture Decision Proposal

**Timestamp:** 18:54, 05.08.2026 Europe/Oslo  
**Decision ID:** `ATL-DEC-20260805-034`  
**Status:** `PENDING_REVIEW`  
**Owner:** Ruben A. Meyer / Atlas architecture and security owners  
**Release effect:** None. `publicAllowed=false`, `purchaseAllowed=false`, production activation remains prohibited.

## Proposed decision

For all Atlas-managed API-metered plans, customers shall execute AI tasks through an authenticated Atlas-owned Workspace. Wix shall remain the public, commercial, account and member-entry surface. Provider applications shall be used only for explicitly defined customer-owned licence lanes. Provider credentials, routing, authoritative entitlements, usage reservations, usage metering, hard caps, protected state and audit functions shall remain server-side in the secure Atlas runtime.

The preferred deployment is a separately deployed protected web application on an Atlas-controlled subdomain, integrated with Wix through a controlled identity and entitlement handoff.

## Rationale

- Preserves approved decision `ATL-DEC-20260725-014` separating Wix from protected routing, ledger, cap, reconciliation and security controls.
- Provides a coherent customer interface for Atlas-managed API plans.
- Prevents browser or Wix code from becoming an authoritative or secret-bearing execution environment.
- Supports provider abstraction, controlled allowances, tenant isolation and auditable workflows.
- Creates a migration path for enterprise SSO and Managed Secure without weakening the public website boundary.

## Considered alternatives

### A. Full Workspace inside Wix Members/Velo

**Disposition:** Not selected as the preferred architecture. It may be evaluated only as a thin client whose protected operations remain external. It must not hold provider secrets, authoritative entitlement logic, tenant state, file-processing trust or usage-ledger authority.

### B. Direct links to provider applications

**Disposition:** Valid only for approved customer-owned licence lanes. It does not satisfy the Atlas-managed API plan model because Atlas cannot consistently enforce provider-neutral workflows, usage caps, audit and entitlement controls.

### C. Separate Atlas-owned Workspace and secure runtime

**Disposition:** Preferred recommendation, pending owner approval and evidence-based architecture review.

## Mandatory controls before approval

1. CIAM, MFA, session and revocation architecture.
2. Tenant and object-level authorization model.
3. Secrets vault and key-rotation model.
4. Provider routing, fallback and emergency disable controls.
5. Atomic reservation, metering, settlement and hard-cap model.
6. Upload quarantine, malware scanning and safe parser controls.
7. Data classification, encryption, retention and deletion model.
8. Append-only audit and privileged-access controls.
9. Threat model, GDPR role assessment and DPIA screening.
10. Staging, pilot, penetration testing, rollback and incident evidence.

## Open decisions

- final frontend framework and hosting platform;
- `app.atlas-ai.no` or another protected route/subdomain;
- CIAM platform and enterprise federation scope;
- initial provider/model policy and fallback behavior;
- persistent conversation and file-retention defaults;
- exact normalized usage unit and customer-facing allowance wording;
- initial MVP workflows and user segments;
- support access model and administrative tooling;
- implementation dates, budget and staffing.

## Review trigger

Explicit owner approval, completed architecture/security review, or evidence that the proposed boundary conflicts with provider, Wix, legal, privacy or operational requirements.

Until approved, this record is advisory and must not be represented as an implemented or released Atlas capability.
