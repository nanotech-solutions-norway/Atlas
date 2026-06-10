# ADR-0005 — Master Claims, Evidence and Vendor Validation Governance — 12:11, 10.06.2026

## Status
Accepted for Atlas website/governance implementation.

## Source basis
- Primary source: `Atlas_Master_Claims_Evidence_Vendor_Validation_Report_1120_10062026.docx`.
- Comparison sources: Atlas website strategy phase files, SEO/AEO/GEO GitHub/Wix/Azure implementation plans, current Atlas-AI Wix test page at `https://www.atlas-ai.no/blank?rc=test-site`, and the current `nanotech-solutions-norway/Atlas` repository baseline.

## Decision
Atlas must treat the master claims/evidence/vendor validation report as the controlling claims-governance overlay for website copy, Wix CMS records, Trust Center content, provider disclosure, sales material, pricing copy, Managed Secure language and future evidence packs.

Atlas may use external AI research, vendor certifications, vendor DPAs and provider SLAs only as contextual or vendor-attributed evidence. Atlas must not convert them into direct Atlas-specific performance, ROI, accuracy, learning-outcome, compliance, security, uptime, data-residency or reliability claims unless Atlas has documented Atlas-specific evidence under comparable conditions.

## Mandatory rules
1. All measurable claims about productivity, time savings, ROI, accuracy, quality, learning outcomes, adoption, satisfaction, security, compliance, uptime, latency, backup/recovery or incident response require a claims-registry entry before publication.
2. External research statistics are context only unless an Atlas pilot, customer deployment, audit or production measurement reproduces the claim under documented conditions.
3. Vendor certifications, DPAs and SLAs must be phrased as vendor-attributed and service-specific. Atlas must not imply it holds a certification or inherits a vendor SLA automatically.
4. Managed Secure public copy must remain evidence-gated until identity, access, logging, revocation, storage, backup/restore and incident workflow evidence exists.
5. Wix status/uptime history must not be described as a formal SLA unless an applicable contract provides one.
6. Domeneshop may be described as having standard DPA terms for relevant hosting services. No public ISO/SOC certification or formal public SLA may be claimed without evidence.
7. Direct Atlas claims such as “Atlas is GDPR compliant”, “Atlas is ISO certified”, “fully secure”, “guaranteed ROI”, “87% time saving”, “73% better grades”, “98% guaranteed uptime”, “all data stored in Norway” or equivalent absolute statements are not approved unless validated evidence is registered.
8. Student content must avoid grade-improvement guarantees, cheating, ghostwriting and direct assignment-submission positioning.
9. Consumer content must avoid emotional-companion positioning, emergency reliance and regulated medical/legal/financial decision support.
10. Ordinary Wix forms remain low-risk qualification only and must not request confidential, restricted, regulated or customer-sensitive files.

## Website finding requiring correction
The current Wix test page contains several direct, measurable or absolute claims that conflict with this ADR until Atlas-specific evidence exists. These include displayed quantitative claims for time savings, grades, satisfied users, NPS/user satisfaction, faster workflow, active users, uptime, Norwegian data storage, “GDPR-safe/GDPR compliant”, ISO/SOC-style certification references and integration/compliance assertions. These should be replaced with context-only, attributed, conditional or design-intent wording before launch.

## Approved interim wording pattern
- Use: “Atlas is designed to reduce manual effort in defined workflows.”
- Use: “External studies show that AI assistance can improve productivity in defined knowledge-work contexts; Atlas does not claim the same result without Atlas-specific evidence.”
- Use: “Atlas uses or may use providers that document security and compliance controls; applicability depends on service, plan, region, contract and configuration.”
- Use: “Managed Secure is a qualified architecture-review path for confidential and control-sensitive workflows. Secure-delivery claims remain gated until implementation evidence is complete.”
- Avoid: fixed outcome percentages, guaranteed ROI, guaranteed grades, Atlas-owned certification claims, blanket GDPR compliance claims, blanket data-residency claims, inherited vendor SLA claims and absolute “fully secure” wording.

## Implementation impact
- Update `docs/claims/claims-registry.yml` with master classification and public-allowed status.
- Update `docs/claims/evidence-index.yml` with source types and vendor caveats.
- Maintain a `docs/claims/not-approved-claims.yml` blocklist for forbidden claims and phrases.
- Add the Wix correction plan to `docs/website/wix-claim-correction-plan-20260610.md`.
- Align Wix CMS `AtlasClaimsRegistry`, `AtlasTrustTopics`, `AtlasFAQs` and legal/provider-disclosure records with this decision.
- Require quarterly claim/vendor revalidation or earlier review before major publication or contract negotiation.

## Review cadence
- High-risk claims: before publication and before contract/procurement use.
- Vendor certifications, DPAs, subprocessors, SLAs and status claims: quarterly and before major publication.
- Atlas performance, ROI and learning claims: after each pilot/customer evidence pack and before external reuse.

## Non-goals
This ADR does not define Atlas-specific benchmark methods, sample sizes, acceptance thresholds or legal advice. Those require a separate measurement protocol and legal review.
