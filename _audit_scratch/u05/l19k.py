# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"solution": "$\\Delta n=1-0=+1$",
        "interpretation": "Como $\\Delta n\\neq0$, comprimir el recipiente sí desplaza este equilibrio heterogéneo, hacia el lado con menos moles de gas: los reactivos (donde no hay ningún gas). Comprimir favorece la formación de más $CaCO_3(s)$ a partir de $CaO(s)$ y $CO_2(g)$.",'''

new = r'''"solution": "$\\Delta n=1-0=+1$. Al comprimir aumenta $p_{\\mathrm{CO_2}}$ ($Q>K_p$): el equilibrio se desplaza hacia la izquierda (formación de $CaCO_3$) hasta que $p_{\\mathrm{CO_2}}$ recupera el valor $K_p$ a esa $T$.",
        "interpretation": "Como $\\Delta n\\neq0$, comprimir el recipiente sí desplaza este equilibrio heterogéneo, hacia el lado con menos moles de gas: los reactivos (donde no hay ningún gas). Comprimir favorece la formación de más $CaCO_3(s)$ a partir de $CaO(s)$ y $CO_2(g)$, consumiendo el exceso de $CO_2$ hasta que su presión parcial vuelve a valer $K_p$ (que no cambia, porque $T$ no ha cambiado).",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
