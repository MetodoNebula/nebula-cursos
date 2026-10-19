import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []
edits.append(("H4_challenge_fullsol",
"$[\\text{B}]_{\\text{eq}}=1{,}00-0{,}286=0{,}714$ mol/L. (Comprobación: $0{,}714/0{,}286\\approx2{,}50=k_+/k_-$ ✓.)",
"$[\\text{B}]_{\\text{eq}}=1{,}00-0{,}286=0{,}714$ mol/L. (Comprobación: $0{,}714/0{,}286\\approx2{,}50=k_+/k_-$ ✓.) En el equilibrio, $v_+=k_+[\\text{A}]_{\\text{eq}}=0{,}050\\times0{,}286=1{,}43\\times10^{-2}\\,\\mathrm{mol\\,L^{-1}\\,s^{-1}}$ y $v_-=k_-[\\text{B}]_{\\text{eq}}=0{,}020\\times0{,}714=1{,}43\\times10^{-2}\\,\\mathrm{mol\\,L^{-1}\\,s^{-1}}$: iguales entre sí y distintas de cero, confirmando que el equilibrio es dinámico."
))

ok = apply(edits)
print("DONE", ok)
