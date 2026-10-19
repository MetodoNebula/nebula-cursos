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

# Finding 4: theory_blocks[2].body - add alcohol+HX and Williamson synthesis
old = 'primero se forma una sal de amonio sustituida, y una segunda molécula de amoniaco actúa como base arrancando un protón para liberar la amina neutra.'
new = ('primero se forma una sal de amonio sustituida, y una segunda molécula de amoniaco actúa como base arrancando un protón para liberar la amina neutra.'
       + NL + NL
       + '**Alcoholes ' + chr(8594) + ' haloalcanos** (sustitución inversa, con un hidrácido): $' + BS + 'mathrm{CH_3CH_2OH + HBr ' + BS + 'longrightarrow CH_3CH_2Br + H_2O}$.'
       + NL + NL
       + '**Éteres (síntesis de Williamson)**: un alcóxido (R' + chr(8242) + 'O' + chr(8315) + ') ataca a un haloalcano para dar un éter: $' + BS + 'mathrm{R{-}X + R' + chr(8242) + 'O^- ' + BS + 'longrightarrow R{-}O{-}R' + chr(8242) + ' + X^-}$.')
data = apply(data, old, new, 'theory_blocks[2] add alcohol/Williamson')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
