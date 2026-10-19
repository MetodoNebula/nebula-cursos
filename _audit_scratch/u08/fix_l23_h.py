import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"23_Condiciones')
i1 = data.find('"24_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

# PLANTILLA: exam_questions[0].mark_scheme[1] — add lesson-specific detail
old = "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"
new = "Sin justificación, 0 puntos aunque la calificación V/F sea correcta; en (b) se exige distinguir explícitamente SN1 de SN2 por el sustrato, y en (d) distinguir oxidación controlada de combustión, no solo repetir la definición"
rep(old, new, 1, "PLANTILLA mark_scheme[1]")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE H")
