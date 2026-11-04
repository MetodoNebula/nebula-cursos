#!/usr/bin/env python3
"""render_tikz_svg.py - Nebula - regenera el SVG *web* de una figura a
partir de su TikZ, reproduciendo el estilo de los bundles.

Pipeline (reconstruido por ingenieria inversa de los SVG existentes):
  TikZ  --(standalone + preambulo Nebula)-->  PDF (pdflatex)
        --(dvisvgm --pdf --no-fonts)-->        SVG con colores del PDF
        --(remapeo de color PDF->web)-->       SVG con la paleta web
        --(+ rect de fondo data-nebula-background)-->  SVG final

Requiere: pdflatex y dvisvgm en el PATH, y las plantillas en
engine/templates/. (dvisvgm esta en el equipo del propietario; no en el
contenedor de la nube.)

Remapeo verificado (coincidencia exacta de conteos en AS-P07-11-1):
  #b23a48 (NebulaError, rojo) -> #7952a3 (morado web)
  #eef3f8 (NebulaSoft)        -> #e4eaf0 (gris-azul claro web)
  #c9a646 (NebulaGold)        -> #b77916 (ambar web)
  (#0b1f3a navy, #2e7d5b verde, #f6f8fb fondo: sin cambio)

Uso:
  # desde un bundle, regenera e inyecta en el propio bundle:
  python3 render_tikz_svg.py --bundle <bundle.json> --lesson <clave> --asset <id> --write
  # o desde un .tikz suelto -> stdout:
  python3 render_tikz_svg.py --tikz fig.tikz > out.svg
"""
import argparse, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TPL  = os.path.join(HERE, "templates")
REMAP = {"#b23a48": "#7952a3", "#eef3f8": "#e4eaf0", "#c9a646": "#b77916"}

WRAP = r"""\documentclass[border=12pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsfonts,mathtools}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta,positioning,decorations.pathmorphing,patterns,angles,quotes,shapes.geometric,intersections,through,3d,decorations.markings}
\usepackage{pgfplots}\pgfplotsset{compat=1.16}
\usepackage{xcolor}\usepackage{etoolbox}
\def\nebulalang{en}
\providecommand{\nbL}[2]{#2}\providecommand{\nbIfES}[2]{#2}
\providecommand{\si}[1]{#1}\providecommand{\SI}[2]{#1\,#2}\providecommand{\num}[1]{#1}
\input{%(palette)s}
\input{%(figures)s}
\input{%(optics)s}
\input{%(waves)s}
\begin{document}
%(tikz)s
\end{document}
"""

def _palette(dst):
    pre = open(os.path.join(TPL, "nebula_preamble.tex"), encoding="utf-8").read()
    colors = [l for l in pre.splitlines() if re.match(r'\s*\\(definecolor|colorlet)', l)]
    m = re.search(r'\\tikzset\{.*?\n\}', pre, re.S)
    open(dst, "w", encoding="utf-8").write("\n".join(colors) + "\n" + (m.group(0) if m else "") + "\n")

def render(tikz):
    with tempfile.TemporaryDirectory() as d:
        pal = os.path.join(d, "palette.tex"); _palette(pal)
        open(os.path.join(d, "fig.tikz"), "w", encoding="utf-8").write(tikz)
        tex = WRAP % dict(palette=pal,
                          figures=os.path.join(TPL, "nebula_figures.tex"),
                          optics=os.path.join(TPL, "nebula_optics.tex"),
                          waves=os.path.join(TPL, "nebula_waves.tex"),
                          tikz=r"\input{%s}" % os.path.join(d, "fig.tikz"))
        open(os.path.join(d, "b.tex"), "w", encoding="utf-8").write(tex)
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "b.tex"],
                           cwd=d, capture_output=True, text=True)
        if not os.path.exists(os.path.join(d, "b.pdf")):
            sys.stderr.write(r.stdout[-1500:]); raise SystemExit("pdflatex failed")
        subprocess.run(["dvisvgm", "--pdf", "--no-fonts", "--output=b.svg", "b.pdf"],
                       cwd=d, capture_output=True, text=True, check=True)
        svg = open(os.path.join(d, "b.svg"), encoding="utf-8").read()
    for k, v in REMAP.items():
        svg = svg.replace(k, v).replace(k.upper(), v)
    m = re.search(r'viewBox=["\']([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)["\']', svg)
    x, y, w, h = m.groups()
    bg = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f6f8fb" data-nebula-background="true"/>'
    return re.sub(r'(<svg[^>]*>)', r'\1' + bg, svg, count=1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tikz"); ap.add_argument("--bundle"); ap.add_argument("--lesson")
    ap.add_argument("--asset"); ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if a.tikz:
        print(render(open(a.tikz, encoding="utf-8").read())); return
    d = json.load(open(a.bundle, encoding="utf-8"))
    for b in d[a.lesson]["theory_blocks"]:
        for asset in b.get("assets", []) or []:
            if asset["id"] == a.asset:
                svg = render(asset["tikz"])
                if a.write:
                    asset["svg"] = svg
                    out = json.dumps(d, ensure_ascii=False, indent=2); json.loads(out)
                    open(a.bundle, "w", encoding="utf-8").write(out)
                    sys.stderr.write("written %s svg len %d\n" % (a.asset, len(svg)))
                else:
                    print(svg)
                return
    raise SystemExit("asset not found")

if __name__ == "__main__":
    main()
