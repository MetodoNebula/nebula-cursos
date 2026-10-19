import io, sys

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

key_start = '"17_Regla_de_SaytzeffZaitsev.json"'
key_end = '"18_Reacciones_de_sustitución.json"'
i0 = data.find(key_start)
i1 = data.find(key_end)
assert i0 != -1 and i1 != -1 and i0 < i1
seg = data[i0:i1]

BS = chr(92) * 2

# #11 summary.formulas[0]: rebalance + mathrm
old_f = '"\\\\text{2-bromobutano} + KOH \\\\rightarrow CH_3-CH=CH-CH_3\\\\ (\\\\text{mayoritario}) + CH_2=CH-CH_2-CH_3\\\\ (\\\\text{minoritario})"'
new_f = (
    f'"{BS}text{{2-bromobutano}} + {BS}mathrm{{KOH}} {BS}xrightarrow{{{BS}text{{etanol}},{chr(92)}{chr(92)} {BS}Delta}} '
    f'{BS}mathrm{{CH_3CH{{=}}CHCH_3}}{BS} ({BS}text{{mayoritario}}) + {BS}mathrm{{CH_2{{=}}CHCH_2CH_3}}{BS} ({BS}text{{minoritario}}) + {BS}mathrm{{KBr}} + {BS}mathrm{{H_2O}}"'
)
c = seg.count(old_f)
print("summary.formulas old count:", c)
assert c == 1
seg = seg.replace(old_f, new_f, 1)
print("OK summary.formulas rebalanced")

# #7 arrow pattern ->(alc.)-> and ->(H2SO4, Delta)->
arrow_edits = [
 (chr(8594)+"(alc.)"+chr(8594), chr(36)+BS+"xrightarrow{"+BS+"text{etanol}}"+chr(36)),
 (chr(8594)+"(H2SO4, "+chr(916)+")"+chr(8594), chr(36)+BS+"xrightarrow[" +BS+"Delta]{"+BS+"text{H}_2"+BS+"text{SO}_4}"+chr(36)),
]
for old, new in arrow_edits:
    n = seg.count(old)
    seg = seg.replace(old, new)
    print(f"ARROW replace {old!r} -> {new!r} : {n}")

# comprehensive plain-text formula conversion (longest-first)
formula_edits = [
 ("CH3-CH(OH)-CH2-CH2-CH3", "CH$_3$-CH(OH)-CH$_2$-CH$_2$-CH$_3$"),
 ("CH3-CH2-CHBr-CH2-CH3", "CH$_3$-CH$_2$-CHBr-CH$_2$-CH$_3$"),
 ("CH3-CH2-CH=CH-CH3", "CH$_3$-CH$_2$-CH=CH-CH$_3$"),
 ("CH3-CH2-CH2-CH=CH2", "CH$_3$-CH$_2$-CH$_2$-CH=CH$_2$"),
 ("(CH3)2CBr-CH2-CH3", "(CH$_3$)$_2$CBr-CH$_2$-CH$_3$"),
 ("(CH3)2C=CH-CH3", "(CH$_3$)$_2$C=CH-CH$_3$"),
 ("CH2=C(CH3)-CH2-CH3", "CH$_2$=C(CH$_3$)-CH$_2$-CH$_3$"),
 ("CH3-CHBr-CH2-CH3", "CH$_3$-CHBr-CH$_2$-CH$_3$"),
 ("CH3-CHCl-CH2-CH3", "CH$_3$-CHCl-CH$_2$-CH$_3$"),
 ("CH3-CH(OH)-CH2-CH3", "CH$_3$-CH(OH)-CH$_2$-CH$_3$"),
 ("CH3-CH2-CH=CH2", "CH$_3$-CH$_2$-CH=CH$_2$"),
 ("CH3-CH=CH-CH3", "CH$_3$-CH=CH-CH$_3$"),
 ("=CH2", "=CH$_2$"),
 ("H2SO4", "H$_2$SO$_4$"),
 ("H2O", "H$_2$O"),
 ("CH3", "CH$_3$"),
]
formula_edits.sort(key=lambda p: -len(p[0]))
for old, new in formula_edits:
    n = seg.count(old)
    seg = seg.replace(old, new)
    print(f"LATEX replace {old!r} -> {new!r} : {n}")

data2 = data[:i0] + seg + data[i1:]
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data2)
print("ALL EDITS APPLIED")
