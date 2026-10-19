# AUDITORÍA COMPLETA DE REESTRUCTURACIÓN — CURSOS

Este documento consolida la especificación maestra y los diez informes por curso. Para ejecución automatizada se recomienda usar los ficheros separados y el ledger machine-readable.

---

# Especificación maestra de reestructuración de los cursos

**Objetivo:** convertir el corpus actual en un sistema de aprendizaje utilizable por un alumno con poca base, un alumno medio y un alumno que busca excelencia **sin mantener tres cursos independientes**.

**Uso:** este documento es normativo. Los documentos de `/cursos` añaden reglas específicas por familia. Si una regla de un curso contradice una regla maestra, prevalece la regla específica del curso únicamente para ese curso.

---

## 1. Resultado que debe producir el agente

El agente NO debe limitarse a corregir erratas ni a reordenar párrafos. Debe transformar el material en una arquitectura con:

1. una **fuente de conocimiento canónica** por lección;
2. varias rutas pedagógicas sobre el mismo conocimiento;
3. prerrequisitos navegables;
4. práctica graduada;
5. evaluación de dominio;
6. modo examen separado del aprendizaje guiado;
7. reglas explícitas de alcance para modelos, aproximaciones y convenciones;
8. QA automático de estructura, cálculos y coherencia de respuestas.

La meta no es "hacer el material más largo". La meta es que cada alumno vea **lo que necesita, en el momento en que lo necesita**.

---

## 2. Dimensiones que nunca deben mezclarse

### 2.1. Nivel curricular / syllabus
Indica si el contenido pertenece oficialmente o funcionalmente al alcance del curso: ESO, Bachillerato, PAU, Cambridge Core, Cambridge Extended, etc.

### 2.2. Profundidad pedagógica
Indica cuánto apoyo/profundidad recibe un alumno para **el mismo objetivo curricular**:

- `FOUNDATION_SUPPORT`: recuperación de prerrequisitos.
- `CORE`: mínimo imprescindible de la lección.
- `STANDARD`: dominio esperado para resolver ejercicios normales/examen.
- `ADVANCED`: comprensión profunda, condiciones, contraejemplos y problemas difíciles.

**Prohibición:** no mapear `Cambridge Extended == ADVANCED`. Un alumno con poca base puede necesitar estudiar un objetivo Extended "desde cero".

### 2.3. Dificultad del ejercicio
Escala 1–5. No equivale a profundidad conceptual.

### 2.4. Nivel cognitivo
`remember`, `understand`, `apply`, `analyse`, `evaluate/create` cuando proceda.

---

## 3. Arquitectura de navegación obligatoria

```text
COURSE
├── 00 Diagnostic + onboarding
├── Foundations (solo cuando el diagnóstico lo requiera)
├── Module 01
│   ├── Unit diagnostic
│   ├── Atomic lesson A
│   ├── Atomic lesson B
│   ├── Atomic lesson C
│   ├── Checkpoint
│   └── Module exam / mixed practice
├── Module 02
│   └── ...
├── Cumulative review
├── Exam mode
└── Mastery dashboard
```

### Decisión del alumno al entrar en una unidad
La UI puede ofrecer cuatro rutas, todas sobre las mismas lecciones canónicas:

- **Aprender desde cero**: prerequisite checks + intuición + Core + ejemplos guiados + práctica L1–L3.
- **Curso normal**: Core + Standard + práctica L2–L4 + preguntas tipo examen.
- **Buscar excelencia**: repaso Core comprimido + Standard + Advanced + L4–L5 + challenge/transfer.
- **Repaso rápido**: diagnóstico corto; si se supera, ir a summary + práctica mixta/examen.

El alumno puede cambiar de ruta por unidad. Nunca clasificar permanentemente a una persona como "baja/media/alta".

---

## 4. Anatomía obligatoria de una lección atómica

Orden recomendado:

1. **Prerequisite check**: 1–3 ítems, máximo 3–5 min.
2. **Problema/fenómeno de entrada**: por qué existe el concepto.
3. **Intuición**: representación verbal/gráfica/experimental antes de formalismo cuando sea posible.
4. **Claim/definición canónica** con condiciones visibles.
5. **Ejemplo resuelto completo**.
6. **Ejemplo desvanecido (faded)**: parte de los pasos los completa el alumno.
7. **Micro-check** inmediato.
8. **Standard layer**: variaciones, conexiones y selección de método.
9. **Práctica independiente** corta y graduada.
10. **Advanced layer**: límites, contraejemplos, derivación/demostración útil, situaciones nuevas.
11. **Pregunta de transferencia/examen**.
12. **Misconception check**.
13. **Summary** derivado de claims, nunca escrito como una segunda teoría independiente.

### Duración objetivo
- Core: 15–25 min.
- Standard completo: 25–40 min.
- Advanced añadido: +15–25 min.
- Si una lección supera ~45 min de estudio real antes de práctica, dividirla.

No usar número de palabras como única métrica: matemáticas/física necesitan tiempo de cálculo, dibujo y pausa.

---

## 5. Modelo de conocimiento canónico

Toda afirmación importante debe existir una sola vez como `claim` y llevar `epistemic_type`:

- `EXACT`: definición/teorema bajo condiciones explícitas.
- `MODEL`: idealización deliberada del curso.
- `APPROXIMATION`: útil en un régimen cuantitativo concreto.
- `HEURISTIC`: regla práctica, no garantía.
- `EXAM_CONVENTION`: convención esperada por un examen/perfil concreto.
- `SPECIAL_CASE`: caso particular que no debe generalizarse.

Las representaciones visibles (teoría, flashcard, MCQ, summary, hint) **deben renderizar o parafrasear ese claim**, no inventarlo de nuevo.

### Regla crítica
La condición de validez aparece **antes o junto a la regla**. Nunca enseñar primero un "siempre" y esconder la excepción al final.

---

## 6. Prerrequisitos como grafo

No usar solo "Lección 1 -> Lección 2". Cada lesson debe declarar `prerequisite_concept_ids`.

Cuando un alumno falla un checkpoint, el sistema debe diagnosticar la habilidad causante:

- contenido actual;
- álgebra/manipulación;
- unidades;
- lectura de gráfica;
- vocabulario científico;
- probabilidad previa;
- etc.

El enlace de recuperación debe apuntar a una **microlección Foundation**, no obligar a repetir un módulo entero.

---

## 7. Ejercicios: taxonomía obligatoria

Cada ejercicio debe tener, como mínimo:

- `skills[]`;
- `difficulty` 1–5;
- `conceptual_depth` 1–5;
- `cognitive_level`;
- `syllabus_scope/official_track` si aplica;
- `estimated_minutes`;
- `hints[]` graduados;
- solución completa;
- errores típicos asociados cuando existan.

### Escalera común
- **L1 — Reconocimiento/recuerdo**.
- **L2 — Aplicación directa de una técnica**.
- **L3 — Variación o combinación sencilla**.
- **L4 — Tipo examen / requiere elegir estrategia**.
- **L5 — Transfer/challenge**.

No presentar bancos de 100+ ejercicios como una "lección". Un Exercise Bank es `lesson_type=exercise_pool` y la UI selecciona subconjuntos según skills/dificultad.

---

## 8. Worked examples y retirada progresiva de ayudas

Para cada skill procedimental importante debe existir la secuencia:

1. ejemplo totalmente resuelto;
2. ejemplo con pasos parcialmente completados;
3. ejercicio independiente;
4. ejercicio de transferencia.

Un alumno con poca base consume los cuatro pasos. Un alumno avanzado puede saltar 1–2 tras diagnóstico.

---

## 9. Feedback

### MCQ
- Correct option: `why_correct` coherente; `why_wrong` vacío.
- Distractor conceptual: `why_wrong` explica **el error mental**, no solo "incorrecto".
- Distractor trivial de aritmética: feedback opcional, según política del curso.
- Pregunta numérica: resultado, opción y explanation deben salir de una solución canónica/calculada.

### Ejercicio abierto
Separar feedback en:
- error conceptual;
- error de método;
- error algebraico/aritmético;
- error de unidades/notación;
- error de interpretación.

---

## 10. Summary layer

El summary se genera exclusivamente desde:

- `core_claims[]`;
- `conditions[]`;
- `formulae[]`;
- `common_mistakes[]`;
- `exam_conventions[]`.

Debe contener:
- 3–7 ideas concretas de esa lección;
- fórmulas con condiciones;
- un error frecuente;
- criterio de "ya lo domino si...".

**Prohibido:** boilerplate genérico como idea principal, claims nuevos, matices eliminados o frases truncadas.

---

## 11. Diagnóstico y mastery

### Diagnóstico inicial del curso
No producir una etiqueta global. Producir un vector de skills.

### Diagnóstico por módulo
5–10 preguntas representativas. La recomendación de ruta puede ser:
- <40%: desde cero;
- 40–75%: estándar;
- >75%: repaso rápido/advanced.

Son umbrales iniciales configurables, no verdades psicométricas.

### Dominio
No basarlo solo en "completado". Una skill requiere evidencia repetida, preferiblemente en más de un momento y en más de un formato.

---

## 12. Repaso acumulativo

Insertar retrieval de contenidos previos en unidades posteriores. El curso debe poder generar repasos de 5–10 min a partir del grafo de skills. No hace falta obligar a un calendario fijo en el contenido; la plataforma puede programarlo.

---

## 13. Modo examen separado del modo aprendizaje

El contenido guiado puede tener hints y scaffolding. `Exam mode` no.

Exam mode debe incluir:
- sets por tema;
- sets mixtos;
- problemas de selección de estrategia;
- simulacros;
- corrección por criterio/mark scheme cuando exista;
- analítica de errores por skill.

Para PAU, almacenar `exam_profile` por comunidad/año si se pretende adaptar estilo, opcionalidad, calculadora o ponderaciones. El conocimiento canónico no debe depender de un único perfil regional.

---

## 14. QA/CI obligatorio

### Estructura
- IDs únicos.
- objective/concept references resuelven.
- canonical_lesson_id único por body canónico.
- variantes guardan delta/config, no copia silenciosa.
- campos obligatorios no truncados.

### MCQ
- exactamente una opción correcta salvo multiselect;
- correct option nunca tiene why_wrong;
- distractor nunca tiene why_correct;
- correct apunta a key existente;
- cálculo de explanation coincide con la opción.

### Cálculo
- recalcular expresiones numéricas parseables;
- validar igualdades encadenadas;
- cifras de guarda y redondeo final;
- unidades dimensionalmente consistentes cuando sea viable.

### Lint semántico
Marcar para revisión: `always`, `never`, `only`, `all`, `any`, `siempre`, `nunca`, `solo`, `cualquier`, `garantiza`, `exactamente`, `por definición`.
Cada flag debe resolverse asignando epistemic_type/conditions o justificando que es realmente exacto.

---

## 15. Flujo de ejecución del agente

### Fase A — congelar y mapear
1. No borrar el corpus original.
2. Generar inventario por course/unit/lesson.
3. Asignar `canonical_lesson_id` estable.
4. Identificar duplicados/variantes.

### Fase B — corregir P0/P1 antes de reestructurar
Aplicar `semantic_change_ledger.csv`. No mover contenido incorrecto a una estructura nueva.

### Fase C — normalizar conocimiento
Extraer claims, fórmulas, condiciones, misconceptions y exam conventions de cada lección.

### Fase D — atomizar
Dividir macro-lecciones. Convertir bancos en pools. Conservar trazabilidad `derived_from`.

### Fase E — construir rutas
Añadir Foundation/Core/Standard/Advanced/Quick review sin duplicar el claim canónico.

### Fase F — regenerar assessments y summaries
Especialmente aquellos que dependían de reglas absolutas corregidas.

### Fase G — QA
Ejecutar validadores, muestreos semánticos y revisión visual/web.

### Fase H — aceptación
Solo marcar una unidad `release_ready=true` si pasa todos los criterios de su documento de curso.

---

## 16. Definition of Done global

Un curso está listo cuando:

- 0 P0 abiertos;
- 0 P1 sin decisión explícita;
- 0 IDs/referencias rotas;
- 0 respuestas correctas con feedback de error;
- 0 lecciones lineales gigantes usadas como Exercise Bank;
- todo claim de alto riesgo tiene scope/conditions;
- cada unidad tiene diagnóstico, checkpoint y práctica mixta;
- cada skill importante tiene worked example + práctica independiente;
- el summary deriva de conocimiento canónico;
- un alumno puede recorrer una ruta desde cero, estándar, excelencia y repaso rápido sin cambiar de curso;
- la UI puede explicar por qué recomienda una recuperación concreta.


---

# Auditoría de reestructuración — Selectividad / PAU — Física

**Curso ID:** `selectividad_fisica`  
**Unidades actuales:** 8  
**Lecciones actuales:** 76  
**Palabras pedagógicas aproximadas:** 1,045,039  
**Mediana de palabras/hora declarada:** ~6,862  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `ondas` | 12 | 166.360 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `optica` | 11 | 149.374 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `nuclear` | 10 | 127.701 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mas` | 7 | 94.259 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `campo_gravitatorio` | 9 | 135.040 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `cuantica` | 6 | 85.328 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `relatividad` | 7 | 100.537 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `electromagnetismo` | 14 | 186.440 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Vectores, trigonometría, despeje algebraico, notación científica, unidades SI, lectura de gráficas y conservación de energía. Solo aparece cuando el diagnóstico detecta carencias.
2. **01 Campo gravitatorio** — Kepler -> gravitación -> campo/potencial -> energía -> órbitas/satélites -> problemas mixtos.
3. **02 Movimiento armónico simple** — Oscilación general -> MAS ideal -> x/v/a -> energía -> resolución de condiciones iniciales -> péndulo/muelle dentro del modelo.
4. **03 Ondas y sonido** — Concepto de onda -> magnitudes -> ecuación -> fase -> superposición/interferencia -> estacionarias -> sonido/dB.
5. **04 Electromagnetismo** — Coulomb/campo -> potencial/energía -> corriente/circuitos si están en alcance -> magnetismo -> fuerza de Lorentz -> flujo/Faraday-Lenz -> aplicaciones.
6. **05 Óptica** — Propagación -> índice/Snell -> TIR -> óptica geométrica -> lentes/espejos -> instrumentos/problemas.
7. **06 Relatividad** — Postulados SR -> simultaneidad -> dilatación/contracción -> transformaciones/energía si están en alcance -> equivalencia local/GR al nivel del curso.
8. **07 Física cuántica** — Planck/fotón -> fotoeléctrico -> Bohr/espectros -> de Broglie -> incertidumbre y límites del modelo.
9. **08 Física nuclear** — Núcleo -> energía de enlace -> estabilidad -> desintegración -> actividad/semivida -> reacciones/fisión/fusión.
10. **09 PAU integrada** — Problemas mixtos, selección de estrategia, simulacros y análisis de errores.


### Reglas pedagógicas específicas de Física PAU
- Cada ley/fórmula debe mostrar **sistema, hipótesis, signos, unidades y límite de validez**.
- Toda lección procedimental termina con al menos un problema en el que el alumno deba **elegir la ley**, no se le diga cuál usar.
- Diagramas de cuerpo libre, campos, rayos y ondas son parte del razonamiento, no decoración.
- La capa Advanced prioriza contraejemplos y cambio de modelo, no matemáticas universitarias gratuitas.
- Las derivaciones largas solo se mantienen si ayudan a reconstruir una fórmula o son examinables; si no, van a Advanced/"por qué funciona".


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `electromagnetismo / 12_El_flujo_magnético_y_qué_induce_corriente` | Inducción presentada como existente solo con movimiento relativo. | Reescribir objetivos, teoría, ejemplos, MCQ, flashcards y summary alrededor de dΦ_B/dt != 0. Presentar movimiento relativo como una de varias formas de variar el flujo. Incluir ejemplo de espira fija con B(t) o transformador. | Ninguna pieza afirma que el movimiento sea condición necesaria; todas las evaluaciones aceptan flujo variable sin movimiento. |
| P0 | `cuantica / 06_Indeterminación_y_la_nueva_mecánica_cuántica` | Criterio dimensional usado como condición suficiente para decidir pares conjugados, contradiciendo la propia teoría. | Usar dimensiones solo como filtro negativo. Para afirmar conjugación, limitarse a pares estudiados o explicar conceptualmente la relación canónica/conmutador. Propagar el cambio a objectives, worked examples, MCQ y summary. | No existe ninguna pregunta que acepte "mismas dimensiones de acción => conjugadas" como criterio suficiente. |
| P1 | `campo_gravitatorio / conservación de energía` | "El rozamiento siempre realiza trabajo negativo". | Acotar al modelo habitual de rozamiento cinético sobre superficie fija. Añadir contraejemplo breve (cinta transportadora) solo en Advanced/nota de alcance. | Toda aparición de "siempre" queda condicionada al modelo. |
| P2 | `campo_gravitatorio / Kepler` | Tercera ley expresada solo con r. | Usar T²/a³ como formulación general y aclarar que en órbita circular a=r. | Resumen y ejercicios distinguen órbita circular de elíptica. |
| P2 | `campo_gravitatorio / caída` | a=g sin explicitar caída libre. | Añadir "si la gravedad es la única fuerza relevante". | No se identifica g con aceleración neta cuando hay otras fuerzas. |
| P2 | `campo_gravitatorio / g máxima` | g máxima en superficie formulado universalmente. | Etiquetar como propiedad del modelo esférico ideal utilizado. | Claim marcado MODEL y no EXACT. |
| P2 | `mas / varias lecciones` | Propiedades del MAS ideal presentadas como propiedades de toda oscilación. | Introducir categoría oscilación y después MAS como modelo especial. Etiquetar independencia del periodo respecto a amplitud y envolvente exponencial con sus hipótesis. | Summary distingue oscilación general de MAS ideal. |
| P1 | `electromagnetismo / 06_El_campo_magnético_un_campo_sin_fuentes` | Negación global de potencial/energía potencial magnética. | Decir que no se usa un potencial escalar de posición análogo al eléctrico para una carga móvil. Añadir nota Advanced: potencial vector A y U=-mu·B para dipolos. | No aparece "no existe potencial magnético" de forma absoluta. |
| P1 | `electromagnetismo / dieléctricos` | Polarización descrita siempre en sentido contrario a E. | Separar vector polarización P (alineado con E en dieléctrico lineal ordinario) del campo de despolarización debido a cargas ligadas. | Diagramas y texto muestran correctamente P y campo de despolarización. |
| P2 | `electromagnetismo / solenoide` | Campo uniforme en todo el interior. | Cambiar a "aproximadamente uniforme lejos de extremos para solenoide largo". | Fórmula B=mu n I marcada APPROX/MODEL con condiciones. |
| P2 | `ondas / intensidad` | Relación intensidad-amplitud demasiado vaga. | Indicar I proporcional a A² bajo condiciones comparables. | Flashcard y MCQ no reducen la relación a mera correspondencia. |
| P2 | `ondas / decibelios` | "Los decibelios no se suman". | Explicar que los niveles en dB no se suman aritméticamente; se suman intensidades/potencias y se transforma. | Ejemplo de dos fuentes idénticas usa suma de intensidades. |
| P2 | `ondas / estacionarias` | Explicación débil de ausencia de transporte neto. | Explicar superposición de ondas viajeras opuestas y cancelación del flujo medio de energía. | Summary usa superposición, no "el nodo no puede hacer trabajo" como razón principal. |
| P2 | `ondas / tubos` | Nodos/antinodos sin indicar magnitud. | Especificar desplazamiento o presión en cada dibujo y regla. | Todos los esquemas etiquetan la magnitud. |
| P2 | `optica / varias lecciones` | Idealizaciones ópticas redactadas como universales. | Etiquetar n>=1, TIR perfecta y formación puntual de imagen como modelos de óptica geométrica/medios ordinarios/interfaz ideal. | Claims absolutos reciben etiqueta de alcance. |
| P1 | `relatividad / introducción a GR` | Motivación incorrecta: "como todos aceleran no existen sistemas inerciales y SR no sirve". | Reescribir: SR no incorpora gravitación como geometría dinámica; equivalencia local conduce a curvatura y mareas. SR sigue siendo válida localmente y puede describir observadores acelerados. | No se afirma que SR sea inútil por inexistencia de marcos inerciales. |
| P2 | `relatividad / equivalencia` | Falta "localmente". | Añadir localmente desde la primera definición y distinguir efectos de marea. | El principio de equivalencia nunca se formula globalmente. |
| P2 | `relatividad / tiempo propio` | Definición imprecisa. | Definir dos eventos sobre la misma línea de universo y reloj comóvil. | La definición no habla de "un evento en reposo". |
| P1 | `nuclear / energía de enlace` | Máximo exacto atribuido a Fe-56. | Hablar de región hierro-níquel; mencionar Ni-62 como referencia de mayor E/A y Fe-56 como muy cercano/relevante. | No se presenta Fe-56 como máximo exacto universal. |
| P1 | `nuclear / estabilidad` | Regla Z>83 inconsistente con estabilidad estricta. | Reformular regla práctica y tratar explícitamente Bi-209 si se habla de estabilidad estricta. | No hay contradicción entre tabla y regla verbal. |
| P2 | `cuantica / producción de pares` | Umbral 2mc² sin recoil. | Marcar 2mc² como umbral ideal y desprecio del retroceso nuclear a este nivel. | Claim marcado MODEL/APPROX. |
| P2 | `cuantica / de Broglie` | lambda=h/mv como fórmula fundamental. | Usar lambda=h/p; h/mv solo aproximación no relativista. | Formula canonical = h/p. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- `selectividad_fisica__ondas / 05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json` — 13830 words / 1.5 h = 9220 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__ondas / 11_Ondas_estacionarias_la_onda_que_no_viaja.json` — 18306 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__optica / 03_El_ángulo_límite_y_la_reflexión_total.json` — 13725 words / 1.5 h = 9150 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__campo_gravitatorio / 02_La_ley_de_gravitación_universal.json` — 18070 words / 2 h = 9035 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__cuantica / 06_Indeterminación_y_la_nueva_mecánica_cuántica.json` — 14633 words / 1.5 h = 9755 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__electromagnetismo / 05_El_potencial_eléctrico_sumar_sin_vectores.json` — 20190 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `selectividad_fisica__ondas` | `05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json` | medium | `content_overload` | 13830 words / 1.5 h = 9220 words/h |
| `selectividad_fisica__ondas` | `11_Ondas_estacionarias_la_onda_que_no_viaja.json` | high | `very_long_lesson` | 18306 words |
| `selectividad_fisica__optica` | `03_El_ángulo_límite_y_la_reflexión_total.json` | medium | `content_overload` | 13725 words / 1.5 h = 9150 words/h |
| `selectividad_fisica__campo_gravitatorio` | `02_La_ley_de_gravitación_universal.json` | medium | `content_overload` | 18070 words / 2 h = 9035 words/h |
| `selectividad_fisica__campo_gravitatorio` | `02_La_ley_de_gravitación_universal.json` | high | `very_long_lesson` | 18070 words |
| `selectividad_fisica__cuantica` | `06_Indeterminación_y_la_nueva_mecánica_cuántica.json` | medium | `content_overload` | 14633 words / 1.5 h = 9755 words/h |
| `selectividad_fisica__electromagnetismo` | `05_El_potencial_eléctrico_sumar_sin_vectores.json` | high | `very_long_lesson` | 20190 words |


Archivo con todas las filas exactas: `../qa/selectividad_fisica_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_fisica`.
2. Resolver el CSV `qa/selectividad_fisica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Selectividad / PAU — Química

**Curso ID:** `selectividad_quimica`  
**Unidades actuales:** 9  
**Lecciones actuales:** 127  
**Palabras pedagógicas aproximadas:** 777,156  
**Mediana de palabras/hora declarada:** ~3,767  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U08_Organica` | 27 | 170.562 | DIVIDIR en 2–3 módulos de navegación (estructura/nomenclatura. isomería. reactividad). |
| `U06_Acido_Base` | 15 | 89.082 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U09_Competencia` | 5 | 34.714 | DISTRIBUIR habilidades transversalmente + conservar módulo final integrador. |
| `U07_Electroquimica` | 14 | 90.940 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U02_Estructura_Atomica` | 12 | 71.923 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U05_Equilibrio` | 19 | 101.877 | DIVIDIR navegación en Cinética + Equilibrio; conservar canonical IDs/derived_from. |
| `U03_Enlace` | 14 | 95.948 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U01_Estequiometria` | 11 | 64.756 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U04_Termoquimica` | 10 | 57.354 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Formulación/nomenclatura imprescindible, mol, unidades, proporcionalidad, logaritmos para pH, cifras significativas y lectura de material/gráficas.
2. **01 Estequiometría** — Ecuaciones -> mol/masa -> gases/disoluciones -> limitante -> pureza/rendimiento -> mezcla/dilución -> problemas integrados.
3. **02 Estructura atómica** — Rutherford/Bohr/espectros -> cuantos/fotón -> números cuánticos -> orbitales -> configuración -> periodicidad.
4. **03 Enlace y estructura** — Lewis -> VSEPR -> polaridad -> fuerzas intermoleculares -> sólidos/propiedades -> comparación de modelos.
5. **04 Termoquímica** — Sistema/energía -> 1er principio -> entalpía -> Hess/formación/combustión -> entropía/Gibbs con hipótesis.
6. **05 Cinética** — Velocidad -> colisiones/Ea -> factores -> ley de velocidad al alcance del curso -> catalizadores.
7. **06 Equilibrio químico** — K/Q -> desplazamientos -> Le Châtelier -> solubilidad si aplica -> problemas.
8. **07 Ácido-base** — Teorías -> pH fuerte/débil -> Ka/Kb -> hidrólisis/buffers si están en alcance -> valoraciones/equivalencia.
9. **08 Electroquímica** — Números de oxidación -> ajuste -> pilas/potenciales -> espontaneidad -> electrólisis.
10. **09 Orgánica A: estructura y nomenclatura** — Hidrocarburos -> grupos funcionales -> isomería constitucional/estereoquímica según alcance.
11. **10 Orgánica B: reactividad** — Transformaciones y tipos de reacción por familias; separar reglas generales de casos de examen.
12. **11 Competencia experimental y PAU** — La competencia U09 se distribuye transversalmente y aquí se integra con datos, diseño experimental y simulacros.


### Reglas pedagógicas específicas de Química PAU
- Separar siempre **modelo microscópico**, **ecuación simbólica**, **magnitud macroscópica** y **procedimiento de cálculo**.
- En pH/equilibrio/termoquímica, las aproximaciones deben tener condiciones visibles antes de aplicarse.
- U09 Competencia no puede vivir solo al final: insertar mini-tareas de lectura de datos, material, seguridad y diseño experimental en cada módulo; mantener U09 como integración final.
- U05 Equilibrio (19 lecciones) debe dividirse al menos en **Cinética** y **Equilibrio** para reducir carga y mejorar dependencias.
- U08 Orgánica (27 lecciones) debe dividirse en estructura/nomenclatura, isomería y reactividad; no presentar 27 pasos como una única unidad de navegación.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `U06_Acido_Base / H2SO4` | Aproximación 2 H+ por mol reaparece como regla exacta en summaries/flashcards. | Distinguir neutralización completa, cálculo riguroso de pH con Ka2 y convención/aproximación PAU cuando proceda. | Cada claim de H2SO4 lleva scope/assumption explícita. |
| P1 | `U06_Acido_Base / neutralización` | "Ácido + base -> sal + agua" como definición general. | Definir Brønsted como transferencia de protón; sal+agua como caso frecuente con OH-/óxidos. | NH3 funciona como contraejemplo conceptual. |
| P1 | `U06_Acido_Base / equivalencia` | "moles ácido = moles base" sin estequiometría. | Usar equivalentes o relación de coeficientes desde el principio. | Ejercicios 2:1 y polipróticos no inducen igualdad molar simple. |
| P1 | `U04_Termoquimica / estado estándar` | Estado estándar definido como 25 C y 1 atm. | Definir presión estándar moderna como 1 bar; 298.15 K como temperatura habitual de tablas. Si un examen usa 1 atm, etiquetarlo EXAM_CONVENTION. | Summary separa definición universal de convención de problema. |
| P2 | `U04_Termoquimica / Qp=ΔH` | Faltan hipótesis. | Añadir sistema cerrado, presión constante y trabajo pV como único trabajo relevante en el modelo escolar. | Fórmula incluye conditions[]. |
| P2 | `U04_Termoquimica / ΔH=ΔU+ΔngRT` | Faltan hipótesis de gas ideal. | Etiquetar gases ideales/modelo. | Formula scope explícito. |
| P2 | `U04_Termoquimica / T=ΔH/ΔS` | Temperatura umbral presentada exacta. | Marcar aproximación suponiendo ΔH y ΔS constantes con T. | No se etiqueta EXACT. |
| P1 | `U05_Equilibrio / K=k+/k-` | Derivación generalizada indebidamente. | Limitar a reacción reversible elemental con las leyes de velocidad mostradas. | No se usa como derivación general de cualquier K. |
| P2 | `U05_Equilibrio / Kc` | Unidades de Kc tratadas como universales. | Mantener formalismo escolar si se necesita, con nota Advanced de actividades y K termodinámica adimensional. | No crea contradicción con química posterior. |
| P1 | `U08_Organica / estereoquímica` | Criterio cis/trans de alquenos extendido a ciclos. | Separar E/Z de dobles enlaces y cis/trans de ciclos. | Ejercicios clasifican por mecanismo geométrico correcto. |
| P2 | `U08_Organica / enantiómeros` | "Mismas propiedades salvo rotación óptica" sin entorno. | Añadir "en entorno achiral" y nota sobre sistemas quirales. | Scope explícito. |
| P2 | `U08_Organica / halogenación` | "Producto único" ignora estereoisómeros. | Distinguir producto constitucional y posibles estereoisómeros; marcar estereoquímica fuera de alcance si procede. | No usa "único" sin definir el nivel de identidad. |
| P2 | `U08_Organica / CCl4` | Referencia puede parecer recomendación experimental actual. | Presentarlo como referencia histórica o sustituir por descripción de solvente inerte no nucleófilo, con nota de seguridad si se conserva. | No se recomienda manipulación actual sin contexto. |
| P2 | `U03_Enlace / orbital` | Orbital igualado a región de probabilidad. | Definir orbital como función de onda; \|psi\|² da densidad de probabilidad. Simplificación visual puede quedar como modelo. | Definición formal y visual no se confunden. |
| P2 | `U03_Enlace / puente de hidrógeno` | "Interacción intermolecular más intensa" universal. | Reformular como tendencia en especies comparables. | No aparece superlativo universal. |
| P2 | `U02_Estructura_Atomica / Madelung` | Regla tratada como orden exacto con solo Cr/Cu como excepciones. | Etiquetar como guía de llenado útil para el nivel y no ley universal. | Claim marcado MODEL/HEURISTIC. |
| P0 | `U09_Competencia / 04_Resolución... / worked_examples[0]` | Redondeo inconsistente: 30,0-27,6 se muestra como 2,44. | Conservar cifras internas y mostrar 27,56 -> 2,44, o usar 27,6 -> 2,4. Introducir regla de cifras de guarda y redondeo final. | Las operaciones visibles son aritméticamente consistentes. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

_No se detectaron incidencias estructurales automáticas en este curso. Esto no elimina los cambios semánticos del ledger._

Archivo con todas las filas exactas: `../qa/selectividad_quimica_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_quimica`.
2. Resolver el CSV `qa/selectividad_quimica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Selectividad / PAU — Matemáticas II

**Curso ID:** `selectividad_matematicas`  
**Unidades actuales:** 12  
**Lecciones actuales:** 101  
**Palabras pedagógicas aproximadas:** 544,496  
**Mediana de palabras/hora declarada:** ~3,487  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `mat_limites` | 8 | 42.218 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_distribuciones` | 7 | 26.623 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_determinantes` | 6 | 61.584 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_vectores` | 7 | 37.017 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_integrales` | 12 | 36.968 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_probabilidad` | 10 | 45.808 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_rectas_planos` | 8 | 47.838 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_sistemas` | 7 | 47.708 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_matrices` | 7 | 73.005 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_geometria_metrica` | 7 | 37.120 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_representacion` | 11 | 40.210 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_derivadas` | 11 | 48.397 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Álgebra, ecuaciones, trigonometría básica, notación, funciones y manipulación simbólica; recuperación opcional.
2. **01 Cálculo I — Límites y continuidad** — Límite -> laterales -> operaciones -> infinito -> indeterminaciones -> continuidad -> asíntotas.
3. **02 Cálculo II — Derivadas** — Definición/tasa -> reglas -> tangente -> monotonicidad/extremos -> concavidad/inflexión -> optimización.
4. **03 Representación de funciones** — Integrar dominio, límites, derivadas, asíntotas y croquis; problemas de decisión, no solo checklist mecánico.
5. **04 Integración** — Primitivas -> técnicas -> integral definida -> áreas -> aplicaciones.
6. **05 Álgebra lineal** — Matrices -> determinantes -> rango/inversa -> sistemas -> discusión de parámetros.
7. **06 Geometría vectorial y afín** — Vectores -> rectas/planos -> posiciones -> producto escalar/vectorial -> distancias/ángulos/proyecciones.
8. **07 Probabilidad y distribuciones** — Sucesos -> condicionada/independencia -> Bayes/árboles -> variables/distribuciones -> problemas mixtos.
9. **08 PAU integrada** — Sets mixtos y simulacros por perfil de examen.


### Reglas pedagógicas específicas de Matemáticas II
- Cada técnica debe tener cuatro niveles: reconocer estructura -> aplicar -> elegir técnica -> problema mixto.
- No enseñar recetas sin hipótesis (L'Hôpital, inversa, inflexión, etc.).
- Añadir "comprobación" al final de cada worked example: dominio, signo, sustitución, derivación inversa o interpretación geométrica según proceda.
- Representación de funciones debe ser módulo integrador de límites+derivadas, no repetición aislada de reglas.
- En geometría, exigir dibujo/esquema y traducción entre forma vectorial, paramétrica, implícita cuando corresponda.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `mat_probabilidad / 04_Tablas_de_contingencia_y_diagramas_de_árbol / mcq[0]` | Opción correcta calcula x=0,4 pero explanation termina x=0,2. | Unificar correct/why_correct/explanation desde una única solución canónica; x=0,4. | No hay dos resultados distintos en campos del mismo item. |
| P1 | `mat_derivadas / inflexión` | f"(x0)=0 presentada como condición necesaria universal. | Definir inflexión por cambio de concavidad. Usar f"=0 o no existencia como candidatos y comprobar cambio de signo/concavidad. | Contraejemplo o nota impide memorizar f"=0 como equivalencia. |
| P1 | `mat_limites / L'Hôpital` | Receta sin hipótesis. | Añadir recuadro de hipótesis y condición de forma indeterminada real. | No se aplica como identidad algebraica. |
| P2 | `mat_derivadas / tangente vertical` | f'(a)=±∞ tratado como derivada ordinaria. | Hablar de pendiente infinita/límite de derivada; la derivada real finita no existe. | Terminología consistente. |
| P2 | `mat_probabilidad / no equiprobable` | No equiprobable equivale a usar frecuencias. | Distinguir estimación empírica y modelo no equiprobable conocido a priori. | Ejemplos cubren ambas situaciones. |
| P2 | `mat_probabilidad / reemplazamiento` | Con reemplazo implica independencia por definición. | Decir que ocurre en el modelo estándar de extracciones idénticas con reemplazo; independencia es propiedad del modelo conjunto. | No se usa como equivalencia semántica. |
| P2 | `matrices/grafos` | (A^k)ij descrito como caminos simples. | Usar walks/recorridos de longitud k; aclarar que pueden repetirse vértices/aristas. | Terminología de grafos correcta. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

_No se detectaron incidencias estructurales automáticas en este curso. Esto no elimina los cambios semánticos del ledger._

Archivo con todas las filas exactas: `../qa/selectividad_matematicas_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_matematicas`.
2. Resolver el CSV `qa/selectividad_matematicas_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Selectividad / PAU — Matemáticas Aplicadas a las CCSS II

**Curso ID:** `selectividad_matematicas_ccss`  
**Unidades actuales:** 9  
**Lecciones actuales:** 66  
**Palabras pedagógicas aproximadas:** 366,079  
**Mediana de palabras/hora declarada:** ~3,856  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `mat_matrices` | 7 | 74.633 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_integrales` | 9 | 24.895 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_sistemas` | 6 | 41.816 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_derivadas` | 10 | 42.884 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_limites` | 7 | 35.701 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_programacion_lineal` | 5 | 30.281 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_representacion` | 9 | 32.853 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_probabilidad` | 6 | 35.248 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_muestreo_inferencia` | 7 | 47.768 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Álgebra, funciones, porcentajes, lectura de tablas/gráficas y probabilidad elemental.
2. **01 Funciones, límites y continuidad** — Interpretación en contextos socioeconómicos además de técnica.
3. **02 Derivadas y optimización** — Razón de cambio -> reglas -> crecimiento/extremos -> optimización contextual.
4. **03 Representación e integración** — Estudio de funciones -> primitivas/integral -> área/aplicaciones del alcance.
5. **04 Álgebra lineal** — Matrices -> sistemas -> aplicaciones contextualizadas.
6. **05 Programación lineal** — Inecuaciones -> región factible -> función objetivo -> interpretación.
7. **06 Probabilidad** — Sucesos -> condicionada -> independencia -> Bayes/árboles/tablas.
8. **07 Muestreo e inferencia** — Población/muestra -> distribuciones muestrales -> intervalos/contrastes según syllabus; lenguaje estadístico riguroso.
9. **08 PAU integrada** — Problemas contextualizados, lectura crítica de datos y simulacros.


### Reglas pedagógicas específicas de CCSS
- Priorizar interpretación de resultados en lenguaje del contexto, además del cálculo.
- En estadística/inferencia, diferenciar con cuidado **estimador, estimación, parámetro, muestra, sesgo, precisión y no rechazo**.
- No convertir reglas heurísticas de examen (por ejemplo n>=30) en teoremas universales.
- Programación lineal debe incluir lectura de restricciones y análisis de solución, no solo dibujar semiplanos.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `mat_derivadas / inflexión` | f"(x0)=0 presentada como condición necesaria universal. | Definir inflexión por cambio de concavidad. Usar f"=0 o no existencia como candidatos y comprobar cambio de signo/concavidad. | Contraejemplo o nota impide memorizar f"=0 como equivalencia. |
| P1 | `mat_limites / L'Hôpital` | Receta sin hipótesis. | Añadir recuadro de hipótesis y condición de forma indeterminada real. | No se aplica como identidad algebraica. |
| P2 | `mat_derivadas / tangente vertical` | f'(a)=±∞ tratado como derivada ordinaria. | Hablar de pendiente infinita/límite de derivada; la derivada real finita no existe. | Terminología consistente. |
| P2 | `mat_probabilidad / no equiprobable` | No equiprobable equivale a usar frecuencias. | Distinguir estimación empírica y modelo no equiprobable conocido a priori. | Ejemplos cubren ambas situaciones. |
| P2 | `mat_probabilidad / reemplazamiento` | Con reemplazo implica independencia por definición. | Decir que ocurre en el modelo estándar de extracciones idénticas con reemplazo; independencia es propiedad del modelo conjunto. | No se usa como equivalencia semántica. |
| P1 | `mat_muestreo_inferencia / representatividad` | Aleatoriedad presentada como garantía de representatividad. | Explicar que reduce sesgo de selección y habilita inferencia probabilística, pero una muestra concreta puede no ser representativa y existen sesgos de marco/no respuesta/medición. | No aparece "garantiza representatividad". |
| P2 | `mat_muestreo_inferencia / TCL` | n>=30 tratado como frontera universal. | Etiquetar HEURISTIC; normal exacta si población normal y posibles n mayores con asimetría/colas pesadas. | Regla 30 nunca marcada EXACT. |
| P2 | `mat_muestreo_inferencia / suma normal` | Suma ~ N(nμ,σ√n) sin distinguir exactitud/aproximación. | Exacta para normales independientes; aproximada por TCL en otros casos bajo condiciones. | Scope explícito. |
| P2 | `mat_muestreo_inferencia / eficiencia` | n/σ² o n/[p(1-p)] llamado definición general de eficiencia. | Reetiquetar como precisión/información en ese contexto. | Terminología no generaliza indebidamente. |
| P2 | `contrastes / región de aceptación` | "Aceptar H0". | Preferir región de no rechazo; explicar no rechazar != probar H0. | Feedback y summaries usan no rechazo. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `selectividad_matematicas_ccss__mat_representacion` | `08_Representar_exponenciales_y_logarítmicas.json` | medium | `dangling_objective_ref` | LO-09-1 at theory_blocks/1/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `08_Representar_exponenciales_y_logarítmicas.json` | medium | `dangling_objective_ref` | LO-09-1 at worked_examples/0/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `08_Representar_exponenciales_y_logarítmicas.json` | medium | `dangling_objective_ref` | LO-09-1 at exercises/0/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `08_Representar_exponenciales_y_logarítmicas.json` | medium | `dangling_objective_ref` | LO-09-1 at exercises/1/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `08_Representar_exponenciales_y_logarítmicas.json` | medium | `dangling_objective_ref` | LO-09-1 at mcq/0/objective_id |
| `selectividad_matematicas_ccss__mat_representacion` | `09_Funciones_definidas_a_trozos_y_con_valor_absoluto.json` | medium | `dangling_objective_ref` | LO-11-1 at theory_blocks/0/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `09_Funciones_definidas_a_trozos_y_con_valor_absoluto.json` | medium | `dangling_objective_ref` | LO-11-1 at theory_blocks/1/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `09_Funciones_definidas_a_trozos_y_con_valor_absoluto.json` | medium | `dangling_objective_ref` | LO-11-1 at worked_examples/0/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `09_Funciones_definidas_a_trozos_y_con_valor_absoluto.json` | medium | `dangling_objective_ref` | LO-11-1 at guided_exercises/0/objective_ids |
| `selectividad_matematicas_ccss__mat_representacion` | `09_Funciones_definidas_a_trozos_y_con_valor_absoluto.json` | medium | `dangling_objective_ref` | LO-11-1 at exam_questions/0/objective_ids |


Archivo con todas las filas exactas: `../qa/selectividad_matematicas_ccss_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_matematicas_ccss`.
2. Resolver el CSV `qa/selectividad_matematicas_ccss_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — ESO — Matemáticas

**Curso ID:** `eso_matematicas`  
**Unidades actuales:** 20  
**Lecciones actuales:** 122  
**Palabras pedagógicas aproximadas:** 600,680  
**Mediana de palabras/hora declarada:** ~4,681  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `mat_trigonometria` | 9 | 51.460 | D ESO CORE / EXTENSION — triángulo rectángulo en Core; circunferencia/identidades/ec. trigonométricas según profundidad. |
| `mat_potencias_raices` | 5 | 25.973 | A FOUNDATIONS / ESO CORE — mantener. graduando radicales avanzados y racionalización según nivel. |
| `mat_numeros_operaciones` | 7 | 34.526 | A FOUNDATIONS — base numérica; obligatoria para alumnos con lagunas y reutilizable como recuperación. |
| `mat_probabilidad` | 7 | 28.218 | E ESO CORE / EXTENSION — sucesos. árboles y Laplace; combinatoria avanzada se etiqueta Extension. |
| `mat_algebra_polinomios` | 5 | 26.346 | B ESO CORE — álgebra y polinomios. |
| `mat_ecuaciones` | 5 | 29.100 | B ESO CORE — progresión 1º/2º grado -> factorizables -> racionales/radicales; partes exponencial/log pueden requerir EXTENSION. |
| `mat_familias_funciones` | 7 | 30.613 | C ESO CORE — lineales/cuadráticas/inversa; exponenciales/log según banda y profundidad. |
| `mat_distribuciones` | 4 | 20.073 | F/G REVIEW — clasificar lesson a lesson; binomial/normal/aproximación pueden ser puente a Bachillerato. |
| `mat_geometria_metrica` | 8 | 39.810 | D ESO CORE — métrica. semejanza. Pitágoras y escalas. |
| `mat_sucesiones` | 6 | 28.277 | F ESO EXTENSION — conservar como ampliación/puente si excede el núcleo de la ruta elegida. |
| `mat_limites_continuidad` | 5 | 26.460 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_proporcionalidad_financiera` | 5 | 24.613 | A FOUNDATIONS / ESO CORE — porcentajes e interés con problemas contextualizados. |
| `mat_geometria_analitica` | 7 | 28.026 | D ESO CORE / EXTENSION — plano cartesiano. vectores y rectas; clasificar partes avanzadas. |
| `mat_funciones_representacion` | 6 | 30.549 | C ESO CORE — lectura. dominio. crecimiento y transformaciones al nivel de etapa. |
| `mat_estadistica_descriptiva` | 5 | 29.670 | E ESO CORE — descripción y lectura crítica. |
| `mat_derivadas` | 7 | 32.582 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_estadistica_bidimensional` | 7 | 31.673 | F ESO EXTENSION — nube/correlación/regresión básica; corregir P0 y evitar sobreformalización. |
| `mat_sistemas_inecuaciones` | 7 | 39.499 | B ESO CORE — etiquetar extensiones como sistemas no lineales/Gauss si exceden la ruta base. |
| `mat_complejos` | 5 | 23.491 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_conicas` | 5 | 19.721 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **A Foundations** — Números y operaciones -> potencias/raíces -> proporcionalidad/porcentajes -> lenguaje algebraico. Ruta de recuperación y también inicio para alumnos con poca base.
2. **B ESO Core — Álgebra** — Polinomios -> ecuaciones -> sistemas/inecuaciones con progresión de dificultad.
3. **C ESO Core — Funciones** — Concepto/representación -> lineales/cuadráticas/proporcionalidad inversa -> transformaciones y lectura gráfica.
4. **D ESO Core — Geometría** — Métrica -> semejanza/Pitágoras -> analítica básica -> trigonometría de triángulos y aplicaciones.
5. **E ESO Core — Estadística y probabilidad** — Descriptiva -> probabilidad -> tablas/árboles -> lectura crítica de datos.
6. **F ESO Extension** — Sucesiones, estadística bidimensional/regresión básica, combinatoria y ampliaciones que sí se quieran ofrecer a altas capacidades.
7. **G Bachillerato Bridge** — Complejos, cónicas, límites, derivadas y contenidos de distribución/normal que excedan el núcleo ESO. Nunca en ruta ESO por defecto.


### Regla estructural principal de ESO Matemáticas
El mayor cambio no es de redacción, sino de **taxonomía**. El agente debe añadir `curriculum_band` a todas las unidades/lecciones y reconstruir la navegación. Un alumno que elija ESO Core no debe ver complejos, cónicas, límites o derivadas como continuación obligatoria.

### Regla de accesibilidad
- Cada lección Core debe poder resolverse con prerrequisitos enlazados dentro de Foundations.
- Evitar introducir formalismo de Bachillerato para explicar un concepto ESO si existe una explicación gráfica/intuitiva suficiente.
- La ruta Excellence puede abrir contenido F/G, pero debe indicar claramente "ampliación" o "puente a Bachillerato".


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `mat_estadistica_bidimensional / 03_Regresión_lineal_básica_interpretar_y_predecir / mcq[1]` | 1,1·3+3,2 se calcula como 6,7; correcto 6,5; residuo 0,5 y ninguna opción lo ofrece. | Cambiar datos/opciones para que exista una única respuesta correcta. Si se conservan datos, respuesta=0,5. | Evaluador numérico confirma opción y explicación. |
| P1 | `catálogo completo` | Mezcla ESO core con complejos, cónicas, límites, derivadas y normal/binomial avanzada como una secuencia homogénea. | Separar curriculum_band: ESO_FOUNDATION, ESO_CORE, ESO_EXTENSION y BACH_BRIDGE. La ruta por defecto nunca incluye BACH_BRIDGE. | Un alumno "ESO" no recibe contenido Bachillerato salvo elección/diagnóstico explícito. |
| P1 | `funciones / inversa` | Algoritmo intercambiar x/y sin comprobar inyectividad. | Comprobar one-to-one/injectiva o restringir dominio antes de construir inversa. | Ejemplos incluyen una función que requiere restricción de dominio. |
| P2 | `estadística descriptiva / cuartiles` | Una convención de cuartiles presentada como única. | Declarar convención del curso/examen/calculadora. | Los resultados se interpretan según convención declarada. |
| P2 | `estadística bidimensional / R²` | 0<=R²<=1 universal. | Acotar a OLS estándar con intercepto; nota Advanced sobre modelos sin intercepto. | Claim no universal. |
| P1 | `mat_ecuaciones / 05_Ecuaciones_exponenciales_y_logarítmicas_básicas` | 7 IDs duplicados dentro de la lección. | Regenerar IDs deterministas únicos y actualizar referencias. | Validador unique IDs pasa sin colisiones. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | TH-0505-5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-6 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-7 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S6 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S7 x2 |


Archivo con todas las filas exactas: `../qa/eso_matematicas_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=eso_matematicas`.
2. Resolver el CSV `qa/eso_matematicas_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — ESO — Física y Química (Foundations / versión standalone)

**Curso ID:** `eso_fisicaquimica`  
**Unidades actuales:** 4  
**Lecciones actuales:** 19  
**Palabras pedagógicas aproximadas:** 26,456  
**Mediana de palabras/hora declarada:** ~857  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U-ESO-01` | 4 | 6.053 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-03` | 5 | 6.900 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-04` | 5 | 6.596 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-02` | 5 | 6.907 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations científicas** — Pregunta/hipótesis/evidencia, SI, conversiones, incertidumbre, tablas y gráficas.
2. **01 Materia y modelo de partículas** — Masa/volumen/densidad -> partículas -> temperatura/cambios de estado -> curvas de calentamiento.
3. **02 Sustancias, mezclas y disoluciones** — Clasificación -> separación -> soluto/disolvente -> concentración -> diseño experimental.
4. **03 Estructura atómica básica** — Partículas subatómicas -> Z/A/isótopos -> iones -> modelos atómicos -> tabla/estructura al alcance.
5. **04 Checkpoint de Foundations** — Evaluación acumulativa que decide si el alumno puede saltar recuperación al entrar en 4.º ESO/Bachillerato.


### Función recomendada de este corpus
Convertirlo en **Foundations de Física y Química**, no mantenerlo como una copia paralela de FQ completo. Debe ser corto, extremadamente claro y reutilizable como recuperación desde cursos posteriores.

- La prioridad es comprensión de medición, partículas, mezclas y átomo.
- Evitar fórmulas que todavía no se puedan interpretar; si aparecen Q=mcΔT o Q=mL, deben ser opcionales/extension si la unidad pretende ser realmente básica.
- Los summaries actuales deben regenerarse completamente si contienen boilerplate/truncado.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U-ESO-02 / lesson_03` | Cambios de estado: "absorber calor => aumenta Ec" contradice meseta a T constante. | Reescribir en tres fases: antes cambia Ec/T; durante cambio T constante y cambia energía potencial/configuración; después vuelve a cambiar Ec/T. | Teoría, summary y MCQ coinciden. |
| P0 | `corpus / versionado` | Duplica 19 lecciones con fq_completo y divergen. | Convertir a fuente canónica: uno de los dos deja de ser copia editable. Usar canonical_lesson_id + variant/config o generación derivada. | No existen dos bodies independientes con mismo canonical_lesson_id. |
| P1 | `summaries` | Boilerplate repetitivo y campos truncados como "Una curva T vs." o "1.". | Regenerar summary desde core_claims/assumptions/formulae/mistakes. Añadir lint de truncado. | Ningún summary contiene fragmentos incompletos o boilerplate genérico como idea principal. |
| P2 | `U-ESO-02 / curvas de calentamiento` | "Mesetas perfectamente horizontales" como afirmación experimental. | Decir horizontal en modelo ideal/aproximadamente horizontal en experimento con sustancia pura bajo condiciones controladas. | Claim etiquetado MODEL. |
| P3 | `MCQ corpus` | 228 distractores sin why_wrong. | No rellenar mecánicamente todos: completar prioritariamente distractores que representan misconceptions; permitir omission para distractores triviales con regla documentada. | 100% de distractores conceptuales tienen feedback útil. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Severidad | Tipo | Cantidad |
|---|---|---:|
| low | `wrong_option_no_explanation` | 228 |

**Nota:** el CSV de QA del curso contiene las filas exactas. No inflar el documento con 228 distractores repetitivos.


Archivo con todas las filas exactas: `../qa/eso_fisicaquimica_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=eso_fisicaquimica`.
2. Resolver el CSV `qa/eso_fisicaquimica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Física y Química — corpus completo ESO / 4.º ESO / 1.º Bachillerato

**Curso ID:** `fq_completo`  
**Unidades actuales:** 22  
**Lecciones actuales:** 143  
**Palabras pedagógicas aproximadas:** 501,685  
**Mediana de palabras/hora declarada:** ~2,250  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U-4Q-03` | 6 | 18.220 | RUTA 4ESO Química. |
| `U-ESO-04` | 5 | 18.179 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-B1F-03` | 8 | 20.310 | RUTA 1Bach Física. |
| `U-B1Q-01` | 7 | 23.139 | RUTA 1Bach Química. |
| `U-B1F-01` | 8 | 28.897 | RUTA 1Bach Física. |
| `U-ESO-01` | 4 | 17.149 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-B1Q-03` | 8 | 25.790 | RUTA 1Bach Química. |
| `U-4F-01` | 6 | 27.280 | RUTA 4ESO Física. |
| `U-4Q-02` | 7 | 21.962 | RUTA 4ESO Química. |
| `U-ESO-02` | 5 | 17.533 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-4Q-04` | 8 | 36.473 | RUTA 4ESO Química. |
| `U-4Q-06` | 6 | 17.734 | RUTA 4ESO Química. |
| `U-4F-03` | 5 | 18.890 | RUTA 4ESO Física. |
| `U-4F-04` | 7 | 24.385 | RUTA 4ESO Física. |
| `U-4Q-05` | 5 | 13.214 | RUTA 4ESO Química. |
| `U-4Q-01` | 6 | 30.818 | RUTA 4ESO Química. |
| `U-B1Q-05` | 7 | 24.399 | RUTA 1Bach Química. |
| `U-4F-02` | 7 | 26.175 | RUTA 4ESO Física. |
| `U-B1Q-04` | 8 | 24.588 | RUTA 1Bach Química. |
| `U-B1F-02` | 8 | 22.056 | RUTA 1Bach Física. |
| `U-B1Q-02` | 7 | 26.937 | RUTA 1Bach Química. |
| `U-ESO-03` | 5 | 17.557 | NO DUPLICAR: referenciar lección canónica de Foundations. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Shared Foundations** — Referenciar de forma canónica U-ESO-01..04; no copiar.
2. **Ruta 4.º ESO Física** — U-4F-01 movimiento -> U-4F-02 fuerzas -> U-4F-03 presión/fluidos -> U-4F-04 energía/calor.
3. **Ruta 4.º ESO Química** — U-4Q-01 enlace -> U-4Q-02 formulación/oxidación -> U-4Q-03 orgánica básica -> U-4Q-04 reacciones -> U-4Q-05 mol -> U-4Q-06 disoluciones/gases.
4. **Ruta 1.º Bach Física** — U-B1F-01 cinemática/vectorial -> U-B1F-02 dinámica -> U-B1F-03 trabajo/energía.
5. **Ruta 1.º Bach Química** — U-B1Q-01 estructura/periodicidad -> U-B1Q-02 enlace -> U-B1Q-03 mol/gases -> U-B1Q-04 estequiometría -> U-B1Q-05 orgánica.
6. **Exam/competency adapters** — Cada ruta tiene sus checkpoints y bancos; el meta-corpus no se presenta al alumno como una lista única de 143 lecciones.


### Regla estructural principal de FQ completo
No exponer "FQ completo" como un curso lineal. Debe ser un **content graph/meta-corpus** del que se construyen rutas por etapa. El alumno elige/recibe una ruta (Foundations, 4ESO Física, 4ESO Química, 1Bach Física, 1Bach Química), y las dependencias cruzadas se resuelven por prerequisitos.

- `U-ESO-*` se comparte por referencia con el curso Foundations.
- Un cambio en una lección canónica debe reflejarse en todas las rutas automáticamente.
- Si se pretende vender cada ruta como "curso completo" de etapa, ejecutar además auditoría de cobertura contra el syllabus oficial correspondiente; este documento solo garantiza reestructuración del contenido existente.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U-B1Q-04 / lesson_01` | Al menos dos opciones correctas contienen why_wrong. | Validar opción correcta: why_wrong nulo y why_correct compatible. | Schema CI bloquea cualquier correct_option_marked_wrong. |
| P0 | `U-ESO-*` | Duplica contenido de eso_fisicaquimica. | Usar misma fuente canónica compartida; este corpus referencia/compone Foundations, no copia. | Hashes/bodies canónicos únicos. |
| P2 | `U-B1Q-02 / polaridad/enlace` | Umbrales Δχ 0,4 y 1,7 como fronteras físicas exactas. | Etiquetar regla orientativa del curso. | Claim HEURISTIC. |
| P2 | `U-4Q-01 / enlace iónico` | Transferencia completa metal->no metal como definición universal. | Presentar como modelo introductorio de formación de iones/red. | Claim MODEL. |
| P2 | `enlace / orden` | "Más pares compartidos => siempre más corto y fuerte". | Acotar a comparación del mismo par de átomos/orden de enlace comparable. | No universal. |
| P2 | `energía / eficiencia` | 0<eta<1 siempre. | Permitir eta=0 en límite conceptual y <=1. | Fórmula/rango matemático correcto. |
| P2 | `mecánica / rozamiento` | Rozamiento siempre resta energía. | Mismo alcance que Selectividad Física: modelo típico superficie fija. | No universal. |
| P2 | `summary layer` | Resúmenes genéricos "se entiende relacionando...". | Regenerar resúmenes específicos desde claims. | Cada summary identifica 3-6 ideas específicas de esa lección. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `fq_completo__U-B1Q-04` | `lesson_01.json` | medium | `correct_option_marked_wrong` | MC-L01-01 A: Es la mitad de 44,0 g; resulta de dividir mal la proporción o de un error de cálculo con n=0,250 mol en lugar de 0,500. |
| `fq_completo__U-B1Q-04` | `lesson_01.json` | medium | `correct_option_marked_wrong` | MC-L01-02 B: Correcta: n(H₂)=4,0/2,0=2,0 mol; proporción 2:1 → n(O₂)=1,0 mol; m(O₂)=1,0·32,0=32,0 g. |


Archivo con todas las filas exactas: `../qa/fq_completo_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=fq_completo`.
2. Resolver el CSV `qa/fq_completo_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Cambridge GCSE/IGCSE — Physics

**Curso ID:** `gcse_ciencias_phys`  
**Unidades actuales:** 10  
**Lecciones actuales:** 62  
**Palabras pedagógicas aproximadas:** 310,944  
**Mediana de palabras/hora declarada:** ~3,252  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U06_Waves_Light_and_Sound` | 8 | 39.500 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U09_Space_Physics` | 4 | 18.904 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U05_Thermal_Physics` | 7 | 44.859 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U08_Nuclear_Physics` | 6 | 22.839 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U07_Electricity_and_Magnetism` | 13 | 75.705 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U04_Energy_Work_and_Power` | 6 | 26.787 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U10_Revision_and_Exam_Practice` | 1 | 6.930 | CONVERTIR en Exam Mode/pool; no mantener como una lección lineal. |
| `U03_Forces_and_Pressure` | 7 | 28.842 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U01_Measurement_and_Motion` | 6 | 32.420 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U02_Mass_Weight_and_Density` | 4 | 14.158 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Units, standard form, rearranging equations, graphs and basic vector/scalar language; diagnostic-driven.
2. **01 Measurement and Motion** — Keep U01 but enforce velocity-time vs speed-time distinction.
3. **02 Mass, Weight and Density** — Keep U02; move Exercise Bank to pool.
4. **03 Forces and Pressure** — Keep U03; integrate vector/resultant and model conditions.
5. **04 Energy, Work and Power** — Keep U04; fix stored-energy balance.
6. **05 Thermal Physics** — Keep U05; fix phase-change contradiction.
7. **06 Waves, Light and Sound** — Keep U06; fix wave definition/refraction wording and add longitudinal-friendly definitions.
8. **07 Electricity and Magnetism** — Keep U07; separate changing flux principle from AC exam rule.
9. **08 Nuclear Physics** — Keep U08.
10. **09 Space Physics** — Keep U09; circular vs elliptical orbit scope.
11. **10 Revision / Exam Mode** — U10 becomes exercise pool + generated mixed papers, not a one-lesson unit.


### Reglas pedagógicas específicas de GCSE/IGCSE Physics
- Mantener `official_track` (Core/Extended si aplica) separado de `learning_route`.
- Reforzar command words y mark-scheme language en Exam Mode, no contaminar la explicación conceptual con frases memorizadas sin comprensión.
- Cada practical/graph skill debe aparecer primero guiado y después en pregunta donde el alumno interpreta datos.
- Exercise Banks pasan a pools etiquetados por syllabus code, skill, track y difficulty.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U05_Thermal_Physics / 03_Melting_boiling_and_evaporation` | Durante meseta se dice que partículas "slow down", contradiciendo T constante. | Tres fases antes/durante/después; durante el cambio no cambia Ec media/T idealmente. | Theory, challenge y summary son consistentes. |
| P1 | `U06_Waves_Light_and_Sound / 01_Wave_quantities_and_types` | Definición de wave exige medium y excluye EM waves. | Definir wave como disturbance/oscillation transferring energy without net matter transport; mechanical waves need medium, EM do not. | MCQ no exige medium para toda wave. |
| P1 | `U01_Measurement_and_Motion / graphs` | Speed-time usado donde se razona aceleración firmada/direccional. | Usar velocity-time cuando el signo/dirección importa; speed-time solo para rapidez. | Los gráficos tienen etiqueta coherente con la magnitud. |
| P1 | `U04_Energy_Work_and_Power` | Balance "energy leaving always equals entered" omite stored energy. | Usar energy in = useful out + wasted out + change in stored energy. | Problemas con acumulación de energía funcionan. |
| P2 | `U09_Space_Physics / orbit` | Gravedad perpendicular al movimiento y speed constante para toda órbita. | Acotar a circular orbit. | Elíptica puede variar speed. |
| P2 | `U06 / wave definitions` | Amplitude/wavelength definidas con vertical/horizontal del dibujo. | Definiciones físicas independientes de la orientación del dibujo y válidas para longitudinales. | Se pueden aplicar a longitudinal waves. |
| P2 | `U06 / refraction` | "denser medium" ambiguo. | Usar optically denser / higher refractive index. | Terminología óptica precisa. |
| P2 | `U06/EM spectrum` | Radio/microwaves "do not harm". | Decir non-ionising, pero alta intensidad puede causar thermal damage. | No se equipara non-ionising con harmless. |
| P2 | `U07 / transformer` | Transformer works with AC, not DC como absoluto. | Explicar que necesita changing magnetic flux; steady DC no mantiene emf, transients/pulses sí varían flujo. | Regla de examen y principio físico ambos presentes. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `gcse_ciencias_phys__U06_Waves_Light_and_Sound` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U05_Thermal_Physics` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U08_Nuclear_Physics` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U07_Electricity_and_Magnetism` | `13_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U04_Energy_Work_and_Power` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U10_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U10_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_practice` |  |
| `gcse_ciencias_phys__U03_Forces_and_Pressure` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U01_Measurement_and_Motion` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U02_Mass_Weight_and_Density` | `04_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |


Archivo con todas las filas exactas: `../qa/gcse_ciencias_phys_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=gcse_ciencias_phys`.
2. Resolver el CSV `qa/gcse_ciencias_phys_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Cambridge GCSE/IGCSE — Chemistry

**Curso ID:** `gcse_ciencias_chem`  
**Unidades actuales:** 13  
**Lecciones actuales:** 70  
**Palabras pedagógicas aproximadas:** 356,803  
**Mediana de palabras/hora declarada:** ~3,339  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U04_Electrochemistry` | 5 | 25.620 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U11_Organic_Chemistry` | 8 | 31.016 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U07_Acids_Bases_and_Salts` | 5 | 36.750 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U08_The_Periodic_Table` | 5 | 22.482 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U03_Formulas_and_Amounts` | 6 | 28.468 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U10_Environmental_Chemistry` | 5 | 28.831 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U12_Experimental_Methods_and_Analysis` | 7 | 41.219 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U09_Metals` | 6 | 31.478 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U01_States_of_Matter` | 6 | 29.659 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U05_Chemical_Energetics` | 4 | 14.532 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U13_Revision_and_Exam_Practice` | 1 | 10.914 | CONVERTIR en Exam Mode/pool; no mantener como una lección lineal. |
| `U02_Atoms_Elements_and_Bonding` | 7 | 29.059 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U06_Chemical_Reactions` | 5 | 26.775 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Particle model vocabulary, formulae, balancing, units, proportional reasoning and practical measurement.
2. **01 States of Matter** — Keep U01; ensure model/experiment distinction.
3. **02 Atoms, Elements and Bonding** — Keep U02.
4. **03 Formulae and Amounts** — Keep U03; worked-example ladder for mole/ratio.
5. **04 Electrochemistry** — Keep U04.
6. **05 Chemical Energetics** — Keep U05; definition vs calorimeter evidence.
7. **06 Chemical Reactions** — Keep U06.
8. **07 Acids, Bases and Salts** — Keep U07; broaden base definition and scope pH/neutralisation claims.
9. **08 Periodic Table** — Keep U08.
10. **09 Metals** — Keep U09.
11. **10 Environmental Chemistry** — Keep U10.
12. **11 Organic Chemistry** — Keep U11; split long sequences if a lesson exceeds atomic target.
13. **12 Experimental Methods and Analysis** — Keep U12 and use it as cross-link target from all practical claims.
14. **13 Revision / Exam Mode** — U13 becomes tagged pool and mixed-paper generator, not ordinary lesson.


### Reglas pedagógicas específicas de GCSE/IGCSE Chemistry
- Mantener `official_track` separado de profundidad del alumno.
- Al pasar del modelo de partículas a enlace/reacción, usar representaciones múltiples: partículas/iones -> fórmula -> ecuación -> observación macroscópica.
- Practical methods deben enlazarse desde las unidades conceptuales; no quedar aislados en U12.
- Todos los Exercise Banks son pools, no lecciones ordinarias.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `U07_Acids_Bases_and_Salts` | Base definida como cualquier metal oxide/hydroxide. | Decir common bases include metal oxides/hydroxides; definición del nivel debe incluir bases como NH3. | NH3 no contradice la definición. |
| P2 | `U07 / pH` | pH 0-14 como límite universal. | Etiquetar rango típico para aqueous dilute solutions near room temperature. | No se presenta como límite físico absoluto. |
| P2 | `U07 / neutralisation` | Neutralisation always salt + water. | Acotar a acid + hydroxide/oxide; no todas las bases generan agua. | Ejemplo NH3 no rompe la regla. |
| P2 | `U05_Chemical_Energetics` | Exo/endo decidido solo por observed ΔT. | Definir por energy transfer/enthalpy; ΔT es evidencia experimental bajo condiciones controladas y puede sufrir heat loss. | Teoría distingue definición y observación. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `gcse_ciencias_chem__U04_Electrochemistry` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U11_Organic_Chemistry` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U07_Acids_Bases_and_Salts` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U08_The_Periodic_Table` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U03_Formulas_and_Amounts` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U10_Environmental_Chemistry` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U12_Experimental_Methods_and_Analysis` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U09_Metals` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U01_States_of_Matter` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U05_Chemical_Energetics` | `04_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U13_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U13_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_practice` |  |
| `gcse_ciencias_chem__U02_Atoms_Elements_and_Bonding` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U06_Chemical_Reactions` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |


Archivo con todas las filas exactas: `../qa/gcse_ciencias_chem_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=gcse_ciencias_chem`.
2. Resolver el CSV `qa/gcse_ciencias_chem_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.


---

# Auditoría de reestructuración — Cambridge GCSE/IGCSE — Mathematics

**Curso ID:** `gcse_mates`  
**Unidades actuales:** 9  
**Lecciones actuales:** 87  
**Palabras pedagógicas aproximadas:** 922,694  
**Mediana de palabras/hora declarada:** ~5,509  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U09_Statistics` | 8 | 81.468 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U07_Transformations_and_Vectors` | 5 | 51.330 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U02_Algebra_and_Graphs` | 21 | 253.906 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U01_Number` | 18 | 204.675 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U05_Mensuration` | 6 | 60.527 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U08_Probability` | 5 | 49.130 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U06_Trigonometry` | 8 | 71.561 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U03_Coordinate_Geometry` | 7 | 52.001 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U04_Geometry` | 9 | 98.096 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Arithmetic fluency, negative numbers, fractions and calculator literacy as diagnostic recovery nodes.
2. **01 Number** — Keep U01 concepts; move L18 Exercise Bank into skill-tagged pool and serve subsets.
3. **02 Algebra and Graphs** — Keep U02; L21 bank must be decomposed/poolized; prerequisites link back to number skills.
4. **03 Coordinate Geometry** — Keep U03.
5. **04 Geometry** — Keep U04; L09 bank -> pool.
6. **05 Mensuration** — Keep U05; L06 bank -> pool.
7. **06 Trigonometry** — Keep U06; bank -> pool.
8. **07 Transformations and Vectors** — Keep U07; split Vector Geometry if study load remains excessive.
9. **08 Probability** — Keep U08; fix random vs independent and use dependency examples.
10. **09 Statistics** — Keep U09; interpolation/outlier rules become conditional.
11. **10 Exam Mode** — Generate Core/Extended-appropriate sets from tagged pools. Official track is separate from learner route.


### Reglas pedagógicas específicas de GCSE/IGCSE Mathematics
- `Core/Extended` oficial y `from_zero/standard/excellence` pedagógico son ejes independientes.
- El alumno con poca base debe poder estudiar un objetivo Extended con más scaffolding; no ocultarlo solo por perfil de apoyo.
- Los Exercise Banks gigantes son repositorios: seleccionar 5–12 ejercicios por sesión según skills y rendimiento.
- La práctica mixta debe obligar a decidir el método. Después de varios temas, evitar bloques de 30 ejercicios idénticos seguidos.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `U01_Number / 03_Ordering_and_the_Four_Operations` | "A difference is always larger minus smaller and never negative". | Distinguir subtraction a-b de absolute difference \|a-b\|. | Ejemplos incluyen diferencia algebraica negativa y distancia absoluta. |
| P1 | `functions / inverse` | Inverse algorithm without one-to-one condition. | Check one-to-one or restrict domain before inverse function. | Ejemplo con quadratic requires domain restriction. |
| P1 | `U08_Probability / 02_Relative_and_Expected_Frequency` | Random = independent trials. | Separate random/unpredictable under model from independent. Use sampling without replacement as counterexample. | Definitions not conflated. |
| P1 | `calculus/graphs/extrema where present` | "A maximum or minimum always has zero gradient". | Acotar a interior differentiable extrema; boundary/corner counterexample in Advanced note. | No universal. |
| P2 | `statistics / interpolation` | Interpolation called reliable. | Use "generally safer than extrapolation if relationship remains appropriate". | No guarantee language. |
| P2 | `statistics / outliers` | Protocol automatic exclude outlier. | Investigate measurement error/subpopulation/legitimate value before exclusion. | Decision flow replaces automatic removal. |
| P2 | `algebra / fractional equations` | Clearing denominators said to create extraneous roots. | State domain restrictions first; loss of restrictions is the practical risk. | Solutions are checked against original domain. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- `gcse_mates__U07_Transformations_and_Vectors / 04_Vector_Geometry.json` — 9415 words / 1 h = 9415 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `gcse_mates__U02_Algebra_and_Graphs / 21_Exercise_Bank_Cambridge_IGCSE.json` — 92935 words / 2.5 h = 37174 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `gcse_mates__U01_Number / 18_Exercise_Bank_Cambridge_IGCSE.json` — 66209 words / 2.5 h = 26484 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `gcse_mates__U05_Mensuration / 06_Exercise_Bank_Cambridge_IGCSE.json` — 18028 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `gcse_mates__U04_Geometry / 09_Exercise_Bank_Cambridge_IGCSE.json` — 20380 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `gcse_mates__U09_Statistics` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U07_Transformations_and_Vectors` | `04_Vector_Geometry.json` | medium | `content_overload` | 9415 words / 1 h = 9415 words/h |
| `gcse_mates__U07_Transformations_and_Vectors` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U02_Algebra_and_Graphs` | `21_Exercise_Bank_Cambridge_IGCSE.json` | high | `content_overload` | 92935 words / 2.5 h = 37174 words/h |
| `gcse_mates__U02_Algebra_and_Graphs` | `21_Exercise_Bank_Cambridge_IGCSE.json` | high | `very_long_lesson` | 92935 words |
| `gcse_mates__U02_Algebra_and_Graphs` | `21_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U01_Number` | `18_Exercise_Bank_Cambridge_IGCSE.json` | high | `content_overload` | 66209 words / 2.5 h = 26484 words/h |
| `gcse_mates__U01_Number` | `18_Exercise_Bank_Cambridge_IGCSE.json` | high | `very_long_lesson` | 66209 words |
| `gcse_mates__U01_Number` | `18_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U05_Mensuration` | `06_Exercise_Bank_Cambridge_IGCSE.json` | high | `very_long_lesson` | 18028 words |
| `gcse_mates__U05_Mensuration` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U08_Probability` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U06_Trigonometry` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U03_Coordinate_Geometry` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_mates__U04_Geometry` | `09_Exercise_Bank_Cambridge_IGCSE.json` | high | `very_long_lesson` | 20380 words |
| `gcse_mates__U04_Geometry` | `09_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |


Archivo con todas las filas exactas: `../qa/gcse_mates_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=gcse_mates`.
2. Resolver el CSV `qa/gcse_mates_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
