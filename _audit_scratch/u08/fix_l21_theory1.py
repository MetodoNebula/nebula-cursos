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

old_eq = '$n' + BS + ' CH_2{=}CH_2 ' + BS + 'longrightarrow (-CH_2-CH_2-)_n$'
new_eq = '$n' + BS + ',' + BS + 'mathrm{CH_2{=}CH_2} ' + BS + 'longrightarrow ' + BS + 'mathrm{({-}CH_2{-}CH_2{-})}_n$'
data = apply(data, old_eq, new_eq, 'theory_blocks[1] main equation')

old_c2h4 = 'con la misma fórmula molecular que el monómero (C2H4), solo que ha cambiado el doble enlace por dos enlaces simples'
new_c2h4 = 'con la misma fórmula molecular que el monómero (C$_2$H$_4$), solo que ha cambiado el doble enlace por dos enlaces simples'
data = apply(data, old_c2h4, new_c2h4, 'theory_blocks[1] C2H4')

old_m = ('Como no se pierde ningún átomo, la masa molar del polímero es, exactamente, $M_{polímero} = n ' + BS[0]
         + 'cdot M_{monómero}$. Esta es la idea cuantitativa clave de toda la lección: la masa molar de un polímero de adición es siempre un múltiplo exacto de la del monómero del que procede.')
new_m = ('Como no se pierde ningún átomo, para una cadena cualquiera (despreciando los dos extremos, restos del iniciador que la empezó) la masa molar es, exactamente, $M_{' + BS + 'text{polímero}} = n ' + BS[0]
         + 'cdot M_{' + BS + 'text{monómero}}$. Esta es la idea cuantitativa clave de la lección, pero con un matiz importante: una muestra real de polímero no tiene todas sus cadenas de la misma longitud, así que lo que se mide es una masa molar media, $' + BS[0] + 'bar{M} = ' + BS[0] + 'bar{n}' + BS[0] + 'cdot M_{' + BS + 'text{monómero}}$, y el grado de polimerización medio $' + BS[0] + 'bar{n}$ no tiene por qué salir un número entero (es un promedio sobre muchas cadenas de longitudes distintas).')
data = apply(data, old_m, new_m, 'theory_blocks[1] multiplo exacto fix')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
