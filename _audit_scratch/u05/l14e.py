# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"mistake": "Creer que Kc cambia al añadir o quitar reactivo/producto.",
        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",'''

new = r'''"mistake": "Creer que Kc cambia al añadir o quitar reactivo/producto.",
        "why": "Se confunde el desplazamiento de la posición del equilibrio (cambian las concentraciones) con un cambio de la constante, que solo depende de $T$.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
