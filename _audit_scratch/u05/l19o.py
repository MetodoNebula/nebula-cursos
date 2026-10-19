# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

# H7 remainder: add Ksp-with-coefficients example to TH-19-3
edits.append(("H7_TH3_example", r'''$K_{sp}$ es, literalmente, el «$K_c$» de ese equilibrio heterogéneo particular.",''',
r'''$K_{sp}$ es, literalmente, el «$K_c$» de ese equilibrio heterogéneo particular. Por ejemplo, para $Ag_2CrO_4(s)\\rightleftharpoons2\\,Ag^+(ac)+CrO_4^{2-}(ac)$: $K_{sp}=[Ag^+]^2[CrO_4^{2-}]$, con el sólido tachado y cada ion elevado a su coeficiente.",'''
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
