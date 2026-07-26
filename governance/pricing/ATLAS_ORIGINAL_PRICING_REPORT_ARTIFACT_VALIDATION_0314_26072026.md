# Atlas AI Original Pricing Report Artifact Validation — 04:08, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Source artifact:** `Atlas AI Pricing, Budget, Unit Economics and Turnover Report — 13:01, 25.07.2026`  
**Commercial authority:** Approved pricing values under `ATL-DEC-20260725-011`  
**Activation authority:** No release effect; `publicAllowed=false`, `purchaseAllowed=false`, checkout disabled  
**Release state:** `NO_GO`

## 1. Artifact integrity

| Check | Result | Evidence |
|---|---|---|
| DOCX present | `PASS` | SHA-256 `8d9d35d97705daa94b6a35edbb97855d5ed6522eebe8e982dc30d39ce7a3cc9b`; 33,088 bytes |
| Markdown present | `PASS` | SHA-256 `e2375d9ea5b7ce8ce4fd612cf13648b978cbd78a0774f9c1d1b32c925c624948`; 44,062 bytes |
| Structure parity | `PASS` | 27/27 section headings match exactly |
| Content equivalence | `PASS_CONTENT_EQUIVALENCE_NOT_BYTE_EQUIVALENCE` | Normalized token-sequence similarity 0.976388 |
| Citation portability | `FAIL / LIMITATION` | Conversation-local citation tokens are not archival source links |

## 2. Approved commercial parity

| Controlled value | Report value | Result |
|---|---:|---|
| Student Basic incl. MVA | NOK 129/month | `PASS` |
| Student Plus incl. MVA | NOK 169/month | `PASS` |
| Everyday Basic incl. MVA | NOK 159/month | `PASS` |
| Family incl. MVA | NOK 399/month | `PASS` |
| Annual public discount | 10% | `PASS_APPROVED_CONTROL` |
| Public delivery | Atlas-managed API with hard caps | `PASS_APPROVED_CONTROL` |
| Copilot/Workspace Gemini | Customer-owned licence lanes | `PASS_APPROVED_CONTROL` |
| Managed Secure Standard floor | NOK 85,000/month ex. MVA | `PASS_APPROVED_COMMERCIAL_BASELINE / ACTIVATION_BLOCKED` |

## 3. Authority conflict resolved

The source report states that Atlas should “launch now” with public subscriptions. That recommendation does not govern release. The later and higher-authority canonical decisions explicitly separate commercial approval from activation. Therefore:

- the price book and approved commercial architecture remain active;
- the report’s immediate-launch recommendation is `SUPERSEDED_FOR_ACTIVATION`;
- no public pricing publication, Wix Pricing Plan, checkout, provider provisioning, entitlement activation, production routing or Managed Secure activation is authorized.

## 4. Arithmetic audit

A reproducible arithmetic audit is stored in `ATLAS_ORIGINAL_PRICING_REPORT_ARITHMETIC_AUDIT_0408_26072026.md`.

| Area | Result | Finding |
|---|---|---|
| Ex-MVA revenue, direct cost, gross profit and gross margin for four public plans | `PASS_WITH_ROUNDING` | Printed calculations reconcile |
| Everyday Basic LTV:CAC and payback | `FAIL_INTERNAL_CONSISTENCY` | Printed 6.0x LTV:CAC implies approximately 2.33 months payback, not 1.9 months; 1.9 months implies approximately 7.37x |
| Lean monthly operating budget | `PASS` | Components total NOK 120,000 |
| Small-team monthly operating budget | `FAIL` | Listed components total NOK 285,000, while the printed total is NOK 265,000 |
| Scaled monthly operating budget | `PASS` | Components total NOK 525,000 |
| Pre-launch budget | `PASS` | Components total NOK 376,000 |
| Scenario forecasts, break-even and runway | `NOT_REPRODUCIBLE_FROM_REPORT_ALONE` | Complete underlying monthly/cohort model is absent |

The raw report remains unchanged. The two inconsistencies do not change the approved public price book, but the affected unit-economics and operating-budget values must not be represented as validated until corrected and approved.

## 5. Remaining financial evidence

The report’s provider prices, FX assumptions, acquisition/churn assumptions, support costs, forecasts and scenario outputs remain dated evidence as of 25.07.2026. They require trigger-based refresh before release or material investment decisions. Final MVA treatment, OSS, reverse charge, top-up tax point, refunds/credit notes and accounting reconciliation remain `PENDING_ACCOUNTING_AND_TAX_REVIEW`.

**Control outcome:** original pricing artifact ingested; approved values reconcile to v0.5.1; arithmetic validation is `PARTIAL / TWO_CONFIRMED_INTERNAL_INCONSISTENCIES`; activation remains `NO_GO`.
