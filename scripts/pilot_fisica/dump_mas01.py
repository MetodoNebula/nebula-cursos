# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__mas.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["01_Movimientos_periódicos_oscilatorios_y_vibratorios.json"]
print("OBJECTIVES:")
for o in lesson["objectives"]:
    print(" -", o.get("statement"))
print()
print("THEORY_BLOCKS[5] FULL BODY:")
print(lesson["theory_blocks"][5]["body"])
print()
print("SUMMARY key_points:")
for kp in lesson["summary"]["key_points"]:
    print(" -", kp)
