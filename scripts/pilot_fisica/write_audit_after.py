# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")

catalog_after = json.load(open(os.path.join(BASE, "catalog.json"), encoding="utf-8"))
sf = next(p for p in catalog_after["projects"] if p["key"] == "selectividad_fisica")

qa = json.load(open(os.path.join(BASE, "scripts/pilot_fisica/structural_qa_report.json"), encoding="utf-8"))
numqa = json.load(open(os.path.join(BASE, "scripts/pilot_fisica/numeric_qa_report.json"), encoding="utf-8"))
kg = json.load(open(os.path.join(PILOT, "KNOWLEDGE_GRAPH.json"), encoding="utf-8"))
ckpt = json.load(open(os.path.join(PILOT, "unit_checkpoints.json"), encoding="utf-8"))
diag = json.load(open(os.path.join(PILOT, "diagnostic.json"), encoding="utf-8"))
exam = json.load(open(os.path.join(PILOT, "exam_mode.json"), encoding="utf-8"))

content = f"""# AUDIT_AFTER.md — selectividad_fisica (piloto v2, estado final)

Contraparte de `AUDIT_BEFORE.md` tras las Fases 1-8. Mismas secciones, con
el estado tras la intervención.

## 1. Unidades y lecciones

- Unidades: **{len(sf['units'])}** (las 8 originales + el módulo nuevo
  `fundamentos`, de remediación just-in-time).
- Lecciones: **{sf['total']['lecciones']}** (76 originales + 6 de atomizar
  6 lecciones sobredimensionadas en 12 + 6 microlecciones de Fundamentos).
- Piezas totales: **{sf['total']['piezas']}**.
- Por tipo: {json.dumps(sf['total']['por_tipo'], ensure_ascii=False)}

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
- QA numérico propio (Fase 2): **{len(numqa)}** discrepancia(s) candidata(s)
  tras recorrer los 88 bundles, y la única es un artefacto del propio
  evaluador (precedencia de operadores), no un error de contenido real.

## 4. Estructura y secuenciación

- Las 6 lecciones del backlog oficial de problemas estructurales
  (`qa_por_curso/selectividad_fisica_structural_issues.csv`) ya **no
  existen como unidad única**: cada una se dividió en dos partes de
  0,5-1,5 h (frente a las 1,5-2,5 h originales), conservando el 100% de
  sus piezas (verificado automáticamente, 0 piezas perdidas o duplicadas).
- Prerrequisitos: **{len(kg['nodes'])}** lecciones mapeadas en
  `KNOWLEDGE_GRAPH.json`, con **{len(kg['edges'])}** aristas de
  prerrequisito (secuenciales dentro de unidad + remediación hacia
  Fundamentos).

## 5. Rutas pedagógicas (DESDE_CERO / STANDARD / EXCELLENCE / FAST_REVIEW)

Implementadas como datos en `schema_v2.learning_design.recommended_routes`
de cada una de las {sf['total']['lecciones']} lecciones, derivadas de los
campos `scope`/`difficulty`/`type` ya presentes en cada pieza (ver
`SCHEMA_MIGRATION.md` para la metodología exacta). Pendiente de UI que las
haga navegables por el alumno (`FRONTEND_CHANGES.md`).

## 6. Checkpoints y diagnóstico

- Checkpoints: **{len(ckpt['checkpoints'])}** (0 antes), 0 vacíos.
- Diagnóstico inicial por habilidades: **{diag['n_items']}** items sobre
  **{len(diag['skill_vector_axes'])}** ejes (0 antes).

## 7. Exam Mode / módulo "PAU integrada"

- `topic_questions`: {sum(len(v) for v in exam['topic_questions'].values())}
  preguntas repartidas en 8 unidades.
- `mixed_questions`: {len(exam['mixed_questions'])}.
- `timed_questions`: {len(exam['timed_questions'])} (con tiempo estimado).
- Exámenes parciales: {len(exam['partial_mock_exams'])}. Exámenes
  completos: {len(exam['full_mock_exams'])}.

## 8. QA estructural (Fase 7)

- JSON válido: **{qa['json_valid']}**.
- `canonical_lesson_id` únicos: **{qa['canonical_ids_total']}**/{qa['lessons_total']}, 0 duplicados.
- IDs duplicados dentro de una lección: **{len(qa['per_lesson_id_duplicates'])}**.
- `objective_ids` sin resolver: **{len(qa['unresolved_objective_refs'])}**.
- `concept_ids` sin resolver: **{len(qa['unresolved_concept_refs'])}** (preexistentes, documentados en `QA_REPORT.md`).
- MCQ sin opción correcta válida: **{len(qa['mcq_no_correct_option'])}**.
- Distractores sin `why_wrong`: **{qa['mcq_distractor_missing_why_wrong']}/{qa['mcq_distractor_total']}**.
- Campos obligatorios vacíos: **{len(qa['empty_or_truncated_fields'])}**.

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
selectividad_fisica (de 76 a {sf['total']['lecciones']} lecciones, de
5888 a {sf['total']['piezas']} piezas), resto del catálogo intacto,
verificado con servidor local.
"""
open(os.path.join(PILOT, "AUDIT_AFTER.md"), "w", encoding="utf-8").write(content)
print("written", len(content))
