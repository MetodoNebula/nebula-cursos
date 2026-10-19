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

# F6: guided_exercises[0].answer + full_solution (b) adición+reducción
old1 = "(a) Oxidación-reducción. (b) Adición. (c) Esterificación. (d) Polimerización por adición."
new1 = "(a) Oxidación-reducción. (b) Adición (y también reducción). (c) Esterificación. (d) Polimerización por adición."
rep(old1, new1, 1, "F6 answer")

old2 = "(b) Doble enlace a dos enlaces simples con catalizador metálico (Ni): adición."
new2 = "(b) El C=C pasa a un enlace C-C simple y cada carbono gana un H, con catalizador metálico (Ni): es una adición (hidrogenación catalítica) que, a la vez, es una reducción."
rep(old2, new2, 1, "F6 full_solution")

# F7: theory_blocks[1].body — Sustitución row + Combustión row
old3 = "| Sustitución | Un grupo saliente es reemplazado por un grupo entrante | Medio básico acuoso y frío (sustratos 1º); disolvente polar, sin base fuerte (sustratos 3º) |"
new3 = "| Sustitución | Un grupo saliente es reemplazado por un grupo entrante (o un H es sustituido por X en alcanos/aromáticos) | Medio básico acuoso y frío (sustratos 1º); disolvente polar, sin base fuerte (sustratos 3º); alcanos + X2 con luz UV (radicalaria); benceno + HNO3/H2SO4 o X2/FeX3 (electrófila aromática) |"
rep(old3, new3, 1, "F7a sustitución row")

old4 = "| Polimerización | Muchos monómeros se encadenan en una macromolécula | Adición: doble enlace, iniciador/calor/presión. Condensación: pérdida de molécula pequeña por unión |"
new4 = old4 + "\n| Combustión | El carbono se oxida por completo hasta CO2 y el H hasta H2O | O2 en exceso y una chispa o llama; destruye por completo el esqueleto de carbono |"
rep(old4, new4, 1, "F7b combustión row")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE D")
