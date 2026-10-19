# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''$s^3=\\dfrac{5{,}6\\times10^{-12}}{4}=1{,}4\\times10^{-12}\\Rightarrow s=1{,}13\\times10^{-4}$ mol/L. $[OH^-]=2s=2{,}26\\times10^{-4}$ M.",'''
new = r'''$s^3=\\dfrac{5{,}6\\times10^{-12}}{4}=1{,}4\\times10^{-12}\\Rightarrow s=1{,}12\\times10^{-4}$ mol/L. $[OH^-]=2s=2{,}24\\times10^{-4}$ M.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
