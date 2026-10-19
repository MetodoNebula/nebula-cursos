# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["10_El_campo_magnético_creado_por_corrientes.json"]

old1 = l["common_mistakes"][5]["how_to_avoid"]
bad_marker = "\\$\\vec"
if bad_marker in old1:
    new1 = ("Pensar en el material, no en la fórmula: el hierro es ferromagnético y sus dominios se "
            "alinean con el campo aplicado, reforzándolo; un dieléctrico lineal ordinario también se "
            "polariza alineándose con el campo —el vector polarización $\\vec P$ tiene el mismo sentido "
            "que $\\vec E$—, pero las cargas ligadas que aparecen en su superficie crean un campo de "
            "despolarización que se opone al campo externo y reduce el campo neto en su interior. La "
            "posición de la constante en la fórmula refleja ese comportamiento, no lo causa.")
    l["common_mistakes"][5]["how_to_avoid"] = new1
    print("fixed how_to_avoid (re-fix from botched escaping)")
else:
    print("how_to_avoid already clean, leaving as is:", old1[:80])

old2 = l["summary"]["key_points"][5]
if bad_marker in old2:
    new2 = ("**El medio**: el hierro es ferromagnético y sus dominios se alinean con el campo, "
            "reforzándolo; un dieléctrico lineal ordinario también se alinea con el campo —su vector "
            "polarización $\\vec P$ tiene el mismo sentido que $\\vec E$—, pero el campo que generan sus "
            "cargas ligadas (campo de despolarización) se opone al campo externo y reduce el campo neto. "
            "Por eso un núcleo de hierro refuerza el campo de una bobina y un dieléctrico, aunque se "
            "polarice, nunca refuerza un campo eléctrico.")
    l["summary"]["key_points"][5] = new2
    print("fixed key_points[5]")
else:
    print("key_points[5] already clean:", old2[:80])

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("saved", fp)
