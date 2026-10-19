# PILOTO DE REESTRUCTURACIÓN — ESO FÍSICA Y QUÍMICA FOUNDATIONS

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = ESO_FISICA_QUIMICA_FOUNDATIONS
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
cursos/06_ESO_FISICA_QUIMICA_FOUNDATIONS.md
```

y el contenido original.

## OBJETIVO PRINCIPAL

Convertir este curso en la capa de fundamentos reutilizable para cursos posteriores.

Las unidades deben ser:

```text
cortas
reutilizables
referenciables
diagnosticables
```

Cada microlección debería poder llamarse desde otro curso como remediation.

## FASE 0

Genera `AUDIT_BEFORE.md`.

## FUNDAMENTOS PRIORITARIOS

Optimiza especialmente:

- unidades;
- conversiones;
- notación científica;
- proporcionalidad;
- despeje;
- gráficas;
- vectores básicos;
- modelo de partículas;
- mol básico;
- ecuaciones químicas;
- magnitudes físicas;
- masa, volumen y densidad;
- energía básica.

## CORRECCIÓN CONCEPTUAL

Revisa especialmente contradicciones conocidas en:

- cambios de estado;
- modelo cinético;
- temperatura;
- energía cinética/potencial;
- definiciones básicas;
- fuerza;
- energía;
- electricidad;
- química básica.

## CLAIMS

Clasifica:

```text
EXACT
DEFINITION
MODEL
APPROXIMATION
HEURISTIC
SPECIAL_CASE
```

Evita reglas absolutas falsas.

## ARQUITECTURA DE MICRO-LECCIÓN

```text
prerequisite_check
→ intuition
→ core concept
→ worked example
→ micro-check
→ short practice
→ misconception
→ summary
```

Las microlecciones no deben convertirse en capítulos largos.

## RUTAS

Permite:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

pero mantén el objetivo de Foundations: accesibilidad y reutilización.

## MAPA DE SKILLS

Genera:

```text
FOUNDATION_SKILLS_GRAPH.json
```

Debe permitir a otros cursos saber exactamente qué microlección invocar cuando un alumno falla una habilidad básica.

## EJERCICIOS

Clasifica L1–L4 principalmente; L5 solo cuando aporte valor.

## ENTREGABLES

```text
pilot/eso_fisica_quimica_foundations_v2/
AUDIT_BEFORE.md
AUDIT_AFTER.md
CHANGELOG.md
PILOT_COMPARISON.md
FOUNDATION_SKILLS_GRAPH.json
KNOWLEDGE_GRAPH.json
QA_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md si procede
FRONTEND_CHANGES.md si procede
```

## DEFINITION OF DONE

```text
0 P0 conocidos
microlecciones reutilizables
skills mapeadas
contradicciones corregidas
rutas disponibles
JSON válido
frontend funcional
QA completado
```

No copies contenido entero de cursos superiores dentro de Foundations.

Implementa la nueva versión.
