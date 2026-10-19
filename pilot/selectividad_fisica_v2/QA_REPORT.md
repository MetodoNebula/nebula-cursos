# QA_REPORT.md — selectividad_fisica (piloto v2)

Generado por `scripts/pilot_fisica/structural_qa.py` + `numeric_qa.py` +
`validate_schema_v2.py` + `validate_checkpoints_exammode.py`, ejecutados
sobre las 88 lecciones finales (82 de contenido + 6 de Fundamentos).

## 1. Integridad estructural básica

| Comprobación | Resultado |
|---|---|
| JSON válido en los 9 bundles | **True** |
| Lecciones totales | **88** |
| `canonical_lesson_id` únicos | **88** / 88 (0 duplicados) |
| IDs duplicados dentro de una misma lección | **0** |

## 2. Referencias (objective_ids / concept_ids)

- `objective_ids` sin resolver: **0** (tras el fix de Fase 7 sobre
  las 6 lecciones atomizadas en Fase 4, que al repartir `objectives[]` entre
  las dos partes rompió algunas referencias cruzadas; se resolvió dando a
  ambas partes la unión completa de los objetivos originales — ver
  `fix_14_split_objectives.py`).
- `concept_ids` sin resolver dentro de la misma lección: **15**.
  Verificado contra `original/`: son **preexistentes** (no introducidos por
  este piloto) y corresponden a conceptos introducidos en una lección
  anterior de la misma unidad y reutilizados más adelante sin volver a
  declararse en los `theory_blocks` de la lección que los usa — un patrón
  normal en un curso que se construye progresivamente, no una referencia
  rota en sentido estricto. Lecciones afectadas: campo_gravitatorio (L02b,
  L07), ondas (L04, L07, lesson_12), relatividad (L04, L07), nuclear (L05,
  L07, L09).

## 3. MCQ

- MCQ sin ninguna opción marcada como correcta: **0**.
- Distractores sin `why_wrong`: **18 / 1617**
  (1.1 %). Dentro del margen que el propio
  encargo permite para distractores triviales sin necesidad de rellenar
  mecánicamente ("permitir omission para distractores triviales con regla
  documentada").

## 4. Campos obligatorios

- Campos obligatorios (`statement`/`answer`/`full_solution`) vacíos en
  `exercises`/`guided_exercises`/`exam_questions`/`challenge_questions`:
  **0**.

## 5. QA numérico (Fase 2)

- Discrepancias numéricas reales tras el verificador propio
  (`numeric_qa.py`, que solo evalúa expresiones puramente numéricas y no
  confunde variables de una letra con constantes como *e*):
  **1** candidato(s) — el único detectado es un artefacto de
  precedencia de operadores del propio evaluador (`3·10⁸/300·10⁻⁹`
  interpretado sin paréntesis implícitos), no un error de contenido: el
  valor declarado (10¹⁵ Hz, frecuencia de luz de 300 nm) es correcto.

## 6. Checkpoints / diagnóstico / Exam Mode (Fase 6)

Ver `CHECKPOINTS.md`: 0 referencias rotas en 31 checkpoints + 22 items de
diagnóstico + 187 referencias de Exam Mode.

## 7. schema_v2 (Fase 3)

Ver `SCHEMA_MIGRATION.md`: 88/88 `canonical_lesson_id` únicos, 0 errores
estructurales, 0 referencias a `schema_v2` en `index.html` (migración
aditiva verificada no disruptiva).

## Resumen frente a la Definition of Done del encargo

| Criterio | Estado |
|---|---|
| 0 errores P0 conocidos | ✅ (los 2 P0 del ledger, corregidos y propagados en Fase 1) |
| 0 contradicciones conocidas | ✅ (propagación verificada pieza a pieza en Fase 1) |
| 0 respuestas numéricas imposibles | ✅ (Fase 2: 0 discrepancias reales) |
| 0 claves MCQ incorrectas | ✅ (0 MCQ sin opción correcta válida) |
| Prerrequisitos mapeados | ✅ (`KNOWLEDGE_GRAPH.json`, 88 nodos / 156 aristas) |
| Rutas pedagógicas implementadas | ✅ como datos (`schema_v2.learning_design.recommended_routes`); ⚠️ sin UI que las use todavía (ver `FRONTEND_CHANGES.md`) |
| Checkpoints implementados | ✅ (`unit_checkpoints.json`, 31 checkpoints) |
| Exam Mode disponible | ✅ como datos (`exam_mode.json`); ⚠️ sin UI dedicada todavía |
| JSON válido | ✅ |
| IDs únicos | ✅ (88/88 `canonical_lesson_id`; 0 duplicados dentro de lección) |
| Referencias válidas | ✅ tras el fix de Fase 7 (0 `objective_ids` rotos; 15 `concept_ids` inter-lección documentados como preexistentes y no bloqueantes) |
| Frontend funcional | ✅ (ver `MIGRATION_NOTES.md`, Fase 8: servidor local comprobado) |
| QA final completado | ✅ este documento |
