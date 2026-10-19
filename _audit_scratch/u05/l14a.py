# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H1_solution", r'''"solution": "$x=0{,}0100$ (las tres concentraciones finales, $0{,}520$, $0{,}0204$ y $0{,}759$ M, ya son correctas y no cambian)",''',
r'''"solution": "$54{,}3=\\dfrac{(0{,}739+2x)^2}{(0{,}530-x)(0{,}0304-x)}\\Rightarrow50{,}3x^2-33{,}39x+0{,}3288=0\\Rightarrow x=\\dfrac{33{,}39\\pm\\sqrt{33{,}39^2-4\\cdot50{,}3\\cdot0{,}3288}}{2\\cdot50{,}3}$: $x_1=0{,}0100$, $x_2=0{,}654$ (se descarta: daría $[I_2]_{eq}<0$). Concentraciones finales: $[H_2]_{eq}=0{,}520$ M, $[I_2]_{eq}=0{,}0204$ M, $[HI]_{eq}=0{,}759$ M.",'''
))

edits.append(("H1_commonmistake", r'''"common_mistake": "Esperar que, como se añadió $H_2$, su concentración de equilibrio vaya a ser mayor que la del primer equilibrio y además $I_2$ se mantenga igual: en realidad $I_2$ también se consume, porque reacciona junto al $H_2$ añadido.",''',
r'''"common_mistake": "Creer que el sistema consume todo el $H_2$ añadido y vuelve a $[H_2]=0{,}330$ M, o que $[I_2]$ no cambia. En realidad la oposición es solo parcial: $[H_2]$ queda en $0{,}520$ M (mayor que $0{,}330$ M, pero menor que los $0{,}530$ M justo tras añadirlo) y el $I_2$ también se consume, de $0{,}0304$ a $0{,}0204$ M.",'''
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
