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

NL = chr(92)+'n'

# F3: tb4 — extend with "Otros polímeros de condensación" block
old = "Esto no cambia el razonamiento de esta lección, pero sí avisa de que el nombre del grupo funcional resultante (éster, amida) no basta por sí solo para decidir el mecanismo: hay que mirar también cuántos monómeros intervienen y si hay un subproducto pequeño liberado en cada unión."
new = old + NL + NL + "No siempre hacen falta dos monómeros distintos, ni el subproducto tiene que ser agua. Un hidroxiácido, HO-R-COOH, tiene en una sola molécula los dos grupos reactivos (un -OH y un -COOH): puede condensar consigo mismo una y otra vez, liberando agua en cada unión, para dar un poliéster como el PLA (ácido poliláctico). Igual ocurre con los aminoácidos, H2N-CHR-COOH: se condensan entre sí formando el enlace peptídico (-CO-NH-), el mismo tipo de enlace amida, para dar las proteínas. Otros subproductos distintos del agua también son posibles: la condensación de un diácido con un cloruro de ácido libera HCl, y la de un diéster con un diol puede liberar metanol. La baquelita, por su parte, se obtiene condensando fenol con metanal (formaldehído): al tener cada monómero más de dos puntos reactivos, el resultado no es una cadena lineal sino una red tridimensional entrecruzada."
rep(old, new, 1, "F3 tb4 otros polímeros")

# F3b: tb4 — nuance poliuretano right before closing, mentioning it's poliadición not condensación
old2 = "El nailon-6, por ejemplo, también es una poliamida, pero se obtiene por apertura de un anillo (un monómero cíclico, la caprolactama, se abre y se encadena consigo mismo) y no por condensación de dos monómeros distintos con liberación de agua."
new2 = "El nailon-6, por ejemplo, también es una poliamida, pero se obtiene por apertura de un anillo (un monómero cíclico, la caprolactama, se abre y se encadena consigo mismo) y no por condensación de dos monómeros distintos con liberación de agua. El poliuretano es el caso contrario: sus monómeros (un diisocianato y un diol) sí son dos y sí son bifuncionales, pero no se libera ningún subproducto pequeño, por lo que en sentido estricto no es un polímero de condensación, sino de poliadición (crecimiento por etapas sin pérdida de masa); se le suele agrupar junto a los poliésteres y poliamidas solo por compartir con ellos la bifuncionalidad de los monómeros."
rep(old2, new2, 1, "F3c tb4 poliuretano")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE E")
