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

# F10: exam_questions[0].statement (d) — unify dicromato terminology
old = "Quemar un alcohol y oxidarlo suavemente con K2Cr2O7 dan, en esencia, el mismo tipo de productos"
new = "Quemar un alcohol y oxidarlo con K2Cr2O7 (una oxidación controlada que conserva el esqueleto de carbono) dan, en esencia, el mismo tipo de productos"
rep(old, new, 1, "F10 exam_questions statement")

# F10b: exam_questions[0].full_solution (d) — same unification
old = "mientras que la oxidación suave con dicromato conserva el esqueleto y da un producto orgánico definido."
new = "mientras que la oxidación controlada con dicromato conserva el esqueleto y da un producto orgánico definido."
rep(old, new, 1, "F10b full_solution")

# F11a: challenge_questions[0].full_solution — mechanism of acid-catalyzed hydration
old = "en medio ácido fuerte que activa la molécula de agua."
new = "en medio ácido fuerte: el H+ protona el doble enlace del eteno formando un carbocatión, y el agua (nucleófilo débil) ataca después a ese carbocatión."
rep(old, new, 1, "F11a challenge_questions")

# F11b: exercises[0].full_solution — same mechanism error
old = "favorecida por el medio ácido fuerte, que activa la molécula de agua."
new = "favorecida por el medio ácido fuerte: el H+ protona el doble enlace, formando un carbocatión, al que ataca después el agua."
rep(old, new, 1, "F11b exercises[0]")

# F12: exam_questions[0].full_solution (a) — false generalization "toda condensación"
old = "la esterificación, como toda condensación con catalizador ácido, es reversible (hidrólisis), alcanzando un equilibrio."
new = "la esterificación es reversible; su inversa es la hidrólisis ácida del éster, y se alcanza un equilibrio."
rep(old, new, 1, "F12 exam_questions full_solution(a)")

# F18: exam_questions[0].statement tuteo
old = "Razone si las siguientes afirmaciones son verdaderas o falsas."
new = "Razona si las siguientes afirmaciones son verdaderas o falsas."
rep(old, new, 1, "F18 tuteo")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE E")
