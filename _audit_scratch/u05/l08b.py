import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H1_WE1_solution",
"$k_{40}\\approx4{,}87\\times10^{4}$ s⁻¹; $k_{40}/k_{75}\\approx1{,}37\\times10^{6}$.",
"$k_{40}=5{,}0\\cdot10^{11}\\,e^{-40000/(8{,}314\\cdot298)}=5{,}0\\cdot10^{11}\\,e^{-16{,}14}\\approx4{,}87\\times10^{4}\\,\\mathrm{s^{-1}}$; $k_{40}/k_{75}=e^{30{,}27-16{,}14}=e^{14{,}13}\\approx1{,}37\\times10^{6}$."
))

edits.append(("H7_WE1_interpretation",
"Reducir Ea de 75 a 40 kJ/mol (una reducción del 47%, similar a la de un catalizador típico) multiplica k por más de un millón: esto ilustra por qué los catalizadores, aun con reducciones de Ea que parecen modestas en términos relativos, pueden acelerar enormemente una reacción.",
"Reducir Ea de 75 a 40 kJ/mol (una reducción del 47 %) multiplica k por más de un millón: esto ilustra por qué los catalizadores, aun con reducciones de Ea que a veces parecen modestas en términos relativos, pueden acelerar enormemente una reacción."
))

edits.append(("H7_WE1_commonmistake",
"Esperar que una reducción de Ea del 47% se traduzca en un aumento de k también de un orden de magnitud parecido (por ejemplo, ×2), sin tener en cuenta que la relación entre Ea y k es exponencial, no proporcional.",
"Pensar que reducir Ea a la mitad (o un 47 %) hace que k aumente aproximadamente al doble, cuando la dependencia exponencial la multiplica realmente por un factor enorme (aquí, ×1,37·10⁶), porque la relación entre Ea y k es exponencial, no proporcional."
))

edits.append(("REF_WE1_reasoning1",
"El cociente muestra el efecto de reducir Ea manteniendo T constante, que es exactamente el mecanismo por el que actúa un catalizador (el apartado correspondiente).",
"El cociente muestra el efecto de reducir Ea manteniendo T constante, que es exactamente el mecanismo por el que actúa un catalizador (lección 7: Catalizadores y perfil energético)."
))

ok = apply(edits)
print("DONE", ok)
