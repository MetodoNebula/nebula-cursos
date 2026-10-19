# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__cuantica.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["05_Dualidad_onda-corpúsculo_Compton_y_de_Broglie.json"]
for i in [3,4,9]:
    print(f"=== theory_blocks[{i}] ===")
    print(l["theory_blocks"][i]["body"])
    print()
print("=== objectives[3] ===", l["objectives"][3])
print("=== keywords[2] ===", l["keywords"][2])
print("=== keywords[3] ===", l["keywords"][3])
print("=== summary ===")
print(json.dumps(l["summary"], ensure_ascii=False, indent=2))
