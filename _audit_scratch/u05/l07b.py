import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H4: exam_questions[0] - cambiar a caso endotermico (datos distintos de WE2)
edits.append(("H4_exam0_statement",
"Una reacción exotérmica tiene $E_{a,\\text{dir}}=65$ kJ/mol y $\\Delta H=-45$ kJ/mol. (a) Calcula $E_{a,\\text{inv}}$ sin catalizar. (b) Un catalizador reduce $E_{a,\\text{dir}}$ a 30 kJ/mol; calcula $E_{a,\\text{inv}}^{\\text{con}}$. (c) Dibuja (describe en palabras) cómo cambia el perfil energético con el catalizador respecto al original, señalando qué partes del perfil cambian y cuáles no.",
"Una reacción endotérmica tiene $E_{a,\\text{dir}}=120$ kJ/mol y $\\Delta H=+50$ kJ/mol. (a) Calcula $E_{a,\\text{inv}}$ sin catalizar. (b) Un catalizador reduce $E_{a,\\text{dir}}$ a 85 kJ/mol; calcula $E_{a,\\text{inv}}^{\\text{con}}$. (c) Dibuja (describe en palabras) cómo cambia el perfil energético con el catalizador respecto al original, señalando qué partes del perfil cambian y cuáles no."
))

edits.append(("H4_exam0_answer",
"(a) $E_{a,\\text{inv}}^{\\text{sin}}=110$ kJ/mol. (b) $E_{a,\\text{inv}}^{\\text{con}}=75$ kJ/mol. (c) Baja el máximo (estado de transición) en 35 kJ/mol; los niveles de reactivos y de productos (y, por tanto, ΔH) permanecen iguales.",
"(a) $E_{a,\\text{inv}}^{\\text{sin}}=70$ kJ/mol. (b) $E_{a,\\text{inv}}^{\\text{con}}=35$ kJ/mol. (c) Baja el máximo (estado de transición) en 35 kJ/mol; los niveles de reactivos y de productos (y, por tanto, ΔH) permanecen iguales."
))

edits.append(("H4_exam0_fullsol",
"(a) $E_{a,\\text{inv}}^{\\text{sin}}=65-(-45)=110$ kJ/mol.\n\n(b) $E_{a,\\text{inv}}^{\\text{con}}=30-(-45)=75$ kJ/mol.\n\n(c) En el nuevo perfil, el máximo (estado de transición) está 35 kJ/mol más bajo que en el perfil sin catalizar (tanto medido desde reactivos como desde productos, ya que $65-30=110-75=35$). Los niveles de energía de reactivos y de productos permanecen exactamente en la misma posición que antes, por lo que ΔH no cambia.",
"(a) $E_{a,\\text{inv}}^{\\text{sin}}=120-50=70$ kJ/mol.\n\n(b) $E_{a,\\text{inv}}^{\\text{con}}=85-50=35$ kJ/mol.\n\n(c) En el nuevo perfil, el máximo (estado de transición) está 35 kJ/mol más bajo que en el perfil sin catalizar (tanto medido desde reactivos como desde productos, ya que $120-85=70-35=35$). Los niveles de energía de reactivos (a 0 kJ/mol) y de productos (a $+50$ kJ/mol) permanecen exactamente en la misma posición que antes, por lo que ΔH no cambia; solo baja el complejo activado, de 120 a 85 kJ/mol."
))

edits.append(("H4_exam0_commonerr",
"En (c), describir el nuevo perfil como si los productos quedaran a una energía distinta (más baja), en vez de limitar el cambio exclusivamente al máximo intermedio.",
"En (c), describir el nuevo perfil como si los productos quedaran a una energía distinta (más baja o más alta), en vez de limitar el cambio exclusivamente al máximo intermedio."
))

# H5: challenge_questions[0] - matizar modelo del inhibidor
edits.append(("H5_challenge_statement",
"Un inhibidor es una sustancia que hace exactamente lo contrario que un catalizador: en vez de ofrecer un camino alternativo más fácil, dificulta el camino existente, aumentando la energía de activación. Para una reacción con $E_{a,\\text{dir}}=75$ kJ/mol y $\\Delta H=-50$ kJ/mol, un inhibidor aumenta $E_{a,\\text{dir}}$ en 20 kJ/mol. Calcula la nueva $E_{a,\\text{inv}}$ con inhibidor, y razona si el inhibidor desplaza o no la posición de equilibrio.",
"Un inhibidor (o veneno de catalizador) bloquea el camino rápido que seguiría la reacción con un catalizador, de modo que esta transcurre por un camino de mayor energía de activación: el efecto neto es como si $E_{a,\\text{dir}}$ aumentara. Para una reacción con $E_{a,\\text{dir}}=75$ kJ/mol y $\\Delta H=-50$ kJ/mol, un inhibidor hace que la reacción transcurra con una $E_{a,\\text{dir}}$ efectiva 20 kJ/mol mayor. Calcula la nueva $E_{a,\\text{inv}}$ con inhibidor, y razona si el inhibidor desplaza o no la posición de equilibrio."
))

edits.append(("H5_keywords2",
"Sustancia que aumenta la energía de activación de una reacción, ralentizándola, sin cambiar tampoco ΔH ni la posición de equilibrio.",
"Sustancia (a menudo un veneno de catalizador) que bloquea el camino rápido de la reacción, de modo que esta transcurre por un camino de mayor energía de activación efectiva, ralentizándola sin cambiar tampoco ΔH ni la posición de equilibrio."
))

ok = apply(edits)
print("DONE", ok)
