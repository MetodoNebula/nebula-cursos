#!/usr/bin/env python3
"""figrender.py <bundle.json> <outdir> [budget]
Renderiza TODAS las figuras (assets con 'tikz') de un bundle, pasa la puerta
de solapes texto-texto y genera PNG. Reanudable (salta ya hechas). Escribe
<outdir>/result.json y PNGs en <outdir>/png/."""
import json,os,re,subprocess,sys,shutil,importlib.util
SH=os.path.dirname(os.path.abspath(__file__))
def load_assets(bundle):
    d=json.load(open(bundle,encoding='utf-8')); out=[]
    for lid,les in d.items():
        if not isinstance(les,dict):continue
        for sec,items in les.items():
            if isinstance(items,list):
                for ii,it in enumerate(items):
                    if isinstance(it,dict) and it.get('assets'):
                        for ai,a in enumerate(it['assets']):
                            if a.get('tikz'): out.append(dict(lesson=lid,sec=sec,item=ii,ai=ai,id=a.get('id'),tikz=a['tikz']))
    return out
def main():
    bundle=sys.argv[1]; outdir=sys.argv[2]; budget=int(sys.argv[3]) if len(sys.argv)>3 else 999
    png=os.path.join(outdir,'png'); rend=os.path.join(outdir,'r'); os.makedirs(png,exist_ok=True); os.makedirs(rend,exist_ok=True)
    spec=importlib.util.spec_from_file_location('co',os.path.join(SH,'check_overlap.py'));co=importlib.util.module_from_spec(spec);spec.loader.exec_module(co)
    figs=load_assets(bundle)
    RES=os.path.join(outdir,'result.json')
    resd={r['id']:r for r in (json.load(open(RES)) if os.path.exists(RES) else [])}
    done={i for i,r in resd.items() if r.get('compiled')}
    DOC="\\documentclass[border=6pt]{standalone}\n\\input{%s/valid_preamble.tex}\n\\begin{document}\n%s\n\\end{document}\n"%( SH,'%s')
    def nm(f): return re.sub(r'[^A-Za-z0-9_]','_',(f['lesson'][:16]+'_'+str(f['id'])))
    n=0
    for f in figs:
        if f['id'] in done: continue
        if n>=budget: break
        n+=1; name=nm(f); d=os.path.join(rend,name); os.makedirs(d,exist_ok=True)
        shutil.copy(os.path.join(SH,'nebula_figures.tex'),os.path.join(d,'nebula_figures.tex'))
        open(os.path.join(d,'f.tex'),'w',encoding='utf-8').write(DOC%f['tikz'])
        r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','f.tex'],cwd=d,capture_output=True,text=True)
        ok=os.path.exists(os.path.join(d,'f.pdf'))
        rec=dict(id=f['id'],lesson=f['lesson'],sec=f['sec'],compiled=ok,overlaps=None,err=None,png=name+'-1.png')
        if not ok:
            mm=re.findall(r'^!.*',r.stdout,re.M); rec['err']=' | '.join(mm[:2]) or r.stdout[-200:]
        else:
            try: rec['overlaps']=co.audit(os.path.join(d,'f.pdf'))
            except Exception as e: rec['overlaps']='ERR:'+str(e)
            subprocess.run(['pdftoppm','-png','-r','150','f.pdf',os.path.join(png,name)],cwd=d,capture_output=True)
        resd[f['id']]=rec; json.dump(list(resd.values()),open(RES,'w'),ensure_ascii=False,indent=1)
    res=list(resd.values())
    nok=sum(1 for r in res if r['compiled']); fail=[r['id'] for r in res if not r['compiled']]
    ov=[r['id'] for r in res if isinstance(r['overlaps'],dict) and r['overlaps'].get('verdict')=='OVERLAP']
    print('procesadas %d/%d | compiladas %d | fallos %s | overlaps_auto %s'%(len(res),len(figs),nok,fail,ov))
if __name__=='__main__': main()
