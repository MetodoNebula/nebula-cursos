# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H5_keyword2", r'''"definition": "Magnitud termodinámica que vale exactamente 1 para un sólido o líquido puro en su estado estándar, independientemente de la cantidad presente; es la razón exacta por la que no aparece en K.",''',
r'''"definition": "Magnitud termodinámica que vale 1 para un sólido o líquido puro en su estado estándar y, a presiones ordinarias, prácticamente 1 sea cual sea la cantidad presente; por eso no aparece en K (no porque su concentración sea pequeña). Para un gas ideal, $a_i=P_i/P^\\circ$.",'''
))

edits.append(("H5_flashcard6", r'''"back": "Porque su actividad termodinámica, en su estado estándar como fase pura, es exactamente 1, no una aproximación.",''',
r'''"back": "Porque su actividad termodinámica es 1 en su estado estándar y, a presiones ordinarias, prácticamente 1 sea cual sea la cantidad presente; por eso no aparece en K (nivel de ampliación, no exigible en PAU).",'''
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
