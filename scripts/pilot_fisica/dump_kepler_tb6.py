# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["01_Las_leyes_de_Kepler.json"]
print(l["theory_blocks"][6]["body"])
print()
print("keywords[2]:", l["keywords"][2])
