# -*- coding: utf-8 -*-
# Compilador por lotes TikZ->SVG reutilizando EXACTAMENTE la tuberia del builder
# del proyecto (bundles/_fix_work/nebula_build.py): PRE + compile_svg + post.
import json,os,sys,importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("nebula_build",os.path.join(ROOT,"bundles","_fix_work","nebula_build.py"))
nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb)

def main():
    figs=json.load(open(sys.argv[1],encoding='utf-8'))
    outp=sys.argv[2]
    d='/tmp/nbld_fis_%d'%os.getpid(); os.makedirs(d,exist_ok=True)
    res={}; errs={}
    for fig in figs:
        for fn in ('f.dvi','f.svg'):
            try: os.remove(os.path.join(d,fn))
            except OSError: pass
        try:
            raw=nb.compile_svg(fig['tikz'],d)
            svg=nb.post(raw,fig['prefix'],fig.get('title',''))
            import xml.dom.minidom as m; m.parseString(svg)
            res[fig['id']]=svg
        except SystemExit as e:
            errs[fig['id']]=str(e)[:300]
        except Exception as e:
            errs[fig['id']]=('%s: %s'%(type(e).__name__,e))[:300]
    # merge into existing output if present (so we can compile incrementally)
    if os.path.exists(outp) and len(sys.argv)>3 and sys.argv[3]=='merge':
        old=json.load(open(outp,encoding='utf-8')); old.update(res); res=old
    json.dump(res,open(outp,'w',encoding='utf-8'),ensure_ascii=False)
    print('OK=%d FAIL=%d'%(len([k for k in res]),len(errs)))
    for k,v in errs.items(): print('FAIL',k,'::',v[:200])
main()
