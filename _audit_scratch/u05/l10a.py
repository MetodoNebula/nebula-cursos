import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("REF_exam1_statement",
"Explica, en una o dos frases, por qué los exponentes de la expresión de Kc son siempre los coeficientes estequiométricos de la ecuación ajustada, mientras que los exponentes de la ley de velocidad (lección el apartado correspondiente) son datos experimentales que no tienen por qué coincidir con ellos.",
"Explica, en una o dos frases, por qué los exponentes de la expresión de Kc son siempre los coeficientes estequiométricos de la ecuación ajustada, mientras que los exponentes de la ley de velocidad (lección 4: Ley de velocidad) son datos experimentales que no tienen por qué coincidir con ellos."
))

edits.append(("H1_exam1_fullsol",
"La expresión de Kc surge de la condición de equilibrio ($v_+=v_-$ generalizada, el apartado correspondiente), una propiedad del **estado final** del sistema que no depende de cómo se llegó a él paso a paso; por eso sus exponentes son siempre los coeficientes de la ecuación ajustada, sea la reacción elemental o compleja. La ley de velocidad, en cambio, describe la **velocidad instantánea** del proceso, que sí depende del mecanismo real paso a paso (cuántas moléculas chocan realmente en cada etapa elemental); por eso sus exponentes (los órdenes) son, en general, distintos de los coeficientes estequiométricos, salvo que la reacción sea elemental (el apartado correspondiente).",
"Kc es una magnitud termodinámica del estado de equilibrio, independiente del camino por el que se llegó a él. Si la reacción transcurre por varias etapas elementales, en el equilibrio cada etapa cumple $v_+=v_-$ (lección 9: Equilibrio químico dinámico) y su propia $K_i=k_{+,i}/k_{-,i}$; al multiplicar las $K_i$ de todas las etapas, las especies intermedias se cancelan y queda siempre la expresión con los coeficientes de la ecuación global, sea la reacción elemental o compleja. La ley de velocidad, en cambio, depende solo de la etapa más lenta del mecanismo; por eso sus exponentes (los órdenes) son, en general, datos experimentales distintos de los coeficientes estequiométricos, y solo coinciden con seguridad con ellos cuando la reacción es elemental (lección 4: Ley de velocidad)."
))

ok = apply(edits)
print("DONE", ok)
