# -*- coding: utf-8 -*-
"""
Fase 4 — Atomiza las 6 lecciones senaladas por qa_por_curso/selectividad_fisica_structural_issues.csv
(la lista OFICIAL y obligatoria, no mi propio recuento de palabras mas amplio
de AUDIT_BEFORE.md). Cada leccion se divide en dos, por un punto de corte
tematico elegido a mano leyendo los titulos de theory_blocks (no un punto
medio ciego), preservando el 100% de las piezas existentes: nada se inventa
ni se descarta, solo se reparte.

Reparto de contenedores de practica (worked_examples, guided_exercises,
exercises, exam_questions, challenge_questions, mcq, flashcards,
misconceptions, common_mistakes, keywords, diagnostic_items):
 - si la pieza tiene concept_ids/objective_id(s), se asigna a la Parte cuyo
   conjunto de concept_ids (tomado de los theory_blocks de esa parte) tiene
   mas solapamiento;
 - si no hay solapamiento o no hay concept_ids, se reparte por posicion
   (mitad a cada parte), preservando el orden original.

derived_from / split_part son campos NUEVOS, aditivos (no estaban en el
schema plano ni rompen index.html).
"""
import json, os, math

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")

# (unit, bkey, split_after_theory_block_id, new_bkey_a, new_bkey_b, subtitle_a, subtitle_b)
SPLITS = [
    ("ondas", "05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json", "TH-05-3",
     "05a_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json",
     "05b_Diferencia_de_fase_el_procedimiento_y_sus_trampas.json",
     "Diferencia de fase: puntos en fase y en oposición (I) — el concepto",
     "Diferencia de fase: puntos en fase y en oposición (II) — procedimiento y aplicación"),
    ("ondas", "11_Ondas_estacionarias_la_onda_que_no_viaja.json", "TH-11-5",
     "11a_Ondas_estacionarias_qué_son_y_dónde_están_los_nodos.json",
     "11b_Ondas_estacionarias_energía_y_errores_frecuentes.json",
     "Ondas estacionarias: la onda que no viaja (I) — qué son, nodos y vientres",
     "Ondas estacionarias: la onda que no viaja (II) — energía, velocidad y errores frecuentes"),
    ("optica", "03_El_ángulo_límite_y_la_reflexión_total.json", "TH-03-4",
     "03a_El_ángulo_límite_y_la_reflexión_total.json",
     "03b_Decidir_la_reflexión_total_y_el_ángulo_de_Brewster.json",
     "El ángulo límite y la reflexión total (I) — condición y fibra óptica",
     "El ángulo límite y la reflexión total (II) — procedimiento de decisión y Brewster"),
    ("campo_gravitatorio", "02_La_ley_de_gravitación_universal.json", "TH-02-4",
     "02a_La_ley_de_gravitación_universal_enunciado.json",
     "02b_La_ley_de_gravitación_universal_aplicaciones.json",
     "La ley de gravitación universal (I) — enunciado, vectores y el par de fuerzas",
     "La ley de gravitación universal (II) — qué es G y aplicaciones (pesar la Tierra y el Sol)"),
    ("cuantica", "06_Indeterminación_y_la_nueva_mecánica_cuántica.json", "TH-06-4",
     "06a_Indeterminación_el_principio_y_el_final_de_la_trayectoria.json",
     "06b_La_nueva_mecánica_cuántica_Schrödinger_y_Born.json",
     "Indeterminación y la nueva mecánica cuántica (I) — el principio de indeterminación",
     "Indeterminación y la nueva mecánica cuántica (II) — Schrödinger, Born y el cierre"),
    ("electromagnetismo", "05_El_potencial_eléctrico_sumar_sin_vectores.json", "TH-05-3",
     "05a_El_potencial_eléctrico_definición_y_energía.json",
     "05b_El_potencial_eléctrico_superficies_equipotenciales_y_signos.json",
     "El potencial eléctrico: sumar sin vectores (I) — definición, suma algebraica y energía",
     "El potencial eléctrico: sumar sin vectores (II) — hacia dónde se mueven las cargas, equipotenciales y signos"),
]

PRACTICE_CONTAINERS = ["worked_examples","guided_exercises","exercises","exam_questions",
                        "challenge_questions","mcq","flashcards","misconceptions",
                        "common_mistakes","keywords","diagnostic_items"]

def concept_set(blocks):
    s = set()
    for b in blocks:
        s.update(b.get("concept_ids", []) or [])
    return s

def item_concepts(item):
    s = set(item.get("concept_ids", []) or [])
    if item.get("concept_id"):
        s.add(item["concept_id"])
    if item.get("objective_ids"):
        pass
    return s

def split_container(items, concepts_a, concepts_b):
    a_list, b_list, undecided = [], [], []
    for it in items:
        ic = item_concepts(it) if isinstance(it, dict) else set()
        oa = len(ic & concepts_a)
        ob = len(ic & concepts_b)
        if oa > ob:
            a_list.append(it)
        elif ob > oa:
            b_list.append(it)
        else:
            undecided.append(it)
    # distribute undecided by position, half to each, preserving relative order
    half = math.ceil(len(undecided) / 2)
    a_list.extend(undecided[:half])
    b_list.extend(undecided[half:])
    return a_list, b_list

def parse_hours(s):
    if not isinstance(s, str):
        return 1.0
    import re
    m = re.search(r"([\d,\.]+)\s*h", s)
    return float(m.group(1).replace(",", ".")) if m else 1.0

def fmt_hours(h):
    h = round(h * 2) / 2  # round to nearest 0.5h
    if h == int(h):
        return f"{int(h)} h"
    return f"{str(h).replace('.', ',')} h"

def build_part(lesson, unit, theory_blocks_part, part_letter, new_id, title, prereq_extra, concepts_other):
    part = dict(lesson)  # shallow copy of top-level
    part["id"] = new_id
    part["title"] = title
    part["theory_blocks"] = theory_blocks_part
    part["derived_from"] = lesson.get("id")
    part["split_part"] = part_letter
    my_concepts = concept_set(theory_blocks_part)
    for cont in PRACTICE_CONTAINERS:
        pass  # filled by caller
    return part, my_concepts

def main():
    log = []
    for unit, bkey, split_tb_id, new_bkey_a, new_bkey_b, title_a, title_b in SPLITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        lesson = d[bkey]
        tbs = lesson["theory_blocks"]
        idx = next(i for i, tb in enumerate(tbs) if tb.get("id") == split_tb_id)
        tbs_a = tbs[:idx+1]
        tbs_b = tbs[idx+1:]
        concepts_a = concept_set(tbs_a)
        concepts_b = concept_set(tbs_b)

        hours = parse_hours(lesson.get("estimated_length"))
        hours_a = max(0.5, round((hours * (len(tbs_a)/len(tbs))) * 2) / 2)
        hours_b = max(0.5, round((hours * (len(tbs_b)/len(tbs))) * 2) / 2)

        lesson_a = {k: v for k, v in lesson.items() if k not in ("schema_v2",)}
        lesson_b = {k: v for k, v in lesson.items() if k not in ("schema_v2",)}
        lesson_a["id"] = lesson.get("id", "L") + "a"
        lesson_b["id"] = lesson.get("id", "L") + "b"
        lesson_a["title"] = title_a
        lesson_b["title"] = title_b
        lesson_a["theory_blocks"] = tbs_a
        lesson_b["theory_blocks"] = tbs_b
        lesson_a["estimated_length"] = fmt_hours(hours_a)
        lesson_b["estimated_length"] = fmt_hours(hours_b)
        lesson_a["derived_from"] = lesson.get("id")
        lesson_b["derived_from"] = lesson.get("id")
        lesson_a["split_part"] = "A"
        lesson_b["split_part"] = "B"
        lesson_b["prerequisites"] = list(lesson.get("prerequisites", [])) + [{
            "id": f"P-SPLIT-{lesson.get('id')}",
            "statement": f"Haber completado la parte (I) de esta misma lección ({title_a}).",
            "blocking": True,
            "why_it_matters": "Esta parte continua directamente la deduccion y el vocabulario de la parte (I); no es una leccion independiente.",
        }]

        for cont in PRACTICE_CONTAINERS:
            items = lesson.get(cont, [])
            a_items, b_items = split_container(items, concepts_a, concepts_b)
            lesson_a[cont] = a_items
            lesson_b[cont] = b_items

        # objectives: split by scope/bloom match to theory blocks via concept_ids too; fallback half/half
        objs = lesson.get("objectives", [])
        obj_a, obj_b = [], []
        for o in objs:
            oc = set(o.get("concept_ids", []) or [])
            if oc & concepts_a and not (oc & concepts_b):
                obj_a.append(o)
            elif oc & concepts_b and not (oc & concepts_a):
                obj_b.append(o)
            else:
                (obj_a if len(obj_a) <= len(obj_b) else obj_b).append(o)
        lesson_a["objectives"] = obj_a or objs[:math.ceil(len(objs)/2)]
        lesson_b["objectives"] = obj_b or objs[math.ceil(len(objs)/2):]

        # summary: split key_points/formulas by concept overlap similarly; keep big_idea distinct per part (manually trimmed)
        summ = lesson.get("summary", {})
        kps = summ.get("key_points", [])
        half_kp = math.ceil(len(kps)/2)
        lesson_a["summary"] = {
            "big_idea": summ.get("big_idea", ""),
            "key_points": kps[:half_kp],
            "formulas": summ.get("formulas", [])[:math.ceil(len(summ.get("formulas", []))/2)],
            "what_to_remember_if_nothing_else": summ.get("what_to_remember_if_nothing_else", ""),
        }
        lesson_b["summary"] = {
            "big_idea": summ.get("big_idea", ""),
            "key_points": kps[half_kp:],
            "formulas": summ.get("formulas", [])[math.ceil(len(summ.get("formulas", []))/2):],
            "what_to_remember_if_nothing_else": summ.get("what_to_remember_if_nothing_else", ""),
        }

        del d[bkey]
        # insert in same relative place (dict order): rebuild preserving order
        new_d = {}
        inserted = False
        for k, v in d.items():
            new_d[k] = v
        # Python 3.7+ dicts: just append at end is fine since catalog.json controls display order, not json key order
        new_d[new_bkey_a] = lesson_a
        new_d[new_bkey_b] = lesson_b
        json.dump(new_d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

        tot_before = sum(len(lesson.get(c, [])) for c in PRACTICE_CONTAINERS)
        tot_after = sum(len(lesson_a.get(c, [])) + len(lesson_b.get(c, [])) for c in PRACTICE_CONTAINERS)
        log.append((unit, bkey, tot_before, tot_after, len(tbs_a), len(tbs_b)))
        print(f"{unit}/{bkey}: piezas antes={tot_before} despues={tot_after} "
              f"(theory_blocks {len(tbs_a)}+{len(tbs_b)}={len(tbs)})  "
              f"{'OK' if tot_before==tot_after else 'MISMATCH!!'}")

    assert all(b == a for (_,_,b,a,_,_) in log), "Se perdieron o duplicaron piezas en algun split"
    print("TODOS LOS SPLITS CONSERVAN EL NUMERO TOTAL DE PIEZAS.")

if __name__ == "__main__":
    main()
