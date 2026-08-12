# General Figma/Gamma Design Reconciliation Transfer Pack — 14:08, 12.08.2026

**Version:** 1.0  
**Scope:** project-agnostic website/page/deck drafting, Gamma/PDF/PPTX-to-Figma reconciliation, measured design correction, QA, validation, debugging, governance and handoff  
**Classification:** `AUTO_APPROVED_TEMPLATE`  
**Authority status:** This file is a reusable template. It does **not** become canonical for a new project until that project's owner explicitly adopts it or maps it into that project's approved governance.  
**Security:** Do not store or expose credentials, API keys, secrets, confidential customer data, private commercial data, banking/accounting data or protected source material in public repositories, public design files, screenshots, URLs or logs.

---

## 1. Purpose

Use this transfer pack to reproduce a controlled design-reconciliation workflow in another project without carrying over project-specific names, claims, commercial facts, routes, legal positions or release decisions.

The workflow is designed for situations where a project has one or more of the following:

- a Gamma webpage/presentation source;
- PDF and/or PPTX exports;
- existing Figma Slides or Figma Design files;
- a previously validated reference design;
- a requirement to correct typography, spacing, card geometry, images, controls or source drift;
- GitHub and Google Drive project records;
- a need for repeatable validation, debugging and traceable handoff.

The workflow separates **design evidence** from **runtime implementation**. A Figma pass never proves that a website, application, payment flow, backend, entitlement, legal status, security control or production release has been implemented.

---

## 2. Bootstrap variables

Before using this pack, resolve the following variables. Do not begin mutation until the required values are known.

```text
PROJECT_NAME=
PROJECT_OWNER=
PROJECT_REPOSITORY=
PROJECT_REPOSITORY_BRANCH=
PROJECT_DRIVE_ROOT=
PROJECT_DRIVE_LOG_FOLDER=
PROJECT_MEMORY_ROOT=
FIGMA_PROJECT_OR_FOLDER_URL=
FIGMA_TARGET_FILE_URL=
FIGMA_TARGET_FILE_KEY=
GAMMA_SOURCE_URL=
SOURCE_PDF_FILENAME=
SOURCE_PPTX_FILENAME=
REFERENCE_FIGMA_URL=
REFERENCE_REPORTS=
PUBLIC_RELEASE_STATE=
TARGET_LANGUAGE=
```

Optional source variables:

```text
DESIGN_SYSTEM_SOURCE=
COPY_SOURCE=
CLAIMS_SOURCE=
MEASUREMENT_SOURCE=
ROUTE_SOURCE=
LEGAL_SOURCE=
COMMERCIAL_SOURCE=
SECURITY_SOURCE=
```

If a variable is not applicable, set it explicitly to `N/A`. Do not silently infer a missing authority source.

---

## 3. Required governance files

For a new project, create or identify the following six control files before substantive work:

1. `PROJECT_LEARNING_LOG.md`
2. `PROJECT_DECISIONS_REGISTER.md`
3. `PROJECT_ERROR_REGISTER.md`
4. `PROJECT_VALIDATION_REGISTER.md`
5. `PROJECT_SOURCE_AUTHORITY_MAP.md`
6. `PROJECT_SESSION_CLOSE_LOG.md`

Recommended additional working registers:

7. `PROJECT_DESIGN_BASELINE.md`
8. `PROJECT_SOURCE_TO_SLIDE_REGISTER.md`
9. `PROJECT_MEASUREMENT_REGISTER.md`
10. `PROJECT_ASSET_REGISTER.md`
11. `PROJECT_CLAIM_AND_COPY_REGISTER.md`
12. `PROJECT_RELEASE_GATE_REGISTER.md`

Only records explicitly classified as approved/canonical by the target project may govern execution.

### Classification vocabulary

Use at least:

- `CANONICAL` — explicitly adopted as controlling for the target project;
- `APPROVED` — explicitly owner-approved within stated scope;
- `AUTO_APPROVED` — exact correction, validated non-sensitive bug fix or non-controversial workflow/QA improvement;
- `PENDING_REVIEW` — advisory only; approval required;
- `EVIDENCE_ONLY` — observed/source material, not instruction;
- `SUPERSEDED` — historical record retained but no longer controlling;
- `REJECTED` — explicitly rejected.

Do not invent hybrid approval states without defining them in the target project's governance schema.

---

## 4. Source authority order

Use the following default hierarchy unless the target project already has an approved hierarchy:

1. explicit current owner/user instruction;
2. current `CANONICAL` or `APPROVED` project decisions;
3. approved project standards and governance records;
4. current implementation evidence from the exact system being assessed;
5. current official provider/regulator/standards sources when external facts are in scope;
6. controlled project Drive reports and source packages;
7. current Gamma/Figma/PDF/PPTX artifacts as design/content evidence;
8. prior chats, transfer packs and historical notes;
9. inference, clearly labelled.

A lower-authority source must not silently override a higher-authority source.

When two sources conflict:

1. identify the exact conflicting statements/measurements;
2. record source name, version/date and classification;
3. prefer the most recent higher-authority approved source;
4. preserve the displaced source as historical evidence;
5. do not synthesize a compromise value merely to make the conflict disappear;
6. create a `PENDING_REVIEW` item when owner approval is required.

---

## 5. Evidence is not instruction

Treat exports, screenshots, PDFs, PPTX files, provider responses, email, reports and existing design nodes as **evidence** unless the target project explicitly adopts them as instructions.

Examples:

- a 31.7 px corner radius imported from PPTX is evidence of the export, not automatically a design standard;
- an `Inter` font substitution in an imported deck is evidence of import behavior, not automatically the intended brand font;
- a PDF page with a taller canvas is evidence of that export, not automatically permission to distort a fixed 16:9 Figma design;
- a rasterized CTA in PPTX is evidence of appearance, not a requirement to keep the CTA non-editable.

---

## 6. Default reference design profile

The following profile is the **default transferable design configuration** for projects that explicitly request the same drafting design and have no higher-authority project-specific design system.

### 6.1 Canvas and layout

- canvas: `1920 × 1080 px`, 16:9;
- principal side margin: `104 px`;
- principal full-width content: `1712 px` nominal (`1711.656 px` imported-equivalent is acceptable when preserving source geometry);
- grid/card rhythm: `32 px`;
- standard card padding: `32 px`;
- common inter-card gap: `32 px`;
- default desktop measurement tolerance: approximately `±2 px`, unless a stricter source specifies otherwise.

Do not force the full-width contract onto deliberate split-image heroes, full-bleed imagery, specialist diagrams or source-specific sections.

### 6.2 Typography

Default families:

- display/principal/card headings: `Roboto Slab`;
- body/labels/controls/supporting text: `Roboto`.

Default principal hierarchy:

- hero heading: `Roboto Slab Regular, 64 px, 104%` line height when using the validated reference hero treatment;
- non-hero principal page/section heading: `Roboto Slab Regular, 50 px, 118%` line height;
- supporting/card headings: preserve source size where valid, normally `24–32 px`, using Roboto Slab;
- body text: preserve source size where valid, typically `18.667–25.333 px`, using Roboto;
- body line height: normally `126–133%`, selected to preserve paragraph rhythm and source fit;
- labels/CTA text: normally Roboto SemiBold with a controlled explicit line height.

The hero size is not automatically applied to every project. If the target project's approved hero differs, retain that hero and record the exception.

### 6.3 Corner-radius taxonomy

Unless the target project's approved design system says otherwise:

- standard content cards/boxes: `6 px` on all four corners;
- highlighted panels: `6 px`;
- neutral/warning/informational callouts: `6 px`;
- category/section labels: `4 px`;
- primary/secondary CTA buttons: `4 px`;
- full-slide backgrounds: `0 px`;
- edge-to-edge image frames: `0 px` unless intentional crop geometry applies;
- circular/intentional image masks: preserve source geometry.

Any other radius above `6 px` must have explicit evidence and a documented exception. Do not retain mechanically scaled export values merely because they are present.

### 6.4 Reference colors

When the new project requests the same drafting design and has no approved brand palette, use these tokenized defaults:

```text
PRIMARY_DARK   = #15213F
PRIMARY        = #3257B8
ACCENT         = #476FD6
SURFACE_MUTED  = #E9ECF2
BORDER_NEUTRAL = #CFD2D8
WHITE          = #FFFFFF
```

For a different brand, replace the values but retain the semantic roles. Never carry source-project brand names into the target project.

### 6.5 CTA and label defaults

Reference defaults:

- CTA height: approximately `72–78 px` unless exact source geometry governs;
- horizontal padding: approximately `36 px`;
- internal spacing: approximately `16 px`;
- primary CTA: solid/approved brand fill, readable contrast, editable text;
- secondary CTA: light/white fill with brand outline;
- CTA radius: `4 px`;
- label radius: `4 px`;
- common strong outline: `2 px` where source/reference uses it;
- smaller status-label outline: approximately `1.5 px` when visually equivalent to the validated reference.

Do not add hyperlinks unless the target project explicitly requests them or a source contract requires them.

---

## 7. Mandatory pre-edit preparation

Before any Figma mutation:

1. activate project memory/context;
2. read the six governance files and apply only approved/canonical records;
3. resolve the exact Figma file key and target node/slide IDs;
4. record the Gamma URL and source export filenames;
5. inspect the PDF visually page by page;
6. inspect the PPTX programmatically for geometry and text where tooling permits;
7. inspect the target Figma file programmatically;
8. render representative or all Figma slides before editing;
9. create a complete pre-edit inventory;
10. create a recoverable version/duplicate if the provider supports it;
11. if immutable backup/version creation is not supported, disclose the limitation and retain source exports plus the pre-edit inventory as recovery evidence.

### Pre-edit inventory fields

For every slide/frame capture:

- file key;
- page/row/slide ID;
- slide order;
- dimensions;
- child count;
- text-node count;
- text strings or controlled digest;
- font family/style/size/line height;
- x/y/width/height for key nodes;
- fills/strokes/stroke weights;
- all four corner values;
- image node IDs, image hashes, scale modes and opacity;
- CTA/card/control structure;
- clipping state;
- source/status metadata;
- visible out-of-bounds nodes;
- suspected rasterized UI surfaces.

Do not perform a destructive edit without this inventory.

---

## 8. PDF inspection instructions

Inspect the PDF visually, not only as parsed text.

For each page record:

- canvas size/aspect ratio;
- section hierarchy;
- line breaks;
- image crop/focal subject;
- card relationships;
- padding/gaps;
- CTA appearance;
- tables/diagrams;
- any page-specific exception.

If PDF page sizes differ from the fixed target canvas, log the discrepancy. Do not silently stretch the target to match an export anomaly.

---

## 9. PPTX measurement instructions

Where a PPTX export exists, programmatically inspect:

- presentation canvas dimensions;
- slide count/order;
- every shape's x/y/width/height;
- text strings and paragraph breaks;
- text frame dimensions;
- fonts/styles/sizes/colors;
- line spacing and paragraph spacing where extractable;
- fills/strokes/transparency;
- corner radii/shape geometry;
- images, crops and source media;
- grouped/object relationships;
- rasterized controls or cards.

Use PPTX geometry as source evidence, but normalize obvious mechanical export artifacts only when the approved design standard supports the correction.

---

## 10. Source-to-target measurement register

Create a measurement record before mutation.

Recommended columns:

| Field | Source value | Target value | Authority | Tolerance | Status | Notes |
|---|---:|---:|---|---:|---|---|
| Canvas | | | | | | |
| Side margin | | | | | | |
| Content width | | | | | | |
| H1 size | | | | | | |
| H1 line height | | | | | | |
| Card gap | | | | | | |
| Card padding | | | | | | |
| CTA height | | | | | | |
| CTA radius | | | | | | |
| Card radius | | | | | | |
| Stroke width | | | | | | |
| Image scale mode | | | | n/a | | |

Every intentional deviation must have an authority/source note.

---

## 11. Controlled mutation rules

1. Modify existing slides/frames in place whenever possible.
2. Do not delete/recreate a validated slide merely because a correction is inconvenient.
3. Use incremental batches and validate each batch.
4. Return and retain every created/mutated node ID.
5. Load the exact font before every text mutation.
6. Preserve exact approved copy, terminology, values and line breaks.
7. Preserve styled emphasis such as bold/italic spans.
8. Reconstruct rasterized UI controls/cards as editable native Figma structures when the control is part of the working design.
9. Preserve source photographs and approved crop intent.
10. Use `FIT` for standalone pictographic icons unless the approved source intentionally crops them.
11. Keep source-designed composite graphics/diagrams as images when reconstructing them would materially change the approved visual or exceed scope.
12. Do not flatten editable working content.
13. Do not create unused variables/tokens.
14. Do not add public links/actions, checkout behavior or runtime claims during a design-only correction.
15. Do not mutate production/runtime systems as a side effect of Figma reconciliation.

---

## 12. Text and line-spacing control

Imported text often carries font substitution and `AUTO` line height. Do not accept those values without inspection.

Required sequence:

1. enumerate available/required fonts;
2. load every target font/style;
3. inspect styled text segments, not only top-level font properties;
4. apply family/style per semantic role;
5. set controlled line height;
6. preserve deliberate paragraph breaks;
7. inspect paragraph spacing and blank-line separation;
8. validate text-frame fit after font replacement;
9. render the slide and visually inspect sentence/paragraph spacing.

For list content, use either native list formatting or literal bullet glyphs—never both.

---

## 13. Editable-control reconstruction

Rasterized buttons and card surfaces are a common export defect.

### CTA reconstruction

A valid editable CTA should normally include:

- editable frame/shape;
- editable label text;
- approved fill;
- approved stroke;
- approved corner radius;
- explicit padding/alignment;
- no image fill pretending to be the entire button.

### Card reconstruction

A valid editable card should normally include:

- native frame/shape surface;
- editable fill/stroke/radius;
- editable heading/body text;
- editable accent/left panel when present;
- icon/asset retained separately;
- no raster image fill representing the complete card UI.

Preserve a raster card only when it is intentionally an illustrative screenshot rather than an editable design component.

---

## 14. Image rules

Validate every image-bearing node on every affected slide.

Required checks:

- image fill exists;
- image hash/source reference is non-empty;
- opacity is visible;
- dimensions are positive and finite;
- transforms are finite;
- node is within intended bounds;
- crop/fit mode is appropriate;
- focal subject remains visible;
- clipping is intentional;
- no source image silently disappears after frame/radius mutations.

Default mode guidance:

- photograph/full-bleed hero: `CROP`;
- standalone icon: `FIT`;
- source-designed composite diagram: usually preserve source `CROP`/source mode;
- logo: normally `FIT` unless an approved lockup requires otherwise.

---

## 15. Page/card drafting model

For projects using Gamma or another generative drafting system, create controlled alternatives from the same approved facts.

Recommended two-alternative model:

### Alternative A — outcome-first

1. clear hero;
2. immediate fit/decision block;
3. three to five benefit/outcome cards;
4. how it works;
5. evidence/qualification;
6. limits/boundaries;
7. status/offer block;
8. CTA.

### Alternative B — trust-first

1. purpose/status hero;
2. problem/context;
3. responsibility boundary;
4. process/architecture diagram;
5. data/provider/security boundary;
6. comparison/decision matrix;
7. evidence/limitations;
8. CTA.

Facts, prices, entitlements, legal status, provider availability, safety rules and public-release status must not differ between alternatives unless a formal decision records the difference.

---

## 16. Card inventory and evaluation

Read every section/card; never rank only from thumbnails.

Record:

- source draft and URL/ID;
- card/section number;
- heading/purpose;
- complete copy/key values;
- component type;
- assets;
- claim/evidence references;
- data/security/legal/commercial statements;
- duplicate relationship;
- contradictions;
- Figma transfer implications;
- disposition.

Allowed dispositions:

`RETAIN`, `RETAIN_WITH_COPY_FIX`, `RETAIN_WITH_QUALIFIER`, `MERGE`, `SPLIT`, `ALTERNATIVE`, `EXCLUDE_DUPLICATE`, `EXCLUDE_UNSUPPORTED`, `PENDING_REVIEW`.

### Generic evaluation score — 100 points

| Criterion | Weight |
|---|---:|
| Accuracy/evidence traceability | 25 |
| Governance/safety/boundary integrity | 15 |
| Strategy/route alignment | 15 |
| Audience clarity/value | 10 |
| Information architecture/component fit | 10 |
| Journey/CTA contribution | 10 |
| Visual hierarchy/Figma transferability | 10 |
| SEO/AEO/accessibility readiness | 5 |
| **Total** | **100** |

Rating bands:

- 90–100: A, preferred;
- 80–89: B, strong;
- 70–79: C, usable;
- 60–69: D, weak;
- below 60: E, reject.

Hard gates override scores.

### Hard gates

- unsupported public claim;
- canonical conflict;
- false implementation status;
- absolute/prohibited wording;
- unsafe/sensitive-data intake;
- unresolved legal/commercial approval presented as final;
- provider/responsibility ambiguity;
- secret/credential exposure;
- destructive edit without recoverable evidence.

---

## 17. Best-of synthesis

Apply this sequence:

1. remove hard-gate failures;
2. remove exact duplicates;
3. resolve canonical-source conflicts;
4. select the strongest card per required page role;
5. retain unique high-value content from alternatives;
6. merge only when facts/qualifiers/status agree;
7. split overloaded cards when meaning is preserved;
8. retain unresolved alternatives separately as `PENDING_REVIEW`;
9. maintain source traceability for every retained/merged/split card.

Do not merge solely because two designs are visually attractive.

---

## 18. Required validation suite

A design/content handoff may pass only after a **separate post-edit readback** and rendered QA.

### 18.1 Structural validation

Validate:

- exact slide/frame count and order;
- target canvas dimensions;
- expected heading on every slide;
- actual node-tree structure;
- no accidental duplicate slides;
- no hidden conflicting/superseded content;
- no unintended flattened UI;
- no visible nodes outside the target canvas;
- no text clipping;
- no text/component overlap;
- expected editable controls/cards;
- all source/status metadata.

For Figma Slides, validate the actual tree rather than relying only on helper methods that may return stale state.

### 18.2 Typography validation

Validate:

- intended font family/style per semantic role;
- missing-font count = 0;
- hero size/line height against baseline;
- every non-hero principal heading against baseline;
- styled-range font replacement;
- text clipping/range-fit warnings;
- paragraph spacing/line spacing;
- duplicate bullet glyphs.

### 18.3 Measurement validation

Validate:

- side margins;
- content widths;
- card dimensions;
- internal padding;
- gaps;
- CTA geometry;
- border widths;
- all four corner values;
- image dimensions/placement;
- source-specific exceptions.

### 18.4 Radius validation

Classify every box-like node as:

- background;
- image mask;
- label;
- CTA;
- card;
- highlighted panel;
- callout;
- special source geometry.

Then validate all four corner values individually.

### 18.5 Copy/content validation

Create a controlled copy digest or exact multiset from expected source text and compare post-edit readback.

The validator must not count helper/metadata text as visible source copy unless intended.

### 18.6 Image validation

Validate every image-bearing node, including hash/source, mode, opacity, dimensions, transforms, containment and rendered crop/focal subject.

### 18.7 Rendered visual QA

Render all slides when practical. At minimum render:

- hero;
- representative card/table slide;
- every source-specific exception;
- every slide with a reconstructed CTA/card;
- every slide with a major image;
- closing/CTA slide.

For a final pass on a small/medium deck, render **every slide**.

A zero-out-of-bounds result alone is not a visual-fidelity pass.

---

## 19. Deterministic validator requirements

The validator must prove its own expected baseline before classifying a design failure.

Before mutating a supposedly failing node, inspect:

1. node ID;
2. parent and coordinate space;
3. expected-record construction;
4. source authority for the expected value;
5. actual property type/value;
6. whether a helper API is stale;
7. whether the node is visible/relevant.

Do not mutate a correct design to satisfy a broken validator.

Recommended final validator output:

```json
{
  "pass": true,
  "errors": [],
  "warnings": [],
  "slideCount": 0,
  "textCount": 0,
  "copyDigest": "",
  "fontViolationCount": 0,
  "missingFontCount": 0,
  "outOfBoundsCount": 0,
  "textClipWarningCount": 0,
  "radiusViolationCount": 0,
  "widthViolationCount": 0,
  "editableCTAcount": 0,
  "editableCardCount": 0,
  "imageCount": 0,
  "imageModes": {},
  "renderedQACount": 0
}
```

---

## 20. Debugger playbook

Use the following order when validation fails.

### D1 — Confirm the failure is real

- inspect exact node ID;
- confirm expected value exists and is authoritative;
- confirm validator coordinate system;
- confirm node visibility and relevance;
- rerun the smallest check.

### D2 — Font mismatch

- load required font/style;
- inspect styled segments/ranges;
- replace mixed ranges, not just top-level `fontName`;
- rerender;
- check text-frame fit.

### D3 — Line-spacing defect

- inspect lineHeight type (`AUTO`, pixels, percent);
- inspect paragraph spacing;
- preserve explicit line/paragraph breaks;
- compare rendered source and target;
- change only the affected text nodes.

### D4 — Width/margin defect

- determine whether coordinates are slide-relative, parent-relative or page-relative;
- inspect parent/group origin;
- compare left/right bounds to the controlled content contract;
- resize wrapper and its transparent background/text children together;
- rerender.

### D5 — Corner-radius defect

- inspect all four values;
- classify node type;
- distinguish image-mask geometry from card/callout geometry;
- correct only the node class that violates the taxonomy;
- rerender affected slides.

### D6 — Image appears cropped/missing

- verify image hash/source;
- verify opacity;
- verify `FIT`/`CROP` mode;
- verify dimensions and transforms;
- verify clipping parent;
- render and inspect focal subject.

### D7 — Raster CTA/card

- determine whether image is an illustration or UI surface;
- if UI surface, rebuild native frame/shape and text;
- retain only icon/art asset separately;
- validate editability and copy digest.

### D8 — Text clipped after font replacement

- inspect text frame and parent frame dimensions;
- compare source line breaks;
- adjust frame dimensions/layout only within approved geometry;
- do not solve by shrinking text below the approved minimum.

### D9 — Stale Figma helper result

- inspect the actual node tree with direct traversal;
- reload/read back after mutation;
- do not rollback a correct deck solely because a helper method returned stale state.

### D10 — PDF/PPTX canvas conflict

- record both source dimensions;
- identify the governing project canvas contract;
- preserve the fixed target geometry;
- treat anomalous export size as evidence, not automatic target geometry.

### D11 — Git branch/PR conflict

- do not force a stale branch over newer canonical work;
- read current `main`;
- create a fresh branch from current `main`;
- transfer only non-conflicting artifacts/commits/blobs;
- close/supersede stale PRs once the replacement is verified.

### D12 — Drive placement drift

- never use Drive root as the project archive;
- set the intended parent explicitly;
- read file metadata after write;
- confirm the expected parent ID;
- move misplaced files without deleting historical evidence.

### D13 — Apparent destructive deletion

- compare pre-edit inventory to live readback before restoring/rolling back;
- do not mutate an intact file solely to resolve an unverified UI discrepancy;
- expose per-slide IDs/counts and provider inventory limitations in the completion report.

---

## 21. Provider and connector limitations

Never claim capabilities that the active connector has not proven.

Common limitations to disclose:

- a Figma connector may not authoritatively enumerate every file in a project folder;
- a connector may not provide a move operation for existing files;
- a connector may not provide an immutable version-history checkpoint;
- helper methods may not immediately reflect the underlying node tree;
- provider runtime behavior may differ from exposed typings;
- Gamma connectors may be unable to rename/delete generated drafts;
- Drive creation may default to root unless parent placement is explicitly validated;
- GitHub branches may become stale during parallel workstreams.

Validation applies only to the exact target/version actually tested.

---

## 22. Required reports and records

At minimum, produce or update:

1. **Source Inventory Report** — exact URLs/file keys/export names/versions.
2. **Pre-Edit Figma Inventory** — IDs, geometry, fonts, images, metadata.
3. **Measurement Baseline** — source vs target dimensions and tolerances.
4. **Mutation Log** — every created/mutated node ID and reason.
5. **Validation Report** — deterministic checks and rendered QA.
6. **Error/Debugger Record** — verified failures, root causes, fixes.
7. **Project Log Update Pack** — issue, root cause, corrective rule, evidence, action, unresolved items, classification.
8. **Session Close Record** — final state and next executable action.
9. **Source Authority Update** — only if a new source actually changes the hierarchy.
10. **Decision Register Update** — only when a decision was made; do not create decisions for simple evidence.

---

## 23. Register templates

### 23.1 Decision register

| ID | Date | Decision | Scope | Rationale/evidence | Owner | Review trigger | Status |
|---|---|---|---|---|---|---|---|

### 23.2 Error register

| ID | Observed | Root cause | Impact | Corrective rule | Evidence | Current status | Classification |
|---|---|---|---|---|---|---|---|

### 23.3 Validation register

| ID | Date | Target | Method | Result | Evidence/output | Follow-up | Classification |
|---|---|---|---|---|---|---|---|

### 23.4 Source authority map

| Source | Version/date | Authority | Scope | Conflicts | Status |
|---|---|---|---|---|---|

### 23.5 Learning log entry

```text
ID:
Timestamp/task:
Issue observed:
Root cause:
Corrective rule:
Evidence/source:
Action taken:
Validation performed:
Unresolved items:
Classification:
```

### 23.6 Session close entry

```text
Timestamp:
Task:
Scope:
Sources used:
Actions completed:
Errors/limitations:
Validation performed:
Unresolved items:
Next executable workstream:
Classification:
Release state:
```

---

## 24. Project Log Update Pack template

```text
# PROJECT LOG UPDATE PACK — <task> — <hh:mm, dd.mm.yyyy>

## Session / task
<what was requested>

## Scope
<exact files/URLs/IDs>

## Authority / baseline
<governing approved sources>

## Source findings
<what source artifacts actually show>

## Issues observed before correction
<numbered defects>

## Root cause
<why the defects existed>

## Corrective rules applied
<rules>

## Actions completed
<per-page/slide/file actions>

## Validation result
<deterministic + rendered QA>

## Provider/workflow limitations
<limitations>

## Release boundary
<what was NOT implemented/released>

## Unresolved items
<remaining work>

## Classification
<AUTO_APPROVED / PENDING_REVIEW / etc.>
```

---

## 25. Figma metadata contract

Where plugin/shared metadata is supported, store non-sensitive traceability such as:

```text
project.sourceGamma
project.sourcePdf
project.sourcePptx
project.referenceDesign
project.handoffStatus
project.deterministicValidation
project.renderedVisualQA
project.validatedAt
project.sourceDiscrepancy
```

Do not store secrets, private tokens, customer content or confidential commercial logic in plugin metadata.

Recommended status values:

- `DRAFTED`
- `MEASUREMENT_CORRECTED`
- `PASS_DESIGN_AND_CONTENT_HANDOFF`
- `IMPLEMENTED`
- `VALIDATED_RUNTIME`
- `APPROVED/RELEASED`

Do not collapse these states.

---

## 26. GitHub write-back procedure

1. identify the canonical repository for the target project;
2. read current `main` before writing;
3. create a fresh reviewable branch;
4. add/update only relevant files;
5. never overwrite newer canonical changes from a stale branch;
6. create a pull request with exact scope and validation evidence;
7. verify the PR is mergeable/current;
8. merge only under the target project's approval policy;
9. read back merged files/commit;
10. update Drive mirrors after the final canonical content is stable.

If a prior PR is stale/conflicted, rebuild on current `main`; do not force it through.

---

## 27. Google Drive write-back procedure

1. identify the exact controlled destination folder;
2. create/import the document;
3. explicitly move it under the intended parent if creation defaults elsewhere;
4. read file metadata;
5. verify `parent_ids`;
6. verify sharing/visibility;
7. read back document text;
8. if a canonical file already exists, update/replace it according to project supersession rules rather than creating uncontrolled duplicates;
9. keep project logs, reusable templates, evidence and canonical mirrors in their designated folders;
10. never treat file presence alone as proof that its content is current.

---

## 28. QA completion checklist

A final `PASS_DESIGN_AND_CONTENT_HANDOFF` requires all applicable items below.

### Source/control

- [ ] exact target file key confirmed;
- [ ] source Gamma/PDF/PPTX filenames/URLs recorded;
- [ ] approved source hierarchy applied;
- [ ] contradictions recorded;
- [ ] pre-edit inventory captured;
- [ ] recovery evidence retained.

### Geometry

- [ ] slide/frame count and order correct;
- [ ] target canvas correct;
- [ ] principal margins correct;
- [ ] content widths correct;
- [ ] key card/callout dimensions correct;
- [ ] internal padding/gaps correct;
- [ ] no visible out-of-bounds nodes.

### Typography

- [ ] display/card headings use approved heading family;
- [ ] body/labels/controls use approved body family;
- [ ] hero matches approved baseline;
- [ ] non-hero principal headings match approved baseline;
- [ ] line heights controlled;
- [ ] paragraph spacing correct;
- [ ] missing fonts = 0;
- [ ] font-family violations = 0;
- [ ] text clipping warnings = 0.

### Components

- [ ] standard cards/callouts have approved radii;
- [ ] labels/CTAs have approved radii;
- [ ] backgrounds use intended square geometry;
- [ ] editable CTA count matches source;
- [ ] editable card count matches intended UI;
- [ ] raster UI surfaces remaining = 0 unless explicitly exempted.

### Images

- [ ] every image-bearing node checked;
- [ ] valid image hash/source;
- [ ] correct `FIT`/`CROP` mode;
- [ ] visible opacity;
- [ ] focal subject/crop visually correct;
- [ ] no missing source imagery.

### Content

- [ ] exact controlled copy digest/multiset passes;
- [ ] intended line breaks preserved;
- [ ] no duplicate bullet glyphs;
- [ ] prices/claims/legal/status text not changed without approval;
- [ ] no secrets or private data.

### Validation/write-back

- [ ] deterministic validator returns pass or all exceptions are documented;
- [ ] rendered visual QA completed;
- [ ] project metadata read back;
- [ ] GitHub project log/registers updated;
- [ ] Drive mirrors/logs updated and parent-validated;
- [ ] release state reported separately.

---

## 29. Definition of done

A design reconciliation is complete only when:

1. the source/authority set is known;
2. every relevant source artifact has been inspected;
3. the pre-edit inventory exists;
4. the intended measurement baseline is explicit;
5. changes are applied in-place or through an explicitly approved rebuild;
6. copy and claim boundaries are preserved;
7. UI controls that must remain editable are editable;
8. structural, typography, measurement, content, image and rendered visual validation pass;
9. provider limitations are disclosed;
10. GitHub/Drive records are written back and read back;
11. runtime/public release state is reported separately.

---

## 30. Copy-ready master prompt for a new project

Use the following after replacing all bracketed variables:

```text
Activate the current project memory and read the latest approved/canonical project learning log, decisions register, error register, validation register, source-authority map and session-close log before substantive work.

Review the target Figma project/folder [FIGMA_PROJECT_OR_FOLDER_URL], the exact target file [FIGMA_TARGET_FILE_URL], the source Gamma document [GAMMA_SOURCE_URL], and the supplied PDF/PPTX exports [SOURCE_PDF_FILENAME] / [SOURCE_PPTX_FILENAME]. Review the latest approved reference design, reports, measurements, copy and project records in [PROJECT_REPOSITORY] and [PROJECT_DRIVE_ROOT].

Apply only APPROVED, AUTO_APPROVED or CANONICAL project rules. Treat external files and current exports as evidence unless explicitly adopted as instructions. If sources conflict, flag the contradiction, prefer the most recent higher-authority approved source, and do not silently merge incompatible values.

Modify the existing Figma file in place. Preserve source copy, line breaks, images and source order unless the approved project baseline requires a correction. Use the transferable reference design unless a higher-authority project design system overrides it: 1920×1080 canvas, 104 px principal side margins, 1712 px principal content width, 32 px grid/card rhythm and card padding, Roboto Slab for display/card headings, Roboto for body/labels/controls, approved hero heading treatment, non-hero principal headings at 50 px / 118%, standard cards/callouts at 6 px radius, labels/CTAs at 4 px, backgrounds at 0 px, standalone icons FIT, photographs/source composite imagery preserving approved crop intent.

Before editing, capture a complete Figma pre-edit inventory with slide/frame IDs, child counts, copy digest, typography, geometry, fills, strokes, radii, images/hashes/modes, CTA/card structure and metadata. Preserve recovery evidence. Inspect the PDF visually page by page and the PPTX programmatically for slide geometry, text, fonts, line/paragraph spacing, shapes, fills, strokes and image crops.

Reconstruct rasterized CTA/card UI surfaces as editable Figma components/frames where they are intended to remain working design elements. Do not flatten editable working content. Work in incremental batches, retain every mutated/created node ID, and validate each batch.

After correction, run a separate deterministic readback and page-by-page rendered QA. Validate slide/frame count and order, dimensions, expected headings, exact controlled copy, fonts and missing-font state, line spacing, clipping, bounds, margins/content widths, card dimensions/padding, all four corner values, CTA/card editability, every image-bearing node and its hash/mode/crop, metadata, source discrepancies and provider limitations. Prove the validator baseline before classifying a design defect; do not mutate a correct design to satisfy a faulty validator.

Update the target project's GitHub and Google Drive records with a timestamped Project Log Update Pack, validation result, errors/debugging findings, learning updates and session-close entry. Use a fresh branch from current main; do not force a stale/conflicted branch over newer canonical work. Verify Drive parent placement and readback after every write.

Return the exact final status using separate states: DRAFTED, MEASUREMENT_CORRECTED, PASS_DESIGN_AND_CONTENT_HANDOFF, IMPLEMENTED, VALIDATED_RUNTIME, APPROVED/RELEASED. A Figma pass must not be represented as runtime implementation or public release.
```

---

## 31. Adoption rule for another project

When moving this pack into a new project:

1. copy the file without project-specific source data;
2. replace bootstrap variables;
3. identify the target project's existing governance and source hierarchy;
4. adopt only the sections the owner approves;
5. mark project-specific commercial, legal, provider, security and release items `PENDING_REVIEW` until separately approved;
6. create target-project-specific measurement exceptions rather than modifying the generic pack invisibly;
7. preserve this template as historical provenance and version it when the reusable method changes.

This prevents the source project's facts and status from contaminating the target project while retaining the validated drafting, measurement, QA, debugging and governance workflow.