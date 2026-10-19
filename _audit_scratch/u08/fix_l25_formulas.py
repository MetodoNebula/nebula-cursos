import sys, re

PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"25_Polimerización')
i1 = data.find('"26_', i0)
seg = data[i0:i1]

a0 = seg.find('"assets": [')
a_end = seg.find('"keywords"', a0)
before = seg[:a0]
protected = seg[a0:a_end]
after = seg[a_end:]

D = chr(36)
def subn(n):
    if len(n) > 1:
        return D + chr(95) + "{" + n + "}" + D
    return D + chr(95) + n + D

def conv(token):
    # insert subscript markers after digit-runs that follow a letter or ')'
    out = []
    i = 0
    n = len(token)
    while i < n:
        c = token[i]
        out.append(c)
        if c.isalpha() or c == ')':
            j = i+1
            if j < n and token[j].isdigit():
                k = j
                while k < n and token[k].isdigit():
                    k += 1
                out.append(subn(token[j:k]))
                i = k
                continue
        i += 1
    return "".join(out)

raw_tokens = [
    "HOOC-C6H4-CO-O-CH2CH2-OH",
    "HOOC-C6H4-COOH",
    "CH3-CO-O-CH2-CH2-OH",
    "CH3-COOH",
    "HO-CH2CH2-OH",
    "CO-C6H4-CO-O-CH2-CH2-O-",
    "NH-(CH2)6-NH-CO-(CH2)4-CO-",
    "H2N-CHR-COOH",
    "HOOC-(CH2)4-COOH",
    "H2N-(CH2)6-NH2",
    "C10H8O4",
    "M(H2O)",
    "H2O",
    "CO2",
    "NH2",
    "NH3",
]
mapping = {t: conv(t) for t in raw_tokens}
order = sorted(mapping.keys(), key=lambda k: -len(k))

report = []
def apply(text, label):
    for k in order:
        c = text.count(k)
        if c:
            text = text.replace(k, mapping[k])
            report.append((label, k, c))
    return text

before2 = apply(before, "before")
after2 = apply(after, "after")
seg2 = before2 + protected + after2

for r in report:
    print(r)

data2 = data[:i0] + seg2 + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE formulas L25")
