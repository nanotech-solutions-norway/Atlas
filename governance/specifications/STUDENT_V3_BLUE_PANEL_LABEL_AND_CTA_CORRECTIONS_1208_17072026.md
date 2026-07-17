# Atlas AI Student v3 — Blue Panel, Label and CTA Corrections

**Timestamp:** 12:08, 17.07.2026 Europe/Oslo  
**Figma:** https://www.figma.com/slides/I8mk7h7D2RtaRVoaZkPNRt  
**Gamma:** https://gamma.app/docs/8n0a8sr0yuuy672  
**Classification:** AUTO_APPROVED

## Scope

Apply the latest explicit corrections to Student v3:

1. adjust the text layout in the blue boxes on Slides 3 and 7;
2. make every label border fit the rendered label text;
3. enforce the approved button font, size and formatting;
4. validate the final live Figma result.

## Source authority

- Gamma controls the exact Student Basic and institution-rule wording.
- The Atlas measurement profile controls padding, spacing, line height, borders, typography and fixed-canvas geometry.
- The user's current instruction supersedes earlier accepted geometry where necessary.

## Slide 3 — Student Basic blue plan card

The exact Gamma copy was retained. No pricing, provider, feature or availability wording was rewritten.

### Final geometry and rhythm

| Element | Final value |
|---|---:|
| Card position | x 104, y 320 |
| Card width | 840 px |
| Card height | 500 px |
| Internal horizontal padding | 32 px |
| Status label y | 28 px |
| Plan title y | 88 px |
| Price y | 144 px |
| Description y | 190 px |
| First bullet y | 270 px |
| Bullet row step | 42 px |
| Body/list line height | 150% |
| Heading/price line height | 125% |

The adjacent Student Plus card was resized to the same 500 px height to preserve the two-column alignment.

The activation and manual-validation notices were moved to y 842 and y 912 respectively, retaining the approved content width and slide-bottom margin.

## Slide 7 — Rules blue panel

The exact Gamma wording was retained:

- heading: `Regler gjelder alltid`
- body: the full institution-rule paragraph from Gamma.

### Final geometry and rhythm

| Element | Final value |
|---|---:|
| Panel position | x 104, y 280 |
| Panel width | 620 px |
| Panel height | 296 px |
| Internal padding | 32 px |
| Heading y | 32 px |
| Body y | 96 px |
| Heading-to-body gap | 16 px |
| Body line height | 150% |
| Bottom padding | 35 px |

The panel height was rounded to the next 8 px measurement-grid increment that fully contains the rendered text.

## Label-border rule

All nine label frames now follow the dynamic text-fit rule:

`label width = rendered text width + 28 px`

Additional label tokens:

- transparent fill;
- 14 px horizontal padding;
- 44 px height;
- 2 px border;
- 4 px radius;
- Roboto SemiBold 18 px;
- 100% line height;
- vertically centred text.

This includes the two plan-status labels on Slide 3.

## CTA typography rule

All four CTA controls were normalized to:

- Roboto SemiBold;
- 36 px;
- 44 px fixed line height;
- centred horizontally and vertically;
- 78 px button height;
- 2 px border;
- 4 px radius;
- 16 px inter-button gap where paired.

The previously approved content-fit widths remain:

- Slide 1: 480 px and 420 px;
- Slide 8: 600 px and 600 px.

## Boundary

No commercial, provider, eligibility, age, payment or public-availability wording was approved or changed by this design correction.