# Atlas AI Figma Slides Phase 1 Alignment Review — 22:05, 14.07.2026

## Executive verdict

| Question | Verdict |
|---|---|
| Measurement/technical alignment | **Partial, not a full pass.** Canvas, fonts, palette, left anchor, slide count and boundary control align. Several mandatory tokens, source-specific layouts, traceability and visual validation requirements do not. |
| Phase 1 coverage | **Ten missing top-level page concepts are represented.** Combined with Home, Solutions, Managed Secure and Contact in Wix, the 14-page top-level shell is represented. Supporting routes, language parity and implementation/launch work remain. |
| Gamma basis | **Conceptual synthesis, not faithful recreation.** The decks use the Gamma subjects and selected structures but are not traceable card-by-card recreations. |
| Students exports | **Readable and stable.** `Atlas AI — Students.pptx` is the preferred export because it preserves editable vector objects; `(1)` contains extensive rasterization. |

## Sources reviewed

- Live Figma Students deck `tHWogSIF3M2EwAwVha1RAx` and all other newly created Phase 1 decks.
- Uploaded Students `.deck.zip` and two PPTX exports.
- Technical drawing and measurement report package v2.1.
- Gamma Student v1/v2, Student Intake family and Responsible AI Study Guide family.
- Atlas recreation prompt, project logs and Phase 1 page-tree evidence.

## Measurement audit

### Passed

- 1920×1080, 16:9.
- Roboto Slab headings and Roboto body.
- Atlas core palette.
- x=104 primary left anchor.
- 54 px dense headings.
- 78 px CTA height.
- Eight slides per new deck.
- Zero out-of-bounds objects across all nine new decks.
- No obvious clipping in the Students PPTX renders.

### Not fully aligned

| Requirement | Observed pattern | Result |
|---|---|---|
| Display H1 72 px | 64 px | Partial |
| CTA text 36 px | 30 px | Fail |
| CTA gap 16 px | 18 px in Students hero/closing | Partial |
| Card padding 32 px | Common inset 28 px | Partial |
| Standard stroke 1 px | Mostly 2 px | Fail |
| 1712 px content frame | Most decks end at x≈1722–1760 rather than x=1816 | Partial |
| Transparent text-hug labels | Fixed 250/300/340 px white-filled labels | Fail |
| Source-specific Gamma visuals | Students behind-image hero replaced by new split panel; no source placeholder | Fail |
| Gamma asset tags | No `[ASSET-GAMMA-…]` tags | Fail |
| Source traceability | No Gamma/card/section map or notes | Fail |
| Clear slide names | Students slides named `1`–`8` | Fail |
| Final screenshot/Gamma comparison | Not completed | Open |

The defensible status is: **geometry baseline applied; detailed measurement compliance not passed.**

## Phase 1 coverage

Top-level Phase 1 surfaces:

1. Home
2. Solutions
3. Business
4. Students
5. Consumers
6. Pricing
7. Platform Lanes
8. Managed Secure
9. Trust
10. Onboarding
11. Resources
12. About
13. Contact
14. Legal

Current representation:

- Wix: Home, Solutions, Managed Secure, Contact.
- Existing Figma: Business.
- New Figma: Students, Consumers, Pricing, Platform Lanes, Trust, Onboarding, Resources, About, Legal.

Thus the top-level shell is represented only when Figma and Wix are considered together. The decks do not provide standalone designs for provider routes, intake routes, resource guides, trust/legal supporting pages, English parity, responsive Wix implementation, CMS, forms, technical SEO, accessibility or launch gates.

## Students-to-Gamma mapping

| Slide | Closest source | Finding |
|---|---|---|
| 1 | Student v1/v2 hero | Newly composed title and split panel; Gamma hero uses image-behind, v2 centered. |
| 2 | Student v1/v2 use areas | Six source areas condensed to four; icons and hierarchy not preserved. |
| 3 | Student v2 journey / guide routines | New four-step composite; Student v2 journey has six steps. |
| 4 | Intake/Study Guide traffic light | Strongest source relationship, but condensed and untraced. |
| 5 | Student plan cards | Plan names retained; prices, premium units, detailed qualifiers and comparison removed. |
| 6 | Provider information | ChatGPT/Claude source-based; “other approved tracks” broadens the Student source. |
| 7 | Privacy/data and Intake | Safe synthesis, not direct card recreation. |
| 8 | Closing interest/process | Newly composed CTA; omits source Basic/Plus choice and detailed activation process. |

The Students deck is a **synthesized page concept**, not an exact Gamma reconstruction.

## Students export comparison

| Export | Size | Slides | Structure | Assessment |
|---|---:|---:|---|---|
| `Atlas AI — Students.pptx` | 10×5.625 in | 8 | 140 auto-shapes; no picture objects | Preferred for editing. |
| `Atlas AI — Students (1).pptx` | 10×5.625 in | 8 | 82 auto-shapes + 58 picture objects | Less editable; extensive rasterization. |

Both are correct 16:9 and visually close to the live Figma deck. Standard PowerPoint widescreen migration requires uniform 1.3333 scaling. Neither export contains source mapping or speaker notes.

## Corrective sequence

1. Correct project status: structural validity passes; measurement and Gamma fidelity remain partial.
2. Create a source-to-slide disposition map for every deck.
3. Resolve and implement shared token deviations: H1, CTA text/gap, card padding, standard stroke, label treatment and content frame.
4. Restore or explicitly map Gamma component hierarchy and source visual locations.
5. Decide whether supporting routes require separate Figma files, then complete Wix responsive implementation and launch gates.

## Classification

### AUTO_APPROVED

- Verified correction to the prior completion status.
- Verified top-level versus full-route Phase 1 distinction.
- Verified Students export/editability findings.
- Source-to-slide mapping and truthful validation-status rule.

### PENDING_REVIEW

- Acceptance of the synthesized eight-slide strategy.
- Whether Business v1 tokens are universal.
- Final H1 and label rules for non-Business decks.
- Pricing, entitlements, legal/provider details.
- Standalone supporting-route deck requirement.
- Final Wix publication and production availability.
