# Migration Notes

## Deployment Checklist

1. **Encrypt all bundle files** using cifrar.js with password `Nebula123!`
2. **Replace** the 10 existing encrypted bundles (U01–U10) on GitHub Pages
3. **Add** the new U00 encrypted bundle
4. **Add** the 3 assessment files (encrypt if required by the viewer)
5. **Update catalog.json** by applying catalog_patch_gcse_phys.json:
   - Insert U00_Foundations as first unit with order: 0
   - Do NOT modify any other catalog entries
6. **Test** the encrypted viewer loads all 11 bundles correctly

## Key Constraints Preserved
- `catalog.json` was NOT modified directly — a patch file is provided
- All existing lesson IDs, titles, and structures are unchanged
- `schema_v2` is purely additive — does not touch existing flat fields
- SVG diagrams use the `svg` field in `assets` (already rendered by frontend)
- MCQ format uses `{key, text, why_wrong}` options with `correct` as letter string

## Content Philosophy
- **No content was trimmed** — all theory, examples, and exercises are preserved or expanded
- Goal: maximise the student's exam grade by making content easier to follow
- P0 scientific accuracy fixes applied with full audit trail in semantic_change_ledger.json
- Syllabus-specific references (0654/0625) replaced with generic "GCSE" / "this course"
- Editorial metadata (source_book, etc.) removed as it is not student-facing
