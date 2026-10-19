# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["04_El_campo_gravitatorio_terrestre_variación_de_g.json"]
print("=== theory_blocks[0] ===")
print(l["theory_blocks"][0]["body"])
print()
print("=== theory_blocks[5] ===")
print(l["theory_blocks"][5]["body"])
print()
print("=== exercises[2] full ===")
print(json.dumps(l["exercises"][2], ensure_ascii=False, indent=2))
print()
print("=== objectives[2] ===", l["objectives"][2])
print("=== summary ===")
print(json.dumps(l["summary"], ensure_ascii=False, indent=2))
