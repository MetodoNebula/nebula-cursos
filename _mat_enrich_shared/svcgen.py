import os,re,subprocess,tempfile,sys,shutil
WORK=os.path.dirname(os.path.abspath(__file__))
REMAP={'#b23a48':'#7952a3','#c9a646':'#b77916','#eef3f8':'#e4eaf0'}
DOC="\\documentclass[border=6pt]{standalone}\n\\input{%s/valid_preamble.tex}\n\\begin{document}\n%s\n\\end{document}\n"
def gen(tikz,M=18.0):
    d=tempfile.mkdtemp()
    shutil.copy(os.path.join(WORK,'nebula_figures.tex'),os.path.join(d,'nebula_figures.tex'))
    open(os.path.join(d,'f.tex'),'w',encoding='utf-8').write(DOC%(WORK,tikz))
    r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','f.tex'],cwd=d,capture_output=True,text=True)
    if not os.path.exists(os.path.join(d,'f.pdf')):
        raise SystemExit('pdflatex failed\n'+r.stdout[-1200:])
    subprocess.run(['dvisvgm','--pdf','--no-fonts','--exact-bbox','f.pdf','-o','f_raw.svg'],cwd=d,capture_output=True,text=True,check=True)
    raw=open(os.path.join(d,'f_raw.svg'),encoding='utf-8').read()
    for k,v in REMAP.items(): raw=raw.replace(k,v).replace(k.upper(),v)
    raw=re.sub(r"<\?xml[^>]*\?>\s*","",raw); raw=re.sub(r"<!--.*?-->\s*","",raw,flags=re.S)
    m=re.search(r"viewBox='([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)'",raw)
    x,y,w,h=[float(v) for v in m.groups()]
    nx,ny,nw,nh=x-M,y-M,w+2*M,h+2*M
    root=("<svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' "
          "viewBox='%.3f %.3f %.3f %.3f' fill='#0b1f3a' role='img' data-nebula-fig='cool'>"
          "<rect x='%.3f' y='%.3f' width='%.3f' height='%.3f' fill='#f6f8fb' data-nebula-background='true'/>"%(nx,ny,nw,nh,nx,ny,nw,nh))
    raw=re.sub(r"<svg[^>]*>",root,raw,count=1)
    shutil.rmtree(d,ignore_errors=True)
    return raw
if __name__=='__main__':
    import json
    fixes=json.load(open(os.path.join(WORK,'fix','fixes.json')))
    out={}
    for fid,tikz in fixes.items():
        svg=gen(tikz); out[fid]=svg
        print(fid,'svg bytes',len(svg),'| colores',sorted(set(re.findall(r'#[0-9a-f]{6}',svg))))
    json.dump(out,open(os.path.join(WORK,'fix','svgs.json'),'w'),ensure_ascii=False)
    print('OK svgs.json')
