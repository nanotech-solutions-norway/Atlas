# Atlas AI — GitHub Compromise and Independent Source-Control Continuity — 02:41, 09.08.2026

## Scope

Atlas AI inherits the NTSN universal GitHub-compromise continuity standard. This applies to Atlas public/commercial code, engineering/governance records, Atlas Workspace, Control Center, Managed Secure deployment assets and customer-runtime source/configuration that belongs in Git.

## Mandatory principle

GitHub is the normal primary engineering/change-control plane while trusted, but it must not be the only independently recoverable copy of critical Atlas source, governance and release evidence.

A suspected GitHub account, organization, repository, App, Actions, runner or platform compromise causes **fail-closed source-control mode**: GitHub-triggered deployment and write-capable automation are suspended until a last-known-good independently verified checkpoint is established.

## Recommended Atlas continuity stack

1. **Primary:** GitHub with protected branches, reviewed PRs, scanning, minimal workflow permissions and short-lived cloud federation.
2. **Managed secondary:** Azure DevOps Repos under Microsoft Entra ID with independent roles/Conditional Access and branch policies. Secondary is normally read-only/warm for continuity, not an automatic production deployment authority.
3. **Immutable recovery:** full Git bundles, SHA-256 release manifests and independent signatures stored in WORM-capable object storage.
4. **Offline recovery:** encrypted cold copy of critical Atlas governance/security/release bundles.
5. **Optional provider-diverse forge:** isolated Forgejo/GitLab on a separately administered European provider when the additional self-hosting operational burden is accepted.

## Why not rely on a simple mirror

A destructive mirror can propagate an attacker’s ref deletions, force updates or tampered history into the backup. Mirroring therefore requires retained checkpoints/divergent refs and must be combined with immutable backups.

## Domeneshop/private server

A Domeneshop-hosted or other private server can technically host a bare Git repository, Forgejo or GitLab. It is acceptable as an additional recovery location if independently administered and hardened. However, using the same provider/account for DNS, production hosting and the only source-control recovery path increases common-mode risk. Higher-security Atlas deployments should prefer a different provider/account for the secondary Git control plane and retain an immutable/offline copy in another trust domain.

Minimum self-hosted safeguards include: separate admin identities, MFA where supported, SSH keys rather than passwords, VPN/private access or strict allowlists, firewalling, patching, monitoring, encrypted storage, no production provider credentials on the Git host, and tested off-host backup/restore.

## Independent trust and release integrity

Critical release/security checkpoints must be verifiable outside GitHub. Use signed commits/tags or signed release manifests whose signing key is not stored in GitHub. Store trusted public verification material and the manifest with immutable recovery evidence.

The manifest should bind at least repository, commit SHA, release/tag, relevant dependency/tool/schema versions and deployment target.

## Incident modes

### GitHub outage without compromise evidence

Development may continue locally or on the secondary using isolated branches, but production promotion remains paused unless an independently validated alternative CI/change-control path exists.

### GitHub compromise suspected

- freeze GitHub-originated deployments and privileged automation;
- activate relevant Atlas/MCP kill switches;
- revoke affected GitHub tokens/Apps/deploy keys/workload trust;
- identify last-known-good signed checkpoint;
- verify secondary/bundle history and release manifest;
- restore into an isolated clean repository/control plane;
- rotate possibly exposed credentials;
- rebuild and validate CI/CD and tenant/runtime controls;
- record explicit return-to-service approval.

### GitHub platform/supply-chain compromise suspected

Treat GitHub-hosted workflow output, Actions artifacts and GitHub-only attestations as untrusted until independently validated. Rebuild from independently signed source on an alternative CI/runtime boundary.

## Atlas customer impact

Customer runtime data and provider credentials remain outside GitHub. A GitHub compromise must not directly expose customer connector secrets because credentials belong in the protected Credential Broker/secret manager boundary. Customer-facing changes and high-risk actions are frozen until the recovered source/control plane is validated.

## Routing

DNS or routing failover can restore availability but does not establish source integrity. Never automatically reroute production deployment authority to an unverified secondary repository.

## Status

This document defines required architecture and recovery behavior. It does not claim Azure DevOps, Forgejo/GitLab, immutable storage or offline recovery is already configured or live.