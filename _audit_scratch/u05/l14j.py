# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []
edits.append(("H13_text", r'''"text": "no se desplaza, porque $\\Delta$n=0.",''',
r'''"text": "no se desplaza, porque $\\Delta n=0$.",'''
))
edits.append(("H13_whywrong", r'''"why_wrong": "$\\Delta n=(1+3)-2=+2$, no es cero: si hay efecto de presion/volumen en este equilibrio"''',
r'''"why_wrong": "$\\Delta n=(1+3)-2=+2$, no es cero: sí hay efecto de presión/volumen en este equilibrio."'''
))

results = []
ok_all = True
for label, old, new in edits:
    n = data.count(old)
    results.append((label, n))
    if n == 1:
        data = data.replace(old, new, 1)
    else:
        ok_all = False
for lb, cnt in results:
    print(lb, cnt)
if ok_all:
    open(PATH, "w", encoding="utf-8").write(data)
    print("ALL WRITTEN")
else:
    print("ABORT")
