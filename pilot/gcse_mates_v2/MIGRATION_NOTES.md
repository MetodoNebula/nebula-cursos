# Migration Notes – GCSE Mathematics v2

**Course:** `gcse_mates`
**Date:** 2026-10-19

---

## Deployment Checklist

### Step 1: Copy Bundle Files
Copy all files from `pilot/gcse_mates_v2/bundles/` to the production bundles
directory, replacing the 9 existing bundles (U01-U09) and adding the new U00:

```
gcse_mates__U00_Foundations.json  (NEW)
gcse_mates__U01_Number.json      (UPDATED - schema_v2 + MEZCLA fixes)
gcse_mates__U02_Algebra_and_Graphs.json  (UPDATED)
gcse_mates__U03_Coordinate_Geometry.json (UPDATED)
gcse_mates__U04_Geometry.json    (UPDATED)
gcse_mates__U05_Mensuration.json (UPDATED)
gcse_mates__U06_Trigonometry.json (UPDATED)
gcse_mates__U07_Transformations_and_Vectors.json (UPDATED)
gcse_mates__U08_Probability.json (UPDATED)
gcse_mates__U09_Statistics.json  (UPDATED)
```

### Step 2: Apply Catalog Patch
Merge `catalog_patch_gcse_maths.json` into `catalog.json`:
- Add the U00 unit entry with `order: 0` (before U01)
- Ensure the `bundle` field references the correct filename

### Step 3: Copy Assessment Files
Place in the course's data directory:
- `unit_checkpoints.json`
- `diagnostic.json`
- `exam_mode.json`

### Step 4: Copy SVG Assets
Place generated SVG files alongside the bundles or in the assets directory
as required by the frontend.

### Step 5: Encrypt
Run encryption on all bundle files:
```bash
node cifrar.js --password "Nebula123!" --input bundles/ --output encrypted/
```

### Step 6: Deploy to GitHub Pages
Commit encrypted bundles and updated catalog to the repository.
Push to the `gh-pages` branch (or whichever branch serves GitHub Pages).

### Step 7: Verify
1. Open the Nebula viewer
2. Select the GCSE Mathematics course
3. Verify U00 Foundations appears first in the unit list
4. Open at least one lesson from each unit to confirm decryption works
5. Test the diagnostic, checkpoint, and exam modes if frontend supports them

## Rollback Plan

If issues are found:
1. Restore the previous bundle files from git history
2. Remove the U00 entry from `catalog.json`
3. Re-encrypt and redeploy

The v2 changes are non-destructive — original content is preserved in all
updated bundles. Only array ordering within `theory_blocks` was changed
(MEZCLA fixes), and `schema_v2` is a new additive field.
