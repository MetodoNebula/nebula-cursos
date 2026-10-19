# Nebula — paquete completo de auditoría y reestructuración

Este ZIP reúne TODO el material generado para ejecutar la mejora de los cursos.

## Orden recomendado de lectura para un agente

1. `00_instrucciones_generales/00_MASTER_IMPLEMENTATION_SPEC.md`
2. `00_instrucciones_generales/AGENT_EXECUTION_INSTRUCTIONS.md`
3. `01_auditoria_original/auditoria_bundles_final.md`
4. `02_auditoria_reestructuracion/AUDITORIA_REESTRUCTURACION_COMPLETA.md`
5. Informe específico del curso en `02_auditoria_reestructuracion/cursos/`
6. `04_machine_readable/semantic_change_ledger.csv` o `.json`
7. CSV de QA específico del curso en `04_machine_readable/qa_por_curso/`
8. `04_machine_readable/target_lesson_schema.example.json`
9. Prompt específico del curso en `03_prompts_por_curso/`

## Archivos machine-readable

- `semantic_change_ledger.csv`: backlog principal de cambios.
- `semantic_change_ledger.json`: misma información para agentes que prefieran JSON.
- `lesson_inventory.csv`: inventario de lecciones.
- `structural_issues.csv`: incidencias estructurales.
- `equality_mismatches_candidates.csv`: candidatos a inconsistencias numéricas; contiene falsos positivos y no sustituye la auditoría validada.
- `qa_por_curso/*.csv`: incidencias estructurales separadas por curso.
- `target_lesson_schema.example.json`: modelo objetivo.
- `implementation_manifest.json`: manifiesto de implementación.

## Orden recomendado de ejecución

1. Selectividad Física
2. GCSE / IGCSE Physics
3. Selectividad Química
4. Selectividad Matemáticas II
5. GCSE / IGCSE Chemistry
6. GCSE / IGCSE Mathematics
7. Selectividad Matemáticas CCSS
8. ESO Matemáticas
9. ESO Física y Química Foundations
10. Física y Química Completo

`FQ_COMPLETO` debería ejecutarse al final, una vez validadas las decisiones de arquitectura en los pilotos anteriores.
