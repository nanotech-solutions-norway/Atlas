# Atlas AI Website and Governance Repository

Updated: 10:54, 03.08.2026 Europe/Oslo

This repository contains the GitHub-governed website source, public static pages, CMS schemas, seed packs, QA scripts, governance records, legal/trust drafts, Velo notes, evidence checklists, and future protected-runtime placeholders for the Atlas AI website workstream.

## Canonical positioning

Atlas AI is a business-first Norwegian AI implementation and governance service. Atlas owns problem framing, workflow design, knowledge architecture, onboarding, governance, controlled configuration, QA, support, and lifecycle management. Third-party providers supply the model, platform and underlying infrastructure where appropriate.

Atlas AI must not be presented as a proprietary foundation-model company, a generic chatbot catalogue, a prompt marketplace, or a reseller of provider subscriptions unless a specific documented agreement exists.

## Canonical Norwegian website-copy baseline

The controlling Phase 1 public-copy source is:

- **Atlas AI Norwegian Website Copy Deep Research Report — 18:21, 02.08.2026**
- Drive DOCX ID: `1YFbBrmESNsWS_QvVZO5ah6Sm1TQsye5x`
- Drive Markdown ID: `1ssEO78IuebRSubl6WgqS_UYTM3_vfIf2`
- Markdown SHA-256: `6ed168ae842df177ac4790b18132a82fdfe640752564f9f4c3203e28d0a4bc57`
- DOCX SHA-256: `2354c572c5bbdec751c5261f16d559ea9ed05aa8c704198b36146750e7984209`

Appendix A of that report is the canonical paste-ready Norwegian Bokmål copy baseline for the 15 Phase 1 pages and the shared header, footer, cookie and status components. The report is authoritative for public wording subject to newer explicit owner decisions, approved Atlas commercial controls, legal review requirements and verified implementation evidence.

## Public website model

- Root `/` is Norwegian Bokmål.
- `/en/` is the reciprocal English mirror and remains evidence-gated.
- Primary public navigation: **Tjenester, Managed Secure, Priser, Tillit, Ressurser, Om oss, Kontakt**.
- Tjenester submenu: **Bedrift, Studenter, Privatpersoner, Plattformer**.
- Persistent header CTA: **Oppstart**.
- The 15 canonical page roles and routes are Home, Tjenester, Bedrift, Studenter, Privatpersoner, Managed Secure, Priser, Tillit, Plattformer, Oppstart, Ressurser, FAQ, Om oss, Kontakt and Juridisk.
- Ordinary public forms are low-risk qualification only and must not accept files or sensitive/confidential information.
- Approved prices are public references, while checkout, payment, provisioning and activation remain separately locked.
- Family remains `Utsatt`.
- Managed Secure remains qualification-only and not self-service.

## Claims and evidence control

ADR-0005 and the current Atlas source-authority controls govern website copy, Wix CMS records, Trust content, provider disclosure, pricing language, sales copy, Managed Secure wording and future evidence packs.

Atlas may use external AI research, provider certifications, provider DPAs and provider SLAs only as contextual or provider-attributed evidence. Atlas must not convert them into direct Atlas-specific performance, ROI, accuracy, learning-outcome, compliance, security, uptime, data-residency or reliability claims unless Atlas has documented Atlas-specific evidence under comparable conditions.

Public Atlas copy must avoid unsupported fixed percentages, guaranteed ROI, guaranteed grades, blanket GDPR compliance, Atlas-owned ISO/SOC certification, blanket Norway-only data residency, inherited provider SLA claims and absolute secure/zero-risk wording.

## Design-artifact boundary

Gamma and Figma are design/copy evidence, not canonical implementation or release evidence. Wix header, navigation, language-selector and mobile-menu configuration guidance may be retained in operator instructions but must not be represented as a public page section or page slide. The first non-page configuration slide was removed from all 15 canonical Figma v4 files on 03.08.2026; Gamma artifacts were intentionally left unchanged.

## Governance model

GitHub is the engineering governance and control plane. Google Drive is the controlled report archive and human-readable mirror. Wix remains the commercial website/CMS surface. A protected runtime remains a future evidence-gated plane. Gamma and Figma remain design/reference surfaces.

## Release state

`NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

No copy, design or manifest update alone authorizes publication, checkout, payment, automatic entitlement, provider credentials, confidential intake or Managed Secure delivery.

## Deployment

GitHub Pages deployment is configured through `.github/workflows/deploy-pages.yml`. The workflow publishes only public website assets and excludes governance/source folders from the Pages artifact.

Manual setting required if not already done: Repository Settings → Pages → Source → GitHub Actions.

## Repository boundary

Do not commit secrets, credentials, protected artifacts, customer confidential data, private packages, bank/accounting data, tokens, API keys, or sensitive personal data.
