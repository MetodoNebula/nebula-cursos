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

old_hyd = "$R-COO-R'+H_2O " + BS + "rightleftharpoons R-COOH+HO-R'$"
new_hyd = '$' + BS + "mathrm{R{-}COO{-}R' + H_2O " + BS + "rightleftharpoons R{-}COOH + HO{-}R'}$"
data = apply(data, old_hyd, new_hyd, 'theory_blocks[3] hydrolysis eq')

old_end = 'Por eso la hidrólisis básica se considera, a efectos prácticos, irreversible, mientras que la hidrólisis ácida sí es un verdadero equilibrio con la esterificación.'
new_end = ('Por eso la hidrólisis básica se considera, a efectos prácticos, irreversible, mientras que la hidrólisis ácida sí es un verdadero equilibrio con la esterificación. En la saponificación, además, la base no actúa como catalizador sino como reactivo que se consume: hace falta 1 mol de NaOH por cada mol de éster hidrolizado. Este es precisamente el origen del nombre: la saponificación (del latín sapo, jabón) de un triglicérido (el éster de la glicerina con tres ácidos grasos) con NaOH da glicerina más 3 moles de la sal del ácido graso, el jabón: $' + BS + 'mathrm{triglicérido + 3' + BS + ',NaOH ' + BS + 'rightarrow glicerina + 3' + BS + ',jabón}$.' + NL + NL
            + 'Como todo equilibrio, la esterificación tiene su constante: $K_c = ' + BS + 'dfrac{[' + BS + 'text{éster}][' + BS + 'mathrm{H_2O}]}{[' + BS + 'text{ácido}][' + BS + 'text{alcohol}]}$. Ejemplo numérico habitual en PAU: se mezcla 1 mol de ácido acético con 1 mol de etanol, con $K_c = 4$. Si reacciona una cantidad $x$ de ácido, en el equilibrio quedan $(1-x)$ mol de ácido y de alcohol, y se forman $x$ mol de éster y de agua; resolviendo $' + BS + 'frac{x^2}{(1-x)^2}=4$ se obtiene $' + BS + 'frac{x}{1-x}=2$, es decir $x=' + BS + 'frac{2}{3}' + BS + 'approx 0{,}67$ mol de éster (rendimiento del 66,7%). Si en vez de 1 mol se usan 3 mol de etanol (exceso del reactivo más barato), el equilibrio se desplaza y $x' + BS + 'approx 0{,}90$ mol, mostrando cómo el exceso de un reactivo aumenta el rendimiento en éster.')
data = apply(data, old_end, new_end, 'theory_blocks[3] add Kc+saponification stoichiometry')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
