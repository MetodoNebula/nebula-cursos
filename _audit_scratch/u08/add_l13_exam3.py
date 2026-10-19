import io

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

old = '''"Explicar la reducción de cuatro a tres formas apelando solo a que 'dos de las combinaciones son enantiómeros', sin mencionar la simetría interna que hace que las otras dos colapsen en una sola forma meso."
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "challenge_questions": ['''

new = '''"Explicar la reducción de cuatro a tres formas apelando solo a que 'dos de las combinaciones son enantiómeros', sin mencionar la simetría interna que hace que las otras dos colapsen en una sola forma meso."
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "EX-Q08-13-EXAM3",
        "statement": "El 2-bromo-3-clorobutano, CH$_3$-CHBr-CHCl-CH$_3$, tiene dos carbonos quirales (C2 y C3). A diferencia del ácido tartárico, aqu\\u00ed las dos mitades de la mol\\u00e9cula vistas desde cada C* no son equivalentes entre s\\u00ed (una es -CHBr-CH$_3$ y la otra es -CHCl-CH$_3$). (a) Indica cu\\u00e1ntos estereois\\u00f3meros distintos puede tener como m\\u00e1ximo, y justifica si puede aparecer alguna forma meso. (b) Describe, usando cu\\u00f1as (cu\\u00f1a = hacia el lector, cu\\u00f1a discontinua = hacia atr\\u00e1s), un par de en\\u00e1ntiomeros de esta mol\\u00e9cula.",
        "marks": 3,
        "answer": "(a) $2^2=4$ estereois\\u00f3meros; no hay forma meso, porque las dos mitades de la mol\\u00e9cula no son equivalentes. (b) Un en\\u00e1ntiomero se obtiene invirtiendo a la vez todas las cu\\u00f1as del otro, en los dos carbonos quirales.",
        "full_solution": "(a) Con dos carbonos quirales hay como m\\u00e1ximo $2^n = 2^2 = 4$ estereois\\u00f3meros. Para que aparezca una forma meso hace falta que exista un plano de simetr\\u00eda interno, lo que exige que las dos mitades de la mol\\u00e9cula sean equivalentes entre s\\u00ed (como en el \\u00e1cido tart\\u00e1rico). Aqu\\u00ed no lo son (-CHBr-CH$_3$ frente a -CHCl-CH$_3$), as\\u00ed que no puede existir ninguna forma meso: los cuatro estereois\\u00f3meros son todos distintos, agrupados en dos pares de en\\u00e1ntiomeros (cada par es, a su vez, diastere\\u00f3mero del otro par). (b) Fijando el C2 con su -Br en cu\\u00f1a y su -H en cu\\u00f1a discontinua, y el C3 con su -Cl tambi\\u00e9n en cu\\u00f1a y su -H en cu\\u00f1a discontinua, se obtiene un primer estereois\\u00f3mero. Su en\\u00e1ntiomero se dibuja invirtiendo TODAS las cu\\u00f1as a la vez, en los dos carbonos quirales (lo que antes iba en cu\\u00f1a pasa a cu\\u00f1a discontinua y viceversa): el -Br y el -Cl quedan ahora en cu\\u00f1a discontinua y los -H en cu\\u00f1a. El resultado es la imagen especular exacta de la primera mol\\u00e9cula, no superponible con ella.",
        "mark_scheme": [
          "1 punto por calcular correctamente $2^n=4$",
          "1 punto por justificar que no hay forma meso al no ser equivalentes las dos mitades de la mol\\u00e9cula",
          "1 punto por describir un par de en\\u00e1ntiomeros invirtiendo todas las cu\\u00f1as a la vez en los dos carbonos quirales"
        ],
        "common_errors": [
          "Aplicar la f\\u00f3rmula $2^n$ sin comprobar si existe simetr\\u00eda interna, dando por hecho que siempre hay una forma meso o que nunca puede haberla.",
          "Al dibujar el en\\u00e1ntiomero, invertir la cu\\u00f1a de un solo carbono quiral en vez de las de todos a la vez, lo que generar\\u00eda un diastere\\u00f3mero y no el en\\u00e1ntiomero."
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "challenge_questions": ['''

c = data.count(old)
print("count:", c)
assert c == 1
data = data.replace(old, new, 1)
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data)
print("inserted")
