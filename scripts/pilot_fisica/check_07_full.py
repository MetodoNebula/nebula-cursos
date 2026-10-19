# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__relatividad.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["07_La_gravedad_es_indistinguible_de_una_aceleración.json"]

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
walk(l, "07", r"no sirve|inútil|no sirve para nada|deja de valer la relatividad especial|relatividad especial.{0,40}no", hits)
for p,t in hits: print(p,'::', t[:250].replace(chr(10),' '))
print("checked, count:", len(hits))
print()
print("theory_blocks[1]:")
print(l["theory_blocks"][1]["body"])
