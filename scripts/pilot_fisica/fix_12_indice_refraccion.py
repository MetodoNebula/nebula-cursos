# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__optica.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["02_El_índice_de_refracción_y_la_ley_de_Snell.json"]

target = None
for k in lesson["keywords"]:
    if k.get("term") == "Índice de refracción":
        target = k
        break
assert target is not None
old = target["definition"]
assert old == "Cociente $n=c/v$ entre la velocidad de la luz en el vacío y su velocidad en el medio. Adimensional y siempre $\\ge1$.", repr(old)
new = "Cociente $n=c/v$ entre la velocidad de la luz en el vacío y su velocidad en el medio. Adimensional; en los medios transparentes ordinarios que se manejan en este curso (vidrio, agua, aire...) vale siempre $\\ge1$, porque $v\\le c$. (Es una propiedad del modelo de medio ordinario, no una ley universal: existen medios artificiales y regímenes especiales en que no se cumple, fuera del temario.)"
target["definition"] = new

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK saved")
