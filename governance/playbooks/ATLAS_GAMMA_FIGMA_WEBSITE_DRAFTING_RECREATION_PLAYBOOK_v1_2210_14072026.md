# Atlas AI Gamma and Figma Website Drafting and Recreation Playbook — 22:10, 14.07.2026

**Version:** 1.0  
**Project:** Atlas AI  
**Classification:** AUTO_APPROVED workflow and quality-control baseline, with commercial, legal, provider, security, production and publication items retained as PENDING_REVIEW.

## 1. Purpose

This playbook governs the end-to-end creation of Atlas AI website-reference alternatives in Gamma, the card-level assessment of those alternatives, the synthesis of the strongest approved content, the reconstruction of that content as editable Figma Slides, and the controlled handoff to Wix.

Gamma and Figma are design and content evidence. Neither surface proves that functionality, pricing, entitlement, legal publication, secure architecture, provider rights, checkout, production availability or launch approval exists.

## 2. Mandatory project boundary

This workflow applies only to Atlas AI project material unless the user explicitly adds another source.

Before substantive work:

1. Activate Atlas project memory and read the latest available approved learning, decision, error, validation, source-authority and session-close records.
2. Read the latest approved project sources in Google Drive, GitHub, uploaded files and the current Atlas project context.
3. Apply only entries marked `APPROVED`, `AUTO_APPROVED` or `CANONICAL` as governing rules.
4. Treat `PENDING_REVIEW` entries as advisory and preserve their status.
5. Flag contradictions and prefer the most recent approved canonical source. Never silently merge conflicts.

Preserve the Atlas safety and publication locks:

- no real-money betting;
- no auto-betting;
- no bookmaker execution;
- no public write endpoint;
- no frontend provider tokens;
- no public production availability unless explicitly approved;
- no secrets, credentials, tokens, customer-confidential information, bank/accounting data or private commercial data in Gamma, Figma, GitHub, Drive write-backs, prompts, screenshots, exports or reports.

## 3. Source-authority order

Apply the following order:

1. Current explicit user instruction.
2. Approved/canonical Atlas instructions, decisions, validation records and exact corrections.
3. Latest approved page contract, route, claim and commercial source.
4. Approved Gamma source for card order, component hierarchy, draft-specific visual treatment and source assets.
5. Latest approved page-specific technical drawing, measurement report, Figma reference or design-token source.
6. Existing target Figma file.
7. Older, superseded or advisory sources.

When sources conflict, identify the sources and dates, preserve the conflict in the register, apply the latest approved canonical source when identifiable, and classify unresolved pricing, legal, provider-policy, security, production and publication matters as `PENDING_REVIEW`.

## 4. Platform roles

| Surface | Authorised role | Prohibited interpretation |
|---|---|---|
| Gamma | Explore two webpage alternatives, card hierarchy, diagrams, matrices, CTA patterns and visual options | Not proof that functionality, pricing, legal status, provider entitlement, secure architecture or public availability exists |
| Figma Slides | Reconstruct the approved best-of concept as editable measured design evidence and validate layout/source traceability | Not the production website and not launch approval |
| Wix | Implement the final approved responsive website, routes, forms, CMS, SEO and links | Must not inherit unreviewed Gamma/Figma claims or publish before launch gates pass |
| GitHub | Canonical route/copy/claim/release governance, prompts, logs, decisions, errors and validation evidence | Must not contain secrets or confidential evidence |
| Google Drive | Controlled source documents, packages, evidence and approved report write-back | Upload time alone does not establish authority, version or approval status |

## 5. Phase 1 drafting scope and naming

The latest validated Phase 1 reference inventory contains 37 page concepts and 74 intended v1/v2 drafts. The primary concepts are:

- Business AI Work Solutions;
- Student AI Study Solutions;
- Consumer AI Everyday Solutions;
- Pricing;
- Platform Lanes;
- Trust;
- Onboarding;
- Resources;
- About;
- Legal.

Supporting Phase 1 concepts include provider lanes, trust/governance pages, intake/onboarding pages, resource guides and legal/disclosure pages.

For every new or replacement Gamma draft, use the exact page-tree name:

```text
<Canonical Page Name> v1
<Canonical Page Name> v2
```

Examples:

```text
Business AI Work Solutions v1
Business AI Work Solutions v2
Student Intake v1
Student Intake v2
```

Current short titles such as `Business v1` or `Student v2` remain historical evidence until manually renamed or replaced. Select one canonical Gamma ID for every page/version before Figma work begins.

Before generation, check existing Wix pages, existing Gamma records and existing Figma decks. Do not create duplicates unless a restart or alternative is explicitly authorised.

## 6. Stage A — Page contract

Create one controlled page contract per page before Gamma generation. Required fields:

- canonical page name and route;
- audience and primary user question;
- primary visitor outcome;
- offer/status: public approved, early access, qualification-gated, proposed or `PENDING_REVIEW`;
- approved claims and claim IDs;
- prohibited claims and wording;
- Atlas/provider responsibility boundary;
- permitted and prohibited data;
- primary and secondary CTA text and destination class;
- mandatory content modules;
- SEO/AEO query intent;
- accessibility requirements;
- governing page-specific measurement/design source;
- content, claim, commercial/legal, design and implementation review owners.

Do not generate alternatives when the route is unresolved, the page duplicates an existing artefact, pricing/entitlement is presented as final without approval, the provider relationship is unclear, a public form would collect sensitive information, or the page would imply unapproved production availability. Non-conflicting work may continue only with the unresolved item labelled `PENDING_REVIEW`.

## 7. Stage B — Two controlled Gamma alternatives

Both alternatives must use the same approved facts, claims, status labels, route, provider boundary, data boundary, pricing status and safety controls. They may differ only in information architecture, pacing, card types and visual emphasis unless an explicit alternative decision is recorded.

### v1 — Outcome-first / conversion-led

Use a concise, action-oriented sequence:

1. clear audience/problem/outcome hero;
2. immediate fit or decision block;
3. three to five outcome cards;
4. how it works or user journey;
5. evidence or qualification block;
6. boundaries and exclusions;
7. offer/status block;
8. primary CTA and low-risk next step.

### v2 — Trust-first / explanatory

Use a more detailed, governance-led sequence:

1. purpose and controlled-status hero;
2. context and visitor problem;
3. Atlas versus user/provider responsibility;
4. process or architecture diagram;
5. provider/data/security boundary;
6. comparison or decision matrix;
7. evidence and limitations;
8. CTA with qualification or onboarding route.

The following may not differ between v1 and v2 without a recorded decision: prices, quotas, entitlements, provider/model availability, package names, routes, legal dates, data handling, provider ownership, security/residency status, public availability and claim qualifiers.

## 8. Stage C — Gamma generation and duplicate control

Generation settings for each page:

- destination: `Atlas AI 3.1`;
- format: webpage;
- dimensions: fluid;
- language: Norwegian Bokmål for public Atlas pages unless an approved exception applies;
- exact canonical title plus v1/v2;
- one generation call per alternative;
- sufficient text to fulfil the page contract without unsupported filler;
- use placeholders where approved/original visuals are unavailable.

Core prompt:

> Create an Atlas AI webpage draft titled exactly `[CANONICAL PAGE NAME] v[1 or 2]` and place it in the approved Atlas AI 3.1 folder. Work only from the attached page contract and approved Atlas sources. Preserve all status labels, provider boundaries, data boundaries, claim qualifiers, pricing status and safety restrictions exactly. Do not invent operational functions, portals, gateways, automatic routing or scoring, audit logs, fixed review periods, DPAs, technical isolation, certifications, provider partnerships, model performance, residency, uptime, public availability or launch readiness. Use Norwegian Bokmål with correct grammar unless the page contract states otherwise. Alternative v1 must be outcome-first and conversion-led. Alternative v2 must be trust-first and explanatory. Use editable cards, process blocks, matrices, callouts and CTA sections suitable for later reconstruction in Figma Slides. Gamma is a design reference only and must not state that a proposed feature is already implemented.

After generation:

1. re-list the folder and allow asynchronous completion before retrying;
2. verify exact titles;
3. record Gamma ID, URL, created/updated timestamps and title;
4. if a title is wrong, create one exact-name replacement;
5. flag duplicate/misnamed drafts;
6. manually archive/delete duplicates in the Gamma editor because the connector cannot rename or delete them;
7. select one canonical ID per page/version.

## 9. Stage D — Card inventory

Read every card/section in both alternatives. Never rank from a thumbnail or title.

Record for every card:

- page, draft title, Gamma ID/URL and v1/v2;
- card number and Gamma section ID;
- heading, purpose and component type;
- complete copy and key values;
- image, icon, video, chart, table, diagram and CTA locations;
- source-specific colours and hierarchy;
- claim IDs/evidence references;
- provider, data, security, legal, pricing and availability statements;
- duplicate/near-duplicate relationship;
- contradictions;
- Figma transfer implications;
- recommended disposition.

Allowed dispositions:

`RETAIN`, `RETAIN_WITH_COPY_FIX`, `RETAIN_WITH_QUALIFIER`, `MERGE`, `SPLIT`, `ALTERNATIVE`, `EXCLUDE_DUPLICATE`, `EXCLUDE_UNSUPPORTED`, `PENDING_REVIEW`.

## 10. Stage E — Card scoring

Score each card out of 100:

| Criterion | Weight |
|---|---:|
| Claim accuracy and evidence traceability | 25 |
| Governance, safety and boundary integrity | 15 |
| Strategy and route alignment | 15 |
| Audience clarity and value proposition | 10 |
| Information architecture and component fit | 10 |
| Journey and CTA contribution | 10 |
| Visual hierarchy and Figma transferability | 10 |
| SEO, AEO and accessibility readiness | 5 |
| **Total** | **100** |

Rating bands:

- 90–100: A, preferred;
- 80–89: B, strong;
- 70–79: C, usable;
- 60–69: D, weak;
- below 60: E, reject.

A high score cannot override a hard gate.

### Hard gates

- `C1 Unsupported public claim`: exclude or replace with supported qualified wording.
- `C2 Canonical conflict`: `PENDING_REVIEW`; do not merge.
- `C3 False implementation status`: reject or rewrite as proposed/future-state/qualification-gated.
- `C4 Absolute or prohibited language`: reject until corrected.
- `C5 Sensitive-data intake`: reject and redesign as low-risk routing.
- `C6 Legal/commercial approval`: retain `PENDING_REVIEW`; never publish as final.
- `C7 Provider ownership ambiguity`: correct or exclude.

## 11. Stage F — Best-of synthesis

Apply this order:

1. remove cards that fail hard gates;
2. remove exact duplicates;
3. resolve canonical-source conflicts;
4. select the highest-scoring card for each required page role;
5. retain unique high-value cards from the other alternative;
6. merge only when meanings, values, claims, qualifiers and status agree;
7. split tall or overloaded cards when meaning is preserved;
8. retain unresolved alternatives separately and mark `PENDING_REVIEW`;
9. verify that the final sequence answers the user’s questions and supports the approved CTA.

Do not merge solely because the visual designs are attractive. Maintain source traceability for every retained, merged or split card.

## 12. Stage G — Figma file model and source-to-slide map

Default outcome for one page concept: one durable editable Figma Slides file containing one synthesised best-of presentation.

Recommended name:

```text
Atlas AI - <Canonical Page Name> - Synthesised v1
```

Do not create separate Figma v1/v2 decks unless explicitly requested. The Gamma alternatives are exploration inputs; Figma is normally the controlled best-of result.

Before writing to Figma, create a complete source-to-slide map containing:

- final slide number and title;
- source Gamma drafts, card numbers and section IDs;
- retained/merged/split/alternative status;
- component type and layout intent;
- governing measurement source;
- visual or placeholder requirement;
- unresolved review item.

Every Gamma card must have a documented disposition.

## 13. Stage H — Design-system extraction

Read the latest approved measurement/design source for the target page. Extract slide size, safe margins, content width, fonts, font sizes, line heights, colour roles, border widths, radii, gaps, card padding, CTA dimensions, recurring components and page-specific exceptions.

The validated Business v1/current primary-deck profile includes:

- 1920 × 1080, 16:9;
- Roboto and Roboto Slab;
- 104 px validated side margins and 1712 px content width;
- common 32 px gaps/padding;
- `#15213F`, `#3257B8`, `#476FD6`, `#E9ECF2`, `#CFD2D8`, `#FFFFFF`;
- display H1 approximately 72 px, with an approved denser 54 px variant;
- CTA approximately 78 px high, 36 px horizontal padding and 16 px internal spacing;
- dynamic text-sized labels with approximately 14 px padding and 2 px blue border;
- editable visual placeholders and icon placeholders displaying only `icon`;
- CTA hyperlinks excluded unless explicitly requested.

These values are a validated source profile, not universal geometry. Do not apply Business-specific pricing or hero structures to unrelated pages unless the latest page-specific source selects them.

## 14. Stage I — Figma build rules

- Use Figma Slides, not a design file.
- Inspect existing decks first and avoid duplicates.
- Modify existing slides in place unless a restart is explicitly requested.
- Build in controlled batches, normally three to five slides per write.
- Load the actual font/style before every text mutation.
- Append nodes to their final parent before setting x/y.
- Use editable text, shapes, frames, cards, labels, borders, tables and diagrams.
- Do not flatten the working source.
- Return all created/mutated node IDs after every write.
- Do not create unused variables or tokens.
- Apply the active slide grid in the approved order and name rows/slides clearly.

When a Gamma card is too tall:

1. optimise spacing within approved tolerances;
2. use an approved denser component variant;
3. split into two traceable slides;
4. request review if splitting changes meaning or hierarchy.

Do not shrink text below the approved minimum or convert vertical cards into tables merely to save space.

### Placeholder policy

Ordinary visuals:

```text
[ASSET-GAMMA-<DRAFT>-C<CARD>-<TYPE>-<INDEX> | project: Atlas AI | draft: <title> | card: <number> | section: <section-id> | source: <description>]
```

Icon placeholders must visibly contain only:

```text
icon
```

Keep placeholders editable. Store full source details in layer names, notes, the source map or validation register.

## 15. Stage J — Figma validation

### Structural audit

Validate:

- direct file access;
- slide count and order;
- actual slide-row/node-tree structure;
- correct dimensions;
- zero out-of-bounds objects;
- zero clipped text;
- zero text/component overlap;
- no accidental duplicate slides;
- no hidden conflicting/superseded content;
- no unintended flattened objects;
- all placeholders present and labelled;
- complete source traceability;
- no secrets, private data, prohibited claims or unapproved production statements.

For multi-batch builds, validate the actual tree:

```text
SLIDE_GRID > SLIDE_ROW > SLIDE
```

Do not rely exclusively on `figma.getSlideGrid()` immediately after a write because a stale helper result has previously occurred while the underlying tree was correct.

### Measurement audit

Use the tolerance stated by the governing measurement source; the normal desktop tolerance is approximately ±2 px. Check dimensions, margins, content width, grids, gaps, padding, typography, line height, label fit, borders, radii, CTA geometry, source colours, visual location and component hierarchy.

### Visual-fidelity audit

Capture and compare the title slide, at least one representative card slide, every source-specific exception, every merged/split slide, every unresolved alternative and the closing CTA slide against the relevant Gamma cards, technical drawing, Figma reference and source-to-slide map.

A zero-OOB result is not sufficient. Do not claim Gamma fidelity when component hierarchy, visual position, typography or spacing materially differs.

### Content and claim audit

Confirm exact prices, units, qualifiers and status labels; provider/Atlas responsibilities; evidence provenance; qualification-gated Managed Secure/Azure language; low-risk forms; retained legal/commercial `PENDING_REVIEW` labels; and absence of absolute security, compliance, accuracy, ROI or availability language.

## 16. Wix handoff and launch gates

Figma completion does not create the website. Wix implementation must:

1. use canonical GitHub routes;
2. use approved copy and claim IDs, not unreviewed Gamma text;
3. recreate the responsive component hierarchy;
4. replace placeholders with approved assets;
5. wire approved CTA links, forms and navigation;
6. maintain low-risk intake rules;
7. implement metadata, internal links, structured data, direct-answer blocks and accessibility semantics;
8. validate at 1440, 1200, 1024, 768, 390 and 320 px;
9. confirm no clipping, overlap or horizontal overflow;
10. pass all launch gates before publication.

A hard NO-GO applies when a blocking criterion fails, evidence is missing, a claim is unsupported, a data flow is unapproved or public availability has not been approved. No Gamma or Figma score overrides the launch gates.

## 17. Required registers

Maintain:

- Gamma draft register;
- card/claim review register;
- best-of selection matrix;
- source-to-slide register;
- measurement and validation record;
- error register;
- Atlas Project Log Update Pack.

The project log must include timestamp, task, issue, root cause, corrective rule, evidence, action, validation result, unresolved items and classification.

## 18. Current status at adoption

- Active Source 00–12 from 11.07.2026 is the consolidated content/governance baseline; later approved logs provide subsequent corrections.
- Phase 1 Gamma inventory contains 37 page concepts and 74 intended v1/v2 drafts, with duplicate/misnamed records requiring manual cleanup.
- Card-level QA is partial; the full card-by-card scoring/hard-gate audit is not complete.
- Business plus nine primary Figma page decks exist.
- Direct read-only inspection on 14.07.2026 confirmed that each current primary deck contains eight 1920 × 1080 slides and zero top-level out-of-bounds elements.
- This is a structural result only. Visual-fidelity review, asset replacement, complete claim audit, commercial/legal approval and Wix implementation remain incomplete.

## 19. Definition of done

A page recreation is complete only when:

1. the page contract is approved or unresolved items are labelled;
2. v1/v2 Gamma drafts have exact names and canonical IDs;
3. every card is inventoried, scored and assigned a disposition;
4. hard claim/safety gates are applied;
5. the best-of matrix and source-to-slide map are complete;
6. the Figma Slides file is durable, editable and source-traceable;
7. structural, measurement, content, claim and visual audits pass;
8. manual asset and Wix tasks are listed;
9. all commercial/legal/provider/security/release items remain `PENDING_REVIEW` until approved;
10. GitHub/Drive records and the Atlas Project Log Update Pack are written back and validated.

Completion of Figma is not completion of the website. Public completion requires Wix implementation and every blocking launch gate to pass.

## 20. Decision classification

### AUTO_APPROVED

- exact page-name and route corrections;
- duplicate avoidance and canonical Gamma ID control;
- two alternatives using the same facts;
- card scoring and source-traceability rules;
- Figma node-tree and zero-OOB validation rules;
- page-specific measurement extraction;
- validated non-sensitive bug fixes and QA improvements.

### PENDING_REVIEW

- final pricing, quotas, boosts, entitlements and checkout;
- legal wording, dates, entity details and publication status;
- provider/model inclusion and commercial delivery rights;
- partnership, certification or compliance claims;
- secure runtime, logging, isolation, residency and production architecture;
- public availability, paid runtime, release and Wix publication decisions;
- changes to the Atlas safety posture or sensitive-data handling.
