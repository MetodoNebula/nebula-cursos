import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"25_Polimerización')
i1 = data.find('"26_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

old1 = "de masas M1=110,0 g/mol y M2=90,0 g/mol respectivamente."
new1 = "de masas $M_1=110{,}0$ g/mol y $M_2=90{,}0$ g/mol respectivamente."
rep(old1, new1, 1, "exercises1 statement M1M2")

old2 = "con n=6 (M1=146,14; M2=116,21) y calcula esa masa."
new2 = "con n=6 ($M_1=146{,}14$; $M_2=116{,}21$) y calcula esa masa."
rep(old2, new2, 1, "exam_questions1 statement M1M2")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE M")
