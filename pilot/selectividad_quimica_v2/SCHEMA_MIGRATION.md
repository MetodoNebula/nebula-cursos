# SCHEMA_MIGRATION.md — selectividad_quimica

Migración **aditiva**: se añade `schema_v2` a cada lección (prefijo canónico `SELQUI::<unidad>::<id>`) sin tocar los campos planos que lee `index.html`. Verificado: el frontend no referencia `schema_v2`.

- **scope**: química no tenía el campo; se añadió a los 660 bloques por heurística (type `derivation`/`extension` o marcadores de título → ADVANCED; resto CORE; ante la duda, CORE para no ocultar contenido esencial). Resultado conservador: {'CORE': 650, 'ADVANCED': 10}. Esto refleja que el curso ya estaba bien secuenciado.
- **rutas** `recommended_routes` (DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW) derivadas de scope/difficulty.
- **epistemic_type** por override para los claims auditados en el ledger (H₂SO₄→EXAM_CONVENTION, estado estándar→EXAM_CONVENTION, T=ΔH/ΔS→APPROXIMATION, Madelung→HEURISTIC, orbital→DEFINITION, Kc→MODEL…); MODEL por defecto.
- Validado: 133/133 canonical únicos, 0 MEZCLA, JSON válido en los 10 bundles.
