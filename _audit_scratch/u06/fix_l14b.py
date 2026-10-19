import json

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U06_Acido_Base.json"
with open(path, encoding="utf-8") as f:
    raw = f.read()
data = json.loads(raw)
key = "14_Indicadores_curvas_de_valoración_y_elección_del_punto.json"
l = data[key]

generic_why = "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema."

cm0_mistake = l["common_mistakes"][0]["mistake"]
cm1_mistake = l["common_mistakes"][1]["mistake"]
assert l["common_mistakes"][0]["why"] == generic_why
assert l["common_mistakes"][1]["why"] == generic_why

old0 = json.dumps(cm0_mistake, ensure_ascii=False) + '",\n        "why": ' + json.dumps(generic_why, ensure_ascii=False)
new0 = json.dumps(cm0_mistake, ensure_ascii=False) + '",\n        "why": ' + json.dumps("Con un buen indicador (y, sobre todo, en la valoración fuerte-fuerte de los primeros ejemplos) ambos volúmenes coinciden casi exactamente, y se acaba generalizando que son lo mismo.", ensure_ascii=False)

old1 = json.dumps(cm1_mistake, ensure_ascii=False) + '",\n        "why": ' + json.dumps(generic_why, ensure_ascii=False)
new1 = json.dumps(cm1_mistake, ensure_ascii=False) + '",\n        "why": ' + json.dumps("La primera valoración que se estudia es fuerte-fuerte, con pH de equivalencia 7,00, y esa igualdad se generaliza sin comprobar si el ácido o la base de partida son débiles.", ensure_ascii=False)

for label, old, new in [("cm0", old0, new0), ("cm1", old1, new1)]:
    n = raw.count(old)
    print(label, "occurrences:", n)
    if n == 1:
        raw = raw.replace(old, new, 1)
    else:
        print("  TRY alt indent search")
        # try without assuming exact indent: search mistake json then up to "why" value generically
        mistake_j = json.dumps(old.split('",\n')[0].strip('"') if False else None)
with open(path, "w", encoding="utf-8") as f:
    f.write(raw)
print("DONE")
