# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"solution": "$\\Delta H<0$ (exotérmica)",'''
new = r'''"solution": "(a) $\\Delta H<0$ (exotérmica), porque $K_c$ disminuye al aumentar $T$. (b) Al seguir subiendo $T$, el equilibrio se desplaza hacia reactivos y la cantidad de $HI$ disminuye.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
