# Atlas Website Repository

Generated: 12:45, 01.06.2026 Europe/Oslo

This repository contains the static Atlas website and the GitHub-governed implementation package for the Atlas website workstream.

## Scope

Atlas is an AI enablement and delivery venture that packages governed, purpose-specific AI work models. This repository contains only public/static website content, governance documentation, schemas, seed data, QA scripts, Velo/source placeholders, and future secure-runtime contracts.

## Deployment

GitHub Pages deployment is configured through `.github/workflows/deploy-pages.yml`.

Manual GitHub settings still required:

1. Repository Settings → Pages → Source: GitHub Actions.
2. Confirm the `github-pages` environment is available.
3. Add custom domain only after domain ownership and DNS records are verified.

## Repository boundary

Do not commit secrets, credentials, customer files, private accounting data, confidential contracts, API keys, or sensitive personal data.

Azure and Managed Secure Mode are represented only as future placeholders until a commercial secure-delivery use case is approved.
