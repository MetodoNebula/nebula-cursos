# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
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

print("=== rozamiento siempre ===")
for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"rozamiento", hits)
    for p,t in hits: print(p,'::', t[:200].replace(chr(10),' '))

print()
print("=== Kepler tercera ley T2 a3 / r3 ===")
l1 = d["01_Las_leyes_de_Kepler.json"]
hits=[]
walk(l1, "01", r"tercera ley|T\^2|T\^\{2\}|a\^3|a\^\{3\}|r\^3|r\^\{3\}", hits)
for p,t in hits: print(p,'::', t[:250].replace(chr(10),' '))
