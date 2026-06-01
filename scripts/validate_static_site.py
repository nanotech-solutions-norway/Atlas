from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
required=['index.html','404.html','robots.txt','sitemap.xml','assets/css/styles.css','assets/js/main.js','schemas/atlas_cms_fields.json','schemas/published_record_policy.json','docs/implementation/implementation-register.md']
errors=[]
for rel in required:
    if not (root/rel).exists(): errors.append(f'Missing required file: {rel}')
for html in root.rglob('*.html'):
    txt=html.read_text(encoding='utf-8')
    if '<meta name="viewport"' not in txt: errors.append(f'Missing viewport: {html.relative_to(root)}')
    if '<title>' not in txt: errors.append(f'Missing title: {html.relative_to(root)}')
for js in root.glob('schemas/*.json'):
    try: json.loads(js.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'Invalid JSON {js.relative_to(root)}: {exc}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Atlas validation passed.')
