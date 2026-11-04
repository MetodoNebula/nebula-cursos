# -*- coding: utf-8 -*-
# Incremental/resumable TikZ->SVG compiler using the project builder pipeline.
import json,os,sys,importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("nebula_build",os.path.join(ROOT,"bundles","_fix_work","nebula_build.py"))
nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb)

def save(outp,res):
    tmp=outp+'.tmp'; json.dump(res,open(tmp,'w',encoding='utf-8'),ensure_ascii=False); os.replace(tmp,outp)

def main():
    figs=json.load(open(sys.argv[1],encoding='utf-8'))
    outp=sys.argv[2]
    res={}; errs={}
    if os.path.exists(outp):
        try: res=json.load(open(outp,encoding='utf-8'))
        except Exception: res={}
    d=os.path.join(HERE,'_latexwork'); os.makedirs(d,exist_ok=True)
    done=0
    for i,fig in enumerate(figs):
        if fig['id'] in res:   # resume: skip already compiled
            continue
        for fn in ('f.dvi','f.svg','f.aux','f.log'):
            try: os.remove(os.path.join(d,fn))
            except OSError: pass
        try:
            raw=nb.compile_svg(fig['tikz'],d)
            svg=nb.post(raw,fig['prefix'],fig.get('title',''))
            import xml.dom.minidom as m; m.parseString(svg)
            res[fig['id']]=svg
        except SystemExit as e:
            errs[fig['id']]=str(e)[:400]
        except Exception as e:
            errs[fig['id']]=('%s: %s'%(type(e).__name__,e))[:400]
        done+=1
        if done%15==0: save(outp,res); print('progress',len(res),'/',len(figs),flush=True)
    save(outp,res)
    json.dump(errs,open(outp+'.errs.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('DONE OK=%d FAIL=%d total=%d'%(len(res),len(errs),len(figs)))
    for k,v in list(errs.items())[:30]: print('FAIL',k,'::',v[:200])
main()
