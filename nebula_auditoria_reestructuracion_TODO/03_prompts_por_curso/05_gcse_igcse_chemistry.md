# PILOTO DE REESTRUCTURACIÓN — GCSE / IGCSE CHEMISTRY

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = GCSE_IGCSE_CHEMISTRY
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
cursos/09_GCSE_IGCSE_CHEMISTRY.md
```

y el contenido original.

## REGLA CRÍTICA

Separa siempre:

```text
official_track = Core / Extended
```

de:

```text
learning_route = DESDE_CERO / STANDARD / EXCELLENCE / FAST_REVIEW
```

No son la misma dimensión.

## FASE 0

Genera `AUDIT_BEFORE.md` antes de implementar.

## AUDITORÍA CIENTÍFICA

Revisa especialmente:

- acid/base definitions;
- ionic equations;
- electrolysis;
- molten vs aqueous electrolysis;
- equilibrium;
- energetic changes;
- bonding;
- structure;
- stoichiometry;
- mole calculations;
- redox;
- rates;
- organic chemistry;
- qualitative analysis;
- unidades y cálculos.

Las definiciones simplificadas deben ser adecuadas al syllabus sin convertirse en falsedades.

## CLAIMS

Usa:

```text
EXACT
DEFINITION
MODEL
APPROXIMATION
HEURISTIC
EXAM_CONVENTION
SPECIAL_CASE
```

## ESTRUCTURA DE LECCIÓN

```text
prerequisite_check
→ intuition
→ model/definition
→ conditions
→ worked example
→ faded example
→ guided practice
→ Core/Extended application
→ exam question
→ advanced
→ misconception
→ summary
→ checkpoint
```

## PRERREQUISITOS

Mapea:

- proporciones;
- masa relativa;
- ecuaciones;
- unidades;
- notación científica;
- interpretación de gráficos.

## EJERCICIOS

Etiqueta por:

```text
topic
skill
official_track
difficulty
conceptual_depth
cognitive_level
learning_route
```

Niveles L1–L5.

## QA

Comprueba cálculos, ecuaciones, balanceos, cargas, unidades, MCQ, distractores y feedback.

## EVALUACIÓN

Crea:

- diagnóstico;
- checkpoints;
- mixed practice;
- spaced retrieval;
- Exam Mode;
- mock exams.

## ENTREGABLES

```text
pilot/gcse_igcse_chemistry_v2/
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
Core/Extended correctamente etiquetado
0 contradicciones
rutas pedagógicas disponibles
prerrequisitos mapeados
checkpoints disponibles
Exam Mode disponible
JSON válido
frontend funcional
QA completado
```

Implementa cambios reales.
