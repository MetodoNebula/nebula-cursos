# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H6_hints", r'''"hints": [
          "La condición límite es Qi=Ksp justo en el instante en que empieza a precipitar.",
          "[Ba2+] en ese instante es prácticamente la original (0,0010 M), porque y es muy pequeño frente a 100 mL."
        ],''',
r'''"hints": [
          "La condición límite es $Q_i=K_{sp}$ justo en el instante en que empieza a precipitar.",
          "$[Ba^{2+}]$ en ese instante es prácticamente la original ($0{,}0010$ M), porque $y$ es muy pequeño frente a 100 mL."
        ],'''
))

edits.append(("H6_answer", r'''"answer": "$[SO_4^{2-}]_{mínimo}=1{,}1\\times10^{-7}$ M en la mezcla; con [Ba2+]≈0,0010 M constante, se necesita una cantidad de SO4^2- añadida muy pequeña, del orden de $y\\approx1{,}1\\times10^{-4}$ mL (prácticamente instantánea).",''',
r'''"answer": "$[SO_4^{2-}]_{mínimo}=1{,}1\\times10^{-7}$ M en la mezcla; con $[Ba^{2+}]\\approx0{,}0010$ M constante, se necesita una cantidad de $SO_4^{2-}$ añadida muy pequeña, del orden de $y\\approx1{,}1\\times10^{-4}$ mL (mucho menos que una gota, $\\approx0{,}05$ mL): precipita con la primera gota.",'''
))

edits.append(("H6_fullsol", r'''"full_solution": "En el límite de empezar a precipitar, $Q_i=K_{sp}$: $[Ba^{2+}][SO_4^{2-}]=1{,}1\\times10^{-10}$. Con $[Ba^{2+}]\\approx1{,}0\\times10^{-3}$ M (apenas diluido), $[SO_4^{2-}]_{mínimo}=\\dfrac{1{,}1\\times10^{-10}}{1{,}0\\times10^{-3}}=1{,}1\\times10^{-7}$ M en el volumen total (≈100 mL). Los moles de SO4^2- necesarios son $1{,}1\\times10^{-7}\\times0{,}100=1{,}1\\times10^{-8}$ mol, que en la disolución 0,10 M corresponden a $y=\\dfrac{1{,}1\\times10^{-8}}{0{,}10}=1{,}1\\times10^{-7}$ L $=1{,}1\\times10^{-4}$ mL: una cantidad diminuta, lo que confirma que $BaSO_4$ precipita prácticamente con la primera gota.",''',
r'''"full_solution": "En el límite de empezar a precipitar, $Q_i=K_{sp}$: $[Ba^{2+}][SO_4^{2-}]=1{,}1\\times10^{-10}$. Con $[Ba^{2+}]\\approx1{,}0\\times10^{-3}$ M (apenas diluido), $[SO_4^{2-}]_{mínimo}=\\dfrac{1{,}1\\times10^{-10}}{1{,}0\\times10^{-3}}=1{,}1\\times10^{-7}$ M en el volumen total ($\\approx100$ mL). Los moles de $SO_4^{2-}$ necesarios son $1{,}1\\times10^{-7}\\times0{,}100=1{,}1\\times10^{-8}$ mol, que en la disolución 0,10 M corresponden a $y=\\dfrac{1{,}1\\times10^{-8}}{0{,}10}=1{,}1\\times10^{-7}$ L $=1{,}1\\times10^{-4}$ mL: una cantidad diminuta (mucho menos que una gota, $\\approx0{,}05$ mL), lo que confirma que $BaSO_4$ precipita prácticamente con la primera gota.",'''
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
