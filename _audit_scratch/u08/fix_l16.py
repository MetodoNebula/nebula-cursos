import io, sys

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

key_start = '"16_Eliminación_y_deshidratación.json"'
key_end = '"17_Regla_de_SaytzeffZaitsev.json"'
i0 = data.find(key_start)
i1 = data.find(key_end)
assert i0 != -1 and i1 != -1 and i0 < i1
seg = data[i0:i1]

NL = chr(10)

# ============ STEP B: content-level fixes (plain text, before LaTeX pass) ============
content_edits = []

# #1 + #7: guided_exercises[0].hints[0] and answer
content_edits.append((
"El Cl está en el C2; su único vecino es el C1.",
"El Cl está en el C1 (CH2Cl); su único vecino es el C2 (CH3).",
"L16-F1-hint"
))
content_edits.append((
'"answer": "(a) El Cl está en el C1; su vecino es el C2 (CH3)",',
'"answer": "(a) El Cl está en el C1 (CH2Cl); su vecino es el C2 (CH3). (b) CH3-CH2Cl + KOH \\u2192(etanol, \\u0394)\\u2192 CH2=CH2 + KCl + H2O; producto: eteno.",',
"L16-F7-answer"
))

# #2: guided_exercises[0].full_solution
content_edits.append((
"En CH3-CH2Cl, el C2 lleva el Cl; su único carbono vecino es el C1, el grupo CH3. El H que se elimina sale del C1, y el Cl sale del C2; se forma el doble enlace entre ambos: CH3-CH2Cl + KOH → CH2=CH2 + KCl + H2O. Ajuste: 2 C, 6 H, 1 Cl, 1 K, 1 O a cada lado.",
"(a) En CH3-CH2Cl, el C1 (CH2Cl) lleva el Cl; su único carbono vecino es el C2, el grupo CH3. (b) El H que se elimina sale del C2, y el Cl sale del C1; se forma el doble enlace entre ambos: CH3-CH2Cl + KOH → CH2=CH2 + KCl + H2O. Ajuste: 2 C, 6 H, 1 Cl, 1 K, 1 O a cada lado. Producto: eteno.",
"L16-F2-fullsol"
))

# #5: worked_examples[0].common_mistake C2->C1 fix
content_edits.append((
"Escribir el doble enlace solo «donde estaba el Br» (en el C2) sin extenderlo hasta el C1, olvidando que el doble enlace une a los dos carbonos implicados, no a uno solo.",
"Escribir el doble enlace solo «donde estaba el Br» (en el C1) sin extenderlo hasta el C2, olvidando que el doble enlace une a los dos carbonos implicados, no a uno solo.",
"L16-F5"
))

# #6: exercises[1].statement reformulated
content_edits.append((
"Clasifica esta reacción y escribe su ecuación ajustada: deshidratación del metanol, CH3OH, con H2SO4 y calor.",
"¿Puede el metanol, CH3OH, dar un alqueno por deshidratación con H2SO4 y calor? Justifícalo. ¿Qué producto se obtiene en realidad?",
"L16-F6"
))
content_edits.append((
"El metanol no puede deshidratarse de esta forma: no tiene ningún carbono vecino al OH del que eliminar un H.",
"No puede dar un alqueno: no tiene ningún carbono vecino al OH del que eliminar un H. Lo que se obtiene en realidad es dimetil éter, CH3-O-CH3, por deshidratación intermolecular entre dos moléculas de metanol.",
"L16-F6-answer"
))

# #3: exercises[1].full_solution add intermolecular dehydration
content_edits.append((
"Por eso esta reacción de deshidratación, tal como se ha definido, no es aplicable al metanol: hace falta al menos dos carbonos en la cadena.",
"Por eso esta reacción de deshidratación intramolecular (a alqueno), tal como se ha definido, no es aplicable al metanol: hace falta al menos dos carbonos en la cadena. Lo que sí ocurre con el metanol y H2SO4 en caliente es una deshidratación intermolecular, entre dos moléculas de alcohol: 2 CH3OH → CH3-O-CH3 + H2O (dimetil éter o metoximetano).",
"L16-F3"
))

# #4: flashcards[6].back
content_edits.append((
"Tener al menos un carbono vecino (adyacente) con un hidrógeno disponible; sin él, no hay eliminación posible (p. ej. el metanol no puede deshidratarse).",
"Tener al menos un carbono vecino (adyacente) con un hidrógeno disponible; sin él no puede formarse un alqueno (p. ej. el metanol no da ningún alqueno; con H2SO4 solo forma dimetil éter por deshidratación intermolecular).",
"L16-F4"
))

# #8: theory_blocks[2].body -- temperature dependence
content_edits.append((
"Se comprueba el ajuste: 2 C, 6 H y 1 O a cada lado (el H2SO4 es catalizador, no reactivo, igual que el catalizador metálico de la hidrogenación en la adición).",
"Se comprueba el ajuste: 2 C, 6 H y 1 O a cada lado (el H2SO4 es catalizador, no reactivo, igual que el catalizador metálico de la hidrogenación en la adición)."
+ NL+NL +
"Con el etanol y H2SO4 concentrado, la temperatura decide el producto: a unos 170 °C se favorece la eliminación (el alqueno, eteno); a una temperatura más baja, hacia 140 °C, y con exceso de alcohol, predomina en cambio una deshidratación intermolecular entre dos moléculas de alcohol: 2 CH3-CH2OH → CH3-CH2-O-CH2-CH3 + H2O (dietil éter o etoxietano).",
"L16-F8"
))

# #9: theory_blocks[1].body -- KOH(aq) vs KOH(alc)
content_edits.append((
"Se comprueba el ajuste contando átomos: 2 C, 6 H, 1 Br, 1 K y 1 O a cada lado.",
"Se comprueba el ajuste contando átomos: 2 C, 6 H, 1 Br, 1 K y 1 O a cada lado."
+ NL+NL +
"Esto depende del medio: en disolución acuosa, el KOH actúa principalmente como nucleófilo y da sustitución (CH3-CH2Br + KOH → CH3-CH2OH + KBr, un alcohol); es precisamente el medio alcohólico y el calor lo que favorece que actúe como base y dé la eliminación. Las condiciones de reacción son las que deciden cuál de los dos productos predomina.",
"L16-F9"
))

# #11: mcq[2].explanation
content_edits.append((
"El H2SO4 concentrado y el calor favorecen la deshidratación, pero actúan de forma catalítica: no aparecen en el balance de átomos de los productos orgánicos.",
"El H2SO4 concentrado actúa como catalizador (y como agente deshidratante): no aparece en el balance de átomos de los productos orgánicos. El calor no es un catalizador, sino que aporta la energía de activación necesaria para que la reacción ocurra a una velocidad apreciable.",
"L16-F11"
))

# #13: summary.key_points[0]
content_edits.append((
">C(H)-C(X)< + KOH →(alc.)→ >C=C< + KX + H2O; el KOH se consume.",
">C(H)-C(X)< + KOH " + chr(36) + chr(92)*2 + "xrightarrow{" + chr(92)*2 + "text{alc.}}" + chr(36) + " >C=C< + KX + H2O; el KOH se consume.",
"L16-F13"
))

# #14: exercises[0] replaced entirely with in-syllabus example (2-chloropropane + KOH alcoholico)
old_ex0 = (
    '"statement": "Escribe la ecuación ajustada de la eliminación de halogenuros vecinales del 1,2-dibromoetano con Zn (medio alcohólico), que da directamente el alqueno sin pasar por una base. (**Ampliación**: esta reacción de deshalogenación vecinal con Zn no se trata en los bloques teóricos de la lección; es complementaria a la deshidrohalogenación.)",\n'
    '        "hints": [\n'
    '          "Aquí se eliminan los dos Br, uno de cada carbono, no un H y un X."\n'
    '        ],\n'
    '        "answer": "CH2Br-CH2Br + Zn \u2192(EtOH)\u2192 CH2=CH2 + ZnBr2.",\n'
    '        "full_solution": "A diferencia de la deshidrohalogenación (que elimina H y X de carbonos vecinos), aquí se eliminan dos átomos de Br, uno de cada carbono, con el Zn actuando como aceptor de ambos halógenos. Ajuste: 2 C, 4 H, 2 Br y 1 Zn a cada lado.",\n'
    '        "common_errors": [\n'
    '          "Confundir este caso con la deshidrohalogenación habitual e incluir una base (KOH) en vez del Zn."\n'
    '        ],'
)
new_ex0 = (
    '"statement": "El 2-cloropropano, CH3-CHCl-CH3, reacciona con KOH en medio alcohólico. (a) Identifica el carbono con el Cl y sus carbonos vecinos con H disponible. (b) Escribe la ecuación ajustada del producto que se forma.",\n'
    '        "hints": [\n'
    '          "El Cl está en el C2 (el carbono central); tiene DOS carbonos vecinos con H disponible, el C1 y el C3."\n'
    '        ],\n'
    '        "answer": "CH3-CHCl-CH3 + KOH \u2192(alc., \u0394)\u2192 CH3-CH=CH2 + KCl + H2O (propeno).",\n'
    '        "full_solution": "(a) El Cl está en el carbono central (C2); sus dos vecinos, C1 y C3, son ambos grupos CH3 con H disponibles. (b) Al retirar el Cl del C2 y un H de cualquiera de sus dos vecinos (aquí equivalentes entre sí, por ser ambos un CH3), se forma un único alqueno posible: CH3-CHCl-CH3 + KOH \u2192 CH3-CH=CH2 + KCl + H2O. Ajuste: 3 C, 7 H, 1 Cl, 1 K, 1 O a cada lado.",\n'
    '        "common_errors": [\n'
    '          "Pensar que, al haber dos carbonos vecinos con H, deben obtenerse dos alquenos distintos: aquí ambos vecinos son grupos CH3 equivalentes entre sí, así que solo hay un producto posible, el propeno."\n'
    '        ],'
)
content_edits.append((old_ex0, new_ex0, "L16-F14"))

# #15: challenge_questions[0] -- add PAU-level note
content_edits.append((
"Sumando las dos etapas: CH2Br-CH2Br + 2 NaNH2 → CH≡CH + 2 NH3 + 2 NaBr. Comprobación por elemento: izquierda 2 C, 4 H (del dibromoetano) + 4 H (de 2 NaNH2) = 8 H, 2 Br, 2 Na, 2 N; derecha 2 C, 2 H (etino) + 6 H (2 NH3) = 8 H, 2 Br (2 NaBr), 2 Na, 2 N. Ajustada.",
"Sumando las dos etapas: CH2Br-CH2Br + 2 NaNH2 → CH≡CH + 2 NH3 + 2 NaBr. Comprobación por elemento: izquierda 2 C, 4 H (del dibromoetano) + 4 H (de 2 NaNH2) = 8 H, 2 Br, 2 Na, 2 N; derecha 2 C, 2 H (etino) + 6 H (2 NH3) = 8 H, 2 Br (2 NaBr), 2 Na, 2 N. Ajustada. (Nota de nivel: el NaNH2 excede el temario de Selectividad; a nivel de Bachillerato se suele plantear la misma doble eliminación con KOH en etanol y exceso, en caliente: CH2Br-CH2Br + 2 KOH →(etanol, \\u0394)→ CH≡CH + 2 KBr + 2 H2O, con el mismo razonamiento por etapas.)",
"L16-F15"
))
content_edits.append((
'"back": "Sí: dos eliminaciones sucesivas de HX con una base fuerte (NaNH2) sobre un dihaloalcano, retirando H y X en dos pasos, dan un triple enlace.",',
'"back": "Sí: dos eliminaciones sucesivas de HX sobre un dihaloalcano, retirando H y X en dos pasos, dan un triple enlace; el reto de esta lección usa NaNH2, aunque a nivel de Bachillerato se suele plantear con KOH en etanol y exceso, en caliente.",',
"L16-F15-flashcard"
))

# #16: theory_blocks[3].body dash/comma fix + concrete example
content_edits.append((
"—por ejemplo, un haloalcano o un alcohol con una cadena más larga a ambos lados del grupo saliente, la eliminación puede retirar el H de cualquiera de esos carbonos vecinos y dar más de un alqueno distinto.",
"—por ejemplo, un haloalcano o un alcohol con cadena a ambos lados del grupo saliente—, la eliminación puede retirar el H de cualquiera de esos carbonos vecinos y dar más de un alqueno distinto (así ocurre, por ejemplo, con el 2-bromobutano, que puede dar but-1-eno o but-2-eno, según de cuál de sus dos carbonos vecinos salga el H).",
"L16-F16"
))

# ============ theory_blocks equations: add \\mathrm (#12) ============
BS = chr(92) * 2  # two literal backslash characters, matching on-disk convention

old_eq1 = f"$>{BS}!C(H)-C(X){BS}!< + KOH {BS}xrightarrow{{{BS}text{{medio alcoh\u00f3lico}}}} >{BS}!C=C{BS}!< + KX + H_2O$"
new_eq1 = f"${BS}mathrm{{>{BS}!C(H)-C(X){BS}!< + KOH}} {BS}xrightarrow{{{BS}text{{medio alcoh\u00f3lico}}}} {BS}mathrm{{>{BS}!C=C{BS}!< + KX + H_2O}}$"
content_edits.append((old_eq1, new_eq1, "L16-F12-theory1-general"))

old_eq2 = f"$CH_3-CH_2Br + KOH {BS}xrightarrow{{{BS}text{{medio alcoh\u00f3lico}}}} CH_2=CH_2 + KBr + H_2O$"
new_eq2 = f"${BS}mathrm{{CH_3{{-}}CH_2Br + KOH}} {BS}xrightarrow{{{BS}text{{medio alcoh\u00f3lico}}}} {BS}mathrm{{CH_2{{=}}CH_2 + KBr + H_2O}}$"
content_edits.append((old_eq2, new_eq2, "L16-F12-theory1-example"))

old_eq3 = f"$>{BS}!C(H)-C(OH){BS}!< {BS}xrightarrow[{BS}Delta]{{H_2SO_4}} >{BS}!C=C{BS}!< + H_2O$"
new_eq3 = f"${BS}mathrm{{>{BS}!C(H)-C(OH){BS}!<}} {BS}xrightarrow[{BS}Delta]{{{BS}mathrm{{H_2SO_4}}}} {BS}mathrm{{>{BS}!C=C{BS}!< + H_2O}}$"
content_edits.append((old_eq3, new_eq3, "L16-F12-theory2-general"))

old_eq4 = f"$CH_3-CH_2OH {BS}xrightarrow[{BS}Delta]{{H_2SO_4}} CH_2=CH_2 + H_2O$"
new_eq4 = f"${BS}mathrm{{CH_3{{-}}CH_2OH}} {BS}xrightarrow[{BS}Delta]{{{BS}mathrm{{H_2SO_4}}}} {BS}mathrm{{CH_2{{=}}CH_2 + H_2O}}$"
content_edits.append((old_eq4, new_eq4, "L16-F12-theory2-example"))

# course_label coherence (not separately flagged but same issue as L15 -- check first)
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

# ============ STEP C: arrow-condition patterns -> proper LaTeX ============
arrow_edits = [
 (chr(8594)+"(H2SO4, "+chr(916)+")"+chr(8594), chr(36)+chr(92)*2+"xrightarrow["+chr(92)*2+"Delta]{"+chr(92)*2+"text{H}_2"+chr(92)*2+"text{SO}_4}"+chr(36)),
 (chr(8594)+"(medio alcoh\u00f3lico)"+chr(8594), chr(36)+chr(92)*2+"xrightarrow{"+chr(92)*2+"text{medio alcoh\u00f3lico}}"+chr(36)),
]
for old, new in arrow_edits:
    n = seg.count(old)
    seg = seg.replace(old, new)
    print(f"ARROW replace {old!r} -> {new!r} : {n} occurrences")

# ============ STEP D: comprehensive LaTeX subscript conversion (bare $_N$ style) ============
formula_edits = [
 ("CH2Br-CH2Br", "CH$_2$Br-CH$_2$Br"),
 ("CH2=CHBr", "CH$_2$=CHBr"),
 ("CH3-CH2-CH2OH", "CH$_3$-CH$_2$-CH$_2$OH"),
 ("CH3-CH2OH", "CH$_3$-CH$_2$OH"),
 ("CH3-CH2Br", "CH$_3$-CH$_2$Br"),
 ("CH3-CH2Cl", "CH$_3$-CH$_2$Cl"),
 ("CH3-CH2I", "CH$_3$-CH$_2$I"),
 ("CH3-CH=CH2", "CH$_3$-CH=CH$_2$"),
 ("CH3-CHCl-CH3", "CH$_3$-CHCl-CH$_3$"),
 ("CH3-O-CH3", "CH$_3$-O-CH$_3$"),
 ("CH3-CH2-O-CH2-CH3", "CH$_3$-CH$_2$-O-CH$_2$-CH$_3$"),
 ("CH2=CH2", "CH$_2$=CH$_2$"),
 ("C3H8O", "C$_3$H$_8$O"),
 ("CH3OH", "CH$_3$OH"),
 ("H2SO4", "H$_2$SO$_4$"),
 ("NaNH2", "NaNH$_2$"),
 ("NH3", "NH$_3$"),
 ("H2O", "H$_2$O"),
 ("CH3", "CH$_3$"),
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
