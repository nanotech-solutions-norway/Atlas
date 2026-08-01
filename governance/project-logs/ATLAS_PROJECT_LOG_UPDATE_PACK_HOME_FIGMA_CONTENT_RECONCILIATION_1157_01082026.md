# Atlas AI Home Figma Content Reconciliation - 11:57, 01.08.2026

**Project:** Atlas Website / Atlas AI  
**Task:** Update all seven single-slide Home section files against the current approved website strategy, business-plan integration and measurement controls.  
**Classification:** `AUTO_APPROVED`  
**Release state:** `NO_GO`; `publicAllowed=false`; `purchaseAllowed=false`; `releaseApproved=false`.

## Governing sources

- GitHub PR #40, merged 01.08.2026 at `2dbe1475192b0795cca1d8acbbe4240116d62db0`.
- `active-source/2026-08-01/01_WEBSITE_STRATEGY_BUSINESS_PLAN_INTEGRATION.md`.
- `active-source/2026-08-01/02_PHASE_1_WEBSITE_DELIVERY_AND_METRICS.md`.
- `active-source/2026-08-01/03_WEBSITE_COPY_ROUTE_AND_TERMINOLOGY_CONTROL.md`.
- `governance/decisions/ATLAS_WEBSITE_STRATEGY_REPORT_DECISION_AND_DISPOSITION_0017_01082026.md`.
- `Atlas_AI_Technical_Drawing_and_Measurement_Report_v2_1_2330_13072026.pdf`.
- `Atlas AI Phase 1 Playbook Validation and Deployment Readiness - 22:59, 14.07.2026`.

## Issue observed

The seven Home section files remained structurally valid but six contained copy from the 19.07.2026 Gamma handoff that predated the website-strategy integration merged on 01.08.2026. Stale terms included KI-first wording and generic English terms such as `review`, `fallback`, `pipeline`, `research`, `Executive`, `compliance` and `Team Workspace`. One visible `icon` placeholder also remained.

## Root cause

Design handoff validation and content-currency validation were completed at different times. The 31.07.2026 Figma reconstruction correctly reproduced the then-approved source, but the 01.08.2026 strategy merge subsequently changed the controlling public-copy and positioning rules.

## Corrective rule

Keep Figma geometry and copy currency as separate validation states. After an approved strategy or terminology change:

1. reconcile every affected Figma text node against the newest approved GitHub source;
2. preserve the latest validated, page-specific measurement profile;
3. re-run structural, terminology and rendered visual checks;
4. record Figma as design evidence only; do not change Wix or release status through a design update.

## Actions completed

1. **Hero:** adopted the approved AI-first Home proposition; added the one-time AI/KI explanation; retained Business as the primary CTA route.
2. **Workflow:** replaced KI-first and `review` terminology with controlled Norwegian wording.
3. **Solution areas:** translated `Executive`, `research`, `pipeline`, `review` and `fallback`; removed standalone product-style `Team Workspace` positioning.
4. **Delivery model:** reframed the comparison as standard working environment versus Managed Secure; retained Managed Secure as qualification/architecture review only; removed the visible `icon` placeholder.
5. **Trust:** changed the section from purchase framing to next-step framing; adopted AI-first and Norwegian etterlevelse wording.
6. **Delivery process:** replaced `review`, `fallback` and generic `onboarding` wording with controlled Norwegian terms.
7. **Closing section:** content remained current; validation metadata was refreshed.

## Measurement and visual validation

- Seven files; exactly one slide per file.
- Canvas: 1920 x 1080 px.
- Side margins: 104 px.
- Content width: 1712 px.
- Grid rhythm: 32 px.
- Card padding: 32 px.
- H1: 72 px on hero/closing sections and 54 px on ordinary sections.
- H1-to-lead spacing: 24 px where the hero reflow changed.
- Lead-to-CTA spacing: 32 px.
- CTA: 78 px height; 24 px text / 30 px line height in the existing Home files.
- Typography: Roboto Slab / Roboto only.
- No text collision, clipping, overflow, stale `icon` placeholder or forbidden English control terminology.
- AI/KI rule: exactly one KI occurrence, inside the approved Home explanation.
- Seven final 1920 x 1080 renders reviewed.

## Execution error and correction

One section-2 text update initially stored intended line breaks as literal `\\n` characters. The update was immediately corrected with actual newline characters, the parent frame was resized to the resulting 165 px text height, and the deterministic and rendered checks were rerun successfully.

## Figma evidence

1. https://www.figma.com/slides/hryHQFz01MX2GLmh56gn8W
2. https://www.figma.com/slides/h2gM9KumIpXlUXEbV2NBvl
3. https://www.figma.com/slides/TxSIwCz3B76gPo7qB1rMsI
4. https://www.figma.com/slides/e2Ov4EANKkHcQ5JAc397ak
5. https://www.figma.com/slides/5itMwVbvfMFG23CPLKJ6eB
6. https://www.figma.com/slides/1OOxUHWlsjizH93FmK7Kot
7. https://www.figma.com/slides/xIiRsFCfKLDwPhrWDfvJ4H

## Final status

`PASS - DESIGN_AND_CONTENT_HANDOFF_VALIDATED`.

Wix was not changed. Responsive Wix implementation, routes, CMS/form bindings, accessibility, metadata, performance, exact release-candidate acceptance and explicit owner GO remain outstanding.
