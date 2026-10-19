# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H1_answer", r'''"answer": "Porque permiten alcanzar el mismo rendimiento de equilibrio en mucho menos tiempo, lo que es crucial económicamente a escala industrial.",''',
r'''"answer": "Porque permiten alcanzar el mismo rendimiento de equilibrio en mucho menos tiempo; además, en reacciones exotérmicas como la síntesis de amoniaco, permiten trabajar a una temperatura más baja (mejor rendimiento) con una velocidad todavía aceptable.",'''
))

edits.append(("H1_fullsol", r'''"full_solution": "Un catalizador no cambia el rendimiento final (la posición de equilibrio es la misma), pero sí reduce drásticamente el tiempo necesario para alcanzarlo. A escala industrial, ese ahorro de tiempo —y por tanto de energía y coste— es la razón real para usar catalizadores, no un supuesto aumento del rendimiento.",''',
r'''"full_solution": "Un catalizador no cambia el rendimiento final (la posición de equilibrio es la misma), pero sí reduce drásticamente el tiempo necesario para alcanzarlo. A escala industrial, ese ahorro de tiempo —y por tanto de energía y coste— es una razón real para usar catalizadores. Además, en la síntesis de $NH_3$ ($\\Delta H<0$) el rendimiento de equilibrio es mayor a baja temperatura, pero ahí la reacción es lentísima; el catalizador (Fe) permite trabajar a temperaturas moderadas ($\\approx400\\text{-}450\\,^{\\circ}\\mathrm{C}$) con una velocidad aceptable: no cambia $K$ a una $T$ dada, pero permite elegir una $T$ más baja —con mejor rendimiento— de la que sería viable sin él.",'''
))

edits.append(("H1_flashcard", r'''"back": "Porque reducen drásticamente el tiempo (y el coste energético) necesario para alcanzar el mismo rendimiento de equilibrio.",''',
r'''"back": "Porque reducen drásticamente el tiempo (y el coste energético) necesario para alcanzar el mismo rendimiento de equilibrio, y además permiten operar a una temperatura más baja (mejor rendimiento en reacciones exotérmicas) con una velocidad aceptable.",'''
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
