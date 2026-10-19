import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H5: A mismas unidades que k
edits.append(("H5_theory1_A_units",
"donde $A$ es el factor de frecuencia (relacionado con la frecuencia de colisiones y su orientación, prácticamente constante para una reacción dada), $E_a$ es la energía de activación (en J/mol), $R=8{,}314$ J·mol⁻¹·K⁻¹ es la constante de los gases, y $T$ es la temperatura absoluta (en K).",
"donde $A$ es el factor de frecuencia (relacionado con la frecuencia de colisiones y su orientación, prácticamente constante para una reacción dada), $E_a$ es la energía de activación (en J/mol), $R=8{,}314$ J·mol⁻¹·K⁻¹ es la constante de los gases, y $T$ es la temperatura absoluta (en K). Como el término exponencial es adimensional, $A$ tiene exactamente las mismas unidades que $k$ (lección 6: Unidades de la constante de velocidad k): $\\mathrm{s^{-1}}$ para una reacción de orden 1, $\\mathrm{L\\,mol^{-1}\\,s^{-1}}$ para orden 2, etc."
))

# H4: mcq[0].options[3].why_wrong - matizar
edits.append(("H4_mcq0_opt3",
"Ea es siempre positiva (por definición, es una energía de activación); no existe el caso de Ea negativa que haría depender la respuesta de su signo.",
"En las reacciones que se estudian en este nivel, Ea es positiva (es la barrera energética que hay que superar para llegar al complejo activado), así que la respuesta no depende de su signo."
))

# H6: worked_examples[0].statement - LaTeX unidades
edits.append(("H6_WE0_statement",
"Para una reacción con $A=5{,}0\\times10^{11}$ s⁻¹ y $E_a=75{,}0$ kJ/mol, calcula k a 298 K y a 308 K, y el cociente $k_2/k_1$.",
"Para una reacción con $A=5{,}0\\cdot10^{11}\\,\\mathrm{s^{-1}}$ y $E_a=75{,}0\\,\\mathrm{kJ\\,mol^{-1}}$, calcula k a 298 K y a 308 K, y el cociente $k_2/k_1$."
))

# REF prerequisites[0]
edits.append(("REF_prereq0",
"Conocer la energía de activación Ea y la teoría de colisiones: solo los choques con energía suficiente y orientación adecuada son eficaces (lección el apartado correspondiente).",
"Conocer la energía de activación Ea y la teoría de colisiones: solo los choques con energía suficiente y orientación adecuada son eficaces (lección 2: Teoría de colisiones y energía de activación)."
))

# REF theory_blocks[0].body
edits.append(("REF_theory0_body",
"Según la teoría de colisiones (el apartado correspondiente), solo una fracción de los choques tiene energía suficiente para superar la energía de activación.",
"Según la teoría de colisiones (lección 2: Teoría de colisiones y energía de activación), solo una fracción de los choques tiene energía suficiente para superar la energía de activación."
))

ok = apply(edits)
print("DONE", ok)
