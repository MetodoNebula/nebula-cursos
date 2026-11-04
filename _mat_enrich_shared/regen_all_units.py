#!/usr/bin/env python3
"""Regenera SVG (paleta casa + margen) de TODAS las figuras de TODAS las
unidades eso_matematicas, saltando funciones_representacion (ya hecha).
Reanudable por cache por bundle. Argumento: presupuesto total de figuras por invocación."""
import json,os,sys,glob,importlib.util
SH=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('sv',os.path.join(SH,'svcgen.py'));sv=importlib.util.module_from_spec(spec);spec.loader.exec_module(sv)
budget=int(sys.argv[1]) if len(sys.argv)>1 else 20
SKIP={'eso_matematicas__mat_funciones_representacion.json'}
bundles=sorted(glob.glob('bundles/eso_matematicas__*.json'))
spent=0; summary=[]
for b in bundles:
    base=os.path.basename(b)
    if base in SKIP or '_backup' in b or b.endswith('.regen.json'): continue
    cache=b+'.regen.json'; done=json.load(open(cache)) if os.path.exists(cache) else {}
    d=json.load(open(b,encoding='utf-8'))
    assets=[]
    for lid,les in d.items():
        if not isinstance(les,dict):continue
        for sec,items in les.items():
            if isinstance(items,list):
                for it in items:
                    if isinstance(it,dict) and it.get('assets'):
                        for a in it['assets']:
                            if a.get('tikz'): assets.append(a)
    todo=[a for a in assets if a['id'] not in done]
    if not todo:
        summary.append((base,len(assets),len(done),0,[])); continue
    changed=False; fails=[]; n=0
    for a in assets:
        if a['id'] in done: a['svg']=done[a['id']]; continue
        if spent>=budget: break
        try: a['svg']=sv.gen(a['tikz']); done[a['id']]=a['svg']; changed=True; spent+=1; n+=1
        except SystemExit: fails.append(a['id'])
        if n%5==0: json.dump(done,open(cache,'w'))
    json.dump(done,open(cache,'w'))
    if changed:
        out=json.dumps(d,ensure_ascii=False,indent=2);json.loads(out);open(b,'w',encoding='utf-8').write(out)
    summary.append((base,len(assets),len(done),n,fails))
    if spent>=budget: break
for base,tot,dn,n,fails in summary:
    mark='' if dn<tot else ' ✔'
    print(f"{base.replace('eso_matematicas__','').replace('.json',''):32s} {dn}/{tot}{mark}"+(f" fails={fails}" if fails else ""))
print("gastado esta tanda:",spent)
