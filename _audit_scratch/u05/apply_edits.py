import json, sys

PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

def raw(s):
    return json.dumps(s, ensure_ascii=False)[1:-1]

def apply(edits, path=PATH, dry=False):
    data = open(path, encoding="utf-8").read()
    results = []
    for label, old_dec, new_dec in edits:
        old_r = raw(old_dec)
        new_r = raw(new_dec)
        n = data.count(old_r)
        results.append((label, n))
        if n == 1:
            data = data.replace(old_r, new_r, 1)
        else:
            print(f"ABORT at '{label}': occurrences={n}")
            for lb, cnt in results:
                print(f"  {lb}: {cnt}")
            return False
    if not dry:
        open(path, "w", encoding="utf-8").write(data)
    print("ALL OK:")
    for lb, cnt in results:
        print(f"  {lb}: {cnt}")
    return True
