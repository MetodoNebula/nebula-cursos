path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

# Finding 1: theory_blocks[2].body rewrite
old1 = 'El nivel de oxidación del carbono funcional sube de izquierda a derecha en la serie: alcohol → aldehído → ácido carboxílico (tres escalones, cuatro especies si se incluye el alcano). Un oxidante suave (como el reactivo de Jones, CrO₃/H₂SO₄) lleva el alcohol al aldehído o a la cetona; un oxidante fuerte (KMnO₄ en frío ácido o el propio Jones en exceso) recorre los dos últimos escalones (aldehído → ácido). En sentido contrario, un reductor fuerte (LiAlH₄) baja el ácido hasta el alcohol.'
new1 = ('El nivel de oxidación del carbono funcional sube de izquierda a derecha en la serie: alcano → alcohol → aldehído (o cetona) → ácido carboxílico (tres escalones). Un oxidante suave (PCC) lleva el alcohol primario solo hasta aldehído, sin pasar de ahí; un oxidante fuerte (KMnO₄ o K₂Cr₂O₇ en medio ácido, o el propio reactivo de Jones, CrO₃/H₂SO₄) lo lleva hasta ácido carboxílico. Un alcohol secundario da cetona con cualquiera de ellos, suave o fuerte, y ahí se detiene siempre. En sentido contrario, un reductor fuerte (LiAlH₄) baja el ácido hasta el alcohol.')
data = apply(data, old1, new1, 'theory_blocks[2] rewrite')

# Finding 2: theory_blocks[3].body - add terciario + destilación
old2 = 'Sobre un alcohol secundario, cualquiera de estos oxidantes (suave o fuerte) da el mismo resultado: cetona, y ahí se detiene siempre, porque no es un límite del oxidante sino del propio carbono (sin hidrógeno que perder).'
new2 = ('Sobre un alcohol secundario, cualquiera de estos oxidantes (suave o fuerte) da el mismo resultado: cetona, y ahí se detiene siempre, porque no es un límite del oxidante sino del propio carbono (sin hidrógeno que perder). Un alcohol terciario, en cambio, no se oxida por esta vía: su carbono funcional no tiene ningún H que perder, así que no hay ningún enlace C-H que romper para ganar el enlace C-O adicional.\n\nUn truco clásico de examen con K₂Cr₂O₇/H⁺: si se quiere aislar el aldehído a partir de un alcohol primario con un oxidante fuerte (que en condiciones normales seguiría hasta ácido), se destila el aldehído a medida que se va formando, retirándolo de la mezcla antes de que termine de oxidarse.')
data = apply(data, old2, new2, 'theory_blocks[3] add terciario+destilacion')

# Finding 8: theory_blocks[3].body - add H2/Ni + Fehling/Tollens block (appended after prior edit)
old8 = 'Esto significa que, para un alcohol primario, el reactivo elegido decide el producto (aldehído o ácido), mientras que para uno secundario el producto es siempre el mismo (cetona) sea cual sea la fuerza del oxidante.'
new8 = ('Esto significa que, para un alcohol primario, el reactivo elegido decide el producto (aldehído o ácido), mientras que para uno secundario el producto es siempre el mismo (cetona) sea cual sea la fuerza del oxidante.\n\nOtras reacciones redox orgánicas habituales en PAU: la hidrogenación con H₂/Ni (o Pt) reduce tanto el doble enlace C=C de un alqueno como el C=O de un aldehído o una cetona, añadiendo H a cada lado del enlace múltiple. Y los reactivos de Fehling y de Tollens distinguen aldehídos de cetonas: un aldehído los reduce (precipitado rojo de Cu₂O con Fehling, espejo de plata con Tollens) porque conserva un H sobre el carbono carbonílico que le permite oxidarse a ácido; una cetona no reacciona, porque no tiene ese H.')
data = apply(data, old8, new8, 'theory_blocks[3] add H2/Ni+Fehling/Tollens')

# Finding 3: common_mistakes[0..2].why
old3a = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Mirar solo el carbono que cambia de grupo funcional y contar sus enlaces C-O y C-H."'
new3a = '"why": "Se traslada mecánicamente el procedimiento de redox inorgánico (número de oxidación de toda la molécula) sin usar el atajo propio de la orgánica, que solo mira el carbono que cambia de grupo funcional.",\n        "how_to_avoid": "Mirar solo el carbono que cambia de grupo funcional y contar sus enlaces C-O y C-H."'
data = apply(data, old3a, new3a, 'common_mistakes[0].why')

old3b = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Contar primero los hidrógenos del carbono funcional'
new3b = '"why": "Se generaliza el comportamiento del alcohol primario (que sí llega a ácido) a todos los alcoholes, sin comprobar cuántos H tiene el carbono funcional.",\n        "how_to_avoid": "Contar primero los hidrógenos del carbono funcional'
data = apply(data, old3b, new3b, 'common_mistakes[1].why')

old3c = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Memorizar la pareja fija: NaBH4 solo aldehídos/cetonas'
new3c = '"why": "Se trata ' + chr(171) + 'reductor' + chr(187) + ' como una etiqueta única, sin distinguir que NaBH4 y LiAlH4 tienen alcances distintos.",\n        "how_to_avoid": "Memorizar la pareja fija: NaBH4 solo aldehídos/cetonas'
data = apply(data, old3c, new3c, 'common_mistakes[2].why')

# Finding 5: exam_notes[3] matizar
old5 = 'No se exige calcular números de oxidación formales en orgánica: el criterio de enlaces C-O/C-H es el que se espera en la respuesta.'
new5 = ('No se exige calcular números de oxidación formales en orgánica para decidir si hay oxidación: basta el criterio de enlaces C-O/C-H. Pero si el enunciado da el oxidante concreto (por ejemplo dicromato o permanganato en medio ácido), puede pedirse ajustar la reacción por ion-electrón: $' + BS + 'mathrm{3' + BS + ',CH_3CH_2OH + 2' + BS + ',Cr_2O_7^{2-} + 16' + BS + ',H^+ ' + BS + 'rightarrow 3' + BS + ',CH_3COOH + 4' + BS + ',Cr^{3+} + 11' + BS + ',H_2O}$.')
data = apply(data, old5, new5, 'exam_notes[3] matizar')

# Finding 6: theory_blocks[1].body fix gaining/losing bonds wording
old6 = 'Oxidación: el carbono gana enlaces C-O (o, equivalentemente, pierde enlaces C-H).\n- Reducción: el carbono pierde enlaces C-O (gana enlaces C-H).'
new6 = 'Oxidación: aumenta el número de enlaces del carbono funcional a oxígeno (o a otro heteroátomo más electronegativo) y/o disminuye el de enlaces C-H.\n- Reducción: lo contrario: disminuye el número de enlaces a oxígeno y/o aumenta el de enlaces C-H (por ejemplo, la hidrogenación de un alqueno, que gana enlaces C-H sin perder ningún C-O, es una reducción).'
data = apply(data, old6, new6, 'theory_blocks[1] oxidation/reduction wording')

# Finding 7: worked_examples[2].reasoning[2], flashcards[10].back, common_mistakes[3].why
old7a = 'Al reducir el éster se rompe el enlace entre el oxígeno y los dos fragmentos: la parte que venía del ácido se convierte en un alcohol primario, y la parte que venía del alcohol original del éster se libera como su propio alcohol (metanol).'
new7a = 'Al reducir el éster se rompe el enlace entre el carbono del carbonilo y el oxígeno del grupo -OCH3: ese oxígeno se queda con el grupo metilo y se libera como metanol, mientras que el carbono del carbonilo, ya sin ese oxígeno saliente, se reduce hasta -CH2OH (alcohol primario).'
data = apply(data, old7a, new7a, 'worked_examples[2].reasoning[2]')

old7b = '"back": "Dos alcoholes distintos: R-CH2OH (de la parte ácida) y R’-OH (de la parte alcohólica del éster), porque el enlace C-O-C se rompe en dos fragmentos."'
new7b = '"back": "Dos alcoholes distintos: R-CH2OH (de la parte ácida) y R’-OH (de la parte alcohólica del éster), porque se rompe el enlace entre el carbono del carbonilo y el oxígeno alcoxílico, no el C-O-C entero a la vez."'
data = apply(data, old7b, new7b, 'flashcards[10].back')

old7c = 'Se piensa en la reducción como un simple ‘añadir hidrógenos’ sin fijarse en que el enlace C-O-C del éster se rompe en dos fragmentos.'
new7c = 'Se piensa en la reducción como un simple ‘añadir hidrógenos’ sin fijarse en que es el enlace C(carbonilo)-O(alcoxi) concreto el que se rompe, separando el éster en sus dos mitades.'
data = apply(data, old7c, new7c, 'common_mistakes[3].why')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
