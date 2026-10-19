# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__relatividad.json")
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

print("=== lesson07: sistemas inerciales / no sirve / aceleran ===")
l7 = d["07_La_gravedad_es_indistinguible_de_una_aceleración.json"]
hits=[]
walk(l7, "07", r"no existen sistemas inerciales|todos aceleran|no sirve|equivalencia", hits)
for p,t in hits: print(p,'::', t[:300].replace(chr(10),' '))

print()
print("=== lesson03: tiempo propio definicion ===")
l3 = d["03_Dilatación_del_tiempo_el_tiempo_propio.json"]
hits=[]
walk(l3, "03", r"tiempo propio|un evento en reposo", hits)
for p,t in hits: print(p,'::', t[:300].replace(chr(10),' '))
