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

# Finding 1: theory_blocks[2] parity rule fix
old1 = ('Con un número impar de carbonos (y sin oxígeno propio que lo compense), el coeficiente x+y/4-z/2 sale a menudo fraccionario. Por ejemplo, para el butano (x=4, y=10, z=0): 4+10/4-0=6,5.')
new1 = ('El coeficiente x+y/4-z/2 sale fraccionario cuando el número 2x+y/2-z (los átomos de O que piden los productos, menos los que ya aporta el combustible) es impar. En los alcanos (sin oxígeno propio) esto ocurre con número PAR de carbonos, no impar: metano y propano (número impar de carbonos) dan coeficiente entero (2 y 5), mientras que etano, butano y octano (número par de carbonos) lo dan fraccionario. Por ejemplo, para el butano (x=4, y=10, z=0): 4+10/4-0=6,5.')
data = apply(data, old1, new1, 'theory_blocks[2] parity rule')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
