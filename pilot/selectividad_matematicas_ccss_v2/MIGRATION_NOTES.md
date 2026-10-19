# MIGRATION_NOTES.md — selectividad_matematicas_ccss
- `original/selectividad_matematicas_ccss/` contiene los 9 bundles originales congelados (rollback).
- Los 9 bundles v2 se escriben en `pilot/selectividad_matematicas_ccss_v2/` y en `bundles/` (lo que lee el frontend).
- `catalog.json` NO se toca aquí: lo regenera el coordinador (los conteos por lección no cambian; sólo se reordenaron bloques y se añadieron diagramas/esquema_v2, sin alterar el número de piezas listadas).
- `bundles/` y `catalog.json` están en `.gitignore` (contenido en claro; la web publica la versión cifrada).
