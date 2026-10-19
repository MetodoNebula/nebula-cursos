# AUDIT_AFTER.md — selectividad_fisica (piloto v2, estado final)

Contraparte de `AUDIT_BEFORE.md` tras las Fases 1-8. Mismas secciones, con
el estado tras la intervención.

## 1. Unidades y lecciones

- Unidades: **9** (las 8 originales + el módulo nuevo
  `fundamentos`, de remediación just-in-time).
- Lecciones: **88** (76 originales + 6 de atomizar
  6 lecciones sobredimensionadas en 12 + 6 microlecciones de Fundamentos).
- Piezas totales: **6047**.
- Por tipo: {"objectives": 528, "prerequisites": 337, "diagnostic_items": 206, "theory_blocks": 713, "keywords": 711, "worked_examples": 327, "guided_exercises": 180, "exercises": 317, "exam_questions": 173, "challenge_questions": 65, "mcq": 539, "flashcards": 779, "misconceptions": 190, "common_mistakes": 457, "exam_notes": 525}

## 2. Backlog obligatorio (semantic_change_ledger)

- **22/22** afirmaciones del ledger de `selectividad_fisica` resueltas:
  13 corregidas con propagación a todas las representaciones afectadas
  (objectives/theory/summary/flashcards/MCQ/exam_notes/common_mistakes
  según el caso) y 9 verificadas como ya correctas en el contenido actual
  (herencia de una revisión previa no registrada en el propio ledger),
  documentadas explícitamente en vez de reescritas sin necesidad.
- 2 P0 (riesgo más alto) resueltos: inducción sin movimiento relativo,
  criterio dimensional como condición suficiente.
- 4 P1 resueltos: rozamiento "siempre negativo", potencial magnético
  negado globalmente, polarización de dieléctricos, energía de enlace
  Fe-56 como máximo exacto.
- Ver `CHANGELOG.md` para el detalle fila a fila.

## 3. Precisión científica / scientific accuracy

- Epistemic typing introducido en `schema_v2.knowledge_model` para las 22
  afirmaciones auditadas (EXACT/MODEL/APPROXIMATION/HEURISTIC/
  SPECIAL_CASE, según el caso — ver `SCHEMA_MIGRATION.md`).
- QA numérico propio (Fase 2): **1** discrepancia(s) candidata(s)
  tras recorrer los 88 bundles, y la única es un artefacto del propio
  evaluador (precedencia de operadores), no un error de contenido real.

## 4. Estructura y secuenciación

- Las 6 lecciones del backlog oficial de problemas estructurales
  (`qa_por_curso/selectividad_fisica_structural_issues.csv`) ya **no
  existen como unidad única**: cada una se dividió en dos partes de
  0,5-1,5 h (frente a las 1,5-2,5 h originales), conservando el 100% de
  sus piezas (verificado automáticamente, 0 piezas perdidas o duplicadas).
- Prerrequisitos: **88** lecciones mapeadas en
  `KNOWLEDGE_GRAPH.json`, con **156** aristas de
  prerrequisito (secuenciales dentro de unidad + remediación hacia
  Fundamentos).

## 5. Rutas pedagógicas (DESDE_CERO / STANDARD / EXCELLENCE / FAST_REVIEW)

Implementadas como datos en `schema_v2.learning_design.recommended_routes`
de cada una de las 88 lecciones, derivadas de los
campos `scope`/`difficulty`/`type` ya presentes en cada pieza (ver
`SCHEMA_MIGRATION.md` para la metodología exacta). Pendiente de UI que las
haga navegables por el alumno (`FRONTEND_CHANGES.md`).

## 6. Checkpoints y diagnóstico

- Checkpoints: **31** (0 antes), 0 vacíos.
- Diagnóstico inicial por habilidades: **22** items sobre
  **14** ejes (0 antes).

## 7. Exam Mode / módulo "PAU integrada"

- `topic_questions`: 173
  preguntas repartidas en 8 unidades.
- `mixed_questions`: 10.
- `timed_questions`: 173 (con tiempo estimado).
- Exámenes parciales: 2. Exámenes
  completos: 2.

## 8. QA estructural (Fase 7)

- JSON válido: **True**.
- `canonical_lesson_id` únicos: **88**/88, 0 duplicados.
- IDs duplicados dentro de una lección: **0**.
- `objective_ids` sin resolver: **0**.
- `concept_ids` sin resolver: **15** (preexistentes, documentados en `QA_REPORT.md`).
- MCQ sin opción correcta válida: **0**.
- Distractores sin `why_wrong`: **18/1617**.
- Campos obligatorios vacíos: **0**.

## 9. Fundamentos (módulo nuevo)

6 microlecciones de remediación just-in-time (vectores, trigonometría,
despeje algebraico, notación científica y SI, lectura de gráficas,
conservación de la energía), enlazadas por `KNOWLEDGE_GRAPH.json` a las
lecciones de contenido que las necesitan como prerrequisito (vectores:
23 lecciones; notación científica/SI y despeje algebraico: 16 cada uno;
trigonometría: 15; lectura de gráficas y conservación de la energía: 6
cada uno).

## 10. Migración de esquema

Ver `SCHEMA_MIGRATION.md`: migración aditiva a `schema_v2`, 0 referencias
en `index.html` (frontend no tocado).

## 11. Release

Ver `MIGRATION_NOTES.md`: `catalog.json` y `bundles/` actualizados para
selectividad_fisica (de 76 a 88 lecciones, de
5888 a 6047 piezas), resto del catálogo intacto,
verificado con servidor local.
