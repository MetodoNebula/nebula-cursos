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
        idx = seg.find(old[:40])
        print("found-near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

# F4: theory_blocks[2].body step 2 (drop PCC, fix nucleophile/addition confusion)
old = "2) Mira el reactivo. ¿Es un nucleófilo (OH-, CN-)? Apunta a sustitución o adición. ¿Es un oxidante reconocible (KMnO4, Cr2O7²⁻, PCC)? Apunta a oxidación. ¿Es un ácido junto con un alcohol? Apunta a esterificación."
new = "2) Mira el reactivo. ¿Es un nucleófilo (OH-, CN-, NH3) y el sustrato tiene un grupo saliente? Apunta a sustitución. ¿Es un electrófilo o una molécula que se adiciona (H2, X2, HX, H2O/H+) y hay un enlace C=C o C≡C? Apunta a adición. ¿Es una base fuerte en disolvente alcohólico y caliente? Apunta a eliminación. ¿Es un oxidante reconocible (KMnO4, Cr2O7²⁻)? Apunta a oxidación. ¿Es un ácido junto con un alcohol? Apunta a esterificación."
rep(old, new, 1, "F4 tb2 step2")

# F4b: step 1 — add alkanes/aromatics/combustion candidates
old = "1) Mira el sustrato. ¿Tiene un enlace doble o triple? (candidato a adición, o a polimerización si es un monómero). ¿Tiene un grupo saliente, como un halógeno? (candidato a sustitución o a eliminación). ¿Tiene un grupo -OH o -COOH? (candidato a oxidación, a esterificación, o a eliminación si es un alcohol)."
new = "1) Mira el sustrato. ¿Tiene un enlace doble o triple? (candidato a adición, o a polimerización si es un monómero). ¿Tiene un grupo saliente, como un halógeno? (candidato a sustitución o a eliminación). ¿Tiene un grupo -OH o -COOH? (candidato a oxidación, a esterificación, o a eliminación si es un alcohol). ¿Es un alcano sin grupo funcional, o un anillo aromático? (candidato a sustitución radicalaria con luz, o a sustitución electrófila aromática con un catalizador, o a combustión si el reactivo es O2 en exceso)."
rep(old, new, 1, "F4b tb2 step1")

# F5: summary.formulas[1] reversible arrow
old = '"R\\\\text{-COOH}+HO\\\\text{-}R\\u0027 \\\\rightarrow R\\\\text{-COO-}R\\u0027+H_2O"'
c = seg.count(old)
print("probe F5 count", c)

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE C partial")
