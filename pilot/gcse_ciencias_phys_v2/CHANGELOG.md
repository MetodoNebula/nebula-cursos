# Changelog — GCSE Physics Pilot v2

## [2.0.0] — 2026-10-20

### Phase 1: Semantic Audit & P0 Corrections
- Created `semantic_change_ledger.json` with 67 entries (1 P0, 62 P1, 4 P2)
- **P0 fix:** Added negligible-losses caveat to energy conservation key_points in U04
- Cleaned 14 syllabus code references (0654/0625 → "this course" / "GCSE")
- Removed 128 editorial labels (source_book, source_chapter, source_page, source_number) from exercises

### Phase 2: Scope & Essential-First Ordering
- Verified `scope` field present on all 264+ theory_blocks across U01–U10
- Fixed 25 MEZCLA violations (ADVANCED/ENRICHMENT blocks reordered after CORE blocks)
- Maintained relative order within each scope group

### Phase 3: schema_v2 Migration
- Added `schema_v2` to all 62 existing lessons (68 total with U00)
- Generated 68 unique `canonical_lesson_id` values (prefix: GCSEPHYS)
- Assigned `recommended_routes` (DESDE_CERO, STANDARD, EXCELLENCE, FAST_REVIEW) to every lesson
- `epistemic_overrides` field present (empty by default, populated where audit flagged issues)

### Phase 4: U00 Foundations Module
- Created 6 new micro-lessons covering prerequisite skills:
  1. Units, prefixes and scientific notation
  2. Rearranging equations
  3. Reading and plotting graphs
  4. Proportionality and ratios
  5. Estimating and checking
  6. Laboratory skills and safety
- Each lesson includes: thorough theory blocks, 2–3 worked examples, guided exercises, 3–4 exercises, 4–5 MCQs, SVG diagrams
- Total new content: 19 theory blocks, 14 worked examples, 8 guided exercises, 19 exercises, 25 MCQs, 6 SVGs
- Created `catalog_patch_gcse_phys.json` for catalog integration

### Phase 5: Assessment Files
- `unit_checkpoints.json` — 3–5 targeted questions per unit
- `diagnostic.json` — 15–20 placement items spanning all units
- `exam_mode.json` — Exam simulation with:
  - `by_topic`: 45 questions across 9 units (5 per unit), covering calculation, explain, describe types
  - `mixed`: 18 cross-topic questions for randomised practice
  - `timed_papers`: 2 full-length 90-minute papers (65 questions total with mark schemes and worked solutions)
  - Every question includes: stem, mark_scheme (mark-by-mark), worked_solution, tier (core/higher), marks

### Phase 6: SVG Diagrams
- Audited all lessons for SVG presence
- Created/verified diagrams for lessons previously missing them
- All 82 SVGs pass XML well-formedness validation
- Nebula palette enforced: teal #0e7a68, amber #c17a17, plum #8a3d6b

### Content Integrity
- **No content trimmed** — all existing theory, examples, and exercises preserved
- All modifications are additive (schema_v2) or correctional (P0/P1 fixes)
- Original lesson structure (id, title, theory_blocks, exercises, mcq) untouched
