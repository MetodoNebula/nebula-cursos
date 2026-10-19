import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
seg = data[i0:i1]

a0 = seg.find('"assets": [')
a_end = seg.find('"keywords"', a0)
before = seg[:a0]
protected = seg[a0:a_end]
after = seg[a_end:]

D = chr(36)
def sub(s):
    return D + chr(95) + s + D

mapping = {
    "CH3-CH2-CH2-CH2-OH": "CH"+sub("3")+"-CH"+sub("2")+"-CH"+sub("2")+"-CH"+sub("2")+"-OH",
    "CH3-(CH2)4-CH2-OH": "CH"+sub("3")+"-(CH"+sub("2")+")"+sub("4")+"-CH"+sub("2")+"-OH",
    "CH3(CH2)5OH": "CH"+sub("3")+"(CH"+sub("2")+")"+sub("5")+"OH",
    "CH3(CH2)4COOH": "CH"+sub("3")+"(CH"+sub("2")+")"+sub("4")+"COOH",
    "CH3CH2CH2NH2": "CH"+sub("3")+"CH"+sub("2")+"CH"+sub("2")+"NH"+sub("2"),
    "CH3CH2COOH": "CH"+sub("3")+"CH"+sub("2")+"COOH",
    "HO-CH2-CH2-OH": "HO-CH"+sub("2")+"-CH"+sub("2")+"-OH",
    "HOCH2CH2OH": "HOCH"+sub("2")+"CH"+sub("2")+"OH",
    "CH3-CH2-OH": "CH"+sub("3")+"-CH"+sub("2")+"-OH",
    "CH3-COOH": "CH"+sub("3")+"-COOH",
    "CH3-O-CH3": "CH"+sub("3")+"-O-CH"+sub("3"),
    "CH3COOH": "CH"+sub("3")+"COOH",
    "(CH3)3N": "(CH"+sub("3")+")"+sub("3")+"N",
    "C2H4O2": "C"+sub("2")+"H"+sub("4")+"O"+sub("2"),
    "C2H6O": "C"+sub("2")+"H"+sub("6")+"O",
    "C3H9N": "C"+sub("3")+"H"+sub("9")+"N",
    "HCOOCH3": "HCOOCH"+sub("3"),
    "CH2-": "CH"+sub("2")+"-",
    "CH3": "CH"+sub("3"),
}
order = sorted(mapping.keys(), key=lambda k: -len(k))

report = []
def apply(text, label):
    for k in order:
        c = text.count(k)
        if c:
            text = text.replace(k, mapping[k])
            report.append((label,k,c))
    return text

before2 = apply(before, "before")
after2 = apply(after, "after")
seg2 = before2 + protected + after2

for r in report: print(r)

data2 = data[:i0] + seg2 + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE formulas L24")
