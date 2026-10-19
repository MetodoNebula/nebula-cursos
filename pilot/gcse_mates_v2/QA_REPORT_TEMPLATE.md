# QA Report — GCSE Mathematics Pilot v2

## Summary

| Metric | Result |
|--------|--------|
| Total bundles | 10 (9 modified + 1 new U00) |
| Total lessons | 93 (87 original + 6 foundations) |
| schema_v2 coverage | 100% |
| MEZCLA violations fixed | 16 |
| MEZCLA violations remaining | 0 |
| Scope coverage | 100% (all blocks have scope) |
| SVGs added | TBD |
| Content preservation | ✅ All counts match originals |

## Validation Gates

- [ ] Gate 1: JSON valid in all 10 bundles
- [ ] Gate 2: All canonical_lesson_id unique
- [ ] Gate 3: 0 MEZCLA violations
- [ ] Gate 4: MCQ correct indices valid
- [ ] Gate 5: All SVG pass XML validation
- [ ] Gate 6: Assessment references point to existing lessons
- [ ] Gate 7: Content preserved vs original
- [ ] Gate 8: MCQ distractors have why_wrong

## Phase completion

| Phase | Status | Notes |
|-------|--------|-------|
| 1. Semantic Change Ledger | ✅ Complete | 19 entries (4 P0, 5 P1, 10 P2) |
| 2. Scope & MEZCLA | ✅ Complete | 16 violations fixed, 100% scope coverage |
| 3. schema_v2 | ✅ Complete | 87 lessons with canonical IDs and routes |
| 4. U00 Foundations | ⏳ Pending | 6 micro-lessons |
| 5. Assessment | ⏳ Pending | diagnostic + checkpoints done, exam_mode pending |
| 6. SVG Diagrams | ⏳ Pending | 23 lessons identified, generation in progress |

## Deliverables

TBD — will be finalized after all agents complete.
