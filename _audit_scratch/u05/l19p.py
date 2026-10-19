# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = r'''También puede escribirse directamente en presiones parciales: $K_p=p_{\\mathrm{CO_2}}$.",
        "concept_ids": [
          "C-Q05-19-3"
        ],
        "objective_ids": [
          "LO-Q05-19-4"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "keywords": ['''

n = data.count(anchor)
print("anchor count:", n)

new_block = r'''También puede escribirse directamente en presiones parciales: $K_p=p_{\\mathrm{CO_2}}$.",
        "concept_ids": [
          "C-Q05-19-3"
        ],
        "objective_ids": [
          "LO-Q05-19-4"
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "TH-Q05-19-6",
        "type": "caveat",
        "title": "El agua líquida: disolvente, líquido puro, o reactivo en fase líquida homogénea",
        "body": "Hay que distinguir tres papeles posibles del agua líquida:\n\n1. Como disolvente de una disolución acuosa diluida, el agua NO aparece en K (su concentración, igual que la de un líquido puro, se considera constante y queda englobada en K).\n2. Como líquido puro reactivo o producto de la propia reacción (por ejemplo en una descomposición), tampoco aparece en K: se tacha igual que cualquier líquido puro.\n3. Como vapor de agua, $H_2O(g)$, SÍ aparece en K, como cualquier otra especie gaseosa.\n\nLa única excepción a (1) y (2) es una reacción en fase líquida homogénea en la que ninguna especie actúa como disolvente mayoritario: todas las sustancias, incluida el agua, forman una única mezcla líquida y todas entran en $K_c$. El ejemplo clásico es la esterificación: $CH_3COOH(l)+C_2H_5OH(l)\\rightleftharpoons CH_3COOC_2H_5(l)+H_2O(l)$, donde $K_c=\\dfrac{[CH_3COOC_2H_5][H_2O]}{[CH_3COOH][C_2H_5OH]}$, con las cuatro especies presentes, porque ninguna de ellas es un disolvente en gran exceso frente a las demás.",
        "concept_ids": [
          "C-Q05-19-1"
        ],
        "objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-2"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "keywords": ['''

if n == 1:
    data = data.replace(anchor, new_block, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
