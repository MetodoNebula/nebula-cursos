# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = r'''"common_mistake": "Pensar que, como hay dos fases de la misma sustancia (líquida y gaseosa), ambas deben entrar en Kc; solo entra la fase cuya concentración puede variar libremente (el gas), nunca el líquido puro.",
        "objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-2"
        ],
        "concept_ids": [
          "C-Q05-19-1"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],'''

n = data.count(anchor)
print("anchor count:", n)

new_block = r'''"common_mistake": "Pensar que, como hay dos fases de la misma sustancia (líquida y gaseosa), ambas deben entrar en Kc; solo entra la fase cuya concentración puede variar libremente (el gas), nunca el líquido puro.",
        "objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-2"
        ],
        "concept_ids": [
          "C-Q05-19-1"
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "WE-Q05-19-5",
        "level": "exam",
        "statement": "En un recipiente cerrado se introduce $NH_4HS(s)$ puro a $25\\,^{\\circ}\\mathrm{C}$. Se descompone según $NH_4HS(s)\\rightleftharpoons NH_3(g)+H_2S(g)$ hasta que la presión total en el equilibrio es $P_{total}=0{,}658\\,\\mathrm{atm}$. Calcula $K_p$ y $K_c$ a esa temperatura ($R=0{,}082\\,\\mathrm{atm\\,L\\,mol^{-1}\\,K^{-1}}$).",
        "knowns": [
          "$NH_4HS(s)\\rightleftharpoons NH_3(g)+H_2S(g)$",
          "$P_{total}=0{,}658\\,\\mathrm{atm}$ en el equilibrio",
          "$T=25\\,^{\\circ}\\mathrm{C}=298\\,\\mathrm{K}$"
        ],
        "unknowns": [
          "$K_p$; $K_c$"
        ],
        "reasoning": [
          "Como todo el $NH_3$ y el $H_2S$ vienen de la descomposición del mismo sólido, en proporción 1:1, $p_{\\mathrm{NH_3}}=p_{\\mathrm{H_2S}}=P_{total}/2$.",
          "$K_p=p_{\\mathrm{NH_3}}\\,p_{\\mathrm{H_2S}}$, con $NH_4HS(s)$ tachado.",
          "$K_c=K_p/(RT)^{\\Delta n}$, con $\\Delta n=2-0=+2$."
        ],
        "solution": "$p_{\\mathrm{NH_3}}=p_{\\mathrm{H_2S}}=0{,}658/2=0{,}329$ atm. $K_p=0{,}329^2=0{,}108\\,\\mathrm{atm^2}$. $RT=0{,}082\\times298=24{,}4\\,\\mathrm{atm\\,L\\,mol^{-1}}$. $K_c=\\dfrac{0{,}108}{24{,}4^2}\\approx1{,}8\\times10^{-4}\\,\\mathrm{mol^2\\,L^{-2}}$.",
        "interpretation": "Esta presión de equilibrio ($0{,}658$ atm) es la misma a $25\\,^{\\circ}\\mathrm{C}$ sea cual sea la masa inicial de $NH_4HS(s)$, siempre que quede algo de sólido sin descomponer: la presión de equilibrio de un sólido que se descompone en dos gases en proporción 1:1 solo depende de $T$.",
        "common_mistake": "Pensar que $p_{\\mathrm{NH_3}}=p_{\\mathrm{H_2S}}=P_{total}$ en vez de dividir entre 2, olvidando que ambos gases se reparten la presión total a partes iguales.",
        "objective_ids": [
          "LO-Q05-19-1",
          "LO-Q05-19-4"
        ],
        "concept_ids": [
          "C-Q05-19-1",
          "C-Q05-19-3"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],'''

if n == 1:
    data = data.replace(anchor, new_block, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
