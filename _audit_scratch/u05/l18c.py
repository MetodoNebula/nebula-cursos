# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"answer": "(a) $s^3=\\dfrac{5{,}6\\times10^{-12}}{4}=1{,}4\\times10^{-12}\\Rightarrow s=1{,}12\\times10^{-4}$ mol/L. (b) $[OH^-]=2s=2{,}24\\times10^{-4}$ M; $pOH=3{,}65$; $pH=10{,}35$. (c) A pH=10, $[OH^-]=1{,}0\\times10^{-4}$ M (más bajo que el de la disolución saturada sin tampón, 2,24×10⁻⁴ M). Usando $K_{sp}=[Mg^{2+}][OH^-]^2$ con $[OH^-]$ fijado por el tampón: $[Mg^{2+}]=s'=\\dfrac{K_{sp}}{[OH^-]^2}=\\dfrac{5{,}6\\times10^{-12}}{(1{,}0\\times10^{-4})^2}=5{,}6\\times10^{-4}$ mol/L. (d) $s'=5{,}6\\times10^{-4}>s=1{,}12\\times10^{-4}$: al fijar [OH-] en un valor MENOR que el de la disolución saturada sin tampón, se permite que se disuelva MÁS Mg(OH)2 (menos OH- en el producto, más Mg2+ puede estar presente para mantener el mismo Ksp) — es decir, bajar el pH (de 10,35 a 10) efectivamente aumenta la solubilidad del hidróxido, confirmando con números la idea cualitativa de que la solubilidad de un hidróxido aumenta al bajar el pH.",
        "full_solution": "(a) $s^3=\\dfrac{5{,}6\\times10^{-12}}{4}=1{,}4\\times10^{-12}\\Rightarrow s=1{,}12\\times10^{-4}$ mol/L. (b) $[OH^-]=2s=2{,}24\\times10^{-4}$ M; $pOH=3{,}65$; $pH=10{,}35$. (c) A pH=10, $[OH^-]=1{,}0\\times10^{-4}$ M (más bajo que el de la disolución saturada sin tampón, 2,24×10⁻⁴ M). Usando $K_{sp}=[Mg^{2+}][OH^-]^2$ con $[OH^-]$ fijado por el tampón: $[Mg^{2+}]=s'=\\dfrac{K_{sp}}{[OH^-]^2}=\\dfrac{5{,}6\\times10^{-12}}{(1{,}0\\times10^{-4})^2}=5{,}6\\times10^{-4}$ mol/L. (d) $s'=5{,}6\\times10^{-4}>s=1{,}12\\times10^{-4}$: al fijar [OH-] en un valor MENOR que el de la disolución saturada sin tampón, se permite que se disuelva MÁS Mg(OH)2 (menos OH- en el producto, más Mg2+ puede estar presente para mantener el mismo Ksp) — es decir, bajar el pH (de 10,35 a 10) efectivamente aumenta la solubilidad del hidróxido, confirmando con números la idea cualitativa de que la solubilidad de un hidróxido aumenta al bajar el pH.",
        "mark_scheme": [
          "1 punto por (a)",
          "1 punto por (b)",
          "1,5 puntos por (c), exigiendo usar el [OH-] del tampón, no el de la disolución sin tampón",
          "0,5 puntos por relacionar correctamente en (d) el aumento de s' con la disminución de pH"
        ],'''

new = r'''"answer": "(a) $s=1{,}12\\times10^{-4}$ M. (b) $\\mathrm{pH}=10{,}35$. (c) $s'=5{,}6\\times10^{-4}$ M. (d) $s'>s$: al bajar el pH (menos $OH^-$) aumenta la solubilidad del hidróxido.",
        "full_solution": "(a) $s^3=\\dfrac{5{,}6\\times10^{-12}}{4}=1{,}4\\times10^{-12}\\Rightarrow s=1{,}12\\times10^{-4}$ mol/L.\n\n(b) $[OH^-]=2s=2{,}24\\times10^{-4}$ M; $\\mathrm{pOH}=3{,}65$; $\\mathrm{pH}=10{,}35$.\n\n(c) A $\\mathrm{pH}=10$, $[OH^-]=1{,}0\\times10^{-4}$ M (más bajo que el de la disolución saturada sin tampón, $2{,}24\\times10^{-4}$ M). Usando $K_{sp}=[Mg^{2+}][OH^-]^2$ con $[OH^-]$ fijado por el tampón: $[Mg^{2+}]=s'=\\dfrac{K_{sp}}{[OH^-]^2}=\\dfrac{5{,}6\\times10^{-12}}{(1{,}0\\times10^{-4})^2}=5{,}6\\times10^{-4}$ mol/L.\n\n(d) $s'=5{,}6\\times10^{-4}>s=1{,}12\\times10^{-4}$: al fijar $[OH^-]$ en un valor MENOR que el de la disolución saturada sin tampón, se permite que se disuelva MÁS $Mg(OH)_2$ (menos $OH^-$ en el producto, más $Mg^{2+}$ puede estar presente para mantener el mismo $K_{sp}$) — es decir, bajar el pH (de 10,35 a 10) efectivamente aumenta la solubilidad del hidróxido, confirmando con números la idea cualitativa de que la solubilidad de un hidróxido aumenta al bajar el pH.",
        "mark_scheme": [
          "(a) vale 1 punto y (b) vale 1 punto.",
          "(c) vale 1,5 puntos: para obtenerlos debes usar la $[OH^-]$ que fija el tampón ($10^{-4}$ M), no $2s'$.",
          "(d) vale 0,5 puntos por relacionar correctamente el aumento de $s'$ con la disminución del pH."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
