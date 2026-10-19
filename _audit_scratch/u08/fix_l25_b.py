import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"25_Polimerización')
i1 = data.find('"26_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+250]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

BS = chr(92)*2
NL = chr(92)+'n'

# F14a: theory_blocks[0].body erratum
old = "el enlace que crece la cadena, y una molécula pequeña"
new = "el enlace que hace crecer la cadena, y una molécula pequeña"
rep(old, new, 1, "F14a tb0")

# F11: theory_blocks[1].body reversible arrow with conditions
old = "$R" + BS + "text{-COOH} + HO" + BS + "text{-}R' " + BS + "rightarrow R" + BS + "text{-CO-O-}R' + H_2O$"
new = "$R" + BS + "text{-COOH} + HO" + BS + "text{-}R' " + BS + "overset{H^+,\\ " + BS + "text{calor}}{" + BS + "rightleftharpoons} R" + BS + "text{-CO-O-}R' + H_2O$"
rep(old, new, 1, "F11 tb1 arrow")

# F6: theory_blocks[2].body IUPAC name
old6 = "el ácido tereftálico (HOOC-C6H4-COOH, M=166,13 g/mol)"
new6 = "el ácido tereftálico o ácido benceno-1,4-dicarboxílico (HOOC-C6H4-COOH, M=166,13 g/mol)"
rep(old6, new6, 1, "F6 tb2 IUPAC")

old6b = "El PET (politereftalato de etileno), usado en envases de bebidas,"
new6b = "El PET, o poli(tereftalato de etileno), usado en envases de bebidas,"
rep(old6b, new6b, 1, "F6b PET IUPAC")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE B")
