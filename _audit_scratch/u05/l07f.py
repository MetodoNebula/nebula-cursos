import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("TEMPLATE_theory4_title_L07",
'"id": "TH-Q05-07-5",\n        "type": "caveat",\n        "title": "Ideas equivocadas que conviene desmontar",',
'"id": "TH-Q05-07-5",\n        "type": "caveat",\n        "title": "Errores habituales sobre catalizadores y equilibrio",'
))

edits.append(("TEMPLATE_exam1_markscheme0",
"1 punto por cada apartado correctamente calificado y justificado",
"1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con el efecto del catalizador sobre Ea, ΔH y la posición de equilibrio"
))

edits.append(("TEMPLATE_exam1_markscheme1",
"Sin justificación, 0 puntos aunque la calificación V/F sea correcta",
"Sin justificar con estos conceptos, no se otorga ningún punto aunque la calificación V/F sea correcta"
))

ok = apply(edits)
print("DONE", ok)
