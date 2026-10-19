path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2
NL = chr(92) + 'n'

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

# ---- theory_blocks[1] ----
old_t1_eq = '$R-COOH + HO-R\' \\rightleftharpoons R-COO-R\' + H_2O$'
new_t1_eq = '$' + BS + 'mathrm{R{-}COOH + HO{-}R\' ' + BS + 'overset{H^+}{' + BS + 'rightleftharpoons} R{-}COO{-}R\' + H_2O}$'
data = apply(data, old_t1_eq, new_t1_eq, 't1 main equation')

old_t1_two = 'se nombra con dos palabras: la primera, terminada en -oato, nombra la parte procedente del ácido (con su propio número de carbonos); la segunda, \'de + nombre del radical\', nombra la parte procedente del alcohol.'
new_t1_two = 'se nombra con la estructura ' + chr(171) + '(raíz del ácido)-oato de (radical del alcohol)-ilo' + chr(187) + ' (tres palabras, no dos): la primera, terminada en -oato, nombra la parte procedente del ácido (con su propio número de carbonos); la segunda, \'de + nombre del radical\', nombra la parte procedente del alcohol.'
data = apply(data, old_t1_two, new_t1_two, 't1 dos palabras fix')

old_t1_ex = 'Por ejemplo, ácido acético (ácido etanoico) + etanol da acetato de etilo (etanoato de etilo): $CH_3COOH + CH_3CH_2OH \\rightleftharpoons CH_3COOCH_2CH_3 + H_2O$.'
new_t1_ex = 'Por ejemplo, ácido acético (ácido etanoico) + etanol da acetato de etilo (etanoato de etilo): $' + BS + 'mathrm{CH_3COOH(l) + CH_3CH_2OH(l) ' + BS + 'overset{H^+}{' + BS + 'rightleftharpoons} CH_3COOCH_2CH_3(l) + H_2O(l)}$.'
data = apply(data, old_t1_ex, new_t1_ex, 't1 example equation')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN part1')
