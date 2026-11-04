#!/usr/bin/env python3
"""injfig.py <bundle.json> <fixes.json>
fixes.json = { "<asset_id>": "<tikz nuevo>", ... }
Regenera el SVG de producción desde el TikZ nuevo (svcgen.gen) e inyecta
tikz+svg en el asset correspondiente del bundle (cualquier sección)."""
import json,sys,os,importlib.util
SH=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('svcgen',os.path.join(SH,'svcgen.py'));sv=importlib.util.module_from_spec(spec);spec.loader.exec_module(sv)
def main():
    bundle,fx=sys.argv[1],sys.argv[2]
    fixes=json.load(open(fx,encoding='utf-8'))
    d=json.load(open(bundle,encoding='utf-8'))
    done=set()
    for lid,les in d.items():
        if not isinstance(les,dict):continue
        for sec,items in les.items():
            if isinstance(items,list):
                for it in items:
                    if isinstance(it,dict) and it.get('assets'):
                        for a in it['assets']:
                            if a.get('id') in fixes:
                                tikz=fixes[a['id']]
                                a['tikz']=tikz; a['svg']=sv.gen(tikz); done.add(a['id'])
                                print('inyectado',a['id'],'svg',len(a['svg']),'bytes')
    missing=set(fixes)-done
    if missing: print('NO ENCONTRADOS:',missing); sys.exit(1)
    out=json.dumps(d,ensure_ascii=False,indent=2); json.loads(out)
    open(bundle,'w',encoding='utf-8').write(out)
    print('OK, figuras inyectadas:',len(done))
if __name__=='__main__': main()
