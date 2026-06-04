# Atlas AI Website and Governance Repository

Updated: 13:02, 04.06.2026 Europe/Oslo

This repository contains the GitHub-governed website source, public static pages, CMS schemas, seed packs, QA scripts, governance records, legal/trust drafts, Velo notes, and future Azure placeholders for the Atlas AI website workstream.

## Canonical positioning

Atlas AI is a governed AI solution-layer company. Atlas owns problem framing, workflow design, knowledge architecture, onboarding, governance, secure delivery, QA, support, and lifecycle management. Third-party model providers supply the model layer where appropriate.

Atlas AI must not be presented as a proprietary foundation-model company, a generic custom-GPT storefront, or a reseller of vendor subscriptions unless a specific vendor agreement exists.

## Public website model

- Root `/` is Bokmål.
- `/en/` is English.
- Primary navigation: Solutions, Managed Secure, Pricing, Trust, Resources, About, Contact.
- Platform Lanes are accessible, but not over-promoted.
- Ordinary public forms are low-risk qualification only.
- Managed Secure and Azure remain gated until validated Phase 3/6 evidence exists.

## Deployment

GitHub Pages deployment is configured through `.github/workflows/deploy-pages.yml`. The workflow publishes only public website assets and excludes governance/source folders from the Pages artifact.

Manual setting required if not already done: Repository Settings → Pages → Source → GitHub Actions.

## Repository boundary

Do not commit secrets, credentials, protected artifacts, customer confidential data, private packages, bank/accounting data, tokens, API keys, or sensitive personal data.
