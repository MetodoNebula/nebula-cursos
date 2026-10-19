# -*- coding: utf-8 -*-
"""
Fase 5/6 — Construye KNOWLEDGE_GRAPH.json: nodos = las 88 lecciones (82 de
contenido + 6 de Fundamentos) con sus canonical_lesson_id, y aristas =
prerequisitos. Dos tipos de arista:
  - "course" : prerequisito ya declarado dentro de la propia unidad
               (prerequisites[].id original de cada leccion, cuando
               corresponde a otra leccion de la unidad: inferido por orden).
  - "foundations" : prerequisito de habilidad transversal (vectores,
               trigonometria, despeje algebraico, notacion cientifica/SI,
               lectura de graficas, conservacion de la energia), detectado
               por coincidencia de palabras clave en el texto de
               prerequisites[].statement, y enlazado al microtema de
               Fundamentos correspondiente para remediacion just-in-time.
"""
import json, os, re

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica",
         "relatividad","cuantica","nuclear","fundamentos"]

FOUNDATIONS_KEYWORDS = {
    "C-FUND-VEC": [r"vector", r"componentes?\b", r"\\vec"],
    "C-FUND-TRIG": [r"trigonometr", r"\\mathrm\{sen\}", r"\bseno\b", r"\bcoseno\b", r"\btangente\b"],
    "C-FUND-ALG": [r"despej", r"algebra"],
    "C-FUND-SI": [r"notaci[oó]n cient", r"unidades? del? SI\b", r"cifras? significativ"],
    "C-FUND-GRAF": [r"gr[aá]fica", r"pendiente", r"[aá]rea bajo"],
    "C-FUND-ENERGIA": [r"conservaci[oó]n de la energ", r"energ[ií]a mec[aá]nica"],
}

def match_foundations(text):
    hits = []
    for concept, patterns in FOUNDATIONS_KEYWORDS.items():
        for p in patterns:
            if re.search(p, text or "", re.IGNORECASE):
                hits.append(concept)
                break
    return hits

def main():
    nodes = []
    edges = []
    lesson_index = {}  # unit -> ordered list of (bkey, canonical_id)

    all_lessons = {}
    for unit in UNITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        lesson_index[unit] = []
        for bkey, lesson in d.items():
            cid = lesson["schema_v2"]["canonical_lesson_id"]
            all_lessons[cid] = (unit, bkey, lesson)
            lesson_index[unit].append((bkey, cid))
            nodes.append({
                "id": cid,
                "unit": unit,
                "bkey": bkey,
                "title": lesson.get("title"),
                "estimated_length": lesson.get("estimated_length"),
                "is_foundations": unit == "fundamentos",
                "derived_from": lesson.get("derived_from"),
            })

    for unit in UNITS:
        if unit == "fundamentos":
            continue
        ordered = lesson_index[unit]
        for i, (bkey, cid) in enumerate(ordered):
            lesson = all_lessons[cid][2]
            # sequential "course" edge: this lesson requires the previous one in the unit
            if i > 0:
                prev_cid = ordered[i-1][1]
                edges.append({"from": prev_cid, "to": cid, "type": "course", "blocking": False,
                              "reason": "orden secuencial declarado en la unidad"})
            for p in lesson.get("prerequisites", []):
                stmt = p.get("statement", "")
                fconcepts = match_foundations(stmt)
                for fc in fconcepts:
                    # find the fundamentos lesson with that tag
                    target = None
                    for fb, fcid in lesson_index["fundamentos"]:
                        if all_lessons[fcid][2].get("foundations_concept_tag") == fc:
                            target = fcid
                            break
                    if target:
                        edges.append({"from": target, "to": cid, "type": "foundations",
                                      "blocking": p.get("blocking", False),
                                      "reason": stmt[:160]})

    # dedupe foundations edges
    seen = set()
    dedup_edges = []
    for e in edges:
        key = (e["from"], e["to"], e["type"])
        if key in seen:
            continue
        seen.add(key)
        dedup_edges.append(e)

    graph = {"nodes": nodes, "edges": dedup_edges,
             "foundations_concepts": list(FOUNDATIONS_KEYWORDS.keys())}
    out_fp = os.path.join(PILOT, "KNOWLEDGE_GRAPH.json")
    json.dump(graph, open(out_fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Nodos: {len(nodes)}  Aristas: {len(dedup_edges)}")
    from collections import Counter
    print(Counter(e["type"] for e in dedup_edges))
    fcount = Counter(e["from"] for e in dedup_edges if e["type"] == "foundations")
    for fc in lesson_index["fundamentos"]:
        bkey, cid = fc
        print(f"  {bkey}: {fcount.get(cid,0)} lecciones lo referencian como prerrequisito")

if __name__ == "__main__":
    main()
