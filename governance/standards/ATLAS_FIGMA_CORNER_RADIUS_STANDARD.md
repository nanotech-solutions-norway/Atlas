# ATLAS FIGMA CORNER-RADIUS STANDARD

**Approved:** 10:57, 05.08.2026 Europe/Oslo  
**Canonical confirmation:** 11:54, 05.08.2026 Europe/Oslo  
**Scope:** Atlas AI Figma Slides and Figma Design website-draft preparation  
**Classification:** `CANONICAL`  
**Authority basis:** explicit owner correction, subsequent explicit owner approval to retain the instructions for future configuration and adjustments, and the approved `Atlas AI Canonical Figma Recreation Specification v3`.

## 1. Canonical radius taxonomy

Use the following defaults unless a later explicit owner instruction or an approved Gamma visual requires a documented exception:

- **Standard content cards and boxes:** `6 px` on all four corners.
- **Neutral, warning and informational callouts:** `6 px` on all four corners.
- **Highlighted pricing/status panels:** `6 px` on all four corners.
- **Category/section label outlines:** `4 px` on all four corners.
- **Primary and secondary CTA buttons:** `4 px` on all four corners.
- **Full-slide backgrounds and edge-to-edge image frames:** `0 px` unless the source intentionally defines a crop shape.
- **Circular or intentionally shaped image masks:** preserve the approved source crop and geometry; do not convert these to the standard card radius.

## 2. Prohibited defaults

Do not retain decorative `18–34 px` radii or mechanically scaled values such as approximately `31.694 px` or `40.517 px` merely because they originated from a PPTX/Gamma export. Such values require an explicit, documented source exception.

Do not leave a standard card or callout at `0 px` unless the approved source explicitly requires square corners.

## 3. Validation requirements

For every Figma adjustment:

1. Inventory every visible box-like node and classify it as background, image mask, label, CTA, card, highlighted panel or callout.
2. Validate all four individual corner values, not only the aggregate `cornerRadius` property.
3. Confirm:
   - cards/callouts/highlighted panels = `6 px`;
   - labels/CTAs = `4 px`;
   - backgrounds = `0 px`;
   - image masks retain approved source geometry.
4. Flag any other radius above `6 px` as an exception requiring evidence.
5. Render every affected slide after mutation and inspect the result visually.
6. Confirm geometry, text, fills, images, headings and slide bounds remain unchanged unless separately instructed.

## 4. Tjenester v4.1 precedent

The following Tjenester v4.1 nodes establish the validated implementation precedent:

- Bedrift price panel `0:51` → `6 px`.
- Studenter price panel `0:88` → `6 px`.
- Privatpersoner cards `0:114`, `0:121`, `0:128` → `6 px`.
- Managed Secure price/status panel `0:154` → `6 px`.
- Managed Secure warning callout `0:168` → `6 px`.
- Closing information callout `0:239` → `6 px`.
- Labels and CTA controls remain `4 px`.

## 5. Persistence rule

This standard is the default for future Atlas AI Figma configuration and adjustment work. Apply it automatically unless a later explicit owner instruction or a higher-authority approved source supersedes it. Any conflict must be flagged rather than silently merged.

This standard does not change Wix implementation or public-release status. Public release remains `NO_GO` until the controlling runtime gates pass.
