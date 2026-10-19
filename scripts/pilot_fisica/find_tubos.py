# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__ondas.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["12_Armónicos_cuerdas_tubos_y_el_timbre.json"]
print("THEORY_BLOCKS titles:")
for i,tb in enumerate(lesson["theory_blocks"]):
    print(i, tb.get("title"))
    if "tubo" in tb.get("title","").lower() or "abierto" in tb.get("title","").lower() or "cerrado" in tb.get("title","").lower():
        print("   BODY:", tb["body"][:1500])
        for a in tb.get("assets", []):
            print("   ASSET caption:", a.get("caption","")[:400])
