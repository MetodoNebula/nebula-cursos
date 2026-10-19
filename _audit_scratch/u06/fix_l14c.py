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

def anchor(mistake_text, why_text):
    m = json.dumps(mistake_text, ensure_ascii=False)  # includes quotes
    w = json.dumps(why_text, ensure_ascii=False)
    return m[:-1] + ',\n        "why": ' + w  # drop closing quote of m, it's re-added inside w's own quoting... wait

old0 = anchor(cm0_mistake, generic_why)
print(repr(old0[:150]))
print("occ0:", raw.count(old0))
