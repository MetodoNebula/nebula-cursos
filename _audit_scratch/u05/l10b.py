import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H2_WE0_solution",
"(a) $K_c=\\dfrac{[\\text{NH}_3]^2}{[\\text{N}_2][\\text{H}_2]^3}$. (b) $K_c=\\dfrac{(0{,}200)^2}{0{,}400\\cdot(0{,}600)^3}=\\dfrac{0{,}0400}{0{,}400\\cdot0{,}216}=\\dfrac{0{,}0400}{0{,}0864}\\approx0{,}463$.",
"(a) $K_c=\\dfrac{[\\text{NH}_3]^2}{[\\text{N}_2][\\text{H}_2]^3}$. (b) $K_c=\\dfrac{(0{,}200)^2}{0{,}400\\cdot(0{,}600)^3}=\\dfrac{0{,}0400}{0{,}400\\cdot0{,}216}=\\dfrac{0{,}0400}{0{,}0864}\\approx0{,}463$. El número de moles de gas disminuye en la reacción directa ($\\Delta n=2-(1+3)=-2$), así que $K_c$ no es adimensional: $K_c\\approx0{,}463\\,\\mathrm{(mol\\,L^{-1})^{-2}}=0{,}463\\,\\mathrm{L^{2}\\,mol^{-2}}$."
))

edits.append(("REF_WE0_commonmistake",
"Confundir estos exponentes con órdenes de reacción que necesitarían determinarse experimentalmente (como en el apartado correspondiente), cuando en realidad para Kc siempre se usan directamente los coeficientes de la ecuación ajustada.",
"Confundir estos exponentes con órdenes de reacción que necesitarían determinarse experimentalmente (como en la lección 5: Determinación experimental del orden de reacción), cuando en realidad para Kc siempre se usan directamente los coeficientes de la ecuación ajustada."
))

edits.append(("H5_WE2_solution",
"(a) $K_c'=(0{,}463)^2\\approx0{,}214$. (b) $K_c''=1/0{,}463\\approx2{,}16$.",
"(a) $K_c'=(0{,}463)^2\\approx0{,}214\\,\\mathrm{L^{4}\\,mol^{-4}}$ ($\\Delta n$ se duplica, de $-2$ a $-4$). (b) $K_c''=1/0{,}463\\approx2{,}16\\,\\mathrm{mol^{2}\\,L^{-2}}$ ($\\Delta n$ cambia de signo, de $-2$ a $+2$)."
))

ok = apply(edits)
print("DONE", ok)
