# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"text": "-1, invirtiendo el signo por error.",
            "misconception_id": null,
            "why_wrong": "No corresponde a ningún conteo correcto de especies'''
new = r'''"text": "+3, contando $NaHCO_3(s)$ como 0 pero $Na_2CO_3$, $H_2O$ y $CO_2$ los tres como gases.",
            "misconception_id": null,
            "why_wrong": "$Na_2CO_3$ es sólido, no gaseoso: no debe contarse en el lado de productos para Δn, aunque sí se tache en la expresión de Kc/Kp. No corresponde a ningún conteo correcto de especies'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
