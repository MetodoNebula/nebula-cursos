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
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+250]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

BS = chr(92)*2
NL = chr(92)+'n'

# F2 (PET): add n-equation and bracket structural unit after the existing formula line in tb2
old = "$C_8H_6O_4 + C_2H_6O_2 - 2" + BS + ",H_2O " + BS + "rightarrow C_{10}H_8O_4 " + BS + "quad (M=192{,}17" + BS + "\\ " + BS + "text{g/mol})$"
# try simpler without escaped-space complexity first
print("probe", seg.count("C_{10}H_8O_4"))
