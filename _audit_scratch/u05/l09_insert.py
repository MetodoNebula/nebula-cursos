import json
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"

new_obj = {
  "id": "TH-Q05-09-1B",
  "type": "theory",
  "title": "Características generales del equilibrio químico",
  "body": "Un equilibrio químico como $\\text{A}\\rightleftharpoons\\text{B}$ cumple siempre estas características: (1) se establece en un **sistema cerrado** (no entra ni sale materia) y a **temperatura constante**; (2) se alcanza el mismo estado de equilibrio final tanto si se parte solo de A, solo de B, o de una mezcla de ambos, siempre que la cantidad total de sustancia y las condiciones (T, V) sean las mismas —por ejemplo, si se parte solo de B, al principio $v_+=0$ (no hay A) y $v_-$ es máxima, y el sistema evoluciona hasta que de nuevo $v_+=v_-$—; (3) las propiedades macroscópicas (concentraciones, color, presión…) permanecen constantes una vez alcanzado, aunque las concentraciones de equilibrio de A y B no tienen por qué ser iguales entre sí. Gráficamente, si se representan $[\\text{A}]$ y $[\\text{B}]$ frente al tiempo, ambas curvas se vuelven horizontales a partir del instante de equilibrio $t_{\\text{eq}}$; si se representan $v_+$ y $v_-$ frente al tiempo, $v_+$ parte de un valor alto y decrece, $v_-$ parte de 0 y crece, y ambas curvas se cruzan exactamente en $t_{\\text{eq}}$, continuando después superpuestas en un valor común distinto de cero.",
  "concept_ids": ["C-Q05-09-1"],
  "objective_ids": ["LO-Q05-09-1"],
  "provenance": "SOURCE_DERIVED"
}

block_text = json.dumps(new_obj, ensure_ascii=False, indent=2)
prefixed = "\n".join(("      " + line if line.strip() else line) for line in block_text.split("\n"))

old_frag = '"provenance": "SOURCE_DERIVED"\n      },\n      {\n        "id": "TH-Q05-09-2",'
new_frag = '"provenance": "SOURCE_DERIVED"\n      },\n' + prefixed + ',\n      {\n        "id": "TH-Q05-09-2",'

data = open(PATH, encoding="utf-8").read()
n = data.count(old_frag)
print("occurrences:", n)
if n == 1:
    data = data.replace(old_frag, new_frag, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("INSERTED OK")
else:
    print("ABORT")
