PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = '''desde el principio.",
        "concept_ids": [
          "C-Q05-12-1"
        ],
        "objective_ids": [
          "LO-Q05-12-1"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "keywords": ['''

new_block = ''',
      {
        "id": "TH-Q05-12-6",
        "type": "formalisation",
        "title": "Moles totales, fracciones molares y Kp en funcion de alfa y P_T",
        "body": "Para un equilibrio en fase gaseosa que parte solo de reactivo(s), conviene expresar tambien los moles totales en el equilibrio y, a partir de ellos, Kp directamente en funcion de alfa y de la presion total P_T, sin pasar por Kc.\\n\\nPara $\\\\text{A}(g)\\\\rightleftharpoons \\\\text{B}(g)+\\\\text{C}(g)$ partiendo de $n_0$ mol de A puro: $n_T=n_0(1-\\\\alpha)+n_0\\\\alpha+n_0\\\\alpha=n_0(1+\\\\alpha)$. Las fracciones molares son $\\\\chi_A=\\\\dfrac{1-\\\\alpha}{1+\\\\alpha}$, $\\\\chi_B=\\\\chi_C=\\\\dfrac{\\\\alpha}{1+\\\\alpha}$, y cada presion parcial es $P_i=\\\\chi_i P_T$ (ley de Dalton). Sustituyendo en $K_p=\\\\dfrac{P_BP_C}{P_A}$ se llega a $K_p=\\\\dfrac{\\\\alpha^2}{1-\\\\alpha^2}P_T$.\\n\\nEjemplo numerico: para $\\\\text{PCl}_5(g)\\\\rightleftharpoons \\\\text{PCl}_3(g)+\\\\text{Cl}_2(g)$, si $\\\\alpha=0{,}40$ y $P_T=2{,}0\\\\,\\\\mathrm{atm}$: $K_p=\\\\dfrac{0{,}40^2}{1-0{,}40^2}\\\\times2{,}0=\\\\dfrac{0{,}16}{0{,}84}\\\\times2{,}0=0{,}381\\\\,\\\\mathrm{atm}$.\\n\\nEsta relacion tambien permite el camino inverso: si se mide experimentalmente la presion total final $P_T$ en un recipiente de volumen y temperatura constantes que partia de una presion inicial $P_0$ de reactivo puro, entonces $P_T=P_0(1+\\\\alpha)$ (porque los moles totales pasan de $n_0$ a $n_0(1+\\\\alpha)$ a V y T constantes), de donde $\\\\alpha=\\\\dfrac{P_T-P_0}{P_0}$, sin necesidad de conocer las concentraciones en moles/L.",
        "concept_ids": [
          "C-Q05-12-2"
        ],
        "objective_ids": [
          "LO-Q05-12-3"
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "keywords": ['''

n = data.count(anchor)
print("anchor count:", n)
if n == 1:
    data = data.replace(anchor, new_block, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
