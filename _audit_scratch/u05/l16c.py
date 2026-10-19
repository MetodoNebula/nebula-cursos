# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("F1_we3", r'''"Se sustituye en Ksp=(2s)^2·s=4s^3."''',
r'''"Se sustituye en $K_{sp}=(2s)^2\\cdot s=4s^3$."'''
))

edits.append(("F2_ge0hint0", r'''"BaSO4 se disocia 1:1: Ba2+ + SO4^2-.",
          "Al ser tipo AB, Ksp=s²."''',
r'''"$BaSO_4$ se disocia 1:1: $Ba^{2+}+SO_4^{2-}$.",
          "Al ser tipo $AB$, $K_{sp}=s^2$."'''
))

edits.append(("F3_ex1hint0", r'''"Ag2CrO4 ⇌ 2Ag+ + CrO4^2-: tipo A2B, igual patrón que AB2."''',
r'''"$Ag_2CrO_4\\rightleftharpoons2\\,Ag^++CrO_4^{2-}$: tipo $A_2B$, igual patrón que $AB_2$."'''
))

edits.append(("F4_ex1commonerr0", r'''"Asignar el factor 2 al ion equivocado (a CrO4^2- en vez de a Ag+)."''',
r'''"Asignar el factor 2 al ion equivocado (a $CrO_4^{2-}$ en vez de a $Ag^+$)."'''
))

edits.append(("F5_examq0markscheme", r'''"1 punto por cada apartado correctamente resuelto",
          "Se exige mostrar la deducción de 108s^5 en (b), no solo el resultado final",
          "Tolerancia de redondeo en (c) y (d) de ±5% por el uso de raíces de índice 5"''',
r'''"Para la puntuación completa debes mostrar en (b) la deducción $(3s)^3(2s)^2=108s^5$, no solo el resultado.",
          "En (c) y (d) se admite un redondeo razonable ($\\pm5\\,\\%$) por el uso de raíces de índice 5."'''
))

edits.append(("F6_cm1howtoavoid", r'''"how_to_avoid": "Rehacer la tabla ICE de disociación (o aplicar Ksp=x^x y^y s^(x+y)) para cada sal antes de despejar s.",''',
r'''"how_to_avoid": "Rehacer la tabla ICE de disociación (o aplicar $K_{sp}=x^xy^ys^{x+y}$) para cada sal antes de despejar s.",'''
))

edits.append(("F7_examnotes2", r'''"Para estequiometrías poco habituales (como fosfatos tipo A3B2), usar la fórmula general Ksp=x^x y^y s^(x+y) en vez de intentar memorizar un caso para cada sal."''',
r'''"Para estequiometrías poco habituales (como fosfatos tipo $A_3B_2$), usar la fórmula general $K_{sp}=x^xy^ys^{x+y}$ en vez de intentar memorizar un caso para cada sal."'''
))

edits.append(("F8_bigidea", r'''"big_idea": "Ksp es la constante de equilibrio heterogéneo de una sal poco soluble con sus iones, y la relación entre Ksp y la solubilidad molar s depende de la estequiometría de disociación: s² para sales tipo AB, 4s³ para AB2/A2B, y en general x^x y^y s^(x+y).",''',
r'''"big_idea": "$K_{sp}$ es la constante de equilibrio heterogéneo de una sal poco soluble con sus iones, y la relación entre $K_{sp}$ y la solubilidad molar $s$ depende de la estequiometría de disociación: $s^2$ para sales tipo $AB$, $4s^3$ para $AB_2$/$A_2B$, y en general $K_{sp}=x^xy^ys^{x+y}$.",'''
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
