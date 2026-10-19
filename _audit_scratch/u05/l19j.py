# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H12_mcq4D", r'''"text": "Su concentración varía demasiado rápido para medirla.",
            "misconception_id": null,
            "why_wrong": "No es un problema de medición: la actividad de una fase pura es, por definición, constante e igua''',
r'''"text": "Su densidad es mucho mayor que la de los gases.",
            "misconception_id": null,
            "why_wrong": "La densidad no tiene nada que ver con la razón por la que no aparece en K: la actividad de una fase pura es, por definición, constante e igua'''
))

edits.append(("H12_mcq1C", r'''"text": "Ksp solo se aplica cuando no hay ningún sólido en el equilibrio.",
            "misconception_id": null,
            "why_wrong": "Al contrario: Ksp se define precisamente para equilibrios que SÍ tienen un sólido puro presente."''',
r'''"text": "Ksp incluye la concentración del sólido elevada a su coeficiente, igual que Kc.",
            "misconception_id": null,
            "why_wrong": "El sólido puro se tacha igual que en cualquier Kc heterogéneo; Ksp no incluye su concentración."'''
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
