import json

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U06_Acido_Base.json"
with open(path, encoding="utf-8") as f:
    raw = f.read()
data = json.loads(raw)
key = "14_Indicadores_curvas_de_valoración_y_elección_del_punto.json"
l = data[key]

generic_why = "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema."
new_why0 = "Con un buen indicador (y, sobre todo, en la valoración fuerte-fuerte de los primeros ejemplos) ambos volúmenes coinciden casi exactamente, y se acaba generalizando que son lo mismo."
new_why1 = "La primera valoración que se estudia es fuerte-fuerte, con pH de equivalencia 7,00, y esa igualdad se generaliza sin comprobar si el ácido o la base de partida son débiles."

cm0_mistake = l["common_mistakes"][0]["mistake"]
cm1_mistake = l["common_mistakes"][1]["mistake"]

def build(mistake_text, why_text):
    m = json.dumps(mistake_text, ensure_ascii=False)  # '"....."'
    w = json.dumps(why_text, ensure_ascii=False)
    return m[:-1] + '",\n        "why": ' + w

old0 = build(cm0_mistake, generic_why)
new0 = build(cm0_mistake, new_why0)
old1 = build(cm1_mistake, generic_why)
new1 = build(cm1_mistake, new_why1)

for label, old, new in [("cm0", old0, new0), ("cm1", old1, new1)]:
    n = raw.count(old)
    print(label, "occurrences:", n)
    if n == 1:
        raw = raw.replace(old, new, 1)
    else:
        print("ABORT", label)

with open(path, "w", encoding="utf-8") as f:
    f.write(raw)
print("DONE")
