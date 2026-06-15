# Wix Claim Correction Plan — 12:38, 10.06.2026

## Scope
Live/test URL reviewed: `https://www.atlas-ai.no/blank?rc=test-site`.

Primary control sources:
- `Atlas_Master_Claims_Evidence_Vendor_Validation_Report_1120_10062026.docx`
- `docs/adr/ADR-0005-master-claims-evidence-vendor-validation.md`
- `docs/claims/claims-registry.yml`
- `docs/claims/evidence-index.yml`
- `docs/claims/not-approved-claims.yml`

## Executive correction rule
The Wix test page must be rewritten so that no direct Atlas-specific claim appears unless it is supported by an approved claims-registry item and evidence reference. External research may be used only as attributed context. Vendor trust/compliance/SLA statements must be vendor-attributed, service-specific and caveated.

## Launch status
Current status: `not publication-ready for claims governance`.

## High-priority corrections from current Wix test copy

| Page area | Current wording / claim type | Status | Required replacement direction |
|---|---|---:|---|
| Proof numbers section | "Bevis i tall – Atlas i praksis" and "Reelle resultater fra norske brukere og virksomheter" | Not approved | Replace with "Ekstern dokumentasjon og styringsprinsipper" or remove until Atlas evidence exists. |
| Proof number | 87% Tidsbesparelse | Not approved | "Designet for å redusere manuelt arbeid i definerte arbeidsflyter." |
| Proof number | 73% Bedre karakterer | Not approved | "Støtter ansvarlig studieplanlegging, forklaring, repetisjon og kildearbeid." |
| Proof number | 91% Fornøyde brukere | Not approved | Remove until Atlas survey evidence exists. |
| Proof number | 94% Brukertilfredshet / NPS | Not approved | Remove until Atlas-approved survey evidence exists. |
| Proof number | 3x Raskere arbeidsflyt | Not approved | "Mer strukturert arbeidsflyt i avgrensede prosesser." |
| Proof number | 12K+ aktive brukere | Not approved | Remove until analytics evidence exists. |
| Proof number | 98% Oppetid / garantert tilgjengelighet | Not approved | "Tilgjengelighet avhenger av valgt leveransemodell, leverandørstack og avtalevilkår." |
| Consumer segment | "En personlig assistent som husker..." | Needs revision | Avoid emotional-companion/persistent-memory implication. Use "praktisk planleggings- og skrivehjelp innenfor tydelige personverngrenser." |
| Student segment | "Oppgavehjelp" and "Skriv oppgaver" | Needs revision | Replace with responsible study wording: no ghostwriting, no direct assignment submission. |
| Trust headline | "GDPR-trygg" | Not approved | "GDPR-tilpasset styring" or "Designet for GDPR-tilpasset bruk" with legal review caveat. |
| Privacy copy | "All databehandling skjer i henhold til norsk og europeisk personvernlovgivning" | Needs evidence/legal review | "Atlas er designet for å støtte GDPR-tilpasset bruk gjennom dataminimering, leverandøravklaringer og dokumenterte rutiner." |
| Comparison table | "Data lagret i Norge" / "Alltid" | Not approved | "Datalagring avklares per leverandør, region, plan og leveransemodell." |
| Integration row | "Altinn, ByggNett, Visma m.fl." | Needs evidence | "Integrasjoner vurderes etter system, API, tilgang og sikkerhetskrav." |
| Sector row | "Finans, helse, offentlig m.fl." | Needs legal/security review | "Sektorbruk vurderes etter datakategori, risikoprofil og regulatoriske krav." |
| Certification cards | ISO 27001 / SOC 2 Type II | Not approved as Atlas claim | Attribute only to relevant vendors and services; do not imply Atlas certification. |
| DPA card | "DPA included for all customers" | Needs legal scope | "Databehandleravtale og leverandørvilkår avklares etter valgt tjeneste og avtaleform." |
| Data residency card | "Servere lokalisert i Norge" | Not approved | "Region og lagring dokumenteres per valgt leveransemodell." |
| Security section | "Atlas overholder GDPR fullt ut" | Not approved | "Atlas er designet for GDPR-tilpasset drift; endelig juridisk posisjon krever behandlingsprotokoll, DPA-kartlegging og legal review." |
| Security section | "Ingen data deles med tredjeparter" | Not approved | "Tredjepartsleverandører og databehandling beskrives i leverandøroversikt og personvernerklæring." |
| Security section | "All data lagres på norske servere" | Not approved | "Datalagring og leverandørtilgang avhenger av tjeneste, region, plan, kontrakt og konfigurert leveransemodell." |

## Replacement section recommendation
Replace the entire quantitative proof block with a controlled trust/evidence block until Atlas-specific measurements exist:

### Suggested block title
`Dokumentert styring før resultatpåstander`

### Suggested short copy
`Atlas bruker eksterne AI-studier og leverandørdokumentasjon som kontekst, ikke som direkte bevis for Atlas-resultater. Tall om tidsbesparelse, ROI, læringsutbytte, brukertilfredshet, oppetid eller sikkerhet publiseres først når Atlas har godkjent pilot-, kunde-, produksjons- eller revisjonsgrunnlag.`

### Suggested cards
1. `Ekstern forskning` — `Brukes som kontekst og alltid med kilde og bruksområde.`
2. `Leverandørdokumentasjon` — `Brukes med tydelig leverandørnavn, tjeneste, plan, region og avtalevilkår.`
3. `Atlas-evidence` — `Kreves før Atlas publiserer egne resultat-, ROI-, uptime- eller sikkerhetstall.`
4. `Menneskelig kontroll` — `AI-resultater kvalifiseres med oppgavegrenser, QA og ansvarlig bruk.`

## Form and intake copy that must be visible before launch
`Ikke last opp konfidensielle, sensitive, regulerte eller kundespesifikke filer i dette skjemaet. Hvis behovet krever kontrollert behandling, rutes saken først til architecture review og deretter til en godkjent sikker inntaksprosess.`

## Completion checklist
- [ ] Remove or rewrite all unsupported quantitative proof numbers.
- [ ] Replace blanket GDPR/data-residency/security claims.
- [ ] Convert provider certification and SLA claims to vendor-attributed caveated wording.
- [ ] Add visible no-confidential-upload warning to ordinary Wix forms.
- [ ] Add provider disclosure link from Trust, Pricing, Managed Secure and all forms.
- [ ] Add student responsible-use boundary to student page/cards.
- [ ] Add consumer safety boundary to consumer page/cards.
- [ ] Validate all public claims against `docs/claims/claims-registry.yml`.
- [ ] Capture Wix screenshots and URL evidence after correction.
- [ ] Mark page as publication-ready only after legal/security review.
