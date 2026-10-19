# Schema Migration Guide — schema_v2

## Overview
`schema_v2` is an **additive** field injected into every lesson object. It does not modify or replace any existing flat fields.

## Structure
```json
{
  "schema_v2": {
    "canonical_lesson_id": "GCSEPHYS::U01_Measurement_and_Motion::scalars_and_vectors",
    "recommended_routes": {
      "DESDE_CERO": {"include": true, "order": 1},
      "STANDARD": {"include": true, "order": 1},
      "EXCELLENCE": {"include": true, "order": 1},
      "FAST_REVIEW": {"include": false}
    },
    "epistemic_overrides": []
  }
}
```

## Fields

### canonical_lesson_id
- Format: `GCSEPHYS::<unit_id>::<slug>`
- Unique across the entire course (68 lessons)
- Stable identifier for cross-referencing, analytics, and inter-course linking

### recommended_routes
Four predefined learning paths:
- **DESDE_CERO** — Complete beginner path (includes U00 Foundations)
- **STANDARD** — Normal GCSE preparation path
- **EXCELLENCE** — Full coverage including all ADVANCED/ENRICHMENT material
- **FAST_REVIEW** — Quick revision path (core concepts and key formulas only)

Each route entry: `{"include": bool, "order": int}`

### epistemic_overrides
Array of overrides for specific theory blocks where the epistemic classification differs from the default. Used to flag blocks where a LAW is actually a MODEL, or where an APPROXIMATION should be noted.

## Frontend Impact
- The frontend reads `schema_v2` as metadata only
- No changes to rendering logic required for basic display
- Route-based filtering can be implemented by reading `recommended_routes`
- The existing flat fields (id, title, theory_blocks, etc.) remain the primary data source

## Backward Compatibility
- Lessons without `schema_v2` (none after this migration) should render normally
- The field is purely additive — removing it returns the lesson to its pre-migration state
