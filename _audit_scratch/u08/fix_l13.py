import json, sys, io

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with io.open(path, 'r', encoding='utf-8') as f:
    data = f.read()

edits = []

edits.append((
"Por eso el giro que produce un carbono se cancela exactamente con el que produce el otro: el ácido mesotartárico es **ópticamente inactivo**, aunque tenga carbonos quirales, y es superponible con su propia imagen especular (no es un enantiómero de nada: es su propio 'espejo').",
"Por tener ese plano de simetría interno, la molécula es superponible con su propia imagen especular: es **aquiral**, aunque tenga dos carbonos marcados como C*, y por eso el ácido mesotartárico es **ópticamente inactivo** (no es un enantiómero de nada: es su propio 'espejo'). De forma intuitiva —aunque no es la causa real, solo una imagen que ayuda a visualizarlo— puede pensarse que «el giro que produciría un carbono se cancela con el que produciría el otro»; pero lo que de verdad determina la inactividad óptica es la aquiralidad de la molécula completa, no una suma de contribuciones independientes de cada centro.",
"L13-F2-theory4"
))

edits.append((
"Este es el motivo por el que el ácido tartárico no tiene cuatro estereoisómeros (como cabría esperar de 'dos carbonos quirales'), sino tres: L, D y meso.",
"Este es el motivo por el que el ácido tartárico no tiene cuatro estereoisómeros (como cabría esperar de 'dos carbonos quirales'), sino tres: L, D y meso.\n\nDe forma general, con $n$ carbonos quirales hay como máximo $2^n$ estereoisómeros distintos; el número real puede ser menor si, como aquí, aparece alguna simetría interna que da lugar a una forma meso. Conviene recordar también que los isómeros cis/trans de la lección anterior son, por definición, un caso particular de diastereómeros: no son imágenes especulares entre sí, y por eso, igual que cualquier otro par de diastereómeros, sí pueden tener propiedades físicas distintas (puntos de fusión, polaridad, etc.).",
"L13-F4-theory4-append"
))

edits.append((
"Por esto a esta propiedad se la llama **actividad óptica**, y a los dos enantiómeros se los suele distinguir con los símbolos + (o d, dextrógiro) y - (o l, levógiro) según hacia qué lado giran la luz. (Existen también las nomenclaturas D/L y R/S para nombrar sin ambigüedad cada enantiómero, pero esta lección no exige aplicarlas en detalle.)",
"Por esto a esta propiedad se la llama **actividad óptica**, y a los dos enantiómeros se los suele distinguir con los símbolos + (o d, dextrógiro) y - (o l, levógiro) según hacia qué lado giran la luz. (Existen también las nomenclaturas D/L y R/S para nombrar sin ambigüedad cada enantiómero, pero esta lección no exige aplicarlas en detalle.)\n\nQuímicamente, los dos enantiómeros reaccionan exactamente igual frente a reactivos no quirales (los reactivos 'ordinarios' de laboratorio). Pero su comportamiento puede ser muy distinto frente a otras moléculas quirales, como las enzimas o los receptores biológicos, que sí distinguen entre una forma y su imagen especular: por eso dos enantiómeros de un mismo fármaco pueden tener efectos muy diferentes en el organismo. El caso más conocido es el de la talidomida, en el que un enantiómero era el sedante buscado y el otro resultó ser teratógeno.",
"L13-F3-theory2-append"
))

edits.append((
"Esa combinación con plano de simetría interno es el ácido mesotartárico: el giro óptico que produciría el C2 se cancela exactamente con el que produciría el C3, dentro de la misma molécula. Las otras dos combinaciones restantes sí son un par de enantiómeros genuinos (D y L), ópticamente activos.",
"Esa combinación con plano de simetría interno es el ácido mesotartárico: por tener ese plano, la molécula es superponible con su propia imagen especular (es aquiral), así que resulta ópticamente inactiva aunque tenga dos carbonos marcados como C* (de forma intuitiva, puede verse como que el giro que produciría el C2 se cancela con el que produciría el C3, pero la causa real es la aquiralidad de la molécula completa). Las otras dos combinaciones restantes sí son un par de enantiómeros genuinos (D y L), ópticamente activos.",
"L13-F2-worked2"
))

edits.append((
"y es ópticamente inactiva, porque el giro que produciría un carbono se cancela con el que produciría el otro.",
"y por tener ese plano de simetría es aquiral, y por eso es ópticamente inactiva (de forma intuitiva, el giro que produciría un carbono se cancela con el que produciría el otro, pero la causa real es la aquiralidad de toda la molécula, no una suma de contribuciones independientes).",
"L13-F2-examq1"
))

edits.append((
"cada molécula de ácido mesotartárico tiene, por sí misma, un plano de simetría interno que hace que el giro óptico producido por uno de sus carbonos quirales se cancele exactamente con el producido por el otro, dentro de esa misma molécula. La inactividad óptica es, aquí, una propiedad de cada molécula individual.",
"cada molécula de ácido mesotartárico tiene, por sí misma, un plano de simetría interno que la hace superponible con su propia imagen especular: es una molécula aquiral, y por eso cada una de ellas es, individualmente, ópticamente inactiva (de forma intuitiva, puede pensarse que el giro producido por uno de sus carbonos quirales se cancela con el producido por el otro, pero la causa real es la aquiralidad de la molécula completa, no una suma de contribuciones independientes). La inactividad óptica es, aquí, una propiedad de cada molécula individual.",
"L13-F2-challenge0"
))

edits.append((
'Estereoisómero con carbonos quirales (C*) pero ópticamente inactivo, por tener un plano de simetría interno que cancela el giro que produciría cada centro quiral por separado; es superponible con su propia imagen especular.',
'Estereoisómero con carbonos quirales (C*) pero ópticamente inactivo, porque un plano de simetría interno lo hace aquiral: es superponible con su propia imagen especular (de forma intuitiva, el giro que produciría cada centro se cancela con el del otro, pero la causa real es la aquiralidad de toda la molécula, no una suma de contribuciones).',
"L13-F2-flashcard6"
))

edits.append((
"esa forma meso es ópticamente inactiva, pese a tener dos carbonos marcados con C*, porque el giro que produce un centro se cancela internamente con el que produce el otro.",
"esa forma meso es aquiral —superponible con su propia imagen especular— y por eso es ópticamente inactiva, pese a tener dos carbonos marcados con C* (de forma intuitiva, el giro que produce un centro se cancela con el que produce el otro, pero la causa real es la aquiralidad de toda la molécula, no una suma de contribuciones independientes).",
"L13-F2-misc1"
))

edits.append((
'Forma meso (ácido tartárico): carbonos quirales presentes, pero un plano de simetría interno cancela el giro neto; ópticamente inactiva, y reduce de 4 a 3 el número de estereoisómeros distintos.',
'Forma meso (ácido tartárico): carbonos quirales presentes, pero un plano de simetría interno la hace aquiral (superponible con su imagen especular); por eso es ópticamente inactiva, y reduce de 4 a 3 el número de estereoisómeros distintos.',
"L13-F2-summary4"
))

edits.append((
'        "mistake": "Marcar como quiral un carbono con un sustituyente \'llamativo\' (halógeno, -OH) sin comprobar los otros tres.",\n        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",',
'        "mistake": "Marcar como quiral un carbono con un sustituyente \'llamativo\' (halógeno, -OH) sin comprobar los otros tres.",\n        "why": "Se asocia la quiralidad a la presencia de un heteroátomo llamativo en vez de a la comparación explícita de los cuatro sustituyentes.",',
"L13-F6-cm0"
))

edits.append((
'        "mistake": "Dar por supuesto que dos carbonos quirales siempre producen cuatro estereoisómeros.",\n        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",',
'        "mistake": "Dar por supuesto que dos carbonos quirales siempre producen cuatro estereoisómeros.",\n        "why": "Se aplica la regla $2^n$ de forma mecánica, sin comprobar si existe una simetría interna que pueda dar lugar a una forma meso.",',
"L13-F6-cm2"
))

edits.append((
"Cuidado: este carbono lleva DOS grupos -CH₃; comprueba si alguno de los cuatro sustituyentes se repite antes de declararlo quiral.",
"Cuidado: este carbono lleva DOS grupos -CH$_3$; comprueba si alguno de los cuatro sustituyentes se repite antes de declararlo quiral.",
"L13-F7-hint"
))

edits.append((
'¿Por qué la geometría tetraédrica del carbono sp3 es necesaria para la quiralidad?',
'¿Por qué la geometría tetraédrica del carbono sp$^3$ es necesaria para la quiralidad?',
"L13-F7-flashcard7"
))

edits.append((
"No es quiral (de hecho, ni siquiera tiene cuatro sustituyentes distintos tomados de dos en dos: le faltan hasta dos tipos distintos).",
"No es quiral: solo tiene dos tipos de sustituyente (-CH$_3$ y -H), cada uno repetido dos veces.",
"L13-F9-examq0"
))

edits.append((
"El carbono central está unido a: -OH, -CH$_3$ (el que cuelga directamente), -CH$_2$-CH$_3$ (el resto de la cadena) y un segundo -CH$_3$, porque el enunciado indica que ese carbono lleva un sustituyente -CH$_3$ además de continuar la cadena principal. Al tener dos grupos -CH$_3$ idénticos entre sus cuatro sustituyentes, la condición de 'cuatro sustituyentes distintos' falla: no es un carbono quiral.",
"El C2 (el carbono central) está unido a: -OH, -CH$_3$ (el C1), -CH$_3$ (la ramificación indicada en el nombre) y -CH$_2$-CH$_3$ (el resto de la cadena, C3-C4). Hay dos grupos -CH$_3$ idénticos entre sus cuatro sustituyentes, así que la condición de 'cuatro sustituyentes distintos' falla: no es un carbono quiral.",
"L13-F10-exercises0"
))

edits.append((
'Procedimiento: El carbono que lleva el -OH es el candidato; sigue la cadena completa hacia cada lado, no solo el átomo vecino más próximo. Conclusión: (a) -CH$_3$, -OH, -H y -CH$_2$-CH$_3$ (etilo). (b) Los cuatro son distintos: es quiral.',
'El carbono que lleva el -OH (C2) está unido a cuatro grupos: -OH, -H, -CH$_3$ (C1) y -CH$_2$-CH$_3$ (C3-C4, etilo). Comparando las seis parejas posibles entre estos cuatro sustituyentes, ninguna coincide: -OH frente a -H, -OH frente a -CH$_3$, -OH frente a -CH$_2$-CH$_3$, -H frente a -CH$_3$, -H frente a -CH$_2$-CH$_3$, y -CH$_3$ frente a -CH$_2$-CH$_3$ (metilo y etilo son grupos distintos, aunque ambos sean hidrocarbonados). Como los cuatro sustituyentes son distintos entre sí, el carbono es quiral.',
"L13-F5-guided0"
))

edits.append((
"Procedimiento: Piensa en qué pasaría si reflejaras la molécula entera en un espejo e intentaras encontrar una molécula distinta. Conclusión: Porque su plano de simetría interno hace que la imagen especular de la molécula se pueda superponer con la molécula original: reflejarla no produce nada nuevo.",
"Al reflejar la molécula completa del ácido mesotartárico en un espejo, se obtiene, a primera vista, una disposición que parece distinta. Pero gracias al plano de simetría interno de la molécula, basta girar esa imagen especular 180 grados para hacerla coincidir, átomo por átomo, con la molécula original. Es decir, la imagen especular del mesotartárico no es una molécula nueva: es la misma molécula, vista desde otra orientación. Por eso se dice que el ácido mesotartárico 'es su propia imagen especular' y no tiene un enantiómero genuino distinto de sí mismo.",
"L13-F5-guided1"
))

ok = True
for old, new, label in edits:
    c = data.count(old)
    if c != 1:
        print(f"FAIL [{label}] count={c}")
        ok = False
    else:
        data = data.replace(old, new, 1)
        print(f"OK [{label}]")

if not ok:
    print("ABORTED - no changes written due to failures above")
    sys.exit(1)

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data)
print("ALL EDITS APPLIED")
