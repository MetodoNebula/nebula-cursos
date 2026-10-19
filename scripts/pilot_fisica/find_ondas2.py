# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__ondas.json")
d = json.load(open(fp, encoding="utf-8"))

lesson11 = d["11_Ondas_estacionarias_la_onda_que_no_viaja.json"]
print("=== LESSON 11 theory_blocks titles ===")
for i,tb in enumerate(lesson11["theory_blocks"]):
    print(i, tb.get("title"))
print()
print("=== summary ===")
print(json.dumps(lesson11["summary"], ensure_ascii=False, indent=1)[:2000])
