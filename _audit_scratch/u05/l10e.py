import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H8: sustituir el reto trivial por uno que combine invertir+multiplicar+sumar
edits.append(("H8_challenge_statement",
"Dadas las reacciones, todas a la misma temperatura: (1) $\\text{A}\\rightleftharpoons2\\,\\text{B}$, $K_{c,1}=0{,}0500$; (2) $2\\,\\text{B}\\rightleftharpoons\\text{C}+\\text{D}$, $K_{c,2}=8{,}00$. Calcula la constante de equilibrio $K_c$ de la reacción global $\\text{A}\\rightleftharpoons\\text{C}+\\text{D}$, y explica cada paso de la manipulación usada.",
"Dadas las reacciones, todas a la misma temperatura: (1) $\\text{N}_2(g)+\\text{O}_2(g)\\rightleftharpoons2\\,\\text{NO}(g)$, $K_{c,1}=4{,}1\\times10^{-4}$; (2) $2\\,\\text{NO}(g)+\\text{O}_2(g)\\rightleftharpoons2\\,\\text{NO}_2(g)$, $K_{c,2}=1{,}0\\times10^{4}$. Calcula la constante de equilibrio $K_c$ de la reacción $\\text{NO}_2(g)\\rightleftharpoons\\tfrac{1}{2}\\,\\text{N}_2(g)+\\text{O}_2(g)$, explicando cada paso (invertir, multiplicar los coeficientes por un factor y sumar ecuaciones) de la manipulación usada."
))

edits.append(("H8_challenge_hints",
"[\"Comprueba que sumar las ecuaciones (1) y (2) tal cual da exactamente la reacción global pedida, sin necesidad de multiplicar ninguna por un número adicional.\", \"Aplica la regla del producto de constantes para una suma de etapas.\"]",
"[\"Primero invierte y suma (1) y (2) para obtener $2\\\\,\\\\text{NO}_2(g)\\\\rightleftharpoons\\\\text{N}_2(g)+2\\\\,\\\\text{O}_2(g)$; después multiplica esa ecuación por $\\\\tfrac{1}{2}$ para llegar a la reacción pedida.\", \"Recuerda: sumar ecuaciones multiplica las constantes; multiplicar los coeficientes por $n$ eleva la constante a la potencia $n$.\"]"
))

ok = apply(edits)
print("DONE", ok)
