# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"body": "1. Calcular el volumen total de la mezcla, $V_{total}=V_1+V_2$.\n2. Calcular la concentración diluida de cada ion relevante en ese volumen total, usando $C_{final}=\\dfrac{C_{inicial}\\,V_{inicial}}{V_{total}}$.\n3. Sustituir esas concentraciones diluidas (no las originales) en la expresión de $Q_i$.\n4. Comparar $Q_i$ con $K_{sp}$ y concluir.",'''

new = r'''"body": "0. Identificar qué par de iones forma la sal poco soluble (los demás iones presentes —$Na^+$, $K^+$, $NO_3^-$, etc.— son espectadores y no entran en $K_{sp}$).\n1. Calcular el volumen total de la mezcla, $V_{total}=V_1+V_2$.\n2. Calcular la concentración diluida de cada ion relevante en ese volumen total, usando $C_{final}=\\dfrac{C_{inicial}\\,V_{inicial}}{V_{total}}$.\n3. Sustituir esas concentraciones diluidas (no las originales) en la expresión de $Q_i$.\n4. Comparar $Q_i$ con $K_{sp}$ y concluir.\n5. Si precipita y se pide la masa: calcular los moles de cada ion; el ion limitante fija la cantidad máxima de precipitado, $m=n\\cdot M$.\n6. La concentración residual del ion limitante en el equilibrio se obtiene despejándola de $K_{sp}$ con la concentración del ion en exceso (p. ej., en el ejemplo 3 de esta lección, $[Ba^{2+}]=K_{sp}/[SO_4^{2-}]_{exceso}=1{,}1\\times10^{-10}/0{,}0125=8{,}8\\times10^{-9}$ M).",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
