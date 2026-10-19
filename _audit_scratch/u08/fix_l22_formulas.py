path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

i0 = data.find('"22_Combustión_e_integración_estequiométrica.json"')
i1 = data.find('"23_', i0)
seg = data[i0:i1]

formula_edits = [
    ('C4H10O', 'C$_4$H$_{10}$O'),
    ('C8H18', 'C$_8$H$_{18}$'),
    ('C4H10', 'C$_4$H$_{10}$'),
    ('C3H8', 'C$_3$H$_8$'),
    ('C2H6O', 'C$_2$H$_6$O'),
    ('CH4O', 'CH$_4$O'),
    ('H2O2', 'H$_2$O$_2$'),
    ('CO2', 'CO$_2$'),
    ('H2O', 'H$_2$O'),
    ('O3', 'O$_3$'),
    ('O2', 'O$_2$'),
]

count_report = []
for old, new in formula_edits:
    c = seg.count(old)
    seg = seg.replace(old, new)
    count_report.append((old, c))

for old, c in count_report:
    print(f'{old!r}: {c}')

data = data[:i0] + seg + data[i1:]
open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
