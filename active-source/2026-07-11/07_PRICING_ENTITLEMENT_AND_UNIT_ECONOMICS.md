# Atlas AI Pricing, Entitlement and Unit-Economics Baseline — 11:35, 11.07.2026

> **Classification:** PENDING_REVIEW. This document preserves the July four-plan proposal but does not approve public sale or guarantee viability.

> **Execution boundary:** No checkout, billing, provider account, API, entitlement or usage system was validated.

## Proposed plans

| Plan | Gross price incl. MVA | Net revenue before fees | Users | Proposed internal allowance reference |
|---|---:|---:|---:|---|
| Student Basic | NOK 119.00 | NOK 95.20 | 1 | 3M normalized standard units |
| Student Plus | NOK 169.00 | NOK 135.20 | 1 | 6M normalized standard units |
| Everyday Basic | NOK 149.00 | NOK 119.20 | 1 | 4M normalized standard units |
| Family | NOK 349.00 | NOK 279.20 | Up to 4 named users | 14M shared normalized standard units |

Net values assume a 25% MVA calculation for planning only. Final tax/accounting treatment requires professional confirmation.

## Public vs internal terminology

| Layer | Permitted term |
|---|---|
| Public card | Monthly AI usage allowance |
| Detailed plan terms | Normalized standard-use reference and premium-use units |
| Runtime | Provider tokens, requests, tools, files, search and model-class costs |
| Finance | NOK cost per ledger event, user, plan and cohort |

Do not call the normalized unit a provider token. Different providers tokenize and price inputs, outputs, caching, tools and modalities differently.

## Provider-delivery gate

Before “ChatGPT and Claude included” can be sold, Atlas must document:

- actual provisioning route;
- applicable provider terms;
- API/seat/resale restrictions;
- age and account requirements;
- data-processing roles;
- model availability;
- billing owner;
- service interruption and fallback;
- customer-facing disclosure.

Retail business seats are not a substitute for a low-price pooled runtime. Current provider pages show distinct seat and API economics [W12-W15].

## Capability-class policy

Use stable internal classes rather than permanent model names:

| Class | Purpose | Routing rule |
|---|---|---|
| Standard | Routine chat, rewrite, summary and planning | Lowest-cost approved provider route |
| Advanced | Longer documents and stronger reasoning | Budget-aware route |
| Premium | High-cost frontier reasoning or tool-intensive task | Premium-use unit required |
| Restricted | Unsupported/high-risk/regulated action | Block or qualified escalation |

A model change updates `routing_policy_version`; it does not silently change the customer’s plan promise.

## Premium-use units

A premium-use unit must represent a deterministic internal cost budget, not a vague “boost.”

Each decrement record should include:

- plan and user;
- capability class;
- provider/model route;
- input/output/tool cost;
- unit cost in NOK;
- timestamp;
- request correlation ID;
- remaining balance.

The public description may say “premium-use capacity for more demanding tasks,” but plan terms must define limitations.

## Recommended cost ceilings for pilot

| Plan | Provider-cost ceiling at 30% of net revenue | Total variable-cost ceiling at 45% |
|---|---:|---:|
| Student Basic | NOK 28.56 | NOK 42.84 |
| Student Plus | NOK 40.56 | NOK 60.84 |
| Everyday Basic | NOK 35.76 | NOK 53.64 |
| Family | NOK 83.76 | NOK 125.64 |

These are pilot guardrails, not approved margins. Total variable cost includes provider use, payment costs, variable support, storage/search/tool costs, refunds and abuse.

## Metering and reconciliation

1. Every user request receives a correlation ID.
2. Routing decision is logged without prompt content.
3. Provider usage is normalized into cost and plan units.
4. Ledger reservation occurs before expensive work.
5. Completion or failure settles the reservation.
6. Customer balance and provider invoice are reconciled.
7. Exceptions create an alert and suspend further cost where necessary.
8. Monthly reset is idempotent and timezone-defined.

## Hard-cap behavior

- Warn at configurable thresholds.
- No negative balance.
- No silent overage.
- On cap: stop, reduce capability or wait for reset.
- Top-ups remain disabled at launch.
- Any later top-up requires explicit price, confirmation, receipt and cancellation treatment.

## Family controls

- One owner and up to three additional named users.
- No shared credentials.
- Owner manages invitations.
- Shared allowance updates atomically.
- Removal revokes future access.
- Individual activity is not exposed to other family members beyond necessary usage summaries, subject to legal/privacy design.

## Unit-economics pilot

Minimum cohort evidence:

- at least one full billing/reset cycle;
- active users and cohort retention;
- p50/p90/p95 provider cost;
- premium-use frequency;
- family-member distribution;
- payment failures;
- cancellations/refunds;
- support minutes per user;
- abuse/cap events;
- gross contribution before fixed overhead.

## Price decision rule

The four prices may proceed only if:

- provider route is lawful and technically available;
- p95 total variable cost stays below the approved ceiling;
- support burden is sustainable;
- hard caps pass;
- customer value is demonstrated;
- consumer terms and cancellation pass review.

Otherwise, change allowance, capability routing, price or plan scope before launch.

## Open commercial decisions

- Is Atlas delivering provider access through API, seats or customer-owned accounts?
- Are the plan names and prices explicitly approved?
- Is “Family” legally and technically appropriate for minors?
- What is the minimum age and guardian model?
- What payment processor and fee assumptions apply?
- Is annual billing offered?
- What refund and right-of-withdrawal treatment applies?
- Are premium-use units transferable or rolled over?

## Source basis

Merges the July low-price report with the June cost/margin analysis and updates provider interpretation using current official pricing pages.
