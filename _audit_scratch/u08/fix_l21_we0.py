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

old = ('{' + BS + 'text{eteno}} = 24{,}022+4{,}032 = 28{,}054' + BS + ',' + BS
       + 'mathrm{g/mol}$; {' + BS + 'text{polímero}} = 500' + BS
       + 'cdot28{,}054 = 14' + chr(92) + '!' + chr(92) + ' 027' + BS + ',' + BS
       + 'mathrm{g/mol} ' + BS + 'approx 1{,}40' + BS + 'times10^{4}' + BS + ',' + BS + 'mathrm{g/mol}$.')
new = ('$M_{' + BS + 'text{eteno}} = 24{,}022+4{,}032 = 28{,}054' + BS + ',' + BS
       + 'mathrm{g/mol}$; $M_{' + BS + 'text{polímero}} = 500' + BS
       + 'cdot28{,}054 = 14' + BS + ',' + '027' + BS + ',' + BS
       + 'mathrm{g/mol} ' + BS + 'approx 1{,}40' + BS + 'times10^{4}' + BS + ',' + BS + 'mathrm{g/mol}$.')
data = apply(data, old, new, 'worked_examples[0].solution fix prefix')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
