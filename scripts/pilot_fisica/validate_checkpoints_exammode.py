# -*- coding: utf-8 -*-
import json, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear","fundamentos"]

# Build a global index: canonical_lesson_id -> set of all item ids present anywhere in that lesson
index = {}
CONTAINERS = ["worked_examples","guided_exercises","exercises","exam_questions","challenge_questions",
              "mcq","diagnostic_items","flashcards","misconceptions","common_mistakes","theory_blocks"]
for unit in UNITS:
    fp = os.path.join(PILOT, f"selectividad_fisica__{unit}.json")
    d = json.load(open(fp, encoding="utf-8"))
    for bkey, lesson in d.items():
        cid = lesson["schema_v2"]["canonical_lesson_id"]
        ids = set()
        for c in CONTAINERS:
            for it in lesson.get(c, []):
                if isinstance(it, dict) and it.get("id"):
                    ids.add(it["id"])
        index[cid] = ids

def check_refs(refs, label):
    bad = []
    for r in refs:
        cid = r.get("ref_lesson")
        iid = r.get("item_id")
        if cid not in index:
            bad.append((label, cid, iid, "lesson not found"))
        elif iid not in index[cid]:
            bad.append((label, cid, iid, "item not found in lesson"))
    return bad

bad_all = []

ckpt = json.load(open(os.path.join(PILOT, "unit_checkpoints.json"), encoding="utf-8"))
for c in ckpt["checkpoints"]:
    bad_all += check_refs([{"ref_lesson": it["ref_lesson"], "item_id": it["item_id"]} for it in c["items"]], c["checkpoint_id"])

diag = json.load(open(os.path.join(PILOT, "diagnostic.json"), encoding="utf-8"))
bad_all += check_refs(diag["diagnostic_items"], "diagnostic")

exam = json.load(open(os.path.join(PILOT, "exam_mode.json"), encoding="utf-8"))
for u, items in exam["topic_questions"].items():
    bad_all += check_refs(items, f"topic:{u}")
bad_all += check_refs(exam["mixed_questions"], "mixed")
bad_all += check_refs(exam["timed_questions"], "timed")
for m in exam["partial_mock_exams"] + exam["full_mock_exams"]:
    bad_all += check_refs(m["items"], m["mock_id"])

print("Total referencias rotas:", len(bad_all))
for b in bad_all[:30]:
    print(" -", b)
