# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"why_wrong": "es el razonamiento invertido: a presión constante, añadir inerte favorece al lado con MÁS moles de gas (NO2), no al de menos, porque así se compensa mejor la dilución."'''
new = r'''"why_wrong": "Es el razonamiento invertido: al diluir, cada presión parcial se multiplica por $\\phi<1$ y, con $\\Delta n=-1$ visto desde productos a reactivos (aquí $\\Delta n=+1$ de $N_2O_4$ a $2\\,NO_2$), $Q_p=K_p\\\\phi^{\\\\Delta n}<K_p$: el sistema evoluciona hacia reactivos (productos de esta reacción), el lado con más moles de gas ($NO_2$), no hacia $N_2O_4$."'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
