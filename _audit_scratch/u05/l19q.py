# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H4_cm2", r'''"mistake": "Asumir que el agua líquida siempre debe incluirse (o siempre debe excluirse) sin comprobar el contexto concreto de la reacción.",
        "why": "Se generaliza un hábito (agua como disolvente de fondo) a cualquier reacción, incluyendo aquellas donde el agua es un reactivo o producto en sí mismo.",
        "how_to_avoid": "Comprobar en cada reacción si el agua es un líquido puro que participa directamente (se tacha) o un disolvente de fondo con solutos diluidos (no se tacha el soluto).",''',
r'''"mistake": "Pensar que el agua líquida disolvente sí debe incluirse en Kc cuando hay solutos diluidos en ella, o que existe un caso especial para «disolvente de fondo».",
        "why": "Se confunde el agua como disolvente de una disolución diluida (nunca aparece en K, igual que un líquido puro) con el único caso real en que sí aparece: cuando no hay disolvente mayoritario, como en la esterificación.",
        "how_to_avoid": "Aplicar la regla general: $H_2O(l)$, como líquido puro o como disolvente de una disolución diluida, nunca aparece en K; $H_2O(g)$ sí aparece, como cualquier gas. La única excepción es una reacción en fase líquida homogénea sin disolvente mayoritario (p. ej. la esterificación), donde todas las especies, incluida el agua, entran en Kc.",'''
))

edits.append(("H4_FC9", r'''"back": "Depende del contexto: si es líquido puro (reactivo o producto de la propia reacción), se tacha; si es vapor de agua (g), sí cuenta como gas.",''',
r'''"back": "Como líquido puro o como disolvente de una disolución diluida, nunca cuenta. Como vapor de agua (g), sí cuenta, como cualquier gas. La única excepción es una reacción en fase líquida homogénea sin disolvente mayoritario (esterificación), donde el agua líquida sí entra en Kc junto con las demás especies.",'''
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
