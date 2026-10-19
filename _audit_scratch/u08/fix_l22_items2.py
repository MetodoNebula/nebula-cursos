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

old8 = 'El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.'
new8 = 'Se memoriza el ajuste de los hidrocarburos (sin oxígeno propio) como una receta fija y se aplica igual a alcoholes, éteres o ácidos, sin contar el oxígeno que la molécula ya trae.'
data = apply(data, old8, new8, 'common_mistakes[0].why')

old9 = 'C3H8 + 5 O2 → 3 CO2 + 4 H2O.'
new9 = '$' + BS + 'mathrm{C_3H_8(g) + 5' + BS + ',O_2(g) ' + BS + 'longrightarrow 3' + BS + ',CO_2(g) + 4' + BS + ',H_2O(l)}$.'
data = apply(data, old9, new9, 'worked_examples[0].solution')

old10 = 'porque el propano tiene un número par de hidrógenos entre 4 (8/4=2, entero) y no contiene oxígeno propio que haya que restar'
new10 = 'porque los productos necesitan 2' + chr(183) + '3 + 4 = 10 átomos de O (un número par) y el propano no aporta oxígeno propio que haya que restar: 10/2 = 5 O2, sin resto'
data = apply(data, old10, new10, 'worked_examples[0].interpretation')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
