# Atlas AI Phase 1 Page, Section and Content Blueprint — 14:19, 02.08.2026

**Project:** Atlas Website / Atlas AI  
**Scope:** Phase 1 public-information and qualification surface  
**Classification:** Approved-source consolidation and non-sensitive implementation guidance: `AUTO_APPROVED`; approved positioning, pricing and terminology retained.  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## 1. Controlling website model

- Atlas Phase 1 is a Norway-first governed AI information and qualification surface, not a self-service subscription storefront.
- Business/professional customers are the dominant lane. Students and private users are controlled secondary lanes.
- The principal journey is **discovery → understanding → trust → qualification → human follow-up**.
- Public pages must show approved prices clearly. Price visibility does not activate Wix plans, checkout, provider access or production entitlement.
- Managed Secure remains qualification and architecture review only.
- Family has an approved reference price but is outside the current activation scope and must not be presented as purchasable.
- Use **AI** throughout Norwegian copy. Home may explain once that AI is also called KI (kunstig intelligens) in Norwegian.
- Public forms collect low-risk contact and qualification data only. No confidential files, credentials, identity documents, special-category data or sensitive architecture details.

## 2. Navigation and common page contract

- **Primary navigation:** Tjenester, Managed Secure, Priser, Tillit, Ressurser, Om oss, Kontakt.
- **Tjenester submenu:** Bedrift, Studenter, Privatpersoner, Plattformer.
- **Primary header CTA:** Oppstart.
- **Footer:** Juridisk, FAQ, privacy/cookies, company identity, contact details and language selector.
- **Language:** Bokmål at root; reciprocal English pages under `/en/` only with full content, metadata, link and hreflang parity.

Each primary page must explain, in sequence:

1. what the page/offering is;
2. who it is for;
3. the concrete problem or situation;
4. what Atlas provides;
5. what is included and excluded;
6. price or pricing method and current availability;
7. how engagement starts;
8. why the information can be trusted.

## 3. Common layout and design system

- Calm, structured and evidence-led; avoid generic robots, glowing brains and unexplained neural imagery.
- Roboto Slab headings and Roboto body/interface copy.
- Core palette: navy `#15213F`, Atlas blue `#3257B8`, controlled highlight `#476FD6`, neutral panel `#E9ECF2`, border `#CFD2D8`, white `#FFFFFF`.
- Reference geometry: 104 px large-desktop side margins, 1712 px content frame, 32 px grid gap and 32 px card padding. Adapt responsively; do not hard-code slide geometry as universal web geometry.
- Hero H1 up to approximately 72 px; standard/dense desktop H1 around 54 px; responsive scaling required.
- Body approximately 18–22 px desktop and 16–18 px mobile, around 150% line height.
- One solid primary CTA and at most one secondary action per section.
- Alternate white and restrained neutral/light-blue sections; use cards, comparison tables and process diagrams only when they improve comprehension.
- Internal quality target: WCAG 2.2 AA. Manual desktop, tablet, mobile, keyboard, focus, contrast, form, reflow and screen-reader QA is mandatory.

# 4. Page contracts

## 4.1 Hjem / Home — `/`

- **Must include:** Atlas positioning; one AI/KI explanation; Business-first value; four audience routes; how Atlas works; practical use cases; trust/boundary summary; pricing preview; resources/FAQ preview; closing CTA.
- **Content buildup:** Hero should explain configured workflows, onboarding, human review and defined provider/data boundaries. Follow with business problems and outcomes, then audience selection, process, examples, limitations and next step. Do not lead with model brands.
- **Layout:** Strong left-aligned or centered hero; four route cards in a 2×2 desktop grid; horizontal process on desktop/vertical mobile; concise pricing strip; primary CTA **Be om løsningsgjennomgang** or **Utforsk løsninger**.

## 4.2 Tjenester / Solutions — `/solutions/`

- **Must include:** Bedrift, Studenter, Privatpersoner and Managed Secure lanes; shared delivery model; Atlas-does/does-not-do boundary; platform/licence model; trust strip; routing CTA.
- **Content buildup:** Define solutions as configured workflows and governance around real needs. Explain discovery, scope, provider fit, configuration, validation and follow-up. Distinguish Atlas from raw model access, generic consulting and unverified secure hosting.
- **Layout:** Intro followed by four large route cards, reusable process component and a concise audience/delivery/next-step comparison.

## 4.3 Bedrift / Business — `/solutions/business-ai/`

- **Must include:** Business problems; concrete work areas; service ladder; delivery process; provider/licence approach; governance; pricing floors; qualification CTA.
- **Content buildup:** Lead with fragmented AI use, inconsistent outputs, unclear data handling, weak ownership and adoption. Show workflows for leadership, sales/marketing, administration, documentation, research and operations. For each example state input, workflow, human review, output and boundary. Explain that customer-owned licences or itemized provider costs may apply.
- **Approved public price floors:** AI Readiness Assessment from NOK 19,000 ex. MVA; Agent Workflow Mapping Sprint from NOK 39,000; Platform Setup Pack from NOK 29,000; Atlas AI Starter from NOK 69,000; Atlas AI Professional from NOK 129,000; Research Multi-Engine from NOK 159,000 plus usage; Managed Workflow Lite from NOK 39,000 setup plus NOK 19,000/month. These are qualification/quote floors, not automatic checkout offers.
- **Layout:** Commercial problem → workflow → proof/boundary → process → pricing → CTA sequence. Use a workflow card grid and a visible governance panel. Primary CTA: **Be om løsningsgjennomgang**.

## 4.4 Studenter / Students — `/solutions/students/`

- **Must include:** Age 16+; responsible study support; permitted/prohibited use; plan comparison; usage caps; privacy/provider boundaries; availability status; FAQ/contact route.
- **Content buildup:** Explain planning, concept understanding, revision, source organization and practice. State that Atlas does not replace independent work, source verification or institutional rules. Users aged 16–17 require the approved adult-payer model; under-16 is excluded.
- **Approved public prices:** Student Basic NOK 129/month incl. MVA; Student Plus NOK 169/month incl. MVA. State monthly renewal, one named user, allowance/hard-cap logic and that current Wix plans are private/non-buyable until release.
- **Layout:** Student-focused hero, use-case cards, side-by-side allowed/not-allowed panel, plan cards, safety block and informational/contact CTA—no purchase button while locked.

## 4.5 Privatpersoner / Consumers — `/solutions/consumers/`

- **Must include:** Everyday scenarios; limitations; privacy/human-review guidance; Everyday Basic plan; deferred Family reference; usage boundaries; current status.
- **Content buildup:** Cover planning, comparison, document understanding, organization and drafting assistance. Avoid presenting Atlas as medical, legal, financial or emergency decision authority. Explain data minimization and verification.
- **Approved public prices:** Everyday Basic NOK 159/month incl. MVA. Family NOK 399/month incl. MVA may appear only as **deferred/not currently available**; no Family CTA or purchasable plan.
- **Layout:** Simple hero, scenario cards, safety/boundary panel, plan summary, getting-started steps and informational/contact CTA.

## 4.6 Plattformer / Platform Lanes — `/platform-lanes/`

- **Must include:** Need-first provider selection; Atlas-managed bounded API lane; customer-owned Microsoft/Google licence lanes; comparison dimensions; decision process; provider-change notice.
- **Content buildup:** Explain that Atlas is provider-neutral and selects a route based on workflow, data, control, integration and cost—not brand preference. Distinguish provider responsibility, customer responsibility and Atlas responsibility. Avoid unsupported partnership or resale claims.
- **Layout:** Decision-tree hero, lane cards, comparison matrix, selection process and links to Tillit and Priser. Date all provider feature/price references.

## 4.7 Managed Secure — `/managed-secure/`

- **Must include:** Qualification-only statement; relevant use cases; qualification criteria; control domains; architecture-review process; unavailable-capability disclosure; price floors; architecture-review CTA.
- **Content buildup:** Explain identity, least privilege, private storage, secrets, network exposure, logging, monitoring, retention/deletion, backup/restore, incident and supplier controls as assessment areas—not completed guarantees. State clearly that secure production delivery is not generally available.
- **Approved public price floors:** Standard from NOK 175,000 setup plus NOK 85,000/month ex. MVA; Enterprise from NOK 300,000 setup plus NOK 125,000/month ex. MVA. Qualification only; architecture, provider, infrastructure and usage may affect final price.
- **Layout:** Restrained hero, control-domain grid, qualification checklist, numbered review process, prominent limitation panel and CTA **Be om arkitekturgjennomgang**.

## 4.8 Priser / Pricing — `/pricing/`

- **Must include:** All approved B2C prices and business/managed floors; MVA labels; billing period; inclusions; usage caps; provider/infrastructure variables; availability status; cancellation/renewal summary; FAQ; qualification CTA.
- **Content buildup:** Begin with how Atlas pricing works, then B2C plan cards, business packages, managed services, what is included, what varies, and current purchase status. Place qualifiers beside each price. Explain that public price display is informational and separate from buyability.
- **Layout:** Segment tabs or anchored sections; price cards for comparable B2C plans; business/managed comparison table; status banner; full inclusion/exclusion and FAQ sections. No active checkout button before release.

## 4.9 Tillit / Trust — `/trust/`

- **Must include:** Governance model; data-flow explanation; provider roles; human review; privacy/security controls; claim/status taxonomy; current limitations; evidence/update practice; links to Legal and Managed Secure.
- **Content buildup:** Separate implemented controls, provider/configuration-dependent controls, target-state controls and unavailable features. Explain what data enters a workflow, where it may go, who reviews it and what is not accepted through public forms. Avoid absolute security/compliance statements.
- **Layout:** Trust pillars, simple data-flow diagram, status-labelled control cards, provider disclosure, human-review panel, limitations/evidence block and contact route.

## 4.10 Ressurser / Resources — `/resources/`

- **Must include:** Business, Student, Consumer, Trust, Secure and Pricing/Usage content clusters; featured resources; author/update/source metadata; FAQ routing; relevant solution CTAs.
- **Content buildup:** Publish practical guides, checklists, explainers and decision tools that answer real questions. Each resource should state audience, direct answer, examples, boundaries, next step, author, publication date, update date and sources where factual.
- **Layout:** Featured resource plus filterable card grid and topic clusters. Keep fewer, stronger resources rather than thin volume.

## 4.11 FAQ — `/resources/faq/`

- **Must include:** Pricing, availability, providers, privacy/data, usage caps, student rules, onboarding and Managed Secure categories; approved CMS publication controls; direct answers; update dates.
- **Content buildup:** Answer the question immediately, then qualification/exception and link to the controlling page. Editorial records remain private; only approved locale-matched records are promoted to the public collection. FAQ schema only when visible content and current eligibility support it.
- **Layout:** Search/category controls and accessible accordions. Keep answers short and route complex topics to full pages. Manually test keyboard, focus, state and screen-reader behavior.

## 4.12 Om oss / About — `/about/`

- **Must include:** Purpose; company identity; operating principles; operating model; verifiable competence; provider relationship; company facts; contact route.
- **Content buildup:** Explain why Atlas exists and its governed workflow approach. State that NanoTech Solutions Norway AS owns/contracts for Atlas AI and that Atlas is an internal business line, not a separate legal entity. Use only verifiable experience and no unsupported team-size/partnership claims.
- **Layout:** Human professional imagery, concise purpose/story section, operating-principle cards and separate company-fact panel.

## 4.13 Kontakt / Contact — `/contact/`

- **Must include:** Contact routing; company/contact details; short form; confidentiality warning; privacy information; success/error states; alternative route.
- **Content buildup:** Request only name, company/organization, email, category and short description. State: **Ikke send konfidensiell, sensitiv eller sikkerhetsgradert informasjon i dette skjemaet.** Do not promise response times unless operational evidence supports them.
- **Layout:** Two-column desktop details/form, single-column mobile. Persistent labels, field-specific errors, clear submission outcome and no file upload.

## 4.14 Oppstart / Onboarding — `/onboarding/`

- **Must include:** Qualification purpose; four-step process; preparation checklist; prohibited submission types; low-risk qualification form; possible outcomes; expectations; trust/legal links.
- **Content buildup:** Explain request → qualification → scope/recommendation → approved next step. Ask for company, contact, target workflow, current platform, urgency and preferred follow-up. State that Oppstart is not checkout and does not guarantee fit, availability, price or result before review.
- **Layout:** Numbered process first, preparation checklist beside/above form, progressive disclosure for optional details and clear confirmation state.

## 4.15 Juridisk / Legal — `/legal/`

- **Must include:** Legal index; version metadata; company identity; privacy; cookies/tracking; terms/status; acceptable use; cancellation/withdrawal; complaints/contact.
- **Content buildup:** Align privacy and cookie text with actual forms, analytics and providers. Cookie choices must be purpose-specific with accept/reject parity and easy withdrawal. Distinguish informational pages, quote-based business engagements and any future consumer checkout. Publish cancellation/withdrawal rules only where supported by approved scope and implementation.
- **Layout:** One controlled hub with anchored sections or versioned document cards. Repeat critical terms beside pricing, forms and future checkout—not only in Legal.

# 5. SEO, AEO and GEO requirements

- Unique title, description, H1, canonical URL and correct index state per page/language.
- Reciprocal `nb-NO`/`en` hreflang only for complete pairs.
- Important content must be visible crawlable text with deliberate internal links.
- Primary pages require a direct-answer block, audience, inclusions/exclusions, provider/data boundary and next step.
- Structured data must match visible content. Do not fabricate reviews, ratings, certifications, prices, availability or partnerships.
- Use Organization, WebSite, BreadcrumbList, Service and Article schema where appropriate; FAQPage only when current eligibility and content conditions are met.
- Resources require author, publication date, update date and source information.
- Current Google guidance supports established SEO fundamentals and useful original content; no special AI file or markup guarantees generative-AI visibility.

# 6. Market and competition interpretation

- Business remains the primary lane because adoption is established while workflow design, governance and implementation maturity remain uneven.
- Native platforms compete strongly on general functionality and seat price. Atlas should not compete as a “better model”.
- Atlas differentiation is configuration, onboarding, provider fit, governance, bounded usage and accountable follow-up.
- Student and consumer pages compete on responsible Norwegian workflows and transparent limits, not generic companion/tutor claims.
- Managed Secure qualifies needs ordinary SaaS/public forms cannot address; it must not claim mature secure-platform parity before evidence exists.
- Provider features and prices are volatile; comparisons require a review date and must not become permanent Atlas promises.

# 7. Current Wix evidence and validation boundary

- Atlas-AI is a Draft Wix Studio site using Norwegian/NOK/Europe-Oslo with Velo enabled.
- Forms, Forms & Payments, Invoices, Members Area, Multilingual and Pricing Plans are installed.
- Engineering evidence identifies 15 public-role page entities plus Account Settings.
- Most page-code files remain boilerplate; Home contains custom metric animation code.
- Three private non-buyable plans exist for Student Basic, Student Plus and Everyday Basic; Family and Managed Secure plans were not created.
- Current evidence does not prove Studio menu hierarchy, slugs, rendered copy, responsive layout, CMS bindings, metadata/hreflang, form routing or live acceptance.

# 8. Required acceptance before release

For each page:

- purpose, audience, CTA and status match this blueprint;
- Bokmål is complete; English has full parity before publication;
- price/MVA/status language matches contract v0.5.1;
- no unsupported performance, security, compliance, residency, partnership or availability claim;
- no confidential-upload route or frontend secret;
- desktop/tablet/mobile and keyboard/focus/contrast/form/reflow/screen-reader QA pass;
- title, description, H1, canonical, index, internal links and hreflang pass;
- structured data matches visible content;
- form routing, privacy and success/error states pass;
- evidence is stored and the exact release candidate receives explicit written approval.

## Validation result

`PASS_AS_CONTROLLED_BLUEPRINT`; Wix implementation `NOT_VALIDATED`; release `NO_GO`.

This blueprint is the controlled page-and-section content contract for continuing Gamma, Figma and Wix Phase 1 work. It does not prove current Wix implementation and does not change any release boolean.
