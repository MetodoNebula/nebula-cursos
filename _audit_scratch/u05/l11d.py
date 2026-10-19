import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []
edits.append(("TEMPLATE_exam1_markscheme",
'"mark_scheme": [\n  "1 punto por cada apartado correctamente calificado y justificado"\n ],\n "common_errors": [\n  "En (c), decir que sí coinciden las unidades',
'"mark_scheme": [\n  "1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con la relación $K_p=K_c(RT)^{\\\\Delta n}$ y la naturaleza física de cada constante"\n ],\n "common_errors": [\n  "En (c), decir que sí coinciden las unidades'
))
ok = apply(edits)
print("DONE", ok)
