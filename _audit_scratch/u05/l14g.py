# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H10_H11_EXAM1", r'''"full_solution": "(a) Añadir $O_2$ (reactivo) sube la cantidad de reactivo disponible; $Q$ baja por debajo de $K_c$: avanza hacia productos. (b) Retirar $SO_3$ (producto) baja el numerador de $Q$; $Q$ baja por debajo de $K_c$: avanza hacia productos. (c) Moles de gas: reactivos $2+1=3$; productos $2$. $\\Delta n=-1\\neq0$. Comprimir favorece al lado con menos moles: avanza hacia productos. (d) Un catalizador no desplaza el equilibrio: acelera por igual la reacción directa e inversa, sin cambiar ni $K_c$ ni la posición final.",
        "mark_scheme": [
          "1 punto por apartado, exigiendo la justificación (Q, Δn o catalizador según corresponda), no solo el sentido",
          "Penalización de 0,5 puntos en (c) si no se justifica contando los moles de gas de esta reacción concreta"
        ],''',
r'''"full_solution": "(a) Añadir $O_2$ (reactivo) sube la cantidad de reactivo disponible; $Q$ baja por debajo de $K_c$: avanza hacia productos.\n\n(b) Retirar $SO_3$ (producto) baja el numerador de $Q$; $Q$ baja por debajo de $K_c$: avanza hacia productos.\n\n(c) Moles de gas: reactivos $2+1=3$; productos $2$. $\\Delta n=-1\\neq0$. Al duplicar la presión total comprimiendo el recipiente a la mitad ($f=0{,}5$), $Q_{nuevo}=K_c\\cdot f^{-\\Delta n}=K_c\\cdot0{,}5^{1}=K_c/2<K_c$: avanza hacia productos, el lado con menos moles de gas.\n\n(d) Un catalizador no desplaza el equilibrio: acelera por igual la reacción directa e inversa, sin cambiar ni $K_c$ ni la posición final.",
        "mark_scheme": [
          "Cada apartado vale 1 punto: para obtenerlo debes justificar con $Q$, $\\Delta n$ o el papel del catalizador, no basta con el sentido.",
          "En (c) pierdes 0,5 puntos si no cuentas los moles de gas de esta reacción."
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
