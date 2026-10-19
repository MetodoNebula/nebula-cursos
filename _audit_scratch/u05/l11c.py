import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H7_WE0_statement",
"Para $CO(g)+H_2O(g)\\rightleftharpoons CO_2(g)+H_2(g)$ a $800$ K, $K_c=4{,}40$. Calcula $K_p$ a esa temperatura.",
"Para $\\text{CO}(g)+\\text{H}_2\\text{O}(g)\\rightleftharpoons\\text{CO}_2(g)+\\text{H}_2(g)$ a $800\\,\\mathrm{K}$, $K_c=4{,}40$. Calcula $K_p$ a esa temperatura."
))

edits.append(("H9_exercises1_statement",
"Deduce, partiendo de $P_i=[\\,i\\,]RT$, qué relación hay entre $K_x$ (con fracciones molares) y $K_p$, sabiendo que $P_i=\\chi_i P_{total}$. ¿De qué depende $K_x$ además de la temperatura?",
"(Contenido de ampliación, no exigible en Selectividad.) Deduce, a partir de $P_i=\\chi_i P_{total}$ (ley de Dalton), qué relación hay entre $K_x$ (con fracciones molares) y $K_p$. ¿De qué depende $K_x$ además de la temperatura?"
))

ok = apply(edits)
print("DONE", ok)
