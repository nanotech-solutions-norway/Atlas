# Atlas AI Checkout, Disclosure, Withdrawal, Cancellation and Refund Operations Pack — 02:06, 26.07.2026

**Project:** Atlas Website / Atlas AI  
**Contract version:** `0.5.1`  
**Research state:** `RESEARCH_COMPLETED_DRAFT_PACK_CREATED`  
**Legal state:** `PENDING_LEGAL_REVIEW`  
**Implementation state:** `NOT_IMPLEMENTED`  
**Checkout state:** `NO_GO`

> All consumer-facing text in this pack is a controlled implementation draft. It must not be published, activated or treated as legal approval before Norwegian counsel approves the exact wording, placement, interaction and evidence design.

---

## 1. Pre-contract disclosure pack

### 1.1 Pricing-page disclosure — Bokmål

**Prisene inkluderer norsk MVA.** Abonnementet fornyes automatisk etter valgt betalingsperiode til du sier det opp. Det finnes ingen skjult eller automatisk belastning for overforbruk. Når inkludert bruk er oppbrukt, stopper eller begrenses relevant funksjon til neste periode eller til du uttrykkelig kjøper et tillegg.

Atlas leveres som en løpende digital AI-tjeneste med Atlas-administrert leverandørtilgang. Tilgjengelige modeller, funksjoner og leverandører kan endres innenfor loven og de godkjente avtalevilkårene. AI-output kan være feil eller ufullstendig og må kontrolleres før vesentlig bruk.

Du har som hovedregel 14 dagers angrerett. Dersom du uttrykkelig ber om at tjenesten starter før angrefristen utløper og deretter angrer, kan du måtte betale et lovlig forholdsmessig beløp for tjenesten som allerede er levert. Aktivering av et løpende abonnement medfører ikke i seg selv at angreretten bortfaller.

### 1.2 Pricing-page disclosure — English

**Prices include Norwegian VAT.** The subscription renews automatically for the selected billing period until cancelled. There is no hidden or automatic excess-use charge. When included use is exhausted, the relevant function stops or is limited until the next period or until you expressly purchase an add-on.

Atlas is supplied as a continuing digital AI service with Atlas-managed provider access. Available models, features and providers may change within applicable law and the approved contract terms. AI output may be inaccurate or incomplete and must be checked before consequential use.

You generally have a 14-day right of withdrawal. If you expressly request commencement before the withdrawal period expires and then withdraw, you may have to pay a lawful proportionate amount for service already supplied. Activating a continuing subscription does not by itself extinguish the withdrawal right.

### 1.3 Plan-card minimum disclosure

Each plan card must display without expansion:

- plan name;
- gross price and billing period;
- named-user limit;
- standard units and premium boosts;
- whether allowances are individual or shared;
- one-line rollover rule;
- `Ingen automatisk belastning for overforbruk` / `No automatic excess-use charge`;
- renewal/cancellation line;
- link to complete plan details and legal information.

### 1.4 Plan-detail disclosure

Each plan-detail page must add:

- service characteristics and intended use;
- account and supported-device/browser requirements;
- functionality, compatibility and interoperability;
- provider/model dependency;
- activation time;
- support channel;
- exact duration and commitment;
- next billing and renewal model;
- cancellation route;
- withdrawal notice;
- early-start choice;
- top-up prices and expiry;
- rollover calculation;
- statutory complaint/remedy summary;
- customer-content export/deletion summary;
- eligibility restrictions;
- terms, privacy and acceptable-use versions.

---

## 2. Final checkout summary

### 2.1 Mandatory order-summary fields

The final screen immediately before the payment action must show prominently:

1. **Selected offer:** plan name and offer ID.
2. **Main characteristics:** named users, included units, boosts and material limitations.
3. **Price:** total amount including MVA and currency.
4. **Billing:** monthly, annual or semester interval; first and next payment dates.
5. **Duration:** continuing or fixed period; minimum commitment if any.
6. **Renewal:** automatic renewal and cancellation deadline/effect.
7. **Top-ups:** not automatic; separate purchase required.
8. **Early commencement:** consumer choice and effect on proportional payment.
9. **Withdrawal:** 14-day right and direct access to notice/form.
10. **Provider/model change:** concise material dependency statement.
11. **Terms:** exact version and downloadable durable copy.
12. **Eligibility:** student, adult payer and Family requirements.

Material information must not be hidden only behind a link or collapsed panel. Links may provide detail, but the statutory core must remain visible near the final button.

### 2.2 Monthly subscription summary — Bokmål

**Du bestiller [PLAN].** Pris: **NOK [BELØP] inkludert MVA per måned**. Abonnementet starter [DATO/TID] og fornyes automatisk hver måned. Neste betaling er [DATO]. Du kan si opp før neste betalingsdato. Oppsigelsen gjelder normalt fra neste betalingsdato, og du beholder tilgang til utløpet av betalt periode.

Inkludert bruk: [ENHETER] standardenheter og [BOOSTS] premium boosts per måned for [BRUKERE]. Det belastes ikke automatisk for overforbruk.

### 2.3 Monthly subscription summary — English

**You are ordering [PLAN].** Price: **NOK [AMOUNT] including VAT per month**. The subscription starts on [DATE/TIME] and renews automatically each month. The next payment is [DATE]. You may cancel before the next payment date. Cancellation normally takes effect on that date and access continues through the paid period.

Included use: [UNITS] standard units and [BOOSTS] premium boosts per month for [USERS]. Excess use is not charged automatically.

### 2.4 Annual and semester warning

Annual and semester variants must remain unavailable until an approved legal model specifies:

- prepaid versus binding-term status;
- total price and effective monthly comparison;
- exact start/end dates;
- renewal or non-renewal;
- cancellation and avbestilling treatment;
- statutory reminder and economic-benefit conditions;
- refund calculation.

---

## 3. Final payment-button copy

### 3.1 Recommended labels

| Purchase | Bokmål | English | Status |
|---|---|---|---|
| Monthly subscription | `Bestill abonnement med forpliktelse til å betale` | `Order subscription with obligation to pay` | `RECOMMENDED_PENDING_LEGAL_APPROVAL` |
| Annual subscription | `Bestill årsabonnement med forpliktelse til å betale NOK [TOTAL]` | `Order annual subscription with obligation to pay NOK [TOTAL]` | `BLOCKED_MODEL_PENDING` |
| Semester subscription | `Bestill semesterabonnement med forpliktelse til å betale NOK [TOTAL]` | `Order semester subscription with obligation to pay NOK [TOTAL]` | `BLOCKED_MODEL_PENDING` |
| Standard top-up | `Kjøp 250 enheter for NOK 39` | `Buy 250 units for NOK 39` | `PENDING_LEGAL_AND_TAX_REVIEW` |
| Premium boosts | `Kjøp 5 premium boosts for NOK 59` | `Buy 5 premium boosts for NOK 59` | `PENDING_LEGAL_AND_TAX_REVIEW` |
| Family top-up | `Kjøp 500 Family-enheter for NOK 79` | `Buy 500 Family units for NOK 79` | `PENDING_LEGAL_AND_TAX_REVIEW` |

### 3.2 Acceptable examples

1. `Bestill abonnement med forpliktelse til å betale`.
2. `Kjøp nå for NOK 159 inkludert MVA`.
3. `Start betalt månedsabonnement – NOK 159 per måned`.
4. `Bestill årsabonnement – betal NOK [TOTAL] nå`.
5. `Kjøp 250 enheter for NOK 39`.

Acceptance remains subject to complete immediate information and counsel approval.

### 3.3 Prohibited examples

1. `Fortsett`.
2. `Neste`.
3. `Bekreft`.
4. `Start`.
5. `Aktiver`.
6. `Opprett konto`.
7. `Fullfør`.
8. `Prøv Atlas` where payment follows.
9. `Kom i gang`.
10. Any button where payment wording appears only elsewhere on the page.

---

## 4. Consent and acknowledgement design

### 4.1 Required interaction separation

| Interaction | Required state | May be combined? |
|---|---|---|
| Acceptance of consumer terms | Explicit affirmative action | May be one terms checkbox, but not pre-ticked |
| Early commencement request | Separate unticked checkbox | Do not bundle with general terms |
| Proportional-payment acknowledgement | Included in the same early-start statement if counsel approves the complete wording | Pending legal approval |
| Loss after full performance of a separately completed service component | Separate statement if relevant | Do not use for continuing subscription access |
| Digital-content waiver | Not default for subscriptions | Separate only if a genuinely separate digital-content supply is legally approved |
| Privacy notice acknowledgement | Informational, not consent where another lawful basis applies | Keep separate from purchase |
| Marketing consent | Optional and unticked | Never condition purchase on it |
| Recurring payment authorisation | Clearly stated in order summary and payment flow | May be part of paid order if explicit |

### 4.2 Terms checkbox — Bokmål

`Jeg har lest og godtar forbrukervilkårene og planinformasjonen som gjelder for bestillingen. Jeg forstår pris, betalingsintervall, automatisk fornyelse, inkludert bruk og hvordan abonnementet sies opp.`

### 4.3 Terms checkbox — English

`I have read and accept the Consumer Terms and plan information for this order. I understand the price, billing interval, automatic renewal, included use and how to cancel the subscription.`

### 4.4 Early commencement — recommended Bokmål

`Jeg ber uttrykkelig om at Atlas starter den betalte digitale tjenesten før angrefristen på 14 dager er utløpt. Jeg forstår at jeg fortsatt kan angre innen fristen, men at jeg kan måtte betale et lovlig forholdsmessig beløp for tjenesten som er levert frem til jeg gir beskjed om at jeg angrer.`

### 4.5 Early commencement — recommended English

`I expressly request Atlas to start the paid digital service before the 14-day withdrawal period expires. I understand that I may still withdraw within that period, but may have to pay a lawful proportionate amount for service supplied until I notify Atlas of my withdrawal.`

### 4.6 Delayed activation alternative

- Bokmål: `Aktiver tjenesten når angrefristen på 14 dager er utløpt.`
- English: `Activate the service after the 14-day withdrawal period has expired.`

The interface should require the consumer to choose early or delayed start. No option may be preselected.

---

## 5. Withdrawal notice

### 5.1 Bokmål

## Informasjon om angrerett

Du har som hovedregel rett til å gå fra avtalen uten å oppgi noen grunn innen 14 dager. Fristen utløper 14 dager etter at avtalen ble inngått.

For å bruke angreretten må du informere **[ATLAS AVTALEPART, ADRESSE OG E-POST TBD]** om beslutningen gjennom en entydig erklæring. Du kan bruke angreskjemaet nedenfor, men det er ikke obligatorisk. Det er tilstrekkelig at meldingen sendes før fristen utløper.

Dersom du uttrykkelig har bedt om at en betalt tjeneste starter før angrefristen utløper, og du deretter angrer, kan du bli ansvarlig for et lovlig forholdsmessig beløp for den delen av tjenesten som er levert frem til du meldte fra. Du skal ikke betale dette dersom Atlas ikke har gitt nødvendig informasjon eller ikke har innhentet den uttrykkelige anmodningen som loven krever.

Ved gyldig angring tilbakebetaler Atlas alle beløp som skal refunderes uten unødig opphold og senest 14 dager etter mottatt melding. Tilbakebetaling skjer med samme betalingsmiddel, med mindre noe annet er uttrykkelig avtalt, og uten gebyr.

### 5.2 English

## Information on the right of withdrawal

You generally have the right to withdraw from the contract without giving a reason within 14 days. The period expires 14 days after the contract is concluded.

To exercise the right, inform **[ATLAS CONTRACTING ENTITY, ADDRESS AND EMAIL TBD]** of your decision through an unequivocal statement. You may use the model form below, but it is not mandatory. It is sufficient to send the notice before the deadline.

If you expressly requested commencement of a paid service before the withdrawal period expired and then withdraw, you may be responsible for a lawful proportionate amount for the service supplied until you notified Atlas. You do not owe that amount where Atlas failed to provide the required information or obtain the express request required by law.

For a valid withdrawal, Atlas reimburses all refundable amounts without undue delay and no later than 14 days after receiving the notice. Reimbursement uses the same payment method unless expressly agreed otherwise and carries no fee.

---

## 6. Model withdrawal form

### 6.1 Bokmål

**Til:** [ATLAS AVTALEPART, ADRESSE OG E-POST]

Jeg/vi gir herved melding om at jeg/vi ønsker å gå fra avtalen om følgende digitale tjeneste:

- Plan eller tillegg:
- Ordrenummer:
- Bestillingsdato:
- Kundens navn:
- Kundens adresse:
- Kundens e-post:
- Dato:
- Signatur, bare dersom skjemaet sendes på papir:

### 6.2 English

**To:** [ATLAS CONTRACTING ENTITY, ADDRESS AND EMAIL]

I/we hereby give notice that I/we withdraw from the contract for the following digital service:

- Plan or add-on:
- Order number:
- Order date:
- Customer name:
- Customer address:
- Customer email:
- Date:
- Signature, only if submitted on paper:

### 6.3 Digital withdrawal route

Current implementation recommendation:

- customer account action: `Angre avtalen` / `Withdraw from contract` during the applicable period;
- email fallback where account access is unavailable;
- immediate automated acknowledgement;
- case ID and durable confirmation;
- no forced reason field;
- optional feedback field clearly marked optional.

Future enacted requirements concerning an electronic withdrawal function must be monitored and activated when their commencement date is confirmed.

---

## 7. Cancellation policy and workflow

### 7.1 Consumer policy

- Monthly plans may be cancelled at any time before the next billing date.
- Cancellation normally stops renewal and takes effect at the next billing date.
- Access continues through the paid period unless immediate termination is chosen or legally required.
- Cancellation is available in the customer account and by email/support fallback.
- A customer who cannot access the account must not be denied cancellation.
- No mandatory retention call, questionnaire or counteroffer may block cancellation.
- Atlas sends immediate durable confirmation.
- Withdrawal, statutory termination for defect and cancellation must remain distinct choices.

### 7.2 End-to-end workflow

1. Authenticate the customer or perform proportionate identity verification.
2. Display plan, next payment date, access-end date and any allowance effect.
3. Offer:
   - `Cancel at next payment date`;
   - `Withdraw from contract`, where applicable;
   - `Report a defect or service problem`;
   - `Request immediate cancellation`, where supported.
4. Ask for optional reason only after the legal route is selected.
5. Confirm the choice without adding new barriers.
6. Create cancellation event and prevent future renewal.
7. Send durable confirmation immediately.
8. Schedule entitlement shutdown at the effective time.
9. Preserve export/deletion route.
10. Reconcile order, payment, entitlement and accounting records.

### 7.3 Cancellation confirmation — Bokmål

**Emne: Bekreftelse på oppsigelse av [PLAN]**

Vi bekrefter at abonnementet ditt er sagt opp.

- Plan: [PLAN]
- Ordrenummer: [ORDER ID]
- Oppsigelse mottatt: [TIMESTAMP]
- Neste betaling: Ingen / [DETAIL]
- Tilgangen avsluttes: [DATE/TIME]
- Ubrukt kvote og tillegg: [TREATMENT]
- Eksport og sletting: [LINK/INSTRUCTION]

Dette er en oppsigelse av fremtidig fornyelse. Dersom du ønsket å bruke angreretten eller gjøre gjeldende en mangel, kontakt [CHANNEL] og oppgi saksnummer [CASE ID].

### 7.4 Cancellation confirmation — English

**Subject: Confirmation of cancellation of [PLAN]**

We confirm that your subscription has been cancelled.

- Plan: [PLAN]
- Order number: [ORDER ID]
- Cancellation received: [TIMESTAMP]
- Next payment: None / [DETAIL]
- Access ends: [DATE/TIME]
- Unused allowance and add-ons: [TREATMENT]
- Export and deletion: [LINK/INSTRUCTION]

This cancellation stops future renewal. If you intended to exercise the right of withdrawal or report non-conformity, contact [CHANNEL] and quote case [CASE ID].

---

## 8. Refund and statutory-remedy decision matrix

| Reason code | Legal/commercial basis | Default decision | Approval level | Required evidence |
|---|---|---|---|---|
| `WITHDRAWAL_NO_START` | Statutory withdrawal; no commencement | Full refund | Automatic after validation | Order, deadline and no activation evidence |
| `WITHDRAWAL_VALID_EARLY_START` | Statutory withdrawal after valid early commencement | Refund less approved proportional amount | Automatic calculation + audit | Consent text/version, activation and elapsed service |
| `WITHDRAWAL_INVALID_CONSENT` | Missing information/request | Full refund; no proportional deduction | Automatic | Consent or disclosure failure |
| `NON_DELIVERY` | Statutory delay | Full refund if terminated | Support lead | Delivery logs and notice |
| `DEFECT_CURE` | Non-conformity | Repair/replacement first where lawful and proportionate | Support | Incident and service evidence |
| `DEFECT_PRICE_REDUCTION` | Statutory price reduction | Proportionate credit/refund | Legal/finance threshold | Defect period, severity and price basis |
| `DEFECT_TERMINATION` | Material non-conformity | Full or prorated statutory refund | Legal + finance | Remedy history and termination basis |
| `ADVERSE_SERVICE_CHANGE` | Statutory termination right | Prorated refund where applicable | Legal + finance | Change notice and impact |
| `DUPLICATE_CHARGE` | Billing error | Full duplicate refund | Automatic | Payment IDs |
| `UNAUTHORISED_RENEWAL` | No valid authorisation/notice | Full affected charge refund | Payment/legal escalation | Contract and payment evidence |
| `ORDINARY_CANCELLATION` | Future renewal stopped | No retrospective refund by default | Automatic | Cancellation timestamp |
| `GOODWILL` | Discretionary | Case-specific | Defined monetary authority | Reason and approval |
| `CHARGEBACK` | Payment-provider process | Prevent double reimbursement | Finance | Provider case ID |
| `TOPUP_UNUSED` | Pending legal/tax model | Block automated decision | Legal + tax | Purchase and entitlement ledger |
| `TOPUP_PARTLY_USED` | Pending legal/tax model | Block automated decision | Legal + tax | Unit-level usage and valuation |

### 8.1 Refund deadlines and method

- Statutory withdrawal refunds: no later than 14 days after receipt of a valid notice.
- Digital-service termination/price-reduction refunds: apply the statutory deadline relevant to the remedy; system target should be materially shorter.
- Use the original payment method unless expressly agreed otherwise.
- Do not deduct administrative, card or processing fees from a statutory refund.
- Generate the required credit note/MVA correction.
- Record payment-provider completion, not merely internal approval.

---

## 9. Internal cancellation SOP

### 9.1 Triage

1. Identify the customer and order.
2. Identify the requested legal route:
   - withdrawal;
   - ordinary cancellation;
   - defect/non-conformity;
   - price or service change;
   - duplicate/unauthorised charge;
   - goodwill.
3. Do not silently reclassify the request to the least costly route.
4. Confirm the consumer’s intended outcome where wording is ambiguous, without delaying a clear cancellation.

### 9.2 Processing

1. Freeze future renewal where cancellation is clear.
2. Capture timestamp, channel and exact customer statement.
3. Calculate effective date.
4. Check withdrawal window and early-start evidence.
5. Check defect and incident records.
6. Determine refund/credit-note requirement.
7. Send durable confirmation.
8. Schedule entitlement and data actions.
9. Reconcile order, payment, ledger and accounting status.

### 9.3 Escalation triggers

Escalate to legal/finance where:

- annual or semester commitment is involved;
- Family member and payer disagree;
- minor or guardian authority is disputed;
- top-up is partly used;
- proportional payment exceeds a simple approved formula;
- chargeback overlaps an internal refund;
- customer alleges misleading marketing or invalid consent;
- material defect or damages are claimed;
- foreign VAT/OSS is involved.

---

## 10. Internal refund SOP

1. Open a refund case with immutable reason code.
2. Validate customer, order, payment and entitlement events.
3. Validate the legal basis and deadline.
4. Determine gross refund and MVA/credit-note dependency.
5. Apply the approved calculation only; otherwise escalate.
6. Submit through the payment provider.
7. Record provider transaction ID and completion state.
8. Send consumer confirmation.
9. Adjust entitlement and usage ledger.
10. Post/reconcile accounting entry and credit note.
11. Close only after payment-provider and finance readback agree.

### 10.1 Approval controls

Exact monetary authority limits remain `PENDING_PROJECT_OWNER_AND_FINANCE_APPROVAL`. Until approved:

- clear statutory full refunds and duplicate charges may be automated only after test evidence;
- proportional, defect, top-up, annual, semester, Family and cross-border cases require manual approval;
- no support agent may waive mandatory rights or invent a fee.

---

## 11. Top-up and premium-boost operations

### 11.1 Required pre-purchase disclosure

- exact units/boosts;
- total gross price;
- account/Family group receiving entitlement;
- expiry and rollover;
- non-transferability;
- no cash value;
- delivery/activation timing;
- withdrawal and partial-use treatment;
- effect of base-plan cancellation;
- provider/model dependency.

### 11.2 Control recommendation

- top-ups may only be purchased by the adult contract holder;
- no top-up purchase by subordinate/minor accounts;
- no auto-reload or one-click purchase until separate payment and consent validation passes;
- no consumption until entitlement event is confirmed;
- maintain unit-level ledger for refunds, reconciliation and disputes;
- block checkout until tax adviser confirms supply/tax-point treatment and counsel confirms withdrawal treatment.

---

## 12. Family, student, minor and guardian operations

### 12.1 Student

- first consumer launch recommendation: purchaser must be 18+;
- verify student status at purchase and periodically;
- disclose evidence types and data retention;
- provide notice before eligibility expiry or plan migration;
- never imply educational exemption or institutional accreditation without evidence.

### 12.2 Family

- adult payer is contract holder;
- maximum four named household users;
- unique identity for each member;
- no credential sharing;
- adult payer controls purchases and renewal;
- individual users retain applicable privacy/data rights;
- member removal does not silently delete data without notice/export opportunity;
- household verification must be proportionate.

### 12.3 Minors

- minors cannot purchase or accept paid terms independently;
- child access remains disabled until guardian, age, privacy and safety controls pass;
- direct exhortation to children to purchase is prohibited;
- no behavioural advertising or unnecessary profiling of children;
- any guardian consent must be verifiable and revocable where applicable.

---

## 13. Durable-medium confirmation

### 13.1 Required record

The confirmation must contain or attach:

- supplier identity, organisation number, MVA status and contacts;
- customer/payer identity;
- order ID and timestamp;
- plan and offer version;
- complete plan characteristics;
- gross price, tax, billing interval and next payment date;
- duration, commitment and renewal;
- allowances, top-ups and rollover;
- activation date/time;
- cancellation method;
- complete terms and policy versions;
- withdrawal notice and form;
- early-start request and exact acknowledgement;
- recurring-payment authorisation;
- complaint/remedy contacts;
- export/deletion information;
- immutable contract snapshot/hash.

### 13.2 Confirmation email — Bokmål

**Emne: Avtalebekreftelse for Atlas AI – [PLAN] – [ORDER ID]**

Takk for bestillingen. Avtalen din er inngått og bekreftes nedenfor og i vedleggene.

- Avtalepart: [ENTITY]
- Kunde: [CUSTOMER]
- Plan: [PLAN]
- Ordrenummer: [ORDER ID]
- Avtaleversjon: [VERSION]
- Pris: NOK [AMOUNT] inkludert MVA [TAX DETAIL]
- Betalingsintervall: [INTERVAL]
- Startdato: [DATE/TIME]
- Neste betaling: [DATE]
- Oppsigelse: [METHOD AND EFFECT]
- Inkludert bruk: [ALLOWANCE]
- Tidlig oppstart valgt: [YES/NO]
- Registrert erklæring: [EXACT TEXT OR ATTACHED RECORD]

Vedlagt finner du forbrukervilkår, planinformasjon, angreinformasjon og angreskjema. Lagre denne meldingen.

Kontakt: [SUPPORT/WITHDRAWAL CHANNEL]

### 13.3 Confirmation email — English

**Subject: Atlas AI contract confirmation – [PLAN] – [ORDER ID]**

Thank you for your order. Your contract has been concluded and is confirmed below and in the attachments.

- Contracting entity: [ENTITY]
- Customer: [CUSTOMER]
- Plan: [PLAN]
- Order number: [ORDER ID]
- Contract version: [VERSION]
- Price: NOK [AMOUNT] including VAT [TAX DETAIL]
- Billing interval: [INTERVAL]
- Start date: [DATE/TIME]
- Next payment: [DATE]
- Cancellation: [METHOD AND EFFECT]
- Included use: [ALLOWANCE]
- Early commencement selected: [YES/NO]
- Recorded declaration: [EXACT TEXT OR ATTACHED RECORD]

The Consumer Terms, plan information, withdrawal notice and model form are attached. Save this message.

Contact: [SUPPORT/WITHDRAWAL CHANNEL]

### 13.4 Delivery controls

- send immediately after contract conclusion and before service performance begins;
- attach or embed complete immutable versions, not only mutable web links;
- log message ID, recipient, timestamp, template version and delivery result;
- provide account download of the same snapshot;
- retry failed delivery and alert operations;
- do not activate until confirmation generation succeeds, unless counsel approves a controlled exception.

---

## 14. Six-month reminder template

### Bokmål

**Emne: Påminnelse om ditt løpende Atlas AI-abonnement**

Du har følgende løpende abonnement:

- Plan: [PLAN]
- Pris: NOK [AMOUNT] inkludert MVA per [INTERVAL]
- Neste betaling: [DATE]
- Inkludert bruk: [ALLOWANCE]

Du kan se eller si opp abonnementet her: [DIRECT CANCELLATION ROUTE]. Du kan også kontakte [SUPPORT]. Oppsigelse skal ikke være vanskeligere enn å inngå avtalen.

### English

**Subject: Reminder about your continuing Atlas AI subscription**

You have the following continuing subscription:

- Plan: [PLAN]
- Price: NOK [AMOUNT] including VAT per [INTERVAL]
- Next payment: [DATE]
- Included use: [ALLOWANCE]

View or cancel here: [DIRECT CANCELLATION ROUTE]. You may also contact [SUPPORT]. Cancellation must not be more difficult than contracting.

---

## 15. Evidence and retention controls

Minimum evidence objects:

1. `OfferVersion`.
2. `DisclosureSnapshot`.
3. `CheckoutSession`.
4. `ConsentEvent`.
5. `PaymentAuthorisation`.
6. `OrderContractSnapshot`.
7. `DurableMediumDelivery`.
8. `EntitlementEvent`.
9. `UsageEvent`.
10. `WithdrawalCase`.
11. `CancellationCase`.
12. `RemedyRefundCase`.
13. `PaymentRefundEvent`.
14. `CreditNoteReference`.
15. `DataExportDeletionCase`.
16. `ReconciliationRun`.

Retention periods must be defined through an approved privacy, accounting and legal-retention schedule. Evidence must be proportionate, access-controlled, auditable and protected from unauthorised alteration.

---

## 16. Operational release gates

This pack may move to implementation only after:

- Norwegian lawyer approves wording and legal classifications;
- contracting entity fields are complete;
- MVA and refund documentation is approved;
- payment-provider capabilities are validated;
- Members Area/identity design is implemented;
- consent and durable-medium storage is implemented;
- cancellation, withdrawal, refund and export flows are implemented;
- Bokmål/English parity and accessibility tests pass;
- all acceptance evidence is read back;
- written release approval is recorded.

Until then, no Wix Pricing Plan or consumer checkout may be created or activated.