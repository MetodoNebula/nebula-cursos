# Frontend Changes Guide

## No Breaking Changes
This pilot introduces **no breaking changes** to the frontend. All modifications are backward-compatible.

## New Files to Deploy

### Bundles (replace existing)
All 10 existing bundle files (U01–U10) have been updated in place. Deploy them to the same paths.

### New Bundle
- `gcse_ciencias_phys__U00_Foundations.json` — New unit, must be added to the bundle list

### New Assessment Files
- `unit_checkpoints.json` — Place alongside bundles
- `diagnostic.json` — Place alongside bundles
- `exam_mode.json` — Place alongside bundles

### Catalog Update
- Apply changes from `catalog_patch_gcse_phys.json` to `catalog.json`
- Insert U00_Foundations as the first unit (order: 0) in the gcse_ciencias_phys project

## Optional Frontend Enhancements

### Route-Based Filtering (schema_v2)
If implementing learning routes:
1. Read `lesson.schema_v2.recommended_routes` 
2. Filter lessons by the selected route (DESDE_CERO, STANDARD, EXCELLENCE, FAST_REVIEW)
3. Sort by `order` within each route

### Assessment Mode
If implementing assessment features:
1. Load the appropriate assessment JSON file
2. `unit_checkpoints.json`: show after completing each unit
3. `diagnostic.json`: show at course start for placement
4. `exam_mode.json`: offer as a practice exam option

### SVG Rendering
- The frontend already renders the `svg` field in assets — no changes needed
- New SVGs follow the same format as existing ones
- All use the Nebula palette and `viewBox` (no fixed width/height)

## Encryption
All bundle files must be encrypted with AES-256-GCM via `cifrar.js` before deployment.
- Password: `Nebula123!`
- Process: Run cifrar.js on each JSON bundle to produce the encrypted version for GitHub Pages
