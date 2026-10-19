# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"mark_scheme": [
          "1 punto por identificar que hay dos efectos distintos (velocidad y posición de equilibrio)",
          "1 punto por relacionar correctamente el sentido del desplazamiento con el signo de ΔH",
          "1 punto por concluir que la afirmación solo es cierta en el caso endotérmico"
        ],'''

new = r'''"mark_scheme": [
          "Para obtener la puntuación completa debes: distinguir los dos efectos (velocidad y posición de equilibrio) (1 p), relacionar el desplazamiento con el signo de $\\Delta H$ (1 p) y concluir que la afirmación solo es cierta para reacciones endotérmicas (1 p)."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
