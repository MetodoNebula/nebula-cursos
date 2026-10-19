import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H6
edits.append(("H6_fc7",
"N2+3H2⇌2NH3; [N2]=0,400, [H2]=0,600, [NH3]=0,200. ¿Kc?",
"$\\text{N}_2+3\\,\\text{H}_2\\rightleftharpoons2\\,\\text{NH}_3$; $[\\text{N}_2]=0{,}400$, $[\\text{H}_2]=0{,}600$, $[\\text{NH}_3]=0{,}200\\,\\mathrm{mol\\,L^{-1}}$. ¿$K_c$?"
))
edits.append(("H6_fc7_back",
"$K_c=(0{,}200)^2/(0{,}400\\times0{,}600^3)\\approx0{,}463$ (mol/L)⁻².",
"$K_c=(0{,}200)^2/(0{,}400\\times0{,}600^3)\\approx0{,}463\\,\\mathrm{mol^{-2}\\,L^{2}}$."
))

# H7
edits.append(("H7_exam0_answer",
"(a) $K_c=[\\text{NH}_3]^2/([\\text{N}_2][\\text{H}_2]^3)$; $\\Delta n=2-4=-2$. (b) $K_c\\approx0{,}463$ (mol/L)⁻². (c) $K_c'\\approx2{,}16$ (mol/L)².",
"(a) $K_c=[\\text{NH}_3]^2/([\\text{N}_2][\\text{H}_2]^3)$; $\\Delta n=2-4=-2$. (b) $K_c\\approx0{,}463\\,\\mathrm{mol^{-2}\\,L^{2}}$. (c) $K_c'\\approx2{,}16\\,\\mathrm{mol^{2}\\,L^{-2}}$."
))
edits.append(("H7_exam0_fullsol",
"(b) $K_c=\\dfrac{(0{,}200)^2}{0{,}400\\times(0{,}600)^3}=\\dfrac{0{,}0400}{0{,}0864}\\approx0{,}463$ (mol/L)⁻² (coherente con $\\Delta n=-2$).\n\n(c) $K_c'=1/K_c=1/0{,}463\\approx2{,}16$ (mol/L)² (las unidades se invierten junto con el valor numérico, porque $\\Delta n'=-\\Delta n=2$).",
"(b) $K_c=\\dfrac{(0{,}200)^2}{0{,}400\\times(0{,}600)^3}=\\dfrac{0{,}0400}{0{,}0864}\\approx0{,}463\\,\\mathrm{mol^{-2}\\,L^{2}}$ (coherente con $\\Delta n=-2$).\n\n(c) $K_c'=1/K_c=1/0{,}463\\approx2{,}16\\,\\mathrm{mol^{2}\\,L^{-2}}$ (las unidades se invierten junto con el valor numérico, porque $\\Delta n'=-\\Delta n=2$)."
))

ok = apply(edits)
print("DONE", ok)
