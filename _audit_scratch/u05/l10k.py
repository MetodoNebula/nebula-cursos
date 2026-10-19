PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()
old = '"id": "TH-Q05-10-5",\n        "type": "caveat",\n        "title": "Ideas equivocadas que conviene desmontar",'
new = '"id": "TH-Q05-10-5",\n        "type": "caveat",\n        "title": "Errores habituales sobre la constante Kc",'
n = data.count(old)
print("occ:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("OK")
else:
    print("ABORT")
