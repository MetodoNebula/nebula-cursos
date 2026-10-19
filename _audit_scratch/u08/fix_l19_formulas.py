path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

key19 = '19_Oxidación_y_reducción_orgánica.json'
key20_prefix = '"20_'
i0 = data.find('"' + key19 + '"')
assert i0 != -1
i1 = data.find(key20_prefix, i0)
assert i1 != -1
seg = data[i0:i1]
print('segment length', len(seg))

protect_start = seg.find('"assets": [')
assert protect_start != -1
protect_end = seg.find('"id": "TH-Q08-19-4"', protect_start)
assert protect_end != -1

before = seg[:protect_start]
protected = seg[protect_start:protect_end]
after = seg[protect_end:]

assert 'ALC2' in protected

formula_edits = [
    ('((CH3)3COH', '((CH$_3$)$_3$COH'),
    ('(CH3)3COH', '(CH$_3$)$_3$COH'),
    ('CH3CH2CH2CH2CH2OH', 'CH$_3$CH$_2$CH$_2$CH$_2$CH$_2$OH'),
    ('CH3CH2CH2CH2CHO', 'CH$_3$CH$_2$CH$_2$CH$_2$CHO'),
    ('CH3CH2CH2CH2COOH', 'CH$_3$CH$_2$CH$_2$CH$_2$COOH'),
    ('CH3CH2CH2CH2OH', 'CH$_3$CH$_2$CH$_2$CH$_2$OH'),
    ('CH3CH(OH)CH2CH3', 'CH$_3$CH(OH)CH$_2$CH$_3$'),
    ('CH3CH(OH)CH3', 'CH$_3$CH(OH)CH$_3$'),
    ('CH3CH2CH2CHO', 'CH$_3$CH$_2$CH$_2$CHO'),
    ('CH3CH2CH2COOH', 'CH$_3$CH$_2$CH$_2$COOH'),
    ('CH3CH2CH2OH', 'CH$_3$CH$_2$CH$_2$OH'),
    ('CH3CH2COOCH3', 'CH$_3$CH$_2$COOCH$_3$'),
    ('CH3CH2COOH', 'CH$_3$CH$_2$COOH'),
    ('CH3CH2CHO', 'CH$_3$CH$_2$CHO'),
    ('CH3COCH2CH3', 'CH$_3$COCH$_2$CH$_3$'),
    ('CH3COCH3', 'CH$_3$COCH$_3$'),
    ('CH3OH', 'CH$_3$OH'),
    ('-CH2OH', '-CH$_2$OH'),
    ('-OCH3', '-OCH$_3$'),
    ('R-CH2OH', 'R-CH$_2$OH'),
    ('C3H8O', 'C$_3$H$_8$O'),
    ('C3H6O', 'C$_3$H$_6$O'),
    ('C4H10', 'C$_4$H$_{10}$'),
    ('4CO2', '4CO$_2$'),
    ('5H2O', '5H$_2$O'),
    ('CO2', 'CO$_2$'),
    ('H2O', 'H$_2$O'),
    ('O2', 'O$_2$'),
    ('KMnO4', 'KMnO$_4$'),
    ('K2Cr2O7', 'K$_2$Cr$_2$O$_7$'),
    ('NaBH4', 'NaBH$_4$'),
    ('LiAlH4', 'LiAlH$_4$'),
    ('CrO3', 'CrO$_3$'),
]

count_report = []
for old, new in formula_edits:
    cb = before.count(old)
    ca = after.count(old)
    before = before.replace(old, new)
    after = after.replace(old, new)
    count_report.append((old, cb, ca))

for old, cb, ca in count_report:
    print(f'{old!r}: before={cb} after={ca}')

new_seg = before + protected + after
data = data[:i0] + new_seg + data[i1:]
open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN new total length', len(data))
