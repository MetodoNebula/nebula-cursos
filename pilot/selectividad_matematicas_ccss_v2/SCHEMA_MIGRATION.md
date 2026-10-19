# SCHEMA_MIGRATION.md — selectividad_matematicas_ccss
Migración **aditiva**: se añade `schema_v2` a cada lección (prefijo canónico `SELMATCCSS::<unidad>::<id>`) sin tocar ningún campo plano que lee `index.html`. Las rutas DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW se derivan de los campos `scope` y `difficulty` ya presentes. 0 referencias a `schema_v2` en el frontend → compatibilidad total.
