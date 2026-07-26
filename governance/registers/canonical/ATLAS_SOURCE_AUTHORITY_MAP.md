# ATLAS SOURCE AUTHORITY MAP

**Project:** Atlas Website / Atlas AI  
**Created:** 02:29, 25.07.2026 Europe/Oslo  
**Canonical repository:** `nanotech-solutions-norway/Atlas`  
**Repository path:** `governance/registers/canonical/`  
**Drive mirror:** https://drive.google.com/drive/folders/1cXjuJQONMu9lEDYqk6uc62SKJqnTWKiz

> **Authority rule:** The file is a canonical container. Each entry has its own classification. Only entries marked `CANONICAL`, `APPROVED`, or `AUTO_APPROVED` may be applied as governing instructions. `PENDING_REVIEW` entries are advisory and must not be represented as approved decisions.

## Governing hierarchy

When sources conflict, apply this order:

1. **Explicit current user approval or correction.**
2. **`CANONICAL` or `APPROVED` entry in `ATLAS_DECISIONS_REGISTER.md`.**
3. **Approved Atlas governance records in the canonical GitHub repository.**
4. **Current implementation evidence from the system being assessed.**
5. **Current official provider, regulator, standards or statistical sources.**
6. **Controlled Drive source-pack documents and approved reports.**
7. **Gamma and Figma drafts as content/design evidence.**
8. **Prior chats and transfer packs as historical context.**
9. **Inference, clearly labelled.**

A lower source cannot silently override a higher source. Contradictions must be recorded in the decision or error register.

## Platform roles

| Platform/source | Authoritative for | Not authoritative for | Current role |
|---|---|---|---|
| GitHub | Canonical machine-readable governance registers, ADRs, controlled specifications, validation records and release history | Current Wix editor page existence without implementation evidence | Primary canonical governance source |
| Google Drive | Controlled source-pack mirror, human-readable documents, evidence archives and approved exports | Git branch state or live Wix runtime state | Controlled mirror and evidence archive |
| Wix | Current website/CMS/forms/business-entity implementation state when verified through authoritative APIs/editor evidence | Canonical governance policy or design intent by itself | Public/commercial implementation plane; currently Draft / NO-GO |
| Gamma | Copy, hierarchy, alternative drafts and design-content evidence | Current Wix implementation, operational runtime or approved legal status | Draft/content evidence |
| Figma | Visual design, geometry, section/page composition and validation evidence | Current Wix implementation, runtime availability or legal approval | Design evidence |
| Azure or other secure backend | Identity, private storage, runtime, audit, entitlement and controlled delivery after implementation | Public marketing source | Not operationally validated for Atlas Website current phase |
| Current official external sources | Provider, legal, standards, regulator and market facts | Atlas-specific implementation or approvals | External evidence only |
| Generated external research report | Source-cited research evidence after complete artifact ingestion and verification | Canonical decision, legal approval, implemented control or release approval by itself | `EVIDENCE_ONLY` until stored, versioned, reviewed and classified |
| Professional legal or tax memorandum | Version-specific professional advice within its stated scope, assumptions and effective date | General project release approval or implementation evidence by itself | `PENDING_REVIEW` until received, sanitized, classified and accepted |
| Static schema or test vector | Interface and negative-path design when versioned and reviewed | Operational endpoint, runtime control, acceptance evidence or release approval | Non-public implementation foundation only |

## Current controlling Atlas sources

| Source | Date | Authority | Scope |
|---|---:|---|---|
| Explicit Atlas project protocol in current project instructions | Current | `CANONICAL` | Memory, classifications, safety locks, contradiction handling |
| `02_Atlas_AI_Phase_by_Phase_Implementation_Guide_1135_11072026` | 11.07.2026 | Approved consolidated working baseline | Active Phase 0–6 execution sequence |
| `Atlas AI Website Phase Page Roadmap` | 23.07.2026 | Approved/AUTO_APPROVED | Final page roles by phase |
| `Atlas AI Wix Page-Tree Correction` | 23.07.2026 | `AUTO_APPROVED` | Current visible Wix page inventory |
| `Atlas AI Wix CMS, Discovery and Navigation Update` | 22.07.2026 | `AUTO_APPROVED` for verified CMS state | CMS records, locks and manual work |
| Trust/Contact/Legal Workstream Status | 24.07.2026 | Mixed: technical findings `AUTO_APPROVED`; claims `PENDING_REVIEW` | Gamma/Figma/Wix trust/legal work |
| These six canonical register files | 25.07.2026 | Canonical containers; entry status governs | Ongoing project memory and control |
| `ATLAS_CONSUMER_LAW_REPORT_REVIEW_0208_26072026.md` | 26.07.2026 | Verified checkpoints `AUTO_APPROVED`; interpretations `PENDING_LEGAL_REVIEW` | Consumer-law evidence boundary and readiness |
| `ATLAS_CONSUMER_LAW_AND_CHECKOUT_DEEP_RESEARCH_REPORT_0206_26072026.md` and associated legal/MVA packs | 26.07.2026 | Research/draft evidence; interpretations require professional review | Consumer terms, checkout, withdrawal, cancellation, refunds and MVA design |
| `ATLAS_EXTERNAL_SOURCE_VALIDATION_UPDATE_0308_26072026.md` | 26.07.2026 | Verified current-source facts `AUTO_APPROVED`; Atlas decisions remain pending | Current legal, tax, Wix, minor/privacy and accessibility validation |
| `ATLAS_PROFESSIONAL_LEGAL_TAX_DECISION_PACK_0308_26072026.md` | 26.07.2026 | `AUTO_APPROVED` as review-preparation workflow; answers absent | Version-specific professional decision request |
| `ATLAS_FAIL_CLOSED_CONSUMER_CHECKOUT_IMPLEMENTATION_BACKLOG_0308_26072026.md` and schemas/test vectors | 26.07.2026 | Non-public design/workflow `AUTO_APPROVED`; runtime/release not approved | Next executable implementation foundation |

## Conflict protocol

1. Identify the exact conflicting statements.
2. Record source name, date, owner and classification.
3. Prefer the most recent higher-authority approved source.
4. Do not combine incompatible values into a synthetic compromise.
5. Mark the displaced record `SUPERSEDED` or `EVIDENCE_ONLY`.
6. Add a `PENDING_REVIEW` decision when approval is required.
7. Update affected claims, routes, pages, designs and release gates only after the governing entry is approved.
8. Preserve historical evidence.

## Report-ingestion protocol

1. Store the complete report artifact in canonical GitHub and controlled Drive.
2. Record stable title, generation timestamp, version and checksum.
3. Verify citations, effective dates and statutory wording against primary sources.
4. Record contradictions and unresolved interpretations.
5. Classify each resulting rule or decision independently.
6. Do not mark legal, implementation or release gates passed solely because a report exists.

## Professional-review ingestion protocol

1. Store the complete professional deliverable privately in controlled Drive.
2. Record title, reviewer, date, scope, assumptions, covered versions and confidentiality classification.
3. Store only a sanitized approval record in GitHub unless explicit approval permits the full document.
4. Separate approved, conditional, rejected and outside-scope conclusions.
5. Do not generalize a version-specific or conditional conclusion.
6. Re-run source, implementation and release validation after applying accepted decisions.

## Sensitive-data boundary

Never store or expose:

- API keys, access tokens, passwords or credentials;
- bank/accounting data;
- confidential customer or supplier data;
- protected artifacts or private commercial logic;
- customer prompts or submitted files;
- secrets in screenshots, URLs, frontend JavaScript, GitHub, Drive logs, Gamma or Figma.

Sanitized evidence must reference the existence and result of a test without reproducing sensitive content.