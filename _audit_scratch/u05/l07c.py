import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

# H7: añadir el límite Ea,inv >= 0 a la teoría (TH-Q05-07-3)
edits.append(("H7_theory3_limite",
"Una forma útil de comprobar un cálculo es recalcular $E_{a,\\text{inv}}^{\\text{cat}}=E_{a,\\text{dir}}^{\\text{cat}}-\\Delta H$ y verificar que coincide con restar $\\Delta E_a$ directamente a la $E_{a,\\text{inv}}$ original.",
"Una forma útil de comprobar un cálculo es recalcular $E_{a,\\text{inv}}^{\\text{cat}}=E_{a,\\text{dir}}^{\\text{cat}}-\\Delta H$ y verificar que coincide con restar $\\Delta E_a$ directamente a la $E_{a,\\text{inv}}$ original. Como ninguna energía de activación puede ser negativa, $E_{a,\\text{inv}}^{\\text{cat}}\\ge0$ limita cuánto puede reducir un catalizador real la $E_{a,\\text{dir}}$: en una reacción endotérmica ($\\Delta H>0$), como $E_{a,\\text{dir}}=E_{a,\\text{inv}}+\\Delta H>\\Delta H$, ningún catalizador puede bajar $E_{a,\\text{dir}}$ por debajo del propio valor de $\\Delta H$ (el estado de transición siempre queda por encima del nivel de los productos)."
))

# H10: mcq[3].options[2].why_wrong - tildes
edits.append(("H10_mcq3_opt2",
"Eso dejaría $E_{a,\\text{dir}}=60-40=20$ kJ/mol, lo cual NO seria valido ($E_{a,\\text{inv}}=20-40=-20$, todavía negativo); el límite real es una reducción de 20 kJ/mol, no de 40.",
"Eso dejaría $E_{a,\\text{dir}}=60-40=20$ kJ/mol, lo cual no sería válido ($E_{a,\\text{inv}}=20-40=-20$, todavía negativo); el límite real es una reducción de 20 kJ/mol, no de 40."
))

# H11: misconceptions[0].related_exercises - tilde "leccion"
edits.append(("H11_misc0_relexc",
"el ejemplo 2 y el ejemplo 3 (apartado c) de esta leccion",
"el ejemplo 2 y el ejemplo 3 (apartado c) de esta lección"
))

# Referencias rotas (5)
edits.append(("REF_prereq0",
"Conocer la energía de activación Ea y el perfil energético de una reacción, incluida la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$ (lección el apartado correspondiente).",
"Conocer la energía de activación Ea y el perfil energético de una reacción, incluida la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$ (lección 2: Teoría de colisiones y energía de activación)."
))

edits.append(("REF_diag0_remediation",
"Repasar la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$ de la lección el apartado correspondiente con varios signos de ΔH antes de introducir el catalizador.",
"Repasar la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$ de la lección 2 (Teoría de colisiones y energía de activación) con varios signos de ΔH antes de introducir el catalizador."
))

edits.append(("REF_WE0_interpretation",
"Una reducción de Ea de 35 kJ/mol, aunque parezca modesta en términos absolutos, corresponde a casi la mitad de la energía de activación original, lo que se traduce (según la ecuación de Arrhenius, lección el apartado correspondiente) en un aumento muy grande de la velocidad.",
"Una reducción de Ea de 35 kJ/mol, aunque parezca modesta en términos absolutos, corresponde a casi la mitad de la energía de activación original, lo que se traduce (según la ecuación de Arrhenius, lección 8: Ecuación de Arrhenius) en un aumento muy grande de la velocidad."
))

edits.append(("REF_WE1_reasoning0",
"Se calcula primero $E_{a,\\text{inv}}^{\\text{sin}}$ con la relación ya conocida de el apartado correspondiente.",
"Se calcula primero $E_{a,\\text{inv}}^{\\text{sin}}$ con la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$, ya conocida de la lección 2 (Teoría de colisiones y energía de activación)."
))

edits.append(("REF_WE2_reasoning0",
"Se aplica la relación de el apartado correspondiente dos veces: con la Ea directa sin catalizar y con la catalizada, usando siempre el mismo ΔH.",
"Se aplica la relación $E_{a,\\text{inv}}=E_{a,\\text{dir}}-\\Delta H$ (lección 2: Teoría de colisiones y energía de activación) dos veces: con la Ea directa sin catalizar y con la catalizada, usando siempre el mismo ΔH."
))

# theory_blocks[4].title (plantilla) -> ya existe "Ideas equivocadas que conviene desmontar"
edits.append(("TEMPLATE_theory4_title",
"\"title\": \"Ideas equivocadas que conviene desmontar\",\n  \"body\": \"Dos errores frecuentes sobre los catalizadores:",
"\"title\": \"Errores habituales sobre catalizadores y equilibrio\",\n  \"body\": \"Dos errores frecuentes sobre los catalizadores:"
))

# exam_questions[1].mark_scheme (plantilla)
edits.append(("TEMPLATE_exam1_markscheme",
'"mark_scheme": [\n  "1 punto por cada apartado correctamente calificado y justificado",\n  "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"\n ],\n "common_errors": [\n  "Responder (a) como verdadera, pensando que el catalizador solo \'ayuda\' a formar el producto deseado.",',
'"mark_scheme": [\n  "1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con el efecto del catalizador sobre Ea, ΔH y la posición de equilibrio",\n  "Sin justificar con estos conceptos, no se otorga ningún punto aunque la calificación V/F sea correcta"\n ],\n "common_errors": [\n  "Responder (a) como verdadera, pensando que el catalizador solo \'ayuda\' a formar el producto deseado.",'
))

ok = apply(edits)
print("DONE", ok)
