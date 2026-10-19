PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old1 = '"id": "TH-Q05-08-5",\n        "type": "caveat",\n        "title": "Ideas equivocadas que conviene desmontar",'
new1 = '"id": "TH-Q05-08-5",\n        "type": "caveat",\n        "title": "Errores habituales sobre la ecuación de Arrhenius",'
n1 = data.count(old1)
print("occ1:", n1)

old2 = 'julios.",\n        "mark_scheme": [\n          "1 punto por cada apartado correctamente calificado y justificado",\n          "Sin justificación, 0 puntos aunque la calificación V/F sea correcta"\n        ],'
new2 = 'julios.",\n        "mark_scheme": [\n          "1 punto por cada apartado (a), (b) y (c) correctamente calificado como verdadero o falso y justificado con la ecuación de Arrhenius y la coherencia de unidades entre Ea y R",\n          "Sin justificar con la ecuaci\\u00f3n de Arrhenius, no se otorga ning\\u00fan punto aunque la calificaci\\u00f3n V/F sea correcta"\n        ],'
n2 = data.count(old2)
print("occ2:", n2)

if n1 == 1 and n2 == 1:
    data = data.replace(old1, new1, 1)
    data = data.replace(old2, new2, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT")
