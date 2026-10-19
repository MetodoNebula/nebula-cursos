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

old_ans = ('Etanol: $1{,}91$ g de CO$_2$ por gramo; combustible estudiado: $3{,}08$ g/g. El segundo produce unas $3{,}08/1{,}91' + BS + 'approx1{,}61$ veces más.')
new_ans = ('Etanol: $1{,}91$ g de CO$_2$ por gramo; octano: $3{,}08$ g de CO$_2$ por gramo. El octano emite unas $3{,}08/1{,}91' + BS + 'approx1{,}61$ veces más CO$_2$ por gramo de combustible.')
data = apply(data, old_ans, new_ans, 'challenge_questions[0].answer')

old_fs = ("convierte una fracción mayor de su propia masa en CO2 al arder. Es el mismo argumento, visto desde el lado de las emisiones, que explica por qué ciertos biocombustibles oxigenados se promueven como alternativa con menor huella de carbono por unidad de masa quemada.")
new_fs = ("convierte una fracción mayor de su propia masa en CO2 al arder. Ojo con la conclusión que podría parecer obvia: que el etanol emita menos CO2 por gramo no lo hace automáticamente mejor para el clima por esa sola razón, porque también libera menos energía por gramo (entalpía de combustión: etanol " + chr(8776) + " 29,7 kJ/g; octano " + chr(8776) + " 47,9 kJ/g); de hecho, el CO2 emitido por unidad de ENERGÍA liberada es muy similar en ambos casos (" + chr(8776) + " 0,064 g CO2/kJ). La verdadera ventaja climática de un biocombustible como el etanol no está en la química de su combustión, sino en que su carbono procede de CO2 atmosférico fijado recientemente por las plantas de las que se obtiene, no de carbono fósil.")
data = apply(data, old_fs, new_fs, 'challenge_questions[0].full_solution')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
