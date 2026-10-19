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

# F5: exercises[2] poliuretano — statement opener, hints, answer, full_solution conclusion
old_s = "El poliuretano se obtiene por condensación de un poliisocianato"
new_s = "El poliuretano se obtiene a partir de un poliisocianato"
rep(old_s, new_s, 1, "F5a statement opener")

old_h = "Revisa la definición general de condensación: ¿exige específicamente que se libere agua, o solo que se formen dos productos distintos en cada unión?"
new_h = "Revisa la definición general de condensación: ¿exige liberar una molécula pequeña en cada unión, o solo que los monómeros sean bifuncionales?"
rep(old_h, new_h, 1, "F5b hint")

old_a = "Es un caso límite: sus monómeros son bifuncionales, pero no libera ningún subproducto pequeño, por lo que no encaja del todo en la definición estricta, aunque se suele clasificar junto a poliésteres y poliamidas por compartir la bifuncionalidad."
new_a = "En sentido estricto, no: no se libera ninguna molécula pequeña en cada unión, así que no cumple la definición de condensación. Se clasifica como polímero de poliadición (o de crecimiento por etapas), aunque a menudo se agrupa junto a los poliésteres y poliamidas por compartir la bifuncionalidad de sus monómeros."
rep(old_a, new_a, 1, "F5c answer")

old_fs = "Por eso algunos lo tratan como un caso intermedio entre adición y condensación clásicas."
new_fs = "En sentido estricto, por tanto, no es un polímero de condensación: no se libera ninguna molécula pequeña. Se clasifica como polímero de poliadición (de crecimiento por etapas), y suele agruparse junto a los poliésteres y poliamidas por compartir con ellos la bifuncionalidad de los monómeros, aunque su mecanismo de unión sea distinto."
rep(old_fs, new_fs, 1, "F5d full_solution")

# F7: mcq[4].options[3].why_wrong
old7 = "El número de enlaces no es el número de parejas de monómeros iguales entre sí"
new7 = "El número de enlaces no es el número de parejas ácido-diol (3), sino el de huecos entre monómeros consecutivos de la cadena"
rep(old7, new7, 1, "F7 mcq4")

# F8: worked_examples[0] — replace fictitious monoacid data with a real example
old8s = "Un ácido monocarboxílico de masa M=116,07 g/mol reacciona con un monoalcohol de masa M=74,12 g/mol en una esterificación sencilla (un único enlace). Calcula la masa molecular del éster obtenido."
new8s = "El ácido hexanoico (un ácido monocarboxílico, M=116,16 g/mol) reacciona con el butan-1-ol (M=74,12 g/mol) en una esterificación sencilla (un único enlace). Calcula la masa molecular del éster obtenido."
rep(old8s, new8s, 1, "F8a statement")

old8k = '"M(ácido)=116,07 g/mol",'
new8k = '"M(ácido hexanoico)=116,16 g/mol",'
rep(old8k, new8k, 1, "F8b knowns")

old8sol = "M(éster) = 116,07+74,12-18,015 = 172,18 g/mol."
new8sol = "M(éster) = 116,16+74,12-18,015 = 172,27 g/mol."
rep(old8sol, new8sol, 1, "F8c solution")

old8int = "Si se hubiera sumado directamente 116,07+74,12=190,19 g/mol sin restar el agua, el resultado sería 18 g/mol demasiado alto: exactamente el error que se comete al tratar una condensación como si fuera una adición."
new8int = "Si se hubiera sumado directamente 116,16+74,12=190,28 g/mol sin restar el agua, el resultado sería 18 g/mol demasiado alto: exactamente el error que se comete al tratar una condensación como si fuera una adición."
rep(old8int, new8int, 1, "F8d interpretation")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE H")
