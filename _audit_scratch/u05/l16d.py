# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H6_flashcard10", r'''"back": "Que la sal es muy poco soluble: se necesita muy poca concentración de iones para alcanzar el equilibrio de solubilidad.",''',
r'''"back": "Que la sal es muy poco soluble: se necesita muy poca concentración de iones para alcanzar el equilibrio de solubilidad. Pero para comparar dos sales esto solo vale si son del mismo tipo estequiométrico (AB con AB, AB2 con AB2); si no, hay que calcular s.",'''
))

edits.append(("H7_diag2", r'''"answer": "x = 8×10⁻¹⁰ / 4 = 2×10⁻¹⁰, sin raíz cúbica",''',
r'''"answer": "$x=8\\times10^{-10}$ (se queda en $x^3$ sin extraer la raíz cúbica)",'''
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
