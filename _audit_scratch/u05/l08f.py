import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []
edits.append(("H6_fc5_front",
"Efecto de aumentar T frente a efecto de aumentar Ea sobre k",
"Efecto de aumentar $T$ frente a efecto de aumentar $E_a$ sobre $k$"
))
edits.append(("H6_fc9_front",
"A=5,0×10¹¹ s⁻¹, Ea=75,0 kJ/mol, T=298 K. ¿k?",
"$A=5{,}0\\times10^{11}\\,\\mathrm{s^{-1}}$, $E_a=75{,}0\\,\\mathrm{kJ\\,mol^{-1}}$, $T=298\\,\\mathrm{K}$. ¿$k$?"
))
edits.append(("H6_cm1_howtoavoid",
"Calcular explícitamente el cociente k2/k1 en vez de estimarlo intuitivamente, recordando que la relación es exponencial, no lineal.",
"Calcular explícitamente el cociente $k_2/k_1$ en vez de estimarlo intuitivamente, recordando que la relación es exponencial, no lineal."
))
ok = apply(edits)
print("DONE", ok)
