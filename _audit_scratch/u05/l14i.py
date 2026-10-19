# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []
edits.append(("H10_G1", r'''"full_solution": "(a) $Q=[COCl_2]/([CO][Cl_2])$; al bajar bruscamente $[COCl_2]$, $Q$ disminuye por debajo de $K_c=100$. (b) Con $Q<K_c$, el sistema avanza hacia productos: se consume parte del $CO$ y del $Cl_2$ presentes para formar más $COCl_2$, oponiéndose parcialmente a la retirada (Le Châtelier).",''',
r'''"full_solution": "(a) $Q=[COCl_2]/([CO][Cl_2])$; al bajar bruscamente $[COCl_2]$, $Q$ disminuye por debajo de $K_c=100$.\n\n(b) Con $Q<K_c$, el sistema avanza hacia productos: se consume parte del $CO$ y del $Cl_2$ presentes para formar más $COCl_2$, oponiéndose parcialmente a la retirada (Le Châtelier).",'''
))
edits.append(("H10_G2", r'''"full_solution": "(a) Productos: 2 moles de gas. Reactivos: $1+3=4$ moles de gas. $\\Delta n=2-4=-2$. (b) Al duplicar $V$, el equilibrio se desplaza hacia el lado con más moles de gas, que aquí son los reactivos (4 frente a 2). El amoniaco formado se descompondría parcialmente en $N_2$ y $H_2$.",''',
r'''"full_solution": "(a) Productos: 2 moles de gas. Reactivos: $1+3=4$ moles de gas. $\\Delta n=2-4=-2$.\n\n(b) Al duplicar $V$, el equilibrio se desplaza hacia el lado con más moles de gas, que aquí son los reactivos (4 frente a 2). El amoniaco formado se descompondría parcialmente en $N_2$ y $H_2$.",'''
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
