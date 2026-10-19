# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__nuclear.json")
d = json.load(open(fp, encoding="utf-8"))
lesson = d["02_Defecto_de_masa_y_energía_de_enlace_la_curva.json"]

old = lesson["summary"]["key_points"][4]
assert old == "**La estabilidad la mide $E_e/A$, no $E_e$.** El $^{56}\\mathrm{Fe}$ es el máximo, con $8{,}79$ MeV por nucleón.", repr(old)
new = "**La estabilidad la mide $E_e/A$, no $E_e$.** El máximo de la curva está en la región hierro-níquel ($A\\approx56$–$62$, pico del hierro); el $^{56}\\mathrm{Fe}$ (8,79 MeV/nucleón) está prácticamente en la cima, pero el valor más alto de todos corresponde al $^{62}\\mathrm{Ni}$."
lesson["summary"]["key_points"][4] = new

old2 = lesson["summary"]["what_to_remember_if_nothing_else"]
assert old2 == "La masa que falta no se pierde: es la energía de enlace. Y lo que mide la estabilidad es esa energía **dividida entre el número de nucleones**, cuyo máximo está en el hierro-56.", repr(old2)
new2 = "La masa que falta no se pierde: es la energía de enlace. Y lo que mide la estabilidad es esa energía **dividida entre el número de nucleones**, cuyo máximo está en la región hierro-níquel (el \"pico del hierro\"), con el $^{56}\\mathrm{Fe}$ muy cerca de la cima y el $^{62}\\mathrm{Ni}$ como el valor más alto."
lesson["summary"]["what_to_remember_if_nothing_else"] = new2

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK saved")
