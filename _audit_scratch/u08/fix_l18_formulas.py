path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()

key18 = '"18_Reacciones_de_sustitución.json"'
key19 = '"19_'
i0 = data.find(key18)
assert i0 != -1
i1 = data.find(key19, i0)
assert i1 != -1
seg = data[i0:i1]
print('segment length', len(seg))

# Exclude the tikz/svg asset block from formula conversion entirely.
tikz_start = seg.find('"tikz":')
assert tikz_start != -1
# find the end of the asset object: locate the closing of "assets": [ ... ] array -> find pattern '"\n          }\n        ]' after tikz_start, safer: find next occurrence of '"provenance": "SOURCE_DERIVED"' AFTER the assets block closes.
# The asset object itself ends with the closing of "svg" string then "}" then "]" (assets array) then "}" (theory_blocks[1] object).
svg_key = '"svg":'
svg_start = seg.find(svg_key, tikz_start)
assert svg_start != -1
# svg value is a big single-line string ending right before '"\n        }\n      ]\n    },' roughly. Let's find the end by searching for the end of theory_blocks[1] object: the next '"id": "TH-Q08-18-3"' marks the start of theory_blocks[2].
next_marker = '"id": "TH-Q08-18-3"'
protect_end = seg.find(next_marker, svg_start)
assert protect_end != -1
protect_start = tikz_start

before = seg[:protect_start]
protected = seg[protect_start:protect_end]
after = seg[protect_end:]

print('protected block length', len(protected))
# sanity: protected should contain R2/B2/A2 tikz node refs
assert '(R2)' in protected and '(B2)' in protected and '(A2)' in protected

formula_edits = [
    ('CH3CH2CH2CH2NH2', 'CH$_3$CH$_2$CH$_2$CH$_2$NH$_2$'),
    ('CH3CH2CH2CH2Cl', 'CH$_3$CH$_2$CH$_2$CH$_2$Cl'),
    ('CH3CH2CH2COOH', 'CH$_3$CH$_2$CH$_2$COOH'),
    ('CH3-CH(OH)-CH2-CH3', 'CH$_3$-CH(OH)-CH$_2$-CH$_3$'),
    ('CH3-CHBr-CH2-CH3', 'CH$_3$-CHBr-CH$_2$-CH$_3$'),
    ('CH3-CH2-CH2-Br', 'CH$_3$-CH$_2$-CH$_2$-Br'),
    ('CH3CH2CH2NH2', 'CH$_3$CH$_2$CH$_2$NH$_2$'),
    ('CH3CH2CH2OH', 'CH$_3$CH$_2$CH$_2$OH'),
    ('CH3CH2CH2CN', 'CH$_3$CH$_2$CH$_2$CN'),
    ('CH3CH2CH2Cl', 'CH$_3$CH$_2$CH$_2$Cl'),
    ('CH3CH2CH2Br', 'CH$_3$CH$_2$CH$_2$Br'),
    ('CH3CH2O' + chr(8315) + 'Na' + chr(8314), 'CH$_3$CH$_2$O' + chr(8315) + 'Na' + chr(8314)),
    ('CH3CH2O' + chr(8315), 'CH$_3$CH$_2$O' + chr(8315)),
    ('CH3CH2-NH-CH3', 'CH$_3$CH$_2$-NH-CH$_3$'),
    ('CH3CH2-O-CH3', 'CH$_3$CH$_2$-O-CH$_3$'),
    ('CH3CH2OCH3', 'CH$_3$CH$_2$OCH$_3$'),
    ('CH3CH2NH2', 'CH$_3$CH$_2$NH$_2$'),
    ('CH3CH2OH', 'CH$_3$CH$_2$OH'),
    ('CH3CH2CN', 'CH$_3$CH$_2$CN'),
    ('CH3CH2Br', 'CH$_3$CH$_2$Br'),
    ('CH3CH=CH2', 'CH$_3$CH=CH$_2$'),
    ('CH2BrCH2Br', 'CH$_2$BrCH$_2$Br'),
    ('CH2=CH2', 'CH$_2$=CH$_2$'),
    ('CH3Br', 'CH$_3$Br'),
    ('NH3(exceso)', 'NH$_3$(exceso)'),
    ('2 NH3', '2 NH$_3$'),
    ('2NH3', '2NH$_3$'),
    ('NH4Br', 'NH$_4$Br'),
    ('NH4Cl', 'NH$_4$Cl'),
    ('NH4' + chr(8314) + 'X' + chr(8315), 'NH$_4$' + chr(8314) + 'X' + chr(8315)),
    ('NH4X)', 'NH$_4$X)'),
    ('R-NH2', 'R-NH$_2$'),
    ('NH3', 'NH$_3$'),
    ('Br2', 'Br$_2$'),
    ('CH4', 'CH$_4$'),
    ('H2O', 'H$_2$O'),
    ('X2', 'X$_2$'),
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
print('WRITTEN, new total length', len(data))
