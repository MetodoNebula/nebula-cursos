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

old_m = ('Como no se pierde ningún átomo, la masa molar del polímero es, exactamente, $M_{polímero} = n ' + BS
         + 'cdot M_{monómero}$. Esta es la idea cuantitativa clave de toda la lección: la masa molar de un polímero de adición es siempre un múltiplo exacto de la del monómero del que procede.')
new_m = ('Como no se pierde ningún átomo, para una cadena cualquiera (despreciando los dos extremos, restos del iniciador que la empezó), la masa molar es, exactamente, $M_{' + BS + 'text{polímero}} = n ' + BS
         + 'cdot M_{' + BS + 'text{monómero}}$. Esta es la idea cuantitativa clave de la lección, con un matiz importante: una muestra real de polímero no tiene todas sus cadenas de la misma longitud, así que lo que se mide es una masa molar media, $' + BS
         + 'bar{M} = ' + BS + 'bar{n}' + BS + 'cdot M_{' + BS + 'text{monómero}}$, y el grado de polimerización medio $' + BS
         + 'bar{n}$ no tiene por qué salir un número entero, porque es un promedio sobre muchas cadenas de longitudes distintas.')
data = apply(data, old_m, new_m, 'theory_blocks[1] multiplo exacto fix')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
