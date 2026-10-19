# QA Report — GCSE Physics Pilot v2

## Validation Summary

| Check                | Result | Details |
|----------------------|--------|---------|
| JSON validity        | ✅ PASS | All 11 bundles parse correctly |
| Canonical IDs        | ✅ PASS | 68 unique IDs, all GCSEPHYS:: format |
| MEZCLA ordering      | ✅ PASS | No ADVANCED/ENRICHMENT before CORE |
| MCQ format           | ✅ PASS | 243 MCQs, all use letter keys (A/B/C/D) |
| SVG validity         | ✅ PASS | 79 SVGs, all valid XML in assets[].svg |
| schema_v2            | ✅ PASS | All 68 lessons have schema_v2 with routes |
| scope field          | ✅ PASS | All 286 theory_blocks have valid scope |
| Syllabus codes       | ✅ PASS | 0 references to 0654/0625 in student text |
| Editorial labels     | ✅ PASS | No source_book/source_chapter/etc. remaining |
| Assessment files     | ✅ PASS | diagnostic (19), checkpoints (45), exam (40) |
| U00 Foundations      | ✅ PASS | 6 micro-lessons, all complete |
| Knowledge graph      | ✅ PASS | 68 nodes, 68 edges |

## Content Statistics

- **Bundles**: 11 (U00–U10)
- **Lessons**: 68 (62 original + 6 new in U00)
- **Theory blocks**: 286
- **Worked examples**: 226
- **Exercises**: 375
- **MCQs**: 243
- **Flashcards**: 295
- **SVG diagrams**: 79

## Phases Completed

### Phase 1: Semantic Audit
- 67 ledger entries in `semantic_change_ledger.json`
- 1 P0 (energy conservation caveat), 62 P1, 4 P2
- All syllabus-specific references (0654/0625) replaced with generic "GCSE"/"this course"
- Editorial metadata (source_book, etc.) removed from exercises

### Phase 2: Scope & MEZCLA
- All theory_blocks have `scope` field (CORE/ADVANCED/ENRICHMENT)
- 25 MEZCLA violations fixed (ADVANCED blocks moved after all CORE blocks)

### Phase 3: schema_v2 Migration
- `schema_v2` added to all 68 lessons
- `canonical_lesson_id` in format GCSEPHYS::<unit>::<slug>
- `recommended_routes` with 4 paths: DESDE_CERO, STANDARD, EXCELLENCE, FAST_REVIEW
- `epistemic_overrides` array (empty where not needed)

### Phase 4: Module Foundations (U00)
- 6 micro-lessons covering prerequisites:
  1. Units, prefixes and scientific notation
  2. Rearranging equations
  3. Reading and plotting graphs
  4. Proportionality and ratios
  5. Estimating and checking
  6. Laboratory skills and safety
- Each lesson includes: 3–4 theory blocks, 2–3 worked examples, 3–4 exercises, 4–5 MCQs, flashcards, keywords

### Phase 5: Assessment Files
- `diagnostic.json`: 19-item placement test with route thresholds
- `unit_checkpoints.json`: 10 checkpoints (45 items total), 60% pass threshold
- `exam_mode.json`: 40-item mock exam with grade boundaries (1–9)

### Phase 6: SVG Coverage
- 79 SVGs validated across 11 bundles
- All use Nebula palette and viewBox (responsive)

## Content Philosophy

**No content was trimmed.** All theory, worked examples, exercises, and exam questions are preserved or expanded. The goal throughout was to make content easier to follow while maximising the student's exam grade.

## Files Delivered

### Bundles (11)
- `bundles/gcse_ciencias_phys__U00_Foundations.json` (NEW)
- `bundles/gcse_ciencias_phys__U01_Measurement_and_Motion.json`
- `bundles/gcse_ciencias_phys__U02_Mass_Weight_and_Density.json`
- `bundles/gcse_ciencias_phys__U03_Forces_and_Pressure.json`
- `bundles/gcse_ciencias_phys__U04_Energy_Work_and_Power.json`
- `bundles/gcse_ciencias_phys__U05_Thermal_Physics.json`
- `bundles/gcse_ciencias_phys__U06_Waves_Light_and_Sound.json`
- `bundles/gcse_ciencias_phys__U07_Electricity_and_Magnetism.json`
- `bundles/gcse_ciencias_phys__U08_Nuclear_Physics.json`
- `bundles/gcse_ciencias_phys__U09_Space_Physics.json`
- `bundles/gcse_ciencias_phys__U10_Revision_and_Exam_Practice.json`

### Assessment
- `diagnostic.json`
- `unit_checkpoints.json`
- `exam_mode.json`

### Metadata
- `semantic_change_ledger.json`
- `catalog_patch_gcse_phys.json`
- `KNOWLEDGE_GRAPH.json`

### Documentation
- `QA_REPORT.md` (this file)
- `CHANGELOG.md`
- `MIGRATION_NOTES.md`
- `SCHEMA_MIGRATION.md`
- `FRONTEND_CHANGES.md`
