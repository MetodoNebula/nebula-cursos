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

# Finding 8/9: common_mistakes[0].why and [2].why
old8 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Antes de calcular, preguntarse explícitamente'
new8 = '"why": "Se aplica por inercia el patrón de la condensación (pérdida de una molécula pequeña en cada unión) a un monómero con C=C, que se une sin ningún subproducto.",\n        "how_to_avoid": "Antes de calcular, preguntarse explícitamente'
data = apply(data, old8, new8, 'common_mistakes[0].why')

old9 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Dibujar explícitamente 3 o 4 unidades consecutivas'
new9 = '"why": "La notación (' + chr(8211) + ')n recuerda visualmente a ' + chr(171) + 'n copias' + chr(187) + ' de algo suelto, y no muestra los enlaces C-C que unen cada unidad con la siguiente.",\n        "how_to_avoid": "Dibujar explícitamente 3 o 4 unidades consecutivas'
data = apply(data, old9, new9, 'common_mistakes[2].why')

# Finding 11: exam_questions[0].full_solution (b)
old11 = 'Falsa: por definición de polimerización por adición, M_polímero=n·M_monómero para cualquier valor de n, por grande que sea.'
new11 = 'Falsa: para cada cadena concreta (despreciando los dos extremos, restos del iniciador), M_polímero=n·M_monómero es exacto para cualquier n, por grande que sea; no se pierde ningún átomo al alargar la cadena. Si una masa molar media no da un cociente exactamente entero no es porque se pierdan átomos, sino porque n̄ es un promedio sobre cadenas de longitudes distintas.'
data = apply(data, old11, new11, 'exam_questions[0].full_solution (b)')

# Finding 12: prerequisites[0].statement naming
old12 = 'Reconocer un doble enlace C=C en una fórmula semidesarrollada y nombrar alquenos sencillos (eteno, propeno, cloruro de vinilo, estireno).'
new12 = 'Reconocer un doble enlace C=C en una fórmula semidesarrollada y nombrar alquenos sencillos: eteno, propeno, cloroeteno (cloruro de vinilo), etenilbenceno o fenileteno (estireno).'
data = apply(data, old12, new12, 'prerequisites[0].statement')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
