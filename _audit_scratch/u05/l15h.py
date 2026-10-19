# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"statement": "Indica si cada afirmación sobre un catalizador es verdadera o falsa: (a) cambia el valor de Kc. (b) acelera solo la reacción directa. (c) reduce la energía de activación de ambos sentidos de la reacción. (d) hace que se alcance antes el equilibrio.",
        "hints": [
          "Repasa la definición: el catalizador ofrece un camino alternativo con menor energía de activación para ambos sentidos."
        ],
        "answer": "(a) Falsa. (b) Falsa. (c) Verdadera. (d) Verdadera.",'''

new = r'''"statement": "Indica si cada afirmación sobre un catalizador es verdadera o falsa: (a) cambia el valor de Kc. (b) acelera solo la reacción directa. (c) reduce la energía de activación de ambos sentidos de la reacción. (d) hace que se alcance antes el equilibrio.",
        "hints": [
          "Repasa la definición: el catalizador ofrece un camino alternativo con menor energía de activación para ambos sentidos."
        ],
        "answer": "(a) Falsa: Kc solo depende de T. (b) Falsa: acelera igual los dos sentidos. (c) Verdadera. (d) Verdadera: se llega antes al mismo equilibrio.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
