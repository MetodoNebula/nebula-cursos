import io, sys

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

key_start = '"15_Regla_de_Markovnikov.json"'
key_end = '"16_Eliminación_y_deshidratación.json"'
i0 = data.find(key_start)
i1 = data.find(key_end)
assert i0 != -1 and i1 != -1 and i0 < i1
seg = data[i0:i1]

NL = chr(10)

# ============ STEP B: content-level fixes (plain text, before LaTeX pass) ============
content_edits = []

# #10 course_label
content_edits.append((
'"course_label": "Química · 2º Bachillerato · Química del carbono e isomería",\n        "subject"' if False else None, None, "skip-placeholder"
))
content_edits.pop()

content_edits.append((
'"course_label": "Química · 2º Bachillerato · Química del carbono e isomería"',
'"course_label": "Química · 2º Bachillerato · Regla de Markovnikov"',
"L15-F10-courselabel"
))

# #11 IUPAC renaming
content_edits.append((
"2-metil-2-buteno, (CH3)2C=CH-CH3",
"2-metilbut-2-eno, (CH3)2C=CH-CH3",
"L15-F11-rename1"
))
content_edits.append((
"Repasar, antes de continuar, el recuento de H en los dos carbonos del doble enlace de 3 alquenos distintos (propeno, 2-metilpropeno, 1-buteno).",
"Repasar, antes de continuar, el recuento de H en los dos carbonos del doble enlace de 3 alquenos distintos (propeno, 2-metilpropeno, but-1-eno).",
"L15-F11-rename2"
))
content_edits.append((
"El 3-metil-1-buteno, CH2=CH-CH(CH3)-CH3, reacciona con HCl.",
"El 3-metilbut-1-eno, CH2=CH-CH(CH3)-CH3, reacciona con HCl.",
"L15-F11-rename3"
))

# #1 ALTA: exercises[0].common_errors[0] real error
content_edits.append((
"Adicionar el Br al carbono que no tiene H, pensando que ese es siempre el más sustituido y por tanto el que recibe el halógeno, sin comprobar antes dónde está realmente el carbocatión más estable.",
"Adicionar el Br al carbono que tiene 1 H (el C3), dando 2-bromo-3-metilbutano, CH3-CHBr-CH(CH3)-CH3, que pasaría por un carbocatión secundario, menos estable que el terciario de la respuesta correcta.",
"L15-F1"
))

# #2 MEDIA: theory_blocks[3].body expansion
content_edits.append((
"4. Ese es el producto **mayoritario**. El producto que resultaría de repartir los grupos al revés es el **minoritario**: también se forma, pero en menor proporción, porque pasa por un carbocatión intermedio menos estable.",
"4. Ese es el producto **mayoritario**. El producto que resultaría de repartir los grupos al revés es el **minoritario**: también se forma, pero en menor proporción, porque pasa por un carbocatión intermedio menos estable."
+ NL+NL +
"Un caso particular: si los dos carbonos del doble enlace tienen el mismo número de H (por ejemplo, en el pent-2-eno, CH3-CH=CH-CH2-CH3, los dos carbonos del doble enlace llevan 1 H cada uno), la regla no decide: los dos carbocationes secundarios intermedios son igual de estables, y se obtiene una mezcla aproximadamente equimolar de los dos productos posibles (2-bromopentano y 3-bromopentano, con HBr)."
+ NL+NL +
"La regla también se aplica a los alquinos: en la adición de HBr al propino, HC" + chr(8801) + "C-CH3, el H va al carbono terminal (que ya tiene 1 H) y el Br al carbono interno, dando 2-bromopropeno, CH2=CBr-CH3; con exceso de HBr, una segunda adición sobre ese mismo doble enlace da 2,2-dibromopropano, CH3-CBr2-CH3 (los dos Br acaban en el mismo carbono, el que ya tenía el primero)."
+ NL+NL +
"(Nota de ampliación: en presencia de peróxidos, el HBr " + chr(8212) + " solo el HBr, no el HCl ni el HI " + chr(8212) + " se adiciona en sentido contrario al que predice Markovnikov, por un mecanismo radicalario distinto; es la llamada adición anti-Markovnikov. No suele exigirse en PAU, pero conviene saber que existe esa excepción.)",
"L15-F2"
))

# #4 BAJA: +I wording fix
content_edits.append((
"un grupo alquilo, al ser menos electronegativo que el carbono positivo vecino, le cede densidad electrónica y reparte (atenúa) la deficiencia de carga.",
"los grupos alquilo son dadores de densidad electrónica (efecto inductivo +I) frente al hidrógeno: comparado con un átomo de H, un grupo alquilo cede más densidad electrónica hacia el carbono con la carga positiva, ayudando a repartir (atenuar) esa deficiencia de carga.",
"L15-F4-theory2"
))

# #4 continued: mcq[1] option D (distractor equivalent to correct answer -> replace with clearly false one)
content_edits.append((
'''            "key": "D",
            "text": "Porque tiene menos átomos de hidrógeno unidos directamente al carbono con la carga.",
            "why_wrong": "El número de H directamente unido al carbono positivo no es, por sí solo, la causa; lo relevante es cuántos grupos alquilo ceden densidad por efecto inductivo."''',
'''            "key": "D",
            "text": "Porque el carbocatión terciario tiene menos impedimento estérico que el primario.",
            "why_wrong": "El impedimento estérico no es el criterio relevante aquí: lo que estabiliza al carbocatión es el reparto de la carga positiva por efecto inductivo +I de los grupos alquilo, no un efecto de tamaño o forma."''',
"L15-F4-mcq1"
))

# #5 BAJA: guided_exercises[1].full_solution step order
content_edits.append((
"El carbono terminal (2 H) recibe el H del HI; el carbono interno (1 H) recibe el I, generando un carbocatión secundario (más estable que el primario de la otra opción).",
"El H$^+$ del HI se adiciona primero al carbono terminal (2 H), generando un carbocatión secundario en el carbono interno (más estable que el primario que daría la otra opción); después, el I$^-$ ataca ese carbocatión secundario.",
"L15-F5"
))

# #6 BAJA: exercises[0].full_solution add minority product
content_edits.append((
"El H del HBr se adiciona al carbono que ya tiene H (el derecho), generando el carbocatión terciario (CH3)2C$^+$-CH2-CH3, y el Br se fija ahí: (CH3)2CBr-CH2-CH3.",
"El H del HBr se adiciona al carbono que ya tiene H (el derecho), generando el carbocatión terciario (CH3)2C$^+$-CH2-CH3, y el Br se fija ahí: (CH3)2CBr-CH2-CH3. El camino alternativo (el H al carbono izquierdo, el que no tenía H) daría un carbocatión secundario, CH3-CH$^+$-CH(CH3)-CH3, y por tanto el producto minoritario 2-bromo-3-metilbutano, CH3-CHBr-CH(CH3)-CH3, menos favorecido por pasar por un intermedio menos estable que el terciario.",
"L15-F6"
))

# #7 BAJA: challenge_questions[0].full_solution add product names + PAU note
content_edits.append((
"Como el terciario es más estable que el secundario, este reordenamiento es favorable y compite con la adición directa.",
"Como el terciario es más estable que el secundario, este reordenamiento es favorable y compite con la adición directa. Los productos son: 2-cloro-3-metilbutano (de la adición directa, vía el carbocatión secundario inicial en el C2) y 2-cloro-2-metilbutano (tras la transposición de hidruro, vía el carbocatión terciario en el C3); experimentalmente, este último, el que pasa por el reordenamiento, suele ser el mayoritario. (Nota: las transposiciones de carbocationes son contenido de ampliación; no se exigen en la prueba de Selectividad.)",
"L15-F7"
))

# #8 BAJA LATEX: summary.formulas -- wrap chemical symbols in \mathrm
content_edits.append((
'"\\\\text{propeno} + HBr \\\\rightarrow CH_3-CHBr-CH_3\\\\ (\\\\text{mayoritario}) + CH_3-CH_2-CH_2Br\\\\ (\\\\text{minoritario})"',
'"\\\\text{propeno} + \\\\mathrm{HBr} \\\\rightarrow \\\\mathrm{CH_3{-}CHBr{-}CH_3}\\\\ (\\\\text{mayoritario}) + \\\\mathrm{CH_3{-}CH_2{-}CH_2Br}\\\\ (\\\\text{minoritario})"',
"L15-F8-formula0"
))
content_edits.append((
'"\\\\text{estabilidad: } (CH_3)_3C^{+} > (CH_3)_2CH^{+} > CH_3-CH_2^{+}"',
'"\\\\text{estabilidad: } (\\\\mathrm{CH_3})_3\\\\mathrm{C}^{+} > (\\\\mathrm{CH_3})_2\\\\mathrm{CH}^{+} > \\\\mathrm{CH_3{-}CH_2}^{+}"',
"L15-F8-formula1"
))

# Chequeos automáticos: TEXTO_PARA_PROFESOR -- misconceptions[0].diagnostic_signal in 2nd person
content_edits.append((
"Al predecir el producto, el alumno mira qué átomo está escrito primero en la fórmula en vez de contar los H de cada carbono del doble enlace.",
"Al predecir el producto, miras qué átomo está escrito primero en la fórmula en vez de contar los H de cada carbono del doble enlace.",
"L15-automatico-TEXTO_PARA_PROFESOR"
))

ok = True
for old, new, label in content_edits:
    c = seg.count(old)
    if c != 1:
        print(f"FAIL [{label}] count={c}")
        ok = False
    else:
        seg = seg.replace(old, new, 1)
        print(f"OK [{label}]")

if not ok:
    print("ABORTED at content edits")
    sys.exit(1)

# ============ STEP C: comprehensive LaTeX subscript conversion ============
formula_edits = [
 ("(CH3)2CBr-CH2-CH3", "(CH$_3$)$_2$CBr-CH$_2$-CH$_3$"),
 ("(CH3)2CCl-CH3", "(CH$_3$)$_2$CCl-CH$_3$"),
 ("(CH3)2C(OH)-CH3", "(CH$_3$)$_2$C(OH)-CH$_3$"),
 ("(CH3)2CH-CH2OH", "(CH$_3$)$_2$CH-CH$_2$OH"),
 ("(CH3)2C$^+$-CH2-CH3", "(CH$_3$)$_2$C$^+$-CH$_2$-CH$_3$"),
 ("(CH3)2C$^+$-CH3", "(CH$_3$)$_2$C$^+$-CH$_3$"),
 ("(CH3)2C=CH-CH3", "(CH$_3$)$_2$C=CH-CH$_3$"),
 ("(CH3)2C=CH2", "(CH$_3$)$_2$C=CH$_2$"),
 ("(CH3)2CH$^+$", "(CH$_3$)$_2$CH$^+$"),
 ("(CH3)3C$^+$", "(CH$_3$)$_3$C$^+$"),
 ("CH2=CH-CH(CH3)-CH3", "CH$_2$=CH-CH(CH$_3$)-CH$_3$"),
 ("CH2I-CH2-CH2-CH3", "CH$_2$I-CH$_2$-CH$_2$-CH$_3$"),
 ("CH3-CH2-CH2Br", "CH$_3$-CH$_2$-CH$_2$Br"),
 ("CH3-CH2-CH2OH", "CH$_3$-CH$_2$-CH$_2$OH"),
 ("CH3-CH2-CH=CH2", "CH$_3$-CH$_2$-CH=CH$_2$"),
 ("CH3-CH=CH-CH2-CH3", "CH$_3$-CH=CH-CH$_2$-CH$_3$"),
 ("CH3-CH=CH2", "CH$_3$-CH=CH$_2$"),
 ("CH3-CHBr-CH(CH3)-CH3", "CH$_3$-CHBr-CH(CH$_3$)-CH$_3$"),
 ("CH3-CHBr-CH3", "CH$_3$-CHBr-CH$_3$"),
 ("CH3-CHI-CH2-CH3", "CH$_3$-CHI-CH$_2$-CH$_3$"),
 ("CH3-CH(OH)-CH3", "CH$_3$-CH(OH)-CH$_3$"),
 ("CH3-CH$^+$-CH(CH3)-CH3", "CH$_3$-CH$^+$-CH(CH$_3$)-CH$_3$"),
 ("CH3-CH2-CH2$^+$", "CH$_3$-CH$_2$-CH$_2^+$"),
 ("CH3-CH2$^+$", "CH$_3$-CH$_2^+$"),
 ("CH3$^+$", "CH$_3^+$"),
 ("C3H7Br", "C$_3$H$_7$Br"),
 ("C3H6", "C$_3$H$_6$"),
 ("CBr2", "CBr$_2$"),
 ("=CH2", "=CH$_2$"),
 ("CH3", "CH$_3$"),
 ("CH2", "CH$_2$"),
 ("H2O", "H$_2$O"),
 ("H2", "H$_2$"),
 ("X2", "X$_2$"),
 ("Cl2", "Cl$_2$"),
 ("Br2", "Br$_2$"),
]
formula_edits.sort(key=lambda p: -len(p[0]))

for old, new in formula_edits:
    n = seg.count(old)
    seg = seg.replace(old, new)
    print(f"LATEX replace {old!r} -> {new!r} : {n} occurrences")

data2 = data[:i0] + seg + data[i1:]
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data2)
print("ALL EDITS APPLIED")
