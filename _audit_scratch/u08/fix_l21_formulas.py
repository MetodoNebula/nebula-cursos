path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

i0 = data.find('"21_Polimerización_por_adición.json"')
i1 = data.find('"22_', i0)
seg = data[i0:i1]

formula_edits = [
    ('(-CH2-CH(C6H5)-)n', '(-CH$_2$-CH(C$_6$H$_5$)-)$_n$'),
    ('(-CH2-CH(CH3)-)n', '(-CH$_2$-CH(CH$_3$)-)$_n$'),
    ('(-CH2-CH2-)n', '(-CH$_2$-CH$_2$-)$_n$'),
    ('(-CH2-CHCl-)n', '(-CH$_2$-CHCl-)$_n$'),
    ('(C2H3Cl)', '(C$_2$H$_3$Cl)'),
    ('(C6H5-)', '(C$_6$H$_5$-)'),
    ('(CH2=CH2)', '(CH$_2$=CH$_2$)'),
    ('(CH2=CHCl)', '(CH$_2$=CHCl)'),
    ('-CH2-CH(CH3)-', '-CH$_2$-CH(CH$_3$)-'),
    ('-CH2-CH2-', '-CH$_2$-CH$_2$-'),
    ('-CH2-CHCl-', '-CH$_2$-CHCl-'),
    ('-CF2-CF2-', '-CF$_2$-CF$_2$-'),
    ('-CH3', '-CH$_3$'),
    ('C2H3Cl', 'C$_2$H$_3$Cl'),
    ('C2H4', 'C$_2$H$_4$'),
    ('C6H5-CH=CH2', 'C$_6$H$_5$-CH=CH$_2$'),
    ('CH2=CH-CH3', 'CH$_2$=CH-CH$_3$'),
    ('CH2=CH-R', 'CH$_2$=CH-R'),
    ('CH2=CH2', 'CH$_2$=CH$_2$'),
    ('CH2=CHCl', 'CH$_2$=CHCl'),
    ('HO-CH2-CH2-OH', 'HO-CH$_2$-CH$_2$-OH'),
    ('el CH2 terminal', 'el CH$_2$ terminal'),
    ('M1=5000', 'M$_1$=5000'),
    ('M1=n1', 'M$_1$=n$_1$'),
    ('M2=10', 'M$_2$=10'),
    ('M2=2M1', 'M$_2$=2M$_1$'),
    ('M2=n2', 'M$_2$=n$_2$'),
    ('M(C2F4)=100', 'M(C$_2$F$_4$)=100'),
    ('(M2', '(M$_2$'),
    ('M1', 'M$_1$'),
    ('M2', 'M$_2$'),
    ('n1', 'n$_1$'),
    ('n2', 'n$_2$'),
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
