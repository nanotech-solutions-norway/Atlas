# Atlas Workspace Memory Update

**Timestamp:** 18:54, 05.08.2026 Europe/Oslo  
**Apply rule:** Use only `APPROVED`, `AUTO_APPROVED` or `CANONICAL` entries as instructions. Workspace architecture remains `PENDING_REVIEW`.

## Current approved context

- Atlas-managed B2C API delivery uses hard caps; retail-seat resale/pass-through is prohibited.
- Wix is the public/CMS/plan/order/member-entry surface.
- Provider routing, authoritative entitlements, usage reservation/ledger, hard caps, reconciliation, protected state and secure controls remain external.
- Customer-owned licence lanes execute in the approved provider/customer application.
- Managed Secure remains qualification/architecture-review only.
- Public, purchase and production activation remain `NO_GO`.

## Workspace proposal — PENDING_REVIEW

Create an authenticated Atlas-owned Workspace for customers on Atlas-managed API-metered plans. Prefer a separately deployed protected app, potentially `app.atlas-ai.no`, integrated with Wix for commercial/account entry and with the secure Atlas runtime for all protected execution.

Minimum proposed features: controlled chat/workflows, permitted uploads, project/history, output review/export, allowance and remaining-cap display, hard-stop states, support and deletion entry points.

## Security requirements

No provider keys or protected logic in Wix/browser. Require CIAM/MFA for privileged roles, tenant/object authorization, vaulting/rotation, provider-only egress, atomic metering and hard caps, quarantine/malware scanning, encrypted tenant-isolated storage, append-only audit, retention/deletion, threat model, DPIA screening, incident/rollback tests and independent penetration testing.

## Recorded contradiction

The research report's Wix Members/Velo MVP option is advisory and may be used only as a thin client. It cannot override approved decision `ATL-DEC-20260725-014`.

## Key controlled files

- `active-source/2026-08-05/ATLAS_WORKSPACE_BUSINESS_SECURITY_IMPLEMENTATION_UPDATE_1854_05082026.md`
- `governance/decisions/ATLAS_WORKSPACE_ARCHITECTURE_DECISION_PROPOSAL_1854_05082026.md`
- `governance/security/ATLAS_WORKSPACE_SECURITY_CONTROL_ADDENDUM_1854_05082026.md`
- `governance/validation/ATLAS_WORKSPACE_VALIDATION_AND_LAUNCH_GATES_1854_05082026.md`
- `governance/registers/canonical/ATLAS_WORKSPACE_UPDATE_REGISTER_1854_05082026.md`
- `governance/source-registers/ATLAS_WORKSPACE_REPORT_SOURCE_REGISTER_1854_05082026.md`
- `governance/project-logs/ATLAS_PROJECT_LOG_UPDATE_PACK_WORKSPACE_1854_05082026.md`
- Drive report ID: `1O_bQyBtYtbeTwZ6fSPDObUvSNOXCNfxOvWSMGoP5YhM`

## Next action

Obtain owner approval/rejection of proposed decision `ATL-DEC-20260805-034`, then create the PRD, UX, architecture/data-flow, CIAM, threat-model, entitlement/metering, upload-security, privacy/DPIA and test specifications.
