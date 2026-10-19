import io, sys

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

key_start = '"17_Regla_de_SaytzeffZaitsev.json"'
key_end = '"18_Reacciones_de_sustitución.json"'
i0 = data.find(key_start)
i1 = data.find(key_end)
assert i0 != -1 and i1 != -1 and i0 < i1
seg = data[i0:i1]

NL = chr(10)
BS = chr(92) * 2

content_edits = []

# #15 theory_blocks[0].body dash fix
content_edits.append((
"—lo más habitual cuando el grupo saliente no está en un extremo de la cadena, la eliminación puede retirar el H de cualquiera de ellos, y cada elección da un alqueno distinto (isómeros de posición entre sí).",
"—lo más habitual cuando el grupo saliente no está en un extremo de la cadena—, la eliminación puede retirar el H de cualquiera de ellos, y cada elección da un alqueno distinto (isómeros de posición entre sí).",
"L17-F15"
))

# #4 theory_blocks[1].body -- add E/Z note for but-2-eno
content_edits.append((
"El but-2-eno, al ser el más sustituido, es el producto mayoritario; el but-1-eno es el minoritario.",
"El but-2-eno, al ser el más sustituido, es el producto mayoritario; el but-1-eno es el minoritario. (El but-2-eno, además, presenta isomería geométrica: se forma como mezcla de (E)-but-2-eno y (Z)-but-2-eno, predominando el (E), con los dos grupos CH3 en lados opuestos del doble enlace, por tener menor repulsión estérica entre ellos que el (Z).)",
"L17-F4"
))

# #12 theory_blocks[3].body table -- mathrm H2O and 3º>2º>1º
content_edits.append((
"Adición (HX, H2O a un alqueno)",
f"Adición (HX, ${BS}mathrm{{H_2O}}$ a un alqueno)",
"L17-F12-table1"
))
content_edits.append((
"Eliminación (HX de un haloalcano, H2O de un alcohol)",
f"Eliminación (HX de un haloalcano, ${BS}mathrm{{H_2O}}$ de un alcohol)",
"L17-F12-table2"
))
content_edits.append((
"Estabilidad de carbocationes intermedios (3º>2º>1º)",
f"Estabilidad de carbocationes intermedios (${BS}mathrm{{3^o}} > {BS}mathrm{{2^o}} > {BS}mathrm{{1^o}}$)",
"L17-F12-table3"
))

# #1 exercises[2].full_solution
content_edits.append((
"No hay ningún carbocatión involucrado en el razonamiento de Saytzeff.",
"El criterio de Saytzeff es la estabilidad de los alquenos producto (aunque en la deshidratación ácida de un alcohol sí se forma un carbocatión intermedio, la regla no se razona comparando carbocationes, sino comparando los alquenos que pueden formarse).",
"L17-F1"
))

# #2 worked_examples[2].common_mistake
content_edits.append((
"que en realidad compara la estabilidad de los alquenos producto, no de ningún carbocatión intermedio.",
"que en realidad se decide comparando la estabilidad de los alquenos producto (el carbocatión, si se forma, es el mismo para ambos caminos y no permite elegir).",
"L17-F2"
))

# #8 mcq[0].options[1].why_wrong
content_edits.append((
"que compara directamente la estabilidad de los alquenos producto, sin carbocationes intermedios.",
"Saytzeff compara la estabilidad de los alquenos producto, no la de carbocationes.",
"L17-F8"
))

# #9 misconceptions[0].correct_model
content_edits.append((
"el criterio es la estabilidad del propio alqueno producto, no de ningún intermedio catiónico)",
"el criterio es la estabilidad del propio alqueno producto)",
"L17-F9"
))

# #3 exam_questions[0] -- E/Z nuance
content_edits.append((
"El 3-bromopentano, CH3-CH2-CHBr-CH2-CH3, reacciona con KOH en medio alcohólico. (a) ¿Cuántos alquenos distintos pueden formarse? (b) Escríbelos y determina cuál es el mayoritario.",
"El 3-bromopentano, CH3-CH2-CHBr-CH2-CH3, reacciona con KOH en medio alcohólico. (a) ¿Cuántos isómeros de posición distintos pueden formarse? (b) Escribe el alqueno resultante, indicando si puede presentar isomería E/Z.",
"L17-F3-statement"
))
content_edits.append((
"(a) Un único alqueno, porque el 3-bromopentano es simétrico. (b) Pent-2-eno, CH3-CH2-CH=CH-CH3, es el único producto (y por tanto el mayoritario por defecto).",
"(a) Un único isómero de posición, pent-2-eno, por la simetría del sustrato. (b) CH3-CH2-CH=CH-CH3; sí presenta isomería E/Z, y se forma como mezcla de (E)-pent-2-eno (mayoritario, más estable) y (Z)-pent-2-eno.",
"L17-F3-answer"
))
content_edits.append((
"(a) El Br está en el C3, que tiene dos carbonos vecinos, el C2 y el C4; pero la molécula es simétrica respecto al C3 (CH3-CH2- a cada lado), así que eliminar el H del C2 o el del C4 da, por simetría, exactamente el mismo alqueno. (b) Por tanto solo hay un alqueno posible, pent-2-eno, CH3-CH2-CH=CH-CH3; no hace falta aplicar Saytzeff para elegir entre dos productos porque, en este caso simétrico, no hay elección que hacer.",
"(a) El Br está en el C3, que tiene dos carbonos vecinos, el C2 y el C4; pero la molécula es simétrica respecto al C3 (CH3-CH2- a cada lado), así que eliminar el H del C2 o el del C4 da, por simetría, exactamente el mismo isómero de posición. (b) Por tanto solo hay un isómero de posición, pent-2-eno, CH3-CH2-CH=CH-CH3; no hace falta aplicar Saytzeff para elegir entre dos isómeros de posición porque, en este caso simétrico, no hay elección que hacer. Sin embargo, el doble enlace del pent-2-eno sí tiene dos sustituyentes distintos de H en cada carbono (CH3 y H en un lado, CH2CH3 y H en el otro), así que presenta isomería geométrica: se forma como mezcla de (E)-pent-2-eno y (Z)-pent-2-eno, predominando el (E) por tener menor repulsión estérica entre los grupos alquilo que el (Z).",
"L17-F3-fullsol"
))

# #10 summary.key_points[4] + related mcq[3]/flashcards[6]/exam_notes[2]
content_edits.append((
"si el sustrato es simétrico respecto al grupo saliente (como el 3-bromopentano), no hay dos productos distintos que comparar.",
"si el sustrato es simétrico respecto al grupo saliente (como el 3-bromopentano), no hay dos isómeros de posición que comparar (aunque sí puede haber isomería E/Z dentro de ese mismo alqueno).",
"L17-F10-summary"
))
content_edits.append((
"Al ser simétrico el sustrato, los dos carbonos vecinos al grupo saliente son equivalentes, así que ambos caminos de eliminación producen el mismo alqueno y no hay mayoritario/minoritario que distinguir.",
"Al ser simétrico el sustrato, los dos carbonos vecinos al grupo saliente son equivalentes, así que ambos caminos de eliminación producen el mismo isómero de posición y no hay mayoritario/minoritario que distinguir entre isómeros de posición (el alqueno resultante sí puede presentar isomería E/Z, pero esa es una cuestión distinta).",
"L17-F10-mcq3"
))
content_edits.append((
"Cuando es simétrico respecto al carbono del grupo saliente (p. ej. 3-bromopentano): ambos carbonos vecinos son equivalentes y dan el mismo alqueno.",
"Cuando es simétrico respecto al carbono del grupo saliente (p. ej. 3-bromopentano): ambos carbonos vecinos son equivalentes y dan el mismo isómero de posición (aunque ese alqueno sí puede presentar isomería E/Z, con el E como mayoritario).",
"L17-F10-flashcard6"
))
content_edits.append((
"Conviene recordar también el caso 'trampa' en que el sustrato es simétrico respecto al grupo saliente: entonces no hay mayoritario/minoritario que elegir, aunque el enunciado dé a entender que sí.",
"Conviene recordar también el caso 'trampa' en que el sustrato es simétrico respecto al grupo saliente: entonces no hay dos isómeros de posición entre los que elegir, aunque el enunciado dé a entender que sí (el alqueno resultante sí puede presentar isomería E/Z, una cuestión distinta).",
"L17-F10-examnotes"
))

# #5, #6 common_mistakes why fixes
content_edits.append((
'        "mistake": "Confundir Saytzeff con Markovnikov, aplicando el razonamiento de carbocationes a un producto de eliminación.",\n        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",',
'        "mistake": "Confundir Saytzeff con Markovnikov, aplicando el razonamiento de carbocationes a un producto de eliminación.",\n        "why": "Ambas reglas premian lo \'más sustituido\' y comparten vocabulario, por lo que se funden fácilmente en una sola.",',
"L17-F5"
))
content_edits.append((
'        "mistake": "Decir que el alqueno minoritario de una eliminación \'no se forma\'.",\n        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",',
'        "mistake": "Decir que el alqueno minoritario de una eliminación \'no se forma\'.",\n        "why": "Se interpreta \'mayoritario\' como \'único\', leyendo la regla como absoluta en vez de como una predicción de proporciones.",',
"L17-F6"
))

ok = True
for old, new, label in content_edits:
    c = seg.count(old)
    if c != 1:
        print(f"FAIL [{label}] count={c}")
        ok = False
    else:
        seg = seg.replace(old, new, 1)
        print(f"OK [{label}]")

if not ok:
    print("ABORTED at content edits")
    sys.exit(1)

print("CONTENT EDITS DONE -- proceeding to challenge_questions replacement")

data2 = data[:i0] + seg + data[i1:]
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data2)
print("STAGE 1 WRITTEN")
