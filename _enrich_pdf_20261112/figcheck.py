import json,re,xml.etree.ElementTree as ET
units=["mat_trigonometria","mat_complejos","mat_algebra_polinomios","mat_estadistica_descriptiva",
       "mat_sucesiones","mat_sistemas_inecuaciones","mat_limites_continuidad",
       "mat_proporcionalidad_financiera","mat_potencias_raices"]
prob=[]; tot=0; svgs=[]
for u in units:
    d=json.load(open(f"bundles/eso_matematicas__{u}.json",encoding="utf-8"))
    for lk,L in d.items():
        for tb in (L.get("theory_blocks") or []):
            for a in (tb.get("assets") or []):
                tot+=1; aid=a.get("id"); sv=a.get("svg") or ""; tk=a.get("tikz") or ""
                tag=f"{u}/{lk[:28]}/{aid}"
                if not sv: prob.append(f"[SIN SVG] {tag}"); continue
                if not tk: prob.append(f"[SIN TIKZ] {tag}")
                try: root=ET.fromstring(sv)
                except Exception as ex: prob.append(f"[SVG NO PARSEA] {tag}: {ex}"); continue
                vb=root.get("viewBox")
                if not vb: prob.append(f"[SIN viewBox] {tag}"); continue
                x0,y0,w,h=[float(v) for v in vb.replace(',',' ').split()]
                if w<20 or h<20: prob.append(f"[SVG DIMINUTO] {tag}: {w}x{h}")
                if len(sv)<300: prob.append(f"[SVG CASI VACIO] {tag}: {len(sv)} bytes")
                rects=root.iter('{http://www.w3.org/2000/svg}rect')
                bg=[r for r in rects if float(r.get('width',0) or 0)>=w*0.9 and float(r.get('height',0) or 0)>=h*0.9]
                if not bg: prob.append(f"[SIN FONDO COMPLETO] {tag}")
                # elementos fuera del viewBox (causa de 'cuadros blancos')
                out=0
                for el in root.iter():
                    xx,yy=el.get('x'),el.get('y')
                    try:
                        if xx is not None and yy is not None:
                            fx,fy=float(xx),float(yy)
                            if fx<x0-1 or fy<y0-1 or fx>x0+w+1 or fy>y0+h+1: out+=1
                    except ValueError: pass
                if out: prob.append(f"[ELEMENTOS FUERA DEL LIENZO] {tag}: {out}")
                if 'data-nebula-fig' not in sv: prob.append(f"[SIN MARCADOR nebula-fig] {tag}")
                svgs.append((tag,aid,sv,w,h))
print(f"figuras: {tot}  | svg validados: {len(svgs)}")
print("PROBLEMAS:",len(prob))
for q in prob[:40]: print(" -",q)
json.dump([[t,i] for t,i,_,_,_ in svgs], open('_enrich_pdf_20261112/figlist.json','w'))
