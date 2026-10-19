path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

old0 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Subrayar siempre, en el sustrato (lado izquierdo), el enlace que se va a romper'
new0 = '"why": "Se mira la carga de las especies en los productos en vez de rastrear qué estaba unido al carbono antes de reaccionar.",\n        "how_to_avoid": "Subrayar siempre, en el sustrato (lado izquierdo), el enlace que se va a romper'
data = apply(data, old0, new0, 'common_mistakes[0].why')

old1 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Antes de clasificar la reacción, comprobar si el sustrato tiene un doble o triple enlace'
new1 = '"why": "Se memoriza la regla ' + chr(171) + 'halógeno + compuesto orgánico = adición' + chr(187) + ' sin comprobar si existe un enlace múltiple sobre el que adicionarse.",\n        "how_to_avoid": "Antes de clasificar la reacción, comprobar si el sustrato tiene un doble o triple enlace'
data = apply(data, old1, new1, 'common_mistakes[1].why')

old2 = '"why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Preguntarse, tras formar un producto con un par de electrones libre nuevo'
new2 = '"why": "Se trata la síntesis como si se detuviera sola en el primer producto, sin pensar que ese producto también es nucleófilo.",\n        "how_to_avoid": "Preguntarse, tras formar un producto con un par de electrones libre nuevo'
data = apply(data, old2, new2, 'common_mistakes[2].why')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
