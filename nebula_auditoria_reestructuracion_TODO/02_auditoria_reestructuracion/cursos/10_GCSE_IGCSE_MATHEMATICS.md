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
