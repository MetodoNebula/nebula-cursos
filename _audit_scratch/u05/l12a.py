import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H1a: theory_blocks[3].body - criterio 5%
edits.append(("H1_theory3_body",
"**Pero la aproximación no se da nunca por buena a ciegas**: después de calcular $x$ con ella, hay que comprobar el error relativo que introduce frente al valor exacto (resolviendo la cuadrática completa, o comparando $x_{aprox}$ con $x_{exacto}$). Un criterio práctico habitual: error estricto aceptable si es menor del $1\\,\\%$; en algunos contextos se admite como tolerable hasta el $10\\,\\%$. Si el error supera el margen que se esté usando, hay que resolver sin aproximar.",
"**Pero la aproximación no se da nunca por buena a ciegas**: tras calcular $x$ con ella, se comprueba a posteriori que $x/c_0<0{,}05$, es decir, que el grado de disociación $\\alpha=x/c_0$ sea menor del $5\\,\\%$ (el criterio habitual en Bachillerato y Selectividad). Si se cumple, la aproximación se considera válida; si no, hay que resolver la ecuación de segundo grado completa, sin aproximar."
))

# H1b: flashcards[4]
edits.append(("H1_fc4_back",
"Solo tras comprobar el error relativo frente al valor exacto: aceptable si es menor del $1\\,\\%$ (criterio estricto) o, en contextos tolerantes, hasta el $10\\,\\%$.",
"Solo tras comprobar, a posteriori, que $x_{aprox}/c_0<0{,}05$ (es decir, $\\alpha<5\\,\\%$). Si se cumple, se acepta; si no, hay que resolver la ecuación completa."
))

# H1c: flashcards[7]
edits.append(("H1_fc7_front",
"Criterio de error relativo para la aproximación",
"Criterio para validar la aproximación $(c_0-x)\\approx c_0$"
))
edits.append(("H1_fc7_back",
"Error relativo $=|x_{aprox}-x_{exacto}|/x_{exacto}$: aceptable estricto $<1\\,\\%$, tolerado en algunos contextos hasta $10\\,\\%$.",
"Se comprueba que $x_{aprox}/c_0<0{,}05$ (α$<5\\,\\%$). Si se cumple, la aproximación es válida; si no, se resuelve la ecuación completa."
))

# H1d: misconceptions[1].correct_model
edits.append(("H1_misc1_correct",
"La aproximación es una hipótesis de trabajo, no una regla automática: tras resolver con ella, hay que calcular el error relativo frente al valor exacto (o recalcular $x$ sin aproximar) y comprobar que es aceptable (criterio estricto: $<1\\,\\%$; tolerado en ciertos contextos: hasta $10\\,\\%$). Si no se cumple, hay que resolver la ecuación completa.",
"La aproximación es una hipótesis de trabajo, no una regla automática: tras resolver con ella, hay que comprobar que $x_{aprox}/c_0<0{,}05$ (α$<5\\,\\%$), el criterio habitual en Bachillerato y Selectividad. Si no se cumple, hay que resolver la ecuación completa, sin aproximar."
))

ok = apply(edits)
print("DONE", ok)
