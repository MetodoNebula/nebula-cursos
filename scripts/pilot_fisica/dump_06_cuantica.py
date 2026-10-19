# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__cuantica.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["06_Indeterminación_y_la_nueva_mecánica_cuántica.json"]
print("=== objectives[1] ==="); print(json.dumps(l["objectives"][1], ensure_ascii=False, indent=2))
print("=== theory_blocks[1] ==="); print(l["theory_blocks"][1]["body"])
print("=== worked_examples[2] ==="); print(json.dumps(l["worked_examples"][2], ensure_ascii=False, indent=2))
print("=== mcq[5] ==="); print(json.dumps(l["mcq"][5], ensure_ascii=False, indent=2))
print("=== flashcards[2] ==="); print(json.dumps(l["flashcards"][2], ensure_ascii=False, indent=2))
print("=== summary ==="); print(json.dumps(l["summary"], ensure_ascii=False, indent=2))
