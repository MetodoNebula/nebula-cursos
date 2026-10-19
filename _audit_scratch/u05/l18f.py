# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H6_mcq_optC", r'''"text": "sumar 0,050 directamente a Ksp antes de calcular la raíz.",
            "misconception_id": null,
            "why_wrong": "Esta operación no corresponde a ningún paso correcto del planteamiento algebraico de Ksp=s'(C+s')."''',
r'''"text": "aproximar $[Ag^+]\\approx0{,}050$ M (confundiendo el ion común con el ion cuya concentración se busca) y despejar $[Cl^-]$ en vez de $s'$.",
            "misconception_id": null,
            "why_wrong": "Confunde qué ion es el común (el que ya está en la disolución) con el ion cuya concentración de equilibrio se pide; hay que despejar $s'$ de $K_{sp}=s'(C+s')$, no asumir que el ion común es la incógnita."'''
))

edits.append(("H9_misconception0", r'''"correct_model": "Ksp no cambia (depende solo de T), pero la solubilidad molar s' en presencia de ion común sí disminuye: para disolver la misma cantidad de Ksp con una concentración ya más alta de uno de los iones, hace falta menos del otro ion, es decir, se disuelve menos sal.",''',
r'''"correct_model": "$K_{sp}$ no cambia (depende solo de $T$), pero la solubilidad molar $s'$ en presencia de ion común sí disminuye: para que el producto de concentraciones siga valiendo $K_{sp}$ con una concentración ya más alta de uno de los iones, la concentración del otro ion tiene que ser menor, es decir, se disuelve menos sal.",'''
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
