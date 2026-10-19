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

old9 = ('La facilidad de reducción de los grupos con carbono unido a oxígeno sigue este orden, de más difícil a más fácil de reducir:' + NL + NL
        + '$-COOH < -COO- < -CO- < -CHO$' + NL + NL
        + '(ácido < éster < cetona < aldehído).')
new9 = ('La facilidad de reducción de los grupos con carbono unido a oxígeno sigue este orden, de más difícil a más fácil de reducir:' + NL + NL
        + 'ácido ($' + BS + 'mathrm{{-}COOH}$) < éster ($' + BS + 'mathrm{{-}COO{-}}$) < cetona ($' + BS + 'mathrm{{>}C{=}O}$) < aldehído ($' + BS + 'mathrm{{-}CHO}$).')
data = apply(data, old9, new9, 'theory_blocks[4] reduction order')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
