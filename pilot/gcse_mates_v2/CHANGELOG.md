# Changelog – GCSE Mathematics Pilot v2

**Course:** `gcse_mates`

---

## [v2.0.0] — 2026-10-19

### Added
- **U00 Foundations module** — 6 new micro-lessons for DESDE_CERO route:
  - 01_Arithmetic_Fluency (BIDMAS, negative numbers, factors, estimation)
  - 02_Fractions_Decimals_Percentages (conversions, operations, ordering)
  - 03_Basic_Algebra (expressions, substitution, like terms, solving equations)
  - 04_Coordinates_and_Graphs (Cartesian plane, quadrants, plotting, tables)
  - 05_Units_and_Measurement (metric units, conversions, time, scales)
  - 06_Shape_Recognition (polygons, triangles, quadrilaterals, 3D, symmetry, angles)
- **`schema_v2`** on all 93 lessons — canonical IDs, recommended routes, epistemic overrides
- **`semantic_change_ledger.json`** — 19 audit findings (4 P0, 5 P1, 10 P2)
- **`unit_checkpoints.json`** — 3-5 checkpoint questions per unit
- **`diagnostic.json`** — 15-20 items across 6 diagnostic axes
- **`exam_mode.json`** — by_topic, mixed, and timed_papers configurations
- **`catalog_patch_gcse_maths.json`** — registration patch for new U00 unit
- **`KNOWLEDGE_GRAPH.json`** — concept dependency graph across all units
- **SVG diagram assets** for lessons requiring visual mathematical content

### Fixed
- **16 MEZCLA violations** — CORE blocks after ADVANCED/ENRICHMENT, reordered
- **Scope field coverage** — verified 100% of theory blocks have `scope`

### Not Changed
- **`catalog.json`** — shared file, not modified; use `catalog_patch_gcse_maths.json` instead
- **Existing lesson content** — no fields removed; `schema_v2` is additive only
- **Mixed practice bank editorial provenance** — P2 cleanup deferred
