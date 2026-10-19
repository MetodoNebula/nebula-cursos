import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import raw

PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old_hint1_anchored = raw("Primero invierte (1) y (2) y súmalas para obtener $2\\,\\text{NO}_2(g)\\rightleftharpoons\\text{N}_2(g)+2\\,\\text{O}_2(g)$ con $K_c=1/(K_{c,1}K_{c,2})$; después multiplica esa ecuación por $\\tfrac{1}{2}$ para llegar a la reacción pedida.") + '",\n          "' + raw("Aplica la regla del producto de constantes para una suma de etapas.")
print("anchored occ:", data.count(old_hint1_anchored))
new_hint1_anchored = raw("Primero invierte (1) y (2) y súmalas para obtener $2\\,\\text{NO}_2(g)\\rightleftharpoons\\text{N}_2(g)+2\\,\\text{O}_2(g)$ con $K_c=1/(K_{c,1}K_{c,2})$; después multiplica esa ecuación por $\\tfrac{1}{2}$ para llegar a la reacción pedida.") + '",\n          "' + raw("Recuerda: sumar ecuaciones multiplica las constantes; multiplicar los coeficientes de una ecuación por $n$ eleva su constante a la potencia $n$.")

n = data.count(old_hint1_anchored)
if n == 1:
    data = data.replace(old_hint1_anchored, new_hint1_anchored, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT", n)
