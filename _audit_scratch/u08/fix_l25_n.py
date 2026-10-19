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
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

old1 = "de un diácido de masa M1 y n moléculas de una diamina de masa M2."
new1 = "de un diácido de masa $M_1$ y n moléculas de una diamina de masa $M_2$."
rep(old1, new1, 1, "statement M1 M2 prose 1")

old2 = "(a) Escribe, en función de n, M1 y M2, la expresión"
new2 = "(a) Escribe, en función de n, $M_1$ y $M_2$, la expresión"
rep(old2, new2, 1, "statement M1 M2 prose 2")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE N")
