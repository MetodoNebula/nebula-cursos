import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H1: theory_blocks[2] advertencia reacciones elementales
edits.append(("H1_theory2_kgerm",
"Este cociente $k_+/k_-$ es, precisamente, un valor constante para una reacción dada a una temperatura dada (porque $k_+$ y $k_-$ lo son): es el germen de la **constante de equilibrio Kc**, que se estudiará formalmente en la lección siguiente para reacciones más generales.",
"Este cociente $k_+/k_-$ es, precisamente, un valor constante para una reacción dada a una temperatura dada (porque $k_+$ y $k_-$ lo son): es el germen de la **constante de equilibrio Kc**, que se estudiará formalmente en la lección siguiente para reacciones más generales. Ojo: esta deducción solo es válida porque aquí las reacciones directa e inversa son **elementales** (su orden coincide con su coeficiente). En general, la expresión de $K_c$ se escribe siempre con los **coeficientes estequiométricos** de la ecuación ajustada, nunca con los órdenes de la ley de velocidad experimental, y su justificación última es termodinámica, no cinética."
))

# H7: theory_blocks[1].title LaTeX
edits.append(("H7_theory1_title",
"La condición de equilibrio: v+ = v-",
"La condición de equilibrio: $v_+=v_-$"
))

# H8: worked_examples[1].solution LaTeX units
edits.append(("H8_WE1_solution",
"$v_{+,0}=0{,}050\\times1{,}00=0{,}050$ mol·L⁻¹·s⁻¹; $v_{-,0}=0{,}020\\times0=0$ (no hay B al inicio). $k_+/k_-=0{,}050/0{,}020=2{,}5$.",
"$v_{+,0}=0{,}050\\times1{,}00=0{,}050\\,\\mathrm{mol\\,L^{-1}\\,s^{-1}}$; $v_{-,0}=0{,}020\\times0=0$ (no hay B al inicio). $k_+/k_-=0{,}050/0{,}020=2{,}5$."
))

# H5: worked_examples[1].interpretation - evitar remitir al reto de forma incómoda
edits.append(("H5_WE1_interpretation",
"Al principio solo actúa la reacción directa ($v_{-,0}=0$). El cociente $k_+/k_-=2{,}5$ indica que, en el equilibrio, habrá 2,5 veces más B que A, aunque todavía no se hayan calculado las concentraciones exactas (eso exige, además, conocer la cantidad total de sustancia, que se verá en el reto de esta lección).",
"Al principio solo actúa la reacción directa ($v_{-,0}=0$). El cociente $k_+/k_-=2{,}5$ indica que, en el equilibrio, $[\\text{B}]_{\\text{eq}}$ será 2,5 veces $[\\text{A}]_{\\text{eq}}$, aunque esta sola relación no basta para fijar los valores absolutos de las concentraciones: para eso hace falta además la conservación de materia (cuánta sustancia hay en total), que se combina con esta relación en el reto de esta lección para obtener $[\\text{A}]_{\\text{eq}}=0{,}286$ y $[\\text{B}]_{\\text{eq}}=0{,}714$ mol/L."
))

# H6: misconceptions[0].related_exercises
edits.append(("H6_misc0_relexc",
"el ejemplo 2 de esta lección",
"el reto de esta lección (donde se calculan explícitamente $v_+=v_-=1{,}43\\times10^{-2}\\,\\mathrm{mol\\,L^{-1}\\,s^{-1}}$ en el equilibrio) y el ejemplo 2"
))

# H3: exercises[1] cifras significativas
edits.append(("H3_exercises1_answer",
"[B]≈0,1667 mol/L.",
"[B]≈0,17 mol/L."
))
edits.append(("H3_exercises1_fullsol",
"$v_+=v_- \\Rightarrow k_+[\\text{A}]=k_-[\\text{B}] \\Rightarrow [\\text{B}]=\\dfrac{k_+[\\text{A}]}{k_-}=\\dfrac{0{,}015\\times0{,}50}{0{,}045}=\\dfrac{7{,}5\\times10^{-3}}{0{,}045}\\approx0{,}1667$ mol/L.",
"$v_+=v_- \\Rightarrow k_+[\\text{A}]=k_-[\\text{B}] \\Rightarrow [\\text{B}]=\\dfrac{k_+[\\text{A}]}{k_-}=\\dfrac{0{,}015\\times0{,}50}{0{,}045}=\\dfrac{7{,}5\\times10^{-3}}{0{,}045}\\approx0{,}17\\,\\mathrm{mol\\,L^{-1}}$ (exactamente $0{,}50/3$)."
))

# REF
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
