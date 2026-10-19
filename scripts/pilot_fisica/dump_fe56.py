# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__nuclear.json")
d = json.load(open(fp, encoding="utf-8"))

l2 = d["02_Defecto_de_masa_y_energía_de_enlace_la_curva.json"]
print("L2 summary:", json.dumps(l2["summary"], ensure_ascii=False, indent=1))
print()
# find theory block mentioning maximo / curva binding energy per nucleon
for i,tb in enumerate(l2["theory_blocks"]):
    if "máximo" in tb.get("body","").lower() or "curva" in tb.get("title","").lower():
        print(i, tb.get("title"))
        print(tb["body"][:1200])
        print("---")
