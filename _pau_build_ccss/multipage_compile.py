# -*- coding: utf-8 -*-
# Fast multipage TikZ->SVG: one latex run per batch (standalone multi=tikzpicture),
# then dvisvgm per page. Reuses project builder PRE + post(). Resumable, incremental.
import json,os,sys,subprocess,re,importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("nebula_build",os.path.join(ROOT,"bundles","_fix_work","nebula_build.py"))
nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb)
PRE_MULTI=nb.PRE.replace("[tikz,border=14pt]{standalone}","[tikz,border=14pt,multi=tikzpicture]{standalone}")

def save(outp,res):
    tmp=outp+'.tmp'; json.dump(res,open(tmp,'w',encoding='utf-8'),ensure_ascii=False); os.replace(tmp,outp)

def compile_batch(batch, d):
    for f in os.listdir(d):
        if f.startswith('m.') or re.match(r'm-\d+\.svg',f):
            try: os.remove(os.path.join(d,f))
            except OSError: pass
    tex=PRE_MULTI + "\n".join(b['tikz'] for b in batch) + "\n\\end{document}\n"
    open(os.path.join(d,'m.tex'),'w',encoding='utf-8').write(tex)
    subprocess.run(['latex','-interaction=nonstopmode','-halt-on-error','m.tex'],cwd=d,capture_output=True,text=True)
    if not os.path.exists(os.path.join(d,'m.dvi')):
        return None  # batch failed (caller will fall back to per-fig)
    subprocess.run(['dvisvgm','--no-fonts=0','-p1-','-o','m-%p.svg','m.dvi'],cwd=d,capture_output=True,text=True)
    out={}
    for i,b in enumerate(batch,1):
        p=os.path.join(d,'m-%d.svg'%i)
        if not os.path.exists(p): return None  # page count mismatch -> fallback
        raw=open(p,encoding='utf-8').read()
        try:
            svg=nb.post(raw, b['prefix'], b.get('title',''))
            import xml.dom.minidom as m; m.parseString(svg)
            out[b['id']]=svg
        except Exception as e:
            out[b['id']]=('__ERR__%s: %s'%(type(e).__name__,e))[:300]
    return out

def main():
    figs=json.load(open(sys.argv[1],encoding='utf-8'))
    outp=sys.argv[2]
    bs=int(sys.argv[3]) if len(sys.argv)>3 else 25
    res={}; errs={}
    if os.path.exists(outp):
        try: res=json.load(open(outp,encoding='utf-8'))
        except Exception: res={}
    if os.path.exists(outp+'.errs.json'):
        try: errs=json.load(open(outp+'.errs.json',encoding='utf-8'))
        except Exception: errs={}
    todo=[f for f in figs if f['id'] not in res and f['id'] not in errs]
    d=os.path.join(HERE,'_mpwork'); os.makedirs(d,exist_ok=True)
    i=0
    while i<len(todo):
        batch=todo[i:i+bs]; i+=bs
        out=compile_batch(batch,d)
        if out is None:
            # fallback: compile each individually to isolate the bad one
            for b in batch:
                o=compile_batch([b],d)
                if o is None: errs[b['id']]='latex batch/single fail'
                else:
                    for k,v in o.items():
                        if isinstance(v,str) and v.startswith('__ERR__'): errs[k]=v[7:]
                        else: res[k]=v
        else:
            for k,v in out.items():
                if isinstance(v,str) and v.startswith('__ERR__'): errs[k]=v[7:]
                else: res[k]=v
        save(outp,res); print('progress',len(res),'ok /',len(errs),'err /',len(figs),'total',flush=True)
    json.dump(errs,open(outp+'.errs.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('DONE OK=%d FAIL=%d'%(len(res),len(errs)))
    for k,v in list(errs.items())[:20]: print('FAIL',k,'::',str(v)[:160])
main()
