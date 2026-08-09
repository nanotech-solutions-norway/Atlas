# Atlas AI Security Policy — 02:41, 09.08.2026 Europe/Oslo

## Scope

This public policy applies to the Atlas AI project, Atlas Workspace, organisation administration, Atlas operator systems, integrations/MCPs and customer-facing Atlas services. It is the public-safe implementation summary of the NTSN Atlas AI & MCP Universal Security Standard.

A policy document does not prove that a control is live. Atlas distinguishes `DESIGNED`, `CONFIGURED`, `IMPLEMENTED`, `TESTED`, `VALIDATED`, `APPROVED`, `RELEASE_APPROVED` and `LIVE` states.

The Atlas source-control continuity overlay is maintained at `docs/security/GITHUB_COMPROMISE_CONTINUITY.md`.

## Three-plane security boundary

Atlas separates:

1. **Public/commercial plane** — website, marketing, pricing, qualification and approved account-entry functions.
2. **Engineering/governance plane** — source control, controlled documentation, CI/CD and release evidence.
3. **Protected runtime/control plane** — customer execution, tenant authorization, entitlements, provider credentials, protected data, connectors, metering, audit and privileged administration.

The public website/browser and public GitHub repositories are never authoritative for tenant policy, provider credentials, usage caps, privileged configuration or security audit evidence.

## Mandatory security principles

- Zero trust and explicit server-side authorization.
- Least privilege for users, administrators, workloads, agents and connectors.
- Raw API keys, passwords, access/refresh tokens, private keys and equivalent credentials never enter LLM/agent prompts, chat history, memory, RAG, tool results, screenshots, public forms, logs, Drive evidence or Git.
- Prefer OAuth/OIDC, managed/workload identities and short-lived/dynamic credentials over static keys.
- Provider credentials are attached server-side by the protected credential boundary; an AI model receives capabilities and opaque connector references, not secret values.
- Every private request is bound server-side to the authenticated tenant and authorized object/action.
- Customer data, memory, vector indexes, credentials, caches and audit views are isolated by tenant.
- New integrations and MCPs are read-only first. Write actions are explicit, bounded, classified by risk and independently authorized.
- Model output is never authorization. Consequential actions require the appropriate server-side policy and explicit approval controls.
- High-risk/destructive actions are blocked by default and require a separately approved release path.
- Production services require rate/resource limits, audit/redaction, monitoring, backup/recovery and incident-response controls.
- Unexpected security-policy, tool-schema, route or runtime-manifest drift fails closed.

## Source-control compromise and continuity

GitHub is the normal engineering/change-control authority while trusted, but Atlas requires an independent recovery chain. A suspected GitHub account, organization, repository, App, Actions, runner or platform compromise suspends trust in GitHub-triggered deployment/write events until a last-known-good independently verified checkpoint is established.

The recommended continuity model is GitHub primary, Azure DevOps Repos as the preferred managed secondary under independent Microsoft Entra roles, immutable independently signed Git bundles/release manifests, and an encrypted offline recovery copy. An isolated Forgejo/GitLab service on a separately administered provider is an optional provider-diverse alternative.

A simple destructive real-time mirror is not a sufficient security backup because compromised or deleted refs can propagate to the mirror. DNS/routing failover can improve availability but does not establish source integrity and must not automatically grant deployment authority to an unverified mirror.

A Domeneshop/private server may be used as an additional recovery location when independently administered and hardened, but it should not be the only recovery platform if it shares the same provider/account boundary as production DNS or hosting.

## Customer credentials and connectors

Atlas should connect customer services through OAuth/OIDC whenever the provider supports it. The provider authorization occurs out-of-band through the provider/secure browser flow; Atlas stores resulting credential material only in the protected server-side credential boundary.

If a provider supports only an API key or similar static secret, the customer must enter it through a protected credential-entry surface—not a chatbot, public form, support message or source file. Atlas must not echo the value after entry. The credential is tenant-bound, encrypted/protected server-side, scoped to the minimum provider permissions and rotated/revoked when required.

For MCP clients/servers, client authorization and upstream-provider authorization are separate. A token presented to an MCP server must not be forwarded unchanged to an upstream provider.

## Atlas customer isolation

All customers receive the universal core controls: authenticated tenant binding, least privilege, encrypted protected storage/transport, no secrets in model context, secure credential handling, audit/redaction, resource limits, secure SDLC and incident handling.

Higher-security offerings may add dedicated runtime/data stores/vaults, private networking, customer-managed keys, SSO/SCIM, enhanced security monitoring, extended audit, penetration testing and customer-specific compliance mappings. These controls are enabled only when implemented and validated for the relevant service/tier.

## Data and AI context

Public website/forms collect only approved low-risk data. Confidential or restricted uploads must use a protected customer intake/Workspace path after that capability has been security-reviewed and released.

Atlas treats external documents, websites, emails, provider responses, RAG sources, tool metadata and user content as untrusted data. Retrieved content cannot promote itself to system policy or grant tool permissions. Prompt-injection/content filters are supplemental controls, not authorization mechanisms.

Cross-tenant retrieval is prohibited. Memory and knowledge writes require tenant binding, provenance and lifecycle/delete controls.

## Tool and agent safety

Production tools are allowlisted, versioned and schema-bounded. Atlas does not expose unrestricted shell, arbitrary filesystem, arbitrary SQL or general secret-retrieval tools to AI agents.

Consequential actions use controls appropriate to risk, including preview/diff, one-use expiring approval, payload binding, idempotency/replay prevention, readback and independent kill switches. Ambiguous mutations are not blindly retried.

Third-party MCP servers, packages and agent tools require security review/allowlisting. Tool names, schemas, descriptions, routes and server identity are security-relevant supply-chain inputs.

## Secure development and GitHub

Do not publish secrets, credentials, private keys, customer confidential data, bank/accounting data, protected artifacts, private packages, production configuration or sensitive personal data in this repository.

Security-sensitive runtime/deployment components and customer data do not belong in the public Atlas repository. Use reviewed changes, minimal CI permissions, secret scanning/push protection and dependency/code security checks appropriate to repository capability. Cloud CI/CD should use workload federation/OIDC instead of long-lived deployment credentials where supported.

Critical release/security checkpoints should be independently verifiable outside GitHub by signed commits/tags and/or signed release manifests stored with immutable recovery evidence.

## Privacy and regulatory posture

Atlas implements privacy/security by design and risk-based controls. Customer deployments must determine controller/processor roles, processing purposes, data classes, retention, subprocessor/provider terms and DPIA requirements where applicable.

The EU AI Act is generally applicable from 2 August 2026, with specific obligations and high-risk transition dates depending on the use case and current law/guidance. Atlas does not classify every customer use case identically; higher-risk or regulated applications require a dedicated review before release.

Do not claim unconditional, universal or absolute GDPR compliance, AI Act compliance, confidentiality or security without evidence for the specific deployed service and customer use case.

## Managed Secure

Managed Secure is a protected architecture/deployment class, not a marketing label that bypasses release evidence. Before production use with real customer sensitive data it requires, as applicable: customer threat model, data classification, secure tenant architecture, privileged-access controls, retention/deletion, incident runbooks, backup/restore validation, provider/subprocessor review, DPIA/security review, adversarial AI testing and external penetration testing.

Managed Secure also requires independent source-control continuity appropriate to its risk: a secondary Git control plane, independently verifiable release checkpoint, immutable recovery evidence and tested restoration without relying solely on GitHub.

## Incident handling

If a credential, account or source-control authority may be compromised: suspend the affected deployment/action trust, revoke/rotate credentials, preserve privacy-minimized evidence, determine scope, identify the last independently verified source checkpoint, reconcile provider/customer state, remediate the root cause and rerun relevant security tests before re-enable. A secret committed to Git is treated as compromised even if rapidly removed.

## Vulnerability reporting

Do not disclose suspected vulnerabilities, credentials or customer-sensitive evidence in a public issue. Report through an established private channel controlled by the repository owner, including the affected component/version, reproduction steps, impact and suggested remediation if known.

## Security limitation statement

No architecture eliminates all risk. Short-lived credentials, encryption, WAFs, prompt filters, tenant controls and independent Git recovery reduce specific risks but do not make authorized misuse, compromised workloads, provider failures or incorrect model outputs impossible. Security and compliance remain dependent on the deployed controls, customer use case, provider behavior, applicable law and continuing validation.