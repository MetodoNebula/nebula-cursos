# -*- coding: utf-8 -*-
# Compilador por lotes TikZ->SVG usando EXACTAMENTE la tuberia del builder del proyecto.
import json,os,subprocess,re,math,sys
PRE=r"""\documentclass[tikz,border=14pt]{standalone}
\usepackage{lmodern}\usepackage{amsmath}\usepackage{amssymb}\usepackage{tikz}\usepackage{pgfplots}\pgfplotsset{compat=1.17}
\usetikzlibrary{calc,arrows.meta,positioning,patterns,decorations.markings,angles,quotes}
\definecolor{NebulaNavy}{HTML}{0B1F3A}
\definecolor{NebulaError}{HTML}{7952A3}
\definecolor{NebulaCheck}{HTML}{2E7D5B}
\definecolor{NebulaAmber}{HTML}{B47916}
\definecolor{NebulaGold}{HTML}{B77916}
\definecolor{NebulaLight}{HTML}{E4EAF0}
\definecolor{NebulaMuted}{HTML}{6E7E90}
\definecolor{NebulaBG}{HTML}{F6F8FB}
\definecolor{NebulaSoft}{HTML}{E4EAF0}
\tikzset{
 nbline/.style={NebulaNavy,thick},
 nbdash/.style={NebulaNavy,thick,dashed},
 nbmass/.style={NebulaNavy},
 nbvec/.style={NebulaError,very thick,-{Stealth[length=2mm]}},
 nbvecb/.style={NebulaCheck,very thick,-{Stealth[length=2mm]}},
 nbaxis/.style={NebulaNavy,thick,-{Stealth[length=2mm]}},
}
\tikzset{nblabel/.style={NebulaNavy}}
\begin{document}
"""
def compile_svg(tikz, d):
    tex=PRE+tikz+"\n\\end{document}\n"
    open(os.path.join(d,'f.tex'),'w').write(tex)
    for fn in ('f.dvi','f.svg'):
        try: os.remove(os.path.join(d,fn))
        except OSError: pass
    subprocess.run(['latex','-interaction=nonstopmode','-halt-on-error','f.tex'],cwd=d,capture_output=True,text=True)
    if not os.path.exists(os.path.join(d,'f.dvi')):
        log=open(os.path.join(d,'f.log'),encoding='utf-8',errors='ignore').read()
        err=re.search(r'\n! .*(?:\n.*){0,6}',log)
        return None, ('LATEX FAIL: '+(err.group(0)[:500] if err else log[-500:]))
    r=subprocess.run(['dvisvgm','--no-fonts=0','f.dvi','-o','f.svg'],cwd=d,capture_output=True,text=True)
    if not os.path.exists(os.path.join(d,'f.svg')):
        return None, ('DVISVGM FAIL: '+r.stderr[-400:])
    return open(os.path.join(d,'f.svg'),encoding='utf-8').read(), None
def post(raw, prefix_num, title):
    svg=raw[raw.index('<svg'):].replace("'",'"')
    vb=re.search(r'viewBox="([^"]+)"',svg).group(1)
    x0,y0,w,h=[float(v) for v in vb.split()]
    PFX='nebula-%s-'%prefix_num
    ids=set(re.findall(r'\bid="([^"]+)"',svg))
    svg=re.sub(r'\bid="([^"]+)"',lambda m:'id="%s%s"'%(PFX,m.group(1)),svg)
    for i in sorted(ids,key=len,reverse=True):
        svg=svg.replace('"#%s"'%i,'"#%s%s"'%(PFX,i))
    M=14.0
    nx0=x0-M; ny0=y0-M; nw=w+2*M; nh=h+2*M
    W=math.ceil(nw); H=math.ceil(nh)
    nvb="%g %g %s %s"%(nx0,ny0,nw,nh)
    newroot=('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
             'width="%d" height="%d" viewBox="%s" fill="#0b1f3a" role="img" data-nebula-svg="2026-10">'%(W,H,nvb))
    svg=re.sub(r'<svg[^>]*>',newroot,svg,count=1)
    bg='<rect x="%g" y="%g" width="%s" height="%s" fill="#f6f8fb" data-nebula-background="true"/>'%(nx0,ny0,nw,nh)
    ttl='<title>%s</title>'%title if title else ''
    svg=svg.replace(newroot,newroot+bg+ttl,1)
    return svg.strip()
if __name__=='__main__':
    spec=json.load(open(sys.argv[1],encoding='utf-8'))
    outp=sys.argv[2]
    d='/tmp/nbld_pau'; os.makedirs(d,exist_ok=True)
    res={}; errs={}
    for fig in spec:
        raw,err=compile_svg(fig['tikz'],d)
        if err:
            errs[fig['id']]=err; continue
        try:
            res[fig['id']]=post(raw, fig['prefix'], fig.get('title',''))
            import xml.dom.minidom as m; m.parseString(res[fig['id']])
        except Exception as e:
            errs[fig['id']]='POST/XML: '+str(e)
    json.dump(res,open(outp,'w',encoding='utf-8'),ensure_ascii=False)
    print('OK=%d FAIL=%d'%(len(res),len(errs)))
    for k,v in errs.items(): print('FAIL',k,v[:200])
