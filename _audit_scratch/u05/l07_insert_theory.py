import json, sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

new_obj = {
  "id": "TH-Q05-07-1B",
  "type": "theory",
  "title": "Tipos de catálisis y aplicaciones",
  "body": "Según en qué fase se encuentre el catalizador respecto a los reactivos, se distinguen tres tipos de catálisis: **homogénea** (el catalizador está en la misma fase que los reactivos, normalmente disuelto en la misma disolución; por ejemplo, el ion $\\text{I}^-$ en la descomposición catalizada de $\\text{H}_2\\text{O}_2$); **heterogénea** (el catalizador está en una fase distinta, típicamente un sólido sobre cuya superficie se adsorben los reactivos gaseosos o disueltos; por ejemplo, el hierro en la síntesis industrial de amoniaco, proceso Haber-Bosch, o el platino, paladio y rodio del catalizador de los automóviles, que transforman CO, $\\text{NO}_x$ e hidrocarburos no quemados en $\\text{CO}_2$, $\\text{N}_2$ y $\\text{H}_2\\text{O}$); y **enzimática** (el catalizador es una enzima, una proteína con una forma muy específica —modelo «llave-cerradura»— que acelera reacciones biológicas con una eficacia enorme, y cuya actividad es muy sensible a la temperatura y al pH). En los tres casos el mecanismo es el mismo que se ha descrito: ofrecer un camino alternativo de menor energía de activación.",
  "concept_ids": ["C-Q05-07-1"],
  "objective_ids": ["LO-Q05-07-1"],
  "provenance": "SOURCE_DERIVED"
}

block_text = json.dumps(new_obj, ensure_ascii=False, indent=2)
prefixed = "\n".join(("      " + line if line.strip() else line) for line in block_text.split("\n"))

old_frag = '"provenance": "SOURCE_DERIVED"\n      },\n      {\n        "id": "TH-Q05-07-2",'
new_frag = '"provenance": "SOURCE_DERIVED"\n      },\n' + prefixed + ',\n      {\n        "id": "TH-Q05-07-2",'

data = open(PATH, encoding="utf-8").read()
n = data.count(old_frag)
print("occurrences:", n)
if n == 1:
    data = data.replace(old_frag, new_frag, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("INSERTED OK")
else:
    print("ABORT")
