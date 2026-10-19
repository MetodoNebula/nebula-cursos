# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
targets = [
    ("ondas", "05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json"),
    ("ondas", "11_Ondas_estacionarias_la_onda_que_no_viaja.json"),
    ("optica", "03_El_ángulo_límite_y_la_reflexión_total.json"),
    ("campo_gravitatorio", "02_La_ley_de_gravitación_universal.json"),
    ("cuantica", "06_Indeterminación_y_la_nueva_mecánica_cuántica.json"),
    ("electromagnetismo", "05_El_potencial_eléctrico_sumar_sin_vectores.json"),
]
for unit, bkey in targets:
    fp = os.path.join(BASE, f"selectividad_fisica__{unit}.json")
    d = json.load(open(fp, encoding="utf-8"))
    lesson = d.get(bkey)
    if lesson is None:
        print(unit, bkey, "NOT FOUND -- keys sample:", list(d.keys())[:3])
        continue
    print(f"=== {unit}/{bkey} ===")
    print("id:", lesson.get("id"), "title:", lesson.get("title"), "len:", lesson.get("estimated_length"))
    print("theory_blocks:", [(tb.get('id'), tb.get('type'), tb.get('title')) for tb in lesson.get("theory_blocks",[])])
    for cont in ["worked_examples","guided_exercises","exercises","exam_questions","challenge_questions","mcq","flashcards","misconceptions","common_mistakes","keywords","diagnostic_items"]:
        print(f"  {cont}: {len(lesson.get(cont,[]))}")
    print()
