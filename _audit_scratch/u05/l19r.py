# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = r'''"objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-2"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "keywords": ['''

n = data.count(anchor)
print("anchor count:", n)

new_block = r'''"objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-2"
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "TH-Q05-19-7",
        "type": "connection",
        "title": "Consecuencias de K=[CO2]: el caso tipico de PAU",
        "body": "Para $CaCO_3(s)\\rightleftharpoons CaO(s)+CO_2(g)$, el hecho de que $K_c=[CO_2]$ (o $K_p=p_{\\mathrm{CO_2}}$) dependa de una sola especie tiene consecuencias importantes que se preguntan a menudo en PAU:\n\n- A una $T$ dada, la concentración (o presión) de $CO_2$ en el equilibrio es un valor FIJO, que no depende de cuánto $CaCO_3$ o $CaO$ sólido haya presente, siempre que quede algo de los dos sólidos.\n- Por lo mismo, añadir o retirar sólido ($CaCO_3$ o $CaO$) no desplaza el equilibrio: no cambia ni $[CO_2]$ ni $Q$, porque los sólidos no aparecen en $Q$.\n- Si se comprime el recipiente, $[CO_2]$ sube momentáneamente por encima del valor de $K_c$ ($Q>K_c$): el $CO_2$ reacciona con el $CaO$ formando más $CaCO_3(s)$ hasta que $[CO_2]$ vuelve a valer exactamente $K_c$ a esa $T$ (nunca se queda «a medio camino» mientras quede sólido suficiente en ambos lados).\n\nEste mismo razonamiento se aplica a cualquier descomposición de un sólido en dos gases, como $NH_4HS(s)\\rightleftharpoons NH_3(g)+H_2S(g)$: a una $T$ dada, con suficiente sólido presente, la presión total en el equilibrio es siempre la misma, sea cual sea la masa de $NH_4HS$ inicial.",
        "concept_ids": [
          "C-Q05-19-1",
          "C-Q05-19-3"
        ],
        "objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-4"
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
