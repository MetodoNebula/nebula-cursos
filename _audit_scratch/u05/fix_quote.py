PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = '\\text{O}_4$ ,\n      {\n        "id": "TH-Q05-12-6"'
n = data.count(old)
print("count:", n)
if n == 1:
    new = '\\text{O}_4$ desde el principio.",\n      {\n        "id": "TH-Q05-12-6"'
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
