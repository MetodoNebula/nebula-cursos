# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__cuantica.json")
d = json.load(open(fp, encoding="utf-8"))

def walk(obj, path, pattern, hits):
    if isinstance(obj, str):
        if re.search(pattern, obj, re.IGNORECASE):
            hits.append((path, obj))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, path + "." + k, pattern, hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, path + f"[{i}]", pattern, hits)

print("=== produccion de pares ===")
for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"producci.n de pares|par.*electr.n.*positr.n|2mc", hits)
    for p,t in hits: print(p,'::', t[:200].replace(chr(10),' '))

print()
print("=== de Broglie h/mv ===")
for bkey, lesson in d.items():
    hits=[]
    walk(lesson, bkey, r"h/mv|h/\(mv\)|lambda\s*=\s*h", hits)
    for p,t in hits: print(p,'::', t[:200].replace(chr(10),' '))

print()
print("=== dimensional / conjugad ===")
lesson06 = d["06_Indeterminación_y_la_nueva_mecánica_cuántica.json"]
hits=[]
walk(lesson06, "06", r"dimensional|conjugad", hits)
for p,t in hits: print(p,'::', t[:250].replace(chr(10),' '))
