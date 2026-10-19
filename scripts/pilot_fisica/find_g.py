# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["04_El_campo_gravitatorio_terrestre_variación_de_g.json"]

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

hits=[]
walk(l, "04", r"caída libre|a\s*=\s*g|g_?m.x|g máxima|máxim.{0,10}superficie", hits)
for p,t in hits: print(p,'::', t[:250].replace(chr(10),' '))
