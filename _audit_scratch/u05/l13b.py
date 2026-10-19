# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H3_hint0", r'''"«Más cerca del equilibrio» significa que $|Q-K_c|$ es menor.",''',
r'''"«Más cerca del equilibrio» significa que $Q/K_c$ está más próximo a 1 (la diferencia absoluta $|Q-K_c|$ no es una medida fiable, porque Q varía multiplicativamente).",'''
))

edits.append(("H3_answer", r'''"answer": "(a) La mezcla A ($|120-100|=20$ frente a $|40-100|=60$). (b) A avanza hacia reactivos; B avanza hacia productos.",''',
r'''"answer": "(a) La mezcla A: $Q_A/K_c=1{,}20$ está más cerca de 1 que $Q_B/K_c=0{,}400$. (b) A avanza hacia reactivos; B avanza hacia productos.",'''
))

edits.append(("H3_fullsol", r'''"full_solution": "(a) $|Q_A-K_c|=20$; $|Q_B-K_c|=60{,}0$. La mezcla A está más cerca del equilibrio. (b) En A, $Q_A=120>K_c=100$: avanza hacia reactivos. En B, $Q_B=40{,}0<K_c=100$: avanza hacia productos. Ambas evolucionarán, cada una por su lado, hasta que $Q=100$ en las dos, pero no necesariamente hasta las mismas concentraciones finales, porque partieron de mezclas distintas.",''',
r'''"full_solution": "(a) $Q_A/K_c=120/100=1{,}20$; $Q_B/K_c=40{,}0/100=0{,}400$. Como $1{,}20$ está más cerca de 1 que $0{,}400$, la mezcla A está más cerca del equilibrio (la diferencia absoluta daría la misma conclusión aquí, pero no es el criterio correcto en general: Q varía multiplicativamente, no de forma aditiva). (b) En A, $Q_A=120>K_c=100$: avanza hacia reactivos. En B, $Q_B=40{,}0<K_c=100$: avanza hacia productos. Ambas evolucionarán, cada una por su lado, hasta que $Q=100$ en las dos, pero no necesariamente hasta las mismas concentraciones finales, porque partieron de mezclas distintas.",'''
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
