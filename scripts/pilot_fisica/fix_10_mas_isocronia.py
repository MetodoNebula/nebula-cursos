# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__mas.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["01_Movimientos_periódicos_oscilatorios_y_vibratorios.json"]

old = lesson["objectives"][5]["statement"]
assert old == "Enunciar la **isocronía** (el periodo no depende de la amplitud) como propiedad observada, sabiendo que se demostrará al estudiar la dinámica del oscilador.", repr(old)
new = "Enunciar la **isocronía** (el periodo no depende de la amplitud, propia del oscilador armónico/MAS y de las pequeñas oscilaciones) como propiedad observada, sabiendo que se demostrará al estudiar la dinámica del oscilador."
lesson["objectives"][5]["statement"] = new

old2 = lesson["summary"]["key_points"][5]
assert old2 == "**Isocronía:** el periodo no depende de la amplitud. Se acepta ahora como hecho observado y se demostrará al estudiar la dinámica del oscilador.", repr(old2)
new2 = "**Isocronía (oscilador armónico / MAS, pequeñas oscilaciones):** el periodo no depende de la amplitud. Es una propiedad del modelo MAS, no de cualquier oscilación; se acepta ahora como hecho observado y se demostrará al estudiar la dinámica del oscilador."
lesson["summary"]["key_points"][5] = new2

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK saved")
