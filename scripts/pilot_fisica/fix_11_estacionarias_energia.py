# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__ondas.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["11_Ondas_estacionarias_la_onda_que_no_viaja.json"]

old = lesson["summary"]["key_points"][5]
assert old == "**No transporta energía** porque un nodo no se mueve y no puede hacer trabajo sobre su vecino. La energía queda en cada huso, pasando de cinética a potencial elástica dos veces por periodo.", repr(old)
new = ("**No transporta energía:** la onda incidente lleva energía hacia la frontera y la reflejada la devuelve con la misma intensidad, de modo que el flujo neto medio de energía es cero en todo punto (superposición de dos ondas viajeras opuestas). "
       "De forma equivalente, un nodo no se mueve y no puede hacer trabajo sobre su vecino, así que la energía no cruza esos puntos. La energía queda en cada huso, pasando de cinética a potencial elástica dos veces por periodo.")
lesson["summary"]["key_points"][5] = new

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK saved")
