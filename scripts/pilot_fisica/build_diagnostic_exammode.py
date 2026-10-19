# -*- coding: utf-8 -*-
"""
Fase 6b — Diagnostico inicial por habilidades + Exam Mode (modulo 09,
"PAU integrada"). Todo por referencia a ids ya existentes, sin duplicar
contenido.

Diagnostico: un vector de habilidades (las 6 de Fundamentos + las 8
unidades de contenido), con 1-2 items representativos por habilidad
(diagnostic_items ya existentes), total 14-20 items -> dentro del rango
12-25 pedido por el encargo.

Exam Mode: 
  - topic_questions: exam_questions agrupadas por unidad (practica por tema).
  - mixed_questions: una mezcla de exam_questions de varias unidades.
  - timed_questions: subconjunto con tiempo estimado por pregunta (2
    minutos por punto de "marks", heuristica estandar PAU).
  - partial_mock_exams: 2 examenes parciales (una opcion de la PAU real:
    2-3 bloques) muestreando exam_questions de 3-4 unidades relacionadas.
  - full_mock_exams: 2 examenes completos de las 8 unidades (como la
    prueba real, que suele pedir elegir entre dos opciones con cuestiones
    de todo el temario).
Todas las preguntas reducen scaffolding: solo se referencia el id, sin
hints (segun pide el encargo para la capa de examen).
"""
import json, os, random

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear"]

random.seed(42)

def load_all():
    data = {}
    for unit in UNITS + ["fundamentos"]:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        data[unit] = json.load(open(fp, encoding="utf-8"))
    return data

def build_diagnostic(data):
    items = []
    # 6 foundations skills
    for bkey, lesson in data["fundamentos"].items():
        tag = lesson.get("foundations_concept_tag")
        dlist = lesson.get("diagnostic_items", [])
        if dlist:
            items.append({"skill": tag, "ref_lesson": lesson["schema_v2"]["canonical_lesson_id"],
                          "item_id": dlist[0]["id"]})
    # 8 content units: take first diagnostic_item of first lesson + one mid-unit lesson
    for unit in UNITS:
        lessons = list(data[unit].items())
        picks = [lessons[0]]
        if len(lessons) > 4:
            picks.append(lessons[len(lessons)//2])
        for bkey, lesson in picks:
            dlist = lesson.get("diagnostic_items", [])
            if dlist:
                items.append({"skill": f"unidad:{unit}", "ref_lesson": lesson["schema_v2"]["canonical_lesson_id"],
                              "item_id": dlist[0]["id"]})
    return {"diagnostic_items": items, "n_items": len(items),
            "skill_vector_axes": sorted(set(it["skill"] for it in items)),
            "scoring_note": "Cada eje de habilidad se puntua como % de items correctos de ese eje; el resultado recomienda ruta (DESDE_CERO si predominan ejes <50%, FAST_REVIEW si todos >80%, STANDARD/EXCELLENCE en el resto, segun objetivo declarado por el alumno)."}

def collect_exam_ids(data):
    by_unit = {}
    for unit in UNITS:
        ids = []
        for bkey, lesson in data[unit].items():
            cid = lesson["schema_v2"]["canonical_lesson_id"]
            for eq in lesson.get("exam_questions", []):
                if eq.get("id"):
                    ids.append({"ref_lesson": cid, "item_id": eq["id"], "marks": eq.get("marks")})
        by_unit[unit] = ids
    return by_unit

def build_exam_mode(data):
    by_unit = collect_exam_ids(data)
    topic_questions = {u: ids for u, ids in by_unit.items()}

    all_ids = [dict(x, unit=u) for u, ids in by_unit.items() for x in ids]
    rng = random.Random(7)
    mixed = rng.sample(all_ids, min(10, len(all_ids)))

    timed = []
    for q in all_ids:
        marks = q.get("marks")
        minutes = None
        if isinstance(marks, (int, float)):
            minutes = round(marks * 2)
        timed.append({**q, "estimated_minutes": minutes or 5})

    def sample_mock(unit_subset, n_per_unit, seed):
        rng2 = random.Random(seed)
        mock = []
        for u in unit_subset:
            pool = by_unit.get(u, [])
            if pool:
                mock.extend(rng2.sample(pool, min(n_per_unit, len(pool))))
        return mock

    partial_mocks = [
        {"mock_id": "PARCIAL-1-mecanica", "units": ["campo_gravitatorio", "mas", "ondas"],
         "items": sample_mock(["campo_gravitatorio", "mas", "ondas"], 2, 101)},
        {"mock_id": "PARCIAL-2-moderna", "units": ["electromagnetismo", "optica", "relatividad", "cuantica", "nuclear"],
         "items": sample_mock(["electromagnetismo", "optica", "relatividad", "cuantica", "nuclear"], 1, 102)},
    ]
    full_mocks = [
        {"mock_id": f"COMPLETO-{i}",
         "items": sample_mock(UNITS, 1, 200+i)}
        for i in (1, 2)
    ]

    return {
        "topic_questions": topic_questions,
        "mixed_questions": mixed,
        "timed_questions": timed,
        "partial_mock_exams": partial_mocks,
        "full_mock_exams": full_mocks,
        "scaffolding_policy": "En Exam Mode no se muestran hints ni se revela full_solution hasta que el alumno entrega una respuesta; mark_scheme se usa para autocorregir.",
    }

def main():
    data = load_all()
    diag = build_diagnostic(data)
    exam = build_exam_mode(data)
    json.dump(diag, open(os.path.join(PILOT, "diagnostic.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(exam, open(os.path.join(PILOT, "exam_mode.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Diagnostico:", diag["n_items"], "items,", len(diag["skill_vector_axes"]), "ejes de habilidad")
    print("Exam mode: topic_questions unidades=", len(exam["topic_questions"]),
          " mixed=", len(exam["mixed_questions"]),
          " timed=", len(exam["timed_questions"]),
          " partial_mocks=", len(exam["partial_mock_exams"]),
          " full_mocks=", len(exam["full_mock_exams"]))
    for m in exam["partial_mock_exams"] + exam["full_mock_exams"]:
        print(" -", m["mock_id"], ":", len(m["items"]), "preguntas")

if __name__ == "__main__":
    main()
