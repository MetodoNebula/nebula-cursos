# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__optica.json")
d = json.load(open(fp, encoding="utf-8"))

def walk(obj, path, pattern, hits):
    if isinstance(obj, str):
        if re.search(pattern, obj, re.IGNORECASE):
            hits.append((path, obj))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, path + "." + k, pattern, hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, path + f"[{i}]", pattern, hits)

for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"siempre.{0,15}mayor que 1|n\s*(>|≥|\\geq)\s*1|índice.{0,20}nunca|jamás menor", hits)
    for p,t in hits: print(p,'::', t[:200].replace(chr(10),' '))

lesson = d["02_El_índice_de_refracción_y_la_ley_de_Snell.json"]
print("--- lesson02 keywords ---")
for k in lesson.get("keywords", []):
    if "índice" in k.get("term","").lower():
        print(k["term"], '::', k["definition"][:300])
