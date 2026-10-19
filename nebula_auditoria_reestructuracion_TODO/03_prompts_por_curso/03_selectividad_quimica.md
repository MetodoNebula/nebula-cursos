# PILOTO DE REESTRUCTURACIÓN — SELECTIVIDAD QUÍMICA

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = SELECTIVIDAD_QUIMICA
```

No modifiques ningún otro curso.

## DOCUMENTOS OBLIGATORIOS

Lee completamente:

```text
00_MASTER_IMPLEMENTATION_SPEC.md
AGENT_EXECUTION_INSTRUCTIONS.md
AUDITORIA_REESTRUCTURACION_COMPLETA.md
semantic_change_ledger.csv
semantic_change_ledger.json
target_lesson_schema.example.json
cursos/02_SELECTIVIDAD_QUIMICA.md
```

y el curso original del bundle.

## OBJETIVO

Transformar el curso para soportar:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

sobre una única fuente conceptual.

## FASE 0

Genera `AUDIT_BEFORE.md` con inventario, P0/P1/P2, estructura, carga, cálculos, ejercicios, duplicados, summaries, flashcards, MCQ y feedback.

## FOCO CIENTÍFICO

Este curso debe diferenciar correctamente:

```text
ley exacta
modelo
aproximación
regla operativa
convención de examen
caso especial
```

Revisa especialmente:

- equilibrio químico;
- ácido–base;
- ácidos polipróticos;
- aproximaciones de pH;
- valoraciones;
- solubilidad;
- redox;
- electroquímica;
- termoquímica;
- cinética;
- estructura atómica;
- enlace;
- estequiometría;
- unidades;
- cifras significativas;
- redondeos.

## CLAIMS

Clasifica como:

```text
EXACT
DEFINITION
MODEL
APPROXIMATION
HEURISTIC
EXAM_CONVENTION
SPECIAL_CASE
```

Cuando una aproximación sea válida para PAU pero no universal, debe conservar explícitamente esa condición.

## CONSISTENCIA

Toda corrección debe propagarse a:

```text
theory
summary
flashcards
MCQ
worked_examples
solutions
feedback
```

No permitas que teoría y resumen enseñen versiones distintas.

## PRERREQUISITOS

Mapea:

- proporciones;
- logaritmos;
- potencias;
- notación científica;
- ecuaciones;
- unidades;
- despejes.

Usa microcontenidos Foundation como remediation, sin convertir el curso en matemáticas básicas.

## ARQUITECTURA DE LECCIÓN

```text
prerequisite_check
→ intuition
→ concept
→ assumptions/conditions
→ worked_example
→ faded_example
→ micro_check
→ standard practice
→ exam application
→ advanced
→ misconception
→ summary
→ checkpoint
```

## EJERCICIOS

Progresión:

```text
identificar
→ sustituir
→ calcular
→ combinar
→ decidir estrategia
→ problema completo PAU
→ challenge
```

Niveles L1–L5.

Separa:

```text
difficulty
conceptual_depth
cognitive_level
```

## VALIDACIÓN NUMÉRICA

Recalcula independientemente.

Comprueba, cuando corresponda:

```text
masa
carga
átomos
electrones
unidades
orden de magnitud
```

## FEEDBACK

Identifica errores específicos, por ejemplo:

- balanceo;
- signo;
- estequiometría;
- unidades;
- elección de equilibrio;
- aproximación inválida.

## EVALUACIÓN

Crea:

- diagnóstico;
- checkpoints;
- spaced retrieval;
- mixed practice;
- Exam Mode;
- mocks.

## ENTREGABLES

```text
pilot/selectividad_quimica_v2/
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
0 contradicciones conocidas
0 cálculos imposibles conocidos
aproximaciones correctamente etiquetadas
prerrequisitos mapeados
rutas pedagógicas implementadas
checkpoints implementados
Exam Mode implementado
JSON válido
frontend funcional
QA completado
```

Implementa el curso v2. No te limites a recomendar.
