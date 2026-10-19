# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__relatividad.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["07_La_gravedad_es_indistinguible_de_una_aceleración.json"]
print(l["theory_blocks"][0]["body"])
print()
print("=== theory_blocks[3] (campos no uniformes / localmente) ===")
print(l["theory_blocks"][3]["body"])
print()
print("=== keywords[3] ===", l["keywords"][3])
print("=== objectives[3] ===", l["objectives"][3])
