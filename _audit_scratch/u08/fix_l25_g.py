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
SIGMA = chr(931)
CDOT = chr(183)

# F4a: flashcards[7].back
old = '"back": "M_oligómero = ' + SIGMA + ' M_monómeros - (k-1)' + CDOT + 'M(H2O).",'
new = '"back": "$M_{' + BS + 'text{oligómero}} = ' + BS + 'sum M_{' + BS + 'text{monómeros}} - (k-1)' + BS + 'cdot M(H_2O)$.",'
rep(old, new, 1, "F4a flashcards7")

# F4b: exam_questions[1].answer
old = '"(a) M_olig = nM1+nM2-(2n-1)' + CDOT + '18,015. (b) M_olig ' + chr(8776) + ' 1376 g/mol."'
new = '"(a) $M_{' + BS + 'text{olig}} = nM_1+nM_2-(2n-1)' + BS + 'cdot18{,}015$. (b) $M_{' + BS + 'text{olig}}' + BS + 'approx1376$ g/mol."'
rep(old, new, 1, "F4b exam_questions1 answer")

# F4c: exercises[1].answer
old = '"Se liberan 19 moléculas de agua; M_oligómero = 2000,0-342,3=1657,7 g/mol."'
new = '"Se liberan 19 moléculas de agua; $M_{' + BS + 'text{oligómero}} = 2000{,}0-342{,}3=1657{,}7$ g/mol."'
rep(old, new, 1, "F4c exercises1 answer")

# F4d: worked_examples[3].solution
old = '"(a) 99 moléculas de H2O. (b) M = 50(166,13)+50(62,07)-99(18,015) = 11410,0-1783,5=9627 g/mol ' + chr(8776) + ' 9,63' + CDOT + '10^3 g/mol."'
new = '"(a) 99 moléculas de $H_2O$. (b) $M = 50(166{,}13)+50(62{,}07)-99(18{,}015) = 11410{,}0-1783{,}5=9627$ g/mol $' + BS + 'approx9{,}63' + BS + 'cdot10^{3}$ g/mol."'
rep(old, new, 1, "F4d worked_examples3 solution")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE G")
