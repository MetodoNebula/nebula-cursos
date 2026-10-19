# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"difficulty": 3,
        "marks": 4,
        "statement": "Para el equilibrio $\\mathrm{NH_4Cl(s)\\rightleftharpoons NH_3(g)+HCl(g)}$:'''
new = r'''"difficulty": 3,
        "marks": 6,
        "statement": "Para el equilibrio $\\mathrm{NH_4Cl(s)\\rightleftharpoons NH_3(g)+HCl(g)}$:'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
