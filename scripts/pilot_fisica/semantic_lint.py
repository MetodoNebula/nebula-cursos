# -*- coding: utf-8 -*-
import json, re, os, sys
from collections import Counter, defaultdict

BASE = os.environ.get("NEBULA_BASE", os.path.expanduser("~/mnt/Nebula_Cursos_Web"))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "original", "selectividad_fisica")
LABEL = sys.argv[2] if len(sys.argv) > 2 else "BEFORE"

UNITS = ["campo_gravitatorio", "mas", "ondas", "electromagnetismo", "optica",
         "relatividad", "cuantica", "nuclear"]

FLAGS = ["siempre","nunca","solo","sólo","cualquier","garantiza","exactamente","por definición",
         "en todos los casos","jamás","todo cuerpo","toda partícula"]

FLAG_RE = re.compile(r"\b(" + "|".join(re.escape(f) for f in FLAGS) + r")\b", re.IGNORECASE)
PROSE_FIELDS = ["objectives","theory_blocks","keywords","worked_examples","guided_exercises",
                 "exercises","exam_questions","challenge_questions","mcq","flashcards",
                 "misconceptions","common_mistakes","exam_notes","summary"]

def walk(obj, path, hits):
    if isinstance(obj, str):
        for m in FLAG_RE.finditer(obj):
            start = max(0, m.start()-60)
            end = min(len(obj), m.end()+60)
            hits.append((path, m.group(1), obj[start:end].replace("\n"," ")))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, path + "." + k, hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, path + f"[{i}]", hits)

all_hits = defaultdict(list)
counter = Counter()
for unit in UNITS:
    fp = os.path.join(SRC, f"selectividad_fisica__{unit}.json")
    with open(fp, encoding="utf-8") as f:
        data = json.load(f)
    for bkey, lesson in data.items():
        for field in PROSE_FIELDS:
            v = lesson.get(field)
            if v is None:
                continue
            hits = []
            walk(v, field, hits)
            for path, term, ctx in hits:
                counter[term.lower()] += 1
                all_hits[(unit, bkey)].append((path, term, ctx))

total = sum(counter.values())
print("TOTAL FLAGGED OCCURRENCES:", total)
for term, n in counter.most_common():
    print(f"  {term}: {n}")
print("lessons with >=1 flagged term:", len(all_hits))

outpath = os.path.join(BASE, "scripts", "pilot_fisica", f"semantic_lint_{LABEL}.json")
out = {"total": total, "by_term": dict(counter),
       "by_lesson": {f"{u}/{b}": [{"path":p,"term":t,"context":c} for p,t,c in hits]
                      for (u,b), hits in all_hits.items()}}
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("->", outpath)
