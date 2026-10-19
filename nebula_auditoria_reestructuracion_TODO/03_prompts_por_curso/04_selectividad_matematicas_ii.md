# PILOTO DE REESTRUCTURACIÓN — SELECTIVIDAD MATEMÁTICAS II

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = SELECTIVIDAD_MATEMATICAS
```

No modifiques otros cursos.

## DOCUMENTOS OBLIGATORIOS

Lee:

```text
00_MASTER_IMPLEMENTATION_SPEC.md
AGENT_EXECUTION_INSTRUCTIONS.md
AUDITORIA_REESTRUCTURACION_COMPLETA.md
semantic_change_ledger.csv
semantic_change_ledger.json
target_lesson_schema.example.json
cursos/03_SELECTIVIDAD_MATEMATICAS.md
```

y el curso original.

## OBJETIVO

El curso debe progresar desde:

```text
comprender
→ ejecutar
→ reconocer
→ combinar
→ seleccionar estrategia
→ resolver examen
→ transferir
```

Implementa:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

sin duplicar la teoría.

## FASE 0

Genera `AUDIT_BEFORE.md`.

Incluye inventario, carga, secuencia, prerrequisitos, errores, cálculos, MCQ, soluciones, summaries, flashcards y ejercicio tipo examen.

## AUDITORÍA MATEMÁTICA PRIORITARIA

Revisa:

- dominio;
- continuidad;
- límites;
- derivadas;
- optimización;
- integrales;
- matrices;
- sistemas;
- vectores;
- geometría;
- probabilidad;
- condiciones de teoremas;
- equivalencias;
- condiciones necesarias y suficientes;
- casos degenerados;
- signos;
- extremos;
- puntos de inflexión;
- hipótesis de L'Hôpital y reglas similares.

Cualquier afirmación “si X entonces necesariamente Y” debe revisarse especialmente.

## CLAIMS

Clasifica:

```text
EXACT
DEFINITION
THEOREM
MODEL
HEURISTIC
SPECIAL_CASE
EXAM_CONVENTION
```

Guarda hipótesis y condiciones de uso.

## ARQUITECTURA DE LECCIÓN

```text
prerequisite_check
→ motivating problem
→ concept
→ theorem/rule + conditions
→ worked example
→ faded example
→ micro-check
→ standard practice
→ exam application
→ advanced
→ counterexample
→ summary
→ checkpoint
```

## PRERREQUISITOS

Mapea:

- álgebra;
- ecuaciones;
- trigonometría;
- funciones;
- operaciones con matrices;
- vectores;
- probabilidad previa.

## EXCELLENCE

Debe incluir:

- contraejemplos;
- condiciones de teoremas;
- casos límite;
- selección de estrategia;
- demostraciones cortas cuando aporten comprensión;
- problemas combinados;
- problemas donde no se indique el método.

## EJERCICIOS

```text
L1 reconocimiento
L2 aplicación
L3 combinación
L4 examen / estrategia
L5 transferencia
```

Separar:

```text
difficulty
conceptual_depth
cognitive_level
```

## EXAM MODE

Incluye preguntas donde no se diga:

```text
"utiliza derivadas"
"calcula mediante una integral"
"aplica..."
```

cuando elegir la herramienta sea parte de la competencia.

## CONSISTENCIA

Revisa:

```text
theory
summary
flashcards
MCQ
solutions
feedback
```

No permitir contradicciones.

## ENTREGABLES

```text
pilot/selectividad_matematicas_v2/
AUDIT_BEFORE.md
AUDIT_AFTER.md
CHANGELOG.md
PILOT_COMPARISON.md
KNOWLEDGE_GRAPH.json
QA_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md si procede
FRONTEND_CHANGES.md si procede
```

## DEFINITION OF DONE

```text
0 P0 conocidos
0 resultados numéricos imposibles
0 teoremas sin condiciones esenciales
0 contradicciones
rutas pedagógicas implementadas
prerrequisitos mapeados
checkpoints disponibles
Exam Mode disponible
JSON válido
frontend funcional
QA completado
```

Implementa la nueva versión.
