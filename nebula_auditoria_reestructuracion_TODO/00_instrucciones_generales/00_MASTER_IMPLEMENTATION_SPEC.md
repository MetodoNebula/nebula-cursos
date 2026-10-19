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
