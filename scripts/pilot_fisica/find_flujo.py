# -*- coding: utf-8 -*-
import json, re, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["12_El_flujo_magnético_y_qué_induce_corriente.json"]

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

hits = []
walk(l, "12", r"movimiento relativo|se mueva|moviendo|en reposo|reposo relativo|mover", hits)
for p, t in hits:
    print(p, "::", t[:350].replace("\n"," "))
    print("---")
