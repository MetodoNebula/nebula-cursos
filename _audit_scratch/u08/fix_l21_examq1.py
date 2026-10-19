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

old_stmt = 'El tetrafluoroeteno, CF2=CF2, polimeriza por adición para dar PTFE (teflón). (a) Escribe la reacción de polimerización, indicando la unidad repetitiva. (b) Sin conocer la masa atómica del flúor, explica igualmente por qué la masa molar del PTFE debe ser un múltiplo exacto de la del tetrafluoroeteno, usando el mismo argumento que para el eteno.'
new_stmt = ('El tetrafluoroeteno, $' + BS + 'mathrm{CF_2{=}CF_2}$, polimeriza por adición para dar PTFE (teflón). (a) Escribe la reacción de polimerización, indicando la unidad repetitiva. '
            '(b) Sabiendo que $A_r(F)=19{,}00$, calcula la masa molar del monómero y explica, con el mismo argumento que para el eteno, por qué la masa molar de una cadena de PTFE es exactamente n veces la del monómero (despreciando los extremos).')
data = apply(data, old_stmt, new_stmt, 'exam_questions[1].statement')

old_ans = "(a) n CF2=CF2 → (-CF2-CF2-)n. (b) Porque es una polimerización por adición: el doble enlace se abre sin perder ningún átomo, con independencia de qué elementos contenga el monómero."
new_ans = ('(a) $n' + BS + ',' + BS + 'mathrm{CF_2{=}CF_2} ' + BS + 'longrightarrow ' + BS + 'mathrm{({-}CF_2{-}CF_2{-})}_n$. '
           '(b) $M(' + BS + 'mathrm{C_2F_4}) = 2' + BS + 'cdot12{,}011+4' + BS + 'cdot19{,}00=100{,}02' + BS + ',' + BS + 'mathrm{g/mol}$; para una cadena concreta, $M=n' + BS + 'cdot100{,}02' + BS + ',' + BS + 'mathrm{g/mol}$, porque la polimerización por adición no libera ningún subproducto, con independencia de qué elementos contenga el monómero.')
data = apply(data, old_ans, new_ans, 'exam_questions[1].answer')

old_fs = ('(a) El doble enlace entre los dos carbonos se abre exactamente igual que en el eteno, conservando los cuatro átomos de flúor. (b) El argumento de M_polímero=n·M_monómero no depende de qué elementos formen el monómero, sino solo de que la polimerización sea por adición: el criterio es que no se libera ningún subproducto en cada unión, y eso es cierto para el tetrafluoroeteno exactamente igual que para el eteno, tenga flúor o no.')
new_fs = ('(a) El doble enlace entre los dos carbonos se abre exactamente igual que en el eteno, conservando los cuatro átomos de flúor: $' + BS + 'mathrm{n' + BS[0] + ',CF_2{=}CF_2 ' + BS + 'longrightarrow ({-}CF_2{-}CF_2{-})_n}$; unidad repetitiva -CF2-CF2-. '
           '(b) $M(' + BS + 'mathrm{C_2F_4}) = 2' + BS + 'cdot12{,}011+4' + BS + 'cdot19{,}00=100{,}02' + BS + ',' + BS + 'mathrm{g/mol}$. El argumento de M=n' + chr(183) + 'M_monómero (para una cadena, despreciando los extremos) no depende de qué elementos formen el monómero, sino solo de que la polimerización sea por adición: no se libera ningún subproducto en cada unión, y eso es cierto para el tetrafluoroeteno exactamente igual que para el eteno, tenga flúor o no.')
data = apply(data, old_fs, new_fs, 'exam_questions[1].full_solution')

old_ms = ['2 puntos por la reacción ajustada con la unidad repetitiva correcta',
          '2 puntos por el razonamiento de (b), que debe apoyarse en el mecanismo de adición y no en un cálculo numérico concreto']
old_err = ['Intentar calcular un número en (b) a pesar de que el enunciado avisa de que no se dispone de la masa atómica del flúor.',
           'Olvidar alguno de los cuatro átomos de flúor al escribir la unidad repetitiva.']

old_ms1 = '"2 puntos por la reacción ajustada con la unidad repetitiva correcta",\n          "2 puntos por el razonamiento de (b), que debe apoyarse en el mecanismo de adición y no en un cálculo numérico concreto"'
new_ms1 = '"2 puntos por la reacción ajustada con la unidad repetitiva correcta",\n          "1 punto por el cálculo correcto de M(C2F4)=100,02 g/mol",\n          "1 punto por el razonamiento de que M=n' + chr(183) + 'M_monómero no depende de los elementos del monómero, solo de que no haya subproducto"'
data = apply(data, old_ms1, new_ms1, 'exam_questions[1].mark_scheme')

old_err1 = '"Intentar calcular un número en (b) a pesar de que el enunciado avisa de que no se dispone de la masa atómica del flúor.",\n          "Olvidar alguno de los cuatro átomos de flúor al escribir la unidad repetitiva."'
new_err1 = '"Olvidar alguno de los cuatro átomos de flúor al escribir la unidad repetitiva o al calcular la masa molar.",\n          "Confundir la masa molar de una cadena concreta (exacta) con la masa molar media de una muestra real (un promedio, que no da necesariamente un n entero)."'
data = apply(data, old_err1, new_err1, 'exam_questions[1].common_errors')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
