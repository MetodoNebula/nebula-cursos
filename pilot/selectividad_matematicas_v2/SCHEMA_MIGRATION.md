# SCHEMA_MIGRATION.md — selectividad_matematicas

Migración **aditiva** a `schema_v2` (prefijo `SELMAT::<unidad>::<id>`), igual que en
física: se añade la clave `schema_v2` a cada lección sin modificar ningún campo
plano que lee `index.html`. Rutas DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW
derivadas de los campos `scope` (CORE / ADVANCED / EXTENDED / EXTENSION) y
`difficulty` ya presentes; claims con `epistemic_type` (THEOREM para enunciados
tipo teorema/regla, EXACT por defecto). 107/107 canonical_lesson_id únicos.
