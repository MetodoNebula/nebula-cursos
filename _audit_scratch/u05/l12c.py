import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H1_GE0_statement",
"(c) ¿Es aceptable la aproximación, con el criterio estricto del $1\\,\\%$? ¿Y con el tolerado del $10\\,\\%$?",
"(c) ¿Es aceptable la aproximación, con el criterio habitual $x_{aprox}/c_0<5\\,\\%$?"
))

edits.append(("H1_GE0_answer",
"(a) $x_{aprox}=9{,}49\\cdot10^{-3}$ M. (b) $x_{exacto}=8{,}63\\cdot10^{-3}$ M. (c) No es aceptable con el criterio estricto (error $\\approx9{,}9\\,\\%$), pero sí queda justo por debajo del $10\\,\\%$ tolerado en algunos contextos.",
"(a) $x_{aprox}=9{,}49\\cdot10^{-3}$ M. (b) $x_{exacto}=8{,}63\\cdot10^{-3}$ M. (c) No es aceptable: $x_{aprox}/c_0=9{,}49\\cdot10^{-3}/0{,}0500\\approx19\\,\\%>5\\,\\%$. Hay que usar el valor exacto, resolviendo la ecuación completa."
))

edits.append(("H1_GE0_fullsol",
"$c_0=0{,}500/10{,}0=0{,}0500$ M. (a) Aproximando $c_0-x\\approx c_0$: $K_c\\approx x^2/c_0\\Rightarrow x=\\sqrt{K_c\\,c_0}=\\sqrt{1{,}80\\cdot10^{-3}\\cdot0{,}0500}=9{,}49\\cdot10^{-3}$ M. (b) Sin aproximar: $K_c=\\dfrac{x^2}{c_0-x}\\Rightarrow x^2+K_c\\,x-K_c\\,c_0=0$. Resolviendo y tomando la raíz positiva: $x=8{,}63\\cdot10^{-3}$ M. (c) Error relativo $=\\dfrac{|9{,}49-8{,}63|}{8{,}63}\\approx9{,}9\\,\\%$. Supera el criterio estricto del $1\\,\\%$; con el criterio tolerante del $10\\,\\%$ queda justo dentro.",
"$c_0=0{,}500/10{,}0=0{,}0500$ M. (a) Aproximando $c_0-x\\approx c_0$: $K_c\\approx x^2/c_0\\Rightarrow x=\\sqrt{K_c\\,c_0}=\\sqrt{1{,}80\\cdot10^{-3}\\cdot0{,}0500}=9{,}49\\cdot10^{-3}$ M. (b) Sin aproximar: $K_c=\\dfrac{x^2}{c_0-x}\\Rightarrow x^2+K_c\\,x-K_c\\,c_0=0$. Con la fórmula general: $x=\\dfrac{-K_c+\\sqrt{K_c^2+4K_cc_0}}{2}=\\dfrac{-1{,}80\\cdot10^{-3}+\\sqrt{(1{,}80\\cdot10^{-3})^2+4\\cdot1{,}80\\cdot10^{-3}\\cdot0{,}0500}}{2}=\\dfrac{-1{,}80\\cdot10^{-3}+0{,}01906}{2}=8{,}63\\cdot10^{-3}$ M (la otra raíz, $-1{,}04\\cdot10^{-2}$, se descarta por no tener sentido físico). (c) $x_{aprox}/c_0=9{,}49\\cdot10^{-3}/0{,}0500\\approx19\\,\\%$, muy por encima del $5\\,\\%$ habitual: la aproximación **no es válida** y hay que usar $x_{exacto}=8{,}63\\cdot10^{-3}$ M."
))

edits.append(("H1_GE0_commonerr0",
"Dar por buena la aproximación sin calcular el error relativo, solo porque $K_c$ «parece pequeña».",
"Dar por buena la aproximación sin comprobar $x_{aprox}/c_0<5\\,\\%$, solo porque $K_c$ «parece pequeña»."
))

ok = apply(edits)
print("DONE", ok)
