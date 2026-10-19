import json, sys, os, textwrap

fname = sys.argv[1]
path = sys.argv[2]
base = os.path.join(os.environ['HOME'], 'mnt/Nebula_Cursos_Web/_audit_scratch/u08', fname)
data = json.load(open(base, encoding='utf-8'))

def get(obj, path):
    import re
    tokens = re.findall(r'[^.\[\]]+|\[\d+\]', path)
    cur = obj
    for t in tokens:
        if t.startswith('['):
            idx = int(t[1:-1])
            cur = cur[idx]
        else:
            cur = cur[t]
    return cur

val = get(data, path)
if isinstance(val, str):
    print(textwrap.fill(val, 100))
else:
    print(json.dumps(val, ensure_ascii=False, indent=2))
