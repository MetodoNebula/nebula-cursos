# -*- coding: utf-8 -*-
import json, os, re
from collections import Counter

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
ORIG = os.path.join(BASE, "original/selectividad_fisica")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear"]
UNITS_AFTER = ["fundamentos"] + UNITS

def parse_hours(s):
    if not isinstance(s, str):
        return 0
    m = re.search(r"([\d,\.]+)\s*h", s)
    return float(m.group(1).replace(",", ".")) if m else 0

def load(base, units):
    out = {}
    for u in units:
        fp = os.path.join(base, f"selectividad_fisica__{u}.json")
        out[u] = json.load(open(fp, encoding="utf-8"))
    return out

before = load(ORIG, UNITS)
after = load(PILOT, UNITS_AFTER)

def count_lessons_over_45(data):
    n = 0
    for u, d in data.items():
        for bkey, lesson in d.items():
            if parse_hours(lesson.get("estimated_length")) > 0.75:  # > 45 min
                n += 1
    return n

def total_pieces(data, types):
    c = Counter()
    for u, d in data.items():
        for bkey, lesson in d.items():
            for t in types:
                c[t] += len(lesson.get(t, []))
    return c

PIECE_TYPES = ["worked_examples","guided_exercises","exercises","exam_questions","challenge_questions","mcq"]

before_counts = total_pieces(before, PIECE_TYPES)
after_counts = total_pieces(after, PIECE_TYPES)

# L4/L5 counts (difficulty field)
def l4_l5_counts(data):
    l4 = l5 = 0
    for u, d in data.items():
        for bkey, lesson in d.items():
            for c in ["exercises","guided_exercises","exam_questions"]:
                for it in lesson.get(c, []):
                    if isinstance(it, dict) and it.get("difficulty") == 4:
                        l4 += 1
                    if isinstance(it, dict) and it.get("difficulty") == 5:
                        l5 += 1
            for it in lesson.get("challenge_questions", []):
                l5 += 1  # challenge questions are L5 by construction
    return l4, l5

l4_before, l5_before = l4_l5_counts(before)
l4_after, l5_after = l4_l5_counts(after)

n_lessons_before = sum(len(d) for d in before.values())
n_lessons_after = sum(len(d) for d in after.values())

over45_before = count_lessons_over_45(before)
over45_after = count_lessons_over_45(after)

print("lecciones:", n_lessons_before, "->", n_lessons_after)
print("lecciones >45min:", over45_before, "->", over45_after)
print("worked_examples:", before_counts["worked_examples"], "->", after_counts["worked_examples"])
print("guided_exercises (faded examples):", before_counts["guided_exercises"], "->", after_counts["guided_exercises"])
print("exercises:", before_counts["exercises"], "->", after_counts["exercises"])
print("exam_questions:", before_counts["exam_questions"], "->", after_counts["exam_questions"])
print("challenge_questions:", before_counts["challenge_questions"], "->", after_counts["challenge_questions"])
print("mcq:", before_counts["mcq"], "->", after_counts["mcq"])
print("L4 items:", l4_before, "->", l4_after)
print("L5 items (challenge + difficulty5):", l5_before, "->", l5_after)

# checkpoints
ckpt = json.load(open(os.path.join(PILOT, "unit_checkpoints.json"), encoding="utf-8"))
print("checkpoints: 0 ->", len(ckpt["checkpoints"]))

# prerequisite links (count of prerequisites entries across lessons) before/after + knowledge graph edges
def prereq_count(data):
    n = 0
    for u, d in data.items():
        for bkey, lesson in d.items():
            n += len(lesson.get("prerequisites", []))
    return n
print("prerequisites declarados (entradas):", prereq_count(before), "->", prereq_count(after))
kg = json.load(open(os.path.join(PILOT, "KNOWLEDGE_GRAPH.json"), encoding="utf-8"))
print("prerequisite links explicitos en KNOWLEDGE_GRAPH.json: 0 ->", len(kg["edges"]))

# MCQ inconsistentes (no correct option) - from structural_qa_report
qa = json.load(open(os.path.join(BASE, "scripts/pilot_fisica/structural_qa_report.json"), encoding="utf-8"))
print("MCQ inconsistentes (sin opcion correcta valida): ? ->", len(qa["mcq_no_correct_option"]))

# P0/P1 ledger status
print("P0 resueltos: 2/2, P1 resueltos/verificados: 6/6 (ver CHANGELOG.md)")

# claims sin condiciones -> proxy: semantic lint totals (documented as non-precision metric) + 22 ledger items resolved
print("Ver semantic_lint_BEFORE.json / semantic_lint_AFTER.json para el detalle (metrica de recall, no de precision).")
