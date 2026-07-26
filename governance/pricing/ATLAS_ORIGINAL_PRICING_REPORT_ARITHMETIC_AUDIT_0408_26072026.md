# Atlas AI Original Pricing Report Arithmetic Audit — 04:08, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Source artifact:** `Atlas AI Pricing, Budget, Unit Economics and Turnover Report — 13:01, 25.07.2026`  
**Audit scope:** Reproducible arithmetic from figures printed in the supplied report  
**Classification:** `AUTO_APPROVED_EVIDENCE_STATE`  
**Commercial decision effect:** `NONE`  
**Release effect:** `NONE`  
**Release state:** `NO_GO`

> This audit does not alter the raw report, approved v0.5.1 prices or commercial architecture. Corrected commercial inputs or forecasts require a separate approved decision.

## 1. Unit-economics recalculation

The following formulas were recomputed from the values printed in the report:

- `revenue ex MVA = consumer price / 1.25`
- `total direct cost = AI cost + infrastructure + support + payment cost`
- `gross profit = revenue ex MVA - total direct cost`
- `gross margin = gross profit / revenue ex MVA`
- `implied CAC from LTV:CAC = LTV / stated LTV:CAC`
- `implied payback = implied CAC / gross profit`

| Plan | Direct cost | Gross profit | Gross margin | Printed LTV | Printed LTV:CAC | Printed payback | Recalculated result |
|---|---:|---:|---:|---:|---:|---:|---|
| Student Basic | NOK 25.97 | NOK 77.23 | 74.84% | NOK 772 | 5.5x | 1.8 months | `PASS_WITH_ROUNDING`; ratio implies 1.82 months |
| Student Plus | NOK 37.71 | NOK 97.49 | 72.11% | NOK 1,170 | 7.3x | 1.6 months | `PASS_WITH_COARSE_ROUNDING`; ratio implies 1.64 months |
| Everyday Basic | NOK 32.25 | NOK 94.95 | 74.65% | NOK 1,329 | 6.0x | 1.9 months | `FAIL_INTERNAL_CONSISTENCY`; 6.0x implies CAC NOK 221.50 and payback 2.33 months. A 1.9-month payback implies CAC NOK 180.41 and LTV:CAC about 7.37x |
| Family | NOK 68.67 | NOK 250.53 | 78.49% | NOK 4,510 | 15.0x | 1.2 months | `PASS_WITH_ROUNDING`; ratio implies 1.20 months |

The ex-MVA revenue, payment-cost, direct-cost, gross-profit and gross-margin figures reconcile for all four plans within displayed rounding.

## 2. Operating-budget totals

| Scenario | Printed component sum | Printed total | Result |
|---|---:|---:|---|
| Lean founder-led | NOK 120,000 | NOK 120,000 | `PASS` |
| Small operating team | NOK 285,000 | NOK 265,000 | `FAIL`; printed total understates listed components by NOK 20,000/month |
| Scaled commercial case | NOK 525,000 | NOK 525,000 | `PASS` |

The small-team component sum is:

`20,000 + 18,000 + 18,000 + 35,000 + 174,000 + 20,000 = NOK 285,000/month`.

## 3. Pre-launch budget

The listed pre-launch components sum to `NOK 376,000`, matching the report. Result: `PASS`.

## 4. Forecast reproducibility boundary

The annual scenario totals, month-level ramp, EBITDA-like figures, cumulative deficit, runway and break-even months cannot be fully reproduced from the report alone because the complete underlying monthly model, cohort/churn schedule and formula workbook are not included in the supplied artifacts. Result: `NOT_REPRODUCIBLE_FROM_REPORT_ALONE`.

These figures remain dated planning evidence, not validated financial forecasts. Provider prices, FX, CAC, churn, support-time and usage assumptions require refresh before release or material funding decisions.

## 5. Required correction path

1. Preserve the original report unchanged.
2. Identify the intended Everyday Basic CAC, LTV:CAC and payback inputs.
3. Correct either the small-team component table or its total; do not silently choose one.
4. Supply the underlying forecast model or calculation export before forecast figures are marked validated.
5. Obtain finance-owner approval for any corrected figures.
6. Re-run unit economics, break-even, runway and scenario reconciliation after correction.

## Control outcome

- Artifact integrity and content parity remain `PASS`.
- Arithmetic audit is `PARTIAL / TWO_CONFIRMED_INTERNAL_INCONSISTENCIES`.
- Approved consumer prices and architecture are unchanged.
- Public publication, checkout, payment, entitlement, provider routing and release remain blocked.
- Overall release remains `NO_GO`.
