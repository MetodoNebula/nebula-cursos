# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H4_bigidea", r'''"big_idea": "$Q$ es $K_c$ calculada en cualquier instante, no solo en el equilibrio; comparar ambos números dice, sin resolver nada, hacia dónde evoluciona un sistema.",''',
r'''"big_idea": "$Q$ tiene la misma expresión que $K_c$, pero evaluada con las concentraciones de un instante cualquiera, no solo en el equilibrio; comparar ambos números dice, sin resolver nada, hacia dónde evoluciona un sistema.",'''
))

edits.append(("H5_answer", r'''"answer": "(a) $Q=0<K_c$: avanza hacia productos. (b) $[H_2]_{eq}=[I_2]_{eq}=0{,}213$ M; $[HI]_{eq}=1{,}573$ M.",''',
r'''"answer": "(a) $Q=0<K_c$: avanza hacia productos. (b) $[H_2]_{eq}=[I_2]_{eq}=0{,}213$ M; $[HI]_{eq}=1{,}57$ M.",'''
))

edits.append(("H5_fullsol", r'''"full_solution": "(a) Con $[HI]_0=0$, $Q=0$, menor que cualquier $K_c>0$: avanza hacia productos. (b) Tabla ICE: $[H_2]=[I_2]=1{,}00-x$, $[HI]=2x$. $\\sqrt{54{,}3}=\\dfrac{2x}{1{,}00-x}=7{,}37\\Rightarrow x=0{,}787$. $[H_2]_{eq}=[I_2]_{eq}=0{,}213$ M, $[HI]_{eq}=1{,}573$ M.",''',
r'''"full_solution": "(a) Con $[HI]_0=0$, $Q=0$, menor que cualquier $K_c>0$: avanza hacia productos. (b) Tabla ICE: $[H_2]=[I_2]=1{,}00-x$, $[HI]=2x$. $\\sqrt{54{,}3}=\\dfrac{2x}{1{,}00-x}=7{,}37\\Rightarrow7{,}37(1{,}00-x)=2x\\Rightarrow x=7{,}37/9{,}37=0{,}787$. $[H_2]_{eq}=[I_2]_{eq}=1{,}00-0{,}787=0{,}213$ M, $[HI]_{eq}=2\\cdot0{,}787=1{,}57$ M (con 3 cifras significativas, igual que los datos).",'''
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
