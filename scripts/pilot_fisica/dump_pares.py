# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__relatividad.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["05_La_energía_en_reposo_E_0mc2.json"]
print("=== theory_blocks[9] ==="); print(l["theory_blocks"][9]["body"])
print()
print("=== challenge_questions[0] ==="); print(json.dumps(l["challenge_questions"][0], ensure_ascii=False, indent=2))
print()
print("=== keywords[6] ==="); print(l["keywords"][6])
print("=== flashcards[8] ==="); print(l["flashcards"][8])
print("=== common_mistakes[4] ==="); print(l["common_mistakes"][4])
