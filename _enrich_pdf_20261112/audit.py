import json, glob, os, hashlib, re, sys
BND="bundles"; BK="bundles/_backup_pdf_enrich_20261112"
units=["mat_trigonometria","mat_complejos","mat_algebra_polinomios","mat_estadistica_descriptiva",
       "mat_sucesiones","mat_sistemas_inecuaciones","mat_limites_continuidad",
       "mat_proporcionalidad_financiera","mat_potencias_raices"]
def load(p):
    with open(p,encoding="utf-8") as f: return json.load(f)
def assets(L):
    out={}
    for tb in (L.get("theory_blocks") or []):
        for a in (tb.get("assets") or []):
            out[a.get("id","")] = hashlib.md5(((a.get("tikz") or "")+"||"+(a.get("svg") or "")).encode()).hexdigest()
    return out
def concepts(L):
    c={k.get("concept_id") for k in (L.get("keywords") or []) if isinstance(k,dict)}
    for o in (L.get("objectives") or []): c|=set(o.get("concept_ids") or [])
    for e in (L.get("exercises") or []): c|=set(e.get("concept_ids") or [])
    return {x for x in c if x}
prob=[]; ids={}; tot=new=0; figs=0
for u in units:
    p=f"{BND}/eso_matematicas__{u}.json"; d=load(p); b=load(f"{BK}/eso_matematicas__{u}.json")
    for lk,L in d.items():
        if lk not in b: prob.append(f"[NEW LESSON KEY] {u}/{lk}"); continue
        BL=b[lk]
        an,ab=assets(L),assets(BL); figs+=len(an)
        if an!=ab: prob.append(f"[FIGURE CHANGED] {u}/{lk}: {sorted(set(an.items())^set(ab.items()))[:3]}")
        for fld in ("theory_blocks","objectives","keywords","misconceptions","worked_examples",
                    "guided_exercises","mcq","flashcards","exam_questions","challenge_questions",
                    "diagnostic_items","common_mistakes","summary","title","prerequisites","exam_notes"):
            if json.dumps(L.get(fld),sort_keys=True,ensure_ascii=False)!=json.dumps(BL.get(fld),sort_keys=True,ensure_ascii=False):
                prob.append(f"[FIELD CHANGED] {u}/{lk}.{fld}")
        oldids=[e["id"] for e in (BL.get("exercises") or [])]
        nowids=[e["id"] for e in (L.get("exercises") or [])]
        if nowids[:len(oldids)]!=oldids: prob.append(f"[OLD EXERCISES ALTERED/REORDERED] {u}/{lk}")
        vobj={o.get("id") for o in (L.get("objectives") or [])}; vcon=concepts(L)
        for e in (L.get("exercises") or []):
            tot+=1; ids.setdefault(e["id"],[]).append(f"{u}/{lk}")
            if e["id"] in oldids: continue
            new+=1
            txt=[e.get("statement",""),e.get("answer",""),e.get("full_solution","")]+list(e.get("hints") or [])+list(e.get("common_errors") or [])
            for t in txt:
                if "\n" in t or "\\n" in t: prob.append(f"[NEWLINE] {u}/{e['id']}")
                if t.count("$")%2: prob.append(f"[UNBALANCED $] {u}/{e['id']}: {t[:60]}")
                if t.count("{")!=t.count("}"): prob.append(f"[UNBALANCED BRACES] {u}/{e['id']}: {t[:70]}")
                if re.search(r"\\\(|\\\[|\\begin\{", t): prob.append(f"[BAD LATEX ENV] {u}/{e['id']}")
                if re.search(r"[0-9],[0-9]", t): prob.append(f"[DECIMAL COMMA SIN {{,}}] {u}/{e['id']}: {t[:70]}")
            for o in e.get("objective_ids") or []:
                if o not in vobj: prob.append(f"[BAD OBJ] {u}/{e['id']}: {o}")
            for c in e.get("concept_ids") or []:
                if c not in vcon: prob.append(f"[BAD CONCEPT] {u}/{e['id']}: {c}")
            if e.get("provenance")!="SOURCE_DERIVED": prob.append(f"[PROVENANCE] {u}/{e['id']}")
            if len(e.get("full_solution",""))<150: prob.append(f"[SOL CORTA] {u}/{e['id']}: {len(e.get('full_solution',''))}")
            if not e.get("hints") or not e.get("common_errors"): prob.append(f"[FALTAN HINTS/ERRORES] {u}/{e['id']}")
            if not isinstance(e.get("difficulty"),int) or not 2<=e["difficulty"]<=5: prob.append(f"[DIFICULTAD] {u}/{e['id']}")
            if e.get("type") not in ("STANDARD","REASONING","CONTEXT"): prob.append(f"[TYPE] {u}/{e['id']}: {e.get('type')}")
for k,v in ids.items():
    if len(v)>1: prob.append(f"[DUP ID] {k}: {v}")
print(f"ejercicios totales: {tot} | nuevos: {new} | figuras verificadas: {figs}")
if prob:
    print(f"\nPROBLEMAS ({len(prob)}):")
    for x in prob[:80]: print(" -",x)
else:
    print("\nSIN PROBLEMAS")
