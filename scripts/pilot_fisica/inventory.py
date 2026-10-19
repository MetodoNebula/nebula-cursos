# -*- coding: utf-8 -*-
import json, re, os, hashlib, sys
from collections import defaultdict, Counter

BASE = os.environ.get("NEBULA_BASE", os.path.expanduser("~/mnt/Nebula_Cursos_Web"))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "original", "selectividad_fisica")
LABEL = sys.argv[2] if len(sys.argv) > 2 else "BEFORE"

UNITS = ["campo_gravitatorio", "mas", "ondas", "electromagnetismo", "optica",
         "relatividad", "cuantica", "nuclear"]

PIECE_TYPES = ["objectives","prerequisites","diagnostic_items","theory_blocks","keywords",
               "worked_examples","guided_exercises","exercises","exam_questions",
               "challenge_questions","mcq","flashcards","misconceptions","common_mistakes","exam_notes"]

MATH_RE = re.compile(r"\$[^$]*\$")
MD_RE = re.compile(r"[*_`#]")
WORD_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{1,}")

def prose_words(s):
    if not isinstance(s, str) or not s.strip():
        return 0
    s = MATH_RE.sub(" ", s)
    s = MD_RE.sub(" ", s)
    return len(WORD_RE.findall(s))

def collect_strings(obj, acc):
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("id","ids","type","kind","key","correct","provenance","scope","bloom",
                      "concept_id","concept_ids","objective_id","objective_ids",
                      "related_exercises","related_misconception","blocking",
                      "source_induced","misconception_id","lang","framework","codes",
                      "status","track","difficulty","marks","level"):
                continue
            collect_strings(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            collect_strings(v, acc)

PROSE_FIELDS = ["objectives","theory_blocks","keywords","worked_examples","guided_exercises",
                 "exercises","exam_questions","challenge_questions","mcq","flashcards",
                 "misconceptions","common_mistakes","exam_notes","summary"]

def lesson_prose_word_count(lesson):
    acc = []
    for field in PROSE_FIELDS:
        v = lesson.get(field)
        if v is not None:
            collect_strings(v, acc)
    return sum(prose_words(s) for s in acc)

def parse_hours(estimated_length):
    if not estimated_length:
        return None
    s = str(estimated_length).replace(",", ".").lower()
    m = re.search(r"([\d.]+)", s)
    if not m:
        return None
    return float(m.group(1))

report = {
    "label": LABEL, "units": {}, "totals": Counter(), "lessons": [],
    "duplicates": [], "long_lessons": [], "overload_lessons": [],
}

all_ids_per_unit = defaultdict(Counter)
content_hashes = defaultdict(list)

for unit in UNITS:
    fp = os.path.join(SRC, f"selectividad_fisica__{unit}.json")
    if not os.path.exists(fp):
        print("MISSING", fp); continue
    with open(fp, encoding="utf-8") as f:
        data = json.load(f)
    unit_piece_counts = Counter()
    unit_words = 0
    for bkey, lesson in data.items():
        words = lesson_prose_word_count(lesson)
        unit_words += words
        hours = parse_hours(lesson.get("estimated_length"))
        piece_counts = {}
        for pt in PIECE_TYPES:
            v = lesson.get(pt)
            n = len(v) if isinstance(v, list) else 0
            piece_counts[pt] = n
            unit_piece_counts[pt] += n
            report["totals"][pt] += n
        lesson_id = lesson.get("id")
        all_ids_per_unit[unit][lesson_id] += 1
        bodies = [tb.get("body","") for tb in (lesson.get("theory_blocks") or [])]
        h = hashlib.sha1((lesson.get("title","") + "||" + "".join(bodies)).encode("utf-8")).hexdigest()
        content_hashes[h].append((unit, bkey))

        rec = {"unit": unit, "bkey": bkey, "id": lesson_id, "title": lesson.get("title"),
               "estimated_length": lesson.get("estimated_length"), "hours": hours,
               "difficulty": lesson.get("estimated_difficulty"), "words": words,
               "piece_counts": piece_counts}
        report["lessons"].append(rec)
        if words >= 12000:
            report["long_lessons"].append(rec)
        if hours and hours > 0:
            rate = words / hours
            if rate >= 9000:
                report["overload_lessons"].append({**rec, "words_per_hour": round(rate)})
    report["units"][unit] = {"n_lessons": len(data), "words": unit_words,
                               "piece_counts": dict(unit_piece_counts)}

report["duplicates"] = [locs for locs in content_hashes.values() if len(locs) > 1]
dup_ids_per_unit = {u: {k:v for k,v in c.items() if v>1} for u,c in all_ids_per_unit.items()}
report["duplicate_lesson_ids_within_unit"] = {u:d for u,d in dup_ids_per_unit.items() if d}
report["n_units"] = len(report["units"])
report["n_lessons_total"] = len(report["lessons"])
report["words_total"] = sum(u["words"] for u in report["units"].values())

outpath = os.path.join(BASE, "scripts", "pilot_fisica", f"inventory_{LABEL}.json")
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("OK ->", outpath)
print("units:", report["n_units"], "lessons:", report["n_lessons_total"], "words(prose):", report["words_total"])
print("long_lessons(>=12000w):", len(report["long_lessons"]))
print("overload_lessons(>=9000w/h):", len(report["overload_lessons"]))
for r in report["overload_lessons"]:
    print("   OVERLOAD:", r["unit"], r["bkey"], r["words"], "words /", r["hours"], "h =", r["words_per_hour"], "w/h")
print("duplicate content groups:", len(report["duplicates"]))
print("duplicate ids within same unit:", report["duplicate_lesson_ids_within_unit"])
for k,v in report["totals"].items():
    print(" ", k, v)
