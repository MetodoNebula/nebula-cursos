# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["07_Conservación_de_la_energía_mecánica_en_el_campo.json"]
print(l["theory_blocks"][4]["body"])
print("\n=== n theory_blocks ===", len(l["theory_blocks"]))
print("\n=== objectives[2] ===", l["objectives"][2])
print("\n=== summary.key_points[3] ===", l["summary"]["key_points"][3])
print("\n=== flashcards[3] ===", l["flashcards"][3])
