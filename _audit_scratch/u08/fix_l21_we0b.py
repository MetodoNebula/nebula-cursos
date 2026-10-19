path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2

old = 'Primero se calcula la masa molar del monómero: {' + BS + 'text{eteno}} = 2' + BS + 'cdot12{,}011 + 4' + BS + 'cdot1{,}008$.'
new = 'Primero se calcula la masa molar del monómero: $M_{' + BS + 'text{eteno}} = 2' + BS + 'cdot12{,}011 + 4' + BS + 'cdot1{,}008$.'
c = data.count(old)
print('count', c)
data = data.replace(old, new)
open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
