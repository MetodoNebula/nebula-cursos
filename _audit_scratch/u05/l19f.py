# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"statement": "A 1000 K, para $C(s)+H_2O(g)\\rightleftharpoons CO(g)+H_2(g)$, $K_c=0{,}20$. Calcula $K_p$ a esa temperatura ($R=0{,}0821$ atm·L/(mol·K)).",
        "hints": [
          "Calcula Δn contando solo las especies gaseosas: H2O (reactivo) frente a CO+H2 (productos)."
        ],
        "answer": "$\\Delta n=2-1=+1$; $K_p=K_c\\,RT=0{,}20\\times0{,}0821\\times1000=16{,}42$",
        "full_solution": "Especies gaseosas: reactivos, H2O (1 mol de gas; C(s) no cuenta); productos, CO+H2 (2 moles de gas). $\\Delta n=2-1=+1$. $K_p=K_c(RT)^{\\Delta n}=0{,}20\\times(0{,}0821\\times1000)^1=0{,}20\\times82{,}1=16{,}42$.",
        "common_errors": [
          "Calcular Δn=2-1 contando C(s) junto con H2O como «2 especies en reactivos», lo que daría Δn=0 y un resultado incorrecto."
        ],'''

new = r'''"statement": "A 1000 K, para $\\mathrm{C(s)+H_2O(g)\\rightleftharpoons CO(g)+H_2(g)}$, $K_c=0{,}20\\,\\mathrm{mol\\,L^{-1}}$. Calcula $K_p$ a esa temperatura ($R=0{,}0821\\,\\mathrm{atm\\,L\\,mol^{-1}\\,K^{-1}}$).",
        "hints": [
          "Calcula $\\Delta n$ contando solo las especies gaseosas: $H_2O$ (reactivo) frente a $CO+H_2$ (productos)."
        ],
        "answer": "$\\Delta n=2-1=+1$; $K_p=K_c\\,RT=0{,}20\\times0{,}0821\\times1000\\approx16\\,\\mathrm{atm}$ (16,4 con una cifra más)",
        "full_solution": "Especies gaseosas: reactivos, $H_2O$ (1 mol de gas; $C(s)$ no cuenta); productos, $CO+H_2$ (2 moles de gas). $\\Delta n=2-1=+1$. $K_p=K_c(RT)^{\\Delta n}=0{,}20\\times(0{,}0821\\times1000)^1=0{,}20\\times82{,}1=16{,}4\\,\\mathrm{atm}$.",
        "common_errors": [
          "Contar $C(s)$ junto con $H_2O$ como «2 especies en reactivos»: $\\Delta n=2-2=0$, lo que daría erróneamente $K_p=K_c=0{,}20$."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
