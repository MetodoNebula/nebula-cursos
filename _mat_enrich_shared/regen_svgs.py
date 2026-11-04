#!/usr/bin/env python3
"""regen_svgs.py <bundle.json> [budget]
Regenera el SVG de producción (paleta casa + margen amplio) desde el TikZ de
CADA figura del bundle y lo reinyecta. Reanudable vía cache <bundle>.regen.json."""
import json,os,sys,importlib.util
SH=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('sv',os.path.join(SH,'svcgen.py'));sv=importlib.util.module_from_spec(spec);spec.loader.exec_module(sv)
def main():
    bundle=sys.argv[1]; budget=int(sys.argv[2]) if len(sys.argv)>2 else 999
    cache=bundle+'.regen.json'
    done=json.load(open(cache)) if os.path.exists(cache) else {}
    d=json.load(open(bundle,encoding='utf-8'))
    assets=[]
    for lid,les in d.items():
        if not isinstance(les,dict):continue
        for sec,items in les.items():
            if isinstance(items,list):
                for it in items:
                    if isinstance(it,dict) and it.get('assets'):
                        for a in it['assets']:
                            if a.get('tikz'): assets.append(a)
    n=0;fail=[]
    for a in assets:
        i=a['id']
        if i in done: a['svg']=done[i]; continue
        if n>=budget: break
        n+=1
        try: svg=sv.gen(a['tikz']); a['svg']=svg; done[i]=svg
        except SystemExit as e: fail.append(i)
        if n%6==0: json.dump(done,open(cache,'w'))
    json.dump(done,open(cache,'w'))
    out=json.dumps(d,ensure_ascii=False,indent=2);json.loads(out);open(bundle,'w',encoding='utf-8').write(out)
    print('total figuras %d | regeneradas acumuladas %d | fallos %s'%(len(assets),len(done),fail))
if __name__=='__main__': main()
