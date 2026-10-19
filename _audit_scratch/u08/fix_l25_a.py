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

# F1: exercises[3].answer + full_solution full rewrite
old_ans = '"answer": "192,17 g/mol."'
new_ans = ('"answer": "(a) HOOC-C6H4-COOH + HO-CH2CH2-OH ' + BS + 'rightarrow HOOC-C6H4-CO-O-CH2CH2-OH + H2O. '
           '(b) [-CO-C6H4-CO-O-CH2-CH2-O-]n (C10H8O4). (c) 192,17 g/mol."')
rep(old_ans, new_ans, 1, "F1 answer")

old_fs = '"full_solution": "$M=166{,}13+62{,}08-2(18{,}02)=192{,}17$ g/mol."'
new_fs = ('"full_solution": "(a) $' + BS[0:0] + 'mathrm{HOOC' + BS + 'text{-}C_6H_4' + BS + 'text{-}COOH + HO' + BS + 'text{-}CH_2CH_2' + BS + 'text{-}OH '
          + BS + 'rightarrow HOOC' + BS + 'text{-}C_6H_4' + BS + 'text{-}CO' + BS + 'text{-}O' + BS + 'text{-}CH_2CH_2' + BS + 'text{-}OH + H_2O}$. '
          '(b) La unidad repetitiva es $' + BS + 'mathrm{' + BS + 'left[' + BS + 'text{-}CO' + BS + 'text{-}C_6H_4' + BS + 'text{-}CO' + BS + 'text{-}O' + BS + 'text{-}CH_2' + BS + 'text{-}CH_2' + BS + 'text{-}O' + BS + 'text{-}' + BS + 'right]_n}$ (C$_{10}$H$_8$O$_4$). '
          '(c) $M=166{,}13+62{,}07-2' + BS + 'cdot18{,}015=192{,}17$ g/mol (usando las masas exactas del enunciado: 62,07 para el etilenglicol y 18,015 para el agua)."')
rep(old_fs, new_fs, 1, "F1 full_solution")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE A")
