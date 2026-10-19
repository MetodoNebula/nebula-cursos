# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"Solo NaHCO3 (reactivo) es sólido junto con Na2CO3 (producto); H2O y CO2 son gaseosos aquí.",'''
new = r'''"$NaHCO_3$ (reactivo) y $Na_2CO_3$ (producto) son sólidos; $H_2O$ y $CO_2$ son gaseosos aquí.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
