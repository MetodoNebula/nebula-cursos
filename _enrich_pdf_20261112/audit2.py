import json, os, hashlib, re
A="bundles/_backup_pdf_enrich_20261112"; B="bundles/_backup_pdf_enrich_20261112b"
U1=["mat_trigonometria","mat_complejos","mat_algebra_polinomios","mat_estadistica_descriptiva",
    "mat_sucesiones","mat_sistemas_inecuaciones","mat_limites_continuidad",
    "mat_proporcionalidad_financiera","mat_potencias_raices"]
U2=["mat_probabilidad","mat_estadistica_bidimensional"]
def load(p): return json.load(open(p,encoding="utf-8"))
def assets(L):
    return {a.get("id"): hashlib.md5(((a.get("tikz") or "")+"||"+(a.get("svg") or "")).encode()).hexdigest()
            for tb in (L.get("theory_blocks") or []) for a in (tb.get("assets") or [])}
def concepts(L):
    c={k.get("concept_id") for k in (L.get("keywords") or []) if isinstance(k,dict)}
    for o in (L.get("objectives") or []): c|=set(o.get("concept_ids") or [])
    for e in (L.get("exercises") or []): c|=set(e.get("concept_ids") or [])
    return {x for x in c if x}
prob=[]; ids={}; tot=new=figs=0
FIXED={"AS-8A01-2","AS-02-03-1","AS-1303-1","AS-0101-1","AS-0101-2"}
for bk,units in ((A,U1),(B,U2)):
    for u in units:
        d=load(f"bundles/eso_matematicas__{u}.json"); b=load(f"{bk}/eso_matematicas__{u}.json")
        for lk,L in d.items():
            BL=b[lk]; an,ab=assets(L),assets(BL)
            if bk==A: figs+=len(an)
            for k,v in an.items():
                if ab.get(k)!=v and k not in FIXED: prob.append(f"[FIGURA ALTERADA] {u}/{k}")
            if set(an)!=set(ab): prob.append(f"[SET DE FIGURAS DISTINTO] {u}/{lk}")
            old=[e["id"] for e in BL["exercises"]]; now=[e["id"] for e in L["exercises"]]
            if now[:len(old)]!=old: prob.append(f"[EJERCICIOS PREVIOS ALTERADOS] {u}/{lk}")
            vobj={o.get("id") for o in (L.get("objectives") or [])}; vcon=concepts(L)
            for e in L["exercises"]:
                if bk==A or u in U2: tot+=1
                ids.setdefault(e["id"],[]).append(u)
                if e["id"] in old: continue
                new+=1
                txt=[e["statement"],e["answer"],e["full_solution"]]+list(e.get("hints") or [])+list(e.get("common_errors") or [])
                for t in txt:
                    if "\n" in t or "\\n" in t: prob.append(f"[SALTO DE LINEA] {u}/{e['id']}")
                    if t.count("$")%2: prob.append(f"[$ DESBALANCEADO] {u}/{e['id']}")
                    if t.count("{")!=t.count("}"): prob.append(f"[LLAVES] {u}/{e['id']}")
                for o in e.get("objective_ids") or []:
                    if o not in vobj: prob.append(f"[OBJETIVO INVALIDO] {u}/{e['id']}: {o}")
                for c in e.get("concept_ids") or []:
                    if c not in vcon: prob.append(f"[CONCEPTO INVALIDO] {u}/{e['id']}: {c}")
                if e.get("provenance")!="SOURCE_DERIVED": prob.append(f"[PROVENANCE] {u}/{e['id']}")
                if len(e["full_solution"])<150: prob.append(f"[SOLUCION CORTA] {u}/{e['id']}")
                if not e.get("hints") or not e.get("common_errors"): prob.append(f"[SIN HINTS/ERRORES] {u}/{e['id']}")
                if e.get("difficulty") not in (2,3,4,5): prob.append(f"[DIFICULTAD] {u}/{e['id']}")
for k,v in ids.items():
    if len(v)>1 and len(set(v))<len(v): prob.append(f"[ID DUPLICADO] {k}: {v}")
print(f"ejercicios nuevos en total: {new} | figuras comprobadas: {figs}")
print("PROBLEMAS:", len(prob))
for q in prob[:30]: print(" -",q)
