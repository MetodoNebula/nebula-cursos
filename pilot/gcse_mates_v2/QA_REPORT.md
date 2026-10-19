# QA Report — GCSE Mathematics Pilot v2

**Course:** `gcse_mates`
**Date:** 2026-10-19
**Auditor:** Claude (automated + manual review)

---

## 1. Scope

Full 6-phase pilot audit and migration for Cambridge IGCSE Mathematics 0580,
covering 10 bundles (U00–U09), 93 lessons, and all associated assessment,
metadata, and SVG assets.

## 2. Validation Gates

| Gate | Check | Result |
|------|-------|--------|
| 1 | JSON valid in all 10 bundles | PASS |
| 2 | All 93 canonical_lesson_id unique | PASS |
| 3 | 0 MEZCLA violations | PASS |
| 4 | MCQ correct indices valid (bundles + assessments) | PASS |
| 5 | All 153 SVGs pass XML validation | PASS |
| 6 | Assessment references point to existing lessons | PASS |
| 7 | Content preserved vs original (exercise/MCQ/flashcard counts) | PASS |
| 8 | MCQ distractors have why_wrong | WARN (99.8% — 3 missing in U00) |

**Result: 7/8 PASS, 1 non-blocking WARN**

## 3. Content Summary

| Metric | Value |
|--------|-------|
| Bundles | 10 (9 modified + 1 new U00) |
| Lessons (total) | 93 (87 original + 6 foundations) |
| Theory blocks | 883 |
| Exercises | 2,587 |
| MCQs | 457 |
| Flashcards | 989 |
| Worked examples | 468 |
| SVGs total | 153 (130 existing + 23 new) |
| schema_v2 coverage | 93/93 (100%) |
| MEZCLA violations remaining | 0 (16 fixed) |
| Scope coverage | 100% |

## 4. Phase Completion

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Semantic Change Ledger | COMPLETE — 19 entries (4 P0, 5 P1, 10 P2) |
| 2 | Scope + MEZCLA fixes | COMPLETE — 16 violations fixed, 100% scope coverage |
| 3 | schema_v2 (canonical IDs + routes) | COMPLETE — 93 lessons with IDs and routes |
| 4 | Module Foundations (U00) | COMPLETE — 6 micro-lessons |
| 5 | Assessment files | COMPLETE — diagnostic + checkpoints + exam_mode |
| 6 | SVG diagrams | COMPLETE — 23 lessons updated, 153 total SVGs |

## 5. Assessment Files

| File | Items | Details |
|------|-------|---------|
| diagnostic.json | 18 | 6 axes × 3 items, pre-course placement test |
| unit_checkpoints.json | 36 | 3–5 MCQ per unit (U01–U09) |
| exam_mode.json | 83 | 29 by_topic + 15 mixed + 39 timed papers (3 papers) |

## 6. Semantic Change Ledger Summary

- **P0 (factual errors):** 4 entries — currency conversion heuristic (×2), difference definition, randomness/independence conflation
- **P1 (pedagogical):** 5 entries — enrichment content mixed with core pathway (×4), missing worked solutions
- **P2 (editorial):** 10 entries — provenance labels in mixed practice banks across all 9 units

## 7. Known Limitations

1. **P0–P1 ledger entries not yet applied to bundle content.** The ledger documents the issues and prescribed fixes; applying them is deferred to a subsequent editorial pass to avoid risk of data corruption during the structural migration.
2. **3 MCQ distractors in U00** missing `why_wrong` field (non-blocking, 99.8% overall coverage).
3. **SVG assets** may need manual review for mathematical accuracy of complex diagrams.
4. **Mixed practice banks** retain editorial provenance labels (P2 items); cleanup deferred.
5. **Epistemic overrides** are heuristic-based and may need manual review for accuracy.

## 8. Deliverables

```
pilot/gcse_mates_v2/
├── bundles/
│   ├── gcse_mates__U00_Foundations.json       (NEW — 6 lessons)
│   ├── gcse_mates__U01_Number.json            (MODIFIED — 18 lessons)
│   ├── gcse_mates__U02_Algebra_and_Graphs.json (MODIFIED — 21 lessons)
│   ├── gcse_mates__U03_Coordinate_Geometry.json (MODIFIED — 7 lessons)
│   ├── gcse_mates__U04_Geometry.json          (MODIFIED — 9 lessons)
│   ├── gcse_mates__U05_Mensuration.json       (MODIFIED — 6 lessons)
│   ├── gcse_mates__U06_Trigonometry.json      (MODIFIED — 8 lessons)
│   ├── gcse_mates__U07_Transformations_and_Vectors.json (MODIFIED — 5 lessons)
│   ├── gcse_mates__U08_Probability.json       (MODIFIED — 5 lessons)
│   └── gcse_mates__U09_Statistics.json        (MODIFIED — 8 lessons)
├── semantic_change_ledger.json
├── diagnostic.json
├── unit_checkpoints.json
├── exam_mode.json
├── catalog_patch_gcse_maths.json
├── KNOWLEDGE_GRAPH.json
├── phase2_3_report.json
├── QA_REPORT.md
├── CHANGELOG.md
├── SCHEMA_MIGRATION.md
├── FRONTEND_CHANGES.md
└── MIGRATION_NOTES.md
```

## 9. Recommendation

The pilot bundle is ready for **internal review and testing**. Before publishing:

1. Review P0 fixes in the semantic change ledger and apply to affected lessons
2. Spot-check generated SVG diagrams for mathematical accuracy
3. Encrypt all bundles: `node cifrar.js` (password: `Nebula123!`)
4. Test the complete flow in the Nebula viewer
5. Deploy to GitHub Pages
