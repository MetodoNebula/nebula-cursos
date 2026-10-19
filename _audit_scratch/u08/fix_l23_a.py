import sys

PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"23_Condiciones')
i1 = data.find('"24_', i0)
assert i0 != -1 and i1 != -1
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

old_mcq2 = '''          {
            "key": "A",
            "text": "Con la sustitución, porque un grupo reemplaza a otro.",
            "why_wrong": "En la esterificación no hay propiamente un 'grupo saliente' que se sustituye por otro en el mismo carbono: dos moléculas se unen liberando una tercera, más pequeña."
          },
          {
            "key": "B",
            "text": "No se relaciona con ningún otro tipo: es una categoría completamente aparte.",
            "why_wrong": "La esterificación no es una categoría aislada: es, precisamente, el ejemplo característico de condensación."
          },
          {
            "key": "C",
            "text": "Con la condensación: dos moléculas se unen liberando una molécula pequeña (agua).",
            "why_wrong": null
          },
          {
            "key": "D",
            "text": "Con la eliminación, porque se elimina agua.",
            "why_wrong": "En la eliminación, la molécula pequeña sale de un único sustrato; en la esterificación son dos moléculas de partida las que se combinan."
          }
        ],
        "correct": "C",
        "explanation": "La esterificación es el ejemplo más característico de condensación: dos moléculas se unen y liberan una molécula pequeña (agua).",'''

new_mcq2 = '''          {
            "key": "A",
            "text": "Es una condensación y, mecanísticamente, también una sustitución en el carbono del grupo carboxilo (el -OH se sustituye por -OR'): las dos clasificaciones no son incompatibles.",
            "why_wrong": null
          },
          {
            "key": "B",
            "text": "Es una adición, porque se rompe un doble enlace C=C.",
            "why_wrong": "En la esterificación no hay ningún doble enlace C=C que se rompa: el ácido carboxílico y el alcohol se unen por el carbono del grupo carboxilo, liberando agua."
          },
          {
            "key": "C",
            "text": "No se relaciona con ningún otro tipo: es una categoría completamente aparte.",
            "why_wrong": "La esterificación no es una categoría aislada: es el ejemplo característico de condensación y, mecanísticamente, puede verse también como una sustitución en el acilo."
          },
          {
            "key": "D",
            "text": "Es una eliminación, porque se elimina agua.",
            "why_wrong": "En la eliminación, la molécula pequeña sale de un único sustrato; en la esterificación son dos moléculas de partida las que se combinan liberando agua."
          }
        ],
        "correct": "A",
        "explanation": "La esterificación es el ejemplo más característico de condensación (dos moléculas se unen liberando agua) y, mecanísticamente, puede describirse también como una sustitución nucleófila en el carbono acilo: ambas clasificaciones son correctas y compatibles.",'''

rep(old_mcq2, new_mcq2, 1, "F1 mcq2")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE F1")
