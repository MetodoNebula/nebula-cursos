# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H5_H16_bigidea", r'''"big_idea": "Para construir Kc o Kp de cualquier equilibrio, primero se identifica el estado físico de cada especie y se tachan los sólidos y líquidos puros (cuya actividad es exactamente 1); Ksp es simplemente el caso particular de esta regla con un sólido y sus iones, y el mismo filtro se aplica al calcular Δn para el efecto de presión.",''',
r'''"big_idea": "Para construir Kc o Kp de cualquier equilibrio, primero se identifica el estado físico de cada especie y se tachan los sólidos y líquidos puros, porque su concentración es constante y queda englobada en el propio valor de K (de forma rigurosa, porque su actividad es 1: ampliación, no exigible en PAU); Ksp es simplemente el caso particular de esta regla con un sólido y sus iones, y el mismo filtro se aplica al calcular Δn para el efecto de presión.",'''
))

edits.append(("H16_keypoint1", r'''"La razón es exacta, no aproximada: su actividad termodinámica en estado estándar es 1.",''',
r'''"La razón, a nivel de Bachillerato: su concentración es constante y se engloba en el valor de K (ampliación: su actividad termodinámica es 1 en estado estándar).",'''
))

edits.append(("H15_formula0", r'''"K=\\prod_i a_i^{\\nu_i}\\ \\text{(con } a_{sólido/líquido\\ puro}=1\\text{)}",''',
r'''"K=\\prod_i a_i^{\\nu_i}\\quad(a_{\\text{sólido o líquido puro}}=1)",'''
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
