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

# F9: common_mistakes[2].why — PLANTILLA generic
old9 = "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema."
new9 = "Se comprueba que el monómero tiene el grupo funcional adecuado (-COOH), pero no cuántos grupos reactivos tiene: con uno solo, la cadena no puede crecer por los dos lados."
rep(old9, new9, 1, "F9 common_mistakes2")

# F10: prerequisites[2].statement — wrong lesson reference
old10 = "recordar cómo funciona la polimerización por adición vista en la lección anterior."
new10 = "recordar cómo funciona la polimerización por adición vista en la lección de polimerización por adición."
rep(old10, new10, 1, "F10 prerequisites2")

# F12: exam_questions[0].mark_scheme[2] — student-directed
old12 = "En (d) se exige mencionar explícitamente la excepción (apertura de anillo), no basta con responder 'falsa' sin más"
new12 = "Para la puntuación completa debes justificar cada apartado; en (d) menciona el nailon-6 (apertura de anillo) y no te limites a responder 'falsa' sin más"
rep(old12, new12, 1, "F12 exam_questions0 mark_scheme")

# F14b: diagnostic_items[0].question — artículo indefinido impropio
old14 = "En la esterificación de un ácido acético (M=60,05 g/mol) con un etanol (M=46,07 g/mol)"
new14 = "En la esterificación del ácido acético (M=60,05 g/mol) con etanol (M=46,07 g/mol)"
rep(old14, new14, 1, "F14b diagnostic_items0")

# F3d: misconceptions[1].correct_model — nuance single bifunctional monomer
old3 = "Para que la cadena pueda seguir creciendo por los dos extremos hace falta un diácido (dos -COOH) combinado con un diol o una diamina (dos -OH o dos -NH2), cada uno con dos puntos de enganche."
new3 = "Para que la cadena pueda seguir creciendo por los dos extremos hace falta que el conjunto de monómeros aporte dos puntos de enganche en cada paso: normalmente un diácido (dos -COOH) combinado con un diol o una diamina (dos -OH o dos -NH2), aunque también basta un único monómero con dos grupos reactivos distintos en la misma molécula (un hidroxiácido, HO-R-COOH, como en el PLA, o un aminoácido, H2N-CHR-COOH, como en las proteínas)."
rep(old3, new3, 1, "F3d misconceptions1")

# F3e: guided_exercises[1].answer(c) y full_solution(c) — matización
old3e_a = "(c) Haría falta un diácido, con dos -COOH."
new3e_a = "(c) Haría falta un diácido, con dos -COOH (o, más en general, cualquier monómero con dos grupos reactivos en sus dos extremos)."
rep(old3e_a, new3e_a, 1, "F3e answer(c)")

old3e_fs = "como ocurre en el ácido tereftálico (HOOC-C6H4-COOH) usado en el PET. Con un diácido y un diol, cada monómero tiene siempre un extremo libre disponible para seguir reaccionando, y la cadena puede crecer sin límite teórico por los dos lados."
new3e_fs = "como ocurre en el ácido tereftálico (HOOC-C6H4-COOH) usado en el PET. Con un diácido y un diol, cada monómero tiene siempre un extremo libre disponible para seguir reaccionando, y la cadena puede crecer sin límite teórico por los dos lados. (En otros casos, como el PLA o las proteínas, ese mismo papel lo cumple un único monómero que ya tiene de por sí dos grupos reactivos distintos, por ejemplo un hidroxiácido.)"
rep(old3e_fs, new3e_fs, 1, "F3e full_solution(c)")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE I")
