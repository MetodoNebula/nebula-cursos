# Instrucciones de ejecución para el agente de reestructuración

## Entrada
- `00_MASTER_IMPLEMENTATION_SPEC.md`
- todos los documentos de `/cursos`
- `semantic_change_ledger.csv` o `.json`
- `/qa/*_structural_issues.csv`
- `target_lesson_schema.example.json`
- corpus original `bundles.zip`

## Orden obligatorio
1. Leer completo el MASTER.
2. Seleccionar un curso y leer su documento completo.
3. Aplicar primero P0/P1 del ledger.
4. Resolver QA estructural.
5. Crear copia/versionado de trabajo; no modificar el original sin rollback.
6. Normalizar a claims/fórmulas/conditions.
7. Atomizar/poolizar.
8. Construir rutas adaptativas y prerequisites.
9. Regenerar summaries y assessments dependientes.
10. Ejecutar tests.
11. Emitir informe de cambios y lista de issues no resueltos.

## Regla de no alucinación
Si una instrucción exige determinar si un contenido pertenece oficialmente a un syllabus y el corpus no contiene evidencia suficiente, **no inventar**. Marcar `NEEDS_SYLLABUS_CHECK` y consultar la fuente oficial configurada. Esto es especialmente importante para segmentar extensiones de ESO y perfiles PAU regionales.

## Regla de conservación
No eliminar un bloque solo porque sea avanzado. Reubicarlo en `ADVANCED`, `BACH_BRIDGE` o un pool si es correcto y útil. Eliminar únicamente duplicados, contenido incorrecto sustituido, boilerplate sin valor o material fuera de alcance cuando exista decisión explícita.

## Salida mínima por curso
- árbol final de módulos/lecciones;
- JSON migrados;
- mapping old_id -> canonical/new_id;
- lista de cambios P0/P1/P2;
- reporte QA con tests pasados/fallidos;
- métricas de cobertura: objetivos antes/después, ejercicios conservados/movidos/eliminados;
- lista de `NEEDS_HUMAN_REVIEW` y razón.

## Política de commits
Recomendado por fases:
- `fix/<course>/p0-p1`
- `refactor/<course>/canonical-schema`
- `refactor/<course>/atomic-lessons`
- `feat/<course>/adaptive-routes`
- `qa/<course>/validation`

No mezclar correcciones semánticas masivas y rediseño visual en un único commit si se quiere poder auditar la regresión.
