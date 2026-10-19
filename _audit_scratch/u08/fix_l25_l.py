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

old = "M_olig = nM1+nM2-(2n-1)(18,015)."
new = "$M_{" + BS + "text{olig}} = nM_1+nM_2-(2n-1)(18{,}015)$."
rep(old, new, 1, "exam_questions1 full_solution part a")

old2 = "Por tanto, M_olig=1574,10-198,17=1375,9" + chr(8776) + "1376 g/mol."
new2 = "Por tanto, $M_{" + BS + "text{olig}}=1574{,}10-198{,}17=1375{,}9" + BS + "approx1376$ g/mol."
rep(old2, new2, 1, "exam_questions1 full_solution part b")

old3 = "nM1+nM2 = 6(146,14)+6(116,21)=876,84+697,26=1574,10 g/mol."
new3 = "$nM_1+nM_2 = 6(146,14)+6(116,21)=876{,}84+697{,}26=1574{,}10$ g/mol."
rep(old3, new3, 1, "exam_questions1 full_solution nM1nM2")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE L")
