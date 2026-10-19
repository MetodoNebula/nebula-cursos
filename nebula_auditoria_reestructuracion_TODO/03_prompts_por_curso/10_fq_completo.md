# REESTRUCTURACIÓN — FÍSICA Y QUÍMICA COMPLETO

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = FQ_COMPLETO
```

Este curso debe migrarse preferiblemente DESPUÉS de validar los cursos piloto anteriores.

## DOCUMENTOS OBLIGATORIOS

Lee:

```text
00_MASTER_IMPLEMENTATION_SPEC.md
AGENT_EXECUTION_INSTRUCTIONS.md
AUDITORIA_REESTRUCTURACION_COMPLETA.md
semantic_change_ledger.csv
semantic_change_ledger.json
target_lesson_schema.example.json
cursos/07_FQ_COMPLETO.md
```

Además, utiliza los resultados finales de pilotos anteriores si están disponibles.

## OBJETIVO PRINCIPAL

`fq_completo` NO debe continuar como una secuencia lineal gigantesca.

Debe convertirse progresivamente en:

```text
CANONICAL KNOWLEDGE CORPUS
```

del que puedan derivarse rutas como:

```text
Shared Foundations
4 ESO Physics
4 ESO Chemistry
1 Bach Physics
1 Bach Chemistry
```

y otras necesarias.

## REGLA ABSOLUTA

Un mismo concepto no debe mantenerse manualmente en varias versiones divergentes.

Identifica duplicados semánticos entre:

```text
fq_completo
eso_fisicaquimica
otros cursos relacionados
```

y establece una fuente canónica.

Las rutas deben referenciar contenido canónico cuando sea posible, no copiarlo.

## FASE 0 — INVENTARIO PROFUNDO

Genera `AUDIT_BEFORE.md`.

Inventaría:

- todas las unidades;
- todas las lecciones;
- conceptos;
- duplicados;
- variantes;
- niveles curriculares;
- skills;
- ejercicios;
- summaries;
- flashcards;
- MCQ;
- P0/P1/P2;
- divergencias entre versiones.

## TAREAS OBLIGATORIAS

1. inventariar las lecciones actuales;
2. detectar duplicados;
3. detectar divergencias;
4. identificar contenido canónico;
5. construir knowledge graph;
6. separar nivel curricular;
7. separar ruta pedagógica;
8. convertir bancos masivos en exercise pools;
9. corregir P0/P1;
10. eliminar inconsistencias de feedback;
11. crear mecanismos de referencia/reutilización.

## MODELO OBJETIVO

El corpus debe poder responder:

```text
¿Qué es este concepto?
¿En qué cursos aparece?
¿Con qué profundidad?
¿Qué prerrequisitos requiere?
¿Qué ejercicios lo evalúan?
¿Qué rutas pedagógicas puede mostrar la web?
¿Qué claims son exactos, modelos o aproximaciones?
```

## DIMENSIONES SEPARADAS

Modela por separado:

```text
curriculum_band
course_route
learning_route
difficulty
conceptual_depth
cognitive_level
```

No mezcles nivel curricular con dificultad.

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

Guarda condiciones de validez.

## PEDAGOGÍA

La fuente canónica debe permitir renderizar:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

sin mantener cuatro copias de la teoría.

## EJERCICIOS

Convierte grandes bancos en:

```text
exercise_pool
```

etiquetados por:

```text
skill
topic
curriculum_band
difficulty
conceptual_depth
cognitive_level
exam_style
```

## DUPLICADOS

Para cada duplicado semántico registra:

```text
canonical_id
duplicate_ids
differences
chosen_version
merged_content
deprecated_references
```

No elimines contenido hasta asegurar que no quedan referencias rotas.

## COMPATIBILIDAD

No destruyas las rutas existentes antes de validar la migración.

Usa adaptadores o compatibilidad transitoria cuando sea necesario.

## ENTREGABLES

Genera:

```text
pilot/fq_completo_v2/

AUDIT_BEFORE.md
AUDIT_AFTER.md
CHANGELOG.md
PILOT_COMPARISON.md
KNOWLEDGE_GRAPH.json
CANONICAL_CONTENT_MAP.json
DUPLICATE_RESOLUTION.md
COURSE_ROUTE_MAP.json
QA_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md
FRONTEND_CHANGES.md si procede
```

## VALIDACIÓN

Comprueba:

- contenido científico;
- duplicados;
- referencias;
- IDs;
- rutas;
- schema;
- claims;
- exercise pools;
- frontend;
- backwards compatibility;
- ausencia de contradicciones.

## DEFINITION OF DONE

```text
0 P0 conocidos
fuente canónica definida
duplicados críticos resueltos
rutas curriculares definidas
learning routes separadas
knowledge graph generado
exercise pools creados cuando proceda
JSON válido
referencias válidas
frontend funcional
QA completado
```

El objetivo NO es simplemente mejorar `fq_completo`.

El objetivo es transformarlo en la fuente canónica reutilizable de Física y Química de Nebula.

Implementa la migración real.
