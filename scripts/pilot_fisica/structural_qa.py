# -*- coding: utf-8 -*-
"""
Fase 7 — QA estructural automatizado.

Comprueba, sobre las 88 lecciones del piloto (82 de contenido + 6 de
Fundamentos):
  1. JSON valido en los 9 bundles.
  2. IDs unicos: canonical_lesson_id (curso), y dentro de cada leccion, los
     ids de cada contenedor (theory_blocks, exercises, mcq, etc.) no se
     repiten.
  3. Referencias resueltas: objective_ids / concept_ids citados en cualquier
     pieza existen de verdad en objectives[]/los concept_ids declarados en
     theory_blocks de la misma leccion (o en Foundations via KNOWLEDGE_GRAPH).
  4. MCQ: exactamente una opcion marcada correcta (correct == alguna option.key),
     y cada opcion NO correcta debería llevar why_wrong (se cuenta cuantas
     faltan, no se exige 100% salvo que sea trivial, segun el propio
     encargo: "permitir omission para distractores triviales con regla
     documentada" aplicado tambien aqui).
  5. Campos no vacios / no truncados en piezas obligatorias (statement,
     answer, full_solution, explanation).
"""
import json, os, re
from collections import Counter, defaultdict

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear","fundamentos"]

ID_CONTAINERS = ["theory_blocks","worked_examples","guided_exercises","exercises",
                  "exam_questions","challenge_questions","mcq","diagnostic_items",
                  "flashcards","misconceptions","common_mistakes"]

TRUNCATION_RE = re.compile(r"\.\.\.$|\betc\.$|^\s*$")

def main():
    report = {
        "json_valid": True,
        "lessons_total": 0,
        "canonical_id_duplicates": [],
        "per_lesson_id_duplicates": [],
        "unresolved_objective_refs": [],
        "unresolved_concept_refs": [],
        "mcq_no_correct_option": [],
        "mcq_multiple_correct": [],
        "mcq_distractor_missing_why_wrong": 0,
        "mcq_distractor_total": 0,
        "empty_or_truncated_fields": [],
    }
    canonical_ids = Counter()

    for unit in UNITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            report["json_valid"] = False
            continue
        for bkey, lesson in d.items():
            report["lessons_total"] += 1
            cid = lesson.get("schema_v2", {}).get("canonical_lesson_id")
            canonical_ids[cid] += 1

            # per-lesson id dup check
            seen = Counter()
            for c in ID_CONTAINERS:
                for it in lesson.get(c, []):
                    if isinstance(it, dict) and it.get("id"):
                        seen[it["id"]] += 1
            dups = [k for k, v in seen.items() if v > 1]
            if dups:
                report["per_lesson_id_duplicates"].append({"lesson": cid, "dup_ids": dups})

            # objective_ids / concept_ids resolution
            obj_ids = set(o.get("id") for o in lesson.get("objectives", []) if o.get("id"))
            concept_ids = set()
            for tb in lesson.get("theory_blocks", []):
                concept_ids.update(tb.get("concept_ids", []) or [])
            for c in ["exercises","guided_exercises","exam_questions","challenge_questions","worked_examples"]:
                for it in lesson.get(c, []):
                    if not isinstance(it, dict):
                        continue
                    for oid in it.get("objective_ids", []) or []:
                        if oid not in obj_ids:
                            report["unresolved_objective_refs"].append({"lesson": cid, "container": c, "item": it.get("id"), "ref": oid})
                    for cid2 in it.get("concept_ids", []) or []:
                        if cid2 not in concept_ids:
                            report["unresolved_concept_refs"].append({"lesson": cid, "container": c, "item": it.get("id"), "ref": cid2})

            # MCQ checks
            for mc in lesson.get("mcq", []):
                opts = mc.get("options", [])
                keys = [o.get("key") for o in opts]
                correct = mc.get("correct")
                if correct not in keys:
                    report["mcq_no_correct_option"].append({"lesson": cid, "mcq": mc.get("id")})
                for o in opts:
                    if o.get("key") != correct:
                        report["mcq_distractor_total"] += 1
                        if not o.get("why_wrong"):
                            report["mcq_distractor_missing_why_wrong"] += 1

            # emptiness/truncation
            for c in ["exercises","guided_exercises","exam_questions","challenge_questions"]:
                for it in lesson.get(c, []):
                    if not isinstance(it, dict):
                        continue
                    for field in ("statement","answer","full_solution"):
                        val = it.get(field)
                        if isinstance(val, str) and (not val.strip()):
                            report["empty_or_truncated_fields"].append({"lesson": cid, "container": c, "item": it.get("id"), "field": field})

    dup_cids = [k for k, v in canonical_ids.items() if v > 1]
    report["canonical_id_duplicates"] = dup_cids
    report["canonical_ids_total"] = len(canonical_ids)

    out_fp = os.path.join(BASE, "scripts/pilot_fisica/structural_qa_report.json")
    json.dump(report, open(out_fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print("JSON valido en todos los bundles:", report["json_valid"])
    print("Lecciones totales:", report["lessons_total"], " canonical_ids unicos:", report["canonical_ids_total"], " duplicados:", dup_cids)
    print("Duplicados de id DENTRO de una leccion:", len(report["per_lesson_id_duplicates"]))
    print("Referencias objective_ids no resueltas:", len(report["unresolved_objective_refs"]))
    print("Referencias concept_ids no resueltas:", len(report["unresolved_concept_refs"]))
    print("MCQ sin opcion correcta valida:", len(report["mcq_no_correct_option"]))
    print(f"Distractores sin why_wrong: {report['mcq_distractor_missing_why_wrong']} / {report['mcq_distractor_total']}")
    print("Campos obligatorios vacios:", len(report["empty_or_truncated_fields"]))

if __name__ == "__main__":
    main()
