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

old = "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"
new = "Sin justificación, 0 puntos aunque la calificación V/F sea correcta; en (a) y (b) se exige distinguir condensación de adición en cuanto a masa y bifuncionalidad, no solo repetir la definición"
rep(old, new, 1, "PLANTILLA mark_scheme")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE K")
