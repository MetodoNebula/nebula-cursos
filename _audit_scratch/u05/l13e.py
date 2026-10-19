# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = r'''"common_mistake": "Al ver que $Q$ no es exactamente igual a $K_c$ hasta la última cifra, concluir que «no está en equilibrio»: hay que tener en cuenta el redondeo de las cifras significativas de partida.",
        "objective_ids": [
          "LO-Q05-13-2",
          "LO-Q05-13-4"
        ],
        "concept_ids": [
          "C-Q05-13-1",
          "C-Q05-13-2"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "guided_exercises": ['''

n = data.count(anchor)
print("anchor count:", n)

new_block = r'''"common_mistake": "Al ver que $Q$ no es exactamente igual a $K_c$ hasta la última cifra, concluir que «no está en equilibrio»: hay que tener en cuenta el redondeo de las cifras significativas de partida.",
        "objective_ids": [
          "LO-Q05-13-2",
          "LO-Q05-13-4"
        ],
        "concept_ids": [
          "C-Q05-13-1",
          "C-Q05-13-2"
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "WE-Q05-13-5",
        "level": "exam",
        "statement": "Para $H_2(g)+I_2(g)\\rightleftharpoons2\\,HI(g)$ ($K_c=54{,}3$), se mezclan $[H_2]_0=[I_2]_0=0{,}0500$ M y $[HI]_0=1{,}00$ M. (a) Calcula $Q$ y el sentido de evolución. (b) Plantea la tabla ICE en el sentido correcto y calcula las concentraciones de equilibrio.",
        "knowns": [
          "$[H_2]_0=[I_2]_0=0{,}0500$ M",
          "$[HI]_0=1{,}00$ M",
          "$K_c=54{,}3$"
        ],
        "unknowns": [
          "$[H_2]_{eq}$",
          "$[I_2]_{eq}$",
          "$[HI]_{eq}$"
        ],
        "reasoning": [
          "Se calcula $Q$ con las concentraciones iniciales: $Q=\\dfrac{1{,}00^2}{0{,}0500\\cdot0{,}0500}=400$.",
          "Como $Q=400>K_c=54{,}3$, hay demasiado producto: el sistema avanza hacia reactivos, al contrario que en los ejemplos anteriores.",
          "Se define $y>0$ como el avance neto hacia reactivos: $H_2$ e $I_2$ aumentan en $y$, $HI$ disminuye en $2y$. Tabla ICE: $[H_2]=[I_2]=0{,}0500+y$; $[HI]=1{,}00-2y$."
        ],
        "solution": "$54{,}3=\\dfrac{(1{,}00-2y)^2}{(0{,}0500+y)^2}\\Rightarrow\\sqrt{54{,}3}=7{,}37=\\dfrac{1{,}00-2y}{0{,}0500+y}\\Rightarrow1{,}00-2y=7{,}37(0{,}0500+y)=0{,}3685+7{,}37y\\Rightarrow y=\\dfrac{0{,}6315}{9{,}37}=0{,}0674$. $[H_2]_{eq}=[I_2]_{eq}=0{,}0500+0{,}0674=0{,}117$ M; $[HI]_{eq}=1{,}00-2\\cdot0{,}0674=0{,}865$ M",
        "interpretation": "Comprobación: $K_c=\\dfrac{0{,}865^2}{0{,}117^2}\\approx54{,}3$, correcto. Al ir el sistema hacia reactivos, $[HI]$ disminuye y $[H_2]$, $[I_2]$ aumentan, al revés que cuando se parte solo de reactivos.",
        "common_mistake": "Definir el avance con el mismo signo que en los ejemplos anteriores (restando en reactivos, sumando en producto) sin comprobar primero, comparando $Q$ con $K_c$, hacia qué lado evoluciona realmente el sistema.",
        "objective_ids": [
          "LO-Q05-13-2",
          "LO-Q05-13-3"
        ],
        "concept_ids": [
          "C-Q05-13-2"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "guided_exercises": ['''

if n == 1:
    data = data.replace(anchor, new_block, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
