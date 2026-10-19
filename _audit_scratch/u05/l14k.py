# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"common_errors": [
          "Olvidar que, aunque el desplazamiento sea desfavorable hacia productos, la velocidad de reacción sigue siendo mayor a mayor T: son dos efectos distintos y no se cancelan entre sí."
        ],'''

new = r'''"common_errors": [
          "Confundir los dos efectos de $T$: subirla desplaza el equilibrio hacia reactivos (menos $NH_3$), pero aun así la velocidad de reacción aumenta; son efectos distintos."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
