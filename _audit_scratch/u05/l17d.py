# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''(c) Cualquier precipitado sólido presente comenzará a redisolverse, porque la disolución ya no está saturada a esta nueva dilución.",'''
new = r'''(c) Cualquier precipitado sólido presente comenzará a redisolverse: si hay sólido suficiente, hasta que los iones recuperen las concentraciones de saturación de antes de diluir ($s$ solo depende de $T$); si el sólido se agota antes, la disolución queda insaturada sin llegar a saturarse.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
