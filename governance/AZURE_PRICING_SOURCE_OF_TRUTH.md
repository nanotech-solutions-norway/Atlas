# Azure commercial pricing source-of-truth reference
**Scope:** Azure-dependent projects. **Status:** policy discovery only; NO Azure deployment or billing API permission.

## Source and authority
Canonical company-wide policy: https://github.com/nanotech-solutions-norway/ntsn-mcp-integrations/blob/main/governance/AZURE_PRICING_SOURCE_OF_TRUTH.md

Owner-restricted Google Drive folder, discover by exact title: `NTSN Azure Billing & Pricing — Restricted`. It contains the COMPLETE, integrity-checked October 2026 corporate billing-profile account price sheet, invoice/usage and subscription-plan evidence, private archive and smaller region index. Authorized connected Drive tools can use it **without asking the operator to resend the October sheet**.

Never publish confidential negotiated prices, subscription/account/billing identifiers, original ZIP/parts, private cache, invoices or tokens to ANY GitHub repo (private or public), issues, CI logs or build artifacts. There is no implicit private Drive access for GitHub Actions or other agents.

## Required project process
1. Establish exact project-to-Azure-subscription-to-billing-profile/offer agreement binding; `Microsoft Azure Plan` and similar subscription names alone are NOT project assignment evidence. There are two active and one deleted corporate plan entries; do not infer which is authorized.
2. Select account rate rows by meter, SKU, region, tier, offer, term and effective dates. October sheet covers ONLY 1–31 October 2026, is historic after that, and does not authorize later-month procurement.
3. Use the owner-controlled Drive archive for account rates; label Microsoft's public Azure Retail Prices API strictly `PUBLIC_ESTIMATE_ONLY`. No assumed credit or free grant.
4. Reconcile total cost including taxes, currency conversion, pooled subscription usage, security/networking, Key Vault, Container Apps, PostgreSQL/storage, retention and teardown liabilities. Azure budgets are alerts, not hard financial ceilings.
5. Obtain independent security/cost review and an explicit project-specific approved deployment budget and cloud role/scope before resources or billable jobs are created. Preserve existing least-privilege identities.
6. Future-month automatic price-sheet retrieval is **NOT** operational. A distinct minimum-rights billing-scope principal, agreement-specific Cost Management API and separately authorized secure archival are still pending. Neither plain Azure Reader nor Monitoring Reader proves billing price-sheet permissions.
7. New projects should adopt this reference at onboarding. Automatic GitHub-wide enforcement is NOT yet installed; see `templates/ONBOARD_NEW_AZURE_DEPENDENT_PROJECT.md` in NTSN-Orchestrator-Control-Plane.

## Checklist
- [x] Historical October private data exists and validated in the central vault.
- [ ] Current project's subscription and Azure agreement privately verified.
- [ ] Current pricing period available and matching meters/term/tiers reconciled.
- [ ] Appropriate independent cost/security review and explicit budget accepted.
- [ ] Any provisioning/deletion approved separately, with an independently verified teardown plan.

## Atlas product separation
`Atlas` has a historical **PENDING_REVIEW / NO_GO** cloud architecture proposal and source-authority register. This policy does not promote Azure as an approved deployment choice or make a reserved cloud commitment. Treat `Atlas` and `atlasorbit` as different repository/project sources until explicit canonical identity reconciliation, and preserve the existing Atlas release controls.

See `governance/decisions/ATLAS_FULL_DEPLOYMENT_ARCHITECTURE_DECISION_PROPOSAL_1545_06082026.md` and `project-memory/atlas/ATLAS_SOURCE_AUTHORITY_MAP.md`.
