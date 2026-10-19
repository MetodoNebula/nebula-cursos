import io

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

old = (
    '"statement": "El 2-bromobutano, eliminado con KOH, da but-2-eno como mayoritario (Saytzeff). Ese mismo but-2-eno, si se hidrogenara con H2/Ni, daría butano. Y el but-1-eno (minoritario de la eliminación), hidrogenado igual, también daría butano. Explica por qué este hecho (que los dos alquenos posibles lleven al mismo alcano por hidrogenación) no contradice que uno de los dos sea claramente mayoritario en la eliminación.",\n'
    '        "hints": [\n'
    '          "Separa mentalmente el paso de eliminación (donde se decide qué alqueno se forma) del paso posterior de hidrogenación (que ocurre después, sobre un alqueno ya elegido).",\n'
    '          "Que dos caminos converjan en un mismo punto final no dice nada sobre cuál de ellos es más probable al principio."\n'
    '        ],\n'
    '        "answer": "No hay contradicción: Saytzeff actúa en el paso de la eliminación (decide qué alqueno se forma a partir del haloalcano), mientras que la hidrogenación es un paso completamente posterior e independiente; que ambos alquenos converjan en el mismo alcano no cambia en nada cuál de los dos se formó en mayor proporción durante la eliminación.",\n'
    '        "full_solution": "La proporción mayoritario/minoritario se decide en el momento de la eliminación, por la estabilidad relativa de los dos alquenos posibles como productos de esa reacción concreta. La hidrogenación posterior es una reacción distinta, que ocurre después y sobre un alqueno que ya ha sido «elegido»: el hecho de que los dos alquenos, llevados por caminos separados, acaben dando el mismo alcano no influye para nada en qué proporción de cada uno se formó originalmente. Es análogo a que dos rutas distintas de carretera lleven a la misma ciudad: eso no dice nada sobre cuál de las dos rutas se usa con más frecuencia para salir de casa.",\n'
    '        "common_errors": [\n'
    '          "Concluir, erróneamente, que si los dos alquenos llevan al mismo producto final entonces «da igual» cuál se forme en la eliminación, perdiendo de vista que la pregunta de Saytzeff se refiere únicamente al paso de la eliminación."\n'
    '        ],'
)

new = (
    '"statement": "El 3-metilbutan-2-ol, CH3-CH(OH)-CH(CH3)-CH3, se calienta con H2SO4. (a) Identifica los alquenos posibles y determina cuál es el mayoritario según Saytzeff. (b) El alqueno mayoritario, ¿puede presentar isomería E/Z? Razónalo comparando los sustituyentes de cada carbono del doble enlace, sin asumir automáticamente que \'más sustituido\' implica E/Z.",\n'
    '        "hints": [\n'
    '          "El OH está en el C2; sus vecinos con H son el C1 (un CH3) y el C3 (que lleva, además, un grupo metilo ramificado).",\n'
    '          "Para que haya isomería E/Z, cada uno de los DOS carbonos del doble enlace debe tener dos sustituyentes distintos entre sí; comprueba esto carbono por carbono, no solo el grado de sustitución total."\n'
    '        ],\n'
    '        "answer": "(a) Mayoritario: 2-metilbut-2-eno, CH3-CH=C(CH3)-CH3 (trisustituido). Minoritario: 3-metilbut-1-eno, CH2=CH-CH(CH3)-CH3 (monosustituido). (b) No: aunque es trisustituido, uno de sus dos carbonos del doble enlace lleva dos grupos CH3 idénticos entre sí, así que no cumple la condición de \'dos sustituyentes distintos en cada carbono\' y no presenta isomería E/Z.",\n'
    '        "full_solution": "(a) El C2 (con el OH) tiene dos carbonos vecinos con H: el C1 (grupo CH3, con 3 H) y el C3 (con 1 H, además de llevar su propio grupo metilo ramificado y el C4). Eliminando el H del C1: doble enlace entre C1-C2, dando CH2=CH-CH(CH3)-CH3 (3-metilbut-1-eno); alrededor de este doble enlace solo hay un grupo alquilo (el resto de la cadena, en el C2): monosustituido. Eliminando el H del C3: doble enlace entre C2-C3, dando CH3-CH=C(CH3)-CH3 (2-metilbut-2-eno); aquí el C2 lleva un CH3 (el antiguo C1) y el C3 lleva DOS grupos alquilo (el metilo ramificado y el C4, también un CH3), así que hay tres grupos alquilo en total alrededor del doble enlace: trisustituido. Por Saytzeff, el 2-metilbut-2-eno (trisustituido) es el mayoritario. (b) Para que un alqueno tenga isomería E/Z, cada uno de sus dos carbonos debe llevar DOS sustituyentes distintos entre sí, no basta con que el conjunto tenga muchos sustituyentes. En el C2 del 2-metilbut-2-eno los dos sustituyentes son CH3 y H: distintos, cumple. Pero en el C3 los dos sustituyentes son el metilo ramificado y el C4, y AMBOS son simplemente -CH3: dos grupos idénticos. Como uno de los dos carbonos no tiene sustituyentes distintos entre sí, el 2-metilbut-2-eno NO presenta isomería E/Z, a pesar de ser el alqueno más sustituido de los dos posibles. Esto muestra que \'más sustituido\' (criterio de Saytzeff) y \'puede tener E/Z\' (criterio de la lección 12) son preguntas independientes que hay que comprobar por separado.",\n'
    '        "common_errors": [\n'
    '          "Asumir que, por ser el alqueno más sustituido, el 2-metilbut-2-eno debe tener necesariamente isomería E/Z, sin comprobar si los DOS sustituyentes de cada carbono del doble enlace son realmente distintos entre sí."\n'
    '        ],'
)

c = data.count(old)
print("count:", c)
assert c == 1
data = data.replace(old, new, 1)
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data)
print("replaced challenge_questions[0]")
