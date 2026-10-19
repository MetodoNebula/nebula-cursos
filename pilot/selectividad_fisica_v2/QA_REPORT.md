# QA_REPORT.md — selectividad_fisica (piloto v2) — Auditoría v2

Regenerado tras auditoría v2 completa (6 fases). Fecha: 2026-10-19.

## 1. Integridad estructural
| Comprobacion | Resultado |
|---|---|
| Lecciones totales | **88** |
| `canonical_lesson_id` unicos | **88** / 88 (duplicados: 0) |
| Formato SELFIS::\<unit\>::\<slug\> | **100%** |
| `content_version` presente | **100%** |
| JSON valido en los 9 bundles | **si** |

## 2. Referencias
- `objective_ids` sin resolver: **0**
- `concept_ids` sin resolver dentro de la misma leccion: **15** (preexistentes: conceptos introducidos en una leccion anterior de la unidad y reutilizados despues; no bloqueantes).

## 3. MCQ
- MCQ sin opcion correcta valida (bundles): **0**
- MCQ sin opcion correcta valida (checkpoints): **0**
- MCQ sin opcion correcta valida (exam_mode): **0**
- Distractores sin `why_wrong`: **0 / 1635**

## 4. Campos obligatorios
- `title` vacios: **0**
- `theory_blocks` vacios: **0**
- `objectives` vacios: **0**

## 5. Orden esencial-primero (scope)
- Bloques con scope asignado: **731 / 731** (100%)
- Distribucion: 686 CORE / 45 ADVANCED
- Violaciones MEZCLA: **0**

## 6. Visuales (SVG)
- Diagramas SVG en el curso: **241** (todas las lecciones cubiertas).
- XML valido: **241 / 241** (100%)
- Font-size en porcentaje: **0**
- Colores fuera de paleta base: 31 unicos (paleta extendida consistente, no errores).

## 7. Capa de datos
- `KNOWLEDGE_GRAPH.json`: 88 nodos, 156 aristas.
- `unit_checkpoints.json`: 31 checkpoints (0 referencias rotas).
- `diagnostic.json`: items diagnosticos con ejes (0 referencias rotas).
- `exam_mode.json`: 8/8 unidades cubiertas, topic/mixed/timed/parciales/completos (0 referencias rotas).
- `schema_v2` en las 88 lecciones, con rutas recomendadas dentro de `learning_design`.

## 8. Correcciones aplicadas en esta auditoría
| Hallazgo | Severidad | Acción |
|----------|-----------|--------|
| Nuclear: Z>83→Z>82 (28 instancias en todo el bundle) | P0 | FIXED |
| Cuántica L02: fracciones ambiguas en exercises[0] | P1 | FIXED (2 instancias) |
| Relatividad L05: conservación del momento en pares | P1 | FIXED (nota añadida) |

## 9. Gates de validacion
| Gate | Estado |
|------|--------|
| JSON valido | PASS |
| canonical_lesson_id unicos | PASS |
| 0 MEZCLA | PASS |
| MCQ correct key | PASS |
| SVG XML valido | PASS |
| Campos obligatorios | PASS |
| **Global** | **100% PASS** |
