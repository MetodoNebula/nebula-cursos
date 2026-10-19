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

def tex(s):
    # replace LaTeX command markers written as @cmd with BS+cmd
    return s.replace("@", BS)

# ---- PET (theory_blocks[2]) ----
old_pet = "$C_8H_6O_4 + C_2H_6O_2 - 2" + BS + ",H_2O " + BS + "rightarrow C_{10}H_8O_4 " + BS + "quad (M=192{,}17" + BS + " " + BS + "text{g/mol})$"

eq_pet = tex("$n@,@mathrm{HOOC@text{-}C_6H_4@text{-}COOH}+n@,@mathrm{HO@text{-}CH_2CH_2@text{-}OH}@rightarrow @mathrm{H@text{-}[O@text{-}CO@text{-}C_6H_4@text{-}CO@text{-}O@text{-}CH_2CH_2]_n@text{-}OH}+(2n-1)@,H_2O$")
unit_pet = tex("$@mathrm{@left[@text{-}CO@text{-}C_6H_4@text{-}CO@text{-}O@text{-}CH_2@text{-}CH_2@text{-}O@text{-}@right]_n}$")

new_pet = old_pet + NL + NL + "La ecuación completa de polimerización, con n moléculas de cada monómero, es:" + NL + NL + eq_pet + NL + NL + "y su unidad repetitiva, marcando el enlace éster que se repite una y otra vez:" + NL + NL + unit_pet

rep(old_pet, new_pet, 1, "F2 PET bracket unit")

# ---- Nailon-6,6 (theory_blocks[3]) ----
old_nyl = "$C_6H_{10}O_4 + C_6H_{16}N_2 - 2" + BS + ",H_2O " + BS + "rightarrow C_{12}H_{22}N_2O_2 " + BS + "quad (M=226{,}32" + BS + " " + BS + "text{g/mol})$"

eq_nyl = tex("$n@,@mathrm{HOOC@text{-}(CH_2)_4@text{-}COOH}+n@,@mathrm{H_2N@text{-}(CH_2)_6@text{-}NH_2}@rightarrow @mathrm{H@text{-}[NH@text{-}(CH_2)_6@text{-}NH@text{-}CO@text{-}(CH_2)_4@text{-}CO]_n@text{-}OH}+(2n-1)@,H_2O$")
unit_nyl = tex("$@mathrm{@left[@text{-}NH@text{-}(CH_2)_6@text{-}NH@text{-}CO@text{-}(CH_2)_4@text{-}CO@text{-}@right]_n}$")

new_nyl = old_nyl + NL + NL + "La ecuación completa de polimerización es análoga a la del PET, cambiando el diol por la diamina:" + NL + NL + eq_nyl + NL + NL + "y su unidad repetitiva, marcando el enlace amida que se repite:" + NL + NL + unit_nyl

rep(old_nyl, new_nyl, 1, "F2 nailon bracket unit")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE D")
