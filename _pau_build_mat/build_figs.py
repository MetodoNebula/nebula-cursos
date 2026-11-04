#!/usr/bin/env python3
"""Device-side figure compiler. Imports the project's nebula_build (untouched),
augments its in-memory preamble to load fillbetween + 3d libs, then compiles each
spec {prefix,title,tikz} to a namespaced SVG. Per-figure error isolation.
Usage: python3 build_figs.py specs.json out_svg_dir [report.json]
"""
import json, os, sys, importlib.util

HERE=os.path.dirname(os.path.abspath(__file__))
WEB=os.path.abspath(os.path.join(HERE,'..'))  # Nebula_Cursos_Web
NB=os.path.join(WEB,'bundles','_fix_work','nebula_build.py')
spec=importlib.util.spec_from_file_location('nebula_build',NB)
nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb)

# augment preamble: add fillbetween + 3d libraries just before \begin{document}
EXTRA=("\\usepgfplotslibrary{fillbetween}\n"
       "\\usetikzlibrary{backgrounds,3d,calc,intersections}\n")
nb.PRE = nb.PRE.replace("\\begin{document}", EXTRA+"\\begin{document}")

def main():
    specs=json.load(open(sys.argv[1],encoding='utf-8'))
    outdir=sys.argv[2]; os.makedirs(outdir,exist_ok=True)
    report=[]; d='/tmp/nbld_pau'; os.makedirs(d,exist_ok=True)
    import re
    for s in specs:
        pfx=s['prefix']
        for fn in ('f.dvi','f.svg'):
            try: os.remove(os.path.join(d,fn))
            except OSError: pass
        try:
            raw=nb.compile_svg(s['tikz'], d)
            svg=nb.post(raw, pfx, s.get('title',''))
            import xml.dom.minidom as m; m.parseString(svg)
            open(os.path.join(outdir,pfx+'.svg'),'w',encoding='utf-8').write(svg)
            report.append({'prefix':pfx,'ok':True,'len':len(svg)})
        except SystemExit as e:
            report.append({'prefix':pfx,'ok':False,'err':str(e)[:300]})
        except Exception as e:
            report.append({'prefix':pfx,'ok':False,'err':repr(e)[:300]})
    ok=sum(1 for r in report if r['ok'])
    print(f'compiled {ok}/{len(report)} OK')
    for r in report:
        if not r['ok']: print('  FAIL',r['prefix'],'::',r.get('err'))
    if len(sys.argv)>3: json.dump(report,open(sys.argv[3],'w'),ensure_ascii=False,indent=1)

if __name__=='__main__': main()
