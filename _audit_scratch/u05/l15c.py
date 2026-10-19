# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H4_theory4", r'''Por tanto: el catalizador **no desplaza** la posición de equilibrio y **no cambia** el valor de $K_c$ ni de $K_p$. Es el único de los agentes estudiados en estas dos lecciones que no tiene ningún efecto sobre el equilibrio en sí, solo sobre la rapidez de alcanzarlo.",''',
r'''Por tanto: el catalizador **no desplaza** la posición de equilibrio y **no cambia** el valor de $K_c$ ni de $K_p$. Es el único de los agentes estudiados que nunca, en ninguna condición, desplaza el equilibrio: el gas inerte sí puede hacerlo (a $P$ constante, con $\\Delta n\\neq0$); el catalizador, jamás, solo afecta a la rapidez de alcanzarlo.",'''
))

edits.append(("H5_ex0fullsol", r'''"full_solution": "La concentración de CO2(g) depende solo de sus propios moles y del volumen, ninguno de los cuales cambia al añadir N2 a V fijo. Como Kc solo depende de [CO2] en este equilibrio heterogéneo, Q no se altera y el equilibrio no se desplaza, aunque la presión total del recipiente aumente.",''',
r'''"full_solution": "La concentración de $CO_2(g)$ depende solo de sus propios moles y del volumen, ninguno de los cuales cambia al añadir $N_2$ a $V$ fijo. Como en este equilibrio heterogéneo $K_c=[CO_2]$ (los sólidos puros no aparecen en la expresión) y $[CO_2]=n_{CO_2}/V$ no cambia, $Q=K_c$ y no hay desplazamiento, aunque la presión total del recipiente aumente.",'''
))

edits.append(("H10_theory0", r'''Si sí cambian —porque el recipiente se expande para mantener constante la presión total, entonces sí hay desplazamiento, exactamente igual que si se hubiera expandido el recipiente a propósito.",''',
r'''Si sí cambian —porque el recipiente se expande para mantener constante la presión total—, entonces sí hay desplazamiento, exactamente igual que si se hubiera expandido el recipiente a propósito.",'''
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
