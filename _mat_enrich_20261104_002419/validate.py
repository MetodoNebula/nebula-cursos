import json,os,re,subprocess,sys,shutil,importlib.util
WORK=os.path.abspath(os.path.dirname(__file__))
figs=json.load(open(os.path.join(WORK,'pilot_figs.json')))
OUT=os.path.join(WORK,'render'); PNG=os.path.join(WORK,'png')
os.makedirs(OUT,exist_ok=True); os.makedirs(PNG,exist_ok=True)
spec=importlib.util.spec_from_file_location('co',os.path.join(WORK,'check_overlap.py'))
co=importlib.util.module_from_spec(spec); spec.loader.exec_module(co)
RES=os.path.join(WORK,'validate_result.json')
res=json.load(open(RES)) if os.path.exists(RES) else []
done={r['id'] for r in res}
DOC=r"""\documentclass[border=6pt]{standalone}
\input{%s/valid_preamble.tex}
\begin{document}
%s
\end{document}
"""
def nm(f): return re.sub(r'[^A-Za-z0-9_]','_',(f['lesson'][:18]+'_'+str(f['id'])))
budget=int(sys.argv[1]) if len(sys.argv)>1 else 999
n=0
for f in figs:
    if f['id'] in done: continue
    if n>=budget: break
    n+=1
    name=nm(f); d=os.path.join(OUT,name); os.makedirs(d,exist_ok=True)
    shutil.copy(os.path.join(WORK,'nebula_figures.tex'),os.path.join(d,'nebula_figures.tex'))
    open(os.path.join(d,'f.tex'),'w',encoding='utf-8').write(DOC%(WORK,f['tikz']))
    r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','f.tex'],cwd=d,capture_output=True,text=True)
    ok=os.path.exists(os.path.join(d,'f.pdf'))
    rec=dict(id=f['id'],lesson=f['lesson'],sec=f['sec'],compiled=ok,overlaps=None,err=None,png=name+'-1.png')
    if not ok:
        m=re.findall(r'^!.*',r.stdout,re.M); rec['err']=' | '.join(m[:3]) or r.stdout[-300:]
    else:
        try: rec['overlaps']=co.audit(os.path.join(d,'f.pdf'))
        except Exception as e: rec['overlaps']='ERR:'+str(e)
        subprocess.run(['pdftoppm','-png','-r','150','f.pdf',os.path.join(PNG,name)],cwd=d,capture_output=True)
    res.append(rec); json.dump(res,open(RES,'w'),ensure_ascii=False,indent=1)
nok=sum(1 for r in res if r['compiled'])
print('total procesadas %d/%d | compiladas %d'%(len(res),len(figs),nok))
print('fallos:',[r['id'] for r in res if not r['compiled']])
