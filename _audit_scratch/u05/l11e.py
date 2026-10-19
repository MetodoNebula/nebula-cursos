PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()
old = '"mark_scheme": [\n          "1 punto por cada apartado correctamente calificado y justificado"\n        ],\n        "common_errors": [\n          "En (c), decir que sí coinciden las unidades'
new = '"mark_scheme": [\n          "1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con la relaci\\u00f3n $K_p=K_c(RT)^{\\\\Delta n}$ y la naturaleza f\\u00edsica de cada constante"\n        ],\n        "common_errors": [\n          "En (c), decir que sí coinciden las unidades'
n = data.count(old)
print("occ:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT")
