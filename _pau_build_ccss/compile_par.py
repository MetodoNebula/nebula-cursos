# -*- coding: utf-8 -*-
# Parallel, resumable, time-budgeted TikZ->SVG compiler using the project builder.
import json,os,sys,time,importlib.util
from concurrent.futures import ProcessPoolExecutor, as_completed
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
def load_nb():
    spec=importlib.util.spec_from_file_location("nebula_build",os.path.join(ROOT,"bundles","_fix_work","nebula_build.py"))
    nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb); return nb

def work(args):
    fid,prefix,title,tikz,wid=args
    nb=load_nb()
    d=os.path.join(HERE,'_lw%d'%wid); os.makedirs(d,exist_ok=True)
    for fn in ('f.dvi','f.svg','f.aux','f.log'):
        try: os.remove(os.path.join(d,fn))
        except OSError: pass
    try:
        raw=nb.compile_svg(tikz,d)
        svg=nb.post(raw,prefix,title or '')
        import xml.dom.minidom as m; m.parseString(svg)
        return (fid, svg, None)
    except SystemExit as e: return (fid, None, str(e)[:400])
    except Exception as e: return (fid, None, '%s: %s'%(type(e).__name__,e)[:400])

def save(outp,res):
    tmp=outp+'.tmp'; json.dump(res,open(tmp,'w',encoding='utf-8'),ensure_ascii=False); os.replace(tmp,outp)

def main():
    figs=json.load(open(sys.argv[1],encoding='utf-8'))
    outp=sys.argv[2]
    budget=float(sys.argv[3]) if len(sys.argv)>3 else 100.0
    W=int(sys.argv[4]) if len(sys.argv)>4 else 4
    res={}; errs={}
    if os.path.exists(outp):
        try: res=json.load(open(outp,encoding='utf-8'))
        except Exception: res={}
    if os.path.exists(outp+'.errs.json'):
        try: errs=json.load(open(outp+'.errs.json',encoding='utf-8'))
        except Exception: errs={}
    todo=[f for f in figs if f['id'] not in res]
    t0=time.time(); done=0
    tasks=[(f['id'],f['prefix'],f.get('title',''),f['tikz'],i%W) for i,f in enumerate(todo)]
    with ProcessPoolExecutor(max_workers=W) as ex:
        futs={ex.submit(work,t):t[0] for t in tasks}
        for fut in as_completed(futs):
            fid,svg,err=fut.result()
            if svg is not None: res[fid]=svg
            else: errs[fid]=err
            done+=1
            if done%12==0:
                save(outp,res); print('progress',len(res),'/',len(figs),'(%.0fs)'%(time.time()-t0),flush=True)
            if time.time()-t0>budget:
                print('BUDGET reached, saving & exiting',flush=True); break
    save(outp,res)
    json.dump(errs,open(outp+'.errs.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('CHUNK OK=%d FAIL=%d total=%d remaining=%d'%(len(res),len(errs),len(figs),len(figs)-len(res)-len(errs)))
main()
