import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"23_Condiciones')
i1 = data.find('"24_', i0)
seg = data[i0:i1]

BS = chr(92) * 2  # two literal backslash chars = one escaped backslash in JSON

old = "R" + BS + "text{-COOH}+HO" + BS + "text{-}R'" + chr(32) + BS + "rightarrow R" + BS + "text{-COO-}R'+H_2O"
new = "R" + BS + "text{-COOH}+HO" + BS + "text{-}R'" + chr(32) + BS + "overset{H^+}{" + BS + "rightleftharpoons} R" + BS + "text{-COO-}R'+H_2O"

c = seg.count(old)
print("count", c)
if c != 1:
    idx = seg.find("R" + BS + "text{-COOH}")
    print(repr(seg[max(0,idx-10):idx+120]))
    sys.exit(1)
seg = seg.replace(old, new)
print("OK F5")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE F5")
