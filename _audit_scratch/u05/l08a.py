import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H1a: WE0 solution - mostrar exponentes
edits.append(("H1_WE0_solution",
"$k_1\\approx3{,}57\\times10^{-2}$ s⁻¹ (298 K); $k_2\\approx9{,}53\\times10^{-2}$ s⁻¹ (308 K); $k_2/k_1\\approx2{,}67$.",
"$k_1=5{,}0\\cdot10^{11}\\,e^{-75000/(8{,}314\\cdot298)}=5{,}0\\cdot10^{11}\\,e^{-30{,}27}=3{,}57\\times10^{-2}\\,\\mathrm{s^{-1}}$ (298 K); $k_2=5{,}0\\cdot10^{11}\\,e^{-75000/(8{,}314\\cdot308)}=5{,}0\\cdot10^{11}\\,e^{-29{,}29}=9{,}53\\times10^{-2}\\,\\mathrm{s^{-1}}$ (308 K); $k_2/k_1=e^{30{,}27-29{,}29}=e^{0{,}98}\\approx2{,}67$."
))

ok = apply(edits)
print("DONE", ok)
