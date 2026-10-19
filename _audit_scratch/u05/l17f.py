# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("F1_we1reasoning1", r'''"Se sustituye en Qi=[Pb2+][I-]^2.",''',
r'''"Se sustituye en $Q_i=[Pb^{2+}][I^-]^2$.",'''
))

edits.append(("F2_ge0hint0", r'''"Calcula Qi=[Ca2+][CO3^2-] y compáralo con Ksp."''',
r'''"Calcula $Q_i=[Ca^{2+}][CO_3^{2-}]$ y compáralo con $K_{sp}$."'''
))

edits.append(("H9_statement", r'''"statement": "Se mezclan 50 mL de $BaCl_2$ 0,10 M con 150 mL de $Na_2SO_4$ 0,050 M. $K_{sp}(BaSO_4)=1{,}1\\times10^{-10}$. ¿Precipitará $BaSO_4$? Si es así, ¿qué ion queda en exceso una vez consumido el precipitado posible?",''',
r'''"statement": "Se mezclan 50 mL de $BaCl_2$ 0,10 M con 150 mL de $Na_2SO_4$ 0,050 M. $K_{sp}(BaSO_4)=1{,}1\\times10^{-10}$. ¿Precipitará $BaSO_4$? Si es así, ¿qué ion queda en exceso una vez formado el precipitado, y en qué concentración?",'''
))

edits.append(("H9_solution", r'''"solution": "$[Ba^{2+}]=\\dfrac{0{,}10\\times50}{200}=0{,}025$ M; $[SO_4^{2-}]=\\dfrac{0{,}050\\times150}{200}=0{,}0375$ M; $Q_i=0{,}025\\times0{,}0375=9{,}4\\times10^{-4}\\gg K_{sp}$",
        "interpretation": "$Q_i\\gg K_{sp}$: precipita masivamente BaSO4. Moles iniciales: $n(Ba^{2+})=0{,}10\\times0{,}050=5{,}0\\times10^{-3}$ mol; $n(SO_4^{2-})=0{,}050\\times0{,}150=7{,}5\\times10^{-3}$ mol. Como reaccionan 1:1, se consume todo el $Ba^{2+}$ (el reactivo limitante) y queda un exceso de $SO_4^{2-}$ de $2{,}5\\times10^{-3}$ mol en los 200 mL, es decir, $0{,}0125$ M de $SO_4^{2-}$ en exceso (antes de la pequeña redisolución residual de equilibrio).",''',
r'''"solution": "$[Ba^{2+}]=\\dfrac{0{,}10\\times50}{200}=0{,}025$ M; $[SO_4^{2-}]=\\dfrac{0{,}050\\times150}{200}=0{,}0375$ M; $Q_i=0{,}025\\times0{,}0375=9{,}4\\times10^{-4}\\gg K_{sp}$: precipita masivamente $BaSO_4$. Moles iniciales: $n(Ba^{2+})=0{,}10\\times0{,}050=5{,}0\\times10^{-3}$ mol; $n(SO_4^{2-})=0{,}050\\times0{,}150=7{,}5\\times10^{-3}$ mol. Como reaccionan 1:1, se consume todo el $Ba^{2+}$ (el reactivo limitante) y queda un exceso de $SO_4^{2-}$ de $2{,}5\\times10^{-3}$ mol en los 200 mL, es decir, $0{,}0125$ M de $SO_4^{2-}$ en exceso (antes de la pequeña redisolución residual de equilibrio).",
        "interpretation": "$Q_i\\gg K_{sp}$: precipita masivamente $BaSO_4$, y el ion que queda en exceso es $SO_4^{2-}$, con $0{,}0125$ M.",'''
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
