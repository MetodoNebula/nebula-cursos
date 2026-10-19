import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []
edits.append(("H6_misc0_relexc",
"Calcular explícitamente $v_+$ y $v_-$ en el equilibrio con datos numéricos, y comprobar que ambas son iguales pero distintas de cero.\",\n  \"related_exercises\": \"el ejemplo 2 de esta lección\"",
"Calcular explícitamente $v_+$ y $v_-$ en el equilibrio con datos numéricos, y comprobar que ambas son iguales pero distintas de cero.\",\n  \"related_exercises\": \"el reto de esta lección (donde se calculan explícitamente $v_+=v_-=1{,}43\\\\times10^{-2}\\\\,\\\\mathrm{mol\\\\,L^{-1}\\\\,s^{-1}}$ en el equilibrio) y el ejemplo 2\""
))
edits.append(("H3_exercises1_answer",
"[B]≈0,1667 mol/L.",
"[B]≈0,17 mol/L."
))
edits.append(("H3_exercises1_fullsol",
"$v_+=v_- \\Rightarrow k_+[\\text{A}]=k_-[\\text{B}] \\Rightarrow [\\text{B}]=\\dfrac{k_+[\\text{A}]}{k_-}=\\dfrac{0{,}015\\times0{,}50}{0{,}045}=\\dfrac{7{,}5\\times10^{-3}}{0{,}045}\\approx0{,}1667$ mol/L.",
"$v_+=v_- \\Rightarrow k_+[\\text{A}]=k_-[\\text{B}] \\Rightarrow [\\text{B}]=\\dfrac{k_+[\\text{A}]}{k_-}=\\dfrac{0{,}015\\times0{,}50}{0{,}045}=\\dfrac{7{,}5\\times10^{-3}}{0{,}045}\\approx0{,}17\\,\\mathrm{mol\\,L^{-1}}$ (exactamente $0{,}50/3$)."
))
edits.append(("REF_prereq0",
"Conocer la ley de velocidad $v=k[\\text{A}]^m[\\text{B}]^n$ y cómo calcular v sustituyendo concentraciones y constante de velocidad (lección el apartado correspondiente).",
"Conocer la ley de velocidad $v=k[\\text{A}]^m[\\text{B}]^n$ y cómo calcular v sustituyendo concentraciones y constante de velocidad (lección 4: Ley de velocidad)."
))
edits.append(("REF_diag0",
"Repasar la sustitución directa en una ley de velocidad de orden 1 (lección el apartado correspondiente) antes de aplicarla a una reacción reversible.",
"Repasar la sustitución directa en una ley de velocidad de orden 1 (lección 4: Ley de velocidad) antes de aplicarla a una reacción reversible."
))
edits.append(("REF_examnotes2",
"Esta lección prepara directamente la constante Kc (el apartado correspondiente): el cociente k+/k- aquí obtenido es, para esta reacción sencilla A⇌B, exactamente el valor de Kc.",
"Esta lección prepara directamente la constante Kc (lección 10: Constante Kc): el cociente k+/k- aquí obtenido es, para esta reacción sencilla A⇌B, exactamente el valor de Kc."
))

ok = apply(edits)
print("DONE", ok)
