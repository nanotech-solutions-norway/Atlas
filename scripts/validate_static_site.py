from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
required = ['index.html','en/index.html','solutions/index.html','en/solutions/index.html','managed-secure/index.html','en/managed-secure/index.html','pricing/index.html','en/pricing/index.html','trust/index.html','en/trust/index.html','onboarding/index.html','en/onboarding/index.html','assets/css/styles.css','assets/js/main.js','schemas/atlas_cms_fields.json','schemas/claims_registry.schema.json','schemas/intake_payload.schema.json','schemas/route_contracts.json','cms-seeds/packages.json','cms-seeds/claims_registry.json','docs/implementation/implementation-register.md']
errors=[]
for rel in required:
    if not (root/rel).exists(): errors.append(f'Missing required file: {rel}')
for html in root.rglob('*.html'):
    txt=html.read_text(encoding='utf-8')
    if '<meta name="viewport"' not in txt: errors.append(f'Missing viewport: {html.relative_to(root)}')
    if '<title>' not in txt: errors.append(f'Missing title: {html.relative_to(root)}')
for js in list((root/'schemas').glob('*.json')) + list((root/'cms-seeds').glob('*.json')):
    try: json.loads(js.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'Invalid JSON {js.relative_to(root)}: {exc}')
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.html','.md','.json','.csv','.js','.css','.yml','.yaml','.txt'}:
        txt=path.read_text(encoding='utf-8', errors='ignore')
        if 'BEGIN PRIVATE KEY' in txt or 'OPENAI_API_KEY=' in txt or re.search(r'sk-[A-Za-z0-9]{10,}', txt): errors.append(f'Potential secret pattern in {path.relative_to(root)}')
claims=json.loads((root/'cms-seeds/claims_registry.json').read_text(encoding='utf-8'))
for c in claims:
    for key in ['claim_id','claim','category','evidence_ref','approval_status','owner','review_date']:
        if not c.get(key): errors.append(f'Claims registry missing {key}: {c}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Atlas AI validation passed.')
