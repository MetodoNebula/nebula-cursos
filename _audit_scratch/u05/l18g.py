# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = '"challenge_questions": [],\n    "mcq": ['

new_block = r'''"challenge_questions": [
      {
        "id": "CH-Q05-18-1",
        "type": "CHALLENGE",
        "objective_ids": [
          "LO-Q05-18-3"
        ],
        "concept_ids": [
          "C-Q05-18-3"
        ],
        "difficulty": 5,
        "statement": "Calcula el pH a partir del cual empieza a precipitar $Mg(OH)_2$ en una disolución $0{,}010$ M de $Mg^{2+}$ ($K_{sp}=5{,}6\\times10^{-12}$).",
        "hints": [
          "La condición límite es $Q_i=K_{sp}$: el $[Mg^{2+}]$ ya está fijado ($0{,}010$ M), así que despeja el $[OH^-]$ mínimo necesario.",
          "Una vez con $[OH^-]$, calcula $\\mathrm{pOH}=-\\log[OH^-]$ y de ahí $\\mathrm{pH}=14-\\mathrm{pOH}$."
        ],
        "answer": "$[OH^-]=2{,}37\\times10^{-5}$ M; $\\mathrm{pOH}=4{,}63$; $\\mathrm{pH}=9{,}37$: precipita a partir de ese pH.",
        "full_solution": "En el límite de empezar a precipitar, $Q_i=K_{sp}$: $[Mg^{2+}][OH^-]^2=5{,}6\\times10^{-12}$. Con $[Mg^{2+}]=0{,}010$ M fijado por el enunciado: $[OH^-]^2=\\dfrac{5{,}6\\times10^{-12}}{0{,}010}=5{,}6\\times10^{-10}\\Rightarrow[OH^-]=\\sqrt{5{,}6\\times10^{-10}}=2{,}37\\times10^{-5}$ M. $\\mathrm{pOH}=-\\log(2{,}37\\times10^{-5})=4{,}63$; $\\mathrm{pH}=14-4{,}63=9{,}37$. Por debajo de $\\mathrm{pH}=9{,}37$, $[OH^-]$ es menor que ese valor, $Q_i<K_{sp}$ y el $Mg(OH)_2$ no precipita (o se redisuelve si ya estaba precipitado); a partir de $\\mathrm{pH}=9{,}37$, empieza a precipitar.",
        "common_errors": [
          "Despejar $[OH^-]$ a partir de la solubilidad en agua pura ($s=\\sqrt[3]{K_{sp}/4}$) en vez de fijar $[Mg^{2+}]=0{,}010$ M, que es el dato del enunciado."
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "mcq": ['''

n = data.count(anchor)
print("anchor count:", n)
if n == 1:
    data = data.replace(anchor, new_block, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
