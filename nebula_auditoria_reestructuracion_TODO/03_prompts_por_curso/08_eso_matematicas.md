# PILOTO DE REESTRUCTURACIÓN — ESO MATEMÁTICAS

## CURSO OBJETIVO

Trabaja exclusivamente sobre:

```text
CURSO_OBJETIVO = ESO_MATEMATICAS
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
cursos/05_ESO_MATEMATICAS.md
```

y el curso original.

## OBJETIVO PRINCIPAL

Este curso requiere una reestructuración curricular importante.

NO trates todo el contenido existente como ESO obligatorio.

Clasifica cada contenido como:

```text
FOUNDATION
ESO_CORE
ESO_EXTENSION
BACHILLERATO_BRIDGE
```

## ARQUITECTURA CURRICULAR OBJETIVO

Aproximadamente:

```text
A. Foundations
B. ESO Core — Álgebra
C. ESO Core — Funciones
D. ESO Core — Geometría
E. ESO Core — Estadística y probabilidad
F. ESO Extension
G. Bachillerato Bridge
```

Contenidos como límites, derivadas, complejos, determinadas distribuciones avanzadas u otros claramente post-ESO no deben desaparecer, pero deben moverse a extensión o puente a Bachillerato.

## NO CONFUNDIR

```text
curriculum_band
```

con:

```text
learning_route
```

Dentro de cada banda curricular debe poder existir:

```text
DESDE_CERO
STANDARD
EXCELLENCE
FAST_REVIEW
```

## FASE 0

Genera `AUDIT_BEFORE.md` e identifica:

- contenidos fuera de nivel;
- contenidos obligatorios;
- contenidos de extensión;
- prerrequisitos;
- duplicados;
- errores;
- lecciones demasiado grandes;
- exercise banks;
- gaps.

## FOUNDATIONS

Presta especial atención a:

- fracciones;
- potencias;
- raíces;
- porcentajes;
- proporciones;
- álgebra elemental;
- ecuaciones;
- lectura de gráficas;
- unidades.

Usa remediation just-in-time.

## PEDAGOGÍA

Cada lección debe tender a:

```text
prerequisite_check
→ intuition
→ concept
→ worked example
→ faded example
→ micro-check
→ practice
→ application
→ challenge
→ misconception
→ summary
→ checkpoint
```

## EJERCICIOS

```text
L1 reconocimiento
L2 aplicación directa
L3 combinación
L4 aplicación no rutinaria
L5 challenge
```

## MAPA DE CONOCIMIENTO

Genera dependencias claras entre:

- aritmética;
- álgebra;
- funciones;
- geometría;
- estadística;
- probabilidad;
- contenidos bridge.

Las lecciones avanzadas no deben aparecer como continuación obligatoria del núcleo ESO.

## EVALUACIÓN

Introduce:

- diagnóstico;
- checkpoints;
- recuperación dirigida;
- mixed practice;
- repaso espaciado;
- pruebas de unidad.

## ENTREGABLES

```text
pilot/eso_matematicas_v2/
AUDIT_BEFORE.md
AUDIT_AFTER.md
CHANGELOG.md
PILOT_COMPARISON.md
KNOWLEDGE_GRAPH.json
CURRICULUM_BAND_MAP.json
QA_REPORT.md
MIGRATION_NOTES.md
SCHEMA_MIGRATION.md si procede
FRONTEND_CHANGES.md si procede
```

## DEFINITION OF DONE

```text
0 P0 conocidos
contenido ESO correctamente separado
Bridge claramente identificado
rutas pedagógicas implementadas
prerrequisitos mapeados
checkpoints disponibles
JSON válido
frontend funcional
QA completado
```

Implementa la nueva versión.
