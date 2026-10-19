# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__nuclear.json")
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
    walk(lesson, bkey, r"Bi(smuto)?[-\s]?209|\bBi\b", hits)
    for p,t in hits: print(p,'::', t[:250].replace(chr(10),' '))

print()
print("=== lesson02 exercises[4] full ===")
lesson = d["02_Defecto_de_masa_y_energía_de_enlace_la_curva.json"]
print(json.dumps(lesson["exercises"][4], ensure_ascii=False, indent=1)[:3000])
