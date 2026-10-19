import json
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

new_obj = {
  "id": "TH-Q05-11-3B",
  "type": "worked_rule",
  "title": "Ley de Dalton: Kp a partir de presiones parciales",
  "body": "En una mezcla de gases, la presión parcial de cada uno es $P_i=\\chi_i\\,P_{total}$, donde $\\chi_i=n_i/n_{total}$ es su fracción molar; además $P_{total}=\\sum_i P_i$ (ley de Dalton). Esto permite calcular $K_p$ directamente a partir de los moles de equilibrio y la presión total, sin pasar por $K_c$, que es el tipo de problema más frecuente en los exámenes de Selectividad.\n\n**Ejemplo:** para $\\text{N}_2\\text{O}_4(g)\\rightleftharpoons2\\,\\text{NO}_2(g)$, en el equilibrio hay 0,40 mol de $\\text{N}_2\\text{O}_4$ y 0,20 mol de $\\text{NO}_2$, con una presión total $P_{total}=1{,}5$ atm. Los moles totales son $n_{total}=0{,}40+0{,}20=0{,}60$ mol, así que $\\chi_{\\text{N}_2\\text{O}_4}=0{,}40/0{,}60=0{,}667$ y $\\chi_{\\text{NO}_2}=0{,}20/0{,}60=0{,}333$. Las presiones parciales son $P_{\\text{N}_2\\text{O}_4}=0{,}667\\times1{,}5=1{,}0$ atm y $P_{\\text{NO}_2}=0{,}333\\times1{,}5=0{,}50$ atm, con las que:\n\n$$K_p=\\frac{P_{\\text{NO}_2}^{\\,2}}{P_{\\text{N}_2\\text{O}_4}}=\\frac{(0{,}50)^2}{1{,}0}=0{,}25\\ \\mathrm{atm}$$",
  "concept_ids": ["C-Q05-11-2"],
  "objective_ids": ["LO-Q05-11-2"],
  "provenance": "SOURCE_DERIVED"
}

block_text = json.dumps(new_obj, ensure_ascii=False, indent=2)
prefixed = "\n".join(("      " + line if line.strip() else line) for line in block_text.split("\n"))

old_frag = '"provenance": "SOURCE_DERIVED"\n      },\n      {\n        "id": "TH-Q05-11-4",'
new_frag = '"provenance": "SOURCE_DERIVED"\n      },\n' + prefixed + ',\n      {\n        "id": "TH-Q05-11-4",'

data = open(PATH, encoding="utf-8").read()
n = data.count(old_frag)
print("occurrences:", n)
if n == 1:
    data = data.replace(old_frag, new_frag, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("INSERTED OK")
else:
    print("ABORT")
