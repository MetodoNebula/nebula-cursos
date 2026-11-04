# -*- coding: utf-8 -*-
# Compila figuras de GRAFICA con la tuberia del proyecto PERO con los recuadros de
# las etiquetas de los ejes en color de tarjeta (#f6f8fb) en vez de blanco, para que
# no se vean "cuadros blancos" sobre el fondo claro.
import json,os,sys,importlib.util,re
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("nebula_build",os.path.join(ROOT,"bundles","_fix_work","nebula_build.py"))
nb=importlib.util.module_from_spec(spec); spec.loader.exec_module(nb)
# PRE con fill=white -> fill=NebulaBG (afecta xticklabel/yticklabel del macro \nbfuncplotlab)
PRE_PATCHED=nb.PRE.replace('fill=white','fill=NebulaBG')
def compile_svg(tikz,d):
    tex=PRE_PATCHED+tikz+"\n\\end{document}\n"
    open(os.path.join(d,'f.tex'),'w').write(tex)
    import subprocess
    subprocess.run(['latex','-interaction=nonstopmode','-halt-on-error','f.tex'],cwd=d,capture_output=True,text=True)
    if not os.path.exists(os.path.join(d,'f.dvi')):
        log=open(os.path.join(d,'f.log'),encoding='utf-8',errors='ignore').read()
        err=re.search(r'\n! .*(?:\n.*){0,4}',log); raise SystemExit('LATEX FAIL: '+(err.group(0)[:400] if err else log[-400:]))
    subprocess.run(['dvisvgm','--no-fonts=0','f.dvi','-o','f.svg'],cwd=d,capture_output=True,text=True)
    return open(os.path.join(d,'f.svg'),encoding='utf-8').read()
def main():
    figs=json.load(open(sys.argv[1],encoding='utf-8')); outp=sys.argv[2]
    d='/tmp/nbld_gr_%d'%os.getpid(); os.makedirs(d,exist_ok=True)
    res={}; errs={}
    for fig in figs:
        for fn in ('f.dvi','f.svg'):
            try: os.remove(os.path.join(d,fn))
            except OSError: pass
        tikz=fig['tikz'].replace('fill=white','fill=NebulaBG')  # tambien en el cuerpo
        try:
            svg=nb.post(compile_svg(tikz,d),fig['prefix'],fig.get('title',''))
            import xml.dom.minidom as m; m.parseString(svg); res[fig['id']]=svg
        except Exception as e: errs[fig['id']]=str(e)[:200]
    json.dump(res,open(outp,'w',encoding='utf-8'),ensure_ascii=False)
    print('OK=%d FAIL=%d'%(len(res),len(errs)))
    for k,v in errs.items(): print('FAIL',k,v[:150])
main()
