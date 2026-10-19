# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H14_TH5", r'''"body": "La relación $K_p=K_c(RT)^{\\Delta n}$, vista para equilibrios homogéneos, sigue siendo válida en un equilibrio heterogéneo, usando el mismo $\\Delta n$ filtrado (solo especies gaseosas) de este bloque. Para $CaCO_3(s)\\rightleftharpoons CaO(s)+CO_2(g)$: $K_p=K_c\\,(RT)^{1}=K_c\\,RT$, exactamente igual que si solo hubiera un gas en toda la reacción (que, de hecho, es el caso una vez filtrados los sólidos).",''',
r'''"body": "La relación $K_p=K_c(RT)^{\\Delta n}$, vista para equilibrios homogéneos, sigue siendo válida en un equilibrio heterogéneo, usando el mismo $\\Delta n$ calculado solo con las especies gaseosas (bloque anterior). Para $CaCO_3(s)\\rightleftharpoons CaO(s)+CO_2(g)$: $K_p=K_c\\,(RT)^{1}=K_c\\,RT$, exactamente igual que si solo hubiera un gas en toda la reacción (que, de hecho, es el caso una vez filtrados los sólidos). También puede escribirse directamente en presiones parciales: $K_p=p_{\\mathrm{CO_2}}$.",'''
))

edits.append(("H14_FC8", r'''"back": "$K_p=K_c(RT)^{\\Delta n}$, usando el mismo Δn filtrado (solo gases) de este bloque.",''',
r'''"back": "$K_p=K_c(RT)^{\\Delta n}$, con $\\Delta n$ calculado solo con las especies gaseosas.",'''
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
