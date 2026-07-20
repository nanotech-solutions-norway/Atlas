# Atlas AI Figma-to-Wix Section Replacement Map — 19:19, 20.07.2026

## Status

**Classification: AUTO_APPROVED for mapping and implementation sequencing.**

Commercial pricing, provider eligibility, legal/privacy/security claims, route renames, public availability and publication approval remain **PENDING_REVIEW**.

**Wix site:** Atlas-AI, site ID `1448ccad-68f0-43ea-8f0e-c9d8c0366082`  
**Current Wix status:** Draft  
**Figma source status:** 30/30 replacement slides validated PASS  
**Wix mutation in this task:** None

## Replacement-action legend

- **REPLACE:** one Figma section replaces one existing Wix section.
- **MERGE-REPLACE:** one Figma section replaces and consolidates two or more Wix sections.
- **INSERT:** the Figma section is new and must be inserted without deleting a valid existing equivalent.
- **SPLIT-REPLACE:** one Wix section is divided between two Figma sections; the original standalone section is retired.
- **KEEP:** no replacement from the seven-section Figma pack.
- **RETIRE:** remove the existing section/card after its valid content has been absorbed elsewhere.

---

## 1. Home

**Wix target:** Home shell, CMS slug `home`; public route should remain the site root.  
**Figma file:** https://www.figma.com/slides/pYqjywOP26KcONlLFpfSSQ

| Figma order | Figma section | Existing Wix section(s) | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Styrte KI-arbeidsflyter for reelt arbeid | Hero — Styrte AI-løsninger for reelt arbeid | REPLACE | First section. Replace the old security/compliance and operational wording; retain the primary/secondary CTA pattern. |
| 2 | Fra enkeltbruk til styrt arbeidsflyt | Jobs to be Done cards + Pain points vs Atlas response | MERGE-REPLACE | Replace both current sections with one problem→method section. Do not retain the old “five most reported” or unsupported measurable/security claims. |
| 3 | Resultatbaserte løsningsområder | Four business package cards | REPLACE | Replace the four-card legacy offer block with the six outcome-led areas. |
| 4 | Team Workspace eller Managed Secure? | Team Workspace vs Managed Secure | REPLACE | Replace the entire old comparison. Managed Secure remains qualification-only and non-public. |
| 5 | Tillit før kjøp | Trust principles | REPLACE | Replace old operational secure-channel/compliance implications. Link to Trust, Platform Lanes and Legal. |
| 6 | Slik starter en bedriftsleveranse | Onboarding process | REPLACE | Replace time-bound 2–6 week, dedicated-contact, monthly-review and go-live promises. |
| 7 | Start med oppgaven — ikke modellnavnet | Closing conversion | REPLACE | Last content section before footer. Route to solution review and low-risk qualification. |

**Home result:** eight current Wix sections become seven sections because the two middle problem sections are consolidated.

---

## 2. Solutions

**Wix target:** `/solutions`  
**Figma file:** https://www.figma.com/slides/AwXFzwDMiWMsygRJpV3Ej6

| Figma order | Figma section | Existing Wix section | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Prismodell og leverandørkostnader | Pricing logic | REPLACE | Keep in existing section-8 position. Do not publish fixed prices, included provider subscriptions, unlimited use, response times, SLA or automatic activation. |
| 2 | Plattformvalg etter dokumentert kontekst | Platform-selection criteria | REPLACE | Keep in existing section-10 position. Align provider/platform wording to capability classes and current licensing/data context. |

**Keep unchanged, subject to normal Wix QA:** Solutions sections 1–7, 9, 11 and 12. The Figma Solutions pack is targeted, not a full-page replacement.

---

## 3. Packages

**Wix target:** current `/packages` shell for staging. A future `/pricing` route and redirect remain PENDING_REVIEW.  
**Figma file:** https://www.figma.com/deck/iUlIgUQhmSPv2Tti4JWA25

| Figma order | Figma section | Existing Wix section/card set | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Seks resultatbaserte bedriftsområder | Entire legacy seven-card offer grid: Atlas Assist, Marketing Assistant, Developer/Technical Assistant, Accounting Expert, LexisMentor, Wix AI Communicator and Managed Secure Mode | MERGE-REPLACE | Replace the seven equal public product cards with the six outcome-led business areas. Retire the old public product names as primary offers. |
| 2 | Omfanget bestemmes etter behovsavklaring | Any current package comparison, tier or price block; otherwise no valid equivalent | INSERT / REPLACE IF PRESENT | Place directly after outcome areas. Present Starter, Professional, Research/Multi-Engine and Business Workspace as delivery levels, not competing product cards. |
| 3 | Kontrollerte student- og forbrukerspor | Student/private cards if mixed into the main offer grid; otherwise no valid equivalent | INSERT | Place after delivery levels as a clearly secondary route section. Do not mix these cards into the primary business grid. |
| 4 | Kvalifiseringskort — Arkitekturgjennomgang | Atlas Managed Secure Mode package card and any public Managed Secure price/availability block | REPLACE | Place after secondary routes. Remove price and operational availability claims; retain architecture-review-only qualification. |

**Packages retirement rule:** all valid content from the old seven-card grid must be absorbed into the new architecture or moved to scoped use-case content. Do not leave duplicate legacy cards below the replacement sequence.

---

## 4. Governance

**Wix target:** `/governance`  
**Figma file:** https://www.figma.com/deck/GHRYg5KepItU2DNCSWbwTZ

| Figma order | Figma section | Existing Wix section | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Oppdatert styringskart | Platform-plane cards | REPLACE | Replace the stale operating map with Wix, GitHub, Gamma/Figma, Domeneshop and conditional Azure roles. |
| 2 | Release-gate oversikt | Existing nine validation-gate cards | REPLACE | Replace or explicitly map the old nine-card set to G00–G22. Do not display both systems as parallel current gate models. |
| 3 | Hver offentlig påstand må kunne spores | Claims registry section | REPLACE | Use as the visible claims-governance explanation; keep the CMS registry as backend evidence data. |
| 4 | Juridisk og publiseringsmessig beredskap | Legal-document registry | REPLACE | Explain document readiness without implying that registry entries are approved legal documents. |
| 5 | FAQ og answer-engine prinsipp | FAQ cards / AEO guidance section | REPLACE | Keep visible FAQ content aligned with structured data; internal-only AEO guidance should not appear as buyer copy unless useful. |
| 6 | Bilingual parity | Locale and bilingual audit/status section | REPLACE | Use as the final governance status block. Do not describe parity as complete until Bokmål/English content and forms are validated. |

**Governance result:** direct six-to-six replacement. CMS registries may remain as data sources but their old rendered blocks must not remain duplicated.

---

## 5. Process

**Wix target:** `/process`  
**Figma file:** https://www.figma.com/slides/YqapmYRPdgngWFtT8UP8JA

| Figma order | Figma section | Existing Wix section | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Kundens leveranseprosess | No valid current equivalent | INSERT | Insert as the first Process content section. This is the customer-facing delivery sequence and must be separate from the internal programme roadmap. |
| 2 | Phase 0–6 med evidens før status | Entire current phase-card roadmap, currently Phase 0/0.5/1–5 | REPLACE | Replace the full stale roadmap with Phase 0–6. Preserve Draft/NO-GO wording and evidence-before-status logic. |

**Process result:** one new customer-facing section plus one full roadmap replacement.

---

## 6. Managed Secure

**Wix target:** current `/managed-secure-mode` shell for staging. Rename to `/managed-secure` only after destination and redirect validation.  
**Figma file:** https://www.figma.com/slides/Iq2cGzkBoN4Xbwhvu0mZ7t

| Figma order | Figma section | Existing Wix section(s) | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Arkitekturgjennomgang for kontrollsensitive behov | Hero and architecture-review CTA + What an architecture review is | MERGE-REPLACE | Replace both opening sections. State evidence-gated qualification, not an available secure service. |
| 2 | Når et kontrollert arkitekturspor kan vurderes | When Azure should be considered + Who the review is for + qualification part of Technical and organisational questions | MERGE-REPLACE / SPLIT-REPLACE | Use provider-neutral conditional criteria. Retire the old standalone Azure and audience sections after absorption. |
| 3 | Velg laveste tilstrekkelige kontrollnivå | Control-level tier diagram + Do not overbuild low-risk needs + Starter/Workspace alternatives | MERGE-REPLACE | Replace all three with the four-level control framework. Do not retain the generic English diagram or incorrect package hierarchy. |
| 4 | Hva som må dokumenteres før Managed Secure kan beskrives som operativt | Evidence before public claim + Controlled-delivery components + evidence/checklist part of Technical and organisational questions | MERGE-REPLACE / SPLIT-REPLACE | Convert current capability claims into a future acceptance checklist. The original technical/questions section is split between slides 2 and 4 and then retired. |
| 5 | Start med kontrollkravet — uten vedlegg | Final CTA | REPLACE | Last content section before footer. Route only to low-risk architecture-review intake; no files or sensitive details. |

**Managed Secure retirement rule:** remove all standalone claims of operational Azure orchestration, isolation, private storage, logging, backup, incident handling, SLA, residency, compliance or secure delivery unless later supported by approved evidence.

---

## 7. Contact

**Wix target:** `/contact`  
**Figma file:** https://www.figma.com/slides/xHQOe7uKx2bmiPpgIxQAvA

| Figma order | Figma section | Existing Wix section(s) | Action | Placement / implementation note |
|---:|---|---|---|---|
| 1 | Lavrisiko kontaktkontrakt | Hero — low-risk contact + What can safely be sent + What must not be sent | MERGE-REPLACE | Replace the first three sections with one visible data-boundary section. Remove deletion/non-processing promises not operationally proven. |
| 2 | Riktig rute etter overordnet behov | Audience route selection + Business enquiry fields + Student/private enquiry fields | MERGE-REPLACE | Replace the route and separate audience-field sections. The actual form remains a Wix-native form below this section and must use one minimal field contract. |
| 3 | Når behovet kan kreve høyere kontroll | Higher-security needs process | REPLACE | Replace any promise of encrypted channel or operational Managed Secure continuation with a stop-and-qualify flow. |
| 4 | Etter innsending | Final CTA and status promise | REPLACE | Replace response-time, confidentiality and no-sharing promises with validated possible-status language and MANUELL VALIDERING KREVES. |

**Contact component rule:** do not replace the actual Wix form with a Figma image or static design. Reconfigure the native form and place it after section 2, with the no-sensitive-upload warning visible at the form.

---

## 8. Intake

**Wix target:** `/intake`  
**Replacement from the seven-section Figma pack:** **NONE**

The current approved content contract remains **Onboarding v3**. Keep and implement its eight-section sequence:

1. low-risk qualification hero;
2. audience selection;
3. need and data classification with a technical stop rule;
4. preferred next step;
5. business intake;
6. architecture review;
7. collect/do-not-collect boundary;
8. possible status after submission.

Do not substitute the Contact deck for the Intake page. Contact is the short public entry point; Intake is the fuller qualification journey.

---

## Implementation order

1. **Home** — complete full-page replacement; highest conversion impact.
2. **Contact** — replace content and reconfigure the native low-risk form.
3. **Managed Secure** — replace all high-risk future-state sections before any public preview.
4. **Packages** — retire the legacy card architecture and install the four-section sequence.
5. **Process** — insert customer journey and replace stale roadmap.
6. **Governance** — replace six rendered sections while preserving CMS evidence records.
7. **Solutions** — perform the two targeted replacements only.
8. **Intake** — implement Onboarding v3 separately; no replacement from this pack.

## Global implementation constraints

- Modify existing Wix pages in place; do not create duplicate pages unless explicitly approved.
- Preserve headers, footers and global navigation unless a separate approved change requires modification.
- After every replacement, delete or hide the superseded rendered section so duplicate claims do not remain.
- Keep CMS evidence collections where needed, but do not continue rendering stale records.
- Validate desktop, tablet and mobile layouts after insertion.
- Validate CTA targets, keyboard order, contrast, metadata, schema, forms, error states and multilingual parity.
- Managed Secure remains architecture-review-only and non-public.
- Public forms remain low-risk only and must not accept confidential files or sensitive material.
- Figma PASS does not establish Wix release readiness.
- Phase 1 public deployment remains NO-GO until launch gates and explicit release approval pass.
