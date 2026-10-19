path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

i0 = data.find('"20_Esterificación.json"')
i1 = data.find('"21_', i0)
seg = data[i0:i1]

formula_edits = [
    ('((CH3)2CHCOOH)', '((CH$_3$)$_2$CHCOOH)'),
    ('((CH3)2CHCOOH', '((CH$_3$)$_2$CHCOOH'),
    ('(CH3CH2CH2COOH', '(CH$_3$CH$_2$CH$_2$COOH'),
    ('(CH3CH2CH2OH)', '(CH$_3$CH$_2$CH$_2$OH)'),
    ('(CH3COOCH2CH3)', '(CH$_3$COOCH$_2$CH$_3$)'),
    ('(C4H8O2)', '(C$_4$H$_8$O$_2$)'),
    ('(CH4O)', '(CH$_4$O)'),
    ('CH3CH2CH2COOH', 'CH$_3$CH$_2$CH$_2$COOH'),
    ('CH3COOCH2CH2CH3', 'CH$_3$COOCH$_2$CH$_2$CH$_3$'),
    ('CH3CH2OH', 'CH$_3$CH$_2$OH'),
    ('CH3COOH', 'CH$_3$COOH'),
    ('CH3OH', 'CH$_3$OH'),
    ('C4H10O3', 'C$_4$H$_{10}$O$_3$'),
    ('C5H12O3', 'C$_5$H$_{12}$O$_3$'),
    ('C6H14O3', 'C$_6$H$_{14}$O$_3$'),
    ('C5H10O2', 'C$_5$H$_{10}$O$_2$'),
    ('C6H12O2', 'C$_6$H$_{12}$O$_2$'),
    ('C4H8O2', 'C$_4$H$_8$O$_2$'),
    ('C3H6O2', 'C$_3$H$_6$O$_2$'),
    ('C3H8O', 'C$_3$H$_8$O'),
    ('C2H4O2', 'C$_2$H$_4$O$_2$'),
    ('C2H6O', 'C$_2$H$_6$O'),
    ('H2O', 'H$_2$O'),
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
