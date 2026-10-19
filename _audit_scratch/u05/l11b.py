import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H2_fc4_back",
"En atm: $R=0{,}082$ atm·L/(mol·K). En Pa: $R=8{,}314$ J/(mol·K). No se mezclan en el mismo problema.",
"Con presiones en atm y concentraciones en mol/L: $R=0{,}082$ atm·L/(mol·K). Con $R=8{,}314$ J·mol⁻¹·K⁻¹ $=8{,}314$ Pa·m³·mol⁻¹·K⁻¹, las concentraciones deben ir en mol/m³ para que $K_p$ salga en Pa (si se usan mol/L, $K_p$ sale en kPa). No se mezclan unidades distintas en el mismo problema."
))

edits.append(("H4_examnotes2",
"Conviene saber razonar, sin calculadora, si $K_p$ debe salir mayor o menor que $K_c$ con solo mirar el signo de $\\Delta n$: es una pregunta de examen habitual, incluso sin pedir el cálculo completo.",
"Conviene saber razonar, sin calculadora, si $K_p$ debe salir mayor o menor que $K_c$ con solo mirar el signo de $\\Delta n$ (como en la práctica $RT>1$ —con $R=0{,}082$, basta $T>12{,}2$ K—, $\\Delta n>0\\Rightarrow K_p>K_c$ y $\\Delta n<0\\Rightarrow K_p<K_c$): es una pregunta de examen habitual, incluso sin pedir el cálculo completo."
))

edits.append(("H5_misc1_correct",
"El exponente es literalmente $\\Delta n$, con su signo: si $\\Delta n<0$, $(RT)^{\\Delta n}=1/(RT)^{|\\Delta n|}$, y $K_p$ resulta menor que $K_c\\cdot RT$, no mayor.",
"El exponente es literalmente $\\Delta n$, con su signo: si $\\Delta n<0$, $(RT)^{\\Delta n}=1/(RT)^{|\\Delta n|}$, así que $K_p=K_c/(RT)^{|\\Delta n|}$ es menor que $K_c$ (para $RT>1$): hay que dividir por $(RT)^{|\\Delta n|}$, no multiplicar."
))

edits.append(("H6_exam0_answer",
"(a) $\\Delta n=1$. (b) $K_c=0{,}0223$. (c) mol/L.",
"(a) $\\Delta n=1$. (b) $K_c=0{,}0223\\,\\mathrm{mol\\,L^{-1}}$. (c) mol/L, porque $\\Delta n=+1$."
))

ok = apply(edits)
print("DONE", ok)
