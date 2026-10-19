import sys, re

PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"23_Condiciones')
i1 = data.find('"24_', i0)
seg = data[i0:i1]

a0 = seg.find('"assets": [', seg.find('theory_blocks'))
a_end = seg.find('"keywords"', a0)
assert a0 != -1 and a_end != -1
before = seg[:a0]
protected = seg[a0:a_end]
after = seg[a_end:]

D = chr(36)  # $

def sub(s):
    return D + chr(95) + s + D  # $_N$

pairs = {
    "CH3COOCH2CH3": "CH3" .replace("3", sub("3")) ,  # placeholder, overwritten below
}

# Build explicit mapping (old substring -> new with $_N$ subscripts)
mapping = {
    "CH3COOCH2CH3": "CH" + sub("3") + "COOCH" + sub("2") + "CH" + sub("3"),
    "CH3CH2OH": "CH" + sub("3") + "CH" + sub("2") + "OH",
    "CH3COOH": "CH" + sub("3") + "COOH",
    "CH2=C(CH3)2": "CH" + sub("2") + "=C(CH" + sub("3") + ")" + sub("2"),
    "CH3-CCl(CH3)2": "CH" + sub("3") + "-CCl(CH" + sub("3") + ")" + sub("2"),
    "CH3-COO-CH2-CH3": "CH" + sub("3") + "-COO-CH" + sub("2") + "-CH" + sub("3"),
    "CH3-COO-CH3": "CH" + sub("3") + "-COO-CH" + sub("3"),
    "CH2=CH-CH2-CH3": "CH" + sub("2") + "=CH-CH" + sub("2") + "-CH" + sub("3"),
    "CH2=CH-CH3": "CH" + sub("2") + "=CH-CH" + sub("3"),
    "CH2=CH2": "CH" + sub("2") + "=CH" + sub("2"),
    "CH2=CHCl": "CH" + sub("2") + "=CHCl",
    "CH2Br-CHBr-CH3": "CH" + sub("2") + "Br-CHBr-CH" + sub("3"),
    "CH2-CH(CH3)-": "CH" + sub("2") + "-CH(CH" + sub("3") + ")-",
    "CH2-CHCl-": "CH" + sub("2") + "-CHCl-",
    "CH3-CH(OH)-CH2-CH3": "CH" + sub("3") + "-CH(OH)-CH" + sub("2") + "-CH" + sub("3"),
    "CH3-CH(OH)-CH3": "CH" + sub("3") + "-CH(OH)-CH" + sub("3"),
    "CH3-CH2-CH2-Br": "CH" + sub("3") + "-CH" + sub("2") + "-CH" + sub("2") + "-Br",
    "CH3-CH2-Br": "CH" + sub("3") + "-CH" + sub("2") + "-Br",
    "CH3-CH2-CH3": "CH" + sub("3") + "-CH" + sub("2") + "-CH" + sub("3"),
    "CH3-CH2-OH": "CH" + sub("3") + "-CH" + sub("2") + "-OH",
    "CH3-CH3": "CH" + sub("3") + "-CH" + sub("3"),
    "CH3-CH=CH-CH3": "CH" + sub("3") + "-CH=CH-CH" + sub("3"),
    "CH3-CHBr-CH3": "CH" + sub("3") + "-CHBr-CH" + sub("3"),
    "CH3-COOH": "CH" + sub("3") + "-COOH",
    "CH3-OH": "CH" + sub("3") + "-OH",
    "C2H6O": "C" + sub("2") + "H" + sub("6") + "O",
    "C2H4": "C" + sub("2") + "H" + sub("4"),
    "CCl4": "CCl" + sub("4"),
    "K2Cr2O7": "K" + sub("2") + "Cr" + sub("2") + "O" + sub("7"),
    "Cr2O7": "Cr" + sub("2") + "O" + sub("7"),
    "H2SO4": "H" + sub("2") + "SO" + sub("4"),
    "KMnO4": "KMnO" + sub("4"),
    "HNO3": "HNO" + sub("3"),
    "FeX3": "FeX" + sub("3"),
    "NH3": "NH" + sub("3"),
    "CO2": "CO" + sub("2"),
    "H2O": "H" + sub("2") + "O",
    "Br2": "Br" + sub("2"),
    "H2": "H" + sub("2"),
    "O2": "O" + sub("2"),
    "X2": "X" + sub("2"),
}

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
print("DONE formulas")
