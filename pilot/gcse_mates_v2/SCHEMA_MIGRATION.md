# Schema Migration – GCSE Mathematics v2

**Course:** `gcse_mates`
**Date:** 2026-10-19

---

## Overview

This document describes the `schema_v2` object added to every lesson in the
GCSE Mathematics course as part of the Phase 3 migration.

## schema_v2 Structure

```json
{
  "schema_v2": {
    "canonical_lesson_id": "GCSEMATHS::U01_Number::types_of_number_factors_and_multiples",
    "recommended_routes": {
      "DESDE_CERO": { "include": true, "order": 1 },
      "STANDARD": { "include": true, "order": 1 },
      "EXCELLENCE": { "include": true, "order": 1 },
      "FAST_REVIEW": { "include": false }
    },
    "epistemic_overrides": [
      {
        "block_id": "TH-NUM-01-3",
        "type": "DEFINITION",
        "note": "Definition of prime numbers"
      }
    ]
  }
}
```

## Fields

### canonical_lesson_id
Format: `GCSEMATHS::<unit_id>::<slug>`

- `unit_id`: e.g. `U01_Number`, `U00_Foundations`
- `slug`: lowercase, underscored version of lesson title

### recommended_routes

| Route | Description |
|---|---|
| `DESDE_CERO` | Complete beginner path. Includes U00 Foundations. Excludes mixed practice banks and ADVANCED-only lessons. |
| `STANDARD` | Core IGCSE pathway. Includes all CORE lessons, excludes ADVANCED-only. |
| `EXCELLENCE` | Full syllabus including ADVANCED/ENRICHMENT content. |
| `FAST_REVIEW` | Pre-exam revision. Only key lessons per unit (defined in FAST_REVIEW_LESSONS). |

Each route has:
- `include`: boolean — whether this lesson appears in the route
- `order`: integer — position within the route sequence

### epistemic_overrides

Tags for theory blocks that carry special epistemic status:
- `DEFINITION` — defines a term or concept
- `LAW` — a theorem, rule, or property
- `MODEL` — a formula or mathematical model
- `APPROXIMATION` — an estimation or approximation method
- `HEURISTIC` — a strategy, tip, or mnemonic
- `EXAM_CONVENTION` — exam-specific notation or expectations

## Migration Notes

- The `schema_v2` field is **additive only** — no existing fields were modified or removed.
- All 93 lessons across 10 bundles (U00-U09) have a `schema_v2` object.
- Content integrity was verified: lesson, block, exercise, and MCQ counts remain unchanged after migration.
- The frontend should gracefully ignore `schema_v2` if not yet supported (it is a new top-level key).
