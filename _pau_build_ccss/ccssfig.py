# -*- coding: utf-8 -*-
"""CCSS figure generators -> TikZ strings compatible with the project builder
(bundles/_fix_work/nebula_build.py preamble: NebulaNavy/Error/Check/Amber/Gold/
Muted/BG, pgfplots compat=1.17, macro \\nbfuncplotlab).

Palette intent: navy lines/axes, teal (Check) fills/secondary, amber/gold accents,
dark text on light card. Keep each figure <= ~520x300 px. Avoid text overlaps by
placing labels with explicit anchors and small fonts.

Every generator returns a TikZ body (no preamble, no \\begin{document})."""

NAVY="NebulaNavy"; TEAL="NebulaCheck"; AMBER="NebulaAmber"; GOLD="NebulaGold"
PURPLE="NebulaError"; MUTED="NebulaMuted"

def _fmt(v):
    s=("%g"%v)
    return s

# ---------------------------------------------------------------------------
def func_plot(exprs, xmin,xmax,ymin,ymax, xtick=1,ytick=1, width=11.0,height=6.6,
              vasymptotes=None, hasymptotes=None, points=None, tangents=None,
              xlabel="x", ylabel="y", samples=200):
    """exprs: list of dicts {expr(pgf, var x), color, domain:(a,b), legend, dashed}
    vasymptotes: list of x values (dashed vertical). hasymptotes: list of y values.
    points: list {x,y,label,anchor}. tangents: list {expr,domain,color}."""
    vasymptotes=vasymptotes or []; hasymptotes=hasymptotes or []
    points=points or []; tangents=tangents or []
    yzero=(0-ymin)/((ymax-ymin)) if ymax!=ymin else 0.5
    L=[]
    L.append(r"\begin{tikzpicture}")
    L.append(r"\begin{axis}[")
    L.append(f"  width={width}cm, height={height}cm, axis lines=middle,")
    L.append(f"  axis line style={{{NAVY},-{{Stealth[length=2mm]}}}},")
    L.append(f"  xmin={_fmt(xmin)}, xmax={_fmt(xmax)}, ymin={_fmt(ymin)}, ymax={_fmt(ymax)},")
    L.append(f"  xlabel={{${xlabel}$}}, ylabel={{${ylabel}$}},")
    L.append(f"  xlabel style={{at={{(axis description cs:1.0,{yzero:.3f})}},anchor=west,font=\\small}},")
    L.append(r"  ylabel style={at={(axis description cs:0.0,1.0)},anchor=south,font=\small},")
    L.append(f"  xtick distance={_fmt(xtick)}, ytick distance={_fmt(ytick)},")
    L.append(r"  xticklabel style={font=\footnotesize,anchor=north,fill=NebulaBG,inner sep=1.4pt},")
    L.append(r"  yticklabel style={font=\footnotesize,anchor=east,fill=NebulaBG,inner sep=1.4pt},")
    L.append(f"  grid=both, grid style={{{MUTED}!40,very thin}}, tick style={{{NAVY}}}, clip=false,")
    L.append(r"  legend style={font=\footnotesize,draw=NebulaMuted,fill=NebulaBG,at={(0.98,0.03)},anchor=south east},")
    L.append(r"]")
    # vertical asymptotes
    for xa in vasymptotes:
        L.append(f"\\addplot[{MUTED},dashed,thick] coordinates {{({_fmt(xa)},{_fmt(ymin)}) ({_fmt(xa)},{_fmt(ymax)})}};")
    for ya in hasymptotes:
        L.append(f"\\addplot[{MUTED},dashed,thick] coordinates {{({_fmt(xmin)},{_fmt(ya)}) ({_fmt(xmax)},{_fmt(ya)})}};")
    legends=[]
    for e in exprs:
        col=e.get("color",NAVY); dom=e.get("domain",(xmin,xmax))
        dash=",dashed" if e.get("dashed") else ""
        L.append(f"\\addplot[{col},very thick{dash},smooth,samples={samples},domain={_fmt(dom[0])}:{_fmt(dom[1])}] {{{e['expr']}}};")
        legends.append(e.get("legend",""))
    for t in tangents:
        dom=t.get("domain",(xmin,xmax)); col=t.get("color",AMBER)
        L.append(f"\\addplot[{col},thick,dashed,domain={_fmt(dom[0])}:{_fmt(dom[1])}] {{{t['expr']}}};")
        legends.append(t.get("legend",""))
    for p in points:
        an=p.get("anchor","north west")
        L.append(f"\\addplot[only marks,mark=*,{NAVY},mark size=1.8pt] coordinates {{({_fmt(p['x'])},{_fmt(p['y'])})}};")
        if p.get("label"):
            L.append(f"\\node[font=\\footnotesize,{NAVY},anchor={an},fill=NebulaBG,inner sep=1pt] at (axis cs:{_fmt(p['x'])},{_fmt(p['y'])}) {{{p['label']}}};")
    if any(legends):
        L.append(r"\legend{"+",".join(legends)+"}")
    L.append(r"\end{axis}")
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)

# ---------------------------------------------------------------------------
def feasible_region(constraints, vertices, xmin,xmax,ymin,ymax, xtick=1,ytick=1,
                    obj=None, width=10.4,height=6.6, xlabel="x", ylabel="y", feas_poly=None):
    """constraints: list {a,b,c,op,label} meaning a*x+b*y (<=/>=) c, drawn as line a x+b y=c.
    vertices: list {x,y,label,anchor}. feas_poly: ordered list of (x,y) to shade (the feasible polygon).
    obj: {expr_label, dir:(dx,dy), at:(x,y)} optional gradient arrow of objective."""
    yzero=(0-ymin)/((ymax-ymin)) if ymax!=ymin else 0.5
    L=[r"\begin{tikzpicture}", r"\begin{axis}["]
    L.append(f"  width={width}cm, height={height}cm, axis lines=middle,")
    L.append(f"  axis line style={{{NAVY},-{{Stealth[length=2mm]}}}},")
    L.append(f"  xmin={_fmt(xmin)}, xmax={_fmt(xmax)}, ymin={_fmt(ymin)}, ymax={_fmt(ymax)},")
    L.append(f"  xlabel={{${xlabel}$}}, ylabel={{${ylabel}$}},")
    L.append(f"  xlabel style={{at={{(axis description cs:1.0,{yzero:.3f})}},anchor=west,font=\\small}},")
    L.append(r"  ylabel style={at={(axis description cs:0.0,1.0)},anchor=south,font=\small},")
    L.append(f"  xtick distance={_fmt(xtick)}, ytick distance={_fmt(ytick)},")
    L.append(r"  xticklabel style={font=\footnotesize,anchor=north,fill=NebulaBG,inner sep=1.4pt},")
    L.append(r"  yticklabel style={font=\footnotesize,anchor=east,fill=NebulaBG,inner sep=1.4pt},")
    L.append(f"  grid=both, grid style={{{MUTED}!40,very thin}}, tick style={{{NAVY}}}, clip=false,")
    L.append(r"]")
    # shaded feasible polygon first (under lines)
    if feas_poly:
        coords=" ".join(f"({_fmt(x)},{_fmt(y)})" for x,y in feas_poly)
        L.append(f"\\addplot[fill={TEAL}!22,draw={TEAL},thick] coordinates {{{coords}}} -- cycle;")
    # constraint lines
    for c in constraints:
        a,b,cc=c["a"],c["b"],c["c"]; col=c.get("color",NAVY)
        # compute two endpoints across the view
        pts=[]
        if b!=0:
            for xv in (xmin,xmax):
                yv=(cc-a*xv)/b; pts.append((xv,yv))
        else:
            xv=cc/a; pts=[(xv,ymin),(xv,ymax)]
        L.append(f"\\addplot[{col},thick] coordinates {{({_fmt(pts[0][0])},{_fmt(pts[0][1])}) ({_fmt(pts[1][0])},{_fmt(pts[1][1])})}};"
                 + (f"  %{c.get('label','')}" if c.get('label') else ""))
    # objective gradient arrow
    if obj and obj.get("dir"):
        x0,y0=obj.get("at",((xmin+xmax)/2,(ymin+ymax)/2)); dx,dy=obj["dir"]
        L.append(f"\\draw[{AMBER},very thick,-{{Stealth[length=2.4mm]}}] (axis cs:{_fmt(x0)},{_fmt(y0)}) -- (axis cs:{_fmt(x0+dx)},{_fmt(y0+dy)});")
        if obj.get("label"):
            L.append(f"\\node[font=\\footnotesize,{AMBER},anchor=south west] at (axis cs:{_fmt(x0+dx)},{_fmt(y0+dy)}) {{{obj['label']}}};")
    # vertices
    for v in vertices:
        an=v.get("anchor","north east")
        L.append(f"\\addplot[only marks,mark=*,{NAVY},mark size=2pt] coordinates {{({_fmt(v['x'])},{_fmt(v['y'])})}};")
        if v.get("label"):
            L.append(f"\\node[font=\\footnotesize,{NAVY},anchor={an},fill=NebulaBG,inner sep=1.2pt] at (axis cs:{_fmt(v['x'])},{_fmt(v['y'])}) {{{v['label']}}};")
    L += [r"\end{axis}", r"\end{tikzpicture}"]
    return "\n".join(L)

# ---------------------------------------------------------------------------
def shaded_area(exprs, a, b, xmin,xmax,ymin,ymax, xtick=1,ytick=1, width=11.0,height=6.4,
                fill_between=None, xlabel="x", ylabel="y", samples=200, label=None, points=None):
    """exprs: list {expr,color,legend}. Shade region of first expr down to y=0 between a,b,
    OR fill between exprs[0] and exprs[1] if fill_between=('0','1')."""
    yzero=(0-ymin)/((ymax-ymin)) if ymax!=ymin else 0.5
    points=points or []
    L=[r"\begin{tikzpicture}", r"\begin{axis}["]
    L.append(f"  width={width}cm, height={height}cm, axis lines=middle,")
    L.append(f"  axis line style={{{NAVY},-{{Stealth[length=2mm]}}}},")
    L.append(f"  xmin={_fmt(xmin)}, xmax={_fmt(xmax)}, ymin={_fmt(ymin)}, ymax={_fmt(ymax)},")
    L.append(f"  xlabel={{${xlabel}$}}, ylabel={{${ylabel}$}},")
    L.append(f"  xlabel style={{at={{(axis description cs:1.0,{yzero:.3f})}},anchor=west,font=\\small}},")
    L.append(r"  ylabel style={at={(axis description cs:0.0,1.0)},anchor=south,font=\small},")
    L.append(f"  xtick distance={_fmt(xtick)}, ytick distance={_fmt(ytick)},")
    L.append(r"  xticklabel style={font=\footnotesize,anchor=north,fill=NebulaBG,inner sep=1.4pt},")
    L.append(r"  yticklabel style={font=\footnotesize,anchor=east,fill=NebulaBG,inner sep=1.4pt},")
    L.append(f"  grid=both, grid style={{{MUTED}!40,very thin}}, tick style={{{NAVY}}}, clip=false,")
    L.append(r"  legend style={font=\footnotesize,draw=NebulaMuted,fill=NebulaBG,at={(0.98,0.97)},anchor=north east},")
    L.append(r"]")
    legends=[]
    # shading
    e0=exprs[0]
    L.append(f"\\addplot[draw=none,fill={TEAL}!22,domain={_fmt(a)}:{_fmt(b)},samples={samples}] {{{e0['expr']}}} \\closedcycle;")
    if fill_between and len(exprs)>=2:
        # approximate fill between by shading expr0 region minus expr1 is complex; draw both and shade e0 to e1
        L.append(f"\\addplot[draw=none,fill=NebulaBG,domain={_fmt(a)}:{_fmt(b)},samples={samples}] {{{exprs[1]['expr']}}} \\closedcycle;")
    for e in exprs:
        col=e.get("color",NAVY)
        L.append(f"\\addplot[{col},very thick,smooth,samples={samples},domain={_fmt(xmin)}:{_fmt(xmax)}] {{{e['expr']}}};")
        legends.append(e.get("legend",""))
    for p in points:
        an=p.get("anchor","north")
        L.append(f"\\addplot[only marks,mark=*,{NAVY},mark size=1.6pt] coordinates {{({_fmt(p['x'])},{_fmt(p['y'])})}};")
        if p.get("label"):
            L.append(f"\\node[font=\\footnotesize,{NAVY},anchor={an},fill=NebulaBG,inner sep=1pt] at (axis cs:{_fmt(p['x'])},{_fmt(p['y'])}) {{{p['label']}}};")
    if any(legends): L.append(r"\legend{"+",".join(legends)+"}")
    L += [r"\end{axis}", r"\end{tikzpicture}"]
    return "\n".join(L)

# ---------------------------------------------------------------------------
def scatter_regression(pts, reg, xmin,xmax,ymin,ymax, xtick=1,ytick=1, width=10.6,height=6.6,
                       xlabel="x", ylabel="y"):
    """pts: list (x,y). reg: {slope,intercept,legend}. Draw cloud + regression line."""
    L=[r"\begin{tikzpicture}", r"\begin{axis}["]
    L.append(f"  width={width}cm, height={height}cm, axis lines=left,")
    L.append(f"  axis line style={{{NAVY}}},")
    L.append(f"  xmin={_fmt(xmin)}, xmax={_fmt(xmax)}, ymin={_fmt(ymin)}, ymax={_fmt(ymax)},")
    L.append(f"  xlabel={{${xlabel}$}}, ylabel={{${ylabel}$}},")
    L.append(r"  xlabel style={font=\small}, ylabel style={font=\small},")
    L.append(f"  xtick distance={_fmt(xtick)}, ytick distance={_fmt(ytick)},")
    L.append(r"  xticklabel style={font=\footnotesize}, yticklabel style={font=\footnotesize},")
    L.append(f"  grid=both, grid style={{{MUTED}!40,very thin}}, tick style={{{NAVY}}},")
    L.append(r"  legend style={font=\footnotesize,draw=NebulaMuted,fill=NebulaBG,at={(0.98,0.03)},anchor=south east},")
    L.append(r"]")
    coords=" ".join(f"({_fmt(x)},{_fmt(y)})" for x,y in pts)
    L.append(f"\\addplot[only marks,mark=*,{NAVY},mark size=1.8pt] coordinates {{{coords}}};")
    s,i=reg["slope"],reg["intercept"]
    L.append(f"\\addplot[{AMBER},very thick,domain={_fmt(xmin)}:{_fmt(xmax)}] {{{_fmt(s)}*x+({_fmt(i)})}};")
    L.append(r"\legend{Datos,"+reg.get("legend","Regresión")+"}")
    L += [r"\end{axis}", r"\end{tikzpicture}"]
    return "\n".join(L)

# ---------------------------------------------------------------------------
def normal_ci(zlo=-1.96, zhi=1.96, label=None, width=10.6,height=5.4, mark_label=None):
    """Standard normal bell with central area [zlo,zhi] shaded."""
    L=[r"\begin{tikzpicture}", r"\begin{axis}["]
    L.append(f"  width={width}cm, height={height}cm, axis lines=left,")
    L.append(f"  axis line style={{{NAVY}}},")
    L.append(r"  xmin=-3.6, xmax=3.6, ymin=0, ymax=0.45,")
    L.append(r"  xlabel={$z$}, ylabel={},")
    L.append(r"  xlabel style={font=\small},")
    L.append(r"  ytick=\empty, xtick={"+f"{_fmt(zlo)},0,{_fmt(zhi)}"+r"},")
    L.append(r"  xticklabel style={font=\footnotesize,/pgf/number format/assume math mode=true},")
    L.append(f"  tick style={{{NAVY}}}, clip=false,")
    L.append(r"]")
    L.append(f"\\addplot[draw=none,fill={TEAL}!25,domain={_fmt(zlo)}:{_fmt(zhi)},samples=100] {{1/sqrt(2*pi)*exp(-x^2/2)}} \\closedcycle;")
    L.append(f"\\addplot[{NAVY},very thick,smooth,samples=120,domain=-3.6:3.6] {{1/sqrt(2*pi)*exp(-x^2/2)}};")
    if label:
        L.append(f"\\node[font=\\footnotesize,{NAVY}] at (axis cs:0,0.17) {{{label}}};")
    if mark_label:
        L.append(f"\\node[font=\\footnotesize,{AMBER},anchor=north] at (axis cs:{_fmt(zhi)},-0.02) {{{mark_label}}};")
    L += [r"\end{axis}", r"\end{tikzpicture}"]
    return "\n".join(L)

# ---------------------------------------------------------------------------
def venn2(labelA, labelB, onlyA, both, onlyB, outside=None, width=None):
    """Two-set Venn with region values. Pure TikZ (no pgfplots)."""
    L=[r"\begin{tikzpicture}[font=\footnotesize]"]
    L.append(r"\draw[NebulaMuted,thin] (-2.8,-2.0) rectangle (2.8,2.0);")
    L.append(f"\\node[{MUTED},anchor=north east] at (2.75,1.95) {{$U$}};")
    L.append(f"\\draw[{NAVY},thick,fill={NAVY}!8] (-0.7,0) circle (1.5);")
    L.append(f"\\draw[{TEAL},thick,fill={TEAL}!12] (0.7,0) circle (1.5);")
    L.append(f"\\node[{NAVY},anchor=south] at (-1.6,1.5) {{{labelA}}};")
    L.append(f"\\node[{TEAL},anchor=south] at (1.6,1.5) {{{labelB}}};")
    L.append(f"\\node[{NAVY}] at (-1.25,0) {{{onlyA}}};")
    L.append(f"\\node[{NAVY}] at (0,0) {{{both}}};")
    L.append(f"\\node[{TEAL}] at (1.25,0) {{{onlyB}}};")
    if outside is not None:
        L.append(f"\\node[{MUTED}] at (2.1,-1.6) {{{outside}}};")
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)

# ---------------------------------------------------------------------------
def prob_tree(branches, vgap=3.0, cgap=1.25, width=None):
    """branches: list of level-1 {label,p, children:[{label,p}]}. Simple 2-level tree.
    vgap: vertical separation between level-1 nodes; cgap: between children of a node."""
    L=[r"\begin{tikzpicture}[font=\footnotesize,>=Stealth]"]
    n=len(branches)
    ys=[((n-1)/2.0 - i)*vgap for i in range(n)]
    for i,b in enumerate(branches):
        y=ys[i]
        L.append(f"\\draw[{NAVY},thick,->] (0,0) -- (2.3,{_fmt(y)});")
        L.append(f"\\node[{NAVY},fill=NebulaBG,inner sep=1pt] at (1.15,{_fmt(y*0.5+0.18)}) {{{b.get('p','')}}};")
        L.append(f"\\node[{NAVY},anchor=west] at (2.4,{_fmt(y)}) {{{b.get('label','')}}};")
        ch=b.get("children",[])
        m=len(ch)
        for j,c in enumerate(ch):
            cy=y + ((m-1)/2.0 - j)*cgap
            L.append(f"\\draw[{TEAL},thick,->] (3.3,{_fmt(y)}) -- (5.5,{_fmt(cy)});")
            L.append(f"\\node[{TEAL},fill=NebulaBG,inner sep=1pt,font=\\scriptsize] at (4.4,{_fmt((y+cy)/2+0.12)}) {{{c.get('p','')}}};")
            L.append(f"\\node[{NAVY},anchor=west,font=\\scriptsize] at (5.6,{_fmt(cy)}) {{{c.get('label','')}}};")
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)

def contingency(col_headers, row_headers, cells, corner="", width=None):
    """Simple contingency / two-way table. col_headers: list[str]; row_headers: list[str];
    cells: list of rows, each a list[str] matching col_headers length. Pure TikZ matrix."""
    ncol=len(col_headers); nrow=len(row_headers)
    cw=2.1; rh=0.95
    L=[r"\begin{tikzpicture}[font=\footnotesize]"]
    W=(ncol+1)*cw; H=(nrow+1)*rh
    # header band
    L.append(f"\\fill[{NAVY}!10] (0,{_fmt(H-rh)}) rectangle ({_fmt(W)},{_fmt(H)});")
    L.append(f"\\fill[{NAVY}!6] (0,0) rectangle ({_fmt(cw)},{_fmt(H)});")
    # grid
    for i in range(nrow+2):
        y=i*rh
        L.append(f"\\draw[{MUTED}!60] (0,{_fmt(y)}) -- ({_fmt(W)},{_fmt(y)});")
    for j in range(ncol+2):
        x=j*cw
        L.append(f"\\draw[{MUTED}!60] ({_fmt(x)},0) -- ({_fmt(x)},{_fmt(H)});")
    def cell(ci,ri,txt,bold=False,col=NAVY):
        x=ci*cw+cw/2; y=H-(ri+0.5)*rh
        b=r"\bfseries " if bold else ""
        L.append(f"\\node[{col},font=\\footnotesize] at ({_fmt(x)},{_fmt(y)}) {{{b}{txt}}};")
    cell(0,0,corner,bold=True)
    for j,h in enumerate(col_headers): cell(j+1,0,h,bold=True)
    for i,rh_ in enumerate(row_headers): cell(0,i+1,rh_,bold=True)
    for i,row in enumerate(cells):
        for j,v in enumerate(row): cell(j+1,i+1,v)
    L.append(r"\end{tikzpicture}")
    return "\n".join(L)

if __name__=="__main__":
    import json,sys
    # self-test: emit sample figspecs
    figs=[
      {"id":"T-funcplot","prefix":" test-fp","title":"Función","tikz":func_plot(
         [{"expr":"(x-2)/(x^2-9)","color":NAVY,"legend":"$f(x)=\\dfrac{x-2}{x^2-9}$","domain":(-2.9,2.9)}],
         -8,8,-4,4, xtick=2,ytick=1, vasymptotes=[-3,3], hasymptotes=[0],
         points=[{"x":0,"y":0.222,"label":"$(0,\\,0{,}22)$","anchor":"north west"}])},
      {"id":"T-feasible","prefix":"test-fr","title":"Región factible","tikz":feasible_region(
         [{"a":1,"b":1,"c":8,"label":"x+y=8"},{"a":1,"b":0,"c":5,"label":"x=5"},{"a":0,"b":1,"c":6,"label":"y=6"}],
         [{"x":0,"y":0,"label":"$O$","anchor":"north east"},{"x":5,"y":0,"label":"$(5,0)$","anchor":"north"},
          {"x":5,"y":3,"label":"$(5,3)$","anchor":"west"},{"x":2,"y":6,"label":"$(2,6)$","anchor":"south"},{"x":0,"y":6,"label":"$(0,6)$","anchor":"east"}],
         0,9,0,9, xtick=1,ytick=1, feas_poly=[(0,0),(5,0),(5,3),(2,6),(0,6)],
         obj={"dir":(2,1.3),"at":(6.0,6.5),"label":"$\\nabla z$"})},
      {"id":"T-area","prefix":"test-ar","title":"Área","tikz":shaded_area(
         [{"expr":"x^2-x+2.718","color":NAVY,"legend":"$f$"}], 1,2, -1,3,0,6, xtick=1,ytick=1)},
      {"id":"T-scatter","prefix":"test-sc","title":"Regresión","tikz":scatter_regression(
         [(1,2.1),(2,2.9),(3,3.7),(4,5.2),(5,5.8)], {"slope":0.97,"intercept":1.1,"legend":"$y=0{,}97x+1{,}1$"},
         0,6,0,7, xtick=1,ytick=1)},
      {"id":"T-normal","prefix":"test-nc","title":"IC normal","tikz":normal_ci(-1.96,1.96,label="$95\\%$")},
      {"id":"T-venn","prefix":"test-vn","title":"Venn","tikz":venn2("Pop","Techno","60","30","40","80")},
      {"id":"T-tree","prefix":"test-tr","title":"Árbol","tikz":prob_tree(
         [{"label":"$A$","p":"$0{,}35$","children":[{"label":"$+$","p":"$0{,}15$"},{"label":"$-$","p":"$0{,}85$"}]},
          {"label":"$B$","p":"$0{,}20$","children":[{"label":"$+$","p":"$0{,}30$"},{"label":"$-$","p":"$0{,}70$"}]}])},
    ]
    json.dump(figs, open(sys.argv[1] if len(sys.argv)>1 else "/home/claude/ccss/figspec/_selftest.json","w"), ensure_ascii=False, indent=1)
    print("wrote", len(figs), "test figs")
