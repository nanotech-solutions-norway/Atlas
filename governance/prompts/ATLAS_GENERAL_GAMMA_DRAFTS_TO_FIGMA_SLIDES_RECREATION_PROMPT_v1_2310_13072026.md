# Atlas AI Project - General Gamma Draft(s) to Figma Slides Recreation Prompt

Use this prompt in a **new chat thread inside the Atlas AI project** to recreate one Gamma draft, several Gamma drafts, or an approved combination of drafts as one durable, editable Figma Slides presentation.

---

Work inside the **Atlas AI project**. Access the Gamma draft or drafts supplied in this chat or identified in the Atlas AI project sources, then recreate them directly in Figma Slides.

## Project scope

This workflow applies only to Atlas AI project material unless the user explicitly adds another source. Do not broaden the task to unrelated Gamma workspaces, websites, brands, companies, presentations, or files.

Before substantive work:

1. Activate Atlas project context and read the latest approved/canonical Atlas learning, decision, error, validation, source-authority, and session-close records when available.
2. Read the latest relevant Atlas AI project files from the project source panel, GitHub, Google Drive, uploaded files, and prior Atlas project threads.
3. Apply only entries marked `APPROVED`, `AUTO_APPROVED`, or `CANONICAL` as governing instructions.
4. Treat `PENDING_REVIEW` entries as advisory and preserve their status.
5. Flag contradictions and prefer the most recent approved canonical source. Do not silently merge conflicting information.

Preserve Atlas safety and publication locks:

- no real-money betting;
- no auto-betting;
- no bookmaker execution;
- no public write endpoint;
- no frontend provider tokens;
- no public production availability unless explicitly approved;
- no secrets, credentials, customer-confidential data, bank/accounting data, private commercial data, or provider/internal keys in Figma, GitHub, prompts, screenshots, exports, or reports.

## Inputs

Use the following inputs when provided:

- **Gamma source(s):** one or more Gamma URLs, Gamma IDs, exported Gamma PDFs, named Gamma drafts, or drafts in the approved Atlas AI Gamma workspace/folder.
- **Target Figma file:** an existing Atlas AI Figma Slides URL to update, or an instruction to create a new file.
- **Measurement/design source:** the latest approved Atlas AI technical drawing, measurement report, brand guide, template deck, or approved Figma reference.
- **Combination instruction:** preserve drafts separately, consolidate them, create a best-of combination, create alternatives, or follow a user-defined page/slide order.
- **Visual policy:** use original visuals, use placeholders for manual insertion, or recreate only explicitly approved elements.
- **Language/output instruction:** preserve the original language, translate, or create bilingual variants only when explicitly requested.

Do not assume a fixed slide count, fixed section names, fixed copy, fixed page tree, or Business v1-specific layout. Derive the presentation plan from the supplied Atlas AI Gamma source or sources.

## Required outcome

Create or update **one durable Figma Slides file in the Atlas AI Figma workspace/team** and return the direct `figma.com/slides/...` link.

Do not return only a generated preview. Do not create duplicate decks unless the user explicitly requests alternatives or separate versions.

## Source-authority order

Apply this hierarchy:

1. The user's explicit instruction in the current Atlas AI project thread.
2. Approved/canonical Atlas AI project instructions, source-authority rules, decision records, validation records, and corrections.
3. The latest approved Gamma source content, card order, component hierarchy, visual locations, and source-specific colors.
4. The latest approved Atlas AI measurement report, brand guide, Figma reference, template, or design-token source for geometry, typography, spacing, borders, and recurring components.
5. Existing content in the target Figma Slides file.
6. Older, superseded, or advisory sources.

When sources conflict:

- flag the contradiction;
- identify each conflicting source and its version/date;
- do not silently combine conflicting copy, prices, claims, legal wording, product names, provider relationships, availability statements, or layouts;
- prefer the most recent approved canonical source when identifiable;
- treat unresolved commercial, pricing, legal, provider-policy, safety, security, public-availability, and production decisions as `PENDING_REVIEW`;
- continue with non-conflicting work.

## One-draft workflow

For one Gamma draft:

1. Read every card/section completely.
2. Record the draft title, URL/ID, card order, section IDs, text, component types, source-specific colors, and visual locations.
3. Create a slide map before editing Figma.
4. Preserve the Gamma component hierarchy unless an approved Atlas measurement rule or explicit user instruction overrides it.
5. Retain traceability from each final slide to the Gamma card/section.

## Multiple-Gamma-draft workflow

When more than one Atlas AI Gamma draft is supplied, first build a source inventory containing:

- Gamma draft title and URL/ID;
- version/date where available;
- card/section number;
- Gamma section ID;
- heading and purpose;
- content type;
- copy and key values;
- image, icon, diagram, chart, table, CTA, video, or infographic locations;
- duplicate or near-duplicate sections;
- alternative versions;
- contradictory wording, pricing, claims, package structures, or visual treatments;
- recommended disposition: retain, merge, select one, split, alternative, exclude by instruction, or pending review.

Then create a final slide map specifying:

- final slide number;
- final slide title;
- source Gamma draft(s);
- source card/section number(s) and section IDs;
- retained, merged, split, alternative, or newly composed status;
- intended layout and component type;
- source visual or placeholder requirement;
- governing measurement/design source;
- unresolved contradiction or `PENDING_REVIEW` item.

For multiple drafts:

- preserve unique, non-duplicative content;
- merge repeated sections only when meaning, values, claims, and commercial wording agree;
- do not blend conflicting alternatives into one statement;
- keep alternatives separate when requested or when no approved choice exists;
- maintain source traceability for every final slide;
- do not discard a newer approved version in favor of an older visually stronger version without approval;
- preserve the latest approved Atlas terminology and product/provider names.

## Figma workflow

1. Read every supplied Gamma draft completely before building.
2. Read the latest approved Atlas measurement/design sources before applying dimensions.
3. Inspect the target Figma Slides file when supplied.
4. Create a new file with `editorType: "slides"` only when no target file exists or the user requests a new file.
5. Use direct Figma editing with `use_figma`, `figma-use`, and `figma-use-slides`.
6. Modify existing slides in place unless the user explicitly requests a restart.
7. Create exactly the slide count defined by the approved slide map.
8. Insert all slides into the active slide grid in the approved order.
9. Use clear slide and section names reflecting the Atlas page/solution structure.
10. Build in controlled batches and validate each batch.
11. Load every text node's actual font before editing it.
12. Return all created and modified node IDs after every write operation.
13. Preserve editable text, shapes, cards, labels, borders, placeholders, tables, and diagrams.
14. Do not flatten the working Figma source.
15. Do not create unused design variables or tokens.

## Format and layout rules

- Use the aspect ratio specified by the user or latest approved Atlas measurement report. Otherwise default to 16:9 Figma Slides.
- Preserve Gamma's component hierarchy unless explicitly overridden.
- Do not convert vertically structured cards into tables merely to save space.
- Do not shrink text below the approved readable minimum to force a tall Gamma card into one slide.
- When a Gamma card is too tall for the target format, resolve it in this order:
  1. optimize spacing within approved tolerances;
  2. use an approved denser component variant;
  3. split the Gamma card into two traceable slides;
  4. request review if splitting changes meaning or commercial hierarchy.
- Apply the approved safe margins, content width, grid gaps, card padding, borders, corner radii, typography, and CTA tokens.
- Preserve source-specific Gamma exceptions when they do not conflict with an explicit user instruction or canonical Atlas rule.
- Label borders must hug rendered label text unless the governing template explicitly specifies fixed label widths.
- Maintain intentional whitespace, but remove obviously unbalanced dead space.

## Visual and placeholder policy

Follow the user's visual policy.

When visuals must not be recreated:

- do not generate, search for, substitute, redraw, or approximate them;
- use editable placeholders at the original Gamma visual location and approximate source aspect ratio;
- place a background-image placeholder behind content when Gamma uses `image-layout="behind"`;
- for ordinary images, diagrams, infographics, charts, videos, and other non-icon visuals, use a unique source-location tag:

  `[ASSET-GAMMA-<DRAFT>-C<CARD>-<TYPE>-<INDEX> | project: Atlas AI | draft: <title> | card: <number> | section: <section-id> | source: <filename-or-description>]`

- for icon placeholders, display only:

  `icon`

- store full icon source details in the layer name, speaker notes, source map, or validation record rather than inside the icon box;
- keep placeholders editable and visually distinct from final artwork;
- do not count placeholder labels as source-copy changes.

When original Gamma visuals are to be inserted:

- use the original asset where access and rights permit;
- preserve crop, position, layering, transparency, and aspect ratio;
- do not replace an original asset with a generated look-alike unless explicitly authorized;
- verify that no hidden provider/internal identifier or sensitive information appears in the asset or its metadata.

## Content and governance rules

- Preserve exact source language unless rewriting or translation is requested.
- Preserve prices, units, qualifiers, disclaimers, package names, CTA wording, safety boundaries, and regulated wording exactly.
- Use the latest approved Atlas terminology.
- Do not add unsupported claims.
- Do not convert vendor evidence into Atlas-specific performance, compliance, security, uptime, data-residency, certification, ROI, accuracy, or reliability claims.
- Do not change product/provider relationships.
- Do not imply Atlas owns a third-party platform or foundation model.
- Keep low-risk form and contact-routing instructions intact where present.
- CTA hyperlinks are out of scope unless explicitly requested.
- Managed Secure, Azure, production availability, provider delivery rights, and similar gated items remain qualified and must follow approved Atlas wording.

## Design-system extraction

Before editing, extract and document the applicable Atlas design system:

- slide size and safe margins;
- content width;
- heading and body font families;
- heading, body, label, card-title, caption, and CTA sizes;
- line heights;
- primary, secondary, neutral, border, panel, and source-specific colors;
- standard and accent border thickness;
- corner radii;
- grid gaps;
- card padding;
- CTA height and spacing;
- recurring label, card, notice, pricing, process, comparison, table, trust, and CTA components.

Bind variables/tokens when useful and supported. Do not create unused variables.

## Slide-construction requirements

For each final slide:

- retain a clear Gamma source reference;
- preserve the correct heading hierarchy;
- preserve the Gamma component type: hero, cards, process, pricing, table, callout, comparison, infographic, trust block, or closing CTA;
- apply the approved Atlas measurement profile;
- use editable objects;
- keep all content within the slide boundary;
- avoid text overlap and clipping;
- maintain consistent alignment with the deck;
- retain user-approved overrides;
- preserve Atlas safety and governance wording;
- keep source-specific alternatives distinguishable.

## Mandatory validation

After completing the deck, run a programmatic and visual audit.

Validate:

- the direct Atlas Figma Slides file exists and is accessible;
- slide count matches the approved slide map;
- slide order is correct;
- every Gamma source card is accounted for as retained, merged, split, alternative, excluded by instruction, or pending review;
- every final slide has source traceability;
- required headings, body copy, prices, tables, labels, CTA text, qualifiers, and disclaimers are present;
- source-specific colors and component hierarchy are correct;
- Atlas measurement/design tokens are applied within tolerance;
- labels use the correct dynamic or fixed sizing rule;
- all required placeholders are present and correctly located;
- icon placeholders contain only `icon`;
- no unsupported generated visuals were inserted;
- zero out-of-bounds objects;
- zero text overlaps;
- zero clipped text;
- no accidental duplicate slides;
- no unintended flattened objects in the working source;
- no hidden conflicting or superseded content remains on the canvas;
- slide-grid rows, section names, and slide names are correct;
- no secrets, tokens, private data, or prohibited public-production claims are present.

Take final screenshots of:

- the first/title slide;
- at least one representative card/content slide;
- every slide with a source-specific exception;
- every slide merged or split from multiple Gamma drafts;
- every unresolved alternative requiring review;
- the final/closing slide.

Correct every failed check before reporting completion.

## GitHub and Atlas project logging

After substantive work:

1. Prepare an `ATLAS PROJECT LOG UPDATE PACK` containing timestamp, task, issue, root cause, corrective rule, evidence, action taken, unresolved items, and classification.
2. Classify exact corrections and validated non-sensitive design/QA rules as `AUTO_APPROVED`.
3. Classify unresolved commercial, pricing, legal, provider-policy, security-posture, public-availability, and production decisions as `PENDING_REVIEW`.
4. When GitHub write-back is authorized, append or create the appropriate log in the canonical Atlas repository.
5. Never commit secrets, provider keys, customer-confidential data, private commercial data, or sensitive screenshots.

## Required final response

Return:

1. the direct Figma Slides link;
2. the final slide map and source-to-slide mapping;
3. a concise list of drafts/cards retained, merged, split, alternative, or excluded;
4. a validation matrix separating content fidelity, structural fidelity, visual fidelity, and measurement compliance;
5. remaining manual asset-insertion tasks;
6. unresolved `PENDING_REVIEW` contradictions;
7. the GitHub log path and commit when write-back occurred;
8. the Atlas Project Log Update Pack.

Do not claim exact Gamma fidelity when component hierarchy, visual position, typography, or spacing materially differs from the source.
