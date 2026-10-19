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

NL = chr(92) + 'n'

# F14a: theory_blocks[0].body — state the three questions explicitly and point to where each is developed
old = "No hace falta memorizar una tabla: basta con aprender a hacerse tres preguntas ante cualquier grupo funcional nuevo, y se desarrollan en los bloques siguientes."
new = "No hace falta memorizar una tabla: basta con aprender a hacerse tres preguntas ante cualquier grupo funcional nuevo. (1) ¿Hay algún H unido directamente a O o N? (decide si puede DONAR enlace de hidrógeno; bloque de ebullición). (2) ¿Cuántos pares de electrones libres hay disponibles para ACEPTAR enlace de hidrógeno del agua, aunque no pueda donar? (decide la solubilidad incluso en éteres, aldehídos o cetonas; bloque de solubilidad). (3) ¿Cuántos carbonos tiene la cadena apolar que acompaña al grupo funcional? (decide si la parte polar basta para compensarla; bloques de ebullición y solubilidad)."
rep(old, new, 1, "F14a theory_blocks[0]")

# F14b: theory_blocks[2].body — add donor/acceptor paragraph right after the first paragraph
old = "Disolver un compuesto orgánico en agua exige romper parte de la red de enlaces de hidrógeno que el agua forma consigo misma, y sustituirla por enlaces de hidrógeno entre el agua y el soluto. Eso solo compensa si el soluto aporta un grupo capaz de hacerlo (-OH, -COOH, -NH2...) y si la parte apolar que arrastra no es demasiado grande."
new = "Disolver un compuesto orgánico en agua exige romper parte de la red de enlaces de hidrógeno que el agua forma consigo misma, y sustituirla por enlaces de hidrógeno entre el agua y el soluto. Eso solo compensa si el soluto aporta un grupo capaz de hacerlo (-OH, -COOH, -NH2...) y si la parte apolar que arrastra no es demasiado grande." + NL + NL + "No hace falta donar: basta con poder aceptar. Un grupo como -OH o -COOH dona Y acepta; pero un éter (-O-), un aldehído o una cetona (C=O) no tienen ningún H unido a O, así que no pueden donar un enlace de hidrógeno, pero SÍ pueden aceptarlo del H del agua, a través de sus pares de electrones libres. Por eso un éter pequeño es más soluble en agua de lo que su bajo punto de ebullición (sin enlace de H entre sus propias moléculas) haría pensar: lo que importa para la solubilidad es la interacción con el agua, no la que el soluto tiene consigo mismo. El -COOH, con un donador y dos aceptores, tiene más puntos de anclaje que el -OH de un alcohol (un donador y un aceptor), lo que explica por qué un ácido carboxílico es más soluble que un alcohol de cadena comparable."
rep(old, new, 1, "F14b theory_blocks[2]")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE D")
