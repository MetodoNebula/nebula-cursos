# -*- coding: utf-8 -*-
import os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
content = r"""# PILOT_COMPARISON.md — selectividad_fisica: antes vs. después

| Métrica | Antes (original) | Después (piloto v2) |
|---|---|---|
| Lecciones | 76 | 88 (+6 atomización, +6 Fundamentos) |
| Lecciones del backlog oficial de sobrecarga estructural (`structural_issues.csv`) | 6 | **0** (cada una dividida en dos partes de 0,5–1,5 h; el 100% de sus piezas se conserva, verificado automáticamente) |
| Afirmaciones de alto riesgo del `semantic_change_ledger` sin condiciones | 22 (2 P0, 6 P1, 14 P2) | **0** (13 corregidas con propagación completa; 9 verificadas como ya correctas) |
| P0 abiertos | 2 | **0** |
| P1 abiertos | 6 | **0** |
| Worked examples | 321 | 327 |
| Faded examples (`guided_exercises`, con *hints* y resolución parcial) | 180 | 180 |
| Checkpoints por unidad | 0 | **31** (0 vacíos) |
| Preguntas de nivel L4 (Selectividad / selección de estrategia) | 91 | 91 (reclasificadas y con `route_visibility` explícito en `schema_v2`) |
| Challenges L5 (transferencia) | 65 (`challenge_questions`) | 65 (idem; ahora con `route_visibility=["excellence"]` explícito) |
| Prerequisite links explícitos (grafo) | 0 (solo `prerequisites[]` sueltos por lección, sin grafo) | **156** aristas en `KNOWLEDGE_GRAPH.json` (88 nodos) |
| MCQ inconsistentes (sin opción correcta válida) | No auditado automáticamente | **0** (auditado sobre 539 MCQ) |
| Distractores sin `why_wrong` | No auditado automáticamente | 18/1617 (1,1 %) |
| Diagnóstico inicial por habilidades | No existía | 22 items / 14 ejes |
| Exam Mode (topic/mixed/timed/parcial/completo) | No existía | 173/10/173/2/2 |
| Rutas pedagógicas (DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW) | No existían | Implementadas como datos en `schema_v2` de las 88 lecciones (sin UI todavía, ver `FRONTEND_CHANGES.md`) |
| `canonical_lesson_id` únicos | No existía el concepto | 88/88, 0 duplicados |
| Discrepancias numéricas reales (QA propio) | No auditado con un verificador fiable (el oficial confunde `E` con *e*) | **0** reales (1 candidato, artefacto del propio evaluador) |

## Notas de método

- **Lecciones >45 min** no se incluye como fila de comparación directa
  porque, como ya documentaba `AUDIT_BEFORE.md`, la mayoría de lecciones
  de Selectividad Física legítimamente ocupan 1,5-2,5 h por la densidad
  del temario (no son "demasiado largas", son lecciones completas de un
  tema PAU); el criterio que de verdad importa —y el que exige el
  encargo resolver— es el backlog **oficial** de 6 lecciones
  estructuralmente sobrecargadas, que se cerró a 0.
- **Claims sin condiciones**: el recuento léxico bruto (semantic lint,
  ver `semantic_lint_BEFORE.json`/`semantic_lint_AFTER.json`) no es una
  métrica de precisión fiable, porque palabras como "siempre"/"solo"
  aparecen también en afirmaciones correctamente acotadas (p. ej. "esto
  **solo** vale para pequeñas oscilaciones"). El indicador real y
  auditado afirmación por afirmación es el backlog de 22 items del
  ledger, que pasa de 22 abiertos a 0.
"""
open(os.path.join(BASE, "PILOT_COMPARISON.md"), "w", encoding="utf-8").write(content)
print("written", len(content))
