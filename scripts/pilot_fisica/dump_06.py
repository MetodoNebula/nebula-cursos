# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["06_El_campo_magnético_un_campo_sin_fuentes.json"]
print("=== theory_blocks[5] ==="); print(json.dumps(l["theory_blocks"][5], ensure_ascii=False, indent=2))
print("=== misconceptions[0] ==="); print(json.dumps(l["misconceptions"][0], ensure_ascii=False, indent=2))
print("=== exam_notes[4] ==="); print(repr(l["exam_notes"][4]))
print("=== objectives[3] ==="); print(json.dumps(l["objectives"][3], ensure_ascii=False, indent=2))
print("=== summary ==="); print(json.dumps(l["summary"], ensure_ascii=False, indent=2))
print("=== theory_blocks count ===", len(l["theory_blocks"]))
