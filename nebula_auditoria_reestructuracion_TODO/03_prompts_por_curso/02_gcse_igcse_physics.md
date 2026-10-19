# PILOTO DE REESTRUCTURACIÓN — GCSE / IGCSE PHYSICS

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = GCSE_IGCSE_PHYSICS
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
cursos/08_GCSE_IGCSE_PHYSICS.md
```

y localiza el curso original en el bundle.

## REGLA CRÍTICA

NO confundas:

```text
Cambridge Core / Extended
```

con:

```text
DESDE_CERO / STANDARD / EXCELLENCE / FAST_REVIEW
```

Son dimensiones distintas.

Modela por separado:

```text
official_track
learning_route
difficulty
conceptual_depth
cognitive_level
```

Un alumno con poca base puede necesitar aprender un objetivo Extended con mayor scaffolding.

## OBJETIVO

Crear un único curso adaptable para:

- poca base;
- nivel normal;
- nota alta;
- excelencia;
- repaso rápido.

Sin duplicar la fuente conceptual.

## FASE 0

Genera `AUDIT_BEFORE.md` con inventario, P0/P1/P2, carga, duplicados, secuenciación, prerrequisitos, MCQ, soluciones, feedback y coherencia Core/Extended.

## REVISIÓN CONCEPTUAL PRIORITARIA

Comprueba especialmente:

- definición de onda;
- ondas mecánicas;
- ondas electromagnéticas;
- propagación en vacío;
- modelo de partículas;
- cambios de estado;
- temperatura durante cambios de fase;
- energía cinética y potencial;
- electricidad;
- magnetismo;
- inducción;
- fuerzas;
- energía;
- unidades;
- condiciones de ecuaciones.

Corrige las contradicciones ya identificadas en la auditoría.

## CLAIMS

Clasifica:

```text
EXACT
DEFINITION
MODEL
APPROXIMATION
HEURISTIC
EXAM_CONVENTION
SPECIAL_CASE
```

Las simplificaciones pedagógicas nunca deben convertirse en falsedades.

## ARQUITECTURA DE LECCIÓN

Usa cuando proceda:

```text
prerequisite_check
→ intuition
→ core concept
→ conditions
→ worked example
→ faded example
→ micro-check
→ standard
→ Core/Extended application
→ exam question
→ advanced/challenge
→ misconception
→ summary
→ checkpoint
```

## PRERREQUISITOS

Mapea:

- álgebra;
- proporciones;
- unidades;
- gráficas;
- vectores básicos;
- notación científica.

Usa remediation just-in-time.

## EJERCICIOS

Etiqueta por:

```text
syllabus_topic
official_track
skill
difficulty
conceptual_depth
cognitive_level
learning_route
```

Niveles:

```text
L1 reconocimiento
L2 aplicación directa
L3 combinación
L4 examen / selección de estrategia
L5 transferencia / challenge
```

## CORE / EXTENDED

El syllabus oficial debe mantenerse correctamente etiquetado.

No ocultes contenido Extended simplemente porque el alumno esté en ruta DESDE_CERO.

No muestres como obligatorio Core contenido que sea exclusivamente Extended.

## WORKED EXAMPLES

Usa:

```text
worked example
→ faded example
→ independent exercise
```

## EVALUACIÓN

Introduce:

- diagnóstico por habilidades;
- checkpoints;
- recuperación dirigida;
- Exam Mode;
- mixed practice;
- mock exams.

## FEEDBACK

Evita “Incorrect”.

Devuelve feedback diagnóstico con:

```text
error_type
misconception
hint
next_action
```

cuando sea posible.

## QA

Comprueba:

- cálculos;
- unidades;
- definiciones;
- MCQ;
- claves;
- distractores;
- feedback;
- duplicados;
- IDs;
- referencias;
- compatibilidad frontend.

## ENTREGABLES

Genera:

```text
pilot/gcse_igcse_physics_v2/
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

No terminar hasta:

```text
0 P0 conocidos
0 contradicciones conocidas
Core/Extended correctamente separado
rutas pedagógicas disponibles
prerrequisitos mapeados
checkpoints disponibles
Exam Mode disponible
JSON válido
IDs únicos
referencias válidas
frontend funcional
QA completado
```

Implementa cambios reales. No produzcas solo recomendaciones.
