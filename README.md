# Atlas AI Website and Governance Repository

Updated: 12:42, 10.06.2026 Europe/Oslo

This repository contains the GitHub-governed website source, public static pages, CMS schemas, seed packs, QA scripts, governance records, legal/trust drafts, Velo notes, evidence checklists, and future Azure placeholders for the Atlas AI website workstream.

## Canonical positioning

Atlas AI is a governed AI solution-layer company. Atlas owns problem framing, workflow design, knowledge architecture, onboarding, governance, secure delivery, QA, support, and lifecycle management. Third-party model providers supply the model layer where appropriate.

Atlas AI must not be presented as a proprietary foundation-model company, a generic custom-GPT storefront, or a reseller of vendor subscriptions unless a specific vendor agreement exists.

## Claims and evidence control

ADR-0005 is the active claims-governance overlay for website copy, Wix CMS records, Trust Center content, provider disclosure, pricing language, sales copy, Managed Secure wording and future evidence packs.

Atlas may use external AI research, vendor certifications, vendor DPAs and provider SLAs only as contextual or vendor-attributed evidence. Atlas must not convert them into direct Atlas-specific performance, ROI, accuracy, learning-outcome, compliance, security, uptime, data-residency or reliability claims unless Atlas has documented Atlas-specific evidence under comparable conditions.

Public Atlas copy must avoid unsupported fixed percentages, guaranteed ROI, guaranteed grades, blanket GDPR compliance, Atlas-owned ISO/SOC certification, blanket Norway-only data residency, inherited vendor SLA claims and absolute secure/zero-risk wording.

## Public website model

- Root `/` is Bokmål.
- `/en/` is English.
- Primary navigation: Solutions, Managed Secure, Pricing, Trust, Resources, About, Contact.
- Controlled audience paths: Business, Students, Consumers.
- Platform Lanes are accessible, but not over-promoted.
- Ordinary public forms are low-risk qualification only.
- Managed Secure and Azure remain gated until validated Phase 3/6 evidence exists.

## Governance model

GitHub is the engineering governance and control plane. Wix remains the commercial website/CMS surface. Azure remains the future secure runtime. Gamma remains design/reference input.

## Deployment

GitHub Pages deployment is configured through `.github/workflows/deploy-pages.yml`. The workflow publishes only public website assets and excludes governance/source folders from the Pages artifact.

Manual setting required if not already done: Repository Settings → Pages → Source → GitHub Actions.

## Repository boundary

Do not commit secrets, credentials, protected artifacts, customer confidential data, private packages, bank/accounting data, tokens, API keys, or sensitive personal data.
