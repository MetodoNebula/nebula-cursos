# Frontend Changes – GCSE Mathematics v2

**Course:** `gcse_mates`
**Date:** 2026-10-19

---

## Summary

The v2 pilot adds new metadata and content to the GCSE Maths course.
Below are the changes relevant to the Nebula frontend.

## 1. New Top-Level Key: `schema_v2`

Every lesson now contains a `schema_v2` object. The frontend does NOT need
to render this directly — it is metadata for route selection and content
classification. However, if you want to support route-based navigation:

```javascript
// Example: filter lessons for DESDE_CERO route
const desdeZero = lessons.filter(
  l => l.schema_v2?.recommended_routes?.DESDE_CERO?.include === true
).sort(
  (a, b) => a.schema_v2.recommended_routes.DESDE_CERO.order
           - b.schema_v2.recommended_routes.DESDE_CERO.order
);
```

**Backward compatibility:** If the frontend ignores unknown top-level keys,
no changes are required. `schema_v2` is purely additive.

## 2. New Bundle: U00 Foundations

- File: `gcse_mates__U00_Foundations.json`
- Must be encrypted with `node cifrar.js` before deployment
- Must be registered in `catalog.json` using `catalog_patch_gcse_maths.json`
- Contains 6 lessons with the same structure as existing bundles

## 3. SVG Assets

New SVG diagram assets follow the existing format:
```json
{
  "id": "svg-xxx",
  "svg": "<svg ...>",
  "caption": "...",
  "purpose": "..."
}
```

The frontend already renders the `svg` field. No changes needed.

## 4. Assessment Files

Three new JSON files support assessment modes. These are **backend/configuration
files** and do not require frontend rendering unless you are building:
- A diagnostic quiz flow → `diagnostic.json`
- Unit checkpoint tests → `unit_checkpoints.json`
- Exam simulation mode → `exam_mode.json`

## 5. catalog.json Patch

**DO NOT overwrite `catalog.json` directly** (it is shared across courses).
Apply the patch in `catalog_patch_gcse_maths.json` to add the U00 unit entry.

## 6. No Breaking Changes

- No existing fields have been removed or renamed
- No existing bundle files have been restructured
- The `scope` field on theory blocks (CORE/ADVANCED/ENRICHMENT) was already
  present; it has been verified as 100% populated
- MEZCLA ordering fixes preserve all content, only changing array order
  within `theory_blocks`
