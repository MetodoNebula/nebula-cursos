# PILOTO DE REESTRUCTURACIÓN — GCSE / IGCSE MATHEMATICS

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = GCSE_IGCSE_MATHEMATICS
```

## DOCUMENTOS OBLIGATORIOS

Lee:

```text
00_MASTER_IMPLEMENTATION_SPEC.md
AGENT_EXECUTION_INSTRUCTIONS.md
AUDITORIA_REESTRUCTURACION_COMPLETA.md
semantic_change_ledger.csv
semantic_change_ledger.json
target_lesson_schema.example.json
cursos/10_GCSE_IGCSE_MATHEMATICS.md
```

y el bundle original.

## OBJETIVO ESPECIAL

Este curso debe probar especialmente el sistema:

```text
exercise_pool
```

Los bancos enormes de ejercicios NO deben mantenerse como lecciones lineales.

## FASE 0

Genera `AUDIT_BEFORE.md`.

Cuantifica:

- número de exercise banks;
- tamaño;
- palabras;
- ejercicios;
- duplicados;
- distribución de dificultad;
- Core/Extended;
- tipos de habilidad.

## CONVERSIÓN DE BANCOS

Convierte colecciones masivas en pools etiquetados por:

```text
topic
subskill
Core/Extended
difficulty
conceptual_depth
cognitive_level
exam_style
previous_error_type
```

La interfaz debe mostrar subconjuntos razonables, no cientos de ejercicios simultáneamente.

## REGLA CORE / EXTENDED

Mantén separadas:

```text
official_track
learning_route
```

Un alumno `DESDE_CERO` puede estudiar Extended con más apoyo.

## PEDAGOGÍA

Para cada competencia:

```text
worked example
→ faded example
→ independent practice
→ mixed practice
→ exam application
→ challenge
```

## AUDITORÍA MATEMÁTICA

Recalcula especialmente:

- probabilidades;
- porcentajes;
- estadística;
- regresión;
- geometría;
- álgebra;
- medidas;
- trigonometría;
- funciones.

Corrige cualquier MCQ cuyo resultado no coincida con sus opciones.

## EJERCICIOS

Niveles:

```text
L1 reconocimiento
L2 aplicación
L3 combinación
L4 exam strategy
L5 transfer
```

Separa `difficulty`, `conceptual_depth` y `cognitive_level`.

## RUTAS

Implementa:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

sin duplicar contenido.

## EVALUACIÓN

Añade:

- diagnóstico por habilidades;
- checkpoints;
- mixed practice;
- spaced retrieval;
- Exam Mode;
- mocks.

## ENTREGABLES

```text
pilot/gcse_igcse_mathematics_v2/
AUDIT_BEFORE.md
AUDIT_AFTER.md
CHANGELOG.md
PILOT_COMPARISON.md
KNOWLEDGE_GRAPH.json
QA_REPORT.md
EXERCISE_POOL_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md si procede
FRONTEND_CHANGES.md si procede
```

`PILOT_COMPARISON.md` debe comparar explícitamente tamaño y presentación de exercise banks antes/después.

## DEFINITION OF DONE

```text
0 P0 conocidos
0 MCQ numéricamente imposibles
exercise banks convertidos cuando proceda
Core/Extended separado de learning_route
rutas implementadas
checkpoints disponibles
Exam Mode disponible
JSON válido
frontend funcional
QA completado
```

Implementa la versión v2.
