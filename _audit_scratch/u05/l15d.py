# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''Este caso es formalmente idéntico a expandir el recipiente: $Q$ se desvía de $K$ en el sentido que favorece al lado con **más moles de gas**, si $\\Delta n\\neq0$. Si $\\Delta n=0$, tampoco hay efecto aquí.",'''

new = r'''Este caso es formalmente idéntico a expandir el recipiente: $Q$ se desvía de $K$ en el sentido que favorece al lado con **más moles de gas**, si $\\Delta n\\neq0$. Si $\\Delta n=0$, tampoco hay efecto aquí.\n\nEn concreto, si a $P$ constante los moles totales pasan de $n$ a $n+n_{inerte}$, cada presión parcial reactiva se multiplica por $\\phi=\\dfrac{n}{n+n_{inerte}}<1$, y $Q_p=K_p\\,\\phi^{\\Delta n}$: si $\\Delta n<0$, $\\phi^{\\Delta n}>1$ y $Q_p>K_p$ ⟹ hacia reactivos; si $\\Delta n>0$, $\\phi^{\\Delta n}<1$ y $Q_p<K_p$ ⟹ hacia productos.\n\nEjemplo numérico: para $N_2O_4(g)\\rightleftharpoons2\\,NO_2(g)$ ($\\Delta n=1$) en equilibrio con $P_{N_2O_4}=0{,}400$ atm y $P_{NO_2}=0{,}245$ atm ($K_p=0{,}245^2/0{,}400=0{,}150$ atm), si se añaden, a $P$ constante, tantos moles de gas inerte como moles de gas reactivo había ($\\phi=0{,}5$): $Q_p=K_p\\,\\phi^{\\Delta n}=0{,}150\\times0{,}5=0{,}0750\\,\\mathrm{atm}<K_p$, así que el sistema avanza hacia $NO_2$ (productos).",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
