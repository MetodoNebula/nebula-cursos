PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = 'de cero.",\n        "related_exercises": "el ejemplo 2 de esta lección",\n        "source_induced": tr'
new = 'de cero.",\n        "related_exercises": "el reto de esta lecci\\u00f3n (donde se calculan expl\\u00edcitamente $v_+=v_-=1{,}43\\\\times10^{-2}\\\\,\\\\mathrm{mol\\\\,L^{-1}\\\\,s^{-1}}$ en el equilibrio) y el ejemplo 2",\n        "source_induced": tr'
n = data.count(old)
print("occ:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT")
