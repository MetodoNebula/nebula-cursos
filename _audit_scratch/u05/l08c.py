import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H2_exam0_fullsol",
"$k_{300}=2{,}0\\times10^{12}\\cdot e^{-60000/(8{,}314\\times300)}\\approx71{,}4$ s⁻¹.\n\n$k_{310}=2{,}0\\times10^{12}\\cdot e^{-60000/(8{,}314\\times310)}\\approx155$ s⁻¹.",
"$k_{300}=2{,}0\\times10^{12}\\cdot e^{-60000/(8{,}314\\times300)}=2{,}0\\times10^{12}\\cdot e^{-24{,}06}\\approx71{,}4$ s⁻¹.\n\n$k_{310}=2{,}0\\times10^{12}\\cdot e^{-60000/(8{,}314\\times310)}=2{,}0\\times10^{12}\\cdot e^{-23{,}28}\\approx155$ s⁻¹."
))

edits.append(("H2_exercises0_fullsol",
"$k_{70}=5{,}0\\times10^{11}\\cdot e^{-70000/(8{,}314\\times298)}\\approx2{,}68\\times10^{-1}$ s⁻¹. $k_{70}/k_{75}=2{,}68\\times10^{-1}/3{,}57\\times10^{-2}\\approx7{,}52$.",
"$k_{70}=5{,}0\\times10^{11}\\cdot e^{-70000/(8{,}314\\times298)}=5{,}0\\times10^{11}\\cdot e^{-28{,}25}\\approx2{,}68\\times10^{-1}$ s⁻¹. $k_{70}/k_{75}=2{,}68\\times10^{-1}/3{,}57\\times10^{-2}\\approx7{,}52$ (comprobación: $e^{30{,}27-28{,}25}=e^{2{,}02}\\approx7{,}5$)."
))

edits.append(("REF_exercises1_hints0",
"Relaciona la dependencia exponencial de k con Ea del ejercicio anterior con el mecanismo de acción de un catalizador (el apartado correspondiente).",
"Relaciona la dependencia exponencial de k con Ea del ejercicio anterior con el mecanismo de acción de un catalizador (lección 7: Catalizadores y perfil energético)."
))

ok = apply(edits)
print("DONE", ok)
