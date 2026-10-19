import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H8_flashcard5_front",
"Ea,dir=75, ΔH=−50. Con catalizador, Ea,dir=40. ¿Ea,inv con catalizador?",
"$E_{a,\\text{dir}}=75$, $\\Delta H=-50$. Con catalizador, $E_{a,\\text{dir}}=40$. ¿$E_{a,\\text{inv}}$ con catalizador?"
))

edits.append(("H8_flashcard6_front",
"¿Qué condición física debe cumplir siempre Ea,inv, aunque se reduzca mucho con un catalizador?",
"¿Qué condición física debe cumplir siempre $E_{a,\\text{inv}}$, aunque se reduzca mucho con un catalizador?"
))

edits.append(("H8_commonmistakes2",
"No comprobar que el resultado de Ea,inv tras catalizar sea físicamente razonable (no negativo).",
"No comprobar que el resultado de $E_{a,\\text{inv}}$ tras catalizar sea físicamente razonable (no negativo)."
))

edits.append(("H8_summary_kp3",
"Ea,inv nunca puede resultar negativa: eso limita cuánto puede reducir Ea,dir un catalizador real.",
"$E_{a,\\text{inv}}$ nunca puede resultar negativa: eso limita cuánto puede reducir $E_{a,\\text{dir}}$ un catalizador real."
))

# H9: etiquetas TS -> ET sin cat./ET con cat.
edits.append(("H9_tikz_label_sin",
'{TS\\\\sin cat.}',
'{ET\\\\sin cat.}'
))
edits.append(("H9_tikz_label_con",
'{TS\\\\con cat.}',
'{ET\\\\con cat.}'
))

ok = apply(edits)
print("DONE", ok)
