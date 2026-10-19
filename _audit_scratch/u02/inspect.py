import json, sys
F = sys.argv[1]
lesson_key = sys.argv[2]
path = sys.argv[3]  # e.g. theory_blocks[1].body  or guided_exercises[0]
d = json.load(open(F, encoding='utf-8'))
obj = d[lesson_key]
import re
cur = obj
for part in re.findall(r'([^\[\.\]]+)(\[(\d+)\])?', path):
    key, idxfull, idx = part
    if key:
        cur = cur[key]
    if idx != '':
        cur = cur[int(idx)]
print(json.dumps(cur, ensure_ascii=False, indent=2))
