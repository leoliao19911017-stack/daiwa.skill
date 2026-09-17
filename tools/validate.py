#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
ROOT=Path(__file__).resolve().parents[1]
errors=[]

def err(msg): errors.append(msg)

# UTF-8 / CRLF / BOM
for p in ROOT.rglob('*'):
    if p.is_file() and '.git' not in p.parts:
        b=p.read_bytes()
        if b.startswith(b'\xef\xbb\xbf'): err(f'BOM: {p.relative_to(ROOT)}')
        if b'\r\n' in b: err(f'CRLF: {p.relative_to(ROOT)}')
        if p.suffix.lower() in {'.md','.json','.jsonl','.py','.yml','.yaml'}:
            try: b.decode('utf-8')
            except UnicodeDecodeError: err(f'non-utf8: {p.relative_to(ROOT)}')

m=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
refs=[]
refs += [m['entrypoint'], m['evals']]
refs += m.get('examples',[])
for v in m.get('knowledge',{}).values():
    if isinstance(v,str): refs.append(v)
for v in m.get('references',{}).values():
    if isinstance(v,str): refs.append(v)
for r in refs:
    if not (ROOT/r).exists(): err(f'missing manifest path: {r}')

# JSONL valid + unique id + rubric schema
ids=set()
for path in [ROOT/m['evals'], *[ROOT/x for x in m.get('examples',[])]]:
    for n,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try: obj=json.loads(line)
        except Exception as e: err(f'bad jsonl {path.name}:{n}: {e}'); continue
        if path == ROOT/m['evals']:
            i=obj.get('id')
            if i in ids: err(f'duplicate eval id: {i}')
            ids.add(i)
            if 'rubric' not in obj or 'forbidden' not in obj: err(f'old eval schema: {i}')

# scenario index targets
idx=json.loads((ROOT/'knowledge/scenario_index.json').read_text(encoding='utf-8'))
for k, vals in idx.items():
    for v in vals:
        target=ROOT/'knowledge'/v
        if not target.exists(): err(f'scenario index {k} -> missing {v}')

# family schema labels present in family_alignment
fa=(ROOT/'knowledge/family_alignment.md').read_text(encoding='utf-8')
required=['本周只练一件事','统一第一句话','如果仍不配合','所有大人都不做','孩子可以有的感受','边界不改变','本周只观察一个进步']
for x in required:
    if x not in fa: err(f'family card missing label: {x}')

if errors:
    print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print(f'OK: validation passed ({len(ids)} evals)')
