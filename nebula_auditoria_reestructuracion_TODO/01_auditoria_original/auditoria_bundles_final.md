# Auditoría independiente completa de `bundles.zip`

**Fecha de auditoría:** 19 de octubre de 2026  
**Objeto:** contenido JSON mostrado en la web de cursos de ESO, Selectividad/PAU y GCSE/IGCSE.  
**Capas revisadas:** (1) corrección técnica/científica/matemática; (2) calidad pedagógica, secuencia, claridad y adecuación de carga; (3) integridad del JSON y trazabilidad de la UI.

---

## 1. Resumen ejecutivo

El producto tiene una base buena: hay abundancia de ejemplos, ejercicios, preguntas de examen, errores frecuentes, flashcards y explicaciones que, en muchos bloques, son claramente superiores a unos apuntes tradicionales. El problema no es una falta general de contenido. El problema es **la falta de un control sistemático de alcance y consistencia**: una lección puede contener una explicación muy buena y, unas líneas después, una regla demasiado absoluta que contradice esa misma explicación.

La auditoría ha encontrado **errores reales de cálculo/respuesta**, **contradicciones internas**, **afirmaciones científicas demasiado fuertes**, **reglas de examen presentadas como verdades universales**, **problemas de versionado** y **carga pedagógica excesiva** en algunas familias.

### Veredicto global

- **No publicaría el corpus completo tal como está** sin corregir primero los P0 y P1.
- **No hace falta rehacerlo desde cero.** La arquitectura pedagógica tiene piezas valiosas; la mayor parte del trabajo es de corrección, normalización y secuenciación.
- El riesgo más importante no es un error aislado: es que ciertas simplificaciones se **repiten en teoría, flashcards y MCQ**, de forma que el alumno acaba memorizándolas como leyes universales.
- Hay señales claras de generación por múltiples versiones/agentes sin una única fuente de verdad: el caso más evidente es **ESO Física y Química**, que aparece duplicado en dos ramas divergentes.

### Volumen auditado

| Familia | Unidades JSON | Lecciones |
|---|---:|---:|
| ESO Física y Química | 4 | 19 |
| ESO Matemáticas | 20 | 122 |
| FQ completo | 22 | 143 |
| GCSE/IGCSE Chemistry | 13 | 70 |
| GCSE/IGCSE Physics | 10 | 62 |
| GCSE Mathematics | 9 | 87 |
| Selectividad Física | 8 | 76 |
| Selectividad Matemáticas | 12 | 101 |
| Selectividad Matemáticas CCSS | 9 | 66 |
| Selectividad Química | 9 | 127 |
| **Total** | **116** | **873** |

El ZIP contiene aproximadamente **84 millones de caracteres brutos**. Eliminando SVG/TikZ y metadatos gráficos quedan en torno a **38 millones de caracteres pedagógicos**.

---

## 2. Metodología

La revisión se ha hecho en tres niveles.

### 2.1. Controles exhaustivos sobre todo el corpus

Se recorrieron las 873 lecciones para comprobar, entre otras cosas:

- IDs duplicados dentro de una lección.
- Referencias a objetivos inexistentes.
- Opciones MCQ correctas con metadatos `why_wrong`.
- Presencia/ausencia de práctica y ejemplos resueltos según esquema.
- Densidad de palabras frente al tiempo estimado de la lección.
- Cadenas de igualdades numéricas susceptibles de incoherencia.
- Uso de expresiones de alto riesgo como “siempre”, “nunca”, “solo”, “únicamente”.
- Coherencia entre `correct`, explicación, opciones y cálculos visibles.

### 2.2. Revisión semántica por familias y unidades

Se revisaron teoría, resúmenes, ejemplos resueltos, MCQ, misconceptions y preguntas de examen de todas las familias, con profundización en los bloques de mayor riesgo: física moderna/electromagnetismo, termoquímica/ácido-base, cálculo/probabilidad/estadística, modelos de partículas y funciones/probabilidad GCSE.

### 2.3. Regla usada para clasificar

- **P0 — Bloqueante:** respuesta objetivamente incorrecta, pregunta imposible, contradicción interna fuerte o fallo de arquitectura que puede servir contenido incorrecto.
- **P1 — Alta:** concepto científicamente/matemáticamente falso si se toma literalmente, regla de examen enseñada como universal, o problema pedagógico grave.
- **P2 — Media:** falta de hipótesis, precisión, terminología o secuenciación que no suele romper el ejercicio prototipo pero sí el entendimiento transferible.
- **P3 — Baja:** feedback incompleto, estilo, consistencia de esquema o mejora de presentación.

---

# 3. BLOQUEANTES DE PUBLICACIÓN (P0)

## P0-01 — Selectividad Matemáticas: MCQ de probabilidad se contradice

**Ruta:** `selectividad_matematicas__mat_probabilidad / 04_Tablas_de_contingencia_y_diagramas_de_árbol / mcq[0]`

Las cuatro hojas son 0,3; 0,2; x; 0,1. La opción C y su `why_correct` calculan correctamente:

**x = 1 - 0,3 - 0,2 - 0,1 = 0,4**.

Sin embargo, el campo `explanation` termina afirmando **x = 0,2**.

**Por qué es bloqueante:** el sistema puede decirle al alumno que ha acertado y, a continuación, enseñarle el cálculo equivocado.

**Corrección:** unificar todas las fuentes de feedback y añadir un test que evalúe la expresión numérica esperada de la opción correcta.

---

## P0-02 — ESO Matemáticas: MCQ de regresión no tiene ninguna respuesta correcta

**Ruta:** `eso_matematicas__mat_estadistica_bidimensional / 03_Regresión_lineal_básica_interpretar_y_predecir / mcq[1]`

Se da:

- recta: y = 1,1x + 3,2
- x = 3
- observado y = 7

El JSON calcula 1,1·3 + 3,2 = 6,7. Es falso:

**1,1·3 + 3,2 = 3,3 + 3,2 = 6,5**.

Por tanto, el residuo observado - estimado es:

**7 - 6,5 = 0,5**.

El material marca 0,3 como correcto y **ninguna opción ofrece 0,5**.

**Corrección:** cambiar datos u opciones. Tal como está, la pregunta es irresoluble correctamente.

---

## P0-03 — GCSE Physics: contradicción directa en cambios de estado

**Ruta:** `gcse_ciencias_phys__U05_Thermal_Physics / 03_Melting_boiling_and_evaporation` (nombre JSON: `03_Melting_boiling_and_evaporation.json`).

La lección explica correctamente que, durante la meseta de una curva de calentamiento/enfriamiento, la temperatura permanece constante porque la energía intercambiada cambia la configuración/energía de interacción y **no la energía cinética media**.

Pero, al explicar condensación y congelación, afirma que durante el cambio las partículas **“slow down”**. Más adelante, el propio `challenge_question` marca explícitamente como error decir que durante la parte plana las partículas se frenan porque eso implicaría que la temperatura sigue descendiendo.

**Diagnóstico:** el mismo JSON contiene los dos modelos opuestos.

**Corrección:** distinguir tres fases:

1. Antes de la temperatura de cambio: baja/sube T y cambia energía cinética media.
2. Durante el cambio: T constante; cambia principalmente la energía potencial/configuración.
3. Después de completar el cambio: vuelve a cambiar la energía cinética media y T.

---

## P0-04 — ESO Física y Química: la misma contradicción sobre la meseta térmica

**Ruta:** `eso_fisicaquimica__U-ESO-02 / lesson_03`.

La teoría/resumen vincula absorber calor con aumentar energía cinética en un contexto donde después se evalúa correctamente que, durante el cambio de estado a temperatura constante, el aporte energético no aumenta la energía cinética media.

**Riesgo:** no es un matiz. La explicación que el alumno debe memorizar y la explicación que luego se considera correcta no coinciden.

**Corrección:** misma estructura en tres fases que en P0-03.

---

## P0-05 — Selectividad Física: inducción = “solo mientras hay movimiento relativo”

**Ruta:** `selectividad_fisica__electromagnetismo / 12_El_flujo_magnético_y_qué_induce_corriente`.

Aparece en objetivos, MCQ y resumen que la corriente inducida existe **solo mientras hay movimiento relativo** y cesa cuando se detiene.

El criterio general es:

**hay fem inducida cuando cambia el flujo magnético**, es decir, cuando dΦB/dt ≠ 0.

Puede existir flujo variable sin movimiento mecánico: por ejemplo, una espira fija en un campo B(t) variable o el secundario de un transformador. De hecho, la propia lección menciona el montaje de Faraday de dos bobinas, lo que hace la contradicción interna todavía más clara.

**Corrección:** “movimiento relativo” debe aparecer como **una manera** de cambiar el flujo, no como condición necesaria.

---

## P0-06 — Selectividad Física cuántica: la teoría corrige una regla y los ejercicios la vuelven a enseñar mal

**Ruta:** `selectividad_fisica__cuantica / 06_Indeterminación_y_la_nueva_mecánica_cuántica`.

La teoría contiene una advertencia correcta: que el producto de dos magnitudes tenga dimensiones de J·s es **condición necesaria pero no suficiente** para que sean conjugadas. Incluso pone el contraejemplo x y p_y.

Sin embargo:

- el objetivo pide decidirlo “mediante el criterio dimensional”;
- un worked example dice que el criterio es “puramente dimensional”;
- el MCQ lo usa como criterio de decisión;
- el resumen vuelve a decir que el criterio para saber qué pares cumplen es dimensional.

**Por qué es bloqueante:** la lección explícitamente sabe cuál es la idea correcta y, después, la contradice en los mecanismos de evaluación y repaso, que son precisamente lo que el alumno retiene.

**Corrección:** usar dimensiones solo como filtro negativo. Para afirmar conjugación, limitarse a pares expresamente estudiados o introducir la relación canónica/conmutador a nivel conceptual.

---

## P0-07 — Dos fuentes divergentes para el mismo curso ESO Física y Química

Existen 19 lecciones equivalentes en:

- `eso_fisicaquimica`
- `fq_completo` (bloques `U-ESO-*`)

No son copias idénticas. La segunda versión es mucho más extensa y, al menos en cambios de estado, corrige un error que sigue presente en la primera.

**Riesgo de producto:** no se puede garantizar que corregir un contenido corrija la versión que consume la web.

**Corrección arquitectónica:**

- una única fuente de verdad;
- `version_id`/hash por lección;
- generación de bundles derivados desde esa fuente;
- test de CI que falle si dos rutas que deberían representar la misma lección divergen sin una razón explícita.

---

## P0-08 — FQ completo: una respuesta correcta contiene `why_wrong`

**Ruta:** `fq_completo__U-B1Q-04 / lesson_01`.

Hay al menos dos casos donde la opción marcada como correcta también tiene `why_wrong`. Uno de ellos llega a explicar por qué “22,0 g” sería incorrecto aunque esa sea la respuesta correcta.

**Riesgo UI:** dependiendo de cómo consuma los metadatos la web, puede mostrar feedback contradictorio o considerar errónea una respuesta acertada.

**Corrección:** validador de esquema obligatorio:

- `option.key == correct` → `why_wrong` debe ser nulo/vacío;
- debería existir `why_correct` o explicación compatible;
- una única opción correcta salvo tipos de pregunta multiselección.

---

# 4. SELECTIVIDAD FÍSICA — Auditoría técnica

## 4.1. Campo gravitatorio

### P1 — “El trabajo del rozamiento siempre es negativo”

En el bloque de conservación de la energía aparece la idea de que el rozamiento **siempre** realiza trabajo negativo y por ello la energía mecánica solo disminuye.

Como regla del problema típico —bloque que desliza con rozamiento cinético sobre una superficie fija— funciona. Como afirmación física general es falsa: la fricción puede hacer trabajo positivo, negativo o nulo sobre un cuerpo según el sistema y la situación; una cinta transportadora es un contraejemplo sencillo.

**Reescritura recomendada:** “En el modelo habitual de rozamiento cinético sobre una superficie fija, el trabajo del rozamiento sobre el bloque es negativo y transforma energía mecánica en energía interna”.

### P2 — Kepler: r frente a semieje mayor a

La tercera ley aparece como T²/r³ = K. Para órbita circular es correcto usar r. Para una órbita elíptica, la magnitud general es el **semieje mayor a**.

**Recomendación:** presentar T²/a³ y añadir “en órbita circular, a=r”.

### P2 — a=g sin condición de caída libre

Algunas formulaciones identifican g con la aceleración que “adquiere cualquier cuerpo”. Debe quedar explícito que a=g si la gravedad es la única fuerza relevante.

### P2 — g máxima en la superficie

Es una propiedad del modelo esférico ideal empleado en Bachillerato, no una afirmación universal sobre cualquier distribución de masa. Conviene etiquetarlo como modelo.

---

## 4.2. Oscilaciones / M.A.S.

Hay una tendencia a convertir propiedades del M.A.S. ideal en propiedades de “las oscilaciones” en general:

- “oscilatorio” ≈ “periódico”;
- periodo independiente de amplitud;
- amplitud exponencial en cualquier amortiguamiento;
- “movimiento de vaivén = giro uniforme visto de canto”.

Estas son imágenes útiles, pero deben estar bajo el encabezado **modelo M.A.S. ideal**. Una oscilación amortiguada no es exactamente periódica y una envolvente exponencial supone amortiguamiento lineal/viscoso subamortiguado.

**Recomendación:** introducir primero la categoría “oscilación” y luego decir “el M.A.S. es el modelo especial que cumple…”.

---

## 4.3. Electromagnetismo

### P1 — “No hay potencial magnético / energía potencial magnética”

La lección `06_El_campo_magnético_un_campo_sin_fuentes` niega de forma global la existencia de potencial magnético y energía potencial magnética.

Para el nivel PAU puede ser útil explicar que **no hay un potencial escalar de posición análogo al potencial eléctrico que permita resolver la fuerza de Lorentz sobre una carga puntual móvil**. Pero la frase global es falsa:

- existe el **potencial vector magnético A**;
- un dipolo magnético tiene energía potencial U = -μ·B;
- en regiones sin corriente puede introducirse un potencial escalar magnético bajo ciertas condiciones.

**Recomendación:** limitar la afirmación al modelo y a la herramienta escalar que no se utiliza en ese bloque.

### P1 — Dirección de la polarización dieléctrica

En varias piezas se dice que un dieléctrico “se polariza siempre en sentido contrario al campo aplicado”. Eso confunde dos cosas:

- el vector polarización P de un dieléctrico lineal ordinario se alinea con E;
- las cargas ligadas creadas por la polarización pueden producir un campo que se opone parcialmente al campo externo en geometrías habituales.

**Corrección:** explicar la alineación del dipolo/P y, por separado, el campo de despolarización.

### P2 — Solenoide “uniforme en todo el interior”

La misma lección incluye una fórmula exacta para un solenoide finito y números que muestran variación pequeña, pero después afirma uniformidad en **todo** el interior. La expresión B=μnI es una aproximación excelente para un solenoide largo y lejos de los extremos; no es exacta para todo el interior de uno finito.

**Recomendación:** “aproximadamente uniforme en la región interior, salvo efectos de borde”.

### P0 ya citado — Inducción por cambio de flujo, no por movimiento necesariamente

Corregir globalmente objectives, theory, flashcards, MCQ y summary para que todos hereden el mismo criterio dΦ/dt.

---

## 4.4. Ondas y sonido

### P2 — Intensidad y amplitud

“I ↔ amplitud” es demasiado vago. En una onda lineal con las demás condiciones fijas, la intensidad es proporcional al **cuadrado de la amplitud**.

### P2 — “Los decibelios no se suman”

Lo correcto es: los **niveles en dB no se suman aritméticamente**; se suman intensidades/potencias y después se transforma logarítmicamente.

### P2 — Onda estacionaria y energía

La explicación de que no hay transporte neto porque “el nodo no se mueve/no puede hacer trabajo al vecino” es débil. La explicación más transferible es que una onda estacionaria ideal es superposición de dos ondas viajeras iguales y opuestas cuyos flujos medios de energía se cancelan.

### P2 — Tubos abiertos/cerrados

Conviene especificar siempre si se está hablando de nodos/antinodos de **desplazamiento** o de **presión**, porque se intercambian.

---

## 4.5. Óptica

Varias frases son correctas dentro de la óptica geométrica escolar pero excesivamente absolutas:

- n ≥ 1 “siempre”;
- si los rayos no convergen en un punto “no hay imagen”; en realidad puede haber una imagen borrosa/PSF extendida;
- en reflexión total interna “toda la luz vuelve” como idealización de interfaz perfecta.

No son prioridades P0, pero deben recibir etiqueta **modelo del curso / interfaz ideal / medios ordinarios**.

---

## 4.6. Relatividad

### P1 — Motivación incorrecta de relatividad general

La lección afirma: todos los cuerpos sienten gravedad → todos aceleran → no existe ningún sistema rigurosamente inercial → SR solo sirve a una situación inexistente.

Eso no es una buena formulación. La relatividad especial puede describir observadores acelerados, y en GR existen marcos **localmente inerciales**. La necesidad de GR es que SR no contiene una teoría de la gravitación como geometría dinámica del espacio-tiempo y que el principio de equivalencia conduce a curvatura y efectos de marea.

### P2 — Principio de equivalencia

Debe aparecer “**localmente**” desde el primer enunciado. En una región extensa, los efectos de marea distinguen un campo gravitatorio real de una aceleración uniforme.

### P2 — Tiempo propio

Definirlo con dos eventos sobre la misma línea de universo y un reloj comóvil es más preciso que hablar de “un evento en reposo”.

---

## 4.7. Física nuclear y cuántica

### P1 — Pico Fe/Ni

El material afirma que el máximo de energía de enlace por nucleón está exactamente en Fe-56. Para un curso escolar se entiende por qué se usa hierro como referencia, pero si se quiere corrección científica: el máximo está en la región hierro-níquel y **Ni-62** es la referencia habitual para el mayor E/A; Fe-56 queda muy cerca y es especialmente importante en nucleosíntesis.

### P1 — Umbral de estabilidad Z

La lección dice que Pb-208 es el último “estrictamente estable” y reconoce que Bi-209 es radiactivo extremadamente longevo, pero la regla práctica se formula como “no hay estable si Z>83”. Si se habla de estabilidad estricta, el corte debe tratar correctamente el caso Z=83.

### P2 — Producción de pares

2mc² es el umbral ideal de energía de masa. Si se necesita un núcleo para conservar momento, el umbral físico es ligeramente superior por recoil. Basta una nota “en este nivel se desprecia el retroceso del núcleo”.

### P2 — de Broglie

La forma fundamental debe ser λ=h/p. λ=h/mv debe aparecer etiquetada como **aproximación no relativista**.

### P0 ya citado — criterio dimensional de incertidumbre

Es uno de los casos donde la corrección debe propagarse a todos los campos, no solo a theory.

---

# 5. SELECTIVIDAD QUÍMICA — Auditoría técnica

## 5.1. Ácido-base

### H2SO4: no es un “error puro”, sino un problema de consistencia de alcance

La revisión profunda cambia la clasificación inicial: el worked example de H2SO4 4,0×10^-3 M **sí dice** que duplicar [H3O+] es una aproximación del nivel PAU y hasta indica que, usando Ka2 ≈ 0,012, el pH realista sería ~2,18 frente al 2,10 de la aproximación completa.

Eso está bien pedagógicamente.

El problema es que otras flashcards/resúmenes vuelven a formular sin matiz “cada mol de H2SO4 da 2 mol de H3O+”.

**Corrección:** marcar sistemáticamente:

- para neutralización completa con base fuerte: 2 equivalentes por mol;
- para pH acuoso riguroso: primera disociación prácticamente completa + segunda con Ka2;
- para PAU, si el convenio del examen lo simplifica, etiqueta explícita “aproximación PAU”.

### P1 — “Ácido + base → sal + agua” como definición general

Funciona para hidróxidos/óxidos en los ejercicios estequiométricos típicos. No define toda reacción ácido-base de Brønsted; por ejemplo HCl + NH3 no genera agua.

**Recomendación:** enseñar transferencia de protón como concepto y “sal + agua” como caso frecuente de neutralización con OH-/óxidos.

### Punto de equivalencia

Evitar “moles de ácido = moles de base” salvo 1:1. La propia parte de equivalentes mejora esto; conviene que sea la formulación principal desde el principio: igualdad según coeficientes/eq de H+ y base.

---

## 5.2. Termoquímica

### P1 — Estado estándar: 1 atm vs 1 bar

El curso define condiciones estándar de termoquímica como 25 °C y 1 atm, con nota de que algunos textos usan 1 bar.

Para precisión moderna:

- presión estándar termodinámica: **1 bar**;
- 298,15 K es una temperatura de referencia muy habitual de las tablas, no parte universal de la definición de estado estándar.

Si por exigencia de PAU se mantiene 1 atm en determinados problemas, debe aparecer como **convención de ese enunciado**, no como definición universal.

### P2 — Qp=ΔH

Añadir que la igualdad requiere el marco habitual de sistema cerrado a presión constante con trabajo pV como único trabajo relevante.

### P2 — ΔH=ΔU+Δn_g RT

Debe indicar gases ideales / condiciones del modelo.

### P2 — T=ΔH/ΔS como “temperatura umbral”

Es una aproximación si se toman ΔH y ΔS constantes con T. Para un nivel de Bachillerato está bien usarla, pero hay que marcar la hipótesis.

---

## 5.3. Equilibrio

### P1 — K = k+/k- derivado de velocidades

Solo es directo en el ejemplo de una reacción reversible **elemental** con las leyes de velocidad mostradas. No debe parecer la derivación general de cualquier K de equilibrio.

### P2 — Unidades de Kc

La formulación escolar con concentraciones puede asociar “unidades formales”, pero termodinámicamente K se define con actividades y es adimensional. Una nota breve evita una futura contradicción universitaria.

---

## 5.4. Orgánica

### P1 — condición de cis/trans de alquenos extendida a ciclos

Separar:

- E/Z en dobles enlaces: cada carbono sp² debe tener dos sustituyentes distintos;
- cis/trans en anillos: relación espacial respecto al plano/estructura del ciclo.

### P2 — enantiómeros “mismas propiedades salvo rotación óptica”

Añadir “en un entorno achiral”. En sistemas/reagentes/enzimas quirales pueden comportarse de forma distinta.

### P2 — halogenación “producto único”

Puede haber un único producto constitucional pero varios estereoisómeros. Si estereoquímica está fuera del ejercicio, decirlo.

### P2 — CCl4

Como referencia histórica de solvente está bien, pero no debería parecer una recomendación experimental actual. Mejor “solvente inerte no nucleófilo” o una nota de seguridad/histórica.

---

## 5.5. Enlace y estructura

- “Orbital = región de probabilidad” es una simplificación. Más correcto: el orbital es una función de onda; |ψ|² da densidad de probabilidad.
- “El puente de hidrógeno es la interacción intermolecular más intensa” debe ser tendencia en especies comparables, no universal ante moléculas grandes/polarizables.
- La regla de Madelung es una guía útil, no el orden exacto sin excepciones salvo Cr/Cu.

---

## 5.6. Error numérico confirmado de redondeo

**Ruta:** `selectividad_quimica__U09_Competencia / 04_Resolución... / worked_examples[0]/solution`.

Se muestra 27,6 g consumidos y después:

30,0 - 27,6 = 2,44 g.

2,44 corresponde a conservar cifras internas (~27,56), pero no a restar los números impresos.

**Corrección correcta:** o mostrar 27,56 y después 2,44, o mostrar 27,6 y dar 2,4. Añadir regla “redondear al final”.

---

# 6. SELECTIVIDAD MATEMÁTICAS — Auditoría técnica

## 6.1. Derivadas: punto de inflexión

En Matemáticas y CCSS aparece f''(x0)=0 como condición necesaria de punto de inflexión.

La definición segura es **cambio de concavidad**. Si f'' existe y es continua en la situación típica, f''(x0)=0 puede ser un candidato; pero una inflexión puede existir con f'' no definida en el punto.

**Recomendación de examen:**

1. localizar candidatos donde f''=0 o no exista;
2. comprobar cambio de signo de f''/concavidad.

---

## 6.2. L'Hôpital

La versión “si 0/0 o ∞/∞, deriva numerador y denominador” necesita un recuadro de hipótesis:

- diferenciabilidad en un entorno perforado;
- g' no nula donde corresponda;
- forma indeterminada real;
- existencia apropiada del límite de f'/g'.

No hace falta convertirlo en análisis universitario, pero sí evitar que la receta parezca una identidad algebraica.

---

## 6.3. Tangente vertical

Si se escribe f'(a)=±∞ como si fuera una derivada ordinaria, se contradice con otra parte que correctamente dice que en una tangente vertical no existe derivada finita. Mejor hablar de **pendiente infinita/límite de la derivada**, no de derivada real igual a infinito.

---

## 6.4. Probabilidad

### No equiprobable ≠ “usar frecuencias” necesariamente

Las frecuencias relativas son una forma empírica de estimar probabilidades; también puede existir un modelo no equiprobable conocido a priori.

### Con reemplazamiento ≠ independencia por definición

En el modelo estándar de urna con extracciones idénticas y reemplazo, sí. Como afirmación general, la independencia es una propiedad del modelo conjunto, no una consecuencia semántica de la palabra “reemplazo”.

---

## 6.5. Matrices y grafos

Para una matriz de adyacencia A, (A^k)_ij cuenta **walks/recorridos** de longitud k, donde se pueden repetir vértices/aristas. Llamarlos “paths/caminos” sin matiz puede ser falso si el alumno interpreta caminos simples.

---

# 7. SELECTIVIDAD MATEMÁTICAS CCSS — Auditoría técnica

Además de los problemas compartidos de derivadas/probabilidad:

## P1 — Representatividad muestral

La selección aleatoria reduce sesgo de selección y permite inferencia probabilística, pero **no garantiza** que una muestra concreta sea representativa. Existen además errores de marco, no respuesta, medición, etc.

Evitar la dicotomía “aleatoriedad decide representatividad; tamaño decide precisión”. Es demasiado limpia para ser correcta.

## P2 — Regla n≥30 para TCL

Debe etiquetarse como heurística. Con colas pesadas o gran asimetría puede requerirse n mucho mayor; si la población es normal, la media es normal para cualquier n.

## P2 — Suma ~ N(nμ, σ√n)

Es exacta si los sumandos son normales independientes; en otro caso es aproximada bajo TCL y sus condiciones.

## P2 — “Eficiencia”

Cantidades como n/σ² o n/[p(1-p)] encajan mejor como **precisión/información** en el contexto dado, no como definición general de eficiencia de un estimador.

## P2 — “Región de aceptación”

Preferir “región de no rechazo”. No rechazar H0 no equivale a probarla/aceptarla como verdadera.

---

# 8. ESO MATEMÁTICAS — Auditoría técnica y curricular

## P1 — El catálogo mezcla ESO con Bachillerato/avanzado

Dentro de `eso_matematicas` aparecen, entre otros:

- números complejos;
- cónicas;
- límites;
- derivadas;
- aproximación binomial-normal;
- trigonometría y ecuaciones avanzadas;
- sistemas de 3 variables/Gauss en extensión.

No es que esos contenidos sean malos. El problema es **taxonómico y de progresión**: un alumno que entra en “ESO Matemáticas” no debería recibirlos como una secuencia homogénea del mismo nivel.

El currículo estatal de ESO enfatiza números reales, funciones y tasas de cambio a nivel gráfico, relaciones lineales/cuadráticas/proporcionalidad inversa, álgebra y estadística de la etapa; límite/derivada aparecen ya explícitamente en Bachillerato. Por tanto, el producto debería separar **ESO Core**, **Extensión/altas capacidades** y **Bachillerato**.

## P1 — Función inversa sin inyectividad

El algoritmo “intercambia x e y y despeja” debe ir después de comprobar que la función es one-to-one/injectiva en el dominio o de restringir ese dominio.

## P2 — Cuartiles

El método “mediana de las mitades excluyendo el central” es una convención entre varias. Debe decirse qué convención usa el examen/calculadora del curso.

## P2 — R²

0≤R²≤1 es la situación estándar para OLS con intercepto. Como regla de regresión escolar está bien si se etiqueta ese contexto; sin intercepto puede ser negativo.

## P0 ya citado — MCQ de residuo imposible

Debe corregirse antes de publicar.

---

# 9. ESO FÍSICA Y QUÍMICA / FQ COMPLETO

## 9.1. Versión standalone de ESO

Además del P0 de cambios de estado:

- resúmenes muy genéricos y repetitivos;
- campos claramente truncados, por ejemplo claves como “Una curva T vs.” o “1.”;
- afirmaciones del tipo “meseta perfectamente horizontal” deberían ser “modelo ideal / aproximadamente horizontal en experimento”.

## 9.2. FQ completo

La versión es, en general, más madura que la standalone. Aun así:

- “enlace polar si 0,4<Δχ<1,7” debe ser **regla orientativa**, no frontera física nítida;
- “transferencia completa metal→no metal” es un modelo introductorio para enlace iónico, no su mecanismo/definición universal;
- “más pares compartidos → enlace siempre más corto y fuerte” es tendencia útil al comparar el mismo par de átomos/orden de enlace, no ley entre especies arbitrarias;
- “eficiencia real siempre 0<η<1” debería admitir η=0 en el límite conceptual;
- “rozamiento siempre resta energía” necesita el mismo alcance que en Física de Selectividad.

### Capa de resumen

Se detectan decenas de frases genéricas del tipo “se entiende relacionando el modelo científico…” o “para aplicar… definir sistema…”. No son errores técnicos, pero desperdician el lugar donde debería consolidarse el concepto específico de la lección.

---

# 10. GCSE/IGCSE PHYSICS

## P1 — Definición de onda exige un medio

**Ruta:** `U06_Waves_Light_and_Sound / 01_Wave_quantities_and_types`.

El resumen y un MCQ definen la onda como algo que transfiere energía “through a medium”. Eso excluye ondas electromagnéticas, que el mismo curso enseña después.

**Definición recomendada:** una onda es una perturbación/oscilación que transporta energía (e información) sin transporte neto de materia; **las ondas mecánicas necesitan medio y las electromagnéticas no**.

## P1 — Speed-time frente a velocity-time

Si se enseña aceleración firmada/direccional, el gradiente correcto es el de una gráfica **velocity-time**. En una speed-time se representa cambio de rapidez; solo coincide bajo condiciones de movimiento sin inversión de dirección.

## P1 — Balance de energía

“Total energy leaving a system always equals total that entered” omite energía almacenada.

Forma general escolar más robusta:

**energy in = useful out + wasted out + change in stored energy**.

## P2 — Órbitas

“Gravity acts perpendicular to the planet’s motion, changing direction but not speed” debe decir **circular orbit**. En una órbita elíptica la rapidez cambia.

## P2 — Amplitud y longitud de onda

Definirlas con “vertical” y “horizontal” depende del dibujo transversal. Una onda longitudinal obliga a usar definiciones físicas: máxima desviación respecto al equilibrio y distancia entre puntos consecutivos en la misma fase.

## P2 — “Denser medium” en refracción

Usar “optically denser / higher refractive index”, no densidad material genérica.

## P2 — Radio/microondas “no dañan”

Mejor: son no ionizantes, pero a suficiente intensidad pueden producir calentamiento y daño térmico.

## P2 — Transformador AC/DC

“Funciona con AC, no DC” es una buena regla de examen si se añade: lo que necesita es **flujo cambiante**. DC estacionaria no mantiene fem; un transitorio/pulsos sí cambian el flujo.

---

# 11. GCSE/IGCSE CHEMISTRY

## P1 — Definición de base demasiado estrecha

En `U07` aparece “a base is any metal oxide or metal hydroxide”. Eso describe una familia importante del syllabus, no la definición general. NH3 es el contraejemplo escolar más evidente.

**Recomendación:** “common bases in this course include metal oxides and metal hydroxides”; después usar la definición ácido-base adecuada al nivel.

## P2 — pH 0–14

Correcto como rango pedagógico típico para disoluciones acuosas diluidas cercanas a temperatura ambiente; no como límite físico universal.

## P2 — Neutralisation always salt + water

Mismo problema de alcance que en Selectividad: válido para ácido + hidróxido/óxido; no todas las bases generan agua.

## P2 — Exo/endo decidido solo por ΔT observado

En el calorímetro escolar, el signo de ΔT es evidencia bajo condiciones controladas. La definición debe hacerse por transferencia de energía/entalpía; pérdidas al entorno pueden distorsionar el dato experimental.

En conjunto, GCSE Chemistry está razonablemente bien y requiere más **calibración de lenguaje** que reconstrucción.

---

# 12. GCSE MATHEMATICS

## P1 — “A difference is always larger minus smaller and never negative”

**Ruta:** `U01_Number / 03_Ordering_and_the_Four_Operations`.

Es incorrecto como definición de subtraction/difference. a-b puede ser negativo. Si se quiere “difference between” como distancia numérica, debe escribirse **absolute difference |a-b|**.

## P1 — Inversa sin one-to-one

Mismo problema que ESO: el procedimiento de intercambiar x/y no garantiza que la inversa sea una función si la original no es one-to-one en el dominio.

## P1 — “Random” = “independent trials”

**Ruta:** `U08_Probability / 02_Relative_and_Expected_Frequency`.

Hay procesos aleatorios dependientes. Muestreo sin reemplazo es el ejemplo que el propio curso terminará usando.

Separar:

- random/unpredictable under a probability model;
- independent = knowing one outcome does not change probability distribution of the other.

## P1 — “A maximum or minimum always has zero gradient”

Solo para extremos **interiores y diferenciables**. Un extremo de frontera o un punto angular no tiene por qué cumplirlo.

## P2 — Interpolation is reliable

Reformular a “interpolation is generally safer than extrapolation, provided the relationship remains appropriate”.

## P2 — Outliers

No se debe enseñar “exclude the outlier” como protocolo automático. Primero se investiga: error de medición, subpoblación real, observación legítima, etc.

## P2 — Fractional equations

Al “clear denominators”, el problema no es que multiplicar cree mágicamente raíces extra: el riesgo aparece si se olvidan las **restricciones del dominio original**. Ponerlas antes del álgebra mejora mucho la explicación.

---

# 13. Integridad del JSON / QA

Los controles estructurales detectaron **294 incidencias**:

| Severidad | Tipo | Cantidad |
|---|---|---:|
| Alta | `very_long_lesson` | 7 |
| Alta | `content_overload` | 2 |
| Media | `content_overload` | 5 |
| Media | `correct_option_marked_wrong` | 2 |
| Media | `dangling_objective_ref` | 10 |
| Media | `duplicate_id_within_lesson` | 7 |
| Media | `no_worked_examples` | 31 |
| Media | `no_practice` | 2 |
| Baja | `wrong_option_no_explanation` | 228 |

## 13.1. IDs duplicados

`eso_matematicas__mat_ecuaciones / 05_Ecuaciones_exponenciales_y_logarítmicas_básicas` contiene 7 IDs duplicados, entre ellos elementos `TH`, `WE` y `EX`.

**Riesgo:** claves de UI, tracking, persistencia, enlaces internos y analítica.

## 13.2. Objetivos inexistentes

`selectividad_matematicas_ccss__mat_representacion` tiene 10 referencias colgantes en las lecciones 08/09 hacia objetivos como `LO-09-1` o `LO-11-1` que no están definidos.

## 13.3. Feedback incompleto

228 distractores incorrectos no tienen explicación `why_wrong`. No es necesario rellenar cada distractor trivial, pero para una plataforma pedagógica conviene exigir explicación cuando el distractor corresponde a un error conceptual típico.

## 13.4. Lecciones sin worked examples

31 flags corresponden en gran parte a Exercise Banks. Puede que exista práctica bajo otra estructura, pero el esquema deja de ser uniforme. La UI debería distinguir `lesson_type=exercise_bank` en lugar de hacer pasar un banco por una lección ordinaria.

---

# 14. Carga cognitiva y longitud

La carga real no coincide bien con las duraciones declaradas.

### Mediana aproximada de palabras por hora declarada

| Familia | Palabras/hora mediana |
|---|---:|
| ESO Física y Química | ~857 |
| FQ completo | ~2.250 |
| GCSE Physics | ~3.252 |
| GCSE Chemistry | ~3.339 |
| Selectividad Matemáticas | ~3.487 |
| Selectividad Matemáticas CCSS | ~3.856 |
| ESO Matemáticas | ~4.681 |
| GCSE Mathematics | ~5.509 |
| Selectividad Física | ~6.862 |

En contenido matemático/físico, “palabras por hora” ya es una medida generosa porque el alumno necesita **detenerse, dibujar, calcular y resolver**.

## Casos extremos

- GCSE Maths `U02 / Exercise Bank`: **~92.935 palabras** para 2,5 h.
- GCSE Maths `U01 / Exercise Bank`: **~66.209 palabras** para 2,5 h.
- Selectividad Física tiene varias lecciones entre **13.000 y 20.000 palabras**.
- `electromagnetismo / 05_El_potencial_eléctrico...`: ~20.190 palabras.
- `ondas / 11_Ondas_estacionarias...`: ~18.306 palabras.
- `campo_gravitatorio / 02_La_ley_de_gravitación...`: ~18.070 palabras.

### Diagnóstico pedagógico

Los Exercise Banks deberían ser **repositorios**, no lecciones lineales. Y las macro-lecciones de Selectividad Física deberían dividirse en:

1. concepto/intución;
2. formalización;
3. cálculo prototipo;
4. errores frecuentes;
5. problema PAU;
6. práctica independiente.

Así la web puede medir progreso real por micro-lección y no por “haber abierto” un bloque de 20.000 palabras.

---

# 15. Problema transversal: reglas absolutas

Este es el patrón más importante de todo el corpus.

Hay explicaciones de alta calidad, pero con frecuencia terminan comprimidas en una flashcard/resumen del tipo:

- “siempre…”
- “nunca…”
- “solo…”
- “cualquier…”

cuando la afirmación depende de un modelo.

Ejemplos auditados:

- rozamiento siempre negativo;
- inducción solo con movimiento;
- solenoide uniforme en todo el interior;
- dieléctrico polarizado contra E;
- onda necesita medio;
- random implica independencia;
- máximo/mínimo siempre tiene pendiente cero;
- H2SO4 siempre aporta cuantitativamente 2 H+ para pH;
- pH siempre entre 0 y 14;
- neutralización siempre sal+agua;
- f''=0 como requisito de inflexión;
- n≥30 como frontera universal del TCL.

## Solución de diseño recomendada

Añadir a cada afirmación/formula una etiqueta de alcance que pueda heredar la UI:

- **EXACTO** — definición/teorema bajo sus hipótesis explícitas.
- **MODELO DEL CURSO** — idealización deliberada de Bachillerato/GCSE.
- **APROXIMACIÓN** — numéricamente útil en un régimen.
- **HEURÍSTICA** — regla práctica, no garantía.
- **CONVENCIÓN DE EXAMEN** — se usa porque el examen lo espera aunque el modelo completo sea más rico.

Esto resolvería una gran parte de los fallos sin hacer las lecciones más difíciles.

---

# 16. Orden pedagógico recomendado

La estructura JSON ya contiene casi todas las piezas necesarias, pero el orden no siempre las explota bien.

Para cada micro-lección recomiendo esta secuencia:

1. **Prerequisite check** — 1–3 preguntas breves.
2. **Intuición / fenómeno / problema inicial**.
3. **Definición o modelo** con condiciones de validez.
4. **Ejemplo resuelto** completamente guiado.
5. **Ejemplo parcialmente guiado** con retirada progresiva de ayudas.
6. **Práctica independiente** corta.
7. **Transfer/exam question**.
8. **Misconception check**.
9. **Resumen específico de la lección**, no boilerplate.
10. **Spaced retrieval** posterior en otro módulo/banco.

### Principio clave

La **condición de validez debe aparecer antes de la regla**, no escondida después en una caveat. Si el alumno ve primero “siempre X” y después “bueno, salvo…”, la memoria de recuperación suele quedarse con X.

---

# 17. Auditoría del summary layer

El resumen debe ser el componente más fiable porque se usa para repasar. Aquí se detectan tres problemas:

1. **Boilerplate** repetido en ESO/FQ.
2. **Reglas demasiado absolutas** que pierden matices presentes en teoría.
3. **Campos truncados** en la versión standalone de ESO FQ.

### Regla de generación recomendada

El summary no debería generarse independientemente de la teoría. Debería construirse a partir de una estructura normalizada:

- `core_claims[]`
- `assumptions[]`
- `formulae[]`
- `common_mistakes[]`
- `exam_conventions[]`

y renderizarse desde esos datos. Así una condición no puede desaparecer al comprimir la lección.

---

# 18. Tests automáticos que deberían entrar en CI

## 18.1. Estructura

- IDs únicos por curso/unidad/lección.
- Todos los `objective_ids` existen.
- Todos los `concept_ids` existen.
- No hay claves React repetidas.
- No hay campos truncados por debajo de una longitud razonable si no están marcados como intencionales.

## 18.2. MCQ

- Una opción correcta exactamente, salvo multiselect.
- Opción correcta nunca tiene `why_wrong`.
- Distractor no puede tener `why_correct`.
- `correct` debe apuntar a una key existente.
- Si el MCQ es numérico, el valor de la explicación debe coincidir con la opción correcta.
- Si se dispone de expresión, recalcular con un evaluador simbólico/numérico.

## 18.3. Matemáticas/cálculo

- Escanear cadenas `a=b=c` y recomputar igualdad cuando sea parseable.
- Mantener cifras de guarda y redondear solo al final.
- En notación científica, usar `\frac{...}{...}` o paréntesis; evitar expresiones ambiguas del tipo `1.0·10^-4/5.0·10^-7`.

## 18.4. Semántica de alto riesgo

Crear lint que no “prohíba”, pero marque para revisión humana frases con:

- always / never / only / all / any;
- siempre / nunca / solo / cualquier / todos;
- “por definición”;
- “exactamente”;
- “garantiza”.

El revisor debe asignar una de las etiquetas EXACTO / MODELO / APROXIMACIÓN / HEURÍSTICA / EXAMEN.

## 18.5. Versionado

- `content_version` por lección.
- hash de fuente.
- ninguna duplicación silenciosa del mismo `canonical_lesson_id`.
- si una variante hereda de otra, almacenar solo delta/configuración, no copia completa.

---

# 19. Priorización de correcciones

## Fase 1 — Antes de cualquier publicación

Corregir los P0:

1. MCQ probabilidad Selectividad Matemáticas.
2. MCQ regresión ESO.
3. Contradicción de cambios de estado GCSE Physics.
4. Contradicción de cambios de estado ESO FQ.
5. Inducción electromagnética.
6. Criterio dimensional en cuántica.
7. Fuente duplicada ESO FQ/FQ completo.
8. `why_wrong` en respuestas correctas.

## Fase 2 — Conceptos de alto impacto

- ondas y medio;
- “difference” GCSE;
- inversas e inyectividad;
- random ≠ independent;
- inflexión y L'Hôpital;
- potencial/energía magnética;
- polarización dieléctrica;
- motivación de GR;
- Fe/Ni;
- ácido-base y estado estándar;
- base en GCSE Chemistry.

## Fase 3 — Pedagogía/arquitectura

- fragmentar macro-lecciones;
- convertir Exercise Banks en bancos consultables;
- separar ESO Core / extensión / Bachillerato;
- regenerar summaries específicos;
- añadir etiquetas de alcance;
- normalizar lesson types.

## Fase 4 — Mejora fina

- completar `why_wrong` relevantes;
- terminología estadística;
- notas de seguridad/solventes;
- convenciones de cuartiles;
- matices de óptica/ondas.

---

# 20. Valoración por familia

| Familia | Corrección técnica | Pedagogía/orden | Estado recomendado |
|---|---|---|---|
| Selectividad Física | **Necesita correcciones importantes** | Muy rica pero excesivamente densa | No publicar completa antes de P0/P1 |
| Selectividad Química | Buena base, varios alcances/hipótesis | Bien estructurada en general | Publicable tras revisión P1 |
| Selectividad Matemáticas | Buena base con algunos errores claros | Buen andamiaje | Corregir P0/P1 |
| Selectividad Matemáticas CCSS | Correcta en núcleo, matices en inferencia | Buena, pero mejorar rigor estadístico | Corregir P1/P2 |
| ESO Matemáticas | Matemáticamente rica | **Nivel mal segmentado** | Reestructurar catálogo antes de vender como ESO |
| ESO Física y Química | Tiene contradicción y versión antigua | Demasiado genérica | Sustituir/derivar de fuente canónica |
| FQ completo | La versión más madura de FQ | Buena base | Corregir QA y simplificaciones |
| GCSE Physics | Varias contradicciones conceptuales puntuales | En general didáctica | Corregir P0/P1 |
| GCSE Chemistry | Bastante sólida | Clara | Ajustes de alcance/terminología |
| GCSE Mathematics | Muy completa | Bancos desmesurados; varios absolutos | Corregir P1 y fragmentar bancos |

---

# 21. Qué conservaría

No conviene que la corrección destruya lo que ya funciona. Mantendría:

- estructura de misconceptions;
- worked examples con razonamiento;
- preguntas de transferencia;
- integración de preguntas de examen;
- flashcards, **si se generan desde claims ya validados**;
- comparaciones/analogías cuando están etiquetadas como modelo;
- ejercicios de “caza del error”;
- explicaciones de por qué un distractor falla;
- separación `core`/extension cuando existe.

El objetivo no debería ser “hacer el material más académico” a costa de claridad. Debería ser **conservar la claridad y eliminar las falsedades creadas por simplificar demasiado**.

---

# 22. Conclusión

El corpus es recuperable y tiene valor. La auditoría no muestra un conjunto de cursos incoherentes o inservibles; muestra un sistema de generación que necesita **una capa fuerte de validación canónica**.

El patrón dominante es:

> explicación extensa bastante buena → resumen simplificado → regla absoluta → MCQ/flashcard que consolida la regla absoluta.

Por eso la solución no es revisar únicamente los PDFs o únicamente la teoría. Hay que validar **todas las representaciones de un mismo claim**: teoría, worked example, MCQ, flashcard, misconception y summary.

La prioridad técnica es crear un **modelo de conocimiento canónico por lección** del que se deriven esas representaciones. La prioridad pedagógica es separar **verdad exacta**, **modelo**, **aproximación**, **heurística** y **convención de examen**.

Con esos dos cambios, la mayor parte del contenido existente puede reutilizarse sin perder el estilo didáctico que ya tiene.

---

## Apéndices generados por la auditoría

1. `lesson_inventory.csv` — inventario de las 873 lecciones, conteo de palabras y densidad estimada.
2. `structural_issues.csv` — 294 incidencias de estructura/pedagogía/schema.
3. `equality_mismatches.csv` — **candidatos** detectados por el escáner numérico. Importante: este fichero contiene falsos positivos (dimensiones de matrices, coordenadas, ejemplos deliberadamente erróneos, etc.); no debe interpretarse como lista de errores confirmados sin revisión humana.

