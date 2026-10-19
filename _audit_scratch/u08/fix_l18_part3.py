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

# Finding 5: common_mistakes[0..2].why - lesson-specific content
old0 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n    "how_to_avoid": "Subrayar siempre, en el sustrato (lado izquierdo), el enlace que se va a romper'
new0 = '"why": "Se mira la carga de las especies en los productos en vez de rastrear qué estaba unido al carbono antes de reaccionar.",\n    "how_to_avoid": "Subrayar siempre, en el sustrato (lado izquierdo), el enlace que se va a romper'
data = apply(data, old0, new0, 'common_mistakes[0].why')

old1 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n    "how_to_avoid": "Antes de clasificar la reacción, comprobar si el sustrato tiene un doble o triple enlace'
new1 = '"why": "Se memoriza la regla ' + chr(171) + 'halógeno + compuesto orgánico = adición' + chr(187) + ' sin comprobar si existe un enlace múltiple sobre el que adicionarse.",\n    "how_to_avoid": "Antes de clasificar la reacción, comprobar si el sustrato tiene un doble o triple enlace'
data = apply(data, old1, new1, 'common_mistakes[1].why')

old2 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n    "how_to_avoid": "Preguntarse, tras formar un producto con un par de electrones libre nuevo'
new2 = '"why": "Se trata la síntesis como si se detuviera sola en el primer producto, sin pensar que ese producto también es nucleófilo.",\n    "how_to_avoid": "Preguntarse, tras formar un producto con un par de electrones libre nuevo'
data = apply(data, old2, new2, 'common_mistakes[2].why')

# Finding 8: theory_blocks[1].body - SN1/SN2 order + R wording
old8 = 'A nivel de mecanismo existen dos variantes, SN1 y SN2, según si la sustitución ocurre en una o dos etapas; en PAU/EBAU basta con reconocer el resultado neto de la reacción, no hace falta describir el mecanismo paso a paso.'
new8 = 'A nivel de mecanismo existen dos variantes: SN2, en una sola etapa concertada (el atacante entra a la vez que el saliente se va), y SN1, en dos etapas, con un carbocatión intermedio (el saliente se va primero, y solo después entra el atacante); los números 1 y 2 indican la molecularidad de la etapa determinante, no el orden de las etapas. En PAU/EBAU basta con reconocer el resultado neto de la reacción, no hace falta describir el mecanismo paso a paso.'
data = apply(data, old8, new8, 'theory_blocks[1] SN1/SN2')

old8b = 'donde: $R$ es el sustrato (la cadena carbonada que no cambia); $A$ es el grupo saliente'
new8b = 'donde: $R$ es el grupo alquilo, la parte del sustrato R-A que no cambia (el sustrato completo es R-A); $A$ es el grupo saliente'
data = apply(data, old8b, new8b, 'theory_blocks[1] R wording')

# Finding 9: guided_exercises[1] naming fix (answer + full_solution)
old9a = '(b) Un éter (metil etil éter); es la síntesis de Williamson.'
new9a = '(b) Un éter, metoxietano (etil metil éter); es la síntesis de Williamson.'
data = apply(data, old9a, new9a, 'guided_exercises[1].answer naming')

old9b = 'es un éter, concretamente el metil etil éter.'
new9b = 'es un éter: metoxietano (nombre de clase funcional, etil metil éter).'
data = apply(data, old9b, new9b, 'guided_exercises[1].full_solution naming')

# Finding 10: mcq[3] stem clarify "principal"
old10 = '"stem": "¿Por qué se usa amoniaco en gran exceso al sintetizar una amina primaria a partir de un haloalcano?",'
new10 = '"stem": "¿Cuál es la razón PRINCIPAL para usar amoniaco en gran exceso al sintetizar una amina primaria a partir de un haloalcano?",'
data = apply(data, old10, new10, 'mcq[3] stem')

# Finding 12: worked_examples[3].reasoning[1] cyanide carbon
old12 = 'pero es el carbono del nitrilo el que forma el enlace nuevo con el sustrato aportando su par disponible.'
new12 = 'pero es el carbono del ion cianuro (' + chr(58) + 'C' + chr(8801) + 'N' + chr(8315) + ') el que forma el enlace nuevo con el sustrato aportando su par disponible.'
data = apply(data, old12, new12, 'worked_examples[3] cyanide carbon')

# Finding 13: theory_blocks[3].body elimination phrasing
old13 = 'compite con el sustrato la posibilidad de eliminación (formar un alqueno) en vez de sustitución, sobre todo si el haloalcano es terciario.'
new13 = 'la base puede provocar eliminación (formar un alqueno) en lugar de sustitución, sobre todo si el haloalcano es terciario y se trabaja en etanol y en caliente.'
data = apply(data, old13, new13, 'theory_blocks[3] elimination')

# Finding 14: theory_blocks[4].body add aromatic examples
old14 = 'No hace falta memorizar esta familia para PAU/EBAU con el mismo detalle que la sustitución sobre haloalcanos; basta con saber que existe y que responde a la misma idea general de sustitución.'
new14 = ('No hace falta memorizar esta familia para PAU/EBAU con el mismo detalle que la sustitución sobre haloalcanos; basta con saber que existe y que responde a la misma idea general de sustitución. '
         'Dos ejemplos para fijar la idea: $' + BS + 'mathrm{C_6H_6 + HNO_3 ' + BS + 'xrightarrow{H_2SO_4} C_6H_5NO_2 + H_2O}$ (nitración) y $' + BS + 'mathrm{C_6H_6 + Br_2 ' + BS + 'xrightarrow{FeBr_3} C_6H_5Br + HBr}$ (bromación).')
data = apply(data, old14, new14, 'theory_blocks[4] aromatic examples')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
