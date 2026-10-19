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

# F2a: misconceptions[2].correct_model
old = "La esterificación es un caso de condensación (dos moléculas se unen liberando agua); la polimerización por adición reutiliza exactamente el mecanismo de adición, una y otra vez, sobre miles de monómeros con doble enlace."
new = "La esterificación es un caso de condensación (dos moléculas se unen liberando agua) y, mecanísticamente, también una sustitución en el acilo. La polimerización por adición comparte con la adición la apertura del enlace π del C=C, pero transcurre por un mecanismo en cadena (normalmente radicalario, con un iniciador) en el que cada monómero se une sucesivamente al extremo de la cadena en crecimiento, no por la simple repetición de una adición puntual."
rep(old, new, 1, "F2a misconceptions[2]")

# F2b: theory_blocks[4].body
old = "cualquier reacción orgánica sencilla que aparezca en un examen debería poder situarse en una (o, a veces, en más de una) de estas seis filas."
# (sanity check, not used)
old2 = "así se ve de un vistazo tanto lo que los distingue (qué cambia en el sustrato) como lo que los conecta (la esterificación es un caso de condensación; la polimerización por adición reutiliza el mecanismo de adición muchas veces seguidas)."
new2 = "así se ve de un vistazo tanto lo que los distingue (qué cambia en el sustrato) como lo que los conecta (la esterificación es un caso de condensación; la polimerización por adición comparte con la adición la apertura del enlace π del C=C, pero avanza por un mecanismo en cadena radicalario, no por la simple repetición de una adición puntual)."
rep(old2, new2, 1, "F2b theory_blocks[4].body")

# F2c: summary.key_points[4]
old = "\"Conexiones internas: la esterificación es un caso de condensación; la polimerización por adición reutiliza el mecanismo de adición muchas veces; ninguna de las dos es un mecanismo aparte.\""
new = "\"Conexiones internas: la esterificación es un caso de condensación (y, mecanísticamente, también una sustitución en el acilo); la polimerización por adición comparte con la adición la apertura del C=C, pero avanza por un mecanismo en cadena radicalario distinto.\""
rep(old, new, 1, "F2c summary.key_points[4]")

# F2d: worked_examples[3].interpretation
old = "Los tres apartados parten del mismo doble enlace y usan el mismo mecanismo de fondo —la adición, pero con un reactivo distinto: una molécula polar pequeña (a), una molécula diatómica simétrica (b), o miles de copias del propio monómero (c)."
new = "Los tres apartados parten del mismo doble enlace, pero (a) y (b) son adiciones puntuales de una sola molécula de reactivo (polar pequeña en (a), diatómica simétrica en (b)), mientras que (c) es una polimerización: comparte con la adición la apertura del enlace π, pero avanza por un mecanismo en cadena radicalario, no por una adición puntual repetida."
rep(old, new, 1, "F2d worked_examples[3].interpretation")

# F3: theory_blocks[3].body Markovnikov/Saytzeff non-sequitur
old = "Esta competencia es la razón por la que Markovnikov y Saytzeff comparten protagonista: en los dos casos, el carbono «más sustituido» (con menos H) decide el producto mayoritario, solo que en la adición ese carbono gana el átomo más electronegativo y en la eliminación pierde un hidrógeno. Tener clara esta simetría evita confundir una regla con la otra al cambiar de tipo de reacción."
new = "Esta competencia sustitución/eliminación es un fenómeno distinto de por qué Markovnikov y Saytzeff comparten protagonista. Markovnikov y Saytzeff señalan ambos al carbono más sustituido (con menos H) por razones de estabilidad: en la adición se forma preferentemente el carbocatión intermedio más estable, que es el más sustituido; en la eliminación se forma preferentemente el alqueno más estable, que también es el más sustituido. Tener clara esta simetría evita confundir una regla con la otra al cambiar de tipo de reacción."
rep(old, new, 1, "F3 theory_blocks[3].body")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE B")
