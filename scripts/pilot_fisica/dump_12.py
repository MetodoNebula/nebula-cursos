# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["12_El_flujo_magnético_y_qué_induce_corriente.json"]

print("=== objectives[5] ==="); print(json.dumps(l["objectives"][5], ensure_ascii=False, indent=2))
print("=== theory_blocks[7] ==="); print(json.dumps(l["theory_blocks"][7], ensure_ascii=False, indent=2))
print("=== keywords[4] ==="); print(json.dumps(l["keywords"][4], ensure_ascii=False, indent=2))
print("=== mcq[2] ==="); print(json.dumps(l["mcq"][2], ensure_ascii=False, indent=2))
print("=== mcq[4] ==="); print(json.dumps(l["mcq"][4], ensure_ascii=False, indent=2))
print("=== flashcards[8] ==="); print(json.dumps(l["flashcards"][8], ensure_ascii=False, indent=2))
print("=== summary ==="); print(json.dumps(l["summary"], ensure_ascii=False, indent=2))
