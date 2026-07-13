# General Gamma Draft(s) to Figma Slides Recreation Prompt

Use this prompt in a new chat to recreate **one Gamma draft or a defined combination of multiple Gamma drafts** as a durable, editable Figma Slides presentation.

---

Access the Gamma draft or drafts supplied in this chat and recreate them directly in Figma Slides.

## Inputs

Use the following inputs when provided:

- **Gamma source(s):** one or more Gamma URLs, Gamma IDs, exported Gamma PDFs, or named Gamma drafts/folders.
- **Target Figma file:** an existing Figma Slides URL to update, or a new-file instruction.
- **Measurement/design source:** an attached technical drawing, measurement report, brand guide, template deck, or approved Figma reference.
- **Merge instruction:** preserve drafts separately, consolidate them, create a best-of combination, or follow a user-defined page/slide order.
- **Visual policy:** use original visuals, use placeholders for manual insertion, or recreate only the elements explicitly approved by the user.

Do not assume a fixed slide count, fixed section names, fixed copy, or Business v1-specific layout. Derive the presentation plan from the supplied Gamma source or sources.

## Required outcome

Create or update **one durable Figma Slides file** in the connected Figma account and return the direct `figma.com/slides/...` link.

Do not return only a generated preview. Do not create duplicate decks unless the user explicitly requests alternatives.

## Source-authority order

Apply the following hierarchy:

1. The user's explicit instructions in the current chat.
2. Approved/canonical project instructions and source-authority rules.
3. Gamma source content, slide/card order, component hierarchy, visual locations, and source-specific colors.
4. The attached measurement report, brand guide, template, or approved Figma reference for geometry, typography, spacing, borders, tokens, and recurring components.
5. Existing content in the target Figma Slides file.

When sources conflict:

- Flag the contradiction.
- Do not silently merge conflicting copy, prices, claims, legal wording, product names, or layouts.
- Prefer the latest approved/canonical source when identifiable.
- Treat unresolved commercial, legal, provider-policy, security, public-availability, or pricing conflicts as `PENDING_REVIEW`.
- Continue with non-conflicting work rather than discarding the entire task.

## Multiple-Gamma-draft workflow

When more than one Gamma draft is supplied, first build a source inventory containing:

- Gamma draft title and URL/ID;
- card/section number;
- Gamma section ID where available;
- heading and purpose;
- content type;
- image, icon, diagram, table, CTA, or infographic locations;
- duplicate or near-duplicate sections;
- contradictory wording or values;
- recommended disposition: retain, merge, select one, split, or pending review.

Then create a slide map before editing Figma.

The slide map must specify:

- final slide number;
- source Gamma draft(s);
- source card/section number(s);
- final title;
- whether the slide is retained, merged, split, or newly composed from approved source content;
- intended layout;
- visual placeholder or source-asset requirement;
- any unresolved contradiction.

For multiple drafts:

- Preserve unique, non-duplicative content.
- Consolidate repeated sections only when their meaning and values agree.
- Do not blend conflicting alternatives into one statement.
- Keep traceability from every final slide to its Gamma source or sources.
- Where the user asks for alternatives, keep each alternative as a separate slide or clearly named section.

## Figma workflow

1. Read every supplied Gamma draft completely before building.
2. Read the complete measurement/design source before applying dimensions.
3. Inspect the target Figma Slides file when one is supplied.
4. Create a new file with `editorType: "slides"` only when a target file does not already exist or the user requests a new file.
5. Use `use_figma` with both `figma-use` and `figma-use-slides` for direct edits.
6. Modify existing slides in place unless the user explicitly requests a restart.
7. Create exactly the slide count defined by the approved slide map.
8. Insert all slides into the active slide grid in the approved order.
9. Build in controlled batches and validate each batch.
10. Load each text node's actual font before editing it.
11. Return all created and modified node IDs after every write operation.
12. Preserve editable text, shapes, borders, cards, placeholders, and diagrams.
13. Do not flatten the working Figma source.

## Format and layout rules

- Use the aspect ratio specified by the user or measurement report. Otherwise default to 16:9 Figma Slides.
- Preserve Gamma's component hierarchy unless the user or approved measurement source explicitly overrides it.
- Do not convert vertically structured cards into a table solely to save space.
- Do not shrink presentation text below the approved readable minimum to force a tall Gamma card into one slide.
- When a Gamma card is too tall for the target aspect ratio, use this order of resolution:
  1. optimize spacing within approved tolerances;
  2. use a denser approved component variant;
  3. split the Gamma card into two traceable slides;
  4. request review if splitting would change meaning.
- Maintain approved safe margins, content widths, grid gaps, card padding, borders, and typography tokens.
- Preserve source-specific exceptions, such as a Gamma-defined panel color, when they do not conflict with an explicit user instruction.
- Label borders must hug the rendered label text rather than use a fixed width, unless the source template explicitly specifies fixed labels.

## Visual and placeholder policy

Follow the user's visual policy. When the user says not to recreate images, icons, diagrams, or infographics:

- Do not generate, search for, substitute, redraw, or approximate them.
- Use editable placeholders at the original Gamma visual location and approximate source aspect ratio.
- Place background-image placeholders behind the content when Gamma uses `image-layout="behind"`.
- For ordinary image, diagram, infographic, chart, or video placeholders, use a unique source-location tag in this form:

  `[ASSET-GAMMA-<SOURCE>-S<SLIDE>-<TYPE>-<INDEX> | draft: <title> | card: <number> | section: <section-id> | source: <filename-or-description>]`

- For icon placeholders, display only:

  `icon`

- Store the full icon source reference in the layer name, speaker notes, source map, or validation record rather than inside the icon box.
- Keep every placeholder editable and clearly distinct from final artwork.
- Do not count placeholder labels as source-copy changes.

When original Gamma visuals are to be inserted:

- Use the original asset where access and rights permit.
- Preserve crop, position, layering, transparency, and aspect ratio.
- Do not replace the original with a generated look-alike unless explicitly authorized.

## Content rules

- Preserve the exact source language unless the user requests rewriting or translation.
- Preserve prices, units, qualifiers, disclaimers, package names, CTA wording, and regulated or safety-sensitive wording exactly.
- Do not add unsupported claims.
- Do not change product/provider relationships.
- Do not infer that a platform, certification, SLA, security property, or compliance status belongs to Atlas unless the source explicitly and validly supports that statement.
- Keep low-risk form and contact-routing instructions intact where present.
- CTA hyperlinks are out of scope unless the user explicitly requests them.

## Design-system extraction

Before editing, extract and document the applicable design system:

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
- recurring label, card, notice, pricing, process, table, and CTA components.

Use variables/tokens where the target file supports them. Do not create unused variables.

## Slide-construction requirements

For each final slide:

- retain a clear source reference;
- preserve the correct heading hierarchy;
- preserve the Gamma component type, such as hero, cards, timeline, pricing, table, callout, comparison, infographic, or closing CTA;
- apply the approved measurement profile;
- use editable objects;
- keep all content within the slide boundary;
- avoid text overlap and clipping;
- preserve intentional whitespace without leaving obviously unbalanced dead space;
- maintain consistent alignment with the rest of the deck;
- retain user-approved overrides.

## Mandatory validation

After completing the deck, run a programmatic and visual audit.

Validate:

- direct Figma Slides file exists and is accessible;
- final slide count matches the approved slide map;
- slide order is correct;
- every Gamma source card is accounted for as retained, merged, split, excluded by instruction, or pending review;
- all required headings, body copy, prices, tables, labels, and CTA text are present;
- source-specific colors are correct;
- measurement/design tokens are applied within tolerance;
- all intended labels use the correct dynamic or fixed sizing rule;
- all required placeholders are present and correctly located;
- icon placeholders contain only `icon`;
- no unsupported generated visuals were inserted;
- zero out-of-bounds objects;
- zero text overlaps;
- zero clipped text;
- no accidental duplicate slides;
- no unintended flattened objects in the working source;
- no hidden conflicting content remains on the canvas;
- all slide-grid rows and slide names are correct.

Take final screenshots of:

- the first/title slide;
- at least one representative content/card slide;
- every slide with a source-specific exception;
- every slide that was merged or split from multiple Gamma drafts;
- the final/closing slide.

Correct every failed check before reporting completion.

## Required final response

Return:

1. the direct Figma Slides link;
2. a source-to-slide mapping summary;
3. a concise list of drafts/cards retained, merged, split, or excluded;
4. a validation matrix;
5. a list of remaining manual asset-insertion tasks;
6. any unresolved `PENDING_REVIEW` contradictions;
7. an Atlas Project Log Update Pack with timestamp, issue, root cause, corrective rule, evidence, action taken, unresolved items, and classification.

Do not claim exact Gamma fidelity when component hierarchy, visual position, typography, or spacing materially differs from the source. Distinguish clearly between content fidelity, structural fidelity, visual fidelity, and measurement-profile compliance.
