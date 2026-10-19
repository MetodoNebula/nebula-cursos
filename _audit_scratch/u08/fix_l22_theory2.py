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

old = ("Este orden " + chr(8212) + "C, H y O al final" + chr(8212) + " no es casualidad: el oxígeno es el elemento que aparece en más sustancias a la vez (O2, CO2, H2O y, a veces, el propio combustible), así que conviene dejarlo para cuando los demás coeficientes ya están fijados.")
new = (old + NL + NL
       + '**Tres tipos de problema PAU que se construyen sobre esta misma ecuación:**' + NL + NL
       + '1) *Fórmula empírica por análisis de combustión*: si se quema una masa conocida de un compuesto C,H,O y se recogen las masas de CO2 y H2O producidas, cada mol de CO2 revela los moles de C y cada mol de H2O revela el doble de moles de H del compuesto original; el oxígeno, si lo hay, se obtiene por diferencia de masa. Por ejemplo: la combustión completa de 2,30 g de un compuesto C,H,O da 4,40 g de CO2 y 2,70 g de H2O; de ahí se llega a la fórmula empírica C2H6O.' + NL + NL
       + '2) *Volumen de gases*: con la ecuación de los gases ideales, $pV=nRT$, se puede pasar de los moles de CO2 (o de O2 consumido) a un volumen en unas condiciones dadas; y, como el aire contiene aproximadamente un 21 % de O2 en volumen, el volumen de O2 necesario se puede convertir en volumen de aire dividiendo entre 0,21.' + NL + NL
       + '3) *Calor de combustión* ($' + BS + 'Delta H_c$): cada combustible tiene una entalpía de combustión característica (energía liberada por mol o por gramo); conocido ese dato, la energía total liberada en una combustión se calcula multiplicando los moles de combustible quemados por su $' + BS + 'Delta H_c$.')
data = apply(data, old, new, 'theory_blocks[1] add empirical/gas/enthalpy block')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
