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

print("LESSONS:", list(d.keys()))
print("=== FE-56 / NI-62 / maximo energia enlace ===")
for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"Fe-?56|hierro.56|N[ií]quel.?62|Ni-?62|m[aá]ximo.{0,30}enlace|enlace.{0,30}m[aá]ximo", hits)
    for p,t in hits: print(p,'::', t[:220].replace(chr(10),' '))
print()
print("=== Z>83 / estabilidad / bismuto ===")
for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"Z\s*>\s*83|Bi-?209|bismuto|83 protones|estables.{0,20}83", hits)
    for p,t in hits: print(p,'::', t[:220].replace(chr(10),' '))
