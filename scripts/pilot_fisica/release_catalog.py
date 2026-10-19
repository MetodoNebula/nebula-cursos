# -*- coding: utf-8 -*-
"""
Fase 8 — Release: sustituye la entrada "selectividad_fisica" de catalog.json
y los bundles/selectividad_fisica__*.json por la version validada del
piloto, SIN TOCAR ningun otro curso del catalogo ni de bundles/.

catalog.json y bundles/ NO estan versionados en git (.gitignore los excluye
a proposito: son el contenido en claro que solo vive en el servidor/maquina
local, la version publicada va cifrada via cifrar.js). Por eso este script
vive en scripts/ (si se versiona) y se ejecuta para regenerar esos ficheros
locales; no se commitea su salida.
"""
import json, os, re
from collections import Counter

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
BUNDLES = os.path.join(BASE, "bundles")
CATALOG_FP = os.path.join(BASE, "catalog.json")

UNIT_ORDER = ["fundamentos","campo_gravitatorio","mas","ondas","electromagnetismo",
              "optica","relatividad","cuantica","nuclear"]
UNIT_TITLES = {
    "fundamentos": "fis fundamentos (remediación)",
    "campo_gravitatorio": "fis campo gravitatorio",
    "mas": "fis mas",
    "ondas": "fis ondas",
    "electromagnetismo": "fis electromagnetismo",
    "optica": "fis óptica",
    "relatividad": "fis relatividad",
    "cuantica": "fis cuántica",
    "nuclear": "fis nuclear",
}
PIECE_TYPES = ["objectives","prerequisites","diagnostic_items","theory_blocks","keywords",
               "worked_examples","guided_exercises","exercises","exam_questions",
               "challenge_questions","mcq","flashcards","misconceptions","common_mistakes","exam_notes"]

def lesson_counts(lesson):
    return {pt: len(lesson.get(pt, [])) if isinstance(lesson.get(pt, []), list) else 0 for pt in PIECE_TYPES}

def natural_key(bkey):
    m = re.match(r"(\d+)", bkey)
    base = int(m.group(1)) if m else 999
    suffix = bkey[len(m.group(1)):] if m else bkey
    return (base, suffix)

def main():
    totals = Counter()
    units_out = []
    for unit in UNIT_ORDER:
        fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
        d = json.load(open(fp, encoding="utf-8"))
        bundle_rel = f"bundles/selectividad_fisica__{unit}.json"
        lecciones = []
        ordered_bkeys = sorted(d.keys(), key=natural_key)
        for n, bkey in enumerate(ordered_bkeys, start=1):
            lesson = d[bkey]
            counts = lesson_counts(lesson)
            for pt, c in counts.items():
                totals[pt] += c
            lecciones.append({
                "n": n,
                "titulo": lesson.get("title"),
                "dificultad": lesson.get("estimated_difficulty"),
                "duracion": lesson.get("estimated_length"),
                "contenido": counts,
                "bundle": bundle_rel,
                "bkey": bkey,
            })
        units_out.append({"id": unit, "titulo": UNIT_TITLES[unit], "lang": "es", "lecciones": lecciones})
        # copy the validated pilot bundle into bundles/ (overwrite only this course's files)
        out_bundle_fp = os.path.join(BUNDLES, f"selectividad_fisica__{unit}.json")
        json.dump(d, open(out_bundle_fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    total_lecciones = sum(len(u["lecciones"]) for u in units_out)
    total_piezas = sum(totals.values())

    catalog = json.load(open(CATALOG_FP, encoding="utf-8"))
    replaced = False
    for i, p in enumerate(catalog["projects"]):
        if p.get("key") == "selectividad_fisica":
            catalog["projects"][i] = {
                "key": "selectividad_fisica",
                "label": p.get("label", "Física"),
                "group": p.get("group", "Selectividad"),
                "motor": p.get("motor", "8.3.0"),
                "total": {"lecciones": total_lecciones, "piezas": total_piezas, "por_tipo": dict(totals)},
                "units": units_out,
            }
            replaced = True
            break
    if not replaced:
        raise SystemExit("No se encontro la entrada selectividad_fisica en catalog.json")

    json.dump(catalog, open(CATALOG_FP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"catalog.json actualizado: {total_lecciones} lecciones, {total_piezas} piezas, {len(units_out)} unidades")
    for u in units_out:
        print(f"  {u['id']}: {len(u['lecciones'])} lecciones")

if __name__ == "__main__":
    main()
