# Atlas AI Consumer Checkout Legal Readiness Matrix — 25.07.2026

**Scope:** Norwegian consumer subscriptions and top-ups  
**Research mandate:** Created 25.07.2026  
**Legal approval:** `PENDING_LEGAL_REVIEW`  
**Checkout state:** `NO_GO`

| Gate | Requirement | Current evidence | Result | Required next evidence |
|---|---|---|---|---|
| LEG-001 | Offer-by-offer legal classification under Angrerettloven and Digitalytelsesloven | General source review only | `BLOCKED` | Signed legal classification memorandum |
| LEG-002 | Complete pre-contract information under Angrerettloven § 8 and electronic contracting rules | Requirement list exists | `PARTIAL` | Bokmål/English copy mapped to page, checkout and durable medium |
| LEG-003 | Required information displayed clearly and prominently immediately before order | No live checkout | `NOT_RUN` | Wix layout and screenshot evidence |
| LEG-004 | Payment button unambiguously acknowledges obligation to pay | No live checkout | `NOT_RUN` | Approved button wording and functional test |
| LEG-005 | Early commencement request for paid services during withdrawal period | No consent design | `BLOCKED` | Approved unchecked checkbox/interaction and evidence fields |
| LEG-006 | Correct distinction between service and digital-content withdrawal loss | Unresolved classification | `BLOCKED` | Legal opinion and offer/component matrix |
| LEG-007 | Durable-medium contract confirmation before service begins | No order flow | `NOT_IMPLEMENTED` | Confirmation email/PDF template and delivery test |
| LEG-008 | Withdrawal notice and statutory form | Draft concepts only | `BLOCKED` | Approved Bokmål/English notice/form and support process |
| LEG-009 | Proportional-payment method for early-started service | Not defined | `BLOCKED` | Calculation rule, evidence and refund test |
| LEG-010 | Cancellation method no harder than contracting and available without account lockout | Members Area absent | `BLOCKED` | Portal/email fallback and acceptance tests |
| LEG-011 | Recurring billing, renewal, annual/semester and pause terms | Commercial rules approved; legal copy absent | `PARTIAL` | Approved terms and reminder/renewal flow |
| LEG-012 | Refund and statutory-remedy matrix | Not final | `BLOCKED` | Consumer policy, internal SOP, decision tree and deadlines |
| LEG-013 | Top-up/boost legal classification, expiry, withdrawal and refund | Not classified | `BLOCKED` | Legal classification and separate checkout copy |
| LEG-014 | Family/minor/guardian/household controls | Not implemented | `BLOCKED` | Legal rules plus technically enforceable identity controls |
| LEG-015 | Service-change, provider/model substitution and price-change rights | General disclosure only | `BLOCKED` | Approved change clause and durable-medium notice |
| LEG-016 | Customer-content export/deletion after withdrawal/termination | Architecture incomplete | `BLOCKED` | Data lifecycle and portal/support workflow |
| LEG-017 | Wix capability and limitation mapping | High-level phase map exists | `PARTIAL` | Requirement-by-requirement Wix/Velo/backend matrix |
| LEG-018 | Bilingual parity | Draft legal content only | `NOT_RUN` | Bokmål/English parity review |
| LEG-019 | Accessibility of checkout, consent and legal information | No live flow | `NOT_RUN` | WCAG/accessibility validation |
| LEG-020 | Legal sign-off and release approval | Absent | `NO_GO` | Named Norwegian counsel approval and written release decision |

## Current official-source checkpoints

- Angrerettloven § 16 requires clear, prominent information immediately before an electronic paid order and an express acknowledgement that the order creates a payment obligation. A button must use “bestilling med forpliktelse til å betale” or equivalent wording; non-compliance can mean the consumer is not bound.
- Angrerettloven §§ 18–19 require durable-medium confirmation and an express request where paid service delivery begins during the withdrawal period.
- Angrerettloven § 22 contains distinct conditions for full performance of services and delivery of digital content not supplied on a physical medium.
- The final Atlas classification and implementation remain subject to Norwegian legal review.

## Control outcome

The research prompt is complete and controlled. The legal work, terms drafting, Wix implementation and acceptance testing have not yet been completed. Consumer checkout, Wix Pricing Plans and immediate paid activation remain disabled.
