PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = 'alcanzarla.",\n        "mark_scheme": [\n          "1 punto por cada apartado correctamente calificado y justificado",\n          "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"\n        ],'
new = 'alcanzarla.",\n        "mark_scheme": [\n          "1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con el efecto del catalizador sobre Ea, \\u0394H y la posici\\u00f3n de equilibrio",\n          "Sin justificar con estos conceptos, no se otorga ning\\u00fan punto aunque la calificaci\\u00f3n V/F sea correcta"\n        ],'
n = data.count(old)
print("occ:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT")
