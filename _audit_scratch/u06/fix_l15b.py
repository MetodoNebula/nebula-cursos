import json

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U06_Acido_Base.json"
with open(path, encoding="utf-8") as f:
    raw = f.read()
data = json.loads(raw)
key = "15_Ácidos_y_bases_en_productos_industria_y_medioambiente.json"
l = data[key]

generic_why = "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema."
cm0_mistake = l["common_mistakes"][0]["mistake"]
assert l["common_mistakes"][0]["why"] == generic_why

def build(mistake_text, why_text):
    m = json.dumps(mistake_text, ensure_ascii=False)
    w = json.dumps(why_text, ensure_ascii=False)
    return m[:-1] + '",\n        "why": ' + w

old0 = build(cm0_mistake, generic_why)
new0 = build(cm0_mistake, "Se trata la escala de pH como lineal, igual que temperaturas o precios, olvidando que pH = −log[H+].")
n = raw.count(old0)
print("cm0 occurrences:", n)
if n == 1:
    raw = raw.replace(old0, new0, 1)
else:
    print("ABORT cm0")

with open(path, "w", encoding="utf-8") as f:
    f.write(raw)
print("DONE")
