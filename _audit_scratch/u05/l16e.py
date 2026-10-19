# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H8_answer", r'''"answer": "$K_{sp}=(xs)^x(ys)^y=x^x y^y s^{x+y}$; para AB: $1^1\\cdot1^1\\cdot s^2=s^2$ ✓; para AB2 (x=1,y=2): $1^1\\cdot2^2\\cdot s^3=4s^3$ ✓.",''',
r'''"answer": "$K_{sp}=(xs)^x(ys)^y=x^x y^y s^{x+y}$; para AB: $1^1\\cdot1^1\\cdot s^2=s^2$ ✓; para AB2 (x=1,y=2): $1^1\\cdot2^2\\cdot s^3=4s^3$ ✓; para A2B (x=2,y=1): $2^2\\cdot1^1\\cdot s^3=4s^3$ ✓, igual que AB2.",'''
))

edits.append(("H8_fullsol", r'''Para AB2 (x=1,y=2): $K_{sp}=1^1\\cdot2^2\\cdot s^{3}=4s^3$, coincide con la fórmula ya vista para sales tipo AB2. Para A3B2''',
r'''Para AB2 (x=1,y=2): $K_{sp}=1^1\\cdot2^2\\cdot s^{3}=4s^3$, coincide con la fórmula ya vista para sales tipo AB2. Para A2B (x=2,y=1, como $Ag_2CrO_4$): $K_{sp}=2^2\\cdot1^1\\cdot s^3=4s^3$, igual que AB2: la fórmula no distingue si el subíndice 2 está en el catión o en el anión, solo importa el conjunto de exponentes. Para A3B2'''
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
