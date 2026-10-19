import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H1_exercises1_fullsol",
"$K_c$ pequeña garantiza que la reacción está poco desplazada hacia productos, pero «poco desplazada» es relativo: si $n_0$ también es pequeño, $x$ puede seguir siendo una fracción apreciable de $n_0$. La única forma fiable de saberlo es calcular, para el problema concreto, tanto $x_{aprox}$ (con la simplificación) como $x_{exacto}$ (resolviendo la ecuación completa) y obtener el error relativo $|x_{aprox}-x_{exacto}|/x_{exacto}$. Solo si ese error queda por debajo del criterio que se esté usando (1 % estricto, hasta 10 % en contextos más tolerantes) se acepta la aproximación.",
"$K_c$ pequeña garantiza que la reacción está poco desplazada hacia productos, pero «poco desplazada» es relativo: si $n_0$ también es pequeño, $x$ puede seguir siendo una fracción apreciable de $n_0$. La única forma fiable de saberlo es calcular $x_{aprox}$ con la simplificación y comprobar a posteriori que $x_{aprox}/c_0<0{,}05$ (es decir, que el grado de disociación $\\alpha$ sea menor del $5\\,\\%$, el criterio habitual en Bachillerato y Selectividad). Solo si se cumple esa condición se acepta la aproximación; si no, hay que resolver la ecuación de segundo grado completa."
))

edits.append(("H1_mcq3_explanation",
"La aproximación se valida comparando $x_{aprox}$ con el valor exacto y calculando el error relativo, no solo mirando el tamaño de $K_c$.",
"La aproximación se valida comprobando que $x_{aprox}/c_0<5\\,\\%$, no solo mirando el tamaño de $K_c$."
))
edits.append(("H1_mcq3_optionB",
"Calcular $x_{exacto}$ (o estimarlo) y comprobar que el error relativo frente a $x_{aprox}$ es aceptable.",
"Comprobar que $x_{aprox}/c_0$ es menor del $5\\,\\%$ (si no, resolver la ecuación completa sin aproximar)."
))

ok = apply(edits)
print("DONE", ok)
