# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H2_TH2", r'''3. Escribir $K_c$ (o $K_p$) como productos entre reactivos, usando solo las especies gaseosas (g) y en disolución (ac) que queden, cada una elevada a su coeficiente estequiométrico.''',
r'''3. Escribir $K_c$ con las concentraciones de las especies gaseosas (g) y disueltas (ac) que queden; $K_p$ solo con las presiones parciales de las especies gaseosas (nunca con especies (ac), que no tienen presión parcial), cada una elevada a su coeficiente estequiométrico.'''
))

edits.append(("H2_keyword1", r'''"definition": "Los sólidos puros y los líquidos puros no se incluyen en la expresión de Kc ni de Kp, solo las especies gaseosas y en disolución.",''',
r'''"definition": "Los sólidos puros y los líquidos puros no se incluyen en la expresión de Kc ni de Kp. En Kc quedan las especies gaseosas y en disolución (ac); en Kp solo las gaseosas, porque las especies (ac) no tienen presión parcial.",'''
))

edits.append(("H2_flashcard0", r'''"back": "Los sólidos puros y los líquidos puros no se incluyen en Kc ni Kp; solo las especies gaseosas y en disolución (ac), cada una elevada a su coeficiente.",''',
r'''"back": "Los sólidos puros y los líquidos puros no se incluyen en Kc ni Kp. En Kc quedan las especies gaseosas y en disolución (ac); en Kp solo las gaseosas (las especies (ac) nunca entran en Kp), cada una elevada a su coeficiente.",'''
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
