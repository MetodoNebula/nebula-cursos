path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

# Finding 2: mcq[3].options[3].why_wrong
old2 = "El éster de ácido acético y metanol es el acetato de metilo (etanoato de metilo, CH₃COOCH₃), no el propanoato de etilo pedido en el enunciado."
new2 = "El éster de ácido acético y metanol es el acetato de metilo (etanoato de metilo, CH₃COOCH₃), no el acetato de propilo pedido en el enunciado: 'de propilo' exige propan-1-ol, no metanol."
data = apply(data, old2, new2, 'mcq[3].options[3].why_wrong')

# Finding 3: mcq[3].options[2]
old3 = '"text": "Propan-1-ol y ácido acético, pero con el alcohol aportando el grupo que da nombre al ácido",\n      "why_wrong": "Intercambia los papeles de las dos palabras del nombre: \'acetato\' siempre nombra la parte del ácido, y \'de propilo\' la parte del alcohol, nunca al revés."'
new3 = '"text": "Ácido propanoico y etanol",\n      "why_wrong": "Ni el ácido (3 carbonos) ni el alcohol (2 carbonos) coinciden con el éster pedido: \'acetato\' exige ácido acético (2 carbonos) y \'de propilo\' exige propan-1-ol (3 carbonos); es simplemente un éster distinto, propanoato de etilo."'
data = apply(data, old3, new3, 'mcq[3].options[2]')

# Finding 4+5: challenge_questions[0] answer + full_solution (both isomers)
old45a = 'Ácido butanoico (CH3CH2CH2COOH); el éster X es butanoato de metilo (CH3CH2CH2COOCH3).'
new45a = 'El ácido C4H8O2 admite dos isómeros válidos: ácido butanoico (CH3CH2CH2COOH, cadena lineal) y ácido 2-metilpropanoico ((CH3)2CHCOOH, cadena ramificada). Con los datos del enunciado no se puede distinguir entre ellos: el éster X es butanoato de metilo (si el ácido es el lineal) o 2-metilpropanoato de metilo (si es el ramificado).'
data = apply(data, old45a, new45a, 'challenge_questions[0].answer')

old45b = 'que es exactamente la fórmula del ácido butanoico, CH3CH2CH2COOH. Comprobación por el camino directo (esterificación): CH3CH2CH2COOH (C4H8O2) + CH3OH (CH4O) ⇌ C5H10O2+H2O. Sumando átomos a la izquierda: C5H12O3; a la derecha: C5H10O2+H2O=C5H12O3. Cuadra. El éster X es, por tanto, el butanoato de metilo.'
new45b = 'que es la fórmula molecular C4H8O2, compatible con dos ácidos distintos: el ácido butanoico (CH3CH2CH2COOH, cadena lineal) y su isómero ramificado, el ácido 2-metilpropanoico ((CH3)2CHCOOH). Comprobación por el camino directo (esterificación) con el isómero lineal: CH3CH2CH2COOH (C4H8O2) + CH3OH (CH4O) ⇌ C5H10O2+H2O. Sumando átomos a la izquierda: C5H12O3; a la derecha: C5H10O2+H2O=C5H12O3. Cuadra, y la misma comprobación de átomos cuadra igual con el isómero ramificado, porque el balance no depende de cómo esté ramificada la cadena. El éster X es, por tanto, butanoato de metilo o 2-metilpropanoato de metilo, según cuál de los dos ácidos isómeros sea el de partida; el enunciado, tal como está, no permite decidir entre ambos.'
data = apply(data, old45b, new45b, 'challenge_questions[0].full_solution')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
