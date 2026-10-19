# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__ondas.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["11_Ondas_estacionarias_la_onda_que_no_viaja.json"]
print(lesson["theory_blocks"][8]["body"])
print("---MISCONCEPTIONS---")
for m in lesson.get("misconceptions", []):
    print(json.dumps(m, ensure_ascii=False, indent=1))
