# -*- coding: utf-8 -*-
"""
Fase 6a — Checkpoints por unidad.

Agrupa las lecciones de cada unidad de contenido (no Fundamentos) en
bloques de 2-5 lecciones consecutivas (segun el propio orden del bundle) y
construye un checkpoint por bloque, REUTILIZANDO ids de piezas ya existentes
(mcq de dificultad <=3 y un exercise por leccion), sin duplicar contenido:
el checkpoint es un indice de referencias (canonical_lesson_id + item id),
no una copia.

Umbral de resultado (needs_support/ready/mastered) declarado de forma
explicita y documentado en CHECKPOINTS.md: se basa en la proporcion de
items del checkpoint respondidos correctamente (dato que la UI tendria que
registrar; aqui se fija el umbral, no el resultado de un alumno real).
"""
import json, os, math

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear"]
BLOCK_SIZE = 3

def main():
    checkpoints = []
    for unit in UNITS:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        items = list(d.items())
        nblocks = math.ceil(len(items) / BLOCK_SIZE)
        for bi in range(nblocks):
            block_lessons = items[bi*BLOCK_SIZE:(bi+1)*BLOCK_SIZE]
            if not block_lessons:
                continue
            checkpoint_items = []
            lesson_ids = []
            for bkey, lesson in block_lessons:
                lesson_ids.append(lesson["schema_v2"]["canonical_lesson_id"])
                for mc in lesson.get("mcq", []):
                    if mc.get("difficulty", 3) <= 3 and mc.get("id"):
                        checkpoint_items.append({"ref_lesson": lesson["schema_v2"]["canonical_lesson_id"],
                                                  "item_type": "mcq", "item_id": mc["id"]})
                exs = lesson.get("exercises", [])
                if exs:
                    ex = min(exs, key=lambda e: e.get("difficulty", 3))
                    if ex.get("id"):
                        checkpoint_items.append({"ref_lesson": lesson["schema_v2"]["canonical_lesson_id"],
                                                  "item_type": "exercise", "item_id": ex["id"]})
            checkpoints.append({
                "checkpoint_id": f"CKPT-{unit}-{bi+1:02d}",
                "unit": unit,
                "covers_lessons": lesson_ids,
                "items": checkpoint_items,
                "n_items": len(checkpoint_items),
                "thresholds": {"needs_support": "<60% correcto", "ready": "60-85% correcto", "mastered": ">85% correcto"},
            })
    out_fp = os.path.join(PILOT, "unit_checkpoints.json")
    json.dump({"checkpoints": checkpoints}, open(out_fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Checkpoints generados: {len(checkpoints)}")
    from collections import Counter
    per_unit = Counter(c["unit"] for c in checkpoints)
    for u, n in per_unit.items():
        print(f"  {u}: {n} checkpoints")
    zero_item = [c["checkpoint_id"] for c in checkpoints if c["n_items"] == 0]
    print("Checkpoints sin items (revisar):", zero_item)

if __name__ == "__main__":
    main()
