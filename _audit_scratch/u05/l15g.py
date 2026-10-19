# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H9_EXAM1", r'''"full_solution": "(a) A V constante, añadir Ar no cambia ninguna concentración reactiva: Q no se altera, no hay desplazamiento. (b) A P constante, Δn=2-(1+1)=0: aunque el recipiente se expanda al añadir Ar, el factor de dilución se cancela igual que en cualquier expansión con Δn=0, así que tampoco hay desplazamiento. (c) Un catalizador acelera ambos sentidos por igual sin cambiar Kc ni la posición de equilibrio.",
        "mark_scheme": [
          "1 punto por cada apartado correctamente justificado",
          "1 punto adicional por reconocer que (a) y (b) coinciden en este caso solo porque Δn=0, no por la misma razón de fondo"
        ],''',
r'''"full_solution": "(a) A V constante, añadir Ar no cambia ninguna concentración reactiva: Q no se altera, no hay desplazamiento.\n\n(b) A P constante, Δn=2-(1+1)=0: aunque el recipiente se expanda al añadir Ar, el factor de dilución se cancela igual que en cualquier expansión con Δn=0, así que tampoco hay desplazamiento.\n\n(c) Un catalizador acelera ambos sentidos por igual sin cambiar Kc ni la posición de equilibrio.\n\nEn conclusión: (a) y (b) coinciden en este caso, pero por razones distintas, no por la misma razón de fondo: en (a) no cambian las concentraciones; en (b) sí se diluyen, pero con $\\Delta n=0$ el factor se cancela.",
        "mark_scheme": [
          "Para la puntuación completa debes justificar cada apartado y explicar que (a) y (b) coinciden por razones distintas: en (a) no cambian las concentraciones; en (b) sí se diluyen, pero con $\\Delta n=0$ el factor se cancela."
        ],'''
))

edits.append(("H9_EXAM2", r'''"mark_scheme": [
          "1 punto por identificar que la afirmación no es universalmente cierta",
          "1 punto por el caso V constante",
          "1 punto por el caso P constante, explicando la causa real (dilución por expansión, no reacción directa con el inerte)"
        ],''',
r'''"mark_scheme": [
          "Para obtener los 3 puntos debes: identificar que la afirmación no es universalmente cierta (1 p), explicar el caso de V constante (1 p) y explicar el caso de P constante, con la causa real: dilución por expansión, no reacción directa con el inerte (1 p)."
        ],'''
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
