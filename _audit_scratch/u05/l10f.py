import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H8_challenge_statement",
"Dadas las reacciones, todas a la misma temperatura: (1) $\\text{A}\\rightleftharpoons2\\,\\text{B}$, $K_{c,1}=0{,}0500$; (2) $2\\,\\text{B}\\rightleftharpoons\\text{C}+\\text{D}$, $K_{c,2}=8{,}00$. Calcula la constante de equilibrio $K_c$ de la reacción global $\\text{A}\\rightleftharpoons\\text{C}+\\text{D}$, y explica cada paso de la manipulación usada.",
"Dadas las reacciones, todas a la misma temperatura: (1) $\\text{N}_2(g)+\\text{O}_2(g)\\rightleftharpoons2\\,\\text{NO}(g)$, $K_{c,1}=4{,}1\\times10^{-4}$; (2) $2\\,\\text{NO}(g)+\\text{O}_2(g)\\rightleftharpoons2\\,\\text{NO}_2(g)$, $K_{c,2}=1{,}0\\times10^{4}$. Calcula la constante de equilibrio $K_c$ de la reacción $\\text{NO}_2(g)\\rightleftharpoons\\tfrac{1}{2}\\,\\text{N}_2(g)+\\text{O}_2(g)$, explicando cada paso (invertir, multiplicar los coeficientes por un factor y sumar ecuaciones) de la manipulación usada."
))

edits.append(("H8_challenge_hint0",
"Comprueba que sumar las ecuaciones (1) y (2) tal cual da exactamente la reacción global pedida, sin necesidad de multiplicar ninguna por un número adicional.",
"Primero invierte (1) y (2) y súmalas para obtener $2\\,\\text{NO}_2(g)\\rightleftharpoons\\text{N}_2(g)+2\\,\\text{O}_2(g)$ con $K_c=1/(K_{c,1}K_{c,2})$; después multiplica esa ecuación por $\\tfrac{1}{2}$ para llegar a la reacción pedida."
))

edits.append(("H8_challenge_hint1",
"Aplica la regla del producto de constantes para una suma de etapas.",
"Recuerda: sumar ecuaciones multiplica las constantes; multiplicar los coeficientes de una ecuación por $n$ eleva su constante a la potencia $n$."
))

edits.append(("H8_challenge_answer",
"$K_c=0{,}400$.",
"$K_c=0{,}49\\,\\mathrm{mol^{1/2}\\,L^{-1/2}}$."
))

edits.append(("H8_challenge_fullsol",
"Sumando (1) A⇌2B y (2) 2B⇌C+D: el término 2B aparece como producto en (1) y como reactivo en (2), así que se cancela exactamente (ambas con el mismo coeficiente 2, sin necesidad de ajustar ninguna de las dos ecuaciones), dejando la reacción global $\\text{A}\\rightleftharpoons\\text{C}+\\text{D}$.\n\nPor la regla de suma de etapas: $K_c=K_{c,1}\\times K_{c,2}=0{,}0500\\times8{,}00=0{,}400$.\n\nA diferencia de otros casos en los que hay que multiplicar previamente una de las ecuaciones por un factor para que los términos intermedios se cancelen exactamente, aquí ambas ecuaciones ya comparten el mismo coeficiente (2) para B, así que no hace falta ningún ajuste adicional antes de multiplicar las constantes.",
"Invirtiendo (1): $2\\,\\text{NO}(g)\\rightleftharpoons\\text{N}_2(g)+\\text{O}_2(g)$, $K_{c,1}'=1/K_{c,1}=1/(4{,}1\\times10^{-4})\\approx2{,}44\\times10^{3}$.\n\nInvirtiendo (2): $2\\,\\text{NO}_2(g)\\rightleftharpoons2\\,\\text{NO}(g)+\\text{O}_2(g)$, $K_{c,2}'=1/K_{c,2}=1/(1{,}0\\times10^{4})=1{,}0\\times10^{-4}$.\n\nSumando ambas ecuaciones invertidas: el término $2\\,\\text{NO}(g)$ aparece como producto en la primera y como reactivo en la segunda, así que se cancela, dejando $2\\,\\text{NO}_2(g)\\rightleftharpoons\\text{N}_2(g)+2\\,\\text{O}_2(g)$, con $K_c=K_{c,1}'\\times K_{c,2}'=2{,}44\\times10^{3}\\times1{,}0\\times10^{-4}\\approx0{,}244$.\n\nEsta ecuación tiene todos los coeficientes el doble de los de la reacción pedida ($\\text{NO}_2(g)\\rightleftharpoons\\tfrac{1}{2}\\text{N}_2(g)+\\text{O}_2(g)$); al multiplicar los coeficientes por $\\tfrac{1}{2}$, la constante se eleva a la potencia $\\tfrac{1}{2}$: $K_c=\\sqrt{0{,}244}\\approx0{,}49$."
))

edits.append(("H8_challenge_commonerr",
"No comprobar que los coeficientes del término intermedio (B) coinciden exactamente entre las dos ecuaciones antes de sumarlas directamente; si no coincidieran, habría que multiplicar primero una de las ecuaciones por el factor adecuado (y elevar su Kc a esa misma potencia) antes de poder sumarlas y multiplicar las constantes.",
"Sumar (1) y (2) directamente sin invertirlas antes, o multiplicar Kc por $\\tfrac12$ en vez de elevarlo a la potencia $\\tfrac12$ en el último paso, confundiendo la regla de 'multiplicar coeficientes' con una operación lineal sobre Kc."
))

ok = apply(edits)
print("DONE", ok)
