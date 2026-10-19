# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''la disolución pasa a estar insaturada, y cualquier precipitado presente comenzará a redisolverse hasta alcanzar un nuevo equilibrio saturado a esa dilución.\n\nEsta es la misma lógica,'''

new = r'''la disolución pasa a estar insaturada, y cualquier precipitado presente comenzará a redisolverse: si hay sólido suficiente, se redisuelve hasta que los iones recuperan exactamente las mismas concentraciones de saturación que antes de diluir (la solubilidad $s$ solo depende de $T$, no del volumen); si el sólido se agota antes de llegar ahí, la disolución queda insaturada, sin alcanzar la saturación.\n\nEsta es la misma lógica,'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
