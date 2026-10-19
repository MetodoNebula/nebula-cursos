PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = '''desde el principio.",
      {
        "id": "TH-Q05-12-6",'''

new = '''desde el principio.",
        "concept_ids": [
          "C-Q05-12-1"
        ],
        "objective_ids": [
          "LO-Q05-12-1"
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "TH-Q05-12-6",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
