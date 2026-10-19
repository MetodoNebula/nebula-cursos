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

NL = chr(92) + 'n'

old6 = ('Oxidación: el carbono gana enlaces C-O (o, equivalentemente, pierde enlaces C-H).' + NL
        + '- Reducción: el carbono pierde enlaces C-O (gana enlaces C-H).')
new6 = ('Oxidación: aumenta el número de enlaces del carbono funcional a oxígeno (o a otro heteroátomo más electronegativo) y/o disminuye el de enlaces C-H.' + NL
        + '- Reducción: lo contrario: disminuye el número de enlaces a oxígeno y/o aumenta el de enlaces C-H (por ejemplo, la hidrogenación de un alqueno, que gana enlaces C-H sin perder ningún C-O, es una reducción).')
data = apply(data, old6, new6, 'theory_blocks[1] oxidation/reduction wording')

old7b = "Dos alcoholes distintos: R-CH2OH (de la parte ácida) y R'-OH (de la parte alcohólica del éster), porque el enlace C-O-C se rompe en dos fragmentos."
new7b = "Dos alcoholes distintos: R-CH2OH (de la parte ácida) y R'-OH (de la parte alcohólica del éster), porque se rompe el enlace entre el carbono del carbonilo y el oxígeno alcoxílico, no el C-O-C entero a la vez."
data = apply(data, old7b, new7b, 'flashcards[10].back')

old7c = "Se piensa en la reducción como un simple 'añadir hidrógenos' sin fijarse en que el enlace C-O-C del éster se rompe en dos fragmentos."
new7c = "Se piensa en la reducción como un simple 'añadir hidrógenos' sin fijarse en que es el enlace C(carbonilo)-O(alcoxi) concreto el que se rompe, separando el éster en sus dos mitades."
data = apply(data, old7c, new7c, 'common_mistakes[3].why')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
