# PILOTO DE REESTRUCTURACIÓN — SELECTIVIDAD FÍSICA

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = SELECTIVIDAD_FISICA
```

No modifiques ningún otro curso.

## DOCUMENTOS OBLIGATORIOS

Antes de realizar cambios debes leer completamente:

```text
00_MASTER_IMPLEMENTATION_SPEC.md
AGENT_EXECUTION_INSTRUCTIONS.md
AUDITORIA_REESTRUCTURACION_COMPLETA.md
semantic_change_ledger.csv
semantic_change_ledger.json
target_lesson_schema.example.json
cursos/01_SELECTIVIDAD_FISICA.md
```

y localizar dentro del bundle original todos los archivos correspondientes a Selectividad Física.

La auditoría específica y el ledger constituyen un backlog obligatorio, no recomendaciones opcionales.

## OBJETIVO

Transforma el curso para que funcione para:

- alumno con poca base;
- alumno estándar;
- alumno que busca nota alta;
- alumno que busca excelencia;
- alumno que únicamente necesita repasar.

Implementa la arquitectura:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

sin duplicar la fuente conceptual.

## PROTECCIÓN DEL ORIGINAL

Conserva intacta la versión original.

Trabaja sobre una copia:

```text
original/selectividad_fisica/
pilot/selectividad_fisica_v2/
```

## FASE 0 — INVENTARIO

Antes de modificar contenido genera:

```text
AUDIT_BEFORE.md
```

Incluye:

- número de unidades;
- número de lecciones;
- número de ejercicios;
- worked examples;
- preguntas de evaluación;
- estructura actual;
- duración estimada;
- lecciones largas;
- duplicados;
- P0/P1/P2;
- problemas de secuencia;
- prerrequisitos;
- precisión científica;
- claims absolutos;
- summaries;
- flashcards;
- MCQ;
- soluciones;
- feedback.

## CORRECCIÓN CIENTÍFICA

Debes auditar especialmente:

- inducción electromagnética;
- flujo magnético;
- condiciones de aplicación de fórmulas;
- solenoides;
- campo y potencial;
- física cuántica;
- criterios dimensionales;
- relatividad;
- rozamiento;
- aproximaciones;
- signos;
- unidades;
- vectores;
- conservación de energía;
- interpretación gráfica.

Cualquier regla que solo sea válida bajo determinadas condiciones debe almacenar dichas condiciones.

Clasifica claims como:

```text
EXACT
DEFINITION
MODEL
APPROXIMATION
HEURISTIC
EXAM_CONVENTION
SPECIAL_CASE
```

Ejemplo: no presentar `B = μnI` como ley universal; registrar las condiciones del modelo.

## CONSISTENCIA

Cada corrección debe propagarse a:

```text
theory
summary
flashcards
MCQ
worked_examples
solutions
feedback
objectives
```

No debe quedar ninguna contradicción entre representaciones.

Recalcula independientemente los resultados numéricos.

## MAPA DE CONOCIMIENTO

Para cada lección identifica:

```text
required_prerequisites
recommended_prerequisites
skills_used
skills_created
```

Mapea especialmente:

- álgebra;
- trigonometría;
- vectores;
- unidades;
- lectura de gráficas.

Usa remediation just-in-time. No conviertas Selectividad Física en un curso de matemáticas básicas.

## ARQUITECTURA PEDAGÓGICA

Cada lección debe tender a:

```text
1. prerequisite_check
2. intuition / motivating_problem
3. learning_objectives
4. core_concept
5. conditions_and_scope
6. worked_example
7. faded_example
8. micro_check
9. standard_explanation
10. standard_practice
11. exam_application
12. advanced_extension
13. misconception_or_counterexample
14. summary
15. checkpoint
16. next_step
```

Atomiza lecciones excesivamente largas.

Referencia aproximada:

```text
simple concept: 10–20 min
normal concept: 20–35 min
complex concept: 30–45 min
```

## EJERCICIOS

Clasifica:

```text
L1 = reconocimiento
L2 = aplicación directa
L3 = combinación
L4 = nivel Selectividad / selección de estrategia
L5 = transferencia / challenge
```

Separa:

```text
difficulty
conceptual_depth
cognitive_level
```

Los problemas L4/L5 no deben indicar qué herramienta usar si elegir el método forma parte del aprendizaje.

## WORKED EXAMPLES

Usa la progresión:

```text
worked example
→ faded example
→ independent exercise
```

## CHECKPOINTS Y DIAGNÓSTICO

Crea diagnóstico inicial por habilidades, no por etiquetas globales.

Ejemplo:

```text
Vectores 42%
Álgebra 85%
Cinemática 71%
Campos 35%
Ondas 68%
```

Introduce checkpoints cada pocas lecciones con resultados:

```text
needs_support
ready
mastered
```

## EXAM MODE

Crea:

```text
topic questions
mixed questions
timed questions
partial mock exams
full mock exams
```

Reducir scaffolding en esta capa.

## FEEDBACK

Nunca responder solo “Incorrecto”.

El feedback debe identificar:

```text
error_type
misconception
hint
next_action
```

cuando sea posible.

## SUMMARIES Y FLASHCARDS

Un summary no puede introducir teoría nueva ni convertir una regla condicionada en universal.

Una flashcard nunca debe:

- convertir una aproximación en ley;
- convertir condición necesaria en suficiente;
- eliminar hipótesis esenciales.

## MCQ

Validar:

- una respuesta correcta;
- respuesta matemáticamente posible;
- explicación coherente;
- distractores plausibles;
- `why_wrong` coherente;
- ausencia de contradicción con `correct_answer`.

## SCHEMA

Migra progresivamente hacia:

```text
target_lesson_schema.example.json
```

Mantén compatibilidad con el frontend cuando sea razonable.

Si el schema cambia, adapta parser o introduce compatibilidad.

## VALIDACIÓN FINAL

Genera:

```text
AUDIT_AFTER.md
PILOT_COMPARISON.md
CHANGELOG.md
KNOWLEDGE_GRAPH.json
QA_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md     si procede
FRONTEND_CHANGES.md     si procede
```

`PILOT_COMPARISON.md` debe comparar, entre otras:

- lecciones;
- lecciones >45 min;
- claims sin condiciones;
- P0;
- P1;
- worked examples;
- faded examples;
- checkpoints;
- preguntas L4;
- challenges L5;
- prerequisite links;
- MCQ inconsistentes.

## DEFINITION OF DONE

No terminar hasta cumplir:

```text
0 errores P0 conocidos
0 contradicciones conocidas
0 respuestas numéricas imposibles
0 claves MCQ incorrectas
prerrequisitos mapeados
rutas pedagógicas implementadas
checkpoints implementados
Exam Mode disponible
JSON válido
IDs únicos
referencias válidas
frontend funcional
QA final completado
```

No produzcas únicamente recomendaciones.

IMPLEMENTA LA NUEVA VERSIÓN DEL CURSO y detente después de terminar y validar SELECTIVIDAD_FISICA.
