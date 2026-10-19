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

# Finding 14
old14 = '"full_solution": "(a) El ácido butanoico reacciona con el metanol, catalizado por ácido sulfúrico, liberando agua. El producto es el butanoato de metilo. (b)'
new14 = ('"full_solution": "(a) El ácido butanoico reacciona con el metanol, catalizado por ácido sulfúrico, liberando agua: $' + BS
         + 'mathrm{CH_3CH_2CH_2COOH + CH_3OH ' + BS + 'overset{H_2SO_4}{' + BS
         + 'rightleftharpoons} CH_3CH_2CH_2COOCH_3 + H_2O}$. El producto es el butanoato de metilo. (b)')
data = apply(data, old14, new14, 'exam_questions[0].full_solution eq')

# Finding 15: worked_examples[3].solution with justification
old15 = '"solution": "(a) Falsa. (b) Verdadera. (c) Falsa. (d) Falsa."'
new15 = '"solution": "(a) Falsa: es un equilibrio, no se agotan los reactivos. (b) Verdadera: es la reacción inversa exacta de la esterificación. (c) Falsa: el carboxilato formado no vuelve a esterificarse con facilidad. (d) Falsa: \'etilo\' viene del alcohol (etanol), no del ácido."'
data = apply(data, old15, new15, 'worked_examples[3].solution')

# Finding 18: exam_questions[1].mark_scheme[0]
old18 = '"1 punto por cada producto correcto (2 productos, 2 experimentos)"'
new18 = '"Para la puntuación completa: da el producto del experimento en medio ácido (1 punto) y el del experimento en medio básico (1 punto)"'
data = apply(data, old18, new18, 'exam_questions[1].mark_scheme[0]')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
