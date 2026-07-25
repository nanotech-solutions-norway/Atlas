# Atlas External Validation Register — Pricing, Delivery and Consumer Controls — 25.07.2026

| ID | Question | Official evidence | Result | Remaining work |
|---|---|---|---|---|
| EXT-001 | Can Atlas build a customer application on OpenAI APIs? | OpenAI Services Agreement permits API integration into Customer Applications for End Users. | `VALIDATED` | Contract/DPA/account setup and use-policy review |
| EXT-002 | Can Atlas resell provider accounts or share credentials? | OpenAI prohibits resale/lease of accounts and transfer of API keys; individual accounts are single-user. | `PROHIBITED` | Enforce API delivery and named-user controls |
| EXT-003 | Are Claude paid plans interchangeable with API access? | Anthropic states paid Claude plans and Claude Console/API are separate; API keys are for applications/integrations and must remain secret. | `VALIDATED_SEPARATION` | Commercial-terms review and Console account/DPA |
| EXT-004 | Can Google personal AI plans be used as a business Workspace lane? | Google distinguishes personal Google AI plans from eligible work/school Workspace accounts. | `NO` | Use customer-owned Workspace business licence |
| EXT-005 | Are provider age controls uniform? | OpenAI requires guardian consent for minors; Anthropic consumer Claude is not offered under 18 and API products serving minors require safeguards; Google AI personal plans in the EEA require 18+. | `NO_UNIFORM_RULE` | Approve Atlas minimum age, verification and guardian model |
| EXT-006 | Is 25% MVA a reasonable planning baseline? | Skatteetaten states the standard Norwegian MVA rate is 25%. | `VALIDATED_PLANNING_BASELINE` | Accounting/legal confirmation for each offer and export case |
| EXT-007 | What must a Norwegian consumer checkout show? | Angrerettloven requires pre-contract information and explicit acknowledgement that the order entails payment. | `VALIDATED_REQUIREMENT` | Final legal copy, button wording and withdrawal implementation |
| EXT-008 | Can Wix support subscriptions and order lifecycle? | Wix Pricing Plans supports recurring plans, visibility, billing terms, Orders, cancellation and pause/resume; recurring payment provider required. | `VALIDATED_CAPABILITY` | Install/configure payment provider, plans and tax; test |
| EXT-009 | Can Wix alone enforce provider usage caps? | Wix plan/order APIs govern purchases and access; no evidence establishes a cross-provider normalized usage ledger or atomic cost cap. | `NOT_VALIDATED / EXTERNAL_BACKEND_REQUIRED` | Implement Phase 3 control plane |
| EXT-010 | Can Wix implement account surfaces now? | Wix Members APIs require Members Area. Atlas-AI does not currently have Members Area installed. | `BLOCKED` | Install and validate Members Area before Phase 2 |

## Official source register

- OpenAI Services Agreement: https://openai.com/en-GB/policies/services-agreement/
- OpenAI Service Terms: https://openai.com/en-GB/policies/service-terms/
- OpenAI DPA: https://openai.com/en-GB/policies/data-processing-addendum/
- Anthropic API/Console separation: https://support.claude.com/en/articles/9876003-i-have-a-paid-claude-subscription-pro-max-team-or-enterprise-plans-why-do-i-have-to-pay-separately-to-use-the-claude-api-and-console
- Anthropic API-key security: https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure
- Anthropic minors/API safety statement: https://www.anthropic.com/news/updating-our-usage-policy
- Google AI personal-plan requirements: https://support.google.com/gemini/answer/14517446
- Google Workspace with Gemini: https://support.google.com/drive/answer/13952129
- Norwegian right-of-withdrawal law: https://lovdata.no/lov/2014-06-20-27
- Wix Pricing Plans introduction: https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/plans-v3/introduction
- Wix Orders introduction: https://dev.wix.com/docs/api-reference/business-solutions/pricing-plans/orders/introduction
- Wix Members introduction: https://dev.wix.com/docs/api-reference/crm/members-contacts/members/member-management/introduction
