# -*- coding: utf-8 -*-
import json, os
from collections import Counter
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear","fundamentos"]

canonical_ids = Counter()
errors = []
for u in UNITS:
    fp = os.path.join(BASE, f"selectividad_fisica__{u}.json")
    try:
        d = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        errors.append(f"{u}: JSON INVALID: {e}")
        continue
    for bkey, lesson in d.items():
        sv2 = lesson.get("schema_v2")
        if not sv2:
            errors.append(f"{u}/{bkey}: missing schema_v2")
            continue
        cid = sv2.get("canonical_lesson_id")
        canonical_ids[cid] += 1
        if not sv2.get("objectives"):
            errors.append(f"{u}/{bkey}: schema_v2 has no objectives")
        routes = sv2["learning_design"]["recommended_routes"]
        for r in ("from_zero","standard","excellence","quick_review"):
            if not isinstance(routes.get(r), list):
                errors.append(f"{u}/{bkey}: route {r} malformed")

dupes = [cid for cid, n in canonical_ids.items() if n > 1]
print("Total canonical_lesson_id:", len(canonical_ids))
print("Duplicates:", dupes)
print("Errors:", len(errors))
for e in errors[:30]:
    print(" -", e)
print("JSON VALID for all 8 bundles:", not any("INVALID" in e for e in errors))
