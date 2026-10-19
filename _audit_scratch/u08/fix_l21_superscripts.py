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

old1 = 'M_monómero=2' + chr(183) + '12,011+3' + chr(183) + '1,008+35,45=62,50 g/mol. M_PVC=250' + chr(183) + '62,50=15 625 g/mol ' + chr(8776) + ' 1,56' + chr(215) + '10^4 g/mol.'
new1 = ('$M_{' + BS + 'text{monómero}}=2' + BS + 'cdot12{,}011+3' + BS + 'cdot1{,}008+35{,}45=62{,}50' + BS + ',' + BS + 'mathrm{g/mol}$. '
        '$M_{' + BS + 'text{PVC}}=250' + BS + 'cdot62{,}50=15' + BS + ',625' + BS + ',' + BS + 'mathrm{g/mol} ' + BS + 'approx 1{,}56' + BS + 'times10^{4}' + BS + ',' + BS + 'mathrm{g/mol}$.')
data = apply(data, old1, new1, 'worked_examples[1].solution')

old2 = 'n = 280 000/28,054 = 9981 ' + chr(8776) + ' 9,98' + chr(215) + '10^3 unidades de eteno por cadena, en promedio.'
new2 = '$n = 280' + BS + ',000/28{,}054 = 9981 ' + BS + 'approx 9{,}98' + BS + 'times10^{3}$ unidades de eteno por cadena, en promedio.'
data = apply(data, old2, new2, 'worked_examples[2].solution')

old3 = 'n=1 084 764 (o redondeado, ' + chr(8776) + '1,08' + chr(183) + '10^6)'
new3 = '$n=1' + BS + ',084' + BS + ',764$ (o redondeado, $' + BS + 'approx1{,}08' + BS + 'cdot10^{6}$)'
data = apply(data, old3, new3, 'mcq[3].options[2].text')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
