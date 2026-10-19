# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")

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

for unit in ["cuantica", "nuclear"]:
    fp = os.path.join(BASE, f"selectividad_fisica__{unit}.json")
    d = json.load(open(fp, encoding="utf-8"))
    for bkey, lesson in d.items():
        hits=[]
        walk(lesson, f"{unit}/{bkey}", r"positr.n|aniquilaci.n|producci.n de pares|2mc", hits)
        for p,t in hits: print(p,'::', t[:200].replace(chr(10),' '))
