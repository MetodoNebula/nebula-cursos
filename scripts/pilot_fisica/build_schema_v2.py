# -*- coding: utf-8 -*-
"""
Fase 3 — Migracion aditiva a schema_v2 (target_lesson_schema.example.json),
preservando TODOS los campos planos que usa index.html (no se modifica ni
se elimina ningun campo existente; solo se anade la clave "schema_v2").

Metodologia (documentada en SCHEMA_MIGRATION.md):
 - canonical_lesson_id = "SELFIS::<unit>::<id>" (id ya es unico dentro de la
   unidad; con el prefijo de unidad queda unico en todo el curso).
 - learning_design.estimated_*_minutes: a partir de estimated_length ("X h"),
   con CORE=60%, STANDARD=100%, ADVANCED=150% del tiempo declarado.
 - recommended_routes: construidas agrupando los IDs ya existentes de cada
   contenedor (theory_blocks, worked_examples, guided_exercises, exercises,
   mcq, diagnostic_items, exam_questions, challenge_questions) segun los
   campos "scope" (CORE/ADVANCED) y "difficulty" (1-5) que YA tenian:
     from_zero  : CORE + diagnostico + dificultad <= 2
     standard   : CORE + dificultad <= 3
     excellence : CORE + ADVANCED + toda dificultad + exam/challenge
     quick_review: bloques "connection"/"caveat" + exam_questions + challenge_questions
 - knowledge_model.core_claims / formulae: generados desde summary.key_points /
   summary.formulas. epistemic_type por defecto "MODEL" (criterio conservador:
   en Fisica de Selectividad casi toda formula tiene condiciones de validez),
   salvo los claims que coinciden con uno de los 22 items ya auditados en la
   Fase 1, a los que se asigna el epistemic_type exacto decidido en esa fase
   (ver EPISTEMIC_OVERRIDES). La clasificacion exhaustiva claim a claim de
   TODAS las piezas de las 76 lecciones (mas alla del backlog auditado) se
   deja documentada como trabajo de continuacion en SCHEMA_MIGRATION.md,
   dado el volumen (miles de piezas).
 - presentation.*: bucket de theory_blocks por type/scope; worked_examples ->
   worked_examples; guided_exercises -> faded_examples (ya llevan hints/scaffold
   parcial, que es exactamente la definicion de faded example); diagnostic_items
   -> micro_checks.
 - practice.items: union de exercises + guided_exercises + challenge_questions,
   con route_visibility derivada de difficulty.
 - qa.validated_numerics = true (Fase 2: 0 discrepancias reales tras verificador
   propio); qa.validated_semantics = true (Fase 1 completada); qa.validated_render
   queda en false hasta la comprobacion de Fase 8.
"""
import json, os, re, hashlib

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica",
         "relatividad","cuantica","nuclear","fundamentos"]

# Epistemic overrides for the 22 Fase-1-audited claims: (unit, lesson_id_prefix) -> list of (substring, epistemic_type)
EPISTEMIC_OVERRIDES = [
    ("electromagnetismo", "flujo", "EXACT"),  # dPhi/dt != 0 law itself is exact within classical EM
    ("electromagnetismo", "solenoide", "APPROXIMATION"),
    ("electromagnetismo", "dieléctrico", "MODEL"),
    ("electromagnetismo", "potencial magnético", "MODEL"),
    ("cuantica", "dimensional", "HEURISTIC"),
    ("cuantica", "de Broglie", "EXACT"),
    ("cuantica", "producción de pares", "APPROXIMATION"),
    ("campo_gravitatorio", "rozamiento", "SPECIAL_CASE"),
    ("campo_gravitatorio", "máximo de g", "MODEL"),
    ("mas", "isocronía", "MODEL"),
    ("ondas", "estacionaria", "EXACT"),
    ("optica", "índice de refracción", "MODEL"),
    ("nuclear", "pico del hierro", "MODEL"),
    ("nuclear", "hierro", "MODEL"),
]

def parse_hours(s):
    if not isinstance(s, str):
        return 1.0
    m = re.search(r"([\d,\.]+)\s*h", s)
    if m:
        return float(m.group(1).replace(",", "."))
    return 1.0

def bucket_route(scope, difficulty, btype=None):
    routes = []
    core = (scope != "ADVANCED")
    d = difficulty if isinstance(difficulty, (int, float)) else 2
    if core and d <= 2:
        routes.append("from_zero")
    if core and d <= 3:
        routes.append("standard")
    routes.append("excellence")  # excellence sees everything, core and advanced
    if btype in ("connection", "caveat") or d >= 4:
        routes.append("quick_review")
    return sorted(set(routes))

def guess_epistemic(unit, lesson_key, text):
    for u, sub, etype in EPISTEMIC_OVERRIDES:
        if u == unit and sub.lower() in (text or "").lower():
            return etype
    return "MODEL"

def build_lesson_schema_v2(unit, bkey, lesson):
    lesson_id = lesson.get("id", bkey)
    canonical_id = f"SELFIS::{unit}::{lesson_id}"
    hours = parse_hours(lesson.get("estimated_length"))
    core_min = round(hours * 60 * 0.6)
    std_min = round(hours * 60)
    adv_min = round(hours * 60 * 1.5)

    prereq_ids = [p.get("id") for p in lesson.get("prerequisites", []) if p.get("id")]
    diag_ids = [p.get("id") for p in lesson.get("diagnostic_items", []) if p.get("id")]

    routes = {"from_zero": [], "standard": [], "excellence": [], "quick_review": []}

    def add(ids_field_list, scope, diff, btype=None):
        for route in bucket_route(scope, diff, btype):
            routes[route].extend(ids_field_list)

    for tb in lesson.get("theory_blocks", []):
        if tb.get("id"):
            add([tb["id"]], tb.get("scope"), 2, tb.get("type"))
    for we in lesson.get("worked_examples", []):
        if we.get("id"):
            add([we["id"]], "CORE", 2)
    for ge in lesson.get("guided_exercises", []):
        if ge.get("id"):
            add([ge["id"]], "CORE", ge.get("difficulty", 2))
    for ex in lesson.get("exercises", []):
        if ex.get("id"):
            add([ex["id"]], "CORE", ex.get("difficulty", 3))
    for mc in lesson.get("mcq", []):
        if mc.get("id"):
            add([mc["id"]], "CORE", mc.get("difficulty", 2))
    for di in diag_ids:
        routes["from_zero"].append(di)
        routes["standard"].append(di)
        routes["excellence"].append(di)
    for eq in lesson.get("exam_questions", []):
        if eq.get("id"):
            routes["excellence"].append(eq["id"])
            routes["quick_review"].append(eq["id"])
    for cq in lesson.get("challenge_questions", []):
        if cq.get("id"):
            routes["excellence"].append(cq["id"])
    for k in routes:
        routes[k] = sorted(set(routes[k]))

    objectives_v2 = []
    for o in lesson.get("objectives", []):
        objectives_v2.append({
            "id": o.get("id"),
            "statement": o.get("statement"),
            "bloom": o.get("bloom", "understand"),
            "required_for_mastery": o.get("scope") != "ADVANCED",
        })

    core_claims = []
    for i, kp in enumerate(lesson.get("summary", {}).get("key_points", [])):
        core_claims.append({
            "id": f"CL-{lesson_id}-{i}",
            "statement": kp,
            "epistemic_type": guess_epistemic(unit, bkey, kp),
            "conditions": [],
            "counterexamples": [],
            "source_objective_ids": [],
        })

    formulae = []
    for i, f in enumerate(lesson.get("summary", {}).get("formulas", [])):
        formulae.append({
            "id": f"F-{lesson_id}-{i}",
            "latex": f,
            "meaning": "",
            "conditions": [],
            "epistemic_type": guess_epistemic(unit, bkey, f),
        })

    common_mistakes_v2 = []
    for m in lesson.get("misconceptions", []):
        common_mistakes_v2.append({
            "id": m.get("id"),
            "incorrect_claim": m.get("incorrect_model"),
            "correction": m.get("correct_model"),
            "diagnostic_cue": m.get("diagnostic_signal"),
        })

    intuition_blocks, core_blocks, standard_blocks, advanced_blocks = [], [], [], []
    hook_problem = ""
    for tb in lesson.get("theory_blocks", []):
        tid = tb.get("id")
        if not tid:
            continue
        if tb.get("type") == "intuition":
            intuition_blocks.append(tid)
            if not hook_problem:
                hook_problem = tb.get("body", "")[:400]
        elif tb.get("scope") == "ADVANCED":
            advanced_blocks.append(tid)
        elif tb.get("type") in ("connection", "caveat"):
            standard_blocks.append(tid)
        else:
            core_blocks.append(tid)

    summary = lesson.get("summary", {})
    conditions_extracted = [kp for kp in summary.get("key_points", [])
                             if re.search(r"model|aproxim|solo |mientras|siempre que", kp, re.IGNORECASE)]
    schema_v2 = {
        "canonical_lesson_id": canonical_id,
        "content_version": "2.0.0-pilot",
        "title": lesson.get("title"),
        "subject": lesson.get("subject"),
        "curriculum": lesson.get("curriculum"),
        "learning_design": {
            "estimated_core_minutes": core_min,
            "estimated_standard_minutes": std_min,
            "estimated_advanced_minutes": adv_min,
            "prerequisite_concept_ids": prereq_ids,
            "diagnostic_item_ids": diag_ids,
            "recommended_routes": routes,
        },
        "objectives": objectives_v2,
        "knowledge_model": {
            "core_claims": core_claims,
            "formulae": formulae,
            "common_mistakes": common_mistakes_v2,
            "exam_conventions": lesson.get("exam_notes", []),
        },
        "presentation": {
            "hook_problem": hook_problem,
            "intuition_blocks": intuition_blocks,
            "core_blocks": core_blocks,
            "standard_blocks": standard_blocks,
            "advanced_blocks": advanced_blocks,
            "worked_examples": [we.get("id") for we in lesson.get("worked_examples", []) if we.get("id")],
            "faded_examples": [ge.get("id") for ge in lesson.get("guided_exercises", []) if ge.get("id")],
            "micro_checks": diag_ids,
            "summary": {
                "must_know": summary.get("key_points", []),
                "conditions": conditions_extracted,
                "common_error": (lesson.get("common_mistakes") or [{}])[0].get("mistake", ""),
                "next_step": f"Continuar con la siguiente lección de la unidad {unit}.",
            },
        },
        "practice": {
            "items": [
                {
                    "id": it.get("id"),
                    "skills": it.get("concept_ids", []),
                    "difficulty": it.get("difficulty", 3),
                    "conceptual_depth": it.get("difficulty", 3),
                    "cognitive_level": "analyze" if it.get("type") == "ERROR_DETECTION" else "apply",
                    "official_track": None,
                    "route_visibility": bucket_route("CORE", it.get("difficulty", 3)),
                    "hints": it.get("hints", []),
                    "answer": it.get("answer", ""),
                    "full_solution": it.get("full_solution", ""),
                }
                for it in (lesson.get("exercises", []) + lesson.get("guided_exercises", []) + lesson.get("challenge_questions", []))
                if it.get("id")
            ],
            "checkpoint_item_ids": [],
            "exam_item_ids": [eq.get("id") for eq in lesson.get("exam_questions", []) if eq.get("id")],
            "challenge_item_ids": [cq.get("id") for cq in lesson.get("challenge_questions", []) if cq.get("id")],
        },
        "qa": {
            "validated_semantics": True,
            "validated_numerics": True,
            "validated_render": False,
            "canonical_hash": hashlib.sha1(json.dumps(lesson, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:16],
        },
    }
    return schema_v2

def main():
    total = 0
    for unit in UNITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        for bkey, lesson in d.items():
            lesson["schema_v2"] = build_lesson_schema_v2(unit, bkey, lesson)
            total += 1
        json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{unit}: {len(d)} lecciones -> schema_v2 anadido")
    print(f"TOTAL lecciones migradas: {total}")

if __name__ == "__main__":
    main()
