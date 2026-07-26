# Atlas research evidence artifacts — 03:14, 26.07.2026

The two complete Markdown source reports are stored as deterministic gzip-compressed, Base64-encoded UTF-8 text so they can be preserved through the GitHub text-file connector.

## Files

- `ATLAS_CONSUMER_LAW_CHECKOUT_REPORT_2037_25072026_RAW.md.gz.b64`
- `ATLAS_PRICING_BUDGET_UNIT_ECONOMICS_REPORT_1301_25072026_RAW.md.gz.b64`
- `ATLAS_RESEARCH_ARTIFACT_INTEGRITY_MANIFEST_0314_26072026.json`

## Decode and verify

```bash
base64 --decode < FILE.md.gz.b64 | gzip --decompress > FILE.md
sha256sum FILE.md
```

Expected decoded SHA-256 values:

- consumer-law Markdown: `09c935fca277ed2e097b5967a293af2818f212ab0725e89226816110c8784e09`
- pricing Markdown: `e2375d9ea5b7ce8ce4fd612cf13648b978cbd78a0774f9c1d1b32c925c624948`

The corresponding original DOCX files are archived in the controlled private Google Drive evidence folder and are fingerprinted in the integrity manifest.

## Authority

The raw reports are evidence. The approved pricing values are governed by the canonical decisions register. Atlas-specific legal interpretations remain pending professional review. These artifacts do not change `publicAllowed=false`, `purchaseAllowed=false`, checkout `NO_GO`, or any production lock.
