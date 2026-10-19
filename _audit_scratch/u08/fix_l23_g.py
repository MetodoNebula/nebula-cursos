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

# F16a: mcq[4].options[0].text — ambiguous mnemonic
old = "Markovnikov decide el producto mayoritario de una adición; Saytzeff, el de una eliminación. Ambas señalan al carbono con menos H, pero en sentidos opuestos (lo gana / lo pierde)."
new = "Markovnikov decide el producto mayoritario de una adición; Saytzeff, el de una eliminación. En la adición, ese carbono recibe el grupo electronegativo (X, OH) y el H va al carbono con más H; en la eliminación, ese mismo carbono es el que pierde un H."
rep(old, new, 1, "F16a mcq4 option A")

# F16b: flashcards[1].back
old = "Ambas señalan al carbono más sustituido (menos H): Markovnikov decide el producto mayoritario de una adición (lo gana); Saytzeff, el de una eliminación (lo pierde)."
new = "Ambas señalan al carbono más sustituido (menos H): en Markovnikov (adición), ese carbono recibe el grupo electronegativo (X, OH); en Saytzeff (eliminación), ese carbono es el que pierde un H."
rep(old, new, 1, "F16b flashcards[1]")

# F17a: mcq[3].stem — PCC out of syllabus
old = "Un alcohol primario se oxida con PCC (un oxidante suave) y se obtiene un aldehído, sin que el resto de la molécula cambie."
new = "Un alcohol primario se oxida con K2Cr2O7/H2SO4, destilando el aldehído según se forma (un oxidante suave en estas condiciones), y se obtiene un aldehído, sin que el resto de la molécula cambie."
rep(old, new, 1, "F17a mcq3 stem")

old = "No, porque el PCC no es un oxidante de verdad."
new = "No, porque el K2Cr2O7 no es un oxidante de verdad."
rep(old, new, 1, "F17a2 mcq3 optB text")

old = "El PCC sí es un oxidante (suave): la reacción descrita es, precisamente, una oxidación."
new = "El K2Cr2O7 sí es un oxidante (suave en estas condiciones): la reacción descrita es, precisamente, una oxidación."
rep(old, new, 1, "F17a3 mcq3 optB why_wrong")

old = "es una oxidación orgánica con un oxidante específico (PCC), que da un producto definido sin destruir el esqueleto de carbono;"
new = "es una oxidación orgánica con un oxidante específico (K2Cr2O7, en condiciones controladas), que da un producto definido sin destruir el esqueleto de carbono;"
rep(old, new, 1, "F17a4 mcq3 optD text")

# F17b: misconceptions[1].diagnostic_signal
old = "Llama combustión a la oxidación de un alcohol con PCC o dicromato, sin exigir O2 en exceso ni destrucción del esqueleto."
new = "Llama combustión a la oxidación de un alcohol con dicromato (K2Cr2O7), sin exigir O2 en exceso ni destrucción del esqueleto."
rep(old, new, 1, "F17b misconceptions[1]")

# F17c: flashcards[6].back
old = "Oxidación suave: oxidante específico (PCC, dicromato), producto definido, esqueleto de carbono intacto."
new = "Oxidación suave: oxidante controlado (K2Cr2O7/H2SO4 en frío o diluido), producto definido, esqueleto de carbono intacto."
rep(old, new, 1, "F17c flashcards[6]")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE G")
