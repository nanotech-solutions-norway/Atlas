# Atlas AI Integrated SEO, AEO and GEO Implementation Blueprint — 11:35, 11.07.2026

> **Control status:** Recommended consolidated working baseline. Commercial pricing, provider-delivery rights, legal interpretation, public availability, production routing and site identity remain approval-gated where identified as PENDING_REVIEW.

> **Execution boundary:** No Wix publication, Gamma editing, Azure deployment, subscription activation or production change was performed.

## Executive interpretation

SEO, answer-engine visibility and generative-search visibility should be treated as one governed discoverability program. There is no separate technical shortcut that guarantees inclusion in AI answers. Google states that established crawlability, quality and technical SEO principles remain applicable to AI features [W5-W6].

## Operating model

| Layer | Responsibility |
|---|---|
| Wix Studio/CMS/Velo | Public pages, metadata, structured data, forms, multilingual routes and analytics |
| GitHub | Page map, schema templates, copy/claim records, QA evidence, release tags and rollback references |
| Azure | Conditional secure intake, protected artifacts or private customer workflows only |
| Gamma | Design and layout reference only |

## Canonical page tree

- `/`
- `/en/`
- `/solutions/`
- `/solutions/business-ai/`
- `/solutions/students/`
- `/solutions/consumers/`
- `/managed-secure/`
- `/pricing/`
- `/trust/`
- `/platform-lanes/`
- `/onboarding/`
- `/resources/`
- `/about/`
- `/contact/`
- `/legal/`

## Technical SEO baseline

1. One indexable canonical URL per language and page purpose.
2. Bokmål root with English `/en/` mirror.
3. Reciprocal `hreflang` for `nb-NO` and `en`.
4. Unique title, description, H1 and Open Graph fields.
5. Clean sitemap and robots controls.
6. Permanent redirects only after destination validation.
7. LCP, INP and CLS monitoring.
8. Server-rendered or reliably crawlable primary content.
9. Consent-aware analytics.
10. No indexable staging/test/query duplicates.

## Structured data

Use visible-content-aligned JSON-LD for:

- Organization
- WebSite
- BreadcrumbList
- Service
- Article
- FAQPage only where the page and eligibility rules support it

Structured data supports understanding and eligibility; it does not guarantee rich results [W7]. Do not fabricate reviews, ratings, prices, certifications or service availability.

## AEO content model

Each primary page should include:

- direct 40-80 word answer block;
- concise definition;
- who the offer is for;
- inclusions/exclusions;
- provider and data boundary;
- next step;
- dated source references where factual claims are used.

FAQ content must answer real customer questions and remain visible. Do not create schema-only Q&A.

## GEO / generative-search model

Focus on:

- stable entity naming;
- clear organization and service descriptions;
- cited statistics and attributed provider facts;
- author/date/review metadata;
- source-grounded guides;
- internal links between solution, trust, pricing and resource pages;
- consistent provider disclosure;
- transparent uncertainty and update dates.

`llms.txt` may be maintained as an optional discoverability aid, but it must not be presented as a ranking or inclusion guarantee.

## Content clusters

| Cluster | Primary page | Supporting resources |
|---|---|---|
| AI for Norwegian SMBs | Business | onboarding, governance, provider comparison, practical workflow guides |
| Responsible student AI | Students | study planning, source discipline, school-policy boundaries |
| Practical consumer AI | Consumers | privacy, safe use, family roles, usage limits |
| Governed AI delivery | Trust | provider disclosure, human review, claims methodology |
| Managed Secure | Managed Secure | architecture review, secure intake, evidence model |
| Pricing and usage | Pricing | allowance, caps, cancellation, licences and provider costs |

## GitHub governance structure

Maintain:

- `sitemap.yml`
- `page-map.yml`
- `route-map.yml`
- `metadata-register.yml`
- `hreflang-register.yml`
- `keyword-map.yml`
- `aeo-faq-register.yml`
- `geo-entity-register.yml`
- `claims-registry.yml`
- `legal-doc-register.yml`
- `event-taxonomy.yml`
- CMS schema and seed files
- launch QA and evidence index

Required checks: JSON/YAML validation, duplicate metadata, route validity, reciprocal hreflang, structured-data syntax, approved claim references, forbidden wording, secret scan and bilingual parity.

## Wix implementation

- Bind repeatable page fields to governed CMS objects.
- Keep protected logic server-side.
- Use route-aware CTAs.
- Keep ordinary forms low risk and without confidential upload.
- Export CMS and metadata snapshots for each release.
- Validate dynamic pages separately from static templates.

## Conditional Azure annex

Azure is not required for public discoverability. Activate it only for secure intake, protected artifacts, private workspaces or Managed Secure.

Minimum controls:

- Microsoft Entra identity
- Key Vault and managed identities
- private storage
- least privilege
- WAF/rate limits where public
- centralized diagnostics
- retention/deletion
- backup/restore
- revocation
- infrastructure as code

Microsoft recommends managed identities to avoid credentials in code [W11]. Security design should follow current identity, secrets, isolation, monitoring and response patterns [W10].

## Accessibility and performance

Target WCAG 2.2 AA [W8], including keyboard use, focus visibility, labels, error identification, reflow, contrast, reduced motion and minimum target size. Accessibility defects are launch defects, not post-launch enhancements.

## Measurement

Track:

- index coverage
- non-brand and brand queries
- CTR
- conversion by audience
- trust-page engagement
- architecture-review requests
- form completion
- resource citations/referrals
- AI-feature referrals where observable
- Core Web Vitals
- content freshness and claim review expiry

## Six-month roadmap

| Month | Outcome |
|---|---|
| 1 | Route, metadata, schema and source baseline |
| 2 | Core business/student/consumer pages and trust content |
| 3 | Resource cluster and FAQ evidence |
| 4 | Conversion and internal-link optimization |
| 5 | Qualified content expansion and authority building |
| 6 | Revalidation, pruning, performance and international readiness |

## Key update from prior SEO files

The prior four-document SEO set is consolidated. Platform-specific instructions remain as implementation annexes, while repeated strategy text is removed. “GEO” is reframed as source-grounded entity/content quality rather than speculative markup.
