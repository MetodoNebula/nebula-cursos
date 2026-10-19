###  · quimica organica

Archivo de la unidad: `selectividad_quimica__U08_Organica`

#### Lección 01 — Carbono, enlaces e hibridación

**Valoración experta: MEDIA.** Teoría clara y bien graduada (direcciones de enlace → hibridación, σ/π, aleno) y ejemplos correctos (recuentos verificados: etano 7σ, eteno 5σ/1π, but-1-ino 9σ/2π, pent-3-en-1-ino 10σ/3π, 2-metilpropeno 11σ/1π, butadieno 9σ/2π). Fallos: la solución del propino acaba en un resultado erróneo (7 σ) que contradice la respuesta, la pregunta de examen repite la molécula del ejemplo 4, la pauta del V/F suma 3 puntos sobre 2 y se presenta como 'coincidencia' la equivalencia de fórmula aleno/alquino. Falta la hibridación de carbonos unidos a O/N (C=O, C≡N), muy frecuente en la PAU. Los ejercicios guiados solo tienen respuesta, sin desarrollo.

**Plan de arreglo:** 1) Corregir el final de exercises[1].full_solution (6 σ, 2 π) y completar su answer con las hibridaciones. 2) Cambiar la molécula de exam_questions[0] y ajustar la pauta de exam_questions[1] a 2 puntos. 3) Reescribir theory_blocks[4] y flashcards[10]: no es coincidencia, cada π resta 2 H. 4) Añadir un bloque y un ejercicio sobre C=O y C≡N. 5) Cambiar los 'why' genéricos de common_mistakes y añadir datos de longitud/energía de enlace.

**Hallazgos de la revisión experta:**

1. **[ALTA · CALCULO]** `exercises[1].full_solution` — La solución del propino recuenta mal al final y concluye 7 σ, contradiciendo la respuesta (6 σ), que es la correcta: el σ del triple ya está incluido en las 2 conexiones C–C. Además el texto queda descuidado ('más... recontando con cuidado').
   - *Texto actual:* «Total conexiones $=2+4=6$ σ más... recontando con cuidado: el triple aporta 1σ (ya incluido en las 2 conexiones entre carbonos) y 2π adicionales; total: $6+1=7$ σ y 2 π.»
   - *Arreglo:* Reescribir el cierre: 'Conexiones C–C: 2 (C1≡C2 y C2–C3); C–H: 1+0+3 = 4. Cada conexión aporta un único σ: 2+4 = 6 σ. El triple enlace aporta además 2 π. Total: 6 σ y 2 π.' (C$_3$H$_4$: 7 átomos, cadena abierta → 6 σ).
2. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — Afirma que la coincidencia de fórmula molecular entre un aleno y un alquino es 'por coincidencia numérica' y la presenta como propia de los dobles enlaces acumulados. No es casualidad: cada enlace π (o anillo) resta 2 H respecto al alcano, así que cualquier compuesto con 2 insaturaciones (aleno, dieno conjugado o aislado, alquino, cicloalqueno) es C$_n$H$_{2n-2}$. Además 'por eso… por coincidencia' es contradictorio.
   - *Texto actual:* «por eso la fórmula molecular de un compuesto con dos dobles enlaces consecutivos en un único carbono coincide, por coincidencia numérica, con la de un alquino»
   - *Arreglo:* 'Como cada enlace π resta 2 H respecto al alcano, cualquier compuesto con dos enlaces π (un aleno, un dieno cualquiera o un alquino) tiene la misma fórmula general C$_n$H$_{2n-2}$, aunque sus estructuras y geometrías sean distintas.'
3. **[MEDIA · CONCEPTO]** `flashcards[10]` — Llama 'pura coincidencia aritmética' a algo que es consecuencia directa del recuento de insaturaciones; y habla de 'alqueno con dos dobles' (es un dieno/aleno).
   - *Texto actual:* «Pura coincidencia aritmética: ambos casos tienen 2 enlaces π en total»
   - *Arreglo:* front: '¿Por qué un aleno (dos dobles consecutivos) tiene la misma fórmula molecular que un alquino del mismo nº de carbonos?'; back: 'No es casualidad: cada enlace π quita 2 H respecto al alcano; ambos tienen 2 π, luego ambos son C$_n$H$_{2n-2}$, aunque su estructura y geometría sean distintas.'
4. **[MEDIA · CALCULO]** `exam_questions[1].mark_scheme[0]` — El reparto de puntos suma 3 (3 apartados × (0,5 + 0,5)) pero la pregunta vale marks = 2.
   - *Texto actual:* «0,5 puntos por cada apartado correctamente calificado; 0,5 puntos adicionales por cada justificación correcta»
   - *Arreglo:* Ajustar a 2 puntos: 'Cada apartado vale 2/3 de punto: solo se puntúa si la calificación V/F va acompañada de su justificación' (o subir marks a 3). Redactar dirigido al alumno ('Para obtener la puntuación completa debes…').
5. **[MEDIA · SOLUCION_INCOMPLETA]** `exercises[1].answer` — El enunciado pide la hibridación de los tres carbonos y el recuento de enlaces, pero la respuesta destacada solo da el recuento.
   - *Texto actual:* «6 enlaces σ y 2 enlaces π»
   - *Arreglo:* 'C1 y C2: $sp$ (lineales, $180^{\circ}$); C3: $sp^3$ (tetraédrico, $109{,}5^{\circ}$). 6 enlaces σ y 2 enlaces π.'
6. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks` — La lección solo trata carbonos unidos a C y H. En la PAU es muy habitual pedir la hibridación de carbonos unidos a heteroátomos (C=O de aldehídos, cetonas y ácidos → $sp^2$; C≡N de nitrilos → $sp$; CO$_2$ → $sp$) y de átomos de O o N. No hay teoría ni ejercicios de ese caso.
   - *Texto actual:* «1 triple y 1 simple** (o, más raro, **2 dobles**) → hibridación $sp$»
   - *Arreglo:* Añadir un bloque breve 'Carbonos unidos a O y N': el criterio de contar direcciones vale igual para C=O y C≡N, con ejemplos (etanal CH$_3$-CHO: C1 $sp^3$, C2 $sp^2$; etanonitrilo CH$_3$-C≡N: C2 $sp$; ácido acético). Añadir un ejercicio que lo pida.
7. **[MEDIA · PLANTILLA]** `exam_questions[0].statement` — La pregunta de examen usa exactamente la misma molécula que el ejemplo resuelto 4 (HC≡C-CH=CH-CH$_3$, pent-3-en-1-ino), solo escrita al revés: el alumno ya tiene la solución vista y no practica nada nuevo. Además la solución numera 'desde el metilo', contraria a la numeración IUPAC del compuesto.
   - *Texto actual:* «Para la molécula CH$_3$-CH=CH-C$\equiv$CH (con un triple en un extremo y un doble en el centro)»
   - *Arreglo:* Cambiar la molécula, p. ej. CH$_2$=CH-CH$_2$-C$\equiv$C-CH$_3$ (hex-1-en-4-ino: C1, C2 $sp^2$; C3 $sp^3$; C4, C5 $sp$; C6 $sp^3$; C$_6$H$_8$ → 13 σ y 3 π) o una con grupo carbonilo/nitrilo, y numerar según IUPAC.
8. **[BAJA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — El razonamiento solo usa el máximo de π por carbono, sin tener en cuenta que cada π es compartido por dos carbonos vecinos (en una cadena, el π del 2.º carbono tiene que ser con el 3.º, etc.). Además el enunciado ya revela la respuesta ('hasta llegar a un carbono con hibridación forzosamente imposible'), y la frase 'No existe ninguna hibridación con una sola dirección de enlace' es innecesaria y confusa.
   - *Texto actual:* «La secuencia 0,1,2,3... es imposible de sostener a partir del cuarto carbono, que debería tener 3 π»
   - *Arreglo:* Añadir: 'Además, cada π une dos carbonos: C2 (1 π) solo puede tenerlo con C3; C3 (2 π) necesita otro π con C4 (aleno C2=C3=C4); C4 ya tendría 1 π y debería tener 3 → imposible.' Reformular el enunciado: '…¿Es posible? Si no, ¿en qué carbono falla y por qué?'.
9. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[5].body` — Explica que el triple es más corto y no tres veces más fuerte, pero sin dar ningún dato que lo ilustre; además 'el primer enlace de cada par' no se entiende (no hay pares).
   - *Texto actual:* «pero la fuerza del enlace **no** crece en la misma proporción exacta: el primer enlace de cada par, el σ, es el más fuerte»
   - *Arreglo:* Sustituir 'el primer enlace de cada par' por 'el primer enlace de cada enlace múltiple' y añadir una tabla orientativa: C–C 154 pm, ≈347 kJ/mol; C=C 134 pm, ≈614 kJ/mol; C≡C 120 pm, ≈839 kJ/mol (839 < 3·347).
10. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico que no explica por qué se comete el error (se repite igual en common_mistakes[1] y [2]).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: 'La notación con tres rayitas sugiere tres enlaces iguales.' [1]: 'Toda fórmula desarrollada se dibuja en el plano del papel.' [2]: 'Se cuentan los tres orbitales híbridos y se olvida el $p$ sin hibridar.'
11. **[BAJA · VISUAL]** `theory_blocks[1].assets[0].svg` — En la figura el rótulo '109,5°' se monta sobre los enlaces del carbono $sp^3$ y no hay arco que marque el ángulo; la cuña se dibuja como una flecha (puede leerse como vector o flecha de reacción); el carbono central no está rotulado.
   - *Texto actual:* «(figura) 109,5° superpuesto a los enlaces; enlace en cuña dibujado como flecha»
   - *Arreglo:* Desplazar el rótulo fuera de los enlaces con un arco, dibujar la cuña como triángulo relleno y rotular el carbono central 'C'.
12. **[BAJA · ESTRUCTURA]** `summary.formulas[0]` — La única fórmula del resumen (C$_n$H$_{2n+2}$) pertenece a la lección siguiente y no resume nada de esta lección (hibridación/σ-π).
   - *Texto actual:* «C_nH_{2n+2}\ \text{(referencia: alcano saturado, próxima lección)}»
   - *Arreglo:* Sustituir por algo propio de la lección, p. ej. '\text{n.º de }\sigma=\text{n.º de conexiones entre átomos};\ \pi=1\ (\text{doble}),\ 2\ (\text{triple})', o dejar formulas vacío.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (3): `common_mistakes[0].why`, `common_mistakes[1].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «El 2-metilpropeno tiene de fórmula CH$_2$=C(CH$_3$)$_2$: un carbono central unido por doble enlace a un -CH$_2$ terminal \|\| RESP: (a) Ambos $sp^2$, $120^{\circ}$. (b) Ambos $sp^3…». Arreglo: Añadir full_solution paso a paso.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (2): `worked_examples[3].statement`, `guided_exercises[1].statement`. Ej.: «Para el compuesto HC$\equiv$C-CH=CH-CH$_3$ (pent-3-en-1-ino), indica la hibridación de cada uno de». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-C". (1): `exam_questions[0].statement`. Ej.: «Para la molécula CH$_3$-CH=CH-C$\equiv$CH (con un triple en un extremo y un doble en el cen». Arreglo: Sustituir el código por una descripción en texto.

#### Lección 02 — Alcanos y nomenclatura de cadenas ramificadas

**Valoración experta: MEDIA.** Las reglas básicas (cadena más larga, primer punto de diferencia, orden alfabético sin multiplicadores) están bien explicadas, y casi todos los ejercicios y test son correctos (verificados nonano, 2-metilpentano, 3-metilheptano, 4-etil-2,2-dimetilhexano C$_{10}$H$_{22}$, 2,4-dimetilhexano, 2,2,4-trimetilhexano). Pero dos de los cuatro ejemplos resueltos están mal: el ejemplo 4 da como solución '2-propilbutano' (debe ser 3-metilhexano) y el ejemplo 2 razona sobre una cadena de 5 C que en realidad es de 6. La lección se contradice sobre si un etilo puede alargar la cadena ('2 o más' / '3 o más'). Falta el desempate alfabético de localizadores, y no hay cicloalcanos ni sustituyentes ramificados.

**Plan de arreglo:** 1) Corregir la solución del ejemplo 4 (3-metilhexano). 2) Rehacer el ejemplo 2 (enunciado, datos, razonamiento) con la cadena de 6 C, o cambiar la molécula. 3) Unificar en '2 o más carbonos' (flashcards[2], key_points[4], exam_notes[3], common_mistakes[3]). 4) Añadir a la teoría el desempate alfabético de localizadores. 5) Arreglar diagnostic_items[1] y la solución del reto (isómeros con cadena de butano). 6) Formato de fórmulas uniforme.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `worked_examples[1].reasoning[0]` — El ejemplo afirma que la cadena principal es de 5 carbonos y que el etilo 'no permite alargarla', pero el etilo está en el carbono contiguo al CH$_3$ terminal y SÍ la alarga: la cadena más larga es de 6 C (CH$_3$-CH$_2$-CH(CH$_3$)-CH(CH$_2$CH$_3$)-CH$_3$ → hexano con dos metilos). Los razonamientos [1] y [2] (metilo en 2 y etilo en 3, alfabetizar etil/metil) también son falsos, y la solución '3,4-dimetilhexano' (correcta) no se deduce de ellos. Es justo el error de 'cadena dibujada en horizontal' que la lección enseña a evitar.
   - *Texto actual:* «La cadena principal es de 5 carbonos: el sustituyente más largo (el etilo, 2 carbonos) no permite alargarla más.»
   - *Arreglo:* Rehacer statement, knowns, reasoning y common_mistake: 'El etilo está en el carbono vecino a un extremo: pasando por él se obtiene una cadena de 6 C (hexano). Los sustituyentes son dos metilos: el del C3 y el CH$_3$ terminal que en el dibujo era cadena (ahora metilo en C4); {3,4} desde ambos extremos. Nombre: 3,4-dimetilhexano, C$_8$H$_{18}$.' Si se quiere un ejemplo de alfabetización etil/metil, usar otra molécula, p. ej. CH$_3$-CH(CH$_3$)-CH(C$_2$H$_5$)-CH$_2$-CH$_2$-CH$_3$ → 3-etil-2-metilhexano.
2. **[ALTA · SOLUCION_EQUIVOCADA]** `worked_examples[3].solution` — El nombre final contradice todo el razonamiento del propio ejemplo, la interpretación y la figura (cadena de 6 C con un metilo en 3). '2-propilbutano' es justo el nombre incorrecto que el ejemplo pretende evitar.
   - *Texto actual:* «2-propilbutano»
   - *Arreglo:* '3-metilhexano' (C$_7$H$_{16}$).
3. **[ALTA · ENUNCIADO]** `worked_examples[1].statement` — El enunciado afirma que la molécula es un pentano con un etilo y un metilo, lo que es falso (la cadena principal es de 6 C) y dirige al alumno a un nombre erróneo.
   - *Texto actual:* «(un grupo etilo y un grupo metilo sobre una cadena de 5 carbonos)»
   - *Arreglo:* Eliminar el paréntesis o sustituirlo por '(comprueba primero cuál es la cadena más larga)'. Corregir también knowns[0] y common_mistake.
4. **[MEDIA · CONCEPTO]** `theory_blocks[5].body` — La lección se contradice sobre qué sustituyente puede alargar la cadena: aquí dice 'de 2 o más carbonos' (correcto: un etilo en C2 ya alarga), pero flashcards[2], summary.key_points[4], exam_notes[3] y common_mistakes[3] dicen 'de 3 o más carbonos'. El ejemplo 2 es precisamente un etilo que alarga la cadena.
   - *Texto actual:* «Hay que comprobarlo siempre que haya un sustituyente de 2 o más carbonos»
   - *Arreglo:* Unificar en todos esos campos: 'Siempre que haya un sustituyente de 2 o más carbonos (un etilo en el C2 desde un extremo ya alarga la cadena), comprueba si pasando por él hay una cadena más larga.' Ampliar este bloque (ahora es una sola frase) con un ejemplo dibujado.
5. **[MEDIA · CONCEPTO]** `flashcards[2].back` — Dice que solo hay que sospechar con sustituyentes de 3 o más carbonos; un etilo (2 C) en posición 2 también alarga la cadena (ejemplo 2 de la lección). Ídem en summary.key_points[4], exam_notes[3] y common_mistakes[3].how_to_avoid.
   - *Texto actual:* «Siempre que haya un sustituyente de 3 o más carbonos»
   - *Arreglo:* 'Siempre que haya un sustituyente de 2 o más carbonos (p. ej. un etilo en el carbono 2): comprueba si pasando por él se obtiene una cadena más larga.' Cambiar igual en summary.key_points[4], exam_notes[3] y common_mistakes[3].
6. **[MEDIA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — Para afirmar que solo hay dos respuestas, la solución tiene que descartar los isómeros de C$_6$H$_{14}$ con cadena de butano y no lo hace. La pista 1 incluso dice que C$_6$H$_{14}$ solo puede ser pentano + metilo o hexano, lo que es falso: también existen 2,2-dimetilbutano y 2,3-dimetilbutano.
   - *Texto actual:* «Con una cadena de pentano y un metilo: … Ambas estructuras cumplen la condición, y ninguna otra posición la cumple»
   - *Arreglo:* Añadir: 'Los isómeros con cadena de 4 C no valen: 2,3-dimetilbutano tiene DOS carbonos unidos a tres C y 2,2-dimetilbutano tiene un carbono unido a cuatro C y ninguno a tres.' Corregir hints[0]: 'C$_6$H$_{14}$ tiene 5 isómeros: hexano, 2- y 3-metilpentano, 2,2- y 2,3-dimetilbutano'.
7. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — Falta la regla de desempate cuando las dos numeraciones dan la misma lista de localizadores: se da el número más bajo al sustituyente que va primero por orden alfabético (p. ej. 3-etil-4-metilhexano, o el 2-bromo-3-metilbutano de la lección de halogenados). La lección siguiente de halogenados la necesita y nunca se enseña.
   - *Texto actual:* «(3) comparar las dos listas **cifra a cifra**, empezando por la primera: gana la lista con el valor menor en el primer punto en que ambas difieran»
   - *Arreglo:* Añadir el paso (4): 'Si ambas listas son idénticas, se da el localizador más bajo al sustituyente citado primero por orden alfabético', con un ejemplo: CH$_3$-CH$_2$-CH(C$_2$H$_5$)-CH(CH$_3$)-CH$_2$-CH$_3$ da {3,4} desde ambos extremos → el 3 va al etilo (e < m) → 3-etil-4-metilhexano.
8. **[MEDIA · ESTRUCTURA]** `diagnostic_items[1]` — La pregunta pide contar C y H de una fórmula, pero la respuesta errónea típica, su interpretación y la acción de refuerzo hablan de la numeración ('La posición 4, por numerar de izquierda a derecha'): no tienen nada que ver con la pregunta. Además usa subíndices Unicode (CH₃, C₅H₁₂) en vez de LaTeX.
   - *Texto actual:* «common_wrong_answers[0].answer = La posición 4, por numerar de izquierda a derecha según esté dibujada.»
   - *Arreglo:* Respuesta errónea: 'C$_5$H$_{10}$, olvidando los 3 H del metilo sustituyente'; interpretación: 'No suma los H de los sustituyentes'; remediación: 'Contar C y H grupo a grupo (CH$_3$ + CH + CH$_3$ + CH$_2$ + CH$_3$)'. Escribir las fórmulas con CH$_3$ y C$_5$H$_{12}$.
9. **[BAJA · ENUNCIADO]** `challenge_questions[0].statement` — '(y a ningún otro)' dice literalmente que ese carbono solo está unido a tres carbonos y a nada más, pero tiene un H; lo que se quiere decir es que no está unido a un cuarto carbono.
   - *Texto actual:* «exactamente un carbono unido a otros tres carbonos distintos (y a ningún otro)»
   - *Arreglo:* '…tiene exactamente un carbono unido a tres átomos de carbono (y ningún carbono unido a cuatro).'
10. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks` — No se tratan los sustituyentes ramificados frecuentes (isopropilo, terc-butilo), los cicloalcanos (C$_n$H$_{2n}$) ni ninguna propiedad física o reacción de los alcanos (combustión, halogenación por radicales, tendencia de los puntos de ebullición), que aparecen en el temario de PAU. Puede que vengan en otra lección: si no, faltan.
   - *Texto actual:* «Esta lección desarrolla esas tres reglas para el caso más sencillo, los alcanos.»
   - *Arreglo:* Añadir al menos un bloque con cicloalcanos (ciclohexano, metilciclopentano) y los nombres de isopropilo/terc-butilo, o remitir con claridad a la lección donde se ven.
11. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Explicación genérica que no dice por qué se comete el error (igual en common_mistakes[2].why).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: 'Se traslada el hábito de lectura de izquierda a derecha.' [2]: 'El nombre se escribe junto y parece natural ordenar por la palabra completa.'
12. **[BAJA · LATEX]** `theory_blocks[1].body` — Las fórmulas químicas van en modo matemático sin \mathrm ($CH_4$, $C_5H_{12}$, $C_nH_{2n+2}$) y salen en cursiva, mezcladas con otras en texto (CH$_3$). Pasa en toda la lección.
   - *Texto actual:* «metano ($CH_4$), etano ($C_2H_6$)»
   - *Arreglo:* Usar $\mathrm{CH_4}$, $\mathrm{C_2H_6}$, $\mathrm{C}_n\mathrm{H}_{2n+2}$ (o el estilo CH$_4$ ya usado en los enunciados) de forma uniforme.
13. **[BAJA · ERRATA]** `theory_blocks[1].body` — Dice que los sustituyentes se nombran con el sufijo '-il' y luego da 'metilo, etilo…'. Lo correcto: el grupo aislado acaba en '-ilo' (metilo) y dentro del nombre se apocopa a '-il' (2-metilbutano).
   - *Texto actual:* «Las mismas raíces, con el sufijo '-il' en vez de '-ano', nombran los sustituyentes: metilo, etilo, propilo, butilo...»
   - *Arreglo:* '…con el sufijo -ilo (metilo, etilo, propilo…), que se acorta a -il dentro del nombre del compuesto (2-metilbutano).'
14. **[BAJA · ERRATA]** `exam_notes[1]` — Dice que tres compuestos de la lección son C$_8$H$_{18}$, pero son cinco (3,4-dimetilhexano, 2,2,4-trimetilpentano, 3-etilhexano, 3-metilheptano y 2,4-dimetilhexano).
   - *Texto actual:* «comparten la fórmula molecular $C_8H_{18}$ (tres de ellos)»
   - *Arreglo:* '(cinco de ellos: 3,4-dimetilhexano, 2,2,4-trimetilpentano, 3-etilhexano, 3-metilheptano y 2,4-dimetilhexano)'.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «El compuesto CH$_3$-CH$_2$-CH(C$_2$H$_5$)-CH$_2$-CH$_2$-CH$_3$ tiene una cadena principal de 6 carbonos con un único sus \|\| RESP: (a) 3 desde un extremo, 4 desde el otro. (b) 3-e…». Arreglo: Añadir full_solution paso a paso.

#### Lección 03 — Alquenos y alquinos

**Valoración experta: MEDIA.** Nombres y fórmulas correctos en todos los ejemplos y ejercicios (but-2-eno, 3-metilbut-1-eno, 4-metilpent-2-eno, 3-metilpenta-1,3-dieno C$_6$H$_{10}$, 4-metilpent-2-ino, hept-2-ino, 5-metilhex-2-eno C$_7$H$_{14}$, 2-metilbut-1-eno) y buena insistencia en la prioridad del enlace múltiple. Pero la regla de prioridad está sobresimplificada ('nunca' decide un sustituyente, cuando sí decide si el doble queda simétrico) y la regla de la cadena principal es ambigua respecto a IUPAC 1993/2013. Los datos del mcq[1] son incoherentes. Se repite que dieno/alquino es una 'coincidencia aritmética' y se explica la pérdida de H por la geometría. Faltan los eninos (que la lección 1 ya usa), la 'a' eufónica de los dienos y la isomería cis/trans.

**Plan de arreglo:** 1) Corregir los datos de mcq[1] (metilo 5/2). 2) Reescribir theory_blocks[3], flashcards[2] y misconceptions[0]: el desempate por sustituyentes cuando el doble es simétrico (ej. 2-metilhex-3-eno). 3) Fijar la regla de cadena principal según la PAU (IUPAC 1993) y revisar mcq[5]. 4) Quitar 'coincidencia' de theory_blocks[4], worked_examples[3] y flashcards[0], y la explicación por la geometría en theory_blocks[0] y prerequisites[0]. 5) Añadir eninos y la 'a' eufónica con un ejercicio.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `theory_blocks[3].body` — Dice que los sustituyentes solo desempatan si hay dos enlaces múltiples. Es incompleto: también desempatan cuando el único enlace múltiple recibe el mismo localizador desde los dos extremos. Ej.: CH$_3$-CH(CH$_3$)-CH=CH-CH$_2$-CH$_3$, con el doble en 3 por ambos lados → el metilo decide → 2-metilhex-3-eno (no 5-metilhex-3-eno). Es un caso típico de PAU y no aparece. Lo mismo dicen misconceptions[0].correct_model y flashcards[1].
   - *Texto actual:* «solo si existieran dos enlaces múltiples con un posible empate entre sí se recurriría a los sustituyentes para desempatar»
   - *Arreglo:* 'Si el enlace múltiple recibe el mismo localizador desde ambos extremos (o hay empate entre varios enlaces múltiples), se aplican después las reglas de los alcanos a los sustituyentes: localizadores más bajos y, si persiste el empate, orden alfabético.' Añadir el ejemplo 2-metilhex-3-eno.
2. **[MEDIA · CONCEPTO]** `flashcards[2].back` — 'Nunca' es falso: cuando el enlace múltiple y los localizadores de los sustituyentes quedan iguales desde ambos extremos, el orden alfabético sí decide la numeración (el primer sustituyente citado lleva el número más bajo). Ej.: CH$_3$-CHBr-CH=CH-CHCl-CH$_3$ → 2-bromo-5-clorohex-3-eno.
   - *Texto actual:* «Nunca para decidir el sentido de numeración (eso lo decide siempre el enlace múltiple)»
   - *Arreglo:* 'Solo como último desempate: si el enlace múltiple y la lista de localizadores de los sustituyentes salen iguales desde ambos extremos, se da el número más bajo al sustituyente citado primero por orden alfabético.'
3. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — Se contradice: llama 'pura coincidencia aritmética' a la igualdad de fórmula dieno/alquino y en la misma frase da la causa (mismo grado de insaturación). No es casualidad. Se repite en worked_examples[3].interpretation ('es solo una coincidencia aritmética') y en flashcards[0] ('por puro azar aritmético').
   - *Texto actual:* «pura coincidencia aritmética (ambos tienen el mismo grado de insaturación, 2), no un parecido estructural»
   - *Arreglo:* '…coincide con la de un alquino del mismo $n$. No es casualidad: ambos tienen 2 insaturaciones y cada una resta 2 H. Lo que difiere es la estructura (cuatro C $sp^2$ frente a dos C $sp$).' Corregir igual worked_examples[3].interpretation y flashcards[0].back.
4. **[MEDIA · CONCEPTO]** `theory_blocks[0].body` — Atribuye la pérdida de hidrógenos a la geometría o a la falta de 'sitio'. La causa real es la tetravalencia: cada enlace extra entre dos carbonos usa una valencia de cada uno, que ya no puede unirse a un H. prerequisites[0].why_it_matters repite la idea ('por la geometría que ya conoces').
   - *Texto actual:* «precisamente porque esos dos carbonos ya no tienen sitio para tantos hidrógenos (recuerda la geometría $sp^2$ y $sp$ de la primera lección)»
   - *Arreglo:* '…porque cada carbono forma siempre 4 enlaces: si gasta dos (doble) o tres (triple) en unirse al otro carbono, le quedan menos valencias para hidrógenos. Cada enlace π extra quita 2 H a la molécula.' Corregir igual prerequisites[0].why_it_matters.
5. **[MEDIA · ENUNCIADO]** `mcq[1].stem` — Los datos no son coherentes. Si el doble enlace tiene localizador 2 desde un extremo y 4 desde el otro, la cadena tiene 6 C, y un metilo en 5 desde el primer extremo está en 2 desde el otro, no en 3. Un alumno que compruebe los datos se queda bloqueado.
   - *Texto actual:* «un sustituyente metilo recibiría el localizador 5 desde el primer extremo, o el 3 desde el segundo»
   - *Arreglo:* '…el localizador 5 desde el primer extremo, o el 2 desde el segundo' y cambiar options[0].text a 'La que da localizador 2 al metilo (y 4 al doble enlace)…' (es la molécula de exercises[3], 5-metilhex-2-eno).
6. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks` — Faltan reglas que la propia unidad usa o que la PAU pide: (1) compuestos con doble y triple enlace (-en-…-ino; con empate de localizadores, el doble lleva el número más bajo). La lección 1 ya usa 'pent-3-en-1-ino' sin explicarlo. (2) La 'a' eufónica de penta-1,3-dieno / buta-1,3-dieno, que se usa sin explicar. (3) Isomería cis/trans del but-2-eno y otros alquenos, si no se ve en otra lección.
   - *Texto actual:* «se nombra con el sufijo '-dieno' y **dos** localizadores»
   - *Arreglo:* Añadir: 'Si hay doble y triple enlace: sufijo -en-…-ino, numerando para dar los localizadores más bajos al conjunto; en caso de empate, el doble lleva el número menor (pent-1-en-4-ino).' y 'Con -dieno, -diino… se añade una a a la raíz: buta-1,3-dieno, penta-1,3-dieno.' Añadir un ejercicio con un enino.
7. **[MEDIA · VERIFICAR]** `theory_blocks[3].body` — La regla de la cadena principal es ambigua y no corresponde exactamente a ninguna norma. Con IUPAC 1993 (la habitual en la PAU) la cadena principal es la que contiene el máximo número de enlaces múltiples, aunque NO sea la más larga. Con IUPAC 2013 manda la longitud y el doble enlace puede quedar fuera (sustituyente 'ilideno'). mcq[5] (clave D: 'ninguna regla deja de aplicarse') y su options[1].why_wrong ('se sigue eligiendo por ser la más larga posible') se basan en esta ambigüedad. Hay que comprobar qué criterio usa la PAU de referencia.
   - *Texto actual:* «cadena principal más larga —que, además, debe incluir siempre el enlace múltiple, orden alfabético de sustituyentes, prefijos di-/tri-/tetra-) se mantienen sin cambios»
   - *Arreglo:* Fijar el criterio de la PAU: 'La cadena principal es la que contiene el enlace múltiple (o el máximo número de ellos); entre esas, la más larga.' Añadir un ejemplo en el que importe: CH$_2$=C(CH$_2$CH$_2$CH$_3$)-CH$_2$CH$_2$CH$_2$CH$_3$ → 2-propilhex-1-eno (IUPAC 1993). Revisar mcq[5]: o se cambia la clave o se reformula la opción B. Cerrar también la raya que queda abierta tras 'más larga —'.
8. **[BAJA · PLANTILLA]** `common_mistakes[1].why` — Explicación genérica que no dice por qué se comete el error (igual en common_mistakes[2].why).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [1]: 'El enlace une dos carbonos y parece natural citar ambos números.' [2]: 'Se recuerda alqueno = C$_n$H$_{2n}$ sin contar las insaturaciones.'
9. **[BAJA · LATEX]** `theory_blocks[1].body` — Las fórmulas generales y moleculares van en modo matemático sin \mathrm ($C_nH_{2n}$, $C_4H_8$) y salen en cursiva. Pasa en toda la lección.
   - *Texto actual:* «la fórmula general es $C_nH_{2n}$»
   - *Arreglo:* $\mathrm{C}_n\mathrm{H}_{2n}$, $\mathrm{C_4H_8}$, etc., de forma uniforme.
10. **[BAJA · ESTRUCTURA]** `diagnostic_items[1].common_wrong_answers[0]` — La respuesta errónea y su interpretación no encajan con la pregunta (que es qué se elige primero, cadena o sustituyentes): la interpretación habla del localizador más bajo.
   - *Texto actual:* «No es el criterio IUPAC; el criterio es el localizador más bajo, comparado cifra a cifra si hay varios.»
   - *Arreglo:* Respuesta errónea: 'Primero se localizan los sustituyentes y luego se busca la cadena que los contiene'; interpretación: 'Invierte el orden: sin cadena principal no hay numeración posible.'

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[1].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «El compuesto HC$\equiv$C-CH$_2$-CH$_2$-CH$_3$ es un alquino de 5 carbonos con el triple enlace en un extremo. **(a)** Nó \|\| RESP: (a) pent-1-ino. (b) $C_5H_8$.». Arreglo: Añadir full_solution paso a paso.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (6): `worked_examples[0].statement`, `worked_examples[1].statement`, `worked_examples[2].statement`, `worked_examples[3].statement`, `exercises[1].statement`, `exercises[3].statement`. Ej.: «Nombra el alqueno CH$_3$-CH=CH-CH$_3$ y da su fórmula molecular.». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-C". (1): `worked_examples[3].statement`. Ej.: «Nombra el dieno CH$_2$=CH-C(CH$_3$)=CH-CH$_3$ y da su fórmula molecular.». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · PLANTILLA] Texto idéntico repetido en 9 lecciones del curso (probable plantilla genérica). (1): `exam_questions[1].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 04 — Derivados halogenados

**Valoración experta: MEDIA.** La nomenclatura básica, la clasificación 1.º/2.º/3.º y la dirección del efecto −I están bien explicadas, y las fórmulas y nombres son correctos (C$_4$H$_9$Cl, C$_3$H$_7$Br, C$_2$H$_4$Cl$_2$, C$_5$H$_{11}$F, 2,2-dibromopropano C$_3$H$_6$Br$_2$, 3-cloropentano). Problemas: el ejercicio guiado 2 necesita el desempate alfabético de localizadores, que no se enseña; la teoría pone el localizador detrás del prefijo; el reto dice que hay varias soluciones cuando la única es 2-cloro-2-metilbutano. La escala −I con −COOH > −X es discutible (las σ$_I$ medidas dicen lo contrario) y sostiene un ejemplo, un test y un V/F. Además 'fluor-' en lugar de 'fluoro-', una referencia rota, y faltan un contraejemplo de orden alfabético (alquilo antes que halógeno) y las propiedades físicas.

**Plan de arreglo:** 1) Añadir a la teoría el desempate alfabético de localizadores y desarrollar G2. 2) Corregir la posición del localizador en theory_blocks[1] y 'fluor-' → 'fluoro-' en todos los campos. 3) Corregir el reto (solución única). 4) Comprobar la escala −I con el temario; si se mantiene, quitar −COOH frente a X y rehacer WE4, mcq[3] y EXAM2(c) con comparaciones seguras (F>Cl>Br>I, −NO$_2$>−X). 5) Arreglar la referencia rota y 'lote', mcq[4] y añadir un ejemplo con alquilo delante del halógeno y un bloque de propiedades.

**Hallazgos de la revisión experta:**

1. **[ALTA · TEORIA_INCOMPLETA]** `guided_exercises[1]` — En CH$_3$-CHBr-CH(CH$_3$)-CH$_3$ las dos numeraciones dan la misma lista {2,3}. Para decidir que el 2 es del bromo hace falta la regla 'en caso de empate, el localizador más bajo va al sustituyente citado primero por orden alfabético'. Esa regla no se explica ni aquí ni en la lección de alcanos (la teoría dice 'no hay ninguna regla nueva de numeración'). Las pistas solo hablan del orden de escritura, así que el alumno no puede justificar la numeración.
   - *Texto actual:* «(a) 2-bromo-3-metilbutano.»
   - *Arreglo:* Añadir a theory_blocks[1]: 'Si las dos numeraciones dan la misma lista de localizadores, se da el número más bajo al sustituyente que se cita primero por orden alfabético.' Añadir una pista a G2 ('Numera desde ambos extremos: obtienes {2,3} en los dos casos; el empate lo decide el orden alfabético: bromo < metil') y una solución desarrollada.
2. **[MEDIA · CONCEPTO]** `theory_blocks[1].body` — Dice que el prefijo va 'seguido del localizador', es decir, localizador detrás del prefijo ('cloro-2'). Es al revés: el localizador va delante del prefijo y unido con guion (2-cloro), como dice el propio mcq[0].options[3].
   - *Texto actual:* «**fluoro-**, **cloro-**, **bromo-**, **yodo-**, seguido (sin espacio) del localizador del carbono al que está unido»
   - *Arreglo:* '…fluoro-, cloro-, bromo-, yodo-, precedido de su localizador y un guion: 2-clorobutano, 1,2-dibromoetano.'
3. **[MEDIA · CONCEPTO]** `challenge_questions[0].full_solution` — La solución y la respuesta dicen que hay otras estructuras posibles, pero 2-cloro-2-metilbutano es el ÚNICO C$_5$H$_{11}$Cl con el Cl en un carbono terciario: el pentano no tiene carbonos terciarios, el 2-metilbutano solo tiene uno (el C2) y el 2,2-dimetilpropano solo tiene un carbono cuaternario y primarios. La coletilla '(sin ramificaciones aparte de las que sean necesarias)' del enunciado tampoco tiene sentido.
   - *Texto actual:* «No es la única estructura posible con un carbono terciario clorado y 5 carbonos en total, pero sí una válida.»
   - *Arreglo:* Respuesta: '2-cloro-2-metilbutano (es la única posible)'. Justificarlo repasando los tres esqueletos de C$_5$: pentano (sin C terciario), 2-metilbutano (C2 terciario → 2-cloro-2-metilbutano) y 2,2-dimetilpropano (sin C terciario). Quitar el paréntesis del enunciado o pedir explícitamente 'razona si es la única'.
4. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — La escala $-NO_2>-CN>-COOH>-X>-OH$ es una regla de libro, discutible y no del temario habitual de PAU. Según las constantes inductivas medidas (σ$_I$ ≈ NO$_2$ 0,65; CN 0,56; F 0,52; Cl 0,47; Br 0,44; I 0,39; COOH ≈ 0,30; OH ≈ 0,25), F, Cl y Br atraen MÁS que −COOH. Además, poner 'X' en un solo escalón oculta que F > Cl > Br > I. De esta escala dependen worked_examples[3], mcq[3], exam_questions[1](c), flashcards[3] y [4] y summary.key_points[3], y la justificación de worked_examples[3].reasoning[2] ('−COOH concentra dos oxígenos') no se sostiene.
   - *Texto actual:* «De mayor a menor efecto inductivo negativo: $-NO_2 > -CN > -COOH > -X\text{(halógeno)} > -OH$.»
   - *Arreglo:* Comprobar con el temario de la PAU. Si se mantiene, quitar −COOH de la comparación con los halógenos y usar solo comparaciones seguras: −NO$_2$ > −F > −Cl > −Br > −I; los grupos alquilo tienen efecto +I. Rehacer worked_examples[3], mcq[3] y exam_questions[1](c) con esas comparaciones (p. ej. '¿qué ejerce mayor efecto −I, −F o −I?').
5. **[MEDIA · CONCEPTO]** `theory_blocks[5].body` — Presenta 'F>Cl>Br>I' como una escala de electronegatividad ajena al tema, cuando es precisamente el orden del efecto −I entre halógenos (lo que más importa en esta lección). Además, la escala de grupos no es 'de electronegatividad'. El bloque confunde más de lo que aclara.
   - *Texto actual:* «La electronegatividad **entre los propios halógenos** ($F>Cl>Br>I$), que no es el tema de esta lección.»
   - *Arreglo:* Reescribir: 'Entre los halógenos, el efecto −I sigue el orden de electronegatividad: −F > −Cl > −Br > −I. Por eso el C–F es el enlace más polar (aunque el C–I, más largo y débil, es el que se rompe con más facilidad en las reacciones).' Corregir igual flashcards[4].
6. **[MEDIA · MCQ]** `mcq[4]` — Dos opciones dan la misma respuesta a la pregunta ('El cloro'), A y B, y solo cambia el motivo. El enunciado pregunta 'qué sustituyente se cita primero', así que la B también es correcta tal y como está formulada.
   - *Texto actual:* «options[1].text = El cloro, porque los halógenos siempre se citan en primer lugar»
   - *Arreglo:* Cambiar el enunciado a '¿Qué sustituyente se cita primero y por qué?', o mejor usar un caso en que el alquilo va primero (etilo y yodo: 3-etil-1-yodopentano), donde la opción 'el halógeno siempre primero' sea claramente falsa.
7. **[MEDIA · TEORIA_INCOMPLETA]** `misconceptions[2]` — La lección combate la idea de que 'el halógeno siempre va primero', pero ningún ejemplo ni ejercicio tiene un alquilo que vaya alfabéticamente delante del halógeno: siempre es cloro o bromo con metil, donde el halógeno va primero de todos modos. El alumno nunca ve el contraejemplo.
   - *Texto actual:* «El halógeno suele ser el 'protagonista' del compuesto y parece razonable que vaya primero en el nombre.»
   - *Arreglo:* Añadir un ejercicio o ejemplo con un alquilo delante, p. ej. ICH$_2$-CH$_2$-CH(C$_2$H$_5$)-CH$_2$-CH$_3$ → 3-etil-1-yodopentano (etil < yodo), o 4-etil-2-fluorohexano.
8. **[MEDIA · REFERENCIA_ROTA]** `prerequisites[0].statement` — Coletilla rota que sale de una sustitución automática.
   - *Texto actual:* «(el apartado correspondiente de esta unidad)»
   - *Arreglo:* '(lección 2 de esta unidad: «Alcanos y nomenclatura de cadenas ramificadas»)'.
9. **[MEDIA · ERRATA]** `flashcards[9].back` — El prefijo IUPAC es 'fluoro-', no 'fluor-' (la teoría y el ejercicio 1-fluoropentano usan 'fluoro'). El error se repite en objectives[0], flashcards[0], flashcards[6], misconceptions[2].correct_model y summary.key_points[0].
   - *Texto actual:* «fluor- (F), cloro- (Cl), bromo- (Br), yodo- (I).»
   - *Arreglo:* 'fluoro- (F), cloro- (Cl), bromo- (Br), yodo- (I)' en todos esos campos.
10. **[BAJA · SOLUCION_INCOMPLETA]** `worked_examples[2].common_mistake` — El campo solo pone el nombre incorrecto, sin explicar cuál es el error.
   - *Texto actual:* «2-metil-2-cloropropano»
   - *Arreglo:* 'Escribir 2-metil-2-cloropropano, poniendo el metilo delante del cloro: el orden alfabético exige cloro (c) antes que metil (m).'
11. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks` — La lección no dice nada de las propiedades físicas (enlace C–X polar, puntos de ebullición más altos que los del alcano, densidad, insolubilidad en agua) ni de los nombres habituales en la PAU (cloroformo CHCl$_3$, tetracloruro de carbono CCl$_4$, cloruro de vinilo). Tampoco trata los derivados halogenados insaturados (el halógeno no compite con el doble enlace al numerar).
   - *Texto actual:* «Esta lección se limita a dos cosas: nombrarlos correctamente y entender por qué el carbono que lleva el halógeno queda especialmente reactivo.»
   - *Arreglo:* Añadir un bloque breve de propiedades y usos, y un ejemplo de haloalqueno: CH$_2$=CH-CH$_2$Cl → 3-cloroprop-1-eno (el doble enlace manda al numerar).
12. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Explicación genérica que no dice por qué se comete el error (igual en common_mistakes[1].why y [2].why).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: 'El halógeno es un sustituyente real y parece natural contarlo.' [1]: 'El nombre efecto inductivo no indica la dirección.' [2]: 'El halógeno parece el protagonista del compuesto.'
13. **[BAJA · REFERENCIA_ROTA]** `theory_blocks[2].body` — 'Lote' es un término interno de producción que no significa nada para el alumno. Además falta el caso del CH$_3$X (carbono sin vecinos de carbono), que no es ni 1.º, 2.º ni 3.º.
   - *Texto actual:* «(otro lote de esta unidad)»
   - *Arreglo:* '(lección de reacciones de sustitución y eliminación de esta unidad)'. Añadir: 'En CH$_3$X el carbono no está unido a ningún otro C (halometano) y suele agruparse con los primarios por su reactividad'.
14. **[BAJA · REFERENCIA_ROTA]** `exercises[3].hints[0]` — La frase se entiende, pero 'correspondiente' salta en el control automático de referencias rotas y es más claro nombrar el prefijo.
   - *Texto actual:* «usa el prefijo multiplicador correspondiente.»
   - *Arreglo:* 'usa el prefijo multiplicador di- y repite el localizador (2,2-).'
15. **[BAJA · LATEX]** `theory_blocks[4].body` — Los grupos van en modo matemático sin \mathrm ($-NO_2$, $-COOH$) y salen en cursiva. Pasa también en flashcards, mcq y exam_questions.
   - *Texto actual:* «$-NO_2 > -CN > -COOH > -X\text{(halógeno)} > -OH$»
   - *Arreglo:* Usar $-\mathrm{NO_2}$, $-\mathrm{COOH}$, $-\mathrm{OH}$ (o texto con subíndices: –NO$_2$).
16. **[BAJA · VISUAL]** `worked_examples[2].assets[0].svg` — La figura escribe los ordinales con el símbolo de grado ('1°', '2°', '3°') en vez de '1.º/2.º/3.º', y la cuña se dibuja como una flecha.
   - *Texto actual:* «1° (primario)»
   - *Arreglo:* Usar '1.º (primario)', etc., y dibujar la cuña como un triángulo relleno.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (3): `common_mistakes[0].why`, `common_mistakes[1].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «El compuesto Cl-CH$_2$-CH$_2$-Cl tiene un cloro en cada uno de sus dos carbonos. **(a)** Nómbralo. **(b)** Clasifica cad \|\| RESP: (a) 1,2-dicloroetano. (b) Ambos son primarios. (…». Arreglo: Añadir full_solution paso a paso.
- [MEDIA · REFERENCIA_ROTA] Frase con referencia rota por sustitución automática de códigos internos ("…correspondiente"): no dice a qué se refiere. (1): `prerequisites[0].statement`. Ej.: «pal, numeración y orden alfabético de sustituyentes ya vistas para los alcanos (el apartado correspondiente de esta unidad)». Arreglo: Reescribir la frase nombrando lo que se refiere (el error, apartado, ejemplo o lección concretos) o eliminar la coletilla.
- [BAJA · PLANTILLA] Texto idéntico repetido en 9 lecciones del curso (probable plantilla genérica). (1): `exam_questions[1].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 05 — Funciones oxigenadas: alcoholes, éteres, aldehídos y cetonas

**Valoración experta: MEDIA.** Teoría clara en nomenclatura básica, pero con un error conceptual repetido (la butanona se presenta como ambigua y se afirma que con ≥4 C la cetona siempre requiere localizador) y carencias de PAU: alcoholes primarios/secundarios/terciarios, elección de la cadena principal con el -OH, punto de ebullición y solubilidad de aldehídos/cetonas, oxidación diferenciadora aldehído/cetona y fenoles. Ejercicios correctos en general pero algunas soluciones flojas (1-metoxipropano sin localizador en la solución, recuento confuso del reto). Dos 'why' de plantilla en common_mistakes. Renderizado sin errores.

**Plan de arreglo:** 1) Corregir el criterio de localizador de cetonas en theory_blocks[3], flashcards[3], exam_questions[0], mcq[3] y guided_exercises[1]. 2) Ampliar teoría: clasificación de alcoholes, cadena principal y prioridad del -OH sobre C=C, Teb y solubilidad de las cuatro funciones, oxidación aldehído/cetona, fenoles. 3) Arreglar soluciones de exercises[0] y del reto, summary.formulas[2] y los dos 'why' genéricos.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `flashcards[3].back` — Afirma que con 4 o más carbonos el localizador de la cetona es obligatorio por ambigüedad. Es falso con el propio criterio de la lección: en la butanona el carbonilo solo puede estar en C2 (C3 es equivalente numerando al revés), así que 'butanona' no es ambigua. Lo correcto es: el localizador sobra cuando no hay ambigüedad (propanona, butanona, ciclohexanona), aunque la IUPAC 2013 recomienda escribirlo siempre (propan-2-ona, butan-2-ona).
   - *Texto actual:* «con 4 o más carbonos, el localizador es obligatorio.»
   - *Arreglo:* Reescribir: «Cuando el carbonilo solo puede ocupar una posición (propanona, butanona): no hay ambigüedad. Aun así, la IUPAC recomienda escribirlo siempre (propan-2-ona, butan-2-ona). A partir de 5 carbonos en cadena lineal (pentan-2-ona/pentan-3-ona) es imprescindible.»
2. **[ALTA · CONCEPTO]** `exam_questions[0].full_solution` — La justificación de (d) dice que con 4 o más carbonos el localizador es obligatorio; la butanona (4 C) tampoco tiene ambigüedad, y las cetonas cíclicas (ciclohexanona) tampoco lo necesitan. La justificación de (b) es circular ('es justo la característica que distingue al éter').
   - *Texto actual:* «con 4 o más carbonos sí es obligatorio.»
   - *Arreglo:* (d) Falsa: si el carbonilo solo puede estar en una posición (propanona, butanona, ciclohexanona) el localizador no aporta información; con 5 o más carbonos en cadena lineal es imprescindible (pentan-2-ona ≠ pentan-3-ona). (b) Verdadera: en nomenclatura sustitutiva el éter no tiene sufijo; se nombra como prefijo alcoxi- (CH3-O-CH2CH3 = metoxietano) o con el nombre radicofuncional 'etil metil éter'.
3. **[MEDIA · CONCEPTO]** `guided_exercises[1].common_errors[1]` — Presenta 'butanona' como error por ambigüedad, pero la butanona no es ambigua (solo existe una butanona lineal). La frase 'ambiguo si la cadena fuera más larga' no tiene sentido para este compuesto.
   - *Texto actual:* «escribir solo 'butanona', ambiguo si la cadena fuera más larga.»
   - *Arreglo:* Sustituir por un error real, p. ej. «Escribir 'butan-3-ona' por numerar desde el extremo equivocado» o «Llamar 'butanal' a (b) confundiendo cetona y aldehído». Si se quiere, añadir: 'butanona' se entiende, pero la IUPAC recomienda butan-2-ona.
4. **[MEDIA · CONCEPTO]** `theory_blocks[3].body` — La regla 'sí necesita localizador … salvo que la cadena sea tan corta que solo exista una posición posible, como en la propanona' sugiere que solo la propanona es la excepción; el ejemplo elegido a continuación (butan-2-ona) es precisamente otro caso sin ambigüedad. Además 'metiletilcetona' no sigue el orden alfabético del nombre radicofuncional (etil metil cetona).
   - *Texto actual:* «salvo que la cadena sea tan corta que solo exista una posición posible, como en la propanona). Ejemplo: butan-2-ona (metiletilcetona)»
   - *Arreglo:* Indicar que propanona y butanona no tienen ambigüedad (IUPAC recomienda igualmente propan-2-ona, butan-2-ona) y poner como ejemplo de localizador imprescindible pentan-2-ona frente a pentan-3-ona. Nombre común: etil metil cetona (MEK).
5. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — Dice que 'esta misma tabla' gobierna la elección del grupo principal, pero la tabla está ordenada alcohol, éter, aldehído, cetona, que no es el orden de prioridad (aldehído > cetona > alcohol > éter). Además anuncia 'la progresión de reactividad' y la tabla no contiene nada sobre reactividad.
   - *Texto actual:* «Fíjate en la progresión de reactividad y de polaridad»
   - *Arreglo:* Reordenar la tabla por prioridad (aldehído, cetona, alcohol, éter) e indicarlo; quitar 'de reactividad' o añadir la columna correspondiente.
6. **[MEDIA · CONCEPTO]** `challenge_questions[0].hints[1]` — La pista dice que el doble enlace 'compense el oxígeno adicional del -OH frente al carbonilo': el alcohol no tiene ningún oxígeno adicional (ambos tienen un O). Lo que compensa el C=C son los 2 H de más del alcohol saturado (C3H8O).
   - *Texto actual:* «de forma que compense el oxígeno adicional del -OH frente al carbonilo.»
   - *Arreglo:* «Un alcohol saturado de 3 C es C3H8O (2 H de más); un doble enlace C=C quita esos 2 H y da C3H6O.»
7. **[MEDIA · CONCEPTO]** `summary.formulas[2]` — 'R en C1' es incorrecto: el carbono C1 es el del grupo -CHO, no R.
   - *Texto actual:* «\text{R-CHO (aldehído, R en C1)}»
   - *Arreglo:* \text{R-CHO (aldehído; el C del -CHO es C1)}
8. **[MEDIA · MCQ]** `mcq[3].options[2].why_wrong` — La explicación del distractor 'Butanal' dice que omite un localizador necesario para una cetona de 4 carbonos: el butanal es otro compuesto (aldehído, CH3CH2CH2CHO) y la butanona no es ambigua. El error real es solo confundir el sufijo (el carbonilo no es terminal).
   - *Texto actual:* «omite el localizador que sí hace falta para una cetona de 4 carbonos.»
   - *Arreglo:* «Butanal es CH3-CH2-CH2-CHO, un aldehído con el carbonilo en el extremo; aquí el carbonilo está entre dos carbonos, así que es una cetona (sufijo -ona).»
9. **[MEDIA · SOLUCION_INCOMPLETA]** `exercises[0].full_solution` — La solución llega a 'metoxipropano' sin localizador, mientras que la respuesta dice '1-metoxipropano'. El localizador es necesario (2-metoxipropano es otro isómero) y la solución no lo justifica.
   - *Texto actual:* «se nombra como prefijo 'metoxi-': metoxipropano.»
   - *Arreglo:* «…se numera la cadena de propano desde el extremo unido al oxígeno: el grupo metoxi queda en C1 → 1-metoxipropano (distinto de 2-metoxipropano, CH3-CH(OCH3)-CH3).»
10. **[MEDIA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — El recuento de hidrógenos del prop-2-en-1-ol no se hace (frase confusa 'el grupo -OH no añade ningún H extra al oxígeno más que el que ya tenía') y se dice que tienen 'una insaturación distinta', cuando ambos tienen exactamente una insaturación (C=O frente a C=C). Fórmulas en cursiva matemática ($C_3H_6O$).
   - *Texto actual:* «el grupo -OH no añade ningún H extra al oxígeno más que el que ya tenía»
   - *Arreglo:* Contar explícitamente: CH2= (2 H) + =CH- (1 H) + -CH2- (2 H) + -OH (1 H) = 6 H → C3H6O. Decir: ambos tienen una insaturación (C=O en el propanal, C=C en el propenol). Mencionar que la propanona (CH3-CO-CH3) también vale. Escribir $\mathrm{C_3H_6O}$ o C$_3$H$_6$O.
11. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — La reactividad menor de las cetonas se justifica solo por impedimento estérico; falta el efecto electrónico (los dos grupos alquilo donan densidad electrónica y hacen menos electrófilo el C carbonílico) y, sobre todo, la diferencia de PAU: los aldehídos se oxidan fácilmente a ácidos (Fehling, Tollens) y las cetonas no.
   - *Texto actual:* «porque el carbono carbonilo de la cetona está más protegido (rodeado de dos cadenas de carbono)»
   - *Arreglo:* Añadir: «…más protegido y menos electrófilo (los grupos alquilo ceden densidad electrónica). Consecuencia práctica: los aldehídos se oxidan con facilidad a ácidos carboxílicos (dan positivo con Fehling y Tollens) y las cetonas no; es la prueba clásica para distinguirlos.»
12. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — No se explica la clasificación de alcoholes en primarios, secundarios y terciarios (clave en PAU para oxidación y deshidratación), ni la regla de que la cadena principal debe contener el carbono que lleva el -OH aunque no sea la más larga, ni que el -OH tiene preferencia sobre dobles y triples enlaces para el localizador (el reto usa prop-2-en-1-ol sin haberlo explicado).
   - *Texto actual:* «Un alcohol lleva el grupo hidroxilo -OH unido a un carbono de la cadena. Se nombra con el sufijo **-ol**»
   - *Arreglo:* Añadir: (1) cadena principal = la que contiene el C del -OH (y después la más larga); (2) el -OH recibe el localizador más bajo, antes que C=C/C≡C: CH2=CH-CH2OH = prop-2-en-1-ol; (3) alcohol primario (C-OH unido a 1 C: propan-1-ol), secundario (2 C: propan-2-ol), terciario (3 C: 2-metilpropan-2-ol).
13. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[0].body` — La teoría compara puntos de ebullición solo de alcohol, éter e hidrocarburo; no dice nada de aldehídos y cetonas (polares, interacciones dipolo-dipolo, punto de ebullición intermedio entre éter y alcohol) ni de la solubilidad en agua (los cuatro grupos aceptan enlaces de hidrógeno del agua; los de cadena corta son solubles), dos preguntas típicas de PAU.
   - *Texto actual:* «los éteres, pese a tener el mismo átomo de oxígeno, apenas se diferencian de un hidrocarburo en este aspecto»
   - *Arreglo:* Añadir un párrafo: orden de Teb para masas parecidas: alcano ≈ éter < aldehído/cetona (dipolo-dipolo) < alcohol (enlace de H); ej. butano −0,5 °C, metoxipropano 39 °C, butanal 75 °C, butan-1-ol 117 °C. Solubilidad: los términos de cadena corta son solubles en agua porque el O acepta enlaces de hidrógeno del agua; disminuye al alargarse la cadena.
14. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica por qué se comete el error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Se generaliza la regla de la cetona: como el aldehído también tiene C=O, se cree que también necesita número; pero el -CHO solo puede estar en C1.»
15. **[MEDIA · PLANTILLA]** `common_mistakes[1].why` — Texto genérico de relleno, idéntico al de common_mistakes[0].
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Como alcoholes (-ol), aldehídos (-al) y cetonas (-ona) tienen sufijo, se supone que el éter también; pero en nomenclatura sustitutiva el éter solo se expresa como prefijo alcoxi-.»
16. **[BAJA · ENUNCIADO]** `exam_questions[1].statement` — Enunciado sin fórmula y que remite a un 'dibujo completo' inexistente; resulta artificial para un examen de PAU.
   - *Texto actual:* «y por qué lo sabes sin necesidad de ver el dibujo completo.»
   - *Arreglo:* Dar la fórmula: «Dado CH3-CO-CH2-CH2-CH2-CH3: (a) ¿aldehído o cetona? Justifícalo. (b) Numera por ambos extremos, elige el localizador y nómbralo.» y quitar la alusión al dibujo.
17. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — No aparecen los fenoles (fenol, C6H5-OH), habituales en la formulación orgánica de PAU, aunque sí se menciona el benzaldehído y el paracetamol (que es un fenol).
   - *Texto actual:* «muchos nombres comunes que no son sistemáticos (paracetamol, colesterol)»
   - *Arreglo:* Añadir una línea: «Si el -OH está unido directamente a un anillo bencénico, el compuesto es un fenol (C6H5-OH, fenol), más ácido que los alcoholes.»
18. **[BAJA · VISUAL]** `theory_blocks[4].assets[0].svg` — La figura solo muestra cuatro cajas con R-OH, R-O-R', R-CHO, R-CO-R' (con apóstrofo recto y mucho espacio vacío debajo); no aporta nada que no esté en la tabla y el pie habla de 'predecir reactividad'.
   - *Texto actual:* «alcohol: R–OH \| éter: R–O–R’ \| aldehído: R–CHO \| cetona: R–CO–R’»
   - *Arreglo:* Sustituir por fórmulas desarrolladas que muestren el C=O terminal (aldehído) frente a interno (cetona) y el O con/sin H, recortando el espacio vacío.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «Nombra el compuesto CH$_3$-CH$_2$-CH(OH)-CH$_3$, cuidando desde qué extremo conviene numerar la cadena. \|\| RESP: Butan-2-ol.». Arreglo: Añadir full_solution paso a paso.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (2): `challenge_questions[0].answer`, `challenge_questions[0].full_solution`. Ej.: «Propanal (CH$_3$CH$_2$CHO) y prop-2-en-1-ol (CH$_2$=CH-CH$_2$OH) son dos ejemplos válidos; ambos son $C_3H_6O$.». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · PLANTILLA] Texto idéntico repetido en 5 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Verdadera. (d) Falsa.». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[0]`. Ej.: «1 punto por cada apartado correctamente calificado y justificado; sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.

#### Lección 06 — Ácidos carboxílicos y ésteres

**Valoración experta: MEDIA.** Nomenclatura de ácidos y ésteres correcta y bien ejemplificada; todos los nombres y ecuaciones verificados son correctos. La teoría tiene una definición imprecisa de éster y le faltan contenidos de PAU: propiedades físicas (dímeros, Teb, solubilidad), neutralización y sales, Ka, catalizador y condiciones de la esterificación e hidrólisis. Algunas justificaciones V/F son mínimas, un 'why' es plantilla y hay remisiones vagas a 'otra parte del curso'. Renderizado sin errores.

**Plan de arreglo:** 1) Corregir la definición de éster (theory_blocks[3]). 2) Añadir propiedades físicas, neutralización/sales con Ka y condiciones de esterificación/hidrólisis con estados de agregación. 3) Arreglar common_mistakes[0].why, mcq[3] opción C, summary.big_idea, flashcards[8], exam_notes[1] y ampliar justificaciones de exam_questions[0].

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `theory_blocks[3].body` — Define el éster diciendo que el -OH del ácido se sustituye por un radical del alcohol; con eso saldría R-CO-R' (una cetona). Lo que se sustituye es el H del -OH por el radical R' (o, equivalentemente, el -OH por el grupo -O-R'). Además, '(manteniendo la raíz y el localizador que tuviera el ácido)' contradice que el -COOH nunca lleve localizador.
   - *Texto actual:* «se forma cuando el -OH del ácido carboxílico se sustituye por un radical procedente de un alcohol: R-COO-R'»
   - *Arreglo:* «…cuando el H del grupo -OH del ácido se sustituye por el radical R' del alcohol (es decir, el -OH se cambia por -O-R'): R-COO-R'.» Cambiar el paréntesis por «(manteniendo la raíz y los localizadores de los sustituyentes que tuviera la cadena del ácido)».
2. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — Faltan las propiedades físicas, pregunta clásica de PAU: los ácidos carboxílicos tienen puntos de ebullición muy altos (forman dímeros por doble enlace de hidrógeno) y los de cadena corta son muy solubles en agua; los ésteres no tienen H unido a O, no forman enlaces de H entre sí y hierven mucho más bajo (son volátiles, de ahí su aroma).
   - *Texto actual:* «Cuando hay dos grupos -COOH en la misma molécula, se nombra como 'ácido...dioico'»
   - *Arreglo:* Añadir un párrafo con Teb comparadas: ácido etanoico 118 °C frente a etanol 78 °C y propanal 49 °C; metanoato de metilo 32 °C frente a su isómero ácido etanoico 118 °C. Explicar dímeros y solubilidad.
3. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — Se explica el carácter ácido pero no la reacción con bases (neutralización) ni el nombre de las sales (etanoato de sodio), habituales en PAU, ni se da ningún dato cuantitativo (Ka del ácido acético ≈ 1,8·10⁻⁵) que conecte con la unidad de ácido-base.
   - *Texto actual:* «son **más ácidos** que un alcohol o que el agua, y son, aun así, **ácidos débiles**»
   - *Arreglo:* Añadir: $\mathrm{CH_3COOH(aq) + H_2O(l) \rightleftharpoons CH_3COO^-(aq) + H_3O^+(aq)}$, $K_a = 1{,}8\cdot10^{-5}$; y $\mathrm{CH_3COOH(aq) + NaOH(aq) \rightarrow CH_3COONa(aq) + H_2O(l)}$ (etanoato de sodio, sal que se nombra igual que el anión '-oato').
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[4].body` — La ecuación de esterificación no indica el catalizador ni las condiciones (ácido sulfúrico concentrado, calor), ni los estados de agregación; tampoco se nombra la reacción inversa (hidrólisis) en la teoría, aunque luego se usa en flashcards y en exam_questions[0](d). Remite a 'otra parte del curso' sin decir cuál.
   - *Texto actual:* «El mecanismo detallado y las condiciones que favorecen uno u otro sentido se estudian con más profundidad en otra parte del curso»
   - *Arreglo:* Escribir $\mathrm{R{-}COOH(l) + R'{-}OH(l) \xrightleftharpoons{H_2SO_4,\ \Delta} R{-}COO{-}R'(l) + H_2O(l)}$; añadir que el sentido inverso es la hidrólisis del éster (y en medio básico, saponificación) y remitir a «la lección de Esterificación de esta unidad».
5. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica el origen del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Se asocia la palabra 'ácido' con los ácidos minerales (HCl, H2SO4) que se disocian por completo, sin pensar en el grado de disociación.»
6. **[BAJA · CONCEPTO]** `summary.big_idea` — Llama al ácido carboxílico 'el grupo oxigenado más reactivo de los vistos hasta ahora'; no es cierto en general (los aldehídos son más reactivos frente a nucleófilos y oxidantes). Lo que es el ácido es el más oxidado y el más ácido. La misma idea aparece en challenge_questions[0].full_solution ('más complejo y más reactivo').
   - *Texto actual:* «es el grupo oxigenado más reactivo de los vistos hasta ahora»
   - *Arreglo:* «…es el grupo oxigenado más oxidado y el único claramente ácido de los vistos hasta ahora…»
7. **[BAJA · CONCEPTO]** `flashcards[8].back` — Frase confusa: dice que el -OH 'forma parte de un grupo carbonilo adyacente'; el -OH no forma parte del carbonilo, está unido al mismo carbono que el C=O.
   - *Texto actual:* «forma parte de un grupo carbonilo adyacente que lo estabiliza»
   - *Arreglo:* «…está unido al mismo carbono que el C=O y juntos forman un grupo distinto (-COOH) con propiedades propias; en la escala de prioridad, el ácido va por encima del alcohol.»
8. **[BAJA · CONCEPTO]** `exercises[1].hints[0]` — La pista ya da la respuesta completa (agua ≈ etanol, el ácido forma un ion más estable): el ejercicio deja de ser ejercicio.
   - *Texto actual:* «El agua y el etanol ceden su H con una facilidad parecida, muy baja; el ácido carboxílico forma un ion mucho más estable al cederlo.»
   - *Arreglo:* «Compara cómo queda repartida la carga negativa en el ion que se forma en cada caso (OH⁻, CH3CH2O⁻, CH3COO⁻).»
9. **[BAJA · MCQ]** `mcq[3].options[2].why_wrong` — La razón dada es falsa como regla general: una sola molécula sí puede perder agua (p. ej. la deshidratación de un alcohol). La justificación correcta es experimental (marcaje isotópico con ¹⁸O: el O del alcohol acaba en el éster) y estructural (el -OH sale del ácido y el H del alcohol).
   - *Texto actual:* «El agua no puede formarse con átomos de una sola molécula; necesita aportaciones de ambas.»
   - *Arreglo:* «En la esterificación el ácido aporta el -OH y el alcohol el H; si se marca el O del alcohol con ¹⁸O, ese oxígeno aparece en el éster, no en el agua.»
10. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[0].full_solution` — Las justificaciones de (b) y (c) son mínimas: (b) no explica por qué el C del -COOH es siempre terminal; (c) solo dice 'tiene siempre dos partes' sin un ejemplo. Con el propio criterio de 'sin justificación, 0 puntos' no darían la nota completa.
   - *Texto actual:* «(c) Verdadera: el nombre de un éster tiene siempre dos partes.»
   - *Arreglo:* (b) «…su carbono tiene ya tres enlaces con oxígenos (C=O y C-OH) y solo le queda uno para unirse a la cadena, así que es terminal: C1.» (c) «…'…oato' indica el ácido y 'de …ilo' el alcohol: etanoato de etilo procede de ácido etanoico + etanol.»
11. **[BAJA · LATEX]** `worked_examples[2].solution` — Las ecuaciones químicas de la lección (worked_examples[2], guided_exercises[1], exam_questions[1], theory_blocks[4]) no llevan estados de agregación ni catalizador, en contra de la convención del curso.
   - *Texto actual:* «\text{CH}_3\text{CH}_2\text{COOH} + \text{CH}_3\text{OH} \rightleftharpoons»
   - *Arreglo:* Añadir (l) a cada especie y H$_2$SO$_4$/calor sobre la flecha en todas las ecuaciones de esterificación.
12. **[BAJA · VISUAL]** `exam_notes[1]` — La nota es solo una cadena de desigualdades sin texto ni contexto.
   - *Texto actual:* «agua ≈ alcohol < ácido carboxílico < ácido mineral fuerte»
   - *Arreglo:* «Orden de acidez que conviene saber justificar: agua ≈ alcohol < ácido carboxílico (débil, Ka ≈ 10⁻⁵) < ácido mineral fuerte (HCl, disociación total).»
13. **[BAJA · ERRATA]** `theory_blocks[0].body` — Inciso abierto con raya que no se cierra, y remisión vaga a 'otra parte del curso'. Además la secuencia alcohol→aldehído→ácido solo vale para alcoholes primarios (los secundarios dan cetonas), y no se dice.
   - *Texto actual:* «No hace falta memorizar esa cadena de transformaciones —se trabajará en otra parte del curso, pero conviene»
   - *Arreglo:* «…de un carbono terminal (alcohol primario → aldehído → ácido; un alcohol secundario da una cetona). No hace falta memorizarla ahora —se trabajará en la lección de oxidación y reducción orgánica—, pero conviene…»

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[0].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (1): `guided_exercises[1]`. Ej.: «Escribe la ecuación de esterificación entre el ácido metanoico y el propan-1-ol, y nombra el éster resultante. \|\| RESP: $\text{HCOOH} + \text{CH}_3\text{CH}_2\text{CH}_2\text{OH}…». Arreglo: Añadir full_solution paso a paso.
- [BAJA · PLANTILLA] Texto idéntico repetido en 5 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Verdadera. (d) Falsa.». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[0]`. Ej.: «1 punto por cada apartado correctamente calificado y justificado; sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.

#### Lección 07 — Aminas, amidas y nitrilos

**Valoración experta: MEDIA.** Nombres, recuentos y claves de test correctos (propanamida, butanonitrilo, pentanonitrilo, metanamida, C2H5NO verificados). La teoría de aminas es insuficiente: no enseña a nombrar aminas secundarias y terciarias (aunque los ejercicios lo exigen) ni su basicidad y propiedades físicas; faltan amidas N-sustituidas y el prefijo ciano-. El reto final está mal planteado (afirmación falsa o trivial con solución circular). Hay dos 'why' de plantilla y errores menores (Teb de nitrilos, errata en una ficha). Renderizado sin errores.

**Plan de arreglo:** 1) Ampliar theory_blocks[1] con nomenclatura de aminas 1ª/2ª/3ª (tradicional y N-sustituida), basicidad con ecuación y propiedades físicas. 2) Añadir amidas N-sustituidas y prefijo ciano-; corregir Teb de nitrilos. 3) Reformular el reto con cálculo de insaturaciones. 4) Reescribir los dos 'why' genéricos y la errata de flashcards[6].

**Hallazgos de la revisión experta:**

1. **[ALTA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — La teoría solo dice 'sufijo -amina' y da como único ejemplo una diamina; no explica cómo se nombran las aminas primarias con localizador (propan-1-amina), ni las secundarias y terciarias (radicales en orden alfabético + 'amina': etilmetilamina, trimetilamina; o sustitutiva con N-: N-metiletanamina, N,N-dimetilmetanamina). Sin embargo los ejercicios piden exactamente esos nombres (worked_examples[0] 'etilmetilamina', guided_exercises[0] 'trimetilamina', exercises[1] 'dimetilamina').
   - *Texto actual:* «Una amina se nombra con el sufijo **-amina** (si el grupo es el principal) o con el prefijo **amino-** (…). Ejemplo real: la etano-1,2-diamina (etilendiamina).»
   - *Arreglo:* Añadir: (1) primarias: raíz + localizador + -amina (CH3CH2CH2NH2 = propan-1-amina) o radical + amina (propilamina); (2) secundarias/terciarias: radicales por orden alfabético + 'amina' (CH3-NH-CH2CH3 = etilmetilamina; (CH3)3N = trimetilamina) o, en sustitutiva, cadena más larga como base y los demás radicales con 'N-' (N-metiletanamina, N,N-dimetilmetanamina).
2. **[MEDIA · CONCEPTO]** `challenge_questions[0].full_solution` — El reto pide demostrar que una amina 'sin ningún grupo carbonilo' no puede tener fórmula C2H5NO, y la solución es circular: como una amina simple no tiene O, no puede ser amina. No es cierto en general: C2H5NO tiene 1 insaturación y admite estructuras con grupo amino sin carbonilo (p. ej. oxiran-2-amina, un anillo con éter + NH2, o el enol 2-aminoetenol), y con carbonilo existe el aminoetanal (H2N-CH2-CHO), que también es amina. La raya del inciso '—como el carbonilo de la amida,' no se cierra.
   - *Texto actual:* «la presencia de ese oxígeno en la fórmula C$_2$H$_5$NO ya descarta, por sí sola, que se trate de una amina simple sin más grupos.»
   - *Arreglo:* Reformular el reto como cálculo de insaturaciones: «C2H5NO: insaturaciones = (2·2+2+1−5)/2 = 1. Una amina saturada con un O (amino-alcohol o amino-éter de cadena abierta) sería C2H7NO; para quitar 2 H hace falta un C=O, un C=C o un anillo. Por eso, una opción estable es la amida (etanamida) o el aminoetanal; una amina saturada de cadena abierta no puede tener esa fórmula.» Cerrar el inciso.
3. **[MEDIA · ENUNCIADO]** `challenge_questions[0].statement` — La pregunta pide justificar algo que es falso tal como está formulado (que ninguna amina sin carbonilo pueda tener fórmula C2H5NO) o, si se entiende 'amina simple', es trivial porque no lleva O. No aporta el nivel de reto previsto (dificultad 4).
   - *Texto actual:* «explica razonadamente por qué no podría tratarse de una amina con esa misma fórmula molecular (sin ningún grupo carbonilo).»
   - *Arreglo:* «…explica por qué no puede ser una amina saturada de cadena abierta con un grupo -OH (amino-alcohol), calculando el número de insaturaciones; propón otro isómero con un grupo amino (p. ej. aminoetanal) y nómbralo.»
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — No se explica en el bloque de aminas su carácter básico (análogo al NH3) ni su reacción con agua y con ácidos, ni sus propiedades físicas (enlace de H N-H···N más débil que O-H···O: Teb menor que la del alcohol análogo; terciarias sin enlace de H entre sí). La basicidad solo aparece de pasada en el bloque de amidas, pero se pregunta en exercises[0] y worked_examples[2].
   - *Texto actual:* «Las aminas son compuestos muy extendidos, tanto en la naturaleza como en la industria farmacéutica»
   - *Arreglo:* Añadir: «Como el NH3, el N tiene un par libre que acepta H⁺: $\mathrm{CH_3NH_2(aq) + H_2O(l) \rightleftharpoons CH_3NH_3^+(aq) + OH^-(aq)}$; con HCl forman sales (cloruro de metilamonio). Teb: propan-1-amina 48 °C < propan-1-ol 97 °C (el enlace de H N-H···N es más débil); la trimetilamina (3 °C) no forma enlaces de H entre sus moléculas.»
5. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Se usa la misma terminología primario/secundario/terciario que en alcoholes y halogenuros, donde el criterio mira el carbono, y se aplica sin cambiarlo al nitrógeno.»
6. **[MEDIA · PLANTILLA]** `common_mistakes[1].why` — Texto genérico de relleno, igual que common_mistakes[0].why.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Ambas tienen N con H unidos y nombres casi iguales, y se olvida que el C=O vecino deslocaliza el par libre del N.»
7. **[BAJA · CONCEPTO]** `theory_blocks[3].body` — Afirma que los nitrilos hierven por encima de los alcoholes de tamaño comparable; los datos dan valores prácticamente iguales: acetonitrilo 82 °C frente a etanol 78 °C, propanonitrilo 97 °C frente a propan-1-ol 97 °C, butanonitrilo 117 °C frente a butan-1-ol 118 °C. Falta además el prefijo 'ciano-' (nitrilo como sustituyente), que se necesita en la lección de compuestos polifuncionales.
   - *Texto actual:* «los nitrilos suelen ser líquidos con puntos de ebullición más altos que los alcoholes de tamaño comparable.»
   - *Arreglo:* «…con puntos de ebullición altos, comparables a los de los alcoholes de tamaño parecido (acetonitrilo 82 °C, etanol 78 °C), aunque no forman enlaces de hidrógeno entre sí: se debe a su gran polaridad (momento dipolar elevado del C≡N).» Añadir: «Cuando no es el grupo principal se nombra con el prefijo ciano-.»
8. **[BAJA · CONCEPTO]** `theory_blocks[0].body` — Dice que el oxígeno formaba dos enlaces a carbono solo en el éter y uno 'en el resto'; en el éster el oxígeno -O- también está unido a dos carbonos (R-CO-O-R').
   - *Texto actual:* «siempre formaba como máximo dos enlaces a carbono (el éter) o uno (el resto)»
   - *Arreglo:* «…como máximo dos enlaces a carbono (en éteres y en el O puente de los ésteres) …»
9. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[0].full_solution` — La justificación de (b) es solo 'es el criterio que distingue…', sin ejemplo; con el criterio de 'sin justificación, 0 puntos' no basta.
   - *Texto actual:* «(b) Verdadera: es el criterio que distingue la clasificación de las aminas de la de los alcoholes.»
   - *Arreglo:* «(b) Verdadera: se cuentan los radicales unidos al N; p. ej. CH3-NH-CH3 tiene dos radicales sobre el N → secundaria, aunque cada C esté unido solo al N.»
10. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — No se explican las amidas N-sustituidas (N-metiletanamida, N,N-dimetilmetanamida), frecuentes en formulación de PAU, ni que el nombre se forma quitando la palabra 'ácido'; tampoco sus propiedades físicas (Teb y puntos de fusión muy altos por enlaces de H; la metanamida es líquida y la etanamida sólida).
   - *Texto actual:* «Se nombra con el sufijo **-amida**, sustituyendo la terminación '-oico' que tendría el ácido carboxílico»
   - *Arreglo:* «Se suprime 'ácido' y '-oico' pasa a '-amida' (ácido etanoico → etanamida). Si el N lleva radicales, se indican con N-: CH3-CO-NH-CH3 = N-metiletanamida.» Añadir una línea sobre enlaces de H y Teb altos.
11. **[BAJA · ERRATA]** `flashcards[6].front` — Palabra duplicada 'un nitrilo -nitrilo'.
   - *Texto actual:* «¿Qué ácido carboxílico se obtiene al convertir un nitrilo -nitrilo de n carbonos?»
   - *Arreglo:* «¿Qué ácido carboxílico se obtiene al hidrolizar un nitrilo de n carbonos (contando el del -CN)?»

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «Clasifica estas dos aminas y nómbralas: **(a)** CH$_3$-CH$_2$-NH$_2$; **(b)** (CH$_3$)$_3$N. \|\| RESP: (a) Amina primaria: etilamina (etanamina). (b) Amina terciaria: trimetilamin…». Arreglo: Añadir full_solution paso a paso.
- [BAJA · PLANTILLA] Texto idéntico repetido en 8 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[0]`. Ej.: «1 punto por cada apartado correctamente calificado y justificado; sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.

#### Lección 08 — Compuestos polifuncionales y prioridad de grupos funcionales

**Valoración experta: MEDIA.** Todos los nombres de ejemplos y ejercicios son correctos (4-hidroxibutanal, 4-oxopentanoato de metilo, 2-aminoetanol, 4-hidroxibutanonitrilo, 3-oxobutanamida, ácido 3-metoxipropanoico, 4-aminobutanal, ácido 3-aminobutanoico, ácido 2-amino-3-hidroxipropanoico) y la escala de prioridad es la habitual. La teoría falla en los criterios de cadena principal y numeración (no hay nada sobre dobles/triples enlaces en polifuncionales), presenta prefijos nuevos (oxo-, ciano-, carboxi-…) sin explicarlos y no trata los multiplicadores en el orden alfabético. Un test tiene dos opciones defendibles (glicina), la figura tiene etiquetas tachadas por las flechas y hay erratas menores y un 'why' de plantilla.

**Plan de arreglo:** 1) Reescribir los pasos 3-4 del procedimiento con los criterios de cadena/numeración incluyendo enlaces múltiples, con ejemplos. 2) Explicar cada prefijo de la tabla con un ejemplo y la regla de los multiplicadores. 3) Cambiar el distractor B de mcq[1]. 4) Rehacer la figura del ácido láctico. 5) Corregir erratas (rayas abiertas, mcq[2] sin formato) y common_mistakes[1].why.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `theory_blocks[2].body` — Los criterios de elección y numeración de la cadena están incompletos o mal: (paso 3) 'a ser posible, el mayor número de los demás grupos presentes' no es el criterio IUPAC; tras contener el máximo número de grupos principales se atiende a los dobles/triples enlaces y a la longitud (o, según la IUPAC 2013, primero la longitud); (paso 4) después del grupo principal se da el localizador más bajo a los enlaces múltiples y solo después a los prefijos. La lección no menciona en ningún sitio los dobles y triples enlaces en compuestos polifuncionales (but-3-en-2-ol, ácido propenoico), muy frecuentes en PAU.
   - *Texto actual:* «3. **Elegir la cadena principal**: debe contener el grupo principal, y a ser posible, el mayor número de los demás grupos presentes.»
   - *Arreglo:* Paso 3: «La cadena principal contiene el mayor número posible de grupos principales; en caso de empate, el mayor número de dobles y triples enlaces; después, la más larga.» Paso 4: «Localizadores más bajos: 1.º al grupo principal; 2.º a los enlaces múltiples (dobles antes que triples si hay empate); 3.º al conjunto de prefijos.» Añadir un ejemplo: CH2=CH-CH(OH)-CH3 = but-3-en-2-ol; CH2=CH-COOH = ácido propenoico.
2. **[MEDIA · MCQ]** `mcq[1].options[1].why_wrong` — La opción B ('Ácido aminoetanoico') se da por incorrecta 'porque falta el localizador', pero la propia explicación admite que solo hay una posición posible; la IUPAC acepta omitir localizadores cuando no hay ambigüedad (el nombre IUPAC preferido de la glicina es ácido aminoacético, sin localizador). Hay, por tanto, dos opciones defendibles (B y D). Además es incoherente con worked_examples[2], donde '2-aminoetanol' omite el localizador 1 del -OH.
   - *Texto actual:* «Falta el localizador del prefijo; aunque en este caso solo hay una posición posible por ser una cadena muy corta, conviene expresarlo con el número.»
   - *Arreglo:* Cambiar la opción B por un distractor claramente erróneo, p. ej. «Ácido 1-aminoetanoico» (el C1 es el del -COOH y no puede llevar el amino) o «2-carboxietanamina» (toma la amina como principal).
3. **[MEDIA · TEORIA_INCOMPLETA]** `prerequisites[0].why_it_matters` — Afirma que la lección no añade ningún prefijo nuevo y que todos se conocen de las lecciones anteriores, pero los prefijos oxo-, carboxi-, carbamoil-, ciano-, alcoxicarbonil- y aciloxi- no se enseñan en las lecciones 05-07 (hidroxi- solo aparece de pasada en el reto de la 06). En la teoría de esta lección solo figuran en la tabla, sin explicar qué significa cada uno (p. ej. que oxo- es un =O sobre un carbono de la cadena, tanto para cetona como para aldehído terminal).
   - *Texto actual:* «Nombrar un compuesto polifuncional no añade ningún sufijo o prefijo nuevo: combina los que ya se conocen de las tres lecciones anteriores»
   - *Arreglo:* Corregir la frase y añadir en theory_blocks[1] un párrafo que explique los prefijos con un ejemplo cada uno: hidroxi- (-OH), oxo- (=O en un C de la cadena: 4-oxopentanoato de metilo), amino-, ciano- (-CN fuera de la cadena: ácido 3-cianopropanoico), carboxi-, alcoxi-.
4. **[MEDIA · PLANTILLA]** `common_mistakes[1].why` — Texto genérico de relleno.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Se cree que, como el sufijo ya 'manda', los grupos de menor prioridad no hace falta nombrarlos; pero siguen formando parte de la molécula y deben aparecer como prefijos.»
5. **[MEDIA · VISUAL]** `theory_blocks[3].assets[0].svg` — En la figura del ácido láctico las flechas se cruzan con el texto: la flecha del C2 atraviesa la etiqueta 'C2: -OH' (se lee 'C2: \|OH') y la del C1 corta 'grupo principal'. Además 'acido...oico' aparece sin tilde.
   - *Texto actual:* «C2: -OH (tachado por la flecha) \| C1: grupo principal \| sufijo: acido...oico»
   - *Arreglo:* Separar las etiquetas de las flechas (etiqueta al lado, flecha desde el borde de la etiqueta hasta el átomo) y escribir 'sufijo: ácido …-oico'.
6. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — La tabla presenta éter (9) y halógenos (10) como si la IUPAC les asignara un puesto en la escala; en realidad la IUPAC no los incluye entre los grupos que pueden ser principales (solo se citan como prefijos). Tampoco aparecen los dobles/triples enlaces, que muchos libros de PAU sitúan en esa misma lista.
   - *Texto actual:* «\| 9 \| Éter \| (nunca sufijo) \| alcoxi- \|»
   - *Arreglo:* Separar las dos últimas filas con una nota: «Grupos que solo se nombran como prefijo (no compiten por el sufijo): éter (alcoxi-), halógenos (fluoro-, cloro-…), radicales alquilo». Mencionar los enlaces dobles/triples (-en/-ino) y su papel en la numeración.
7. **[BAJA · CONCEPTO]** `theory_blocks[0].body` — La adrenalina no tiene 'un alcohol' sino un alcohol secundario y dos -OH fenólicos (catecol); el ejemplo induce a pensar que solo tiene un -OH.
   - *Texto actual:* «la adrenalina combina un alcohol, una amina y un anillo aromático»
   - *Arreglo:* «la adrenalina combina un alcohol, una amina (secundaria) y un anillo aromático con dos grupos -OH (fenol)».
8. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — El orden alfabético de prefijos no aclara que los multiplicadores (di-, tri-) no cuentan al ordenar (etil antes que dimetil), dato muy preguntado; tampoco se da ningún ejemplo resuelto con dos prefijos (solo el reto de la serina).
   - *Texto actual:* «5. **Nombrar los grupos restantes como prefijos**, cada uno con su propio localizador, ordenados alfabéticamente entre sí.»
   - *Arreglo:* Añadir: «Los prefijos multiplicadores di-, tri- no cuentan para el orden alfabético: 3-etil-2,2-dimetil…, no 2,2-dimetil-3-etil…». Añadir un ejemplo resuelto con dos prefijos, p. ej. ácido 2-amino-3-hidroxipropanoico o 4-cloro-3-hidroxibutanal.
9. **[BAJA · LATEX]** `mcq[2].options[2].why_wrong` — Fórmula sin subíndices y flecha ASCII '->'.
   - *Texto actual:* «(CH3-CO-CH2-CO-NH2 -> 3-oxobutanamida)»
   - *Arreglo:* (CH$_3$-CO-CH$_2$-CO-NH$_2$ → 3-oxobutanamida)
10. **[BAJA · ERRATA]** `challenge_questions[0].full_solution` — Inciso con raya abierta que no se cierra, y los grupos se enumeran en orden 1, 8, 7 aunque la pista pide ordenarlos de mayor a menor prioridad.
   - *Texto actual:* «De los tres grupos presentes —ácido carboxílico (prioridad 1), amina (prioridad 8) y alcohol (prioridad 7), el de mayor prioridad»
   - *Arreglo:* «De los tres grupos presentes —ácido carboxílico (prioridad 1), alcohol (7) y amina (8)—, el de mayor prioridad…»
11. **[BAJA · ERRATA]** `mcq[3].options[0].why_wrong` — Inciso con raya que no se cierra.
   - *Texto actual:* «—esa escala ya se usó para elegir el sufijo, sino por el orden alfabético.»
   - *Arreglo:* «El orden de los prefijos no se decide por la escala de prioridad —esa escala ya se usó para elegir el sufijo—, sino por el orden alfabético.»

**Chequeos automáticos:**

- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «Nombra el compuesto HO-CH$_2$-CH$_2$-CH$_2$-C$\equiv$N, que combina un nitrilo y un alcohol. \|\| RESP: 4-hidroxibutanonitrilo.». Arreglo: Añadir full_solution paso a paso.
- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 8 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[0]`. Ej.: «1 punto por cada apartado correctamente calificado y justificado; sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.

#### Lección 09 — Isomería de cadena

**Valoración experta: MEDIA.** Teoría clara y bien orientada (definición, procedimiento sistemático, ejemplos), pero con dos errores graves de nomenclatura idénticos (guided_exercises[1] y mcq[4]): llaman 3-metilpentano al 2-metilpentano y concluyen que son la misma molécula. La figura de alcoholes C5H12O omite uno de los cuatro isómeros, el ejemplo 2 mezcla 'tres' y 'cuatro', el dato de 'miles de isómeros con 10 C' es falso y el caso límite de ésteres confunde. Falta teoría sobre equivalencias por simetría, uso de radicales etilo y relación ramificación–punto de ebullición (que se pregunta en examen).

**Plan de arreglo:** 1) Corregir guided_exercises[1] y mcq[4] (2-metilpentano vs 3-metilpentano → isómeros de cadena; clave A). 2) Añadir 2-metilbutan-1-ol a la figura y unificar 'cuatro' en WE2. 3) Corregir dato de C10 (75 isómeros). 4) Completar WE3 con los 5 isómeros del hexano y la full_solution del guiado 1 y 2. 5) Ampliar teoría: simetría, radicales mayores, ramificación vs Teb; rehacer el caso límite de ésteres.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `guided_exercises[1].answer` — Nomenclatura errónea: CH3-CH(CH3)-CH2-CH2-CH3 es 2-metilpentano (metilo en C2 numerando por la izquierda; por la derecha quedaría en C4), no 3-metilpentano. Las dos estructuras propuestas son 3-metilpentano y 2-metilpentano: SÍ son isómeros de cadena (C6H14 ambos). La lección enseña justo lo contrario.
   - *Texto actual:* «(a) Las dos se nombran 3-metilpentano. (b) No son isómeros: son la misma molécula»
   - *Arreglo:* (a) CH$_3$-CH$_2$-CH(CH$_3$)-CH$_2$-CH$_3$: 3-metilpentano; CH$_3$-CH(CH$_3$)-CH$_2$-CH$_2$-CH$_3$: 2-metilpentano (por el otro extremo sería 4-metil, mayor). (b) Ambas son C$_6$H$_{14}$ con distinto esqueleto (metilo en C3 frente a C2): son isómeros de cadena. Si se quiere mantener el objetivo 'misma molécula escrita al revés', cambiar la 2.ª estructura por CH$_3$-CH$_2$-CH$_2$-CH(CH$_3$)-CH$_3$ (= 2-metilpentano escrito al revés) frente a CH$_3$-CH(CH$_3$)-CH$_2$-CH$_2$-CH$_3$.
2. **[ALTA · CONCEPTO]** `guided_exercises[1].common_errors[0]` — El error típico descrito ('contarlas como dos isómeros') es en realidad la respuesta correcta para estas dos estructuras (2-metilpentano y 3-metilpentano).
   - *Texto actual:* «Contarlas como dos isómeros de cadena distintos solo por estar escritas en sentidos opuestos»
   - *Arreglo:* Reescribir acorde con la corrección del enunciado/answer (p. ej. 'Nombrar 3-metilpentano la segunda estructura por no probar a numerar desde el otro extremo / no ver que el metilo está en C2').
3. **[ALTA · MCQ]** `mcq[4].correct` — Clave incorrecta. CH3-CH2-CH(CH3)-CH2-CH3 es 3-metilpentano y CH3-CH(CH3)-CH2-CH2-CH3 es 2-metilpentano: son isómeros de cadena. La opción correcta es A, no C. La explicación y los why_wrong de A y D afirman algo falso ('renumerando... el metilo también queda en el C3').
   - *Texto actual:* «correct = C; A.why_wrong: 'Renumerando la segunda estructura por el otro extremo, el metilo también queda en el C3'»
   - *Arreglo:* Poner correct = A; why_wrong de A = None; C.why_wrong: 'La 2.ª estructura renumerada por el otro extremo daría 4-metil, no 3-metil: es 2-metilpentano, otra molécula'; explicación: 'La primera es 3-metilpentano y la segunda 2-metilpentano: misma fórmula C$_6$H$_{14}$, distinto esqueleto → isómeros de cadena'. Alternativa: cambiar la 2.ª estructura del enunciado por CH$_3$-CH$_2$-CH(CH$_3$)-CH$_2$-CH$_3$ escrita de otra forma si se quiere conservar la clave C.
4. **[MEDIA · CONCEPTO]** `worked_examples[2].interpretation` — Dato falso: con 10 carbonos hay 75 isómeros estructurales de alcano (C10H22), no miles. Se llega a los miles hacia C14 (1858) y C15 (4347).
   - *Texto actual:* «a partir de unos 10 carbonos, el número de isómeros de cadena posibles se cuenta ya por miles»
   - *Arreglo:* 'el decano (C$_{10}$H$_{22}$) tiene ya 75 isómeros, el C$_{15}$H$_{32}$ más de 4000 y el C$_{20}$H$_{42}$ más de 366 000'.
5. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — El ejemplo 'límite' es confuso: metanoato de propilo y etanoato de etilo no son isómeros de cadena (la cadena carbonada no es continua a través del -COO-); en los textos de Bachillerato se clasifican como isomería de posición (del grupo éster) o metamería. Presentarlo como dudoso entre cadena y posición enseña ambigüedad innecesaria en la lección que define la isomería de cadena.
   - *Texto actual:* «algunos materiales los clasifican como isomería de posición en vez de cadena»
   - *Arreglo:* Sustituir por un caso límite real o reescribir: 'metanoato de propilo y etanoato de etilo (C$_4$H$_8$O$_2$) no son isómeros de cadena: lo que cambia es dónde se sitúa el grupo -COO- dentro del esqueleto; se consideran isómeros de posición (metámeros)'. Un buen caso para comparar: metanoato de propilo vs metanoato de isopropilo (1-metiletilo), que sí difieren solo en la ramificación (cadena).
6. **[MEDIA · ENUNCIADO]** `theory_blocks[3].assets[0].svg` — La figura muestra solo tres alcoholes (pentan-1-ol, 3-metilbutan-1-ol, 2,2-dimetilpropan-1-ol); falta el 2-metilbutan-1-ol, aunque el pie de figura y el texto hablan de cuatro isómeros.
   - *Texto actual:* «caption: 'Los cuatro isómeros de cadena de un alcohol de fórmula C$_5$H$_{12}$O' (la figura tiene 3 recuadros)»
   - *Arreglo:* Añadir un cuarto recuadro: 2-metilbutan-1-ol, HOCH$_2$-CH(CH$_3$)-CH$_2$-CH$_3$, 1 ramificación.
7. **[MEDIA · INSTRUCCIONES_EN_VEZ_DE_SOLUCION]** `guided_exercises[0].full_solution` — La 'solución' copia literalmente las pistas ('sigue el procedimiento…', 'cuenta los H…') en vez de hacerlo; no muestra el recuento de H del apartado (c).
   - *Texto actual:* «Procedimiento: Para (a), sigue el procedimiento de la teoría: acorta la cadena principal… Para (c), cuenta los H de cada carbono…»
   - *Arreglo:* (a) Cadena de 3 C con el 4.º C como metilo en C2: CH$_3$-CH(CH$_3$)-CH$_3$. (b) 2-metilpropano. (c) H: 3+1+3+3=10 → C$_4$H$_{10}$; butano: 3+2+2+3=10 → C$_4$H$_{10}$. Mismo C y H, distinto esqueleto: isómeros de cadena.
8. **[MEDIA · SOLUCION_AUSENTE]** `guided_exercises[1]` — El ejercicio guiado no tiene full_solution (solo answer), a diferencia del guiado anterior; falta la numeración razonada por ambos extremos.
   - *Texto actual:* «claves: answer, common_errors, hints (sin full_solution)»
   - *Arreglo:* Añadir full_solution: numerar cada cadena por los dos extremos, indicar localizadores (3/3 en la 1.ª; 2/4 en la 2.ª), nombrar y concluir que son isómeros de cadena C$_6$H$_{14}$.
9. **[MEDIA · SOLUCION_INCOMPLETA]** `worked_examples[2].reasoning[1]` — El recuento de 5 isómeros no se justifica: 'se pueden distribuir de varias formas distintas' y 'se puede comprobar dibujando' sin decir cuáles son; no se nombran los isómeros ni se explica por qué no hay más (etilo en C3 alargaría la cadena, etc.).
   - *Texto actual:* «cadena de 4 con 2 metilos, que se pueden distribuir de varias formas distintas sobre los 2 carbonos centrales»
   - *Arreglo:* Enumerar: hexano; 2-metilpentano; 3-metilpentano; 2,2-dimetilbutano; 2,3-dimetilbutano (exactamente 2 formas con cadena de 4). Indicar que 3,3-dimetil = 2,2-dimetil renumerado y que un etilo sobre butano daría 3-metilpentano.
10. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — El procedimiento no explica dos claves que el alumno necesita: (1) posiciones equivalentes por simetría (metilo en C2 ≡ C4 del pentano), que se descartan; (2) cuándo se puede usar un etilo u otro radical mayor (un etilo en C2 alarga la cadena; solo es válido a partir del C3 de una cadena de 5, p. ej. 3-etilpentano en C7H16). El paso 3 ('sigue acortando… hasta que ya no queden carbonos suficientes para que la cadena principal tenga sentido') es vago.
   - *Texto actual:* «Sigue acortando la cadena principal y añadiendo más ramificaciones, hasta que ya no queden carbonos suficientes para que la cadena principal tenga sentido como tal.»
   - *Arreglo:* Añadir: 'Las posiciones simétricas (C2 y C4 de una cadena de 5) dan el mismo compuesto. Un radical de n carbonos solo puede ir en un carbono que diste al menos n+1 posiciones de cada extremo (un etilo nunca en C2). Parar cuando la cadena principal ya no sea la más larga posible.'
11. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[0].body` — exam_questions[0](c) pide justificar por qué los isómeros de C5H12 tienen distintos puntos de ebullición, pero la teoría no explica en ningún bloque la relación ramificación → menor superficie de contacto → menores fuerzas de London → menor Teb.
   - *Texto actual:* «existen compuestos distintos -con propiedades físicas y químicas distintas-»
   - *Arreglo:* Añadir un párrafo (o bloque) con la idea y datos: pentano 36 °C, 2-metilbutano 28 °C, 2,2-dimetilpropano 9,5 °C; más ramificación → forma más esférica → menos contacto → menos fuerzas de dispersión → menor Teb.
12. **[MEDIA · ERRATA]** `worked_examples[1].unknowns[0]` — Incoherencia 3/4: el enunciado pide cuatro isómeros, pero las incógnitas, la comprobación y la interpretación hablan de 'tres' esqueletos/estructuras.
   - *Texto actual:* «Los tres esqueletos posibles. / 'que las tres estructuras tienen la misma fórmula... 12 en los tres casos' / 'en los tres casos'»
   - *Arreglo:* Cambiar a 'Los cuatro isómeros (tres esqueletos distintos: lineal, con un metilo y con dos metilos)' y en reasoning[3] e interpretation 'las cuatro estructuras… en los cuatro casos'.
13. **[BAJA · ENUNCIADO]** `exercises[0].statement` — Pide 'los dos isómeros de cadena del 1-bromobutano' y la respuesta incluye al propio 1-bromobutano; un compuesto no es isómero de sí mismo. Además, la solución no menciona que el 1-bromo-2-metilpropano es el único isómero de cadena con Br terminal.
   - *Texto actual:* «Escribe y nombra los dos isómeros de cadena del 1-bromobutano (C$_4$H$_9$Br) que conservan el bromo en un carbono extremo»
   - *Arreglo:* 'Escribe y nombra los dos bromoalcanos de fórmula C$_4$H$_9$Br con el Br en un carbono terminal y explica por qué son isómeros de cadena entre sí'.
14. **[BAJA · SOLUCION_INCOMPLETA]** `worked_examples[1].reasoning[3]` — Afirma que hay 12 H 'en los tres casos' sin mostrar el recuento ni incluir el cuarto isómero.
   - *Texto actual:* «Se comprueba que las tres estructuras tienen la misma fórmula molecular contando H: 12 en los tres casos»
   - *Arreglo:* Mostrar el recuento de cada una, p. ej. pentan-1-ol: 3+2+2+2+2+1(OH)=12; 2-metilbutan-1-ol: 2+1+3+2+3+1=12; 3-metilbutan-1-ol: 2+2+1+3+3+1=12; 2,2-dimetilpropan-1-ol: 2+0+3·3+1=12.
15. **[BAJA · TEORIA_INCOMPLETA]** `exam_questions[1].full_solution` — La respuesta exige identificar 'isomería de función', concepto que esta lección no explica (solo nombra isomería estructural/espacial y de cadena).
   - *Texto actual:* «así que es un caso de isomería de función, no de cadena»
   - *Arreglo:* Añadir en theory_blocks[0] la lista de los tres tipos de isomería estructural (cadena, posición, función) con una línea cada uno, o remitir a la lección de isomería de función.
16. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica por qué aparece el error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Se interpreta la forma del dibujo (recto, zigzag, en L) como si fuera información estructural, cuando solo importa qué átomo está unido a cuál.'
17. **[BAJA · LATEX]** `worked_examples[1].reasoning[1]` — Fórmulas con subíndices Unicode (HOCH₂, CH₃) en vez del formato LaTeX del resto del curso.
   - *Texto actual:* «HOCH₂-CH(CH₃)-CH₂-CH₃»
   - *Arreglo:* HOCH$_2$-CH(CH$_3$)-CH$_2$-CH$_3$ y HOCH$_2$-CH$_2$-CH(CH$_3$)-CH$_3$.
18. **[BAJA · LATEX]** `diagnostic_items[1].expected_answer` — Subíndice químico sin formato y 'x' como signo de multiplicación.
   - *Texto actual:* «Cada CH3 aporta 3 H: 4x3 = 12 H.»
   - *Arreglo:* Cada CH$_3$ aporta 3 H: $4\cdot 3 = 12$ H.
19. **[BAJA · VISUAL]** `theory_blocks[3].body` — Mezcla subíndices Unicode (CH₃) con LaTeX (CH$_3$), y la frase 'C1 con CH₃ lateral, o el extremo opuesto' es confusa.
   - *Texto actual:* «sobre el esqueleto de 2-metilbutano el -OH puede ir en dos extremos no equivalentes (C1 con CH₃ lateral, o el extremo opuesto)»
   - *Arreglo:* Usar CH$_3$; reescribir: 'el -OH puede ir en el extremo próximo a la ramificación (2-metilbutan-1-ol) o en el extremo alejado (3-metilbutan-1-ol)'.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[0].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (1): `guided_exercises[1]`. Ej.: «Se proponen dos estructuras: CH$_3$-CH$_2$-CH(CH$_3$)-CH$_2$-CH$_3$ y CH$_3$-CH(CH$_3$)-CH$_2$-CH$_2$-CH$_3$. (a) Nombra \|\| RESP: (a) Las dos se nombran 3-metilpentano. (b) No so…». Arreglo: Añadir full_solution paso a paso.

#### Lección 10 — Isomería de posición

**Valoración experta: MEDIA.** Lección correcta en lo químico (nomenclatura, recuentos, xilenos, ⌈n/2⌉ y MCQ verificados) y bien estructurada. Los fallos son puntuales: definición de 'sustituyente' que choca con la isomería de cadena, remisión rota a cis-trans como 'próxima lección', diagnóstico 1 incoherente, los dos ejercicios guiados sin solución desarrollada y el caso del esqueleto ramificado sin ejemplo. Figuras correctas.

**Plan de arreglo:** 1) Precisar la definición (sustituyentes no alquílicos). 2) Corregir la remisión a la L12. 3) Rehacer diagnostic_items[0]. 4) Escribir full_solution de los dos guiados. 5) Añadir ejemplo de posiciones en 2-metilbutano. 6) Retoques menores (mcq[1], Unicode, plantilla).

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `theory_blocks[1].body` — La definición incluye 'o un sustituyente' sin restringirlo. Si el sustituyente es un radical alquilo, mover un metilo (2-metilpentano / 3-metilpentano) cambia el esqueleto y es isomería de CADENA según la lección anterior; con esta definición el alumno lo clasificaría como de posición. Hay que precisar qué 'sustituyentes' cuentan (halógenos, -NO2…), no los radicales alquilo. Lo mismo en objectives[0], flashcards[0] y misconceptions[0].correct_model.
   - *Texto actual:* «pero ese grupo (o un doble enlace, o un sustituyente) ocupa una posición distinta sobre la cadena»
   - *Arreglo:* '…pero ese grupo funcional (o un enlace múltiple, o un sustituyente no carbonado como un halógeno o -NO$_2$) ocupa una posición distinta. Cambiar de sitio una ramificación alquílica modifica el esqueleto: eso es isomería de cadena.'
2. **[MEDIA · SOLUCION_AUSENTE]** `guided_exercises[0]` — Ejercicio guiado sin full_solution: solo respuesta final, sin mostrar la numeración por ambos extremos ni las fórmulas semidesarrolladas pedidas en (b).
   - *Texto actual:* «claves: answer, common_errors, hints (sin full_solution)»
   - *Arreglo:* Añadir full_solution: numeración C1…C4 / C4…C1 → C1≡C4, C2≡C3 → 2 posiciones; (b) CH$_3$-CH$_2$-CH$_2$-CH$_2$Br (1-bromobutano) y CH$_3$-CH$_2$-CHBr-CH$_3$ (2-bromobutano), ambos C$_4$H$_9$Br.
3. **[MEDIA · SOLUCION_AUSENTE]** `guided_exercises[1]` — Ejercicio guiado sin full_solution: la respuesta solo da 'Posición. Cadena. Ninguna' sin razonar (el enunciado pide decir por qué).
   - *Texto actual:* «answer = (a) Posición. (b) Cadena. (c) Ninguna»
   - *Arreglo:* Añadir full_solution con fórmulas: (a) CH$_3$-CHOH-CH$_2$-CH$_2$-CH$_3$ y CH$_3$-CH$_2$-CHOH-CH$_2$-CH$_3$: mismo esqueleto lineal C5, -OH en C2/C3 → posición; (b) cadena lineal C5 frente a C4 con metilo, -OH en C1 en ambos → cadena; (c) C$_5$H$_{12}$ frente a C$_6$H$_{14}$: no son isómeros.
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — El caso del esqueleto ramificado se despacha con una frase ('hay que comprobarla numerando con cuidado') sin ningún ejemplo, y en examen es frecuente. El alumno no aprende a contar posiciones no equivalentes en, p. ej., 2-metilbutano.
   - *Texto actual:* «En un esqueleto ramificado, la simetría puede ser distinta y hay que comprobarla numerando con cuidado por los dos sentidos posibles de cada caso.»
   - *Arreglo:* Añadir ejemplo: -OH sobre el esqueleto de 2-metilbutano → 4 posiciones no equivalentes: 2-metilbutan-1-ol, 2-metilbutan-2-ol, 3-metilbutan-2-ol, 3-metilbutan-1-ol (los dos CH$_3$ de C1 y la ramificación son equivalentes).
5. **[MEDIA · REFERENCIA_ROTA]** `theory_blocks[4].body` — Remite a la isomería cis-trans 'en la próxima lección', pero la siguiente lección (L11) es Isomería de función; cis-trans es la L12. Lo mismo en common_mistakes[3].how_to_avoid ('cis-trans, próxima lección').
   - *Texto actual:* «con la isomería cis-trans, que se estudiará en la próxima lección»
   - *Arreglo:* '…que se estudiará en la lección de isomería geométrica (cis-trans y E/Z)'. Corregir igual common_mistakes[3].how_to_avoid.
6. **[MEDIA · ESTRUCTURA]** `diagnostic_items[0].common_wrong_answers[0].answer` — Incoherencia: la pregunta pide nombrar CH3-CH2-CH2-CHOH-CH3, pero el error típico ('5 posiciones, una por cada carbono') y la interpretación hablan de contar posiciones no equivalentes, que no es lo que se pregunta.
   - *Texto actual:* «5 posiciones, una por cada carbono. / 'Sin contar correctamente las posiciones no equivalentes…'»
   - *Arreglo:* Error típico: 'pentan-4-ol', numerando desde el extremo equivocado; interpretación: 'No aplica la regla del localizador más bajo al grupo funcional'. (O bien cambiar la pregunta a '¿cuántas posiciones no equivalentes hay para el -OH en una cadena de 5 C?').
7. **[BAJA · CONCEPTO]** `worked_examples[3].interpretation` — Frase confusa: dice que es 'el mismo tipo de confusión… pero en sentido contrario', cuando en ambas lecciones la idea es la misma (girar/doblar el dibujo no cambia la estructura).
   - *Texto actual:* «Este es el mismo tipo de confusión que confundir la forma del dibujo con la estructura, vista en la lección anterior, pero en sentido contrario»
   - *Arreglo:* 'Igual que en la lección anterior, girar el dibujo no cambia la estructura; lo que distingue a los tres xilenos es la distancia entre los metilos, que ningún giro modifica.'
8. **[BAJA · CONCEPTO]** `theory_blocks[3].body` — Restringe orto/meta/para a 'dos sustituyentes iguales'; los prefijos se usan igual con sustituyentes distintos (o-nitrotolueno, p-cloroanilina…).
   - *Texto actual:* «se aplica a un anillo bencénico con dos sustituyentes iguales»
   - *Arreglo:* '…a un anillo bencénico con dos sustituyentes (iguales o distintos)'; mencionar que IUPAC 2005 prefiere localizadores numéricos (1,2-; 1,3-; 1,4-) aunque o/m/p sigan aceptados.
9. **[BAJA · MCQ]** `mcq[1].stem` — Par mal elegido: pentan-2-ol y 2-metilbutan-1-ol difieren a la vez en el esqueleto y en el tipo/posición del -OH (secundario en C2 frente a primario en C1), así que no es un ejemplo limpio de isomería de cadena y puede confundir.
   - *Texto actual:* «El pentan-2-ol y el 2-metilbutan-1-ol tienen la misma fórmula molecular»
   - *Arreglo:* Usar pentan-2-ol y 3-metilbutan-2-ol (ambos -OH en C2, distinto esqueleto) o pentan-1-ol y 2-metilbutan-1-ol; ajustar explicación.
10. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica la causa del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Se compara solo el grupo funcional y la fórmula molecular sin dibujar el esqueleto desnudo de cada compuesto.'
11. **[BAJA · LATEX]** `diagnostic_items[0].question` — Fórmula con subíndices Unicode (CH₃, CH₂) en vez del formato LaTeX del resto del curso.
   - *Texto actual:* «CH₃-CH₂-CH₂-CHOH-CH₃»
   - *Arreglo:* CH$_3$-CH$_2$-CH$_2$-CHOH-CH$_3$
12. **[BAJA · VISUAL]** `summary.formulas[0]` — La fórmula aparece sin explicar qué representa (n y el resultado), y sola en el resumen pierde sentido.
   - *Texto actual:* «\lceil n/2 \rceil»
   - *Arreglo:* N_{\text{posiciones}} = \lceil n/2 \rceil \ (\text{un sustituyente en cadena lineal de } n \text{ C})

**Chequeos automáticos:**

- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (2): `guided_exercises[0]`, `guided_exercises[1]`. Ej.: «Sobre una cadena lineal de 4 carbonos. (a) ¿Cuántas posiciones no equivalentes hay para un sustituyente como el Br? (b)  \|\| RESP: (a) 2 posiciones (C1≡C4, C2≡C3). (b) 1-bromobuta…». Arreglo: Añadir full_solution paso a paso.
- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[0].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.

#### Lección 11 — Isomería de función

**Valoración experta: BAJA.** Lección químicamente sólida: recuentos, fórmulas, temperaturas de ebullición (propan-1-ol 97 °C, metoxietano 7 °C, etanol 78/-24 °C, ácido acético 118/32 °C) y claves de test correctas. Fallos menores: una pista del reto que contradice la solución, el guiado 2 con solución que copia las pistas y el guiado 1 sin solución, ecuaciones de saponificación/neutralización sin escribir, una errata en la figura y algunas generalizaciones imprecisas sobre el enlace de hidrógeno. Teoría algo corta en solubilidad y en otros pares de isómeros de función; peso excesivo de la tautomería, que probablemente está fuera del temario.

**Plan de arreglo:** 1) Corregir hints[1] del reto y completar su solución con el esqueleto ramificado. 2) Escribir full_solution de los guiados. 3) Añadir ecuaciones con estados en exam_questions[0]. 4) Errata de la figura. 5) Precisar enlace de H (diagnóstico, resumen) y añadir solubilidad y otros pares de función. 6) Revisar si la tautomería está en el temario y reducir su peso.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `challenge_questions[0].hints[1]` — La pista contradice la solución: dice que el carbonilo puede estar en 'dos posiciones no equivalentes' para dar cetonas en C4, cuando la solución (correcta) concluye que solo existe una cetona (butanona). Las dos posiciones no equivalentes son C1 (aldehído) y C2 (cetona).
   - *Texto actual:* «el carbono del carbonilo puede estar en dos posiciones no equivalentes de la cadena de 4 carbonos: identifica cuáles»
   - *Arreglo:* 'Para $n=4$, prueba el carbonilo en C2 y en C3 de la cadena lineal y comprueba si renumerando dan el mismo compuesto; recuerda que el esqueleto ramificado de 4 C no deja ningún carbono con dos vecinos libres para el C=O.'
2. **[MEDIA · INSTRUCCIONES_EN_VEZ_DE_SOLUCION]** `guided_exercises[1].full_solution` — La 'solución' copia literalmente las pistas ('Procedimiento: Para (b), identifica si…') y no hace el recuento del apartado (a).
   - *Texto actual:* «Procedimiento: Para (b), identifica si alguno de los dos puede formar enlaces de hidrógeno entre sus propias moléculas, y cuál.»
   - *Arreglo:* (a) CH$_3$-COOH: 2 C, H 3+1=4, 2 O → C$_2$H$_4$O$_2$; HCOO-CH$_3$: 2 C, H 1+3=4, 2 O → C$_2$H$_4$O$_2$. (b) El ácido forma enlaces de hidrógeno (dímeros cíclicos, dos por molécula); el éster solo tiene fuerzas dipolo-dipolo y de dispersión → 118 °C frente a 32 °C.
3. **[MEDIA · SOLUCION_AUSENTE]** `guided_exercises[0]` — Ejercicio guiado sin full_solution; la respuesta no muestra el recuento de átomos que pide (a).
   - *Texto actual:* «answer = (a) Ambas C$_4$H$_8$O. (b) Butanal: aldehído…»
   - *Arreglo:* Añadir full_solution: butanal 4 C, H 3+2+2+1=8, 1 O; butanona 4 C, H 3+2+0+3=8, 1 O → C$_4$H$_8$O ambos; -CHO terminal frente a C=O interior → isómeros de función.
4. **[BAJA · CONCEPTO]** `diagnostic_items[1].expected_answer` — Explicación imprecisa del enlace de hidrógeno: mezcla la condición de dador (H unido a O, N, F) con la de aceptor ('con un par libre accesible'). El éter sí tiene O con pares libres (es aceptor); lo que le falta es un H unido a O.
   - *Texto actual:* «el éter no tiene ningún H unido a un átomo muy electronegativo con un par libre accesible de la misma manera»
   - *Arreglo:* '…el éter no tiene ningún H unido a O (solo H unidos a C), así que sus moléculas no pueden formar enlaces de hidrógeno entre sí, aunque su O sí podría aceptarlos del agua.'
5. **[BAJA · CONCEPTO]** `summary.key_points[2]` — Generalización falsa: el enlace de hidrógeno no es 'posible solo con -OH o -COOH'; también lo forman N-H (aminas, amidas) y H-F.
   - *Texto actual:* «el enlace de hidrógeno (posible solo con -OH o -COOH)»
   - *Arreglo:* '(entre los compuestos oxigenados, solo los que tienen -OH, como alcoholes y ácidos; también lo forman aminas y amidas por sus N-H)'.
6. **[BAJA · CONCEPTO]** `exam_questions[1].full_solution` — Atribuye la diferencia a la 'estabilidad relativa', cuando lo esencial es la interconversión rápida (equilibrio) frente a compuestos que no se interconvierten; la estabilidad relativa es otra cosa (qué forma predomina).
   - *Texto actual:* «La diferencia esencial está en la estabilidad relativa de cada caso»
   - *Arreglo:* 'La diferencia esencial es si las dos formas se interconvierten espontáneamente (tautomería, equilibrio) o no (isómeros ordinarios, separables).'
7. **[BAJA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — Solo analiza la cadena lineal; para afirmar que la butanona es la única cetona de C4H8O falta descartar el esqueleto ramificado (en (CH3)2CH- no hay carbono que pueda llevar el C=O con un carbono a cada lado sin ser el C central, que ya tiene 3 C).
   - *Texto actual:* «No hay una segunda cetona distinta para $n=4$: solo existe la butanona.»
   - *Arreglo:* Añadir: 'Con el esqueleto ramificado (CH$_3$)$_2$CH-CHO solo cabe un aldehído (2-metilpropanal): el carbono central ya tiene tres vecinos de carbono y no puede ser C=O. Por tanto la única cetona es la butanona.'
8. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[0].full_solution` — El apartado (c) describe las dos reacciones con NaOH pero no escribe las ecuaciones químicas, que es lo que se espera en PAU (con estados de agregación).
   - *Texto actual:* «El éster no tiene ningún H ácido de ese tipo; con NaOH reacciona por un mecanismo distinto, la hidrólisis básica del éster (saponificación)»
   - *Arreglo:* Añadir: CH$_3$-CH$_2$-COOH(aq) + NaOH(aq) → CH$_3$-CH$_2$-COONa(aq) + H$_2$O(l); CH$_3$-COO-CH$_3$(l) + NaOH(aq) → CH$_3$-COONa(aq) + CH$_3$OH(aq). Mencionar que el otro éster válido es el metanoato de etilo, HCOO-CH$_2$-CH$_3$.
9. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — El objetivo 3 y exam_notes[1] mencionan la solubilidad, pero la teoría no la explica (alcoholes de cadena corta y ácidos miscibles con agua; éteres y ésteres menos solubles, aunque aceptan enlaces de H del agua).
   - *Texto actual:* «objectives[2]: 'pueden tener puntos de ebullición, solubilidad o reactividad muy distintos'»
   - *Arreglo:* Añadir un párrafo sobre solubilidad en agua: el -OH/-COOH dona y acepta enlaces de H con el agua; éteres, ésteres, aldehídos y cetonas solo los aceptan → menor solubilidad a igual nº de C.
10. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — Solo presenta los tres pares oxigenados. No menciona otros isómeros de función frecuentes en PAU para una misma fórmula, que el reto ('entre otros isómeros') y las preguntas de 'todos los isómeros de C3H6O' suponen: alcohol insaturado/éter insaturado (prop-2-en-1-ol, metoxieteno), alqueno/cicloalcano (C$_n$H$_{2n}$), alquino/dieno (C$_n$H$_{2n-2}$).
   - *Texto actual:* «tres parejas de familias aparecen una y otra vez como isómeros de función entre sí»
   - *Arreglo:* Añadir una línea: 'También son isómeros de función, p. ej., propanal / prop-2-en-1-ol / metoxieteno (C$_3$H$_6$O), propeno / ciclopropano (C$_3$H$_6$) o but-1-ino / buta-1,3-dieno (C$_4$H$_6$).'
11. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Se identifica misma fórmula con mismo compuesto, olvidando que las propiedades dependen de cómo están unidos los átomos (grupo funcional).'
12. **[BAJA · NIVEL]** `theory_blocks[4].body` — La tautomería ceto-enólica (y 1 objetivo, 1 ejemplo, 1 ejercicio, 1 pregunta de examen, 1 MCQ y 2 fichas dedicados a ella) no figura habitualmente en los currículos LOMLOE/PAU de Química de 2.º Bachillerato; ocupa una parte desproporcionada de la lección.
   - *Texto actual:* «Existe un caso particular de isomería de función que merece un tratamiento distinto: la **tautomería**.»
   - *Arreglo:* VERIFICAR con el temario oficial; si no aparece, marcarla como ampliación y reducir su peso (sustituir exam_questions[1]/exercises[2] por preguntas de pares clásicos o de 'todos los isómeros de C$_3$H$_6$O').
13. **[BAJA · ERRATA]** `theory_blocks[1].assets[0].svg` — En la figura falta la preposición en el nombre del éster.
   - *Texto actual:* «Etanoato metilo (éster)»
   - *Arreglo:* Etanoato de metilo (éster)
14. **[BAJA · VERIFICAR]** `worked_examples[0].statement` — Se usa solo el nombre de clase funcional 'etil metil éter' / 'metil propil éter'. IUPAC 2005 prefiere el sustitutivo (metoxietano, 1-metoxipropano); conviene dar ambos, como se acepta en PAU.
   - *Texto actual:* «el etil metil éter (CH$_3$-CH$_2$-O-CH$_3$)»
   - *Arreglo:* 'el metoxietano (etil metil éter)'; igual en exercises[1]: '1-metoxipropano (metil propil éter)'.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[0].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (1): `guided_exercises[0]`. Ej.: «Se dan el butanal (CH$_3$-CH$_2$-CH$_2$-CHO) y la butanona (CH$_3$-CH$_2$-CO-CH$_3$). (a) Cuenta los átomos de cada uno  \|\| RESP: (a) Ambas C$_4$H$_8$O. (b) Butanal: aldehído. Bu…». Arreglo: Añadir full_solution paso a paso.

#### Lección 12 — Isomería geométrica cis-trans y marco E/Z

**Valoración experta: MEDIA.** La teoría está bien motivada: explica el enlace π, la condición carbono a carbono y los ciclos, y hay buenos ejemplos de casos sin isomería (cloroeteno, 2-metilpropeno, buta-1,3-dieno). Hay dos errores graves. Las DOS figuras tienen los rótulos cis/trans (y Z/E) intercambiados. El ejemplo canónico «solo E/Z», BrCH=CHCl, sí admite cis/trans (lleva un H en cada carbono), y aparece en el ejemplo 4, la pregunta de examen 2, el test 4 y el resumen. Además, la lección da criterios contradictorios sobre cuándo usar cis/trans. Las soluciones guiadas son flojas o de plantilla, y hay frases «why» genéricas.

**Plan de arreglo:** 1) Corregir los rótulos de las dos figuras SVG. 2) Sustituir BrCH=CHCl por una molécula sin sustituyente común (p. ej. BrClC=CH-CH3) en worked_examples[3], exam_questions[1], mcq[3], summary y misconceptions. 3) Unificar en todos los campos el criterio de uso de cis/trans (sustituyente común de referencia, normalmente H). 4) Añadir la regla CIP elemental (número atómico) y la advertencia de que cis≠Z en general. 5) Redactar las soluciones de guided_exercises y los «why» de plantilla.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `theory_blocks[1].assets[0].svg` — Las etiquetas de la figura están intercambiadas. La molécula de la izquierda, rotulada «cis-but-2-eno (Z)», tiene un CH$_3$ arriba a la izquierda y otro abajo a la derecha, así que es el isómero trans (E). La de la derecha, rotulada «trans-but-2-eno (E)», tiene los dos CH$_3$ arriba, así que es el cis (Z). Contradice el pie de figura y el texto, y enseña justo lo contrario.
   - *Texto actual:* «Rótulos del SVG: izquierda «cis-but-2-eno (Z)» con CH3 arriba-izq. y CH3 abajo-dcha.; derecha «trans-but-2-eno (E)» con los dos CH3 arriba.»
   - *Arreglo:* Intercambiar los rótulos: izquierda «trans-but-2-eno (E)» y derecha «cis-but-2-eno (Z)». También se puede dejar el orden cis→trans y redibujar los sustituyentes. Comprobar que el pie de figura sigue coincidiendo.
2. **[ALTA · CONCEPTO]** `worked_examples[1].assets[0].svg` — Pasa lo mismo que en la figura del but-2-eno. La estructura de la izquierda, rotulada «cis-1,2-dicloroeteno (Z)», tiene un Cl arriba a la izquierda y otro abajo a la derecha, así que es trans (E). La de la derecha, rotulada «trans… (E)», tiene los dos Cl arriba, así que es cis (Z).
   - *Texto actual:* «Rótulos del SVG: «cis-1,2-dicloroeteno (Z)» bajo la estructura con los Cl en lados opuestos; «trans-1,2-dicloroeteno (E)» bajo la estructura con los dos Cl arriba.»
   - *Arreglo:* Intercambiar los rótulos de las dos estructuras (o redibujarlas) para que cis/Z sea la que tiene los dos Cl al mismo lado.
3. **[ALTA · CONCEPTO]** `worked_examples[3].statement` — El ejemplo elegido para mostrar un caso que «no se puede nombrar con cis/trans» no sirve, porque BrCH=CHCl lleva un H en cada carbono. Según el propio theory_blocks[3] («funciona siempre que al menos un sustituyente se repita… normalmente el H») y exercises[1] (pent-2-eno nombrado con cis/trans tomando los H como referencia), esta molécula sí admite cis/trans. De hecho, cis-/trans-1-bromo-2-cloroeteno son nombres de uso corriente. reasoning[0] dice además que «no hay ningún sustituyente que se repita», lo cual es falso porque se repite el H.
   - *Texto actual:* ««(a) explica por qué no se puede nombrar con cis/trans de forma directa» / reasoning[0]: «no hay ningún sustituyente que se repita entre los dos lados»»
   - *Arreglo:* Cambiar la molécula por una sin ningún sustituyente común en los dos carbonos, por ejemplo BrClC=CH-CH$_3$ (1-bromo-1-cloropropeno; prioridades dadas Br > Cl y CH$_3$ > H) o la de exercises[2] (Br, CH$_3$ / Cl, H). Rehacer reasoning, solution e interpretation con esa molécula. En (b), la disposición con los dos sustituyentes más prioritarios al mismo lado es Z.
4. **[ALTA · CONCEPTO]** `exam_questions[1].full_solution` — La respuesta modelo pone como ejemplo de «molécula en la que solo se puede usar E/Z» a BrCH=CHCl, que tiene un H en cada carbono y admite cis/trans (cis-1-bromo-2-cloroeteno). Además formula la regla como «cis/trans exige que el par de sustituyentes sea el mismo en los dos carbonos», lo que contradice theory_blocks[3] y exercises[1].
   - *Texto actual:* ««BrCH=CHCl (…) no tiene un sustituyente que se repita en los dos carbonos para nombrarla con cis/trans»»
   - *Arreglo:* Dar un ejemplo correcto: un alqueno trisustituido o tetrasustituido sin ningún grupo común en los dos carbonos, como BrClC=CH-CH$_3$, ClCH$_3$C=CBrH o 3-metilpent-2-eno con las prioridades dadas. Corregir también answer y mark_scheme[1]. Formular la diferencia así: cis/trans necesita un sustituyente común (o análogo) en los dos carbonos que sirva de referencia; E/Z no lo necesita.
5. **[ALTA · MCQ]** `mcq[3].stem` — El enunciado da por cierto algo falso: que BrCH=CHCl «no se puede nombrar de forma directa con cis/trans». La explicación de la opción C se apoya en la misma idea («cis/trans exige además que se repita el mismo par»), que contradice theory_blocks[3]. Un alumno que haya aprendido la teoría podría elegir C con razón.
   - *Texto actual:* ««La molécula BrCH=CHCl cumple la condición general (…) pero no se puede nombrar de forma directa con cis/trans.»»
   - *Arreglo:* Sustituir la molécula del enunciado por una sin sustituyente común, por ejemplo BrClC=CH-CH$_3$, y ajustar options[2].why_wrong y explanation.
6. **[MEDIA · CONCEPTO]** `summary.key_points[3]` — El resumen y las fichas repiten el ejemplo erróneo de BrCH=CHCl como molécula «con E/Z sin cis/trans aplicable». Se repite también en misconceptions[1].diagnostic_signal.
   - *Texto actual:* ««hay moléculas (como BrCH=CHCl) con E/Z sin cis/trans aplicable»»
   - *Arreglo:* Usar el mismo ejemplo nuevo que en worked_examples[3], por ejemplo BrClC=CH-CH$_3$, en summary.key_points[3] y en misconceptions[1].diagnostic_signal.
7. **[MEDIA · CONCEPTO]** `theory_blocks[1].body` — La lección da tres criterios incompatibles para saber cuándo se puede usar cis/trans. (1) theory_blocks[1], objectives[2], flashcards[2] y summary.key_points[1]: solo cuando los dos carbonos llevan «el mismo par de sustituyentes». (2) theory_blocks[3]: «siempre que al menos un sustituyente se repita (normalmente el H)». (3) exercises[1]: en el pent-2-eno se usa cis/trans aunque el par no sea el mismo. El alumno no sabe qué regla aplicar.
   - *Texto actual:* «theory_blocks[1]: «el único que trata la nomenclatura cis-trans propiamente dicha- los dos carbonos del doble enlace llevan el mismo par de sustituyentes» frente a theory_blocks[3]: «funciona siempre que al menos un sustituyente se repita»»
   - *Arreglo:* Unificar el criterio en todos esos campos. Propuesta: cis/trans se usa cuando cada carbono del doble enlace tiene un sustituyente en común con el otro (casi siempre un H), que sirve de referencia. Si no hay ningún sustituyente común, solo cabe E/Z. Reescribir en coherencia objectives[2], theory_blocks[1], flashcards[2], summary.key_points[1] y exam_questions[1].
8. **[BAJA · MCQ]** `mcq[0].options[3].text` — El distractor D es absurdo y no lo elegiría ningún alumno, así que no mide nada.
   - *Texto actual:* ««No, porque el cloro es demasiado grande para caber en la molécula.»»
   - *Arreglo:* Sustituirlo por un distractor plausible, por ejemplo «No, porque el cloro es más prioritario que el H y eso impide la isomería», o «Sí, porque los dos carbonos del doble enlace son distintos entre sí».
9. **[BAJA · SOLUCION_INCOMPLETA]** `guided_exercises[0]` — El ejercicio guiado no tiene full_solution. La respuesta da los sustituyentes y un «No» seco, sin la frase que justifica (b).
   - *Texto actual:* «answer: «(b) No presenta isomería cis-trans.»»
   - *Arreglo:* Añadir full_solution: «C1 lleva dos H idénticos: la condición falla en C1. Aunque C2 lleve H y etilo (distintos), no hay isomería cis-trans en el but-1-eno.»
10. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — La teoría no da ningún criterio, ni el más elemental, para ordenar prioridades. Sin embargo, worked_examples[3].reasoning[1] afirma que «H es siempre el sustituyente dado como de menor prioridad» sin justificarlo. Tampoco avisa de que cis y Z no coinciden necesariamente en alquenos trisustituidos.
   - *Texto actual:* ««En Bachillerato no se exige aplicar las reglas CIP para deducir la prioridad desde cero»»
   - *Arreglo:* Añadir una frase: «regla CIP básica: tiene más prioridad el sustituyente cuyo átomo unido al carbono tiene mayor número atómico (Br > Cl > O > C > H)». Añadir la advertencia: «cis/trans y E/Z son descriptores distintos; en algunos alquenos trisustituidos un isómero cis puede ser E».
11. **[BAJA · PLANTILLA]** `guided_exercises[1].full_solution` — La solución es un relleno automático. Copia la pista con la etiqueta «Procedimiento:» y después la respuesta con «Conclusión:», sin desarrollo propio. Además, common_errors[0] habla de «rotación libre alrededor del doble enlace» en un ejercicio sobre un anillo saturado.
   - *Texto actual:* ««Procedimiento: Piensa en 'los dos lados' del doble enlace como 'las dos caras'…» / common_errors[0]: «interconvertir los isómeros mediante rotación libre alrededor del doble enlace»»
   - *Arreglo:* Redactar una solución real. (a) Para que un metilo pase a la otra cara del anillo habría que romper un enlace C-C del ciclo; los enlaces del anillo no pueden girar 180° libremente. (b) cis: los dos CH$_3$ hacia la misma cara; trans: hacia caras opuestas. Cambiar el error común por «intentar convertir cis en trans girando un enlace C-C del anillo como si fuera una cadena abierta».
12. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — El «why» es una frase genérica que no explica por qué se comete el error. Ocurre lo mismo en common_mistakes[1].why.
   - *Texto actual:* ««El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»»
   - *Arreglo:* [0]: «Se comprueba solo el carbono con el sustituyente llamativo y se olvida el otro». [1]: «Se confunde la condición de existencia de la isomería con la condición para usar la nomenclatura cis/trans».

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (1): `guided_exercises[0]`. Ej.: «El but-1-eno (CH$_2$=CH-CH$_2$-CH$_3$) es un isómero de posición del but-2-eno. (a) Identifica los sustituyentes de cada \|\| RESP: (a) C1 lleva H y H; C2 lleva H y -CH$_2$-CH$_3$ …». Arreglo: Añadir full_solution paso a paso.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (8): `diagnostic_items[1].question`, `worked_examples[0].statement`, `worked_examples[0].knowns[0]`, `guided_exercises[0].statement`, `exercises[1].statement`, `exam_questions[0].statement`, `exam_questions[0].statement`, `challenge_questions[0].statement`. Ej.: «En CH$_3$-CH=CH-CH$_3$ (but-2-eno), ¿qué dos sustituyentes lleva cada uno de l». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · TEXTO_PARA_PROFESOR] Texto dirigido al profesor/corrector en lugar de al alumno. (1): `exam_questions[1].mark_scheme[0]`. Ej.: «1 punto por explicar que E/Z no exige que el par de sustituyentes se repita en los dos carbonos». Arreglo: Reescribir en segunda persona dirigido al alumno.

#### Lección 13 — Quiralidad e isomería óptica

**Valoración experta: BAJA.** Es una lección sólida y correcta en lo esencial. Las definiciones de C*, enantiómero, racémico y meso están bien, el ácido tartárico (L-(+), D-(-) y meso) está bien tratado, y la comparación meso frente a racémico está bien hecha. No hay errores de cálculo ni claves de test mal puestas. Puntos débiles: la meso se explica por «compensación interna de giros» en lugar de por aquiralidad, y faltan la regla 2^n en la teoría y la diferente actividad biológica de los enantiómeros. La figura de enantiómeros no muestra la relación especular. Las soluciones guiadas son de plantilla y falta un ejercicio de dibujar enantiómeros y localizar varios C*.

**Plan de arreglo:** 1) Reformular la causa de la inactividad de la forma meso (molécula aquiral, superponible) en todos los campos donde aparece. 2) Añadir a la teoría: 2^n estereoisómeros, cis-trans como diastereómeros y la diferente acción biológica de los enantiómeros. 3) Redibujar la figura como reflejo, con el espejo y el C* marcados. 4) Redactar las full_solution guiadas y los «why» genéricos. 5) Añadir un ejercicio PAU de dibujar enantiómeros y contar estereoisómeros.

**Hallazgos de la revisión experta:**

1. **[MEDIA · TEORIA_INCOMPLETA]** `exercises` — Falta el tipo de ejercicio más habitual de PAU sobre isomería óptica: representar los dos enantiómeros en 3D (cuñas) de una molécula dada. También falta localizar los C* en moléculas algo más complejas, con varios grupos funcionales o con dos C* no simétricos (p. ej. 2-bromo-3-clorobutano, gliceraldehído, alanina). Todos los ejercicios son de «sí/no es quiral» con moléculas de 3-4 carbonos o de teoría verbal.
   - *Texto actual:* «Ningún ejercicio pide dibujar los enantiómeros; exam_questions[0] solo usa moléculas de 3-4 C con un único candidato.»
   - *Arreglo:* Añadir un ejercicio de examen: «Señala los C* del 2-bromo-3-clorobutano (o de la alanina, CH$_3$-CH(NH$_2$)-COOH), indica cuántos estereoisómeros puede tener y dibuja con cuñas los dos enantiómeros de uno de ellos». Incluir la solución con el dibujo.
2. **[BAJA · CONCEPTO]** `theory_blocks[4].body` — La inactividad óptica de la forma meso se explica como si cada carbono quiral produjera «su» giro y los dos se anularan («compensación interna»). La rotación óptica no es una suma de contribuciones de cada centro. El motivo real es que la molécula meso es aquiral: es superponible con su imagen especular por tener un plano de simetría. La misma idea se repite en worked_examples[2].reasoning[2], exam_questions[1].full_solution, challenge_questions[0].full_solution, flashcards[6].back, misconceptions[1].correct_model y summary.key_points[4].
   - *Texto actual:* ««Por eso el giro que produce un carbono se cancela exactamente con el que produce el otro»»
   - *Arreglo:* Reformular: «Por tener un plano de simetría interno, la molécula meso es superponible con su imagen especular: es aquiral y, por tanto, ópticamente inactiva, aunque tenga dos C*». La «compensación interna» puede quedar, como mucho, como imagen intuitiva señalada como tal.
3. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — La teoría presenta a los enantiómeros como idénticos salvo en el giro de la luz polarizada. No menciona que se comportan de forma distinta frente a otras sustancias quirales: enzimas, receptores y fármacos (p. ej. la talidomida, o los olores de la carvona). Es una pregunta frecuente de V/F en PAU. Solo aparece de pasada en exercises[1].common_errors.
   - *Texto actual:* ««Tienen exactamente las mismas propiedades físicas 'ordinarias' (…), con una excepción notable: desvían la luz polarizada en sentidos opuestos.»»
   - *Arreglo:* Añadir un párrafo: «Químicamente reaccionan igual con reactivos no quirales, pero pueden comportarse de forma muy distinta con otras moléculas quirales (enzimas, receptores biológicos); por eso dos enantiómeros de un fármaco pueden tener efectos distintos (talidomida)».
4. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[4].body` — La teoría no enuncia la regla del máximo de 2$^n$ estereoisómeros para n carbonos quirales; solo aparece en misconceptions[1]. Tampoco dice que los isómeros cis-trans de la lección anterior también son diastereómeros. La definición de diastereómero queda restringida a «varios carbonos quirales».
   - *Texto actual:* ««En principio, dos carbonos quirales permitirían hasta cuatro combinaciones distintas»»
   - *Arreglo:* Añadir: «Con n carbonos quirales hay como máximo $2^n$ estereoisómeros (menos si hay formas meso)». Añadir también: «diastereómeros = estereoisómeros que no son enantiómeros; los isómeros cis/trans son un ejemplo».
5. **[BAJA · PLANTILLA]** `guided_exercises[0].full_solution` — Las full_solution de los dos ejercicios guiados son relleno automático («Procedimiento: <pista> Conclusión: <respuesta>»), sin desarrollo propio. Ocurre en guided_exercises[0] y guided_exercises[1].
   - *Texto actual:* ««Procedimiento: El carbono que lleva el -OH es el candidato; sigue la cadena completa… Conclusión: …»»
   - *Arreglo:* [0]: listar los cuatro sustituyentes del C2 y comparar las parejas, como en worked_examples[1]. [1]: explicar que al reflejar el mesotartárico y girar 180° se recupera la misma molécula (por el plano de simetría), así que su imagen especular es él mismo.
6. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — El «why» es una frase genérica sin contenido. Pasa lo mismo en common_mistakes[2].why.
   - *Texto actual:* ««El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»»
   - *Arreglo:* [0]: «Se asocia quiralidad a la presencia de un heteroátomo llamativo en vez de a la comparación de los cuatro grupos». [2]: «Se aplica 2$^n$ de forma mecánica sin buscar simetría interna».
7. **[BAJA · LATEX]** `exercises[0].hints[0]` — Hay fórmulas con subíndice Unicode o sin formato, incoherentes con el resto de la lección (que usa CH$_3$): «CH₃» en exercises[0].hints[0] y «sp3» en flashcards[7].front.
   - *Texto actual:* ««lleva DOS grupos -CH₃» / «del carbono sp3»»
   - *Arreglo:* Escribir CH$_3$ y sp$^3$.
8. **[BAJA · VISUAL]** `theory_blocks[2].assets[0].svg` — El «Enantiómero 2 (imagen especular)» no está dibujado como reflejo del 1, sino intercambiando las posiciones de H y COOH. El resultado sí es el enantiómero, pero el alumno no ve la relación especular que anuncian el título y el pie de figura. Tampoco se marca el C* ni hay un plano de espejo.
   - *Texto actual:* «Enantiómero 1: H en cuña discontinua y COOH en cuña; Enantiómero 2: COOH en cuña discontinua y H en cuña, con HO y CH3 en las mismas posiciones.»
   - *Arreglo:* Dibujar el enantiómero 2 como reflejo horizontal del 1 (HO↔CH$_3$ intercambiados de lado, cuñas iguales), con una línea vertical discontinua de «espejo» entre ambos y el C* marcado en los dos.
9. **[BAJA · VISUAL]** `exam_questions[0].full_solution` — En el apartado (c) hay una coletilla confusa que no aporta nada.
   - *Texto actual:* ««(de hecho, ni siquiera tiene cuatro sustituyentes distintos tomados de dos en dos: le faltan hasta dos tipos distintos)»»
   - *Arreglo:* Eliminarla o sustituirla por: «solo tiene dos tipos de sustituyente (CH$_3$ y H), cada uno repetido dos veces».
10. **[BAJA · VISUAL]** `exercises[0].full_solution` — La identificación de los dos metilos es confusa. Distingue un «-CH3 que cuelga directamente» de un «segundo -CH3 porque el enunciado indica…», cuando en la fórmula los dos metilos son el C1 y la ramificación.
   - *Texto actual:* ««-CH$_3$ (el que cuelga directamente), -CH$_2$-CH$_3$ (el resto de la cadena) y un segundo -CH$_3$, porque el enunciado indica que ese carbono lleva un sustituyente -CH$_3$ además de continuar la cadena principal»»
   - *Arreglo:* Reescribir: «El C2 está unido a: -OH, -CH$_3$ (el C1), -CH$_3$ (la ramificación) y -CH$_2$-CH$_3$. Hay dos grupos -CH$_3$ idénticos, así que no es quiral».

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.

#### Lección 14 — Reacciones de adición

**Valoración experta: MEDIA.** La teoría es correcta y clara. La tabla de los cuatro tipos de adición y sus condiciones, y la distinción entre adición y sustitución radicalaria, están bien. Todas las ecuaciones y recuentos de átomos son correctos (comprobados). Los fallos están en los ejercicios guiados: piden ecuaciones ajustadas y solo dan el producto. El reto usa el grado de insaturación, que no se enseña en la teoría, y concluye «pentano» sin que el esqueleto esté definido. También hay imprecisiones menores (los «enlaces π» del doble enlace, el agua de bromo frente a CCl4, el éter) y la adición a alquinos no tiene ninguna ecuación.

**Plan de arreglo:** 1) Escribir las ecuaciones ajustadas en guided_exercises[0] y [1]. 2) Explicar el grado de insaturación en la teoría (o eliminarlo) y corregir «pentano» por «C5H12 (según el esqueleto)». 3) Añadir ecuaciones de adición a alquinos. 4) Corregir las imprecisiones (enlace π, agua de bromo, éter) y el LaTeX de flashcards[9]. 5) Sustituir el «why» de plantilla.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `challenge_questions[0].full_solution` — La solución da como producto final el «pentano», pero el enunciado no fija el esqueleto. Un C$_5$H$_8$ con dos dobles enlaces puede ser ramificado: el isopreno (2-metilbuta-1,3-dieno) da 2-metilbutano. Solo se puede afirmar que se obtiene un alcano C$_5$H$_{12}$.
   - *Texto actual:* ««para obtener el alcano saturado C$_5$H$_{12}$ (pentano)»»
   - *Arreglo:* Escribir «el alcano C$_5$H$_{12}$ (pentano si la cadena es lineal, p. ej. desde el penta-1,3-dieno; 2-metilbutano si es el isopreno)». Otra opción es dar en el enunciado un dieno concreto.
2. **[MEDIA · SOLUCION_INCOMPLETA]** `guided_exercises[0].answer` — El enunciado pide «Escribe la ecuación ajustada» en (a) y (b), pero la respuesta solo da el producto. No hay full_solution, ni ecuación, ni comprobación del ajuste.
   - *Texto actual:* ««(a) CH$_3$-CHCl-CHCl-CH$_3$ (2,3-diclorobutano). (b) CH$_3$-CH$_2$-CHI-CH$_3$ (2-yodobutano).»»
   - *Arreglo:* Añadir full_solution con las ecuaciones: (a) CH$_3$-CH=CH-CH$_3$ + Cl$_2$ $\xrightarrow{\text{CCl}_4}$ CH$_3$-CHCl-CHCl-CH$_3$ (2,3-diclorobutano); (b) CH$_3$-CH=CH-CH$_3$ + HI → CH$_3$-CH$_2$-CHI-CH$_3$ (2-yodobutano). Añadir el recuento de átomos y la frase sobre la simetría del alqueno.
3. **[MEDIA · SOLUCION_INCOMPLETA]** `guided_exercises[1].full_solution` — El enunciado pide «(a) Escribe la ecuación de su adición de Br$_2$», pero ni answer ni full_solution la escriben. full_solution es una plantilla («Procedimiento: <pistas> Conclusión: <respuesta>») y tampoco hace la comprobación del ajuste que pide (b).
   - *Texto actual:* ««Procedimiento: El anillo no se rompe… Conclusión: 1,2-dibromociclohexano, C$_6$H$_{10}$Br$_2$.»»
   - *Arreglo:* Escribir: C$_6$H$_{10}$ (ciclohexeno) + Br$_2$ $\xrightarrow{\text{CCl}_4}$ C$_6$H$_{10}$Br$_2$ (1,2-dibromociclohexano). Ajuste: 6 C, 10 H y 2 Br a cada lado. El anillo se conserva.
4. **[MEDIA · TEORIA_INCOMPLETA]** `keywords[5]` — El «grado de insaturación» y su fórmula $x+1-y/2$ aparecen en la palabra clave, el reto, flashcards[9] y summary.formulas[0], pero ningún bloque de teoría los explica (la fórmula solo sale en una pista del reto). summary.formulas[0] presenta «x+1-\frac{y}{2}» sin decir qué son x e y. Además, el concepto es periférico en el temario PAU.
   - *Texto actual:* «summary.formulas[0] = «x+1-\frac{y}{2}»; challenge_questions[0].hints[0]: «El grado de insaturación de un hidrocarburo C$_x$H$_y$ (…) es $x+1-y/2$»»
   - *Arreglo:* Añadir un párrafo breve en theory_blocks[3] que defina el grado de insaturación (cada doble enlace o anillo = 1; cada triple = 2), dé la fórmula para C$_x$H$_y$ con un ejemplo y explique que cada mol de H$_2$ adicionado lo reduce en 1, salvo los anillos. En summary.formulas escribir «Grado de insaturación de C_xH_y = x+1-y/2». También se puede quitar el concepto si se considera fuera de temario.
5. **[BAJA · CONCEPTO]** `theory_blocks[0].body` — Un doble enlace tiene un solo enlace π, así que «uno de los enlaces π del doble enlace» es incorrecto; solo el triple tiene dos.
   - *Texto actual:* ««se rompe uno de los enlaces π del doble enlace»»
   - *Arreglo:* «se rompe el enlace π del doble enlace (o uno de los dos enlaces π del triple)».
6. **[BAJA · CONCEPTO]** `worked_examples[0].interpretation` — El ejemplo es Br$_2$ en CCl$_4$ (producto 1,2-dibromoetano), pero la interpretación habla del «agua de bromo». En disolución acuosa el producto principal es la bromohidrina (2-bromoetanol), no el dibromuro. Lo mismo se repite en mcq[2].stem, que además afirma «dando un único producto».
   - *Texto actual:* ««Es la reacción clásica de 'decoloración del agua de bromo'»»
   - *Arreglo:* Escribir «decoloración de una disolución de bromo (en CCl$_4$, o agua de bromo): el color pardo desaparece porque el Br$_2$ se adiciona al doble enlace». En mcq[2] usar «decolora una disolución de Br$_2$ en CCl$_4$».
7. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — La adición a alquinos solo se describe con palabras, sin ninguna ecuación de ejemplo. mcq[3] y flashcards[7] la evalúan (alquino + exceso de HBr), pero la teoría no dice dónde quedan los dos Br (en el mismo carbono, por Markovnikov) ni muestra la hidrogenación parcial alquino → alqueno.
   - *Texto actual:* ««Por ejemplo, con exceso de Br$_2$ un alquino acaba totalmente saturado con cuatro átomos de halógeno.»»
   - *Arreglo:* Añadir ecuaciones: HC≡CH + Br$_2$ → CHBr=CHBr (1,2-dibromoeteno); + otro Br$_2$ → CHBr$_2$-CHBr$_2$ (1,1,2,2-tetrabromoetano); HC≡CH + H$_2$ → CH$_2$=CH$_2$ y, con exceso, → CH$_3$-CH$_3$.
8. **[BAJA · PLANTILLA]** `common_mistakes[1].why` — El «why» es una frase genérica sin contenido.
   - *Texto actual:* ««El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»»
   - *Arreglo:* «Se clasifica la reacción por el reactivo (X$_2$) en vez de por lo que le ocurre al sustrato (saturado o con enlace múltiple).»
9. **[BAJA · LATEX]** `flashcards[9].front` — La fórmula está fuera de modo matemático: el alumno ve literalmente «C_xH_y».
   - *Texto actual:* ««Fórmula del grado de insaturación de un hidrocarburo C_xH_y»»
   - *Arreglo:* Escribir C$_x$H$_y$.
10. **[BAJA · LATEX]** `theory_blocks[1].body` — Las ecuaciones no indican estados de agregación, como pide la convención del curso para ecuaciones químicas. Tampoco lo hacen worked_examples[*].solution ni exam_questions[1]. En química orgánica de PAU es tolerable, pero conviene ser coherente al menos en los ejemplos resueltos.
   - *Texto actual:* ««CH$_2$=CH$_2$ + Br$_2$ $\xrightarrow{\text{CCl}_4}$ CH$_2$Br-CH$_2$Br»»
   - *Arreglo:* Añadir los estados en los ejemplos resueltos, p. ej. CH$_2$=CH$_2$(g) + H$_2$(g) $\xrightarrow{\text{Pt}}$ CH$_3$-CH$_3$(g). También vale una nota que diga que en orgánica se omiten por convención.
11. **[BAJA · VERIFICAR]** `theory_blocks[2].body` — El éter como disolvente «habitual» de la hidrohalogenación no es una convención de los libros de PAU, que suelen escribir HX sin condiciones. Además es incoherente con la tabla de theory_blocks[1], que pone «éter» en la ecuación general pero no en el ejemplo, ni en exam_questions[1].
   - *Texto actual:* ««La hidrohalogenación suele escribirse en éter como disolvente»»
   - *Arreglo:* Quitar la referencia al éter («la hidrohalogenación no necesita condiciones especiales; reactividad HI > HBr > HCl») o hacerla coherente en la tabla, la ecuación general y los ejemplos.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [MEDIA · SOLUCION_INCOMPLETA] Solo hay "answer" (resultado), sin resolución razonada. (1): `guided_exercises[0]`. Ej.: «El but-2-eno, CH$_3$-CH=CH-CH$_3$, es un alqueno simétrico. (a) Escribe la ecuación ajustada de su adición de Cl$_2$ y n \|\| RESP: (a) CH$_3$-CHCl-CHCl-CH$_3$ (2,3-diclorobutano).…». Arreglo: Añadir full_solution paso a paso.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (7): `diagnostic_items[0].question`, `guided_exercises[0].statement`, `exercises[0].answer`, `exercises[1].answer`, `exam_questions[1].full_solution`, `exam_questions[1].full_solution`, `exam_questions[1].full_solution`. Ej.: «En el but-2-eno, CH$_3$-CH=CH-CH$_3$, ¿cuántos hidrógenos lleva cada uno de los dos carbonos». Arreglo: Sustituir el código por una descripción en texto.

#### Lección 15 — Regla de Markovnikov

**Valoración experta: MEDIA.** El contenido químico es correcto en lo esencial. El enunciado de la regla, la justificación por carbocationes, los productos mayoritarios y minoritarios y los test están bien (las claves son correctas). Los problemas son: un «error común» que contradice la respuesta correcta (exercises[0]); toda la lección escrita sin subíndices químicos (H2O, CH3…); nomenclatura antigua (2-metil-2-buteno); y una explicación imprecisa del efecto +I. A la teoría le faltan el caso en que los dos carbonos tienen igual número de H, un ejemplo con alquinos y, opcionalmente, la mención del efecto peróxido.

**Plan de arreglo:** 1) Corregir exercises[0].common_errors[0]. 2) Formatear todos los subíndices químicos (H$_2$O, CH$_3$…) y las fórmulas de summary.formulas y de la figura. 3) Actualizar los nombres a IUPAC (2-metilbut-2-eno, but-1-eno, 3-metilbut-1-eno). 4) Precisar el efecto +I y el distractor D de mcq[1]. 5) Ampliar el procedimiento: mismo número de H → mezcla, ejemplo con alquino. 6) Completar las soluciones del reto y de exercises[0], y corregir course_label.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `exercises[0].common_errors[0]` — El «error común» describe justo la respuesta correcta del ejercicio. En el 2-metilbut-2-eno, el Br SÍ se adiciona al carbono sin H, que es el más sustituido y donde está el carbocatión terciario. Presentarlo como error contradice la propia answer.
   - *Texto actual:* ««Adicionar el Br al carbono que no tiene H, pensando que ese es siempre el más sustituido y por tanto el que recibe el halógeno, sin comprobar antes dónde está realmente el carbocatión más estable.»»
   - *Arreglo:* Sustituirlo por el error real: «Adicionar el Br al carbono que tiene 1 H (C3), dando 2-bromo-3-metilbutano, CH$_3$-CHBr-CH(CH$_3$)-CH$_3$, que pasaría por un carbocatión secundario, menos estable».
2. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — Faltan casos que la PAU suele usar para comprobar que se entiende la regla. (1) Alquenos asimétricos cuyos dos carbonos del doble enlace tienen el mismo número de H, como el pent-2-eno + HBr: la regla no decide y se obtiene una mezcla aproximadamente equimolar de 2- y 3-bromopentano. (2) Aplicación a alquinos, que la teoría menciona sin ningún ejemplo: propino + HBr → 2-bromopropeno; con exceso → 2,2-dibromopropano. (3) La adición anti-Markovnikov de HBr en presencia de peróxidos, aunque sea solo como mención.
   - *Texto actual:* «El procedimiento solo contempla «el carbono con más H» frente al «carbono con menos H».»
   - *Arreglo:* Añadir al procedimiento: «si los dos carbonos tienen el mismo número de H, la regla no decide y se obtiene una mezcla». Añadir un ejemplo con alquino. Opcional, según el temario autonómico: una nota sobre el HBr con peróxidos (anti-Markovnikov).
3. **[MEDIA · LATEX]** `theory_blocks[2].body` — Toda la lección escribe las fórmulas químicas sin subíndices: H2O, CH3-CH=CH2, (CH3)2C=CH2, C3H6, C3H7Br, CH3-CH$^+$-CH3… Son unas 66 líneas de show.py, en objectives, prerequisites, theory_blocks[0-3], worked_examples, guided_exercises, exercises, exam_questions, mcq, flashcards, misconceptions, exam_notes y summary. Es incoherente con las demás lecciones de la unidad (CH$_3$) y se ve mal.
   - *Texto actual:* «theory_blocks[2]: «la parte nucleofílica (X$^-$ o H2O) ataca ese carbocatión»; worked_examples[0].reasoning[3]: «C3H6 + HBr da C3H7Br»»
   - *Arreglo:* Pasar todos los subíndices a formato: H$_2$O, CH$_3$-CH=CH$_2$, (CH$_3$)$_2$C=CH$_2$, C$_3$H$_6$, CH$_3$-CH$^+$-CH$_3$, etc. Se puede hacer con una sustitución por regex (letra o paréntesis seguido de dígitos → $_n$) en los campos visibles, revisando después los localizadores C1, C2…
4. **[BAJA · CONCEPTO]** `theory_blocks[2].body` — La justificación del efecto +I es imprecisa. Afirma que un grupo alquilo es «menos electronegativo que el carbono positivo vecino», cuando el grupo alquilo está unido al carbono a través de otro carbono. Lo que se suele enseñar es que los grupos alquilo son dadores de densidad electrónica (+I) respecto al H. La idea se repite en mcq[1].options[2].why_wrong y en prerequisites[2]. Además, en mcq[1] el distractor D («menos átomos de H unidos al carbono con la carga») es prácticamente equivalente a la opción correcta A en un carbocatión alquílico.
   - *Texto actual:* ««un grupo alquilo, al ser menos electronegativo que el carbono positivo vecino, le cede densidad electrónica»»
   - *Arreglo:* Reformular: «los grupos alquilo son dadores de electrones (efecto inductivo +I) frente al H: ceden densidad electrónica al carbono con carga positiva y la dispersan». Cambiar el distractor D de mcq[1] por uno claramente falso, p. ej. «porque el terciario tiene menos impedimento estérico».
5. **[BAJA · CONCEPTO]** `guided_exercises[1].full_solution` — El orden de los pasos está invertido. El carbocatión secundario se forma al adicionarse el H$^+$, no el I; el I$^-$ entra después.
   - *Texto actual:* ««el carbono interno (1 H) recibe el I, generando un carbocatión secundario»»
   - *Arreglo:* «El H$^+$ se adiciona al carbono terminal, generando un carbocatión secundario en el C2; después el I$^-$ ataca ese carbono».
6. **[BAJA · SOLUCION_INCOMPLETA]** `exercises[0].full_solution` — La solución no nombra el producto minoritario ni el carbocatión secundario alternativo con el que se compara el terciario. Se limita a decir que el H va al carbono «que ya tiene H».
   - *Texto actual:* ««El H del HBr se adiciona al carbono que ya tiene H (el derecho), generando el carbocatión terciario…»»
   - *Arreglo:* Añadir: «El camino alternativo (H al C2) daría el carbocatión secundario CH$_3$-CH$^+$-CH(CH$_3$)-CH$_3$… y el 2-bromo-3-metilbutano, minoritario».
7. **[BAJA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — La solución explica la transposición de hidruro, pero no nombra los productos. Tampoco aclara que experimentalmente el producto transpuesto suele ser el mayoritario. Las transposiciones de carbocationes quedan además fuera del temario PAU (aceptable solo como reto).
   - *Texto actual:* ««este reordenamiento es favorable y compite con la adición directa»»
   - *Arreglo:* Añadir: «Productos: 2-cloro-3-metilbutano (adición directa, vía carbocatión secundario) y 2-cloro-2-metilbutano (tras la transposición, vía carbocatión terciario), que suele ser el mayoritario». Añadir también: «(contenido de ampliación, no exigido en PAU)».
8. **[BAJA · LATEX]** `summary.formulas[0]` — En summary.formulas los símbolos químicos están en modo matemático sin \mathrm, así que se ven en cursiva (HBr, CHBr, CH_3 como variables). Lo mismo pasa en las etiquetas de la figura theory_blocks[2].assets[0].svg.
   - *Texto actual:* ««\text{propeno} + HBr \rightarrow CH_3-CHBr-CH_3\ (\text{mayoritario})…»»
   - *Arreglo:* Usar \mathrm{HBr}, \mathrm{CH_3{-}CHBr{-}CH_3}, etc., o \ce{} si estuviera disponible. Regenerar la figura con las fórmulas en redonda.
9. **[BAJA · VISUAL]** `theory_blocks[2].assets[0].svg` — En la figura de estabilidad de carbocationes, las fórmulas están en cursiva matemática y el rótulo «terciario: 3 grupos alquilo» aparece cortado como «3 gru- / pos alquilo».
   - *Texto actual:* «Rótulo inferior derecho: «terciario: 3 gru- pos alquilo»»
   - *Arreglo:* Ensanchar la caja de texto o reducir la fuente para que no se parta la palabra, y poner las fórmulas en redonda.
10. **[BAJA · ESTRUCTURA]** `course_label` — El course_label no sigue el patrón de las demás lecciones de la unidad («Química · 2º Bachillerato · <título de la lección>»).
   - *Texto actual:* ««Química · 2º Bachillerato · Química del carbono e isomería»»
   - *Arreglo:* «Química · 2º Bachillerato · Regla de Markovnikov».
11. **[BAJA · ERRATA]** `exercises[0].statement` — Se usa nomenclatura anterior a IUPAC 1993/2005 («2-metil-2-buteno»), mientras el resto de la unidad usa but-2-eno o but-1-eno. Lo mismo ocurre en diagnostic_items[0].remediation_action («1-buteno») y challenge_questions[0].statement («3-metil-1-buteno»).
   - *Texto actual:* ««2-metil-2-buteno» / «1-buteno» / «3-metil-1-buteno»»
   - *Arreglo:* Escribir 2-metilbut-2-eno, but-1-eno y 3-metilbut-1-eno.

**Chequeos automáticos:**

- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH3". (1): `exercises[0].statement`. Ej.: «yoritario de la adición de HBr al 2-metil-2-buteno, (CH3)2C=CH-CH3, e indica el tipo de carbocatión intermedio implicado.». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH". (1): `challenge_questions[0].statement`. Ej.: «El 3-metil-1-buteno, CH2=CH-CH(CH3)-CH3, reacciona con HCl. Si la adición siguiera ingenua». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · TEXTO_PARA_PROFESOR] Texto dirigido al profesor/corrector en lugar de al alumno. (1): `misconceptions[0].diagnostic_signal`. Ej.: «Al predecir el producto, el alumno mira qué átomo está escrito primero en la fórmula en vez de contar los H de cad». Arreglo: Reescribir en segunda persona dirigido al alumno.

#### Lección 16 — Eliminación y deshidratación

**Valoración experta: MEDIA.** Teoría correcta pero escueta: faltan las condiciones que deciden el producto (KOH acuoso → sustitución vs alcohólico → eliminación; H2SO4 a 170 °C → alqueno vs 140 °C → éter). El ejercicio guiado 1 tiene numeración del Cl contradictoria (pista/answer/solución) y respuesta sin apartado (b); el caso del metanol enseña que «no puede deshidratarse», lo cual es falso (da dimetil éter). Presentación: casi todas las fórmulas en texto plano sin subíndices.

**Plan de arreglo:** 1) Corregir la numeración del Cl en guided_exercises[0] y completar su answer (b). 2) Corregir el caso del metanol (exercises[1], flashcards[6]) mencionando el dimetil éter. 3) Añadir a la teoría las condiciones KOH(aq)/KOH(alc) y 140/170 °C. 4) Corregir worked_examples[0].common_mistake (C1/C2). 5) Pasar fórmulas a LaTeX \mathrm con subíndices; reubicar los ejercicios Zn/NaNH2 como ampliación.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `guided_exercises[0].hints[0]` — La pista sitúa el Cl en el C2, la respuesta lo sitúa en el C1 y la solución completa vuelve a ponerlo en el C2: tres afirmaciones contradictorias en el mismo ejercicio. Según la IUPAC (cloroetano), el Cl está en el C1 y el vecino es el C2 (CH3).
   - *Texto actual:* «El Cl está en el C2; su único vecino es el C1.»
   - *Arreglo:* Unificar: «El Cl está en el C1 (CH2Cl); su único vecino es el C2 (CH3)», y corregir igual full_solution.
2. **[ALTA · CONCEPTO]** `guided_exercises[0].full_solution` — Numeración contraria a la IUPAC y a la respuesta: dice que el C2 lleva el Cl y que el C1 es el CH3.
   - *Texto actual:* «En CH3-CH2Cl, el C2 lleva el Cl; su único carbono vecino es el C1, el grupo CH3. El H que se elimina sale del C1, y el Cl sale del C2»
   - *Arreglo:* «En CH3-CH2Cl, el C1 (CH2Cl) lleva el Cl; su único vecino es el C2 (CH3). El H sale del C2 y el Cl del C1...». Separar además (a) y (b) en párrafos.
3. **[MEDIA · CONCEPTO]** `exercises[1].full_solution` — Afirma que la deshidratación «no es aplicable al metanol» sin matizar que solo se descarta la deshidratación intramolecular (a alqueno); el alumno puede concluir que el metanol no reacciona con H2SO4 caliente, cuando forma dimetil éter.
   - *Texto actual:* «Por eso esta reacción de deshidratación, tal como se ha definido, no es aplicable al metanol»
   - *Arreglo:* Añadir: «Lo que sí ocurre es una deshidratación intermolecular: 2 CH3OH → CH3-O-CH3 + H2O (dimetil éter/metoximetano)».
4. **[MEDIA · CONCEPTO]** `flashcards[6].back` — «El metanol no puede deshidratarse» es falso en sentido general: no puede dar alqueno, pero sí se deshidrata a dimetil éter.
   - *Texto actual:* «sin él, no hay eliminación posible (p. ej. el metanol no puede deshidratarse).»
   - *Arreglo:* «...sin él no puede formarse un alqueno (p. ej. el metanol no da ningún alqueno; con H2SO4 solo forma dimetil éter por deshidratación intermolecular).»
5. **[MEDIA · CONCEPTO]** `worked_examples[0].common_mistake` — Contradice la numeración del propio ejemplo: el razonamiento dice que el Br está en el C1, pero el error típico habla del Br «en el C2».
   - *Texto actual:* «Escribir el doble enlace solo «donde estaba el Br» (en el C2) sin extenderlo hasta el C1»
   - *Arreglo:* «Escribir el doble enlace solo «donde estaba el Br» (en el C1) sin extenderlo hasta el C2...».
6. **[MEDIA · ENUNCIADO]** `exercises[1].statement` — El enunciado pide «Clasifica esta reacción y escribe su ecuación ajustada» para la deshidratación del metanol, pero la solución concluye que no existe tal reacción. Además es químicamente incompleto: el metanol con H2SO4 y calor SÍ se deshidrata, de forma intermolecular, dando dimetil éter.
   - *Texto actual:* «Clasifica esta reacción y escribe su ecuación ajustada: deshidratación del metanol, CH3OH, con H2SO4 y calor.»
   - *Arreglo:* Reformular: «¿Puede el metanol dar un alqueno por deshidratación con H2SO4 y calor? Justifícalo. ¿Qué producto se obtiene en realidad?» y completar la solución: no puede formar alqueno (no hay C vecino), pero se deshidrata entre dos moléculas: $2\,\mathrm{CH_3OH} \xrightarrow{\mathrm{H_2SO_4},\ \Delta} \mathrm{CH_3{-}O{-}CH_3} + \mathrm{H_2O}$ (metoximetano).
7. **[MEDIA · SOLUCION_INCOMPLETA]** `guided_exercises[0].answer` — La respuesta solo contiene el apartado (a); falta el (b): ecuación ajustada y nombre del producto.
   - *Texto actual:* «(a) El Cl está en el C1; su vecino es el C2 (CH3)»
   - *Arreglo:* «(a) El Cl está en el C1; su vecino es el C2 (CH3). (b) CH3-CH2Cl + KOH →(etanol, Δ)→ CH2=CH2 + KCl + H2O; producto: eteno.»
8. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — No se indica la temperatura ni la competencia con la formación de éter, típica de PAU: el etanol con H2SO4 concentrado a ~170-180 °C da eteno (eliminación), mientras que a ~140 °C da dietil éter (deshidratación intermolecular). Sin esto el alumno no puede contestar preguntas del tipo «¿qué se obtiene a 140 °C?».
   - *Texto actual:* «se deshidrata calentándolo con un ácido fuerte (típicamente H2SO4)»
   - *Arreglo:* Añadir un párrafo: «Con H2SO4 concentrado a unos 170 °C se obtiene el alqueno; a temperatura más baja (≈140 °C) y con exceso de alcohol predomina la deshidratación entre dos moléculas: 2 CH3CH2OH → CH3CH2-O-CH2CH3 + H2O (etoxietano)».
9. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — No se explica por qué el medio debe ser alcohólico: con KOH en disolución acuosa el haloalcano da mayoritariamente sustitución (alcohol), y en medio alcohólico/caliente predomina la eliminación. Es una distinción clásica en la PAU y la lección 18 la da por sabida.
   - *Texto actual:* «reacciona con una base fuerte (típicamente KOH, en medio alcohólico)»
   - *Arreglo:* Añadir un caveat: «KOH(aq) → sustitución: CH3CH2Br + KOH → CH3CH2OH + KBr; KOH en etanol y calor → eliminación: CH2=CH2 + KBr + H2O. Las condiciones deciden el producto».
10. **[MEDIA · LATEX]** `worked_examples[0].solution` — Toda la lección (soluciones, respuestas, fichas, test, resumen) escribe fórmulas en texto plano con subíndices sin formato (CH3-CH2Br, H2SO4, CH2=CH2) y flechas «→(H2SO4, Δ)→». Solo la teoría usa $...$.
   - *Texto actual:* «CH3-CH2Br + KOH → CH2=CH2 + KBr + H2O (eteno).»
   - *Arreglo:* Pasar todas las fórmulas y ecuaciones a $\mathrm{...}$ con subíndices y \xrightarrow{} para las condiciones (afecta a worked_examples, guided_exercises, exercises, exam_questions, challenge, mcq, flashcards, summary.key_points, diagnostic_items).
11. **[BAJA · CONCEPTO]** `mcq[2].explanation` — Dice que el calor «actúa de forma catalítica», lo cual no tiene sentido: el calor no es un catalizador. Además el H2SO4 concentrado actúa también como agente deshidratante.
   - *Texto actual:* «El H2SO4 concentrado y el calor favorecen la deshidratación, pero actúan de forma catalítica»
   - *Arreglo:* «El H2SO4 concentrado actúa como catalizador (y deshidratante); el calor aporta la energía necesaria. El ácido no aparece en el balance de átomos.»
12. **[BAJA · LATEX]** `theory_blocks[1].body` — Las ecuaciones químicas se escriben en modo matemático sin \mathrm (C, H, K, O en cursiva) y sin estados de agregación, contra la convención del curso. El título del bloque 2 lleva «H2O»/«H2SO4» sin subíndices.
   - *Texto actual:* «$CH_3-CH_2Br + KOH \xrightarrow{\text{medio alcohólico}} CH_2=CH_2 + KBr + H_2O$»
   - *Arreglo:* Usar \mathrm{...} (o \ce) y estados: $\mathrm{CH_3{-}CH_2Br\,(l) + KOH\,(alc) \xrightarrow{etanol,\ \Delta} CH_2{=}CH_2\,(g) + KBr + H_2O}$; títulos «H₂O», «H₂SO₄».
13. **[BAJA · LATEX]** `summary.key_points[0]` — Ecuación general en texto plano con notación improvisada «→(alc.)→» mientras summary.formulas tiene la misma en LaTeX.
   - *Texto actual:* «>C(H)-C(X)< + KOH →(alc.)→ >C=C< + KX + H2O; el KOH se consume.»
   - *Arreglo:* Escribirla en $...$ como en summary.formulas o remitir a la fórmula.
14. **[BAJA · NIVEL]** `exercises[0].statement` — La deshalogenación de dihalogenuros vecinales con Zn no figura en el temario PAU y no se trata en la teoría (lo admite el propio enunciado). Ejercicio de ampliación en la sección de ejercicios estándar.
   - *Texto actual:* «(**Ampliación**: esta reacción de deshalogenación vecinal con Zn no se trata en los bloques teóricos de la lección»
   - *Arreglo:* Moverlo a challenge_questions o sustituirlo por un ejercicio del temario (p. ej. 2-cloropropano + KOH alcohólico → propeno + KCl + H2O).
15. **[BAJA · NIVEL]** `challenge_questions[0].statement` — El uso de NaNH2 (amiduro de sodio) excede el nivel PAU y no se menciona en la teoría; en Bachillerato suele usarse KOH alcohólico en exceso y calor para la doble eliminación. El cálculo de ajuste es correcto.
   - *Texto actual:* «con dos equivalentes de una base fuerte (NaNH2)»
   - *Arreglo:* Mantener como reto pero indicar la alternativa de nivel: «CH2Br-CH2Br + 2 KOH →(etanol, Δ)→ CH≡CH + 2 KBr + 2 H2O», o añadir una nota en la teoría.
16. **[BAJA · ERRATA]** `theory_blocks[3].body` — Inciso abierto con raya «—por ejemplo, ...» que se cierra con una coma.
   - *Texto actual:* «—por ejemplo, un haloalcano o un alcohol con una cadena más larga a ambos lados del grupo saliente, la eliminación»
   - *Arreglo:* «—por ejemplo, un haloalcano o un alcohol con cadena a ambos lados del grupo saliente—, la eliminación...». Conviene añadir un ejemplo concreto (2-bromobutano → but-2-eno / but-1-eno).

#### Lección 17 — Regla de Saytzeff/Zaitsev

**Valoración experta: MEDIA.** Teoría clara y bien estructurada (procedimiento en 4 pasos y tabla Markovnikov/Saytzeff), con ejemplos correctos (2-bromobutano, butan-2-ol, 2-bromo-2-metilbutano, pentan-2-ol). Problemas: repite en varios sitios que en la eliminación no interviene ningún carbocatión (falso en la deshidratación ácida), ignora la isomería E/Z de los productos (el caso 3-bromopentano se da como «un único alqueno»), dos «why» de plantilla y todas las fórmulas en texto plano sin subíndices.

**Plan de arreglo:** 1) Eliminar la afirmación «no hay carbocatión» (exercises[2], worked_examples[2], mcq[0], misconceptions[0]) y formularla como «se comparan los alquenos producto». 2) Añadir a la teoría la mezcla E/Z del alqueno Saytzeff (E mayoritario) y matizar el caso 3-bromopentano (exam_questions[0], summary, mcq[3], flashcards[6]). 3) Reescribir common_mistakes[0..1].why. 4) Pasar todas las fórmulas a LaTeX \mathrm y ajustar summary.formulas. 5) Retocar figura y sustituir el reto.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `exercises[2].full_solution` — Afirma que en Saytzeff no interviene ningún carbocatión. Es falso para la deshidratación ácida de alcoholes secundarios/terciarios (la propia reacción de la lección, p. ej. butan-2-ol con H2SO4), que transcurre a través de un carbocatión (E1) del que se pierde un H+ dando el alqueno más estable. Lo correcto es que la regla compara la estabilidad de los alquenos producto, haya o no carbocatión intermedio.
   - *Texto actual:* «No hay ningún carbocatión involucrado en el razonamiento de Saytzeff.»
   - *Arreglo:* «El criterio de Saytzeff es la estabilidad de los alquenos producto (aunque en la deshidratación ácida de un alcohol sí se forma un carbocatión intermedio, la regla no se razona comparando carbocationes, sino comparando los alquenos que pueden formarse).»
2. **[MEDIA · CONCEPTO]** `worked_examples[2].common_mistake` — Dice que la deshidratación del butan-2-ol no pasa por «ningún carbocatión intermedio»; en realidad la deshidratación ácida de un alcohol secundario sí pasa por un carbocatión secundario (mecanismo E1).
   - *Texto actual:* «que en realidad compara la estabilidad de los alquenos producto, no de ningún carbocatión intermedio.»
   - *Arreglo:* «...que en realidad se decide comparando la estabilidad de los alquenos producto (el carbocatión, si se forma, es el mismo para ambos caminos y no permite elegir).»
3. **[MEDIA · CONCEPTO]** `exam_questions[0].answer` — El curso trata la isomería E/Z (lección 12): el 3-bromopentano da pent-2-eno, que existe como (E) y (Z). Responder «un único alqueno» y «único producto» es incorrecto si se pregunta por «alquenos distintos»: se obtiene un único isómero de posición (pent-2-eno) como mezcla de (E)-pent-2-eno (mayoritario, más estable) y (Z)-pent-2-eno.
   - *Texto actual:* «(a) Un único alqueno, porque el 3-bromopentano es simétrico. (b) Pent-2-eno, CH3-CH2-CH=CH-CH3, es el único producto»
   - *Arreglo:* «(a) Un único isómero de posición, pent-2-eno, por la simetría del sustrato (aunque se forma como mezcla de E y Z, predominando el E). (b) CH3-CH2-CH=CH-CH3; no hay que elegir entre isómeros de posición.» Ajustar el enunciado a «¿Cuántos isómeros de posición...?».
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — No se menciona que el producto Saytzeff but-2-eno (y pent-2-eno, 2-metil... ) presenta isomería geométrica, y que el isómero E (trans) es el mayoritario por ser más estable. Las preguntas PAU que combinan eliminación e isomería lo piden, y la lección 12 del curso lo cubre.
   - *Texto actual:* «El but-2-eno, al ser el más sustituido, es el producto mayoritario; el but-1-eno es el minoritario.»
   - *Arreglo:* Añadir: «El but-2-eno se forma como mezcla de (E)- y (Z)-but-2-eno; predomina el (E), con los dos CH3 en lados opuestos, por menor repulsión estérica.»
5. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Frase genérica que no explica por qué se produce el error (es idéntica en common_mistakes[1].why).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Ambas reglas premian lo ‘más sustituido’ y comparten vocabulario, por lo que se funden en una sola.»
6. **[MEDIA · PLANTILLA]** `common_mistakes[1].why` — Misma frase de relleno; no explica la causa del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* «Se interpreta ‘mayoritario’ como ‘único’, leyendo la regla como absoluta en vez de como una predicción de proporciones.»
7. **[MEDIA · LATEX]** `worked_examples[0].solution` — La lección no tiene ni una fórmula en LaTeX fuera del resumen: todas las fórmulas y ecuaciones (teoría, ejemplos, ejercicios, test, fichas) van en texto plano con subíndices sin formato (CH3-CHBr-CH2-CH3, H2SO4) y flechas «→(alc.)→». Tampoco hay estados de agregación.
   - *Texto actual:* «CH3-CHBr-CH2-CH3 + KOH →(alc.)→ CH3-CH=CH-CH3 (but-2-eno, mayoritario)»
   - *Arreglo:* Convertir todas las fórmulas a $\mathrm{...}$ con subíndices y \xrightarrow{\text{etanol},\ \Delta}; aplicar a toda la lección.
8. **[BAJA · CONCEPTO]** `mcq[0].options[1].why_wrong` — Misma afirmación falsa: «sin carbocationes intermedios». La clave (D) es correcta, pero la justificación del distractor enseña algo falso sobre la deshidratación de alcoholes.
   - *Texto actual:* «que compara directamente la estabilidad de los alquenos producto, sin carbocationes intermedios.»
   - *Arreglo:* «...Saytzeff compara la estabilidad de los alquenos producto, no la de carbocationes.»
9. **[BAJA · CONCEPTO]** `misconceptions[0].correct_model` — Repite que en la eliminación no hay «ningún intermedio catiónico», lo que no es cierto para la deshidratación ácida (E1). Afecta también a objectives[2] y summary.big_idea, que oponen «producto de eliminación» a «intermedio de adición» como si fueran excluyentes.
   - *Texto actual:* «(el criterio es la estabilidad del propio alqueno producto, no de ningún intermedio catiónico)»
   - *Arreglo:* Quitar «no de ningún intermedio catiónico» y decir «el criterio es la estabilidad del alqueno producto».
10. **[BAJA · CONCEPTO]** `summary.key_points[4]` — «No hay dos productos distintos que comparar» ignora la mezcla E/Z del pent-2-eno; lo mismo en mcq[3], flashcards[6] y exam_notes[2].
   - *Texto actual:* «si el sustrato es simétrico respecto al grupo saliente (como el 3-bromopentano), no hay dos productos distintos que comparar.»
   - *Arreglo:* «...no hay dos isómeros de posición que comparar (sí puede haber isómeros E/Z del mismo alqueno).»
11. **[BAJA · LATEX]** `summary.formulas[0]` — La ecuación del resumen no está ajustada (faltan KBr y H2O) y mezcla texto y fórmulas en cursiva sin \mathrm.
   - *Texto actual:* «\text{2-bromobutano} + KOH \rightarrow CH_3-CH=CH-CH_3\ (\text{mayoritario}) + CH_2=CH-CH_2-CH_3\ (\text{minoritario})»
   - *Arreglo:* $\mathrm{CH_3CHBrCH_2CH_3 + KOH \xrightarrow{etanol,\ \Delta} CH_3CH{=}CHCH_3}$ (mayoritario) $\mathrm{+\ CH_2{=}CHCH_2CH_3}$ (minoritario) $\mathrm{+\ KBr + H_2O}$.
12. **[BAJA · LATEX]** `theory_blocks[3].body` — En la tabla, «H2O», «HX» y «3º>2º>1º» en texto plano.
   - *Texto actual:* «Adición (HX, H2O a un alqueno)»
   - *Arreglo:* Usar $\mathrm{H_2O}$ y $3^{\text{o}} > 2^{\text{o}} > 1^{\text{o}}$.
13. **[BAJA · VISUAL]** `theory_blocks[1].assets[0].svg` — En la figura, el eje vertical «estabilidad creciente» atraviesa la fórmula del but-1-eno (se superpone a «CH2»); las fórmulas aparecen en cursiva (sin \mathrm) y los pies de las barras están mal divididos en sílabas («may-oritario», «mi-noritario»).
   - *Texto actual:* «but-2-eno (may- oritario, más sustituido)»
   - *Arreglo:* Desplazar el eje a la izquierda de la fórmula, usar \mathrm en las fórmulas y evitar el corte de palabra (o cortar «ma-yoritario»).
14. **[BAJA · NIVEL]** `challenge_questions[0].statement` — El reto (difícil 5) es trivial conceptualmente (que la hidrogenación posterior no cambia la proporción de la eliminación) y no exige razonamiento químico de nivel reto; desaprovecha la sección.
   - *Texto actual:* «Explica por qué este hecho (que los dos alquenos posibles lleven al mismo alcano por hidrogenación) no contradice»
   - *Arreglo:* Sustituirlo por un reto real, p. ej.: deshidratación del 2-metilbutan-2-ol o del 3-metilbutan-2-ol (alquenos posibles, mayoritario e isomería E/Z del producto).
15. **[BAJA · ERRATA]** `theory_blocks[0].body` — Inciso con raya abierto y no cerrado.
   - *Texto actual:* «—lo más habitual cuando el grupo saliente no está en un extremo de la cadena, la eliminación puede»
   - *Arreglo:* «—lo más habitual cuando el grupo saliente no está en un extremo de la cadena—, la eliminación puede...»

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH3". (11): `diagnostic_items[0].question`, `theory_blocks[1].body`, `worked_examples[0].solution`, `worked_examples[1].solution`, `guided_exercises[0].answer`, `exercises[1].answer`, `exam_questions[0].answer`, `exam_questions[0].full_solution`, `exam_questions[1].answer`, `flashcards[7].back`, `flashcards[10].back`. Ej.: «para el but-1-eno, CH3-CH2-CH=CH2, con el but-2-eno, CH3-CH=CH-CH3. ¿Cuántos grupos alquilo (distintos de H) llevan los carbon». Arreglo: Sustituir el código por una descripción en texto.

#### Lección 18 — Reacciones de sustitución

**Valoración experta: MEDIA.** Teoría bien orientada (saliente/atacante, alcoholes, nitrilos, aminas, X2 adición vs sustitución) y ejemplos correctos, pero falta la sustitución de alcoholes con HX y Williamson se usa sin teoría. El reto tiene ecuaciones sin ajustar y contradictorias entre answer y full_solution; la figura del esquema general dibuja la flecha del grupo saliente desde R. Un ejercicio estándar sin datos («para cada haloalcano»), tres «why» de plantilla y fórmulas en texto plano.

**Plan de arreglo:** 1) Ajustar y unificar las ecuaciones del reto (2 NH3; 2 etilaminas o + HBr) y usar nombres IUPAC. 2) Redibujar la figura (flechas desde A y hacia B). 3) Dar un sustrato concreto en exercises[0]. 4) Añadir a la teoría R-OH + HX y la síntesis de Williamson; aclarar SN1/SN2. 5) Reescribir common_mistakes[*].why. 6) Pasar fórmulas a LaTeX \mathrm con estados.

**Hallazgos de la revisión experta:**

1. **[ALTA · CALCULO]** `challenge_questions[0].answer` — Las dos ecuaciones de la respuesta están sin ajustar. Paso 1: CH3CH2Br + NH3 → CH3CH2NH2 + NH4Br tiene 1 N a la izquierda y 2 a la derecha (hacen falta 2 NH3, como la propia lección enseña). Paso 2: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + CH3CH2NH3⁺Br⁻ tiene C3H10NBr a la izquierda y C5H17N2Br a la derecha (faltan una segunda etilamina).
   - *Texto actual:* «Paso 1: CH3CH2Br + NH3(exceso) → CH3CH2NH2 + NH4Br (etilamina). Paso 2: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + CH3CH2NH₃⁺·Br⁻»
   - *Arreglo:* Paso 1: CH3CH2Br + 2 NH3 → CH3CH2NH2 + NH4Br. Paso 2: 2 CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + CH3CH2NH3⁺Br⁻ (o bien CH3CH2NH2 + CH3Br → CH3CH2NHCH3 + HBr, escrito igual en answer y full_solution).
2. **[MEDIA · SOLUCION_EQUIVOCADA]** `challenge_questions[0].full_solution` — La solución completa escribe el paso 2 con «+ HBr» mientras la respuesta da «+ CH3CH2NH3⁺·Br⁻»; y repite el paso 1 sin ajustar («+ NH3(exceso)» con coeficiente 1). Además, el producto se llama «etilmetilamina»: el nombre IUPAC es N-metiletanamina (o etil(metil)amina), y «1-bromoetano» lleva un localizador innecesario (bromoetano).
   - *Texto actual:* «CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + HBr»
   - *Arreglo:* Unificar la ecuación con answer, ajustar el paso 1 con 2 NH3, nombrar N-metiletanamina y usar «bromoetano». Puede comentarse que en la práctica la alquilación directa da mezclas.
3. **[MEDIA · ENUNCIADO]** `exercises[0].statement` — Dice «Para cada haloalcano» pero no da ningún haloalcano; el ejercicio queda genérico y la respuesta no puede nombrar productos.
   - *Texto actual:* «Para cada haloalcano, indica el reactivo (y el medio) que habría que usar para obtener»
   - *Arreglo:* Dar un sustrato concreto: «A partir del 1-bromobutano, indica el reactivo y el medio para obtener: (a) butan-1-ol; (b) pentanonitrilo; (c) butan-1-amina», y añadir las ecuaciones a la solución.
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — Falta la sustitución en alcoholes con hidrácidos (R-OH + HX → R-X + H2O), muy habitual en la PAU (p. ej. etanol + HBr → bromoetano), y la síntesis de Williamson aparece como keyword, ejercicio guiado y ficha sin explicarse en la teoría.
   - *Texto actual:* «Cambiando solo el nucleófilo que ataca al haloalcano se accede a tres funciones orgánicas distintas»
   - *Arreglo:* Añadir: «**Alcoholes → haloalcanos**: $\mathrm{CH_3CH_2OH + HBr \rightarrow CH_3CH_2Br + H_2O}$» y «**Éteres (Williamson)**: $\mathrm{R{-}X + R'O^- \rightarrow R{-}O{-}R' + X^-}$».
5. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Frase de relleno idéntica en common_mistakes[0], [1] y [2]; no explica la causa del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: «Se mira la carga de las especies en los productos en vez de rastrear qué estaba unido al carbono antes». [1]: «Se memoriza ‘halógeno + compuesto orgánico = adición’ sin mirar si hay enlace múltiple». [2]: «Se trata la síntesis como si se detuviera sola en el primer producto».
6. **[MEDIA · LATEX]** `worked_examples[0].solution` — Toda la lección (salvo tres fórmulas de la teoría y el resumen) escribe fórmulas en texto plano sin subíndices (CH3CH2CH2Br, NH4Cl, 2NH3) y condiciones con «→(etanol)→». Las ecuaciones de la teoría usan letras en cursiva sin \mathrm y no hay estados de agregación.
   - *Texto actual:* «CH3CH2CH2Br + NaOH → CH3CH2CH2OH + NaBr (propan-1-ol).»
   - *Arreglo:* Pasar todas las fórmulas a $\mathrm{...}$ con subíndices, \xrightarrow{\text{etanol}} y estados de agregación (aq), (l), (g).
7. **[MEDIA · VISUAL]** `theory_blocks[1].assets[0].svg` — La flecha «grupo saliente» parte de R (no de A) y termina en A⁻: el diagrama sugiere que el grupo saliente es la cadena R. La flecha «atacante» parte de B⁻ y apunta a R del producto, no a B. Además los espacios separan «R» de «−A» y el guion parece un signo menos.
   - *Texto actual:* «grupo saliente (flecha que sale de R y llega a A⁻)»
   - *Arreglo:* Redibujar: flecha «grupo saliente» desde A (en R–A) hasta A⁻; flecha «atacante» desde B⁻ hasta B (en R–B); escribir R–A y R–B juntos con \mathrm.
8. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — «Dos variantes, SN1 y SN2, según si la sustitución ocurre en una o dos etapas» empareja el orden al revés de lo que sugiere la numeración: SN2 es en una etapa (concertada) y SN1 en dos (vía carbocatión). Además R no es «el sustrato» sino el grupo alquilo (el sustrato es R-A).
   - *Texto actual:* «existen dos variantes, SN1 y SN2, según si la sustitución ocurre en una o dos etapas»
   - *Arreglo:* «SN2: una sola etapa concertada; SN1: dos etapas, con un carbocatión intermedio (los números indican la molecularidad, no las etapas)». Y «R es el grupo alquilo (la parte del sustrato que no cambia)».
9. **[BAJA · CONCEPTO]** `guided_exercises[1].answer` — Nombre no IUPAC: «metil etil éter». Según la IUPAC el producto es metoxietano (nombre de clase funcional: etil metil éter, en orden alfabético).
   - *Texto actual:* «Un éter (metil etil éter); es la síntesis de Williamson.»
   - *Arreglo:* «Un éter, metoxietano (etil metil éter); síntesis de Williamson.» Corregir también en full_solution.
10. **[BAJA · MCQ]** `mcq[3].options[3].text` — La opción D («para neutralizar el ácido que se produce») es parcialmente cierta (la segunda molécula de NH3 actúa como base, como admite la propia why_wrong), por lo que puede considerarse correcta junto a C.
   - *Texto actual:* «Para neutralizar el ácido que se produce»
   - *Arreglo:* Cambiar el enunciado a «¿Cuál es la razón principal de usar un GRAN exceso...?» o sustituir D por un distractor claramente falso (p. ej. «Para que el amoniaco actúe como catalizador»).
11. **[BAJA · LATEX]** `summary.key_points[0]` — Ecuaciones en texto plano y pegadas, sin espacios ni formato.
   - *Texto actual:* «Esquema general: R-A+B⁻→R-B+A⁻;»
   - *Arreglo:* Usar $\mathrm{R{-}A + B^- \rightarrow R{-}B + A^-}$ (igual en key_points[1..3]).
12. **[BAJA · ERRATA]** `worked_examples[3].reasoning[1]` — Habla del «carbono del nitrilo» cuando se refiere al carbono del ion cianuro (el nucleófilo), lo que confunde reactivo y producto.
   - *Texto actual:* «es el carbono del nitrilo el que forma el enlace nuevo con el sustrato»
   - *Arreglo:* «es el carbono del ion cianuro (:C≡N⁻) el que forma el enlace nuevo...»
13. **[BAJA · ERRATA]** `theory_blocks[3].body` — Frase mal construida: «compite con el sustrato la posibilidad de eliminación».
   - *Texto actual:* «compite con el sustrato la posibilidad de eliminación (formar un alqueno) en vez de sustitución»
   - *Arreglo:* «...la base puede provocar eliminación (formar un alqueno) en lugar de sustitución, sobre todo si el haloalcano es terciario y se trabaja en etanol y en caliente.»
14. **[BAJA · VERIFICAR]** `theory_blocks[4].body` — La sustitución electrófila aromática se presenta como «no hace falta memorizar»; en varias comunidades la PAU incluye la nitración/halogenación del benceno. Conviene al menos una ecuación de ejemplo.
   - *Texto actual:* «No hace falta memorizar esta familia para PAU/EBAU con el mismo detalle»
   - *Arreglo:* Añadir: $\mathrm{C_6H_6 + HNO_3 \xrightarrow{H_2SO_4} C_6H_5NO_2 + H_2O}$ y $\mathrm{C_6H_6 + Br_2 \xrightarrow{FeBr_3} C_6H_5Br + HBr}$.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (3): `common_mistakes[0].why`, `common_mistakes[1].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 8 lecciones del curso (probable plantilla genérica). (1): `worked_examples[3].solution`. Ej.: «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 19 — Oxidación y reducción orgánica

**Valoración experta: MEDIA.** Lección bien enfocada (criterio de enlaces C-O/C-H, primario/secundario, PCC vs oxidantes fuertes, NaBH4 vs LiAlH4) y todos los ajustes con [O]/[H] y la combustión del butano son correctos. Pero theory_blocks[2] llama «suave» al reactivo de Jones y cuenta mal los escalones, en contradicción con el resto; la teoría no cubre alcoholes terciarios aunque se preguntan; se descarta el ajuste por ion-electrón, habitual en PAU. Tres «why» de plantilla y fórmulas en texto plano.

**Plan de arreglo:** 1) Reescribir theory_blocks[2] (Jones = fuerte, PCC = suave; escalones bien contados). 2) Añadir alcoholes terciarios y destilación del aldehído a theory_blocks[3]. 3) Incluir un ejemplo de ajuste ion-electrón (etanol + dicromato) y matizar exam_notes[3]/objectives[0]. 4) Precisar el criterio C-O/C-H y la rotura del éster. 5) Reescribir common_mistakes[*].why; fórmulas a LaTeX \mathrm; retocar figura.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `theory_blocks[2].body` — El bloque presenta el reactivo de Jones (CrO3/H2SO4) como oxidante SUAVE que lleva el alcohol al aldehído, y en la misma frase como oxidante fuerte «en exceso». Contradice el bloque siguiente (theory_blocks[3]), las fichas y los ejercicios, donde Jones/CrO3/H+ es fuerte y lleva el alcohol primario hasta ácido. Además cuenta mal los escalones: «alcohol → aldehído → ácido (tres escalones, cuatro especies si se incluye el alcano)» (son dos escalones; tres con el alcano), y «KMnO4 en frío ácido» es una condición confusa.
   - *Texto actual:* «Un oxidante suave (como el reactivo de Jones, CrO₃/H₂SO₄) lleva el alcohol al aldehído o a la cetona; un oxidante fuerte (KMnO₄ en frío ácido o el propio Jones en exceso) recorre los dos últimos escalones»
   - *Arreglo:* «El nivel de oxidación del carbono funcional sube en la serie alcano → alcohol → aldehído (o cetona) → ácido (tres escalones). Un oxidante suave (PCC) lleva el alcohol primario solo hasta aldehído; un oxidante fuerte (KMnO4 o K2Cr2O7 en medio ácido, reactivo de Jones CrO3/H2SO4) lo lleva hasta ácido. Un alcohol secundario da cetona con cualquiera de ellos. En sentido contrario, LiAlH4 baja el ácido hasta alcohol.»
2. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — La teoría no trata los alcoholes terciarios, pero el ejercicio estándar 2, el ejemplo 4(c), una ficha y los errores comunes los preguntan (solo se mencionan en misconceptions). Tampoco se menciona el truco clásico de PAU para aislar el aldehído con dicromato (destilarlo según se forma).
   - *Texto actual:* «Sobre un alcohol secundario, cualquiera de estos oxidantes (suave o fuerte) da el mismo resultado: cetona»
   - *Arreglo:* Añadir: «Un alcohol terciario (sin H en el carbono del OH) no se oxida en estas condiciones». Y: «con K2Cr2O7/H+ puede aislarse el aldehído si se destila a medida que se forma».
3. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Frase de relleno idéntica en common_mistakes[0], [1] y [2]; no explica la causa de cada error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: «Se traslada el método de redox inorgánico sin usar el atajo de los enlaces C-O/C-H». [1]: «Se generaliza el caso del alcohol primario a todos». [2]: «Se trata ‘reductor’ como etiqueta única sin distinguir su fuerza».
4. **[MEDIA · LATEX]** `worked_examples[0].solution` — Salvo una fórmula de la teoría y el resumen, todas las fórmulas de la lección van en texto plano sin subíndices (CH3CH2CH2OH, KMnO4, K2Cr2O7/H+, C4H10+O2→CO2+H2O) y las condiciones con «→(PCC)→». En los títulos y keywords aparece «KMnO4», «NaBH4», «LiAlH4» sin formato, mientras flashcards[11] sí usa KMnO$_4$ (incoherente).
   - *Texto actual:* «CH3CH2CH2OH + [O] →(PCC)→ CH3CH2CHO + H2O (propanal).»
   - *Arreglo:* Pasar todas las fórmulas a $\mathrm{...}$ con subíndices y \xrightarrow{\text{PCC}}; unificar notación en toda la lección.
5. **[MEDIA · VERIFICAR]** `exam_notes[3]` — La lección afirma (también en objectives[0], misconceptions[0], flashcards[6]) que en orgánica nunca se exige ajustar semirreacciones. En la PAU es muy frecuente ajustar por ion-electrón la oxidación de un alcohol con dicromato o permanganato (p. ej. etanol + K2Cr2O7/H2SO4 → ácido acético + Cr3+). Comprobar el temario de la comunidad y, en todo caso, incluir un ejemplo ajustado.
   - *Texto actual:* «No se exige calcular números de oxidación formales en orgánica: el criterio de enlaces C-O/C-H es el que se espera en la respuesta.»
   - *Arreglo:* Matizar: «Para decidir si hay oxidación basta el criterio de enlaces; pero si el enunciado da el oxidante concreto, puede pedirse ajustar por ion-electrón: $\mathrm{3\,CH_3CH_2OH + 2\,Cr_2O_7^{2-} + 16\,H^+ \rightarrow 3\,CH_3COOH + 4\,Cr^{3+} + 11\,H_2O}$» (comprobado: O 17/17, H 34/34, carga +12/+12).
6. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — «Gana enlaces C-O (o, equivalentemente, pierde enlaces C-H)»: no son equivalentes (la hidratación de un alqueno gana un C-O y un C-H y no es redox neta; la hidrogenación gana C-H sin perder C-O). Lo correcto es mirar el balance, y considerar también enlaces C-N y C-X como enlaces a heteroátomo.
   - *Texto actual:* «Oxidación: el carbono gana enlaces C-O (o, equivalentemente, pierde enlaces C-H).»
   - *Arreglo:* «Oxidación: aumenta el número de enlaces del carbono a O (o a otro heteroátomo más electronegativo) y/o disminuye el de enlaces C-H. Reducción: lo contrario (p. ej. la hidrogenación de un alqueno es una reducción).»
7. **[BAJA · CONCEPTO]** `worked_examples[2].reasoning[2]` — Descripción imprecisa de qué enlace se rompe en la reducción del éster: no se rompe «el enlace entre el oxígeno y los dos fragmentos», sino el enlace C(acilo)–O(alcoxi); el oxígeno alcoxílico se queda con R' (formando metanol).
   - *Texto actual:* «se rompe el enlace entre el oxígeno y los dos fragmentos»
   - *Arreglo:* «se rompe el enlace entre el carbono del carbonilo y el oxígeno del grupo -OCH3; ese oxígeno queda en el metanol y el carbonilo se reduce a -CH2OH.» Igual en flashcards[10] y common_mistakes[3] («el enlace C-O-C se rompe en dos fragmentos»).
8. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — No aparecen otras reacciones redox orgánicas habituales en PAU: hidrogenación de alquenos/aldehídos/cetonas (H2/Ni o Pt) como reducción, oxidación de alquenos con KMnO4 y la distinción de aldehídos y cetonas con Fehling/Tollens (el aldehído se oxida, la cetona no).
   - *Texto actual:* «La serie de oxidación tiene varios escalones, pero no todos los oxidantes los recorren todos»
   - *Arreglo:* Añadir un bloque breve: «H2/Ni reduce C=C y C=O; aldehídos dan positivo en Fehling (Cu2O rojo) y Tollens (espejo de plata), cetonas no».
9. **[BAJA · LATEX]** `theory_blocks[4].body` — La serie de facilidad de reducción «-COOH < -COO- < -CO- < -CHO» en modo matemático se lee como restas y signos menos; ambigua.
   - *Texto actual:* «$-COOH < -COO- < -CO- < -CHO$»
   - *Arreglo:* Escribir con palabras y fórmulas: «ácido ($\mathrm{{-}COOH}$) < éster ($\mathrm{{-}COO{-}}$) < cetona ($\mathrm{{>}C{=}O}$) < aldehído ($\mathrm{{-}CHO}$)».
10. **[BAJA · VISUAL]** `theory_blocks[2].assets[0].svg` — La figura usa «Alcohol 1^rio / 2^rio» (abreviatura no española; lo correcto es «1.º/2.º» o «primario/secundario») y fórmulas en cursiva (R-CH_3 en modo matemático sin \mathrm).
   - *Texto actual:* «Alcohol 1rio R-CH2OH»
   - *Arreglo:* Rotular «Alcohol primario» / «Alcohol secundario» y escribir las fórmulas en redonda.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (3): `common_mistakes[0].why`, `common_mistakes[1].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `worked_examples[3].solution`. Ej.: «(a) Verdadera. (b) Falsa. (c) Falsa. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 20 — Esterificación

**Valoración experta: MEDIA.** Teoría correcta en lo esencial (equilibrio, desplazamiento, hidrólisis ácida vs saponificación, nomenclatura), pero con un error conceptual sobre el origen del -OH del agua y sin ningún tratamiento cuantitativo (Kc) ni la saponificación de grasas. Ejercicios bien resueltos salvo el reto (falta el isómero 2-metilpropanoato de metilo) y un test con distractor duplicado y explicación que cita otro éster. Presentación deficiente: todas las fórmulas en texto plano sin subíndices y una notación de flecha inventada '⇌(H2SO4)⇌'.

**Plan de arreglo:** 1) Corregir theory_blocks[2] (el OH del agua viene del ácido). 2) Pasar todas las fórmulas/ecuaciones a LaTeX con catalizador sobre la flecha y estados. 3) Arreglar mcq[3] (opción C y why_wrong de D). 4) Completar el reto con los dos isómeros. 5) Añadir Kc/rendimiento con un ejemplo numérico y matizar exam_notes[3]; reescribir common_mistakes[2].why.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `theory_blocks[2].body` — Afirma que el grupo alcohílico del éster es 'el que se perdió como -OH en la reacción'. Es falso: en la esterificación (Fischer) el alcohol conserva su oxígeno y solo pierde el H; el -OH que forma el agua procede del ácido (demostrado con marcaje isotópico de 18O). El alumno aprende al revés de dónde sale el agua.
   - *Texto actual:* «viene del alcohol, y es el que se perdió como -OH en la reacción»
   - *Arreglo:* Sustituir por: 'la segunda palabra corresponde al grupo unido al oxígeno sencillo (viene del alcohol, que conserva su oxígeno y solo pierde el H del -OH; el -OH que forma el agua lo aporta el ácido)'. Conviene añadir una frase: R-CO–OH + H–O-R' → R-CO–O-R' + H–OH.
2. **[MEDIA · MCQ]** `mcq[3].options[3].why_wrong` — La explicación del distractor D cita un éster que no es el del enunciado: el test pregunta por 'acetato de propilo', no por 'propanoato de etilo'.
   - *Texto actual:* «no el propanoato de etilo pedido en el enunciado»
   - *Arreglo:* '…es el acetato de metilo (CH3COOCH3), no el acetato de propilo pedido: 'de propilo' exige propan-1-ol, no metanol.'
3. **[MEDIA · MCQ]** `mcq[3].options[2].text` — Distractor C nombra exactamente las mismas sustancias que la clave A (propan-1-ol y ácido acético) con una coletilla confusa; no es una opción química distinta y puede leerse como correcta.
   - *Texto actual:* «Propan-1-ol y ácido acético, pero con el alcohol aportando el grupo que da nombre al ácido»
   - *Arreglo:* Sustituir por un distractor real del error de inversión: 'Ácido propanoico y etanol' o 'Ácido metanoico y propan-2-ol' (por qué está mal: 'acetato' fija el ácido acético y 'propilo' el propan-1-ol).
4. **[MEDIA · ENUNCIADO]** `challenge_questions[0].answer` — Enunciado sin dato que fije la cadena lineal; la respuesta única no está justificada.
   - *Texto actual:* «Ácido butanoico (CH3CH2CH2COOH); el éster X es butanoato de metilo»
   - *Arreglo:* Añadir 'de cadena lineal' al enunciado o dar las dos soluciones.
5. **[MEDIA · SOLUCION_INCOMPLETA]** `challenge_questions[0].full_solution` — C4H8O2 como ácido carboxílico admite dos isómeros: ácido butanoico y ácido 2-metilpropanoico. Con los datos dados X puede ser butanoato de metilo o 2-metilpropanoato de metilo; la solución da solo uno como si fuera único.
   - *Texto actual:* «que es exactamente la fórmula del ácido butanoico, CH3CH2CH2COOH»
   - *Arreglo:* Indicar las dos posibilidades: CH3CH2CH2COOH (ácido butanoico → butanoato de metilo) y (CH3)2CHCOOH (ácido 2-metilpropanoico → 2-metilpropanoato de metilo). O bien añadir al enunciado un dato que discrimine (p. ej. 'el ácido es de cadena lineal'). Ajustar también answer.
6. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — No hay ningún tratamiento cuantitativo del equilibrio (Kc, rendimiento) ni se explica que la base en la saponificación es reactivo estequiométrico (se consume), no catalizador; tampoco se cita el origen del nombre (jabones a partir de grasas/triglicéridos), dato muy preguntado en PAU.
   - *Texto actual:* «la reacción que ocurre no es la simple reacción inversa de la esterificación, sino la saponificación»
   - *Arreglo:* Añadir: expresión $K_c=\dfrac{[\text{éster}][\mathrm{H_2O}]}{[\text{ácido}][\text{alcohol}]}$ con un ejemplo numérico; precisar que en la saponificación se consume 1 mol de NaOH por mol de éster; mencionar triglicérido + 3 NaOH → glicerina + 3 jabón.
7. **[MEDIA · PLANTILLA]** `common_mistakes[2].why` — Texto genérico que no explica por qué se invierten ácido y alcohol en el nombre.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Porque en otras nomenclaturas el término principal va al final; en los ésteres, en cambio, la primera palabra (-oato) es la del ácido y la segunda (de …ilo) la del alcohol.'
8. **[MEDIA · LATEX]** `theory_blocks[2].body` — Fórmulas químicas en texto plano sin subíndices (CH3COOH, CH3OH, (CH3)2CHOH) en la tabla y en prácticamente toda la lección (≈59 apariciones de 'CH3'): ejercicios, respuestas, opciones de test y fichas. La lección 06 del mismo bloque sí usa $\text{CH}_3$.
   - *Texto actual:* «\| ácido acético (CH3COOH) \| metanol (CH3OH) \| acetato de metilo \|»
   - *Arreglo:* Pasar todas las fórmulas a $\mathrm{CH_3COOH}$, $\mathrm{CH_3OH}$, $\mathrm{(CH_3)_2CHOH}$, etc. en todos los campos visibles (worked_examples, guided_exercises, exercises, exam_questions, challenge, mcq, flashcards, summary.key_points).
9. **[MEDIA · VISUAL]** `worked_examples[0].solution` — Notación de flecha inventada '⇌(H2SO4)⇌' (dos flechas con el catalizador entre paréntesis) y fórmulas sin subíndices ni LaTeX. Se repite en worked_examples[1].solution, guided_exercises[0..1].full_solution, exercises[2].full_solution, exam_questions[0].answer, exam_questions[1].full_solution y flashcards[1].back.
   - *Texto actual:* «CH3COOH + CH3CH2OH ⇌(H2SO4)⇌ CH3COOCH2CH3 + H2O»
   - *Arreglo:* Escribir en LaTeX con catalizador sobre la flecha y estados: $\mathrm{CH_3COOH(l) + CH_3CH_2OH(l) \xrightleftharpoons{H_2SO_4} CH_3COOCH_2CH_3(l) + H_2O(l)}$ (si \xrightleftharpoons no está disponible, $\overset{\mathrm{H_2SO_4}}{\rightleftharpoons}$).
10. **[MEDIA · VERIFICAR]** `exam_notes[3]` — Afirma que no se exigen cálculos de Kc en esterificación. En varias PAU (p. ej. Madrid, Andalucía, C. Valenciana) aparecen problemas de equilibrio de esterificación (Kc≈4 para ácido acético + etanol). La lección no tiene ningún ejercicio numérico, lo que deja al alumno sin practicar ese tipo de pregunta.
   - *Texto actual:* «No se exige calcular constantes de equilibrio numéricas para la esterificación en este nivel»
   - *Arreglo:* Matizar ('depende de la comunidad; en algunas aparece el cálculo de Kc') y añadir un ejercicio: 1 mol de ácido acético + 1 mol de etanol, Kc=4 → x=2/3 mol de acetato de etilo (rendimiento 66,7 %); con 3 mol de etanol: x≈0,90 mol, para cuantificar el efecto del exceso de reactivo.
11. **[BAJA · CONCEPTO]** `worked_examples[0].reasoning[0]` — Formulación ambigua sobre qué átomos forman el agua: 'Se une el grupo -COOH del ácido con el grupo -OH del alcohol' sugiere que se combinan los dos OH. Debe dejar claro que sale OH del ácido y H del alcohol.
   - *Texto actual:* «Se une el grupo -COOH del ácido con el grupo -OH del alcohol, liberando una molécula de agua.»
   - *Arreglo:* 'El -OH del grupo carboxilo y el H del -OH del alcohol forman agua; el carbono del carbonilo queda unido al oxígeno del alcohol.'
12. **[BAJA · CONCEPTO]** `theory_blocks[2].body` — Nomenclatura: 'butanoato de isopropilo' es nombre aceptado, pero la convención IUPAC que pide el curso es 'butanoato de propan-2-ilo'; no se menciona el nombre sistemático en ningún sitio (también en worked_examples[2] y exercises[2]: 'propanoato de isopropilo').
   - *Texto actual:* «butanoato de isopropilo»
   - *Arreglo:* Dar ambos: 'butanoato de propan-2-ilo (isopropilo)'; 'propanoato de propan-2-ilo (isopropilo)'.
13. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — Dice que el éster 'se nombra con dos palabras', pero el nombre tiene la estructura '-oato de -ilo' (tres palabras: metanoato de propilo).
   - *Texto actual:* «se nombra con dos palabras»
   - *Arreglo:* 'se nombra con la estructura «(raíz del ácido)-oato de (radical del alcohol)-ilo»'.
14. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[0].full_solution` — El apartado (a) de la resolución no escribe la ecuación, solo la describe en palabras (la ecuación está únicamente en answer), aunque el criterio da 1 punto a la ecuación ajustada.
   - *Texto actual:* «(a) El ácido butanoico reacciona con el metanol, catalizado por ácido sulfúrico, liberando agua.»
   - *Arreglo:* Incluir la ecuación en la resolución: $\mathrm{CH_3CH_2CH_2COOH + CH_3OH \overset{H_2SO_4}{\rightleftharpoons} CH_3CH_2CH_2COOCH_3 + H_2O}$ y el nombre.
15. **[BAJA · SOLUCION_INCOMPLETA]** `worked_examples[3].solution` — Pregunta tipo V/F razonada cuya 'Resolución' solo dice Falsa/Verdadera; la justificación está únicamente en reasoning. La convención pide justificar cada apartado en la solución.
   - *Texto actual:* «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Falsa.»
   - *Arreglo:* Añadir a cada letra su justificación breve (equilibrio; inversa exacta; carboxilato no esterifica; 'etilo' viene del etanol).
16. **[BAJA · REFERENCIA_ROTA]** `diagnostic_items[0].remediation_action` — Remite a 'ejemplos de condensación ya vistos (formación de un éter, formación de una amida)', pero la formación de amidas por condensación no se ha tratado como reacción antes de esta lección (la lección 07 es de formulación de amidas; la condensación de poliamidas está en la 25).
   - *Texto actual:* «formación de un éter, formación de una amida»
   - *Arreglo:* Cambiar por ejemplos realmente vistos (deshidratación intermolecular de alcoholes a éter, L16) o explicar el patrón con un ejemplo concreto.
17. **[BAJA · LATEX]** `theory_blocks[1].body` — Las ecuaciones de teoría no incluyen estados de agregación ni catalizador sobre la flecha, que la convención del curso pide en las ecuaciones químicas.
   - *Texto actual:* «$R-COOH + HO-R' \rightleftharpoons R-COO-R' + H_2O$»
   - *Arreglo:* $\mathrm{R{-}COOH + HO{-}R' \overset{H^+}{\rightleftharpoons} R{-}COO{-}R' + H_2O}$ y en el ejemplo con (l).
18. **[BAJA · VISUAL]** `exam_questions[1].mark_scheme[0]` — Criterio ambiguo: '1 punto por cada producto correcto (2 productos, 2 experimentos)' puede sumar 2 o 4 puntos; con marks=3 debe quedar claro. Además está redactado para el corrector, no para el alumno.
   - *Texto actual:* «1 punto por cada producto correcto (2 productos, 2 experimentos)»
   - *Arreglo:* 'Para la puntuación completa debes: dar los productos del medio ácido (1 punto) y del medio básico (1 punto); justificar la reversibilidad (1 punto).'

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `worked_examples[3].solution`. Ej.: «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Falsa.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 21 — Polimerización por adición

**Valoración experta: MEDIA.** Teoría clara en lo básico (monómero/polímero, unidad repetitiva, M = n·M0, sp2→sp3) y cálculos todos correctos (28,054; 62,50; 9981; 998,5; 100). Pero el ejemplo 4 enseña un criterio falso (decidir adición/condensación por si el cociente de masas es entero), reforzado en exam_notes, y la idea de 'múltiplo exacto siempre' choca con los grados de polimerización medios no enteros. Falta el mecanismo radicalario, los cauchos/dienos y otros polímeros de adición; la justificación de no calcular el PTFE 'porque contiene flúor' no tiene sentido. Fórmulas y potencias en texto plano y dos 'why' de plantilla.

**Plan de arreglo:** 1) Reescribir WE[3] (c)/interpretation/common_mistake y exam_notes[2] con el criterio estructural. 2) Matizar 'múltiplo exacto' (por cadena, sin extremos; n̄ medio). 3) Quitar el argumento del flúor (dar Ar(F)=19,00). 4) Añadir mecanismo radicalario, dienos/caucho, PAN/PMMA y copolímeros; nombres IUPAC de los monómeros. 5) Pasar fórmulas y potencias a LaTeX; rehacer common_mistakes[0,2].why.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `worked_examples[3].reasoning[2]` — Enseña un criterio falso: decidir adición/condensación según si M_PS/M_estireno da 'aproximadamente un entero'. Con masas molares medias (y cocientes ~1000) cualquier valor es 'casi entero' o no lo es por azar (aquí da 998,5, que no es entero y la propia solución dice que es adición). El criterio correcto es estructural: ¿el monómero tiene C=C y se une sin subproducto, o tiene dos grupos funcionales que se condensan liberando H2O/HCl?
   - *Texto actual:* «si el cociente M_PS/M_estireno da (aproximadamente) un número entero, es coherente con una polimerización de adición»
   - *Arreglo:* Sustituir por: '(c) Se mira la estructura del monómero: el estireno solo tiene un C=C y ningún par de grupos funcionales capaces de condensar (–OH, –COOH, –NH2), luego solo puede polimerizar por adición.' Eliminar cualquier uso del cociente como criterio.
2. **[ALTA · CONCEPTO]** `worked_examples[3].interpretation` — Repite el criterio numérico falso ('si el cociente de masas no diera aproximadamente un entero, eso sería indicio de que el polímero no es de adición'). Contradice la propia solución (998,5 no es entero) y lo dicho en worked_examples[2] (n medio no tiene por qué ser entero).
   - *Texto actual:* «si el cociente de masas no diera (aproximadamente) un entero, eso sería indicio de que el polímero no es de adición»
   - *Arreglo:* 'El grado de polimerización medio (≈998,5) no es entero porque es un promedio; el tipo de polimerización se decide por la estructura del monómero, no por el cociente.'
3. **[ALTA · CONCEPTO]** `worked_examples[3].common_mistake` — Presenta como error lo correcto (razonar por la estructura: 'el estireno tiene doble enlace, luego es adición') y empuja a usar el dato numérico, que no sirve como criterio.
   - *Texto actual:* «razonar solo cualitativamente ('el estireno tiene doble enlace, luego es adición') sin usar el dato numérico disponible»
   - *Arreglo:* 'En (c), intentar decidirlo con el cociente de masas: n medio nunca tiene por qué ser entero; hay que razonar con la estructura del monómero (C=C sin grupos funcionales condensables).'
4. **[MEDIA · CONCEPTO]** `exam_notes[2]` — Afirma que en examen se distingue adición/condensación 'a partir de si la masa del polímero es o no un múltiplo exacto de la del monómero'. No es un criterio usado en PAU ni válido con masas medias; lo que se pide es reconocer el tipo de monómero y si se libera subproducto.
   - *Texto actual:* «pide distinguir adición de condensación a partir de si la masa del polímero es o no un múltiplo exacto de la del monómero»
   - *Arreglo:* 'Un apartado recurrente pide clasificar un polímero como de adición o de condensación a partir del monómero (C=C frente a dos grupos funcionales) y de si se libera una molécula pequeña (H2O, HCl).'
5. **[MEDIA · CONCEPTO]** `theory_blocks[1].body` — 'La masa molar de un polímero de adición es siempre un múltiplo exacto de la del monómero' es una simplificación que choca con los propios ejemplos (n medio = 9981, 998,5 no enteros) y omite los grupos terminales (fragmentos del iniciador). El alumno recibe mensajes contradictorios ('exacto' vs 'promedio').
   - *Texto actual:* «la masa molar de un polímero de adición es siempre un múltiplo exacto de la del monómero del que procede»
   - *Arreglo:* 'Para una cadena, despreciando los extremos (restos del iniciador), M = n·M0. Una muestra real contiene cadenas de distinta longitud: M̄ = n̄·M0, y el grado de polimerización medio n̄ no tiene por qué ser entero.' Ajustar igual summary.big_idea, summary.key_points[1], keywords[2], flashcards[1] y mcq[4].options[2].
6. **[MEDIA · CONCEPTO]** `theory_blocks[2].body` — Justificación sin sentido: el PTFE aparece 'sin cálculo numérico porque su monómero contiene flúor'. La masa atómica del F (19,00) es un dato estándar; no hay ninguna razón química para no calcular. Lo mismo se arrastra a exam_questions[1].statement ('Sin conocer la masa atómica del flúor'), flashcards[11] y summary.key_points[3].
   - *Texto actual:* «aunque sin cálculo numérico porque su monómero contiene flúor»
   - *Arreglo:* Eliminar la coletilla; si se quiere, dar el cálculo: M(C2F4)=2·12,011+4·19,00=100,02 g/mol. En exam_questions[1].(b) pedir la justificación sin la premisa artificial del flúor (o dar Ar(F)=19,00 y pedir un cálculo de n).
7. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — Falta el mecanismo (aunque sea cualitativo) de la polimerización por adición: iniciador (peróxido) que genera radicales, etapas de iniciación–propagación–terminación; tampoco aparecen otros polímeros de adición habituales en PAU (caucho natural/poliisopreno y polibutadieno a partir de dienos, poliacrilonitrilo, PMMA/metacrilato, poli(acetato de vinilo)) ni la idea de copolímero.
   - *Texto actual:* «La regla que se ha visto para el eteno es general para cualquier monómero del tipo CH2=CH-R»
   - *Arreglo:* Añadir un bloque breve: R–O–O–R → 2 RO·; RO· + CH2=CH2 → RO–CH2–CH2·; propagación…; terminación por combinación de radicales. Ampliar la tabla con CH2=CH–CN (PAN), CH2=C(CH3)COOCH3 (PMMA), CH2=C(CH3)–CH=CH2 (isopreno → caucho) y definir copolímero.
8. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica el porqué del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Porque se aplica por inercia el patrón de la condensación (pérdida de H2O en cada unión) a un monómero con C=C, que se une sin subproducto.'
9. **[MEDIA · PLANTILLA]** `common_mistakes[2].why` — Mismo texto genérico de relleno.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Porque la notación (…)n recuerda a «n copias» y no muestra los enlaces C–C entre unidades consecutivas.'
10. **[MEDIA · LATEX]** `worked_examples[0].solution` — Potencias y fórmulas en texto plano: '1,40×10^4', 'M_polímero', 'CH2=CH2' sin subíndices. Mismo problema en worked_examples[1].solution ('1,56×10^4'), worked_examples[2].solution ('9,98×10^3'), mcq[3].options[2].text ('1,08·10^6') y en casi todas las fórmulas de la lección (tabla de theory_blocks[2], ejercicios, test, fichas).
   - *Texto actual:* «M_polímero = 500·28,054 = 14 027 g/mol ≈ 1,40×10^4 g/mol»
   - *Arreglo:* $M_{\text{polímero}} = 500\cdot 28{,}054 = 14\,027\ \mathrm{g\,mol^{-1}} \approx 1{,}40\cdot10^{4}\ \mathrm{g\,mol^{-1}}$; fórmulas como $\mathrm{CH_2{=}CH_2}$, $\mathrm{({-}CH_2{-}CHCl{-})_n}$.
11. **[BAJA · CONCEPTO]** `exam_questions[0].full_solution` — El apartado (b) se declara falso 'por definición' sin matizar que, en una muestra real, la masa molar es media y n̄ no es entero (lo que la propia lección muestra en el ejemplo 3 y 4). Conviene precisar para no contradecir esos ejemplos.
   - *Texto actual:* «por definición de polimerización por adición, M_polímero=n·M_monómero para cualquier valor de n, por grande que sea»
   - *Arreglo:* Añadir: 'para cada cadena (despreciando los extremos); la longitud no introduce ninguna pérdida de átomos. Si una masa media no da un cociente entero es porque n̄ es un promedio, no porque se pierdan átomos.'
12. **[BAJA · CONCEPTO]** `prerequisites[0].statement` — Nomenclatura: los monómeros solo se nombran con nombres tradicionales (cloruro de vinilo, estireno). La convención IUPAC del curso requiere al menos citar cloroeteno y etenilbenceno (fenileteno); 'politetrafluoretileno' es además una grafía no sistemática.
   - *Texto actual:* «nombrar alquenos sencillos (eteno, propeno, cloruro de vinilo, estireno)»
   - *Arreglo:* Dar ambos nombres: cloroeteno (cloruro de vinilo), etenilbenceno o fenileteno (estireno), tetrafluoroeteno; PTFE = poli(tetrafluoroeteno)/politetrafluoroetileno.
13. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[1].full_solution` — El apartado (a) de la resolución describe en palabras pero no escribe la ecuación ni la unidad repetitiva (solo aparecen en answer), aunque el criterio da 2 puntos a la reacción.
   - *Texto actual:* «(a) El doble enlace entre los dos carbonos se abre exactamente igual que en el eteno, conservando los cuatro átomos de flúor.»
   - *Arreglo:* Añadir: $n\,\mathrm{CF_2{=}CF_2 \longrightarrow ({-}CF_2{-}CF_2{-})_n}$; unidad repetitiva –CF2–CF2–.
14. **[BAJA · REFERENCIA_ROTA]** `misconceptions[1].related_exercises` — Remite a 'teoría §3', que (tabla de monómeros vinílicos) no trata la idea de que (–CH2–CH2–)n es una única macromolécula.
   - *Texto actual:* «errores frecuentes 3 y teoría §3»
   - *Arreglo:* 'errores frecuentes 3, ficha 6 y teoría §1' (o añadir esa aclaración en theory_blocks[1]).
15. **[BAJA · LATEX]** `theory_blocks[1].body` — Fórmulas químicas en modo matemático sin \mathrm (salen en cursiva: CH como variables) y 'M_{polímero}' con texto acentuado en cursiva; C2H4 sin subíndice.
   - *Texto actual:* «$n\ CH_2{=}CH_2 \longrightarrow (-CH_2-CH_2-)_n$»
   - *Arreglo:* $n\,\mathrm{CH_2{=}CH_2} \longrightarrow \mathrm{({-}CH_2{-}CH_2{-})}_n$ y $M_{\text{polímero}} = n\cdot M_{\text{monómero}}$.
16. **[BAJA · VISUAL]** `theory_blocks[1].assets[0].svg` — La figura etiqueta el monómero con '(enlace π cerrado)', expresión no estándar que puede confundir (el enlace π no está 'cerrado', está presente).
   - *Texto actual:* «monómero (enlace π cerrado)»
   - *Arreglo:* Cambiar la etiqueta a 'monómero (con enlace π)' o 'C=C: enlace σ + π'.

**Fallos de renderizado (vistos en el navegador):**

- [MEDIA · LATEX] `worked_examples[0].solution` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^4] …8,054 g/mol; M_polímero = 500·28,054 = 14 027 g/mol ≈ 1,40×10^4 g/mol. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».
- [MEDIA · LATEX] `worked_examples[1].solution` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^4] …008+35,45=62,50 g/mol. M_PVC=250·62,50=15 625 g/mol ≈ 1,56×10^4 g/mol. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».
- [MEDIA · LATEX] `worked_examples[2].solution` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^3] …n = 280 000/28,054 = 9981 ≈ 9,98×10^3 unidades de eteno por cadena, en promedio. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».
- [MEDIA · LATEX] `mcq[3].options[2].text` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^6] …n=1 084 764 (o redondeado, ≈1,08·10^6) …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH3". (7): `theory_blocks[2].body`, `theory_blocks[2].body`, `guided_exercises[1].statement`, `guided_exercises[1].hints[1]`, `guided_exercises[1].answer`, `guided_exercises[1].full_solution`, `mcq[2].options[1].text`. Ej.: «ón \| Polímero (usos típicos) \| ⏎ \|---\|---\|---\| ⏎ \| Propeno, CH2=CH-CH3 \| n CH2=CH-CH3 → (-CH2-CH(CH3)-)n \| Polipropileno (PP): env». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-R". (3): `theory_blocks[2].body`, `keywords[5].definition`, `flashcards[7].back`. Ej.: «ra el eteno es general para cualquier monómero del tipo CH2=CH-R (llamado monómero vinílico): el doble enlace se abre y R qu». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 7 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Verdadera. (b) Falsa. (c) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 22 — Combustión e integración estequiométrica

**Valoración experta: MEDIA.** Los cálculos son correctos (etanol 104/95,5/58,7 g; propano limitante 1,73 g; butano, metanol, octano, butanol y rendimiento verificados) y la ecuación general CxHyOz está bien explicada. Pero la teoría enseña una regla falsa sobre cuándo el coeficiente de O2 es fraccionario ('número impar de carbonos', con el butano de ejemplo), repetida en examen y diagnóstico; hay incoherencia entre el modelo de O2 limitante (solo CO2) y la afirmación de que aparece CO; y la conclusión sobre biocombustibles es engañosa. Faltan los problemas PAU típicos de combustión (fórmula empírica por análisis, volúmenes de gas/aire, ΔHc). Fórmulas en texto plano.

**Plan de arreglo:** 1) Corregir la regla del coeficiente fraccionario en theory_blocks[2], exam_questions[0], diagnostic_items[0], WE[0]. 2) Aclarar el modelo idealizado de O2 limitante y coherentar mcq[3], summary. 3) Rehacer la conclusión del reto. 4) Añadir fórmula empírica por combustión, gases/aire y ΔHc con ejemplos. 5) LaTeX y estados en ecuaciones; intermedios con más cifras; reescribir common_mistakes[0].why.

**Hallazgos de la revisión experta:**

1. **[ALTA · CONCEPTO]** `theory_blocks[2].body` — Regla falsa y contradicha por su propio ejemplo: dice que el coeficiente del O2 sale fraccionario 'con un número impar de carbonos' y pone como ejemplo el butano (4 C, par). En los alcanos CnH2n+2 el coeficiente es (3n+1)/2: sale fraccionario con n PAR (etano 3,5; butano 6,5; octano 12,5) y entero con n impar (metano 2, propano 5). La condición general es que 2x + y/2 − z sea impar.
   - *Texto actual:* «Con un número impar de carbonos (y sin oxígeno propio que lo compense), el coeficiente x+y/4-z/2 sale a menudo fraccionario. Por ejemplo, para el butano (x=4»
   - *Arreglo:* 'El coeficiente x + y/4 − z/2 sale fraccionario cuando el número total de átomos de O que piden los productos menos los que aporta el combustible (2x + y/2 − z) es impar. En los alcanos ocurre con número PAR de carbonos: butano (x=4, y=10): 4 + 10/4 = 6,5.'
2. **[ALTA · CONCEPTO]** `exam_questions[0].full_solution` — Repite la regla falsa en la justificación de (b): el coeficiente fraccionario es frecuente en alcanos con número PAR de carbonos (etano, butano, octano), no impar (propano da 5, entero, como muestra la propia lección).
   - *Texto actual:* «es el resultado más frecuente al ajustar la combustión de hidrocarburos con número impar de carbonos»
   - *Arreglo:* '…es muy frecuente (p. ej., en los alcanos con número par de carbonos: butano 13/2, octano 25/2).'
3. **[MEDIA · CONCEPTO]** `diagnostic_items[0].interpretation` — Misma regla falsa ('hidrocarburos con número impar de carbonos').
   - *Texto actual:* «muchas combustiones de hidrocarburos con número impar de carbonos»
   - *Arreglo:* '…de muchas combustiones (p. ej., alcanos con número par de carbonos como el butano o el octano).'
4. **[MEDIA · CONCEPTO]** `mcq[3].options[3].why_wrong` — Contradicción interna: califica de imposible el modelo 'menos CO2 y H2O y sobra combustible', que es exactamente el modelo usado en worked_examples[3] (O2 limitante, solo CO2 y H2O, sobra 1,73 g de propano). Además la 'proporción 2:1' entre CO2 y H2O no es general. El alumno no sabe qué modelo es el correcto.
   - *Texto actual:* «sobraría combustible sin reaccionar en vez de cambiar la naturaleza de los productos»
   - *Arreglo:* Explicar en teoría que hay dos niveles: (1) modelo estequiométrico idealizado (O2 limitante, productos de combustión completa, sobra combustible) que se usa en los problemas; (2) realidad química: con defecto de O2 aparece CO/hollín. Reescribir D: 'Ninguno: solo se forma menos CO2 y H2O' → why_wrong: 'En la práctica, con defecto de O2 parte del C queda como CO; el modelo de «sobra combustible» es una idealización de cálculo.' Quitar '2:1'.
5. **[MEDIA · CONCEPTO]** `theory_blocks[4].body` — Mezcla dos modelos sin advertirlo con claridad: dice que con O2 insuficiente 'pasan dos cosas a la vez' (O2 limitante y combustión incompleta con CO), pero los cálculos (worked_examples[3]) suponen solo CO2 y H2O con combustible sobrante. summary.key_points[4] también dice 'si falta, la combustión se vuelve incompleta (aparece CO)'.
   - *Texto actual:* «Esta lección trabaja el caso de reactivo limitante manteniendo los productos de combustión completa»
   - *Arreglo:* Decir explícitamente: 'En los problemas tipo PAU se supone que el O2 limitante reacciona según la combustión completa (modelo idealizado); en la realidad parte del carbono saldría como CO.' Coherentar summary.key_points[4] y mcq[3].
6. **[MEDIA · CONCEPTO]** `challenge_questions[0].full_solution` — La conclusión sobre biocombustibles es engañosa: su menor huella no se debe a emitir menos CO2 por gramo (el etanol también libera menos energía por gramo: ~29,7 kJ/g frente a ~47,9 kJ/g del octano, y por unidad de energía emiten CO2 similar), sino a que su carbono procede de CO2 fijado recientemente por las plantas.
   - *Texto actual:* «explica por qué ciertos biocombustibles oxigenados se promueven como alternativa con menor huella de carbono por unidad de masa quemada»
   - *Arreglo:* Sustituir por: 'Ojo: por gramo emite menos CO2, pero también libera menos energía; la ventaja climática de los biocombustibles se debe a que su carbono procede de CO2 atmosférico fijado por las plantas.' Además, dar la relación cuantitativa: g CO2/g = x·44,009/M (etanol 2·44,009/46,069 = 1,91; octano 8·44,009/114,232 = 3,08).
7. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — Para una lección de 'integración estequiométrica' de combustión faltan los tipos de problema PAU más habituales: (1) determinación de la fórmula empírica/molecular a partir de las masas de CO2 y H2O (análisis por combustión); (2) volúmenes de gases (pV = nRT, condiciones normales) y volumen de aire (21 % O2 en volumen); (3) calor de combustión (ΔHc). Ningún ejercicio los trabaja.
   - *Texto actual:* «la combustión completa con oxígeno en exceso se escribe siempre»
   - *Arreglo:* Añadir un bloque y al menos un ejemplo de cada: p. ej. 'La combustión de 2,30 g de un compuesto C,H,O da 4,40 g CO2 y 2,70 g H2O → C2H6O'; volumen de CO2 a 25 °C y 1 atm; volumen de aire necesario; energía liberada con ΔHc dado.
8. **[MEDIA · PLANTILLA]** `common_mistakes[0].why` — Texto genérico de relleno que no explica la causa del error.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Porque se memoriza el ajuste de los hidrocarburos (sin O propio) y se aplica a alcoholes, éteres o ácidos sin contar el O que ya trae la molécula.'
9. **[MEDIA · LATEX]** `worked_examples[0].solution` — Fórmulas, ecuaciones y magnitudes en texto plano sin subíndices ni estados (C3H8 + 5 O2 → 3 CO2 + 4 H2O; m_O2, n_CO2, CxHyOz…) en casi toda la lección: ejemplos, ejercicios, test, fichas y summary.key_points. Solo theory_blocks[1-2] usan LaTeX.
   - *Texto actual:* «C3H8 + 5 O2 → 3 CO2 + 4 H2O.»
   - *Arreglo:* $\mathrm{C_3H_8(g) + 5\,O_2(g) \longrightarrow 3\,CO_2(g) + 4\,H_2O(l)}$; magnitudes como $m_{\mathrm{O_2}} = 104\ \mathrm{g}$.
10. **[BAJA · CONCEPTO]** `worked_examples[0].interpretation` — Justificación confusa del coeficiente entero ('número par de hidrógenos entre 4'), coherente con la regla errónea de la teoría. Lo relevante es que 2·3 + 8/2 = 10 átomos de O es par.
   - *Texto actual:* «porque el propano tiene un número par de hidrógenos entre 4 (8/4=2, entero)»
   - *Arreglo:* 'Sale entero porque los productos necesitan 2·3 + 4 = 10 átomos de O (número par) y el propano no aporta oxígeno: 10/2 = 5 O2.'
11. **[BAJA · CONCEPTO]** `exam_questions[0].full_solution` — (c) 'con oxígeno suficiente, cualquier combustible arde de forma completa' es una simplificación excesiva: también influyen la mezcla aire-combustible, la temperatura y el tiempo de contacto.
   - *Texto actual:* «con oxígeno suficiente, cualquier combustible arde de forma completa»
   - *Arreglo:* 'La causa principal es la falta de O2 en la zona de reacción (poco aire o mala mezcla), no la «calidad» del combustible.'
12. **[BAJA · CALCULO]** `worked_examples[2].solution` — Los valores intermedios mostrados no cuadran con las multiplicaciones escritas: 3·1,09 = 3,27 (no 3,26) y 2·1,09 = 2,18 (no 2,17); el resultado sale de usar 1,0853 sin mostrarlo. Contradice visualmente el consejo del propio ejemplo de no redondear. Igual en exercises[0]: 10,9·31,998 = 349 (no 350).
   - *Texto actual:* «n_etanol=50,0/46,069=1,09 mol. (b) n_O2=3·1,09=3,26 mol»
   - *Arreglo:* Mostrar más cifras en los intermedios: n = 1,085 mol; n(O2) = 3,256 mol → 104 g; n(CO2) = 2,171 mol → 95,5 g; n(H2O) = 3,256 mol → 58,7 g. En exercises[0]: n = 0,8754 mol; n(O2) = 10,94 mol → 350 g.
13. **[BAJA · MCQ]** `mcq[1].stem` — El enunciado pregunta '¿Qué parte de la ecuación general sirve para decidir esto?' pero las opciones son procedimientos; además el enunciado ya revela que el O2 se agota, con lo que la pregunta pierde sentido.
   - *Texto actual:* «y resulta que el O2 se agota antes de que reaccione todo el combustible. ¿Qué parte de la ecuación general sirve para decidir esto?»
   - *Arreglo:* 'Se queman 10,0 g de un hidrocarburo con 15,0 g de O2. ¿Cómo se decide cuál es el reactivo limitante?'
14. **[BAJA · ENUNCIADO]** `exercises[1].statement` — No da la masa molar del propano ni las masas atómicas (otros ejercicios sí las dan), y define el rendimiento como 'fracción de propano que realmente se transforma en CO2' en un problema que dice 'oxígeno en exceso' y combustión completa, lo que es químicamente artificial.
   - *Texto actual:* «Se queman 20,0 g de propano con oxígeno en exceso, pero el rendimiento real del proceso»
   - *Arreglo:* Añadir 'M(C3H8) = 44,097 g/mol; M(CO2) = 44,009 g/mol' y reformular el contexto (p. ej. 'solo se recoge el 92,0 % del CO2 producido').
15. **[BAJA · ENUNCIADO]** `mcq[4].stem` — Usa 'x gramos' para la masa cuando x ya designa el número de carbonos en CxHyOz en toda la lección; confuso.
   - *Texto actual:* «Se queman completamente x gramos de un hidrocarburo puro (CaHb»
   - *Arreglo:* Usar 'una masa m' en lugar de 'x gramos'.
16. **[BAJA · VISUAL]** `challenge_questions[0].answer` — Llama 'combustible estudiado' al octano (no lo nombra) y usa LaTeX solo aquí, mientras el resto de la lección va en texto plano.
   - *Texto actual:* «combustible estudiado: $3{,}08$ g/g»
   - *Arreglo:* 'Etanol: 1,91 g CO2/g; octano: 3,08 g CO2/g; el octano emite ≈1,61 veces más CO2 por gramo.' (con formato LaTeX homogéneo).
17. **[BAJA · ERRATA]** `exam_questions[0].statement` — Cambia a tratamiento de usted ('Razone') cuando toda la lección tutea al alumno.
   - *Texto actual:* «Razone si las siguientes afirmaciones son verdaderas o falsas.»
   - *Arreglo:* 'Razona si las siguientes afirmaciones son verdaderas o falsas.'

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[0].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 7 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Verdadera. (b) Falsa. (c) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 23 — Condiciones de reacción y mapa de transformaciones

**Valoración experta: MEDIA.** Lección de repaso integrador bien planteada (algoritmo sustrato–reactivo–condiciones, competencia SN/E, ejemplos correctos: 2-bromobutano, 1-bromopropano, butan-2-ol, propeno, eteno→ácido acético). Pero contiene errores conceptuales: un test cuya explicación niega que la esterificación sea una sustitución en el acilo (y cuya clave no está entre los seis tipos), la idea de que la polimerización 'reutiliza exactamente el mecanismo de adición', una relación causal inventada entre la competencia SN/E y Markovnikov/Saytzeff, y un esquema de adición incorrecto en el mapa. Falta la sustitución radicalaria de alcanos y la aromática; fórmulas en texto plano.

**Plan de arreglo:** 1) Rehacer mcq[2] y aclarar la doble clasificación de la esterificación. 2) Corregir el 'mismo mecanismo' de la polimerización (misconceptions[2], theory_blocks[4], summary, WE[3]). 3) Reescribir el párrafo final de theory_blocks[3] con las razones de estabilidad. 4) Corregir el paso 2 del algoritmo y completar la tabla (sustitución radicalaria/aromática, combustión). 5) Corregir la figura (adición, ⇌) y summary.formulas[1]; LaTeX en fórmulas; quitar PCC; unificar dicromato.

**Hallazgos de la revisión experta:**

1. **[ALTA · MCQ]** `mcq[2].options[0].why_wrong` — La justificación es químicamente falsa: en la esterificación SÍ hay un grupo que se sustituye en el mismo carbono (el –OH del carbono acílico es reemplazado por –OR'; es una sustitución nucleófila en el acilo) y muchos libros de 2.º de Bachillerato la clasifican como sustitución. Además la clave C ('condensación') no es ninguno de los seis tipos de la tabla de la lección, a pesar de que el enunciado pide 'los tipos básicos de reacción de esta lección'. Hay dos opciones defendibles.
   - *Texto actual:* «En la esterificación no hay propiamente un 'grupo saliente' que se sustituye por otro en el mismo carbono»
   - *Arreglo:* Reformular: '¿Cómo se clasifica la esterificación?' con clave 'Es una condensación y, mecanísticamente, una sustitución en el carbono del grupo carboxilo (–OH → –OR')'; o cambiar A por un distractor claramente falso (p. ej. 'Con la adición, porque se rompe un doble enlace C=C'). Explicar en theory_blocks[1] ambas clasificaciones.
2. **[MEDIA · CONCEPTO]** `misconceptions[2].correct_model` — Afirma que la polimerización por adición 'reutiliza exactamente el mecanismo de adición'. Es falso: la adición de HX/X2/H2O a alquenos es electrófila (iónica), mientras que la polimerización de PE, PP, PVC… es una reacción en cadena radicalaria (iniciación–propagación–terminación). Lo que comparten es el resultado (apertura del C=C), no el mecanismo. Se repite en theory_blocks[4].body, summary.key_points[4] y worked_examples[3].interpretation ('mismo mecanismo de fondo').
   - *Texto actual:* «la polimerización por adición reutiliza exactamente el mecanismo de adición, una y otra vez»
   - *Arreglo:* 'La polimerización por adición comparte con la adición la apertura del enlace π del C=C, pero transcurre por un mecanismo en cadena (normalmente radicalario, con un iniciador) en el que cada monómero se une al extremo de la cadena en crecimiento.'
3. **[MEDIA · CONCEPTO]** `theory_blocks[3].body` — Non sequitur: dice que la competencia sustitución/eliminación 'es la razón' de que Markovnikov y Saytzeff compartan protagonista. No hay relación causal; además la lección no explica el porqué real de cada regla (estabilidad del carbocatión más sustituido en la adición; mayor estabilidad del alqueno más sustituido en la eliminación).
   - *Texto actual:* «Esta competencia es la razón por la que Markovnikov y Saytzeff comparten protagonista»
   - *Arreglo:* Separar en dos ideas: '(1) Competencia SN/E: …'. '(2) Markovnikov y Saytzeff señalan ambos al carbono más sustituido por razones de estabilidad: en la adición se forma el carbocatión más estable (más sustituido), y en la eliminación se forma el alqueno más estable (más sustituido).'
4. **[MEDIA · CONCEPTO]** `theory_blocks[2].body` — El algoritmo dice que un nucleófilo (OH-, CN-) 'apunta a sustitución o adición'. A este nivel la adición a alquenos es electrófila (HX, X2, H2O/H+), no nucleófila; además el paso 2 omite los casos clave: reactivo electrófilo (HX, X2, H2O/H+) → adición y base fuerte (KOH/NaOH en etanol) → eliminación.
   - *Texto actual:* «¿Es un nucleófilo (OH-, CN-)? Apunta a sustitución o adición.»
   - *Arreglo:* '¿Es un nucleófilo (OH-, CN-, NH3) y el sustrato tiene grupo saliente? → sustitución. ¿Es un electrófilo o una molécula que se adiciona (H2, X2, HX, H2O/H+) y hay C=C o C≡C? → adición. ¿Es una base fuerte en etanol caliente? → eliminación.'
5. **[MEDIA · CONCEPTO]** `summary.formulas[1]` — La ecuación resumen de la esterificación se escribe con flecha simple, contradiciendo lo que el curso insiste en enseñar (es un equilibrio y debe ir con ⇌; la lección 20 marca la flecha simple como error típico).
   - *Texto actual:* «R\text{-COOH}+HO\text{-}R' \rightarrow R\text{-COO-}R'+H_2O»
   - *Arreglo:* R\text{-COOH}+HO\text{-}R' \overset{H^+}{\rightleftharpoons} R\text{-COO-}R'+H_2O
6. **[MEDIA · SOLUCION_INCOMPLETA]** `guided_exercises[0].answer` — (b) CH2=CH2 + H2 (Ni) → CH3-CH3 se clasifica solo como 'adición', pero la propia tabla de la lección pone 'H2+catalizador… para reducir' en la fila de oxidación-reducción: es a la vez adición e hidrogenación (reducción). El alumno puede ser penalizado por una respuesta que la lección considera válida. Además la resolución dice 'Doble enlace a dos enlaces simples', impreciso (el C=C pasa a un enlace C–C sencillo y se forman dos C–H).
   - *Texto actual:* «(b) Doble enlace a dos enlaces simples con catalizador metálico (Ni): adición.»
   - *Arreglo:* '(b) Adición (hidrogenación catalítica), que además es una reducción: el C=C pasa a C–C sencillo y cada C gana un H.'
7. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — El mapa de reactividad deja fuera sustituciones muy preguntadas en PAU que no tienen grupo saliente clásico: halogenación radicalaria de alcanos (CH4 + Cl2, luz UV) y sustitución electrófila aromática del benceno (nitración HNO3/H2SO4, halogenación con FeBr3). Con el algoritmo actual ('¿tiene un grupo saliente?') el alumno no las clasificaría. Tampoco aparece la combustión en el mapa pese a citarse en ejemplos y test.
   - *Texto actual:* «\| Sustitución \| Un grupo saliente es reemplazado por un grupo entrante \| Medio básico acuoso y frío (sustratos 1º); disolvente polar, sin base fuerte (sustratos 3º) \|»
   - *Arreglo:* Añadir a la fila de sustitución: 'alcanos + X2 con luz (radicalaria); benceno + HNO3/H2SO4 o X2/FeX3 (electrófila aromática)', y una fila o nota 'Combustión: O2 en exceso → CO2 + H2O'. Ajustar el paso 1 del algoritmo.
8. **[MEDIA · LATEX]** `worked_examples[0].statement` — Fórmulas químicas en texto plano sin subíndices ni cargas formateadas (CH3-CH2-Br, OH-, H2SO4, K2Cr2O7, KMnO4…) en toda la lección: tabla de teoría, ejemplos, ejercicios, test y fichas (≈40 apariciones de 'CH3').
   - *Texto actual:* «CH3-CH2-Br + NaOH(ac, frío) → CH3-CH2-OH + NaBr.»
   - *Arreglo:* $\mathrm{CH_3{-}CH_2{-}Br + NaOH(aq) \xrightarrow{\text{frío}} CH_3{-}CH_2{-}OH + NaBr}$; $\mathrm{OH^-}$, $\mathrm{K_2Cr_2O_7}$, etc.
9. **[MEDIA · VISUAL]** `theory_blocks[4].assets[0].svg` — En el mapa, el esquema de la adición está mal: '>C=C< + reactivo → >C−C<' no muestra los átomos incorporados (el producto parece haber perdido el reactivo). Además la casilla de esterificación usa '→' a la vez que dice 'reacción reversible, en equilibrio', y la de condensación habla solo de 'pérdida de H2O' (también puede ser HCl).
   - *Texto actual:* «>C=C< + reactivo → >C−C<  ·  R–COOH+HO–R′ → R–COO–R′+H2O»
   - *Arreglo:* Adición: '>C=C< + A–B → >C(A)–C(B)<'. Esterificación con '⇌'. Condensación: 'pérdida de una molécula pequeña (H2O, HCl) por unión'.
10. **[BAJA · CONCEPTO]** `exam_questions[0].statement` — Inconsistencia sobre el dicromato: aquí 'oxidarlo suavemente con K2Cr2O7' y flashcards[6] lo llama oxidación suave, pero guided_exercises[0].full_solution y challenge_questions[0] lo tratan como 'oxidante fuerte' que lleva el etanol a ácido acético.
   - *Texto actual:* «oxidarlo suavemente con K2Cr2O7»
   - *Arreglo:* Unificar: 'K2Cr2O7/H2SO4 oxida alcoholes 1º a aldehído (si se destila) o a ácido carboxílico (a reflujo); a efectos de esta comparación, es una oxidación controlada que conserva el esqueleto'.
11. **[BAJA · CONCEPTO]** `challenge_questions[0].full_solution` — Dice que el medio ácido 'activa la molécula de agua'; en la hidratación de alquenos el ácido protona el doble enlace (formando el carbocatión), como explica correctamente exercises[2]. Mismo error en exercises[0].full_solution.
   - *Texto actual:* «en medio ácido fuerte que activa la molécula de agua»
   - *Arreglo:* '…en medio ácido: el H+ protona el doble enlace y el agua ataca al carbocatión formado.'
12. **[BAJA · CONCEPTO]** `exam_questions[0].full_solution` — Generalización falsa en (a): 'como toda condensación con catalizador ácido, es reversible'. No se puede generalizar a toda condensación.
   - *Texto actual:* «la esterificación, como toda condensación con catalizador ácido, es reversible (hidrólisis)»
   - *Arreglo:* 'Verdadera: la esterificación es reversible; su inversa es la hidrólisis ácida del éster, y se alcanza un equilibrio.'
13. **[BAJA · ENUNCIADO]** `exercises[2].statement` — Enunciado genérico ('Un alqueno') sin compuesto concreto, por lo que la respuesta es solo 'alcano'/'alcohol'; no practica la escritura de productos ni Markovnikov.
   - *Texto actual:* «Un alqueno se trata, por separado, con: (i) H2 con catalizador de Pt; (ii) H2O en medio ácido fuerte.»
   - *Arreglo:* Dar un alqueno concreto (p. ej. propeno) y pedir productos: (i) propano; (ii) propan-2-ol (Markovnikov).
14. **[BAJA · SOLUCION_INCOMPLETA]** `worked_examples[1].solution` — No menciona que el but-2-eno presenta isomería geométrica y que el producto mayoritario es el (E)-but-2-eno (trans), cuestión habitual al combinar Saytzeff e isomería.
   - *Texto actual:* «El producto mayoritario es el but-2-eno»
   - *Arreglo:* Añadir: 'mayoritariamente (E)-but-2-eno (trans), más estable que el (Z)'. Opcional en WE[2](ii).
15. **[BAJA · SOLUCION_INCOMPLETA]** `worked_examples[2].solution` — El producto de (i) se da solo como fórmula sin nombre IUPAC (butan-2-ol), y los alquenos de (ii) sin fórmula.
   - *Texto actual:* «(i) Predomina la sustitución (SN2: CH3-CH(OH)-CH2-CH3 + NaBr)»
   - *Arreglo:* '(i) … CH3-CH(OH)-CH2-CH3 (butan-2-ol) + NaBr. (ii) … CH3-CH=CH-CH3 (but-2-eno, mayoritario) y CH2=CH-CH2-CH3 (but-1-eno).'
16. **[BAJA · VISUAL]** `mcq[4].options[0].text` — La fórmula mnemotécnica '(lo gana / lo pierde)' es ambigua (¿qué gana el carbono con menos H?). En Markovnikov ese carbono gana el X/OH, no un H; en Saytzeff pierde un H. Igual en flashcards[1].back.
   - *Texto actual:* «Ambas señalan al carbono con menos H, pero en sentidos opuestos (lo gana / lo pierde).»
   - *Arreglo:* '…en la adición ese carbono recibe el grupo electronegativo (X, OH) y el H va al carbono con más H; en la eliminación ese carbono es el que pierde el H.'
17. **[BAJA · NIVEL]** `mcq[3].stem` — El PCC (clorocromato de piridinio) no forma parte del temario de Química de 2.º de Bachillerato; aparece en mcq[3], theory_blocks[2], flashcards[6], misconceptions[1] y en el mapa.
   - *Texto actual:* «Un alcohol primario se oxida con PCC (un oxidante suave)»
   - *Arreglo:* Sustituir por 'K2Cr2O7/H2SO4 destilando el aldehído según se forma' o 'un oxidante suave'.
18. **[BAJA · ERRATA]** `exam_questions[0].statement` — Tratamiento de usted ('Razone') frente al tuteo del resto de la lección.
   - *Texto actual:* «Razone si las siguientes afirmaciones son verdaderas o falsas.»
   - *Arreglo:* 'Razona si las siguientes afirmaciones son verdaderas o falsas.'

**Chequeos automáticos:**

- [BAJA · REFERENCIA_ROTA] Código interno visible para el alumno: "CH-CH3". (4): `worked_examples[3].statement`, `worked_examples[3].solution`, `worked_examples[3].solution`, `worked_examples[3].solution`. Ej.: «A partir del propeno, CH2=CH-CH3, indica qué reactivo y condiciones usarías para obtener: (a». Arreglo: Sustituir el código por una descripción en texto.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 4 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Verdadera. (b) Falsa. (c) Verdadera. (d) Falsa.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 24 — Propiedades físicas y químicas de los grupos funcionales

**Valoración experta: MEDIA.** Teoría correcta en ebullición y solubilidad, con buenos ejemplos de isómeros, pero el bloque de acidez es de dos frases (sin Ka/pKa, resonancia dibujada, fenol ni basicidad de aminas) pese a que se evalúa. La pregunta de examen 2 tiene el apartado (b), su solución y su baremo copiados de otro ejercicio (conductividad de un ácido débil). Cálculos correctos (143; 1,6·10^11; °C→K). Presentación con fórmulas químicas y potencias en texto plano y nomenclatura no IUPAC.

**Plan de arreglo:** 1) Rehacer exam_questions[1] (b): respuesta, full_solution y baremo sobre la solubilidad del butanol. 2) Ampliar theory_blocks[3] (Ka/pKa, resonancia, fenol, aminas como bases). 3) Añadir aldehído/cetona a la tabla y la idea donador/aceptor. 4) Corregir la definición de isómeros, 'de los cinco', 'O-H por duplicado'. 5) Formatear fórmulas/potencias en LaTeX y usar nombres IUPAC; ejes de las figuras.

**Hallazgos de la revisión experta:**

1. **[ALTA · SOLUCION_EQUIVOCADA]** `exam_questions[1].answer` — El apartado (b) del enunciado pregunta por qué el 1-butanol es menos miscible que el ácido etanoico, pero la respuesta (b) habla de la conductividad eléctrica de un ácido débil: corresponde a otro ejercicio.
   - *Texto actual:* «(b) Aunque la disociación es parcial, los iones H3O+ y CH3COO- que sí se forman transportan la corriente.»
   - *Arreglo:* (b) El 1-butanol tiene un único -OH (un donador y un aceptor) y una cadena apolar de 4 C que ya pesa frente al grupo polar; el ácido etanoico tiene un -COOH (un donador y dos oxígenos aceptores) y solo un CH3 apolar: por eso el ácido es miscible y el butanol solo parcialmente soluble (≈7,7 g/100 g de agua).
2. **[ALTA · SOLUCION_EQUIVOCADA]** `exam_questions[1].full_solution` — La resolución del apartado (b) explica el equilibrio de disociación del ácido acético y la conductividad de su disolución, que no se pregunta; no explica en ningún momento la baja solubilidad del 1-butanol (cadena apolar de 4 C frente a un único -OH).
   - *Texto actual:* «(b) Ser un ácido débil significa que el equilibrio CH3COOH + H2O ⇌ CH3COO- + H3O+ está desplazado mayoritariamente hacia la izquierda... hace que la disolución conduzca la corriente»
   - *Arreglo:* Reescribir (b): comparar la parte polar (un -OH: 1 donador + 1 aceptor) con la parte apolar (cadena de 4 C, que rompe la red de enlaces de H del agua sin compensarlo); a partir de 4-5 C la cadena domina, de ahí la solubilidad limitada (7,7 g/100 g) frente a la miscibilidad total del ácido etanoico (solo un CH3 apolar y tres puntos de enlace de H).
3. **[ALTA · SOLUCION_EQUIVOCADA]** `exam_questions[1].mark_scheme` — Dos de los tres criterios de corrección puntúan la conductividad y la disociación parcial de un ácido débil, contenidos que el enunciado no pide; el criterio para (b) (cadena apolar del butanol) no existe.
   - *Texto actual:* «1 punto por relacionar conductividad con presencia de iones libres, no con la cantidad total de ácido»
   - *Arreglo:* Sustituir por: 1 punto por los puntos de enlace de H del -COOH (a); 1 punto por identificar que el butanol solo tiene un -OH; 1 punto por relacionar la cadena apolar de 4 C con la menor solubilidad (b). Redactar dirigido al alumno.
4. **[ALTA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — El bloque de acidez son dos frases: no explica qué es Ka/pKa ni por qué un pKa menor indica ácido más fuerte, no dibuja las estructuras resonantes del carboxilato ni el alcóxido, no cuantifica qué significa '10^11' ni trata el fenol, que se pide en exercises[2] y flashcards[9]. Tampoco hay propiedad química alguna de las aminas (basicidad), aunque el título promete 'propiedades químicas'.
   - *Texto actual:* «Los ácidos carboxílicos son mucho más ácidos que los alcoholes porque su base conjugada... la razón de constantes es $10^{16-4{,}8}\approx1{,}6\cdot10^{11}$.»
   - *Arreglo:* Ampliar a 3-4 párrafos: (1) R-COOH + H2O ⇌ R-COO⁻ + H3O⁺, Ka y pKa = −log Ka; (2) formas resonantes del acetato (carga −1/2 en cada O) frente al etóxido; (3) fenol (pKa ≈ 10) como caso intermedio: deslocalización hacia el anillo; (4) basicidad de las aminas (par libre del N; R-NH2 + H2O ⇌ R-NH3⁺ + OH⁻). Añadir la deducción Ka(A)/Ka(B) = 10^{pKa(B)−pKa(A)}.
5. **[MEDIA · CONCEPTO]** `exam_questions[1].full_solution` — En (a) se compara con el propan-1-ol (que no aparece en el enunciado, que habla del 1-butanol) y se afirma que el ácido es 'incluso más soluble que un alcohol de masa parecida'; el propan-1-ol (60 g/mol) también es miscible en cualquier proporción, así que la afirmación es falsa para ese alcohol.
   - *Texto actual:* «Un alcohol como el propan-1-ol solo dispone de un oxígeno... resulta, de hecho, incluso más soluble que un alcohol de masa parecida.»
   - *Arreglo:* Comparar con el 1-butanol del enunciado y eliminar 'incluso más soluble que un alcohol de masa parecida' (o decir 'más soluble que el 1-butanol').
6. **[MEDIA · CONCEPTO]** `keywords[5].definition` — Definición de isómeros incorrecta: exige 'distinta conectividad', lo que excluye los estereoisómeros (cis-trans, ópticos), que tienen la misma conectividad y se estudian en esta misma unidad.
   - *Texto actual:* «Compuestos con la misma fórmula molecular pero distinta conectividad»
   - *Arreglo:* Compuestos con la misma fórmula molecular pero distinta estructura (distinta conectividad —isómeros estructurales— o distinta disposición espacial —estereoisómeros—), que pueden diferir mucho en sus propiedades.
7. **[MEDIA · CONCEPTO]** `theory_blocks[1].body` — En la tabla, para el ácido acético se indica 'O-H, por duplicado', lo que sugiere que la molécula tiene dos enlaces O-H. Solo tiene uno; lo que se duplica es el enlace de hidrógeno en el dímero cíclico.
   - *Texto actual:* «\| Ácido acético \| ácido carboxílico \| Sí (O-H, por duplicado) \|»
   - *Arreglo:* Escribir: 'Sí (un O-H; forma dímeros con dos enlaces de H)'.
8. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — La tabla comparativa no incluye aldehídos ni cetonas (dipolo-dipolo, sin enlace de H), que son los ejemplos más habituales en la PAU (p. ej., propanal/propanona frente a propan-1-ol y butano). Tampoco se explica el efecto de la masa o de la ramificación dentro de una serie homóloga.
   - *Texto actual:* «\| Metil formiato \| éster \| No \| 60,1 \| 31,5°C \|»
   - *Arreglo:* Añadir propanal (M = 58,1; Teb ≈ 48 °C) y propanona (M = 58,1; Teb ≈ 56 °C) a la tabla como ejemplos de dipolo-dipolo, y una frase sobre el aumento de Teb con la longitud de cadena y su descenso con la ramificación.
9. **[MEDIA · LATEX]** `worked_examples[3].reasoning[0]` — Potencias y constantes en texto plano (check_lesson lo detecta): 'Ka=10^-pKa', '10^(16-4,8)=10^11,2', y en flashcards[7].back 'Ka(A)/Ka(B) = 10^(pKa(B)-pKa(A))'. También el enunciado del ejemplo usa 'pKa≈4,8' sin formato.
   - *Texto actual:* «pKa=-log Ka, así que Ka=10^-pKa»
   - *Arreglo:* Usar $\mathrm{p}K_a=-\log K_a$, $K_a=10^{-\mathrm{p}K_a}$, $10^{16-4{,}8}=10^{11{,}2}\approx1{,}6\cdot10^{11}$ y $K_a(A)/K_a(B)=10^{\mathrm{p}K_a(B)-\mathrm{p}K_a(A)}$ en worked_examples[3].statement/knowns/reasoning[0-1] y flashcards[7].back.
10. **[MEDIA · LATEX]** `theory_blocks[1].body` — Toda la lección escribe fórmulas químicas sin subíndices (C2H6O, CH3-O-CH3, C2H4O2, HOCH2CH2OH, H3O+, CH3COO-), temperaturas como 'Teb=-0,5°C' y la ecuación de disociación sin estados ni formato (exam_questions[1].full_solution).
   - *Texto actual:* «Teb=-0,5°C ... CH3COOH + H2O ⇌ CH3COO- + H3O+»
   - *Arreglo:* Formatear con $\mathrm{C_2H_6O}$, $\mathrm{CH_3{-}O{-}CH_3}$, $T_{eb}=-0{,}5\,^{\circ}\mathrm{C}$, $\mathrm{CH_3COOH(aq)+H_2O(l)\rightleftharpoons CH_3COO^-(aq)+H_3O^+(aq)}$ en enunciados, soluciones, tablas y fichas.
11. **[MEDIA · ERRATA]** `mcq[4].explanation` — El enunciado habla de cuatro compuestos y la explicación dice 'de los cinco'.
   - *Texto actual:* «El butano es el único de los cinco sin ningún átomo electronegativo»
   - *Arreglo:* Cambiar 'de los cinco' por 'de los cuatro'.
12. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — Nomenclatura no IUPAC y poco coherente: 'metil formiato' (IUPAC: metanoato de metilo), '1-butanol/1-octanol/1-hexanol' junto a 'propan-1-ol', 'dimetil éter', 'ácido acético', 'propilamina', 'trimetilamina' sin dar el nombre sistemático en ningún sitio.
   - *Texto actual:* «\| Metil formiato \| éster \|»
   - *Arreglo:* Usar 'metanoato de metilo', 'butan-1-ol', 'octan-1-ol', 'hexan-1-ol', 'metoximetano (dimetil éter)', 'ácido etanoico (acético)', 'propan-1-amina (propilamina)', 'N,N-dimetilmetanamina (trimetilamina)', al menos en la primera aparición.
13. **[BAJA · ENUNCIADO]** `guided_exercises[1].hints[1]` — La pista pide contar 'los carbonos que no llevan ningún grupo -OH' (lo que daría 0 en el etanodiol y 5 en el hexanol), pero la respuesta (b) cuenta todos los carbonos (2 y 6). Además common_errors[0] habla de 'masa molecular parecida' cuando las masas son 62 y 102 g/mol.
   - *Texto actual:* «Para (b), cuenta los carbonos que no llevan ningún grupo -OH.»
   - *Arreglo:* Unificar: o la pista pide 'cuenta los carbonos de la cadena' (2 y 6), o la respuesta da 0 y 5 carbonos sin -OH. En common_errors[0] sustituir por 'Pensar que, al ser más pesado, el hexanol debería ser más soluble...' o eliminar 'parecida'.
14. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[0].body` — Se anuncia que la lección enseña 'tres preguntas' (¿H sobre O/N?, ¿cuántos oxígenos aporta el grupo?, ¿longitud de cadena?) que 'se desarrollan en los bloques siguientes', pero los bloques se organizan por propiedad (ebullición, solubilidad, acidez) y la segunda pregunta (número de oxígenos / capacidad aceptora) nunca se desarrolla en la teoría; solo aparece en exam_questions[1] y challenge_questions[0].
   - *Texto actual:* «basta con aprender a hacerse tres preguntas ante cualquier grupo funcional nuevo, y se desarrollan en los bloques siguientes.»
   - *Arreglo:* Añadir en el bloque de solubilidad un párrafo sobre donadores y aceptores de enlace de H (éteres, cetonas, ésteres aceptan pero no donan; -COOH aporta 1 donador + 2 aceptores) y enunciar explícitamente las tres preguntas en un bloque resumen.
15. **[BAJA · VISUAL]** `theory_blocks[1].assets[0]` — La figura no tiene título ni rótulo de eje con magnitud y unidad (solo números 0-400); usa kelvin mientras la tabla y todo el texto usan °C, y los valores llevan punto decimal (272.6) en vez de coma.
   - *Texto actual:* «Puntos de ebullición en kelvin de cinco compuestos»
   - *Arreglo:* Rotular el eje vertical '$T_{eb}$ / °C' y usar los mismos valores de la tabla (−0,5; 31,5; 48,0; 97,2; 117,9), con coma decimal; o al menos rotular 'T_eb (K)'.
16. **[BAJA · VISUAL]** `theory_blocks[1].assets[1]` — Las etiquetas 'dipolo' y 'puente de H' quedan atravesadas por la línea; además se habla de 'puente de H' mientras el texto usa siempre 'enlace de hidrógeno'.
   - *Texto actual:* «(figura: etiquetas superpuestas a la recta)»
   - *Arreglo:* Desplazar las etiquetas fuera de la línea y usar 'enlace de hidrógeno' para ser coherente con el texto.
17. **[BAJA · TEXTO_PARA_PROFESOR]** `exam_questions[0].mark_scheme` — Criterios de corrección redactados para el corrector ('se exige', 'Sin justificación, 0 puntos') en lugar de dirigidos al alumno, como pide la convención del curso.
   - *Texto actual:* «En (b), se exige explícitamente mencionar que el oxígeno del éster no lleva H unido»
   - *Arreglo:* 'Para obtener la puntuación completa debes justificar cada apartado; en (b) indica expresamente que ningún H del éster está unido a O.' (aplicar igual a exam_questions[1].mark_scheme).
18. **[BAJA · ERRATA]** `exercises[1].statement` — 'Más del doble de carbonos': el ácido hexanoico tiene 6 C y el propanoico 3 C (exactamente el doble). En la solución se dice 'casi tres veces más larga' (5 frente a 2 = 2,5 veces).
   - *Texto actual:* «con la misma cantidad de grupos -COOH pero más del doble de carbonos»
   - *Arreglo:* Decir 'el doble de carbonos (6 frente a 3)' y en la solución 'una cadena apolar de 5 C frente a 2 C (2,5 veces más larga)'.
19. **[BAJA · ERRATA]** `mcq[0].options[0].why_wrong` — La frase sugiere que el éter o la cetona son ejemplos de H unido a O, cuando son justo lo contrario (contraejemplos).
   - *Texto actual:* «hace falta además que algún H esté unido directamente a él, como en un éter o una cetona, que tienen O pero no pueden donar.»
   - *Arreglo:* '...hace falta además que algún H esté unido directamente a él. Un éter o una cetona, por ejemplo, tienen O pero no pueden donar.'
20. **[BAJA · ERRATA]** `misconceptions[0].correct_model` — 'causada únicamente por que' debe ser 'porque'; además 'únicamente' es excesivo (el ácido también es más polar).
   - *Texto actual:* «una diferencia de casi 87°C causada únicamente por que uno puede formar enlaces de hidrógeno»
   - *Arreglo:* '...una diferencia de casi 87 °C debida, sobre todo, a que uno puede formar enlaces de hidrógeno (tiene H unido a O) y el otro no.'

**Fallos de renderizado (vistos en el navegador):**

- [MEDIA · LATEX] `worked_examples[3].reasoning[0]` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^-] …pKa=-log Ka, así que Ka=10^-pKa; el cociente de dos Ka es 10 elevado a la diferencia de los pKa, con el s…». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».
- [MEDIA · LATEX] `worked_examples[3].reasoning[1]` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^(] …Ka(ácido)/Ka(etanol)=10^(16-4,8)=10^11,2. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».
- [MEDIA · LATEX] `flashcards[7].back` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^(] …Ka(A)/Ka(B) = 10^(pKa(B)-pKa(A)); nunca se divide directamente un pKa entre otro. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».

**Chequeos automáticos:**

- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 5 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Falsa. (c) Verdadera. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 25 — Polimerización por condensación

**Valoración experta: MEDIA.** Los cálculos son correctos y están bien explicados (88,11; 172,18; 594,53; 696,98; 9627; 470,66; 1657,7; 1375,9; unidades C10H8O4 = 192,17 y C12H22N2O2 = 226,32). La teoría no muestra nunca la estructura de la unidad repetitiva ni la ecuación de polimerización con [ ]n y (2n−1) H2O, que es lo que se pide en la PAU. exercises[3] tiene solución incompleta (solo la masa). Faltan los polímeros de condensación de un solo monómero (hidroxiácidos, aminoácidos/proteínas) y la baquelita. Fórmulas en texto plano.

**Plan de arreglo:** 1) Añadir ecuaciones de polimerización y unidades repetitivas estructurales de PET y nailon-6,6. 2) Completar exercises[3] (a)(b)(c). 3) Bloque sobre otros polímeros de condensación (PLA, proteínas, baquelita) y matizar que no siempre se necesitan dos monómeros. 4) Aclarar el poliuretano como poliadición. 5) Formatear fórmulas y corregir la referencia 'lección anterior'.

**Hallazgos de la revisión experta:**

1. **[ALTA · SOLUCION_INCOMPLETA]** `exercises[3].full_solution` — El enunciado pide (a) la reacción de condensación entre una molécula de cada monómero, (b) la estructura de la unidad repetitiva y (c) su masa molar. La solución solo da (c), en una línea, y además usa datos distintos de los del enunciado (62,08 y 18,02 en vez de 62,07 y 18,015).
   - *Texto actual:* «$M=166{,}13+62{,}08-2(18{,}02)=192{,}17$ g/mol.»
   - *Arreglo:* (a) $\mathrm{HOOC{-}C_6H_4{-}COOH + HO{-}CH_2CH_2{-}OH \rightarrow HOOC{-}C_6H_4{-}CO{-}O{-}CH_2CH_2{-}OH + H_2O}$; (b) $\mathrm{\left[{-}CO{-}C_6H_4{-}CO{-}O{-}CH_2{-}CH_2{-}O{-}\right]_n}$ (C10H8O4); (c) $M=166{,}13+62{,}07-2\cdot18{,}015=192{,}17\,\mathrm{g/mol}$. Ampliar también answer con los tres apartados.
2. **[ALTA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — En toda la lección no aparece nunca la fórmula estructural de la unidad repetitiva de PET ni de nailon-6,6 entre corchetes con subíndice n, ni la ecuación global de polimerización; solo se da la fórmula molecular mediante una 'resta' de H2O. Es lo que más se pide en la PAU (exam_notes[1] lo reconoce) y lo exige exercises[3](b).
   - *Texto actual:* «$C_8H_6O_4 + C_2H_6O_2 - 2\,H_2O \rightarrow C_{10}H_8O_4 \quad (M=192{,}17\ \text{g/mol})$»
   - *Arreglo:* Añadir: $n\,\mathrm{HOOC{-}C_6H_4{-}COOH}+n\,\mathrm{HO{-}CH_2CH_2{-}OH}\rightarrow \mathrm{H{-}[O{-}CO{-}C_6H_4{-}CO{-}O{-}CH_2CH_2]_n{-}OH}+(2n-1)\,\mathrm{H_2O}$ y la unidad $\mathrm{[{-}CO{-}C_6H_4{-}CO{-}O{-}CH_2{-}CH_2{-}O{-}]_n}$, marcando el enlace éster. Igual en theory_blocks[3] para el nailon-6,6: $\mathrm{[{-}NH{-}(CH_2)_6{-}NH{-}CO{-}(CH_2)_4{-}CO{-}]_n}$, marcando el enlace amida.
3. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[1].body` — La teoría solo contempla el esquema diácido + diol/diamina. Faltan: monómeros con dos grupos distintos en la misma molécula (hidroxiácidos → PLA; aminoácidos → proteínas, enlace peptídico), polímeros de condensación naturales (proteínas, polisacáridos), otros subproductos (HCl con cloruros de ácido, metanol), y resinas de condensación entrecruzadas como la baquelita (fenol + metanal), que la lección 26 usa como ejemplo. De hecho misconceptions[1].correct_model afirma que 'hace falta un diácido... combinado con un diol o una diamina'.
   - *Texto actual:* «Un diácido, HOOC-R-COOH, puede reaccionar por los dos lados»
   - *Arreglo:* Añadir un bloque: 'Otros polímeros de condensación': (1) un solo monómero con dos grupos distintos: HO-R-COOH → poliéster (PLA), H2N-CHR-COOH → proteínas (enlace peptídico -CO-NH-); (2) otros subproductos (HCl, CH3OH); (3) baquelita (fenol + metanal, red tridimensional). Matizar misconceptions[1].correct_model y guided_exercises[1](c): 'un diácido o un monómero con dos grupos reactivos'.
4. **[MEDIA · LATEX]** `summary.formulas[0]` — Fórmulas fuera de LaTeX o mal formateadas: flashcards[7].back 'M_oligómero = Σ M_monómeros - (k-1)·M(H2O)', exam_questions[1].answer 'M_olig = nM1+nM2-(2n-1)·18,015', exercises[1].answer 'M_oligómero', worked_examples[3].solution '9,63·10^3' (detectado por check_lesson). En la teoría, $HO$ y $H_2O$ salen en cursiva por no usar \mathrm. Fórmulas químicas en todo el texto sin subíndices (H2O, CH2, C6H4).
   - *Texto actual:* «M_olig = nM1+nM2-(2n-1)·18,015»
   - *Arreglo:* Usar $M_{\text{olig}}=nM_1+nM_2-(2n-1)\cdot18{,}015$, $9{,}63\cdot10^{3}\,\mathrm{g/mol}$, $\mathrm{HO{-}R'}$, $\mathrm{H_2O}$, $\mathrm{HOOC{-}C_6H_4{-}COOH}$, etc.
5. **[BAJA · CONCEPTO]** `exercises[2].full_solution` — El poliuretano se deja como 'caso límite' sin decir cómo se clasifica: según la IUPAC y la mayoría de textos es un polímero de poliadición (crecimiento por etapas sin subproducto), no de condensación. Además el enunciado afirma de entrada que 'se obtiene por condensación' y la pista habla de que la definición exige 'dos productos distintos', lo que no coincide con la definición dada en la teoría.
   - *Texto actual:* «Por eso algunos lo tratan como un caso intermedio entre adición y condensación clásicas.»
   - *Arreglo:* Concluir: 'En sentido estricto no es un polímero de condensación (no se libera ninguna molécula pequeña); se clasifica como de poliadición o crecimiento por etapas, y a menudo se agrupa con poliésteres y poliamidas por usar monómeros bifuncionales'. Cambiar el enunciado a 'se obtiene a partir de...' y la pista a '¿exige liberar una molécula pequeña?'.
6. **[BAJA · CONCEPTO]** `theory_blocks[2].body` — Nombres no sistemáticos sin su equivalente IUPAC: 'ácido tereftálico' (ácido benceno-1,4-dicarboxílico), 'politereftalato de etileno' (poli(tereftalato de etileno)).
   - *Texto actual:* «el ácido tereftálico (HOOC-C6H4-COOH, M=166,13 g/mol)»
   - *Arreglo:* Añadir 'ácido benceno-1,4-dicarboxílico (ácido tereftálico)' y escribir 'poli(tereftalato de etileno)'.
7. **[BAJA · MCQ]** `mcq[4].options[3].why_wrong` — La opción D habla de 'una por cada pareja ácido-diol', pero la explicación del error habla de 'parejas de monómeros iguales entre sí', que no es lo que dice la opción.
   - *Texto actual:* «El número de enlaces no es el número de parejas de monómeros iguales entre sí»
   - *Arreglo:* 'El número de enlaces no es el número de parejas ácido-diol (3), sino el de huecos entre monómeros consecutivos de la cadena: 5.'
8. **[BAJA · ENUNCIADO]** `worked_examples[0].statement` — Un ácido 'monocarboxílico' de M = 116,07 g/mol no corresponde a ningún ácido sencillo: 116,07 es la masa de C4H4O4 (ácido maleico/fumárico), que es un diácido. El dato confunde a quien intente identificar el compuesto.
   - *Texto actual:* «Un ácido monocarboxílico de masa M=116,07 g/mol»
   - *Arreglo:* Usar un ácido real, p. ej., ácido hexanoico (M = 116,16 g/mol) con butan-1-ol (74,12): M(éster) = 116,16 + 74,12 − 18,015 = 172,27 g/mol; o nombrar los compuestos.
9. **[BAJA · PLANTILLA]** `common_mistakes[2].why` — Frase genérica sin relación con el error descrito (proponer un monómero monofuncional).
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Se comprueba que el monómero tiene el grupo funcional adecuado (-COOH), pero no cuántos tiene.'
10. **[BAJA · REFERENCIA_ROTA]** `prerequisites[2].statement` — Dice que la polimerización por adición se vio 'en la lección anterior', pero la lección anterior (24) trata de propiedades de grupos funcionales; la adición está en la lección 21.
   - *Texto actual:* «recordar cómo funciona la polimerización por adición vista en la lección anterior»
   - *Arreglo:* '...vista en la lección de polimerización por adición'.
11. **[BAJA · LATEX]** `theory_blocks[1].body` — Las ecuaciones de esterificación y amidación no indican estados de agregación ni condiciones (catalizador ácido, calor), en contra de la convención del curso, y usan → en lugar de ⇌ (la esterificación es un equilibrio, como se dice en la lección 27).
   - *Texto actual:* «$R\text{-COOH} + HO\text{-}R' \rightarrow R\text{-CO-O-}R' + H_2O$»
   - *Arreglo:* Escribir $\mathrm{R{-}COOH + HO{-}R' \rightleftharpoons R{-}COO{-}R' + H_2O}$ con 'H⁺, calor' sobre la flecha.
12. **[BAJA · TEXTO_PARA_PROFESOR]** `exam_questions[0].mark_scheme` — Baremos redactados para el corrector ('se exige', 'Sin justificación, 0 puntos'), no para el alumno.
   - *Texto actual:* «En (d) se exige mencionar explícitamente la excepción (apertura de anillo)»
   - *Arreglo:* 'Para la puntuación completa debes justificar cada apartado; en (d) menciona el nailon-6 (apertura de anillo)'. Igual en exam_questions[1].mark_scheme.
13. **[BAJA · ESTRUCTURA]** `challenge_questions` — La lista de retos está vacía, a diferencia de las lecciones vecinas.
   - *Texto actual:* «challenge_questions = []»
   - *Arreglo:* Añadir un reto, p. ej., deducir los monómeros a partir de un fragmento de poliamida/poliéster dado, o el grado de polimerización a partir de la masa molar.
14. **[BAJA · ERRATA]** `theory_blocks[0].body` — 'el enlace que crece la cadena' (crecer es intransitivo); se repite en exercises[0].full_solution. En diagnostic_items[0] 'de un ácido acético ... con un etanol' (artículo indefinido impropio).
   - *Texto actual:* «se forman dos productos: el enlace que crece la cadena, y una molécula pequeña»
   - *Arreglo:* 'el enlace que hace crecer la cadena'; 'del ácido acético con etanol'.

**Fallos de renderizado (vistos en el navegador):**

- [MEDIA · LATEX] `worked_examples[3].solution` — Potencia/superíndice escrito fuera de fórmula: se ve el «^» literal en pantalla. Texto: «[0^3] …3)+50(62,07)-99(18,015) = 11410,0-1783,5=9627 g/mol ≈ 9,63·10^3 g/mol. …». Arreglo: Envolver en $...$ con llaves: p. ej. «10^23» → «$10^{23}$», «3d^6» → «$3d^6$».

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[2].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 5 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Falsa. (c) Verdadera. (d) Falsa.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 26 — Clasificación, estructura y propiedades de los polímeros

**Valoración experta: BAJA.** Lección conceptualmente sólida: ramificación frente a reticulación, termoplástico/elastómero/termoestable y PE-HD frente a PE-LD están bien razonados, y los ejercicios y V/F están completos y justificados. Puntos débiles: el PET como ejemplo de copolímero (ambiguo según la IUPAC) en el test, un diagnóstico cuya interpretación no corresponde a la pregunta, teoría presentada en muros de texto, y faltan criterios de clasificación (mecanismo, comportamiento térmico) y tipos de copolímero. Sin cálculos.

**Plan de arreglo:** 1) Cambiar el ejemplo de copolímero (SBR/ABS) o añadir una nota IUPAC. 2) Corregir la interpretación y la remediación de diagnostic_items[1]. 3) Pasar las clasificaciones a listas o tablas. 4) Añadir los criterios de mecanismo y comportamiento térmico, los tipos de copolímero y una tabla de polímeros comunes. 5) Corregir las plantillas, la errata y el pie de figura.

**Hallazgos de la revisión experta:**

1. **[MEDIA · VISUAL]** `theory_blocks[1].body` — Las clasificaciones se presentan en un único párrafo largo con categorías separadas por punto y coma y paréntesis anidados (natural/sintético/semisintético; homo/copolímero). Lo mismo ocurre en theory_blocks[0] (tres criterios), theory_blocks[2] (lineal/ramificada/reticulada) y theory_blocks[3] (termoplástico/termoestable): son muros de texto difíciles de estudiar.
   - *Texto actual:* «Según su origen: Naturales (se obtienen directamente de seres vivos, ...); Sintéticos (...); Semisintéticos (...»
   - *Arreglo:* Convertir cada clasificación en una lista con viñetas ('- **Naturales**: ... Ej.: ...') o en una tabla 'Tipo \| Definición \| Ejemplos'. Para termoplástico/elastómero/termoestable, usar una tabla 'estructura \| al calentar \| ejemplos \| reciclaje mecánico'.
2. **[MEDIA · ESTRUCTURA]** `diagnostic_items[1].common_wrong_answers[0].interpretation` — La pregunta diagnóstica trata del monómero del PE y de si es de adición o de condensación, pero la interpretación del error, la remediación y la respuesta errónea típica ('invertir los dos') hablan de la clasificación por origen (natural/sintético), que no tiene nada que ver.
   - *Texto actual:* «No tiene claro el criterio de clasificación por origen (existir ya en un ser vivo frente a fabricarse a partir de monómeros).»
   - *Arreglo:* Interpretación: 'Confunde adición (monómero con doble enlace, sin subproducto) con condensación'. Remediación: 'Repasar CH2=CH2 → [−CH2−CH2−]n y comprobar que no se libera ninguna molécula'. Respuesta errónea: 'Decir que es de condensación'.
3. **[MEDIA · VERIFICAR]** `mcq[4]` — Se usa el PET como ejemplo de copolímero (aquí, en theory_blocks[1], exercises[0] y flashcards[8]). Muchos libros de Bachillerato lo aceptan, pero la IUPAC considera homopolímeros los polímeros de dos monómeros complementarios (AA + BB), como el PET o el nailon-6,6, porque derivan de un único 'monómero implícito' (la unidad repetitiva). La opción A ('Homopolímero') sería correcta según la IUPAC, aunque con una justificación equivocada. Es un ejemplo ambiguo para la pregunta de test.
   - *Texto actual:* «D: Copolímero, porque intervienen dos monómeros químicamente distintos.»
   - *Arreglo:* Verificar el criterio de la PAU de referencia. Para que el test no sea ambiguo, usar como ejemplo de copolímero uno indiscutible (SBR: estireno + buta-1,3-dieno; ABS; EVA) en mcq[4], exercises[0] y theory_blocks[1], y añadir una nota: 'el PET y el nailon-6,6 se describen a menudo como copolímeros alternados, aunque la IUPAC los trata como homopolímeros de su unidad repetitiva'.
4. **[BAJA · CONCEPTO]** `diagnostic_items[0].remediation_action` — Sobrestima las fuerzas de Van der Waals: por cada interacción son típicamente de 0,1 a unos 10 kJ/mol (el enlace de hidrógeno, de 10 a 40 kJ/mol), no 'unas pocas decenas'; el C-C ronda 350 kJ/mol.
   - *Texto actual:* «una interacción de Van der Waals apenas llega a unas pocas decenas»
   - *Arreglo:* 'un enlace C-C ronda 350 kJ/mol, mientras que una interacción de Van der Waals suele ser de 0,1 a unos 10 kJ/mol (un enlace de hidrógeno, hasta unos 40 kJ/mol)'.
5. **[BAJA · SOLUCION_INCOMPLETA]** `exam_questions[1].answer` — El campo answer solo recoge el apartado (a); el (b), que vale 2 de los 3 puntos, no aparece en el resumen destacado.
   - *Texto actual:* «(a) Material X: termoplástico. Material Y: termoestable.»
   - *Arreglo:* Añadir: '(b) X: cadenas independientes unidas por fuerzas intermoleculares (se ablanda y se disuelve); Y: red covalente (no funde, se descompone; insoluble)'.
6. **[BAJA · TEORIA_INCOMPLETA]** `theory_blocks[0].body` — Se presentan solo tres criterios de clasificación. Faltan los habituales en la PAU: por mecanismo de polimerización (adición/condensación) y por comportamiento frente al calor o propiedades (termoplásticos, termoestables, elastómeros, fibras), aunque luego se usan. Tampoco se citan los tipos de copolímero (alternado, al azar, de bloque, de injerto) ni los polímeros de adición más comunes con su monómero (PP, PS, PTFE, PMMA).
   - *Texto actual:* «Un mismo polímero se puede clasificar a la vez por tres criterios independientes»
   - *Arreglo:* Añadir a la lista: 'por el mecanismo de formación (adición o condensación)' y 'por su comportamiento térmico (termoplásticos, termoestables, elastómeros)'; una línea con los tipos de copolímero y una tabla breve de polímeros comunes (monómero → polímero → uso).
7. **[BAJA · PLANTILLA]** `common_mistakes[0].why` — Frase genérica sin relación con el error (confundir ramificación con reticulación); se repite literalmente en common_mistakes[1].why.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* [0]: 'Ambas palabras sugieren una cadena «no recta» y no se comprueba si el enlace extra une cadenas distintas'. [1]: 'Se extrapola la fusión de sólidos moleculares sin pensar en una red covalente'.
8. **[BAJA · LATEX]** `worked_examples[1].statement` — Unidades y fórmulas sin formato: 'g/cm3' (en enunciado y knowns), CH₂=CH₂ con subíndices Unicode en diagnostic_items[1] y texto plano en el resto.
   - *Texto actual:* «densidad típica de referencia en torno a 0,95 g/cm3»
   - *Arreglo:* Escribir $0{,}95\,\mathrm{g/cm^3}$, $0{,}92\,\mathrm{g/cm^3}$ y $\mathrm{CH_2{=}CH_2}$.
9. **[BAJA · VISUAL]** `theory_blocks[2].assets[0].caption` — El pie dice que las ramas aparecen 'en azul', pero en la figura las ramas son del mismo color azul oscuro casi negro que la cadena principal y no se distinguen. Además, la estructura reticulada se representa solo como una 'escalera' entre dos cadenas, no como una red tridimensional.
   - *Texto actual:* «ramificada (ramas dentro de la misma macromolécula, en azul)»
   - *Arreglo:* Colorear las ramas de azul claro (o quitar 'en azul' del pie) y dibujar una red reticulada con 3-4 cadenas unidas en varias direcciones.
10. **[BAJA · TEXTO_PARA_PROFESOR]** `exam_questions[0].mark_scheme` — Baremos dirigidos al corrector ('se exige', 'Sin justificación, 0 puntos').
   - *Texto actual:* «En (c) se exige mencionar explícitamente que el entrecruzamiento del caucho vulcanizado es ligero, no ausente»
   - *Arreglo:* 'Para la puntuación completa debes justificar cada apartado; en (c) indica que el entrecruzamiento es ligero, no ausente'.
11. **[BAJA · ESTRUCTURA]** `challenge_questions` — challenge_questions y summary.formulas están vacíos.
   - *Texto actual:* «challenge_questions = []»
   - *Arreglo:* Añadir un reto (p. ej., predecir el comportamiento al calentar y al disolver de un polímero a partir de un esquema de red dado) o eliminar el campo vacío de fórmulas si la web no lo muestra.
12. **[BAJA · ERRATA]** `worked_examples[3].common_mistake` — Frase sin sentido al final.
   - *Texto actual:* «lo que calienta de más es la propia red química.»
   - *Arreglo:* '...en un termoestable no hay cadenas sueltas que fundir: al calentar de más lo que se rompe es la propia red covalente'.

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (2): `common_mistakes[0].why`, `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.
- [BAJA · PLANTILLA] Texto idéntico repetido en 8 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].answer`. Ej.: «(a) Falsa. (b) Verdadera. (c) Falsa. (d) Verdadera.». Arreglo: Escribir contenido específico de cada lección.

#### Lección 27 — Aplicaciones, reciclaje e impacto ambiental de los polímeros

**Valoración experta: MEDIA.** Lección bien enfocada (decidir con criterios estructurales) y con buenos ejercicios razonados (compostable frente a persistente, nailon frente a proteína, mezcla de PVC y PET). Errores conceptuales: atribuye la resistencia del PE a que el enlace C-C es 'mucho más fuerte' (falso; es una cuestión de reactividad) y niega que exista reciclaje químico para polímeros de adición. La teoría ambiental es estrecha (falta valorización energética, microplásticos, 3R, bioplásticos), no hay ninguna ecuación de hidrólisis del PET y el bloque de aplicaciones es un muro de texto.

**Plan de arreglo:** 1) Corregir el argumento 'C-C más fuerte' en la teoría, WE3 y V/F (c). 2) Ampliar la definición de reciclaje químico (pirólisis). 3) Añadir la ecuación de hidrólisis del PET. 4) Bloque de gestión de residuos (valorización, vertedero, microplásticos, 3R, PLA). 5) Tabla de aplicaciones; corregir la ficha 2, la plantilla y los baremos.

**Hallazgos de la revisión experta:**

1. **[MEDIA · CONCEPTO]** `theory_blocks[2].body` — Se justifica que el PE no se hidroliza diciendo que los enlaces C-C son 'mucho más fuertes'. Es falso: la energía media del enlace C-C (≈347 kJ/mol) es parecida a la del C-O del éster (≈358 kJ/mol). La hidrólisis del éster es fácil porque el carbono del carbonilo, polar y electrófilo, ofrece una vía de reacción con el agua, no porque el enlace sea más débil. El error se repite en worked_examples[2].reasoning[2] y exam_questions[0].full_solution (c).
   - *Texto actual:* «hace falta romper enlaces covalentes C-C mucho más fuertes, normalmente con procesos de temperatura muy alta (pirólisis)»
   - *Arreglo:* '...la cadena C-C es apolar y no tiene ningún punto que el agua pueda atacar (no hay C=O electrófilo), así que no existe una vía de reacción suave; para romperla hay que recurrir a la pirólisis o craqueo a alta temperatura y sin oxígeno'. Corregir igual en worked_examples[2].reasoning[2] y exam_questions[0].full_solution.
2. **[MEDIA · CONCEPTO]** `summary.key_points[2]` — Se afirma que el reciclaje químico 'no es posible' en polímeros de adición, identificando reciclaje químico con hidrólisis. En realidad la pirólisis o el craqueo de poliolefinas y la despolimerización térmica de PMMA o PS a sus monómeros son formas de reciclaje químico. La propia teoría menciona la pirólisis, pero no la llama reciclaje químico, lo que lleva a una conclusión falsa.
   - *Texto actual:* «Reciclaje químico: hidrólisis de enlaces éster o amida, posible en poliésteres y poliamidas ..., no en polímeros de adición de cadena C-C pura (como el PE).»
   - *Arreglo:* 'Reciclaje químico: romper el polímero en moléculas pequeñas reutilizables. En poliésteres y poliamidas, por hidrólisis (o glicólisis/metanólisis) hasta los monómeros; en polímeros de adición como el PE, solo con procesos más duros (pirólisis o craqueo → hidrocarburos).' Ajustar keywords[1] y theory_blocks[2].
3. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[3].body` — El impacto ambiental se reduce a la hidrolizabilidad de la cadena. Faltan contenidos habituales de este epígrafe en la PAU: valorización energética o incineración (y sus problemas, como el HCl o las dioxinas del PVC), vertederos, microplásticos, la regla de las 3R o la economía circular, y la distinción entre bioplástico de origen biológico, biodegradable y compostable (con ejemplos como PLA o PHA).
   - *Texto actual:* «La razón química de esa persistencia es la misma que la del reciclaje químico»
   - *Arreglo:* Añadir un bloque 'Gestión de residuos plásticos': reducir/reutilizar/reciclar (mecánico, químico, valorización energética con sus emisiones de CO2 y, en el PVC, HCl y dioxinas) y vertedero; microplásticos; bioplásticos (PLA de almidón de maíz, compostable industrialmente).
4. **[MEDIA · TEORIA_INCOMPLETA]** `theory_blocks[2].body` — El reciclaje químico del PET solo se describe con palabras: no hay ninguna ecuación de hidrólisis, aunque exam_notes[1] dice que es una pregunta habitual y worked_examples[2] la pide.
   - *Texto actual:* «Calentando el polímero con agua (y, normalmente, un catalizador) se recuperan el diácido y el diol»
   - *Arreglo:* Añadir: $\mathrm{[{-}CO{-}C_6H_4{-}CO{-}O{-}CH_2CH_2{-}O{-}]_n + 2n\,H_2O \xrightarrow{H^+\ o\ OH^-,\ \Delta} n\,HOOC{-}C_6H_4{-}COOH + n\,HOCH_2CH_2OH}$, y mencionar la glicólisis y la metanólisis como variantes industriales.
5. **[MEDIA · VISUAL]** `theory_blocks[1].body` — Cinco casos de aplicación (envase, tubería, bolsa, aislante, mango) en un único párrafo largo: es un muro de texto.
   - *Texto actual:* «Envase ligero y transparente para una bebida, ... Tubería rígida, ... Bolsa flexible y barata, ... Aislante térmico ligero ... Mango de una sartén»
   - *Arreglo:* Pasar a una tabla 'Aplicación \| Propiedad exigida \| Polímero \| Razón estructural' (PET, PVC, PE-LD, EPS, baquelita) y, si cabe, añadir PP, PTFE (antiadherente) y nailon (fibras).
6. **[BAJA · CONCEPTO]** `theory_blocks[1].body` — Se dice que el PET admite reciclaje químico (hidrólisis) 'al ser termoplástico'. El reciclaje químico por hidrólisis depende de que sea un poliéster, no de que sea termoplástico.
   - *Texto actual:* «Al ser termoplástico, además, admite reciclaje mecánico (refundido) y químico (hidrólisis a sus monómeros).»
   - *Arreglo:* 'Al ser termoplástico admite reciclaje mecánico, y al ser un poliéster admite además reciclaje químico por hidrólisis.'
7. **[BAJA · CONCEPTO]** `mcq[4].options[1].why_wrong` — Generalización falsa: hay termoplásticos de alta temperatura (PTFE, el recubrimiento antiadherente de las sartenes; PEEK) que no se ablandan con el calor de la cocina.
   - *Texto actual:* «Un termoplástico, ramificado o no, se ablandaría con el calor de la cocina»
   - *Arreglo:* 'Un termoplástico común (como el PE ramificado) se ablandaría a unos 100 °C, justo lo que se quiere evitar.'
8. **[BAJA · CONCEPTO]** `theory_blocks[4].body` — Nombres comerciales sin la forma IUPAC (PVC 'policloruro de vinilo' = poli(cloroeteno); PS = poli(feniletileno); PET = poli(tereftalato de etileno)). Es un detalle menor, pero el curso sigue la nomenclatura IUPAC.
   - *Texto actual:* «\| 3 \| PVC (policloruro de vinilo) \|»
   - *Arreglo:* Añadir entre paréntesis el monómero o nombre sistemático: PVC, poli(cloruro de vinilo), monómero cloroeteno; PS, monómero feniletileno (estireno); PP, monómero propeno.
9. **[BAJA · PLANTILLA]** `common_mistakes[1].why` — Frase genérica sin relación con el error descrito.
   - *Texto actual:* «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.»
   - *Arreglo:* 'Se repite la idea divulgativa «el plástico tarda siglos» sin relacionarla con el tipo de enlace de la cadena principal.'
10. **[BAJA · TEXTO_PARA_PROFESOR]** `exam_questions[0].mark_scheme` — Baremos dirigidos al corrector ('se exige', 'Sin justificación, 0 puntos').
   - *Texto actual:* «En (c) se exige mencionar explícitamente la ausencia de enlaces hidrolizables en la cadena del PE»
   - *Arreglo:* 'Para la puntuación completa debes justificar cada apartado; en (c) indica que la cadena del PE no tiene enlaces hidrolizables.'
11. **[BAJA · ERRATA]** `flashcards[2].back` — Frase confusa: 'aunque no sean fácilmente reciclables mecánicamente o viceversa' no tiene sentido.
   - *Texto actual:* «posible en poliésteres y poliamidas aunque no sean fácilmente reciclables mecánicamente o viceversa.»
   - *Arreglo:* 'No: también existe el reciclaje químico (hidrólisis hasta los monómeros en poliésteres y poliamidas; pirólisis en poliolefinas).'

**Chequeos automáticos:**

- [MEDIA · PLANTILLA] Texto genérico de plantilla, no específico de esta lección/ejercicio. (1): `common_mistakes[1].why`. Ej.: «El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.». Arreglo: Sustituir por contenido específico.
- [BAJA · PLANTILLA] Texto idéntico repetido en 56 lecciones del curso (probable plantilla genérica). (1): `exam_questions[0].mark_scheme[1]`. Ej.: «Sin justificación, 0 puntos aunque la calificación V/F sea correcta». Arreglo: Escribir contenido específico de cada lección.

