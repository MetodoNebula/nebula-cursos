import json
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

new_obj = {
  "id": "TH-Q05-10-2B",
  "type": "theory",
  "title": "Qué indica el valor de Kc",
  "body": "El valor numérico de $K_c$ informa de hacia qué lado está desplazado el equilibrio: si $K_c\\gg1$, en el equilibrio predominan los productos (la reacción directa está muy favorecida); si $K_c\\ll1$, predominan los reactivos (apenas se forma producto); si $K_c\\approx1$, reactivos y productos están presentes en cantidades comparables. Por ejemplo, para $\\text{N}_2(g)+3\\,\\text{H}_2(g)\\rightleftharpoons2\\,\\text{NH}_3(g)$, $K_c\\approx0{,}463$ (del ejemplo 1) indica una mezcla con cantidades comparables de reactivos y producto, mientras que para $\\text{H}_2(g)+\\text{I}_2(g)\\rightleftharpoons2\\,\\text{HI}(g)$ a cierta temperatura $K_c=25{,}0$ indica un equilibrio bastante desplazado hacia el HI.\n\nEn la expresión de $K_c$ solo aparecen las especies en **disolución (ac)** y en **fase gas (g)**: los sólidos y los líquidos puros no se incluyen, porque su concentración (mol por litro de la propia sustancia pura) es constante y queda absorbida en el valor de $K_c$ (se trata con detalle en la lección de equilibrios heterogéneos). Además, $K_c$ **solo depende de la temperatura**: no cambia si se modifican las concentraciones iniciales, la presión, el volumen o si se añade un catalizador (ideas que se desarrollan en las lecciones sobre el principio de Le Châtelier).",
  "concept_ids": ["C-Q05-10-1"],
  "objective_ids": ["LO-Q05-10-1"],
  "provenance": "SOURCE_DERIVED"
}

block_text = json.dumps(new_obj, ensure_ascii=False, indent=2)
prefixed = "\n".join(("      " + line if line.strip() else line) for line in block_text.split("\n"))

old_frag = '"provenance": "SOURCE_DERIVED"\n      },\n      {\n        "id": "TH-Q05-10-3",'
new_frag = '"provenance": "SOURCE_DERIVED"\n      },\n' + prefixed + ',\n      {\n        "id": "TH-Q05-10-3",'

data = open(PATH, encoding="utf-8").read()
n = data.count(old_frag)
print("occurrences:", n)
if n == 1:
    data = data.replace(old_frag, new_frag, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("INSERTED OK")
else:
    print("ABORT")
