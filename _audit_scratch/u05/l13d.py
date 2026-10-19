# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''hasta coincidir exactamente con ella cuando se alcanza el equilibrio. En ese momento, y solo en ese momento, tiene sentido escribir $Q=K_c$.",'''

new = r'''hasta coincidir exactamente con ella cuando se alcanza el equilibrio. En ese momento, y solo en ese momento, tiene sentido escribir $Q=K_c$.\n\nPara reacciones en fase gaseosa puede usarse, de forma equivalente, el cociente en presiones parciales $Q_p=\\dfrac{P_C^cP_D^d}{P_A^aP_B^b}$, que se compara con $K_p$ con el mismo criterio que $Q$ con $K_c$. Y, igual que en $K_c$ y $K_p$, ni en $Q$ ni en $Q_p$ aparecen los sólidos ni los líquidos puros.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
