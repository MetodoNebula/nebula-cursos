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

# Fix answer: use unicode arrow instead of broken LaTeX
old1 = "(a) HOOC-C6H4-COOH + HO-CH2CH2-OH " + BS + "rightarrow HOOC-C6H4-CO-O-CH2CH2-OH + H2O. (b) [-CO-C6H4-CO-O-CH2-CH2-O-]n (C10H8O4). (c) 192,17 g/mol."
new1 = "(a) HOOC-C6H4-COOH + HO-CH2CH2-OH → HOOC-C6H4-CO-O-CH2CH2-OH + H2O. (b) [-CO-C6H4-CO-O-CH2-CH2-O-]n (C10H8O4). (c) 192,17 g/mol."
rep(old1, new1, 1, "fix answer arrow")

# Fix full_solution: missing backslash before mathrm
old2 = "(a) $mathrm{HOOC"
new2 = "(a) $" + BS + "mathrm{HOOC"
rep(old2, new2, 1, "fix mathrm backslash")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE A2")
