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

old_t1_eq = "$R-COOH + HO-R' " + BS + "rightleftharpoons R-COO-R' + H_2O$"
new_t1_eq = '$' + BS + "mathrm{R{-}COOH + HO{-}R' " + BS + "overset{H^+}{" + BS + "rightleftharpoons} R{-}COO{-}R' + H_2O}$"
data = apply(data, old_t1_eq, new_t1_eq, 't1 main equation')

old_t1_ex = ('acetato de etilo (etanoato de etilo): $CH_3COOH + CH_3CH_2OH ' + BS
             + 'rightleftharpoons CH_3COOCH_2CH_3 + H_2O$.')
new_t1_ex = ('acetato de etilo (etanoato de etilo): $' + BS + 'mathrm{CH_3COOH(l) + CH_3CH_2OH(l) '
             + BS + 'overset{H^+}{' + BS + 'rightleftharpoons} CH_3COOCH_2CH_3(l) + H_2O(l)}$.')
data = apply(data, old_t1_ex, new_t1_ex, 't1 example equation')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
