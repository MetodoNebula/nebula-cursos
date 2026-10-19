# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H10_examq0", r'''"full_solution": "(a) $Ca_3(PO_4)_2(s)\\rightleftharpoons 3\\,Ca^{2+}(ac)+2\\,PO_4^{3-}(ac)$; $K_{sp}=[Ca^{2+}]^3[PO_4^{3-}]^2$. (b) Si se disuelven s mol/L de sal, $[Ca^{2+}]=3s$ y $[PO_4^{3-}]=2s$; sustituyendo: $K_{sp}=(3s)^3(2s)^2=27s^3\\cdot4s^2=108\\,s^5$. (c) $s^5=\\dfrac{2{,}07\\times10^{-33}}{108}=1{,}917\\times10^{-35}\\Rightarrow s=(1{,}917\\times10^{-35})^{1/5}=1{,}14\\times10^{-7}$ mol/L. (d) $s_{g/L}=1{,}14\\times10^{-7}\\times310{,}2=3{,}53\\times10^{-5}$ g/L.",''',
r'''"full_solution": "(a) $Ca_3(PO_4)_2(s)\\rightleftharpoons 3\\,Ca^{2+}(ac)+2\\,PO_4^{3-}(ac)$; $K_{sp}=[Ca^{2+}]^3[PO_4^{3-}]^2$.\n\n(b) Si se disuelven s mol/L de sal, $[Ca^{2+}]=3s$ y $[PO_4^{3-}]=2s$; sustituyendo: $K_{sp}=(3s)^3(2s)^2=27s^3\\cdot4s^2=108\\,s^5$.\n\n(c) $s^5=\\dfrac{2{,}07\\times10^{-33}}{108}=1{,}917\\times10^{-35}\\Rightarrow s=(1{,}917\\times10^{-35})^{1/5}=1{,}14\\times10^{-7}$ mol/L.\n\n(d) $s_{g/L}=1{,}14\\times10^{-7}\\times310{,}2=3{,}53\\times10^{-5}$ g/L.",'''
))

edits.append(("H10_ge0", r'''"full_solution": "(a) $BaSO_4(s)\\rightleftharpoons Ba^{2+}+SO_4^{2-}$, ambos con coeficiente 1: $K_{sp}=[Ba^{2+}][SO_4^{2-}]$. (b) Al disolverse s mol/L, $[Ba^{2+}]=[SO_4^{2-}]=s$, así que $K_{sp}=s^2$, de donde $s=\\sqrt{1{,}1\\times10^{-10}}=1{,}05\\times10^{-5}$ mol/L.",''',
r'''"full_solution": "(a) $BaSO_4(s)\\rightleftharpoons Ba^{2+}+SO_4^{2-}$, ambos con coeficiente 1: $K_{sp}=[Ba^{2+}][SO_4^{2-}]$.\n\n(b) Al disolverse s mol/L, $[Ba^{2+}]=[SO_4^{2-}]=s$, así que $K_{sp}=s^2$, de donde $s=\\sqrt{1{,}1\\times10^{-10}}=1{,}05\\times10^{-5}$ mol/L.",'''
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
