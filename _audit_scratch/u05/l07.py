import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H1: theory_blocks[3].body - justificación catalizador/equilibrio
edits.append(("H1_theory3", 
"Como el catalizador acelera igual la reacción directa y la inversa, y no cambia ΔH, **no altera la posición de equilibrio** de una reacción reversible: las concentraciones de equilibrio son las mismas con catalizador que sin él. Lo único que cambia es el **tiempo** que se tarda en alcanzar ese equilibrio, que es mucho menor con catalizador.",
"El catalizador multiplica por el mismo factor las constantes de velocidad directa e inversa, porque reduce en la misma cantidad $E_{a,\\text{dir}}$ y $E_{a,\\text{inv}}$: la relación entre ambas constantes —que es la que determina la posición de equilibrio— no cambia. Además, el catalizador no modifica ΔH ni ΔG de la reacción (son funciones de estado que solo dependen del estado inicial y final de reactivos y productos), por lo que tampoco puede hacer espontánea una reacción que no lo sea. Por todo ello, **no altera la posición de equilibrio** de una reacción reversible: las concentraciones de equilibrio son las mismas con catalizador que sin él. Lo único que cambia es el **tiempo** que se tarda en alcanzar ese equilibrio, que es mucho menor con catalizador."
))

# H1b: mcq[2] explanation (ligero ajuste)
edits.append(("H1_mcq2_explanation",
"Al no cambiar ΔH y acelerar igual ambos sentidos, la relación entre las velocidades directa e inversa en el equilibrio es la misma con o sin catalizador.",
"Al reducir igual $E_{a,\\text{dir}}$ y $E_{a,\\text{inv}}$, el catalizador multiplica por el mismo factor las constantes de velocidad directa e inversa, y no cambia ΔH ni ΔG: la relación entre las velocidades directa e inversa en el equilibrio es la misma con o sin catalizador."
))

# H1c: exercises[1] full_solution - añadir mención de ΔG
edits.append(("H1_exercises1_fullsol",
"El equilibrio se alcanza cuando la velocidad directa y la velocidad inversa se igualan. El catalizador reduce la Ea directa y la Ea inversa en la misma cantidad, acelerando ambas velocidades en una proporción equivalente. Por tanto, el punto en el que ambas velocidades se igualan (la posición de equilibrio) no cambia: lo único que cambia es el tiempo necesario para llegar hasta él, que es mucho menor con catalizador.",
"El equilibrio se alcanza cuando la velocidad directa y la velocidad inversa se igualan. El catalizador reduce la Ea directa y la Ea inversa en la misma cantidad, acelerando ambas velocidades en una proporción equivalente. Por tanto, el punto en el que ambas velocidades se igualan (la posición de equilibrio) no cambia: lo único que cambia es el tiempo necesario para llegar hasta él, que es mucho menor con catalizador. Tampoco cambia ΔG de la reacción (función de estado), así que un catalizador nunca puede hacer espontánea una reacción que no lo sea."
))

# H1d: worked_examples[2].solution (c) - añadir ΔG
edits.append(("H1_WE2_solution_c",
"(c) El catalizador no cambia ΔH (los niveles de reactivos y productos son los mismos) y acelera por igual la reacción directa e inversa (la misma reducción de Ea en ambos sentidos), así que la relación entre las velocidades directa e inversa en el equilibrio no se altera: solo se llega más rápido a la misma posición de equilibrio.",
"(c) El catalizador no cambia ΔH (los niveles de reactivos y productos son los mismos) y acelera por igual la reacción directa e inversa (la misma reducción de Ea en ambos sentidos), así que la relación entre las velocidades directa e inversa en el equilibrio no se altera: solo se llega más rápido a la misma posición de equilibrio. Tampoco cambia ΔG, por lo que un catalizador no puede hacer espontánea una reacción que no lo sea."
))

# H2: guided_exercises[1] - reformular como pregunta "¿es posible?"
edits.append(("H2_GE1_statement",
"Una reacción endotérmica tiene $E_{a,\\text{dir}}=100$ kJ/mol y $\\Delta H=+80$ kJ/mol. Calcula $E_{a,\\text{inv}}$ sin catalizar, y con catalizar si $E_{a,\\text{dir}}$ se reduce a 55 kJ/mol.",
"Una reacción endotérmica tiene $E_{a,\\text{dir}}=100$ kJ/mol y $\\Delta H=+80$ kJ/mol. (a) Calcula $E_{a,\\text{inv}}$ sin catalizar. (b) Un compañero afirma que un catalizador puede reducir $E_{a,\\text{dir}}$ hasta 55 kJ/mol. ¿Es eso posible? Justifica y, si no lo es, calcula el valor mínimo teórico que podría alcanzar $E_{a,\\text{dir}}$ con catalizador."
))

edits.append(("H2_GE1_hints",
"El signo positivo de ΔH hace que $E_{a,\\text{inv}}$ sea menor que $E_{a,\\text{dir}}$, al revés que en una reacción exotérmica.",
"El signo positivo de ΔH hace que $E_{a,\\text{inv}}$ sea menor que $E_{a,\\text{dir}}$, al revés que en una reacción exotérmica. Antes de aceptar el dato de 55 kJ/mol, comprueba el signo que saldría para $E_{a,\\text{inv}}^{\\text{con}}$."
))

ok = apply(edits)
print("DONE", ok)
