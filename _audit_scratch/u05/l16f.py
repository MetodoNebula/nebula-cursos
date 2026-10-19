# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"related_exercises": "el ejemplo 2 de esta lección",
        "source_induced": true
      },
      {
        "id": "MIS-Q05-16-2",'''
new = r'''"related_exercises": "los ejemplos 1 y 3 de esta lección y la primera pregunta del test",
        "source_induced": true
      },
      {
        "id": "MIS-Q05-16-2",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
