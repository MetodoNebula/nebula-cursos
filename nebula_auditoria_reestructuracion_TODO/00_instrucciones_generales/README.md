# Paquete de auditoría y reestructuración para agente

Este paquete transforma la auditoría previa en una especificación ejecutable. Orden de lectura:

1. `00_MASTER_IMPLEMENTATION_SPEC.md`
2. `AGENT_EXECUTION_INSTRUCTIONS.md`
3. documento del curso en `/cursos`
4. `semantic_change_ledger.csv`
5. CSV QA correspondiente
6. `target_lesson_schema.example.json`

## Documentos por curso
- `01_SELECTIVIDAD_FISICA.md` — Selectividad / PAU — Física
- `02_SELECTIVIDAD_QUIMICA.md` — Selectividad / PAU — Química
- `03_SELECTIVIDAD_MATEMATICAS.md` — Selectividad / PAU — Matemáticas II
- `04_SELECTIVIDAD_MATEMATICAS_CCSS.md` — Selectividad / PAU — Matemáticas Aplicadas a las CCSS II
- `05_ESO_MATEMATICAS.md` — ESO — Matemáticas
- `06_ESO_FISICA_QUIMICA_FOUNDATIONS.md` — ESO — Física y Química (Foundations / versión standalone)
- `07_FQ_COMPLETO.md` — Física y Química — corpus completo ESO / 4.º ESO / 1.º Bachillerato
- `08_GCSE_IGCSE_PHYSICS.md` — Cambridge GCSE/IGCSE — Physics
- `09_GCSE_IGCSE_CHEMISTRY.md` — Cambridge GCSE/IGCSE — Chemistry
- `10_GCSE_IGCSE_MATHEMATICS.md` — Cambridge GCSE/IGCSE — Mathematics

## Ficheros machine-readable
- `semantic_change_ledger.csv/json`: cambios semánticos priorizados y criterios de aceptación.
- `qa/*.csv`: incidencias estructurales exactas.
- `target_lesson_schema.example.json`: forma objetivo sugerida para una lección canónica.
