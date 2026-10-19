# -*- coding: utf-8 -*-
import json, os
from collections import Counter
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
UNITS = ["campo_gravitatorio","mas","ondas","electromagnetismo","optica","relatividad","cuantica","nuclear"]
diffs = Counter()
guided_keys=None
chall_keys=None
for u in UNITS:
    fp = os.path.join(BASE, f"selectividad_fisica__{u}.json")
    d = json.load(open(fp, encoding="utf-8"))
    for bkey, lesson in d.items():
        for ex in lesson.get("exercises", []):
            diffs[ex.get("difficulty")] += 1
        if lesson.get("guided_exercises") and guided_keys is None:
            guided_keys = list(lesson["guided_exercises"][0].keys())
        if lesson.get("challenge_questions") and chall_keys is None:
            chall_keys = list(lesson["challenge_questions"][0].keys())
print("exercises difficulty distribution:", diffs)
print("guided_exercises keys:", guided_keys)
print("challenge_questions keys:", chall_keys)
