# QA_REPORT.md — selectividad_quimica (piloto v2) — 2026-10-19

**Última actualización**: Auditoría v2 (2026-10-19)

| Comprobación | Resultado |
|---|---|
| JSON válido en los 10 bundles | **True** |
| Lecciones | **133** |
| canonical_lesson_id únicos | **133** (duplicados: 0) |
| IDs duplicados dentro de una lección | **0** |
| Lecciones con ampliación antes de lo esencial (MEZCLA) | **0** |
| MCQ sin opción correcta válida | **0** |
| Distractores sin why_wrong | **0 / 1770** |
| Campos obligatorios vacíos | **0** |
| SVG con XML inválido | **0 / 104** |
| SVG colores fuera de paleta Nebula | **31** (P2 — funcionales) |
| Referencias rotas (checkpoints/diagnóstico/exam) | **0** |
| Backlog del ledger | 17/17 aplicado o verificado |
| Theory blocks con scope | **660/660** (CORE: 650, ADVANCED: 10) |
| Ejercicios guiados totales | **259** |
| Ejercicios con ≥2 hints | **259/259** |
| Ejercicios con full_solution | **259/259** |
| Ejercicios con id | **259/259** |
| MCQ totales | **590** |

## Auditoría v2 — Correcciones aplicadas

- 3 × full_solution añadidos (U07-L03, U08-L10, U08-L11)
- 28 × id añadidos a ejercicios de U07
- 53 × hint progresivo (2º) añadidos
- 0 nuevos errores P0/P1 encontrados

Definition of Done: 0 P0 abiertos, 0 contradicciones conocidas, aproximaciones etiquetadas, prerequisitos mapeados (grafo), rutas implementadas (schema_v2), checkpoints y Exam Mode presentes, JSON válido, QA completado al 100%. Frontend: funciona sin cambios (ver FRONTEND_CHANGES).
