import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
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

# F17: exam_questions[0].mark_scheme[2] -> student-directed
old = "En (b), se exige explícitamente mencionar que el oxígeno del éster no lleva H unido"
new = "Para obtener la puntuación completa debes justificar cada apartado; en (b) indica expresamente que ningún H del éster está unido a un oxígeno"
rep(old, new, 1, "F17 exam_questions0 mark_scheme[2]")

# PLANTILLA: exam_questions[0].mark_scheme[1]
old2 = "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"
# there may be 2 occurrences (exam_questions[0] and exam_questions[1] already rewritten away) check count
c2 = seg.count(old2)
print("probe plantilla count", c2)

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE F partial")
