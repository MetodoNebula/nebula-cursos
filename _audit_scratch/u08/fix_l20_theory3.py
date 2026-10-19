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

old = ('| ácido acético (CH3COOH) | metanol (CH3OH) | acetato de metilo |' + NL
       + '| ácido propanoico (CH3CH2COOH) | etanol (CH3CH2OH) | propanoato de etilo |' + NL
       + '| ácido butanoico (CH3CH2CH2COOH) | propan-2-ol ((CH3)2CHOH) | butanoato de isopropilo |' + NL + NL
       + 'El truco para no confundir qué parte es cuál: la primera palabra del nombre (la que termina en -oato) siempre corresponde al grupo que, en la fórmula del éster, está unido al doble enlace a oxígeno (viene del ácido); la segunda palabra corresponde al grupo que cuelga del oxígeno sencillo (viene del alcohol, y es el que se perdió como -OH en la reacción).')

new = ('| ácido acético ($' + BS + 'mathrm{CH_3COOH}$) | metanol ($' + BS + 'mathrm{CH_3OH}$) | acetato de metilo |' + NL
       + '| ácido propanoico ($' + BS + 'mathrm{CH_3CH_2COOH}$) | etanol ($' + BS + 'mathrm{CH_3CH_2OH}$) | propanoato de etilo |' + NL
       + '| ácido butanoico ($' + BS + 'mathrm{CH_3CH_2CH_2COOH}$) | propan-2-ol ($' + BS + 'mathrm{(CH_3)_2CHOH}$) | butanoato de propan-2-ilo (isopropilo) |' + NL + NL
       + 'El truco para no confundir qué parte es cuál: la primera palabra del nombre (la que termina en -oato) siempre corresponde al grupo que, en la fórmula del éster, está unido al doble enlace a oxígeno (viene del ácido); la segunda palabra corresponde al grupo que cuelga del oxígeno sencillo (viene del alcohol, que conserva ese oxígeno y solo pierde el H de su -OH; el -OH que forma la molécula de agua lo aporta el ácido, no el alcohol, como demuestra el marcaje isotópico con ' + chr(185) + chr(56) + 'O). Dicho con los enlaces: R-CO-OH + H-O-R\' ' + BS + 'rightarrow R-CO-O-R\' + H-OH.')

data = apply(data, old, new, 'theory_blocks[2] table + explanation')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
