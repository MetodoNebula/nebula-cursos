# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

anchor = r'''"common_errors": [
          "Justificar la aproximación solo con «Kc es pequeña», sin mencionar que también depende de n0 y sin describir el paso de verificación."
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "exam_questions": ['''

n = data.count(anchor)
print("anchor count:", n)

new_tail = r'''"common_errors": [
          "Justificar la aproximación solo con «Kc es pequeña», sin mencionar que también depende de n0 y sin describir el paso de verificación."
        ],
        "provenance": "SOURCE_DERIVED"
      },
      {
        "id": "EX-Q05-12-S3",
        "type": "STANDARD",
        "objective_ids": [
          "LO-Q05-12-3"
        ],
        "concept_ids": [
          "C-Q05-12-2"
        ],
        "difficulty": 3,
        "statement": "Para $\\text{PCl}_5(g)\\rightleftharpoons\\text{PCl}_3(g)+\\text{Cl}_2(g)$, en un recipiente de volumen y temperatura constantes se introduce $\\text{PCl}_5$ puro a una presión inicial $P_0=1{,}00\\,\\mathrm{atm}$. Una vez alcanzado el equilibrio, la presión total medida es $P_T=1{,}60\\,\\mathrm{atm}$. (a) Calcula el grado de disociación $\\alpha$ a partir de $P_T=P_0(1+\\alpha)$. (b) Calcula $K_p$ en función de $\\alpha$ y $P_T$. (c) Comprueba el resultado calculando las fracciones molares y las presiones parciales de cada especie.",
        "hints": [
          "Los moles totales pasan de $n_0$ a $n_0(1+\\alpha)$ a $V$ y $T$ constantes, así que la presión total aumenta en ese mismo factor: $P_T=P_0(1+\\alpha)$.",
          "Con $\\alpha$ ya calculado, sustituye directamente en $K_p=\\dfrac{\\alpha^2}{1-\\alpha^2}P_T$, sin necesidad de pasar por concentraciones."
        ],
        "answer": "(a) $\\alpha=0{,}60$. (b) $K_p=0{,}900\\,\\mathrm{atm}$. (c) $\\chi_{PCl_5}=0{,}25$, $\\chi_{PCl_3}=\\chi_{Cl_2}=0{,}375$; $P_{PCl_5}=0{,}400\\,\\mathrm{atm}$, $P_{PCl_3}=P_{Cl_2}=0{,}600\\,\\mathrm{atm}$; $K_p=\\dfrac{0{,}600^2}{0{,}400}=0{,}900\\,\\mathrm{atm}$, coincide.",
        "full_solution": "(a) $P_T=P_0(1+\\alpha)\\Rightarrow\\alpha=\\dfrac{P_T-P_0}{P_0}=\\dfrac{1{,}60-1{,}00}{1{,}00}=0{,}60$. (b) $K_p=\\dfrac{\\alpha^2}{1-\\alpha^2}P_T=\\dfrac{0{,}60^2}{1-0{,}60^2}\\times1{,}60=\\dfrac{0{,}36}{0{,}64}\\times1{,}60=0{,}900\\,\\mathrm{atm}$. (c) Fracciones molares: $\\chi_{PCl_5}=\\dfrac{1-\\alpha}{1+\\alpha}=\\dfrac{0{,}40}{1{,}60}=0{,}25$; $\\chi_{PCl_3}=\\chi_{Cl_2}=\\dfrac{\\alpha}{1+\\alpha}=\\dfrac{0{,}60}{1{,}60}=0{,}375$. Presiones parciales: $P_{PCl_5}=0{,}25\\times1{,}60=0{,}400\\,\\mathrm{atm}$; $P_{PCl_3}=P_{Cl_2}=0{,}375\\times1{,}60=0{,}600\\,\\mathrm{atm}$. Verificación: $K_p=\\dfrac{P_{PCl_3}P_{Cl_2}}{P_{PCl_5}}=\\dfrac{0{,}600\\times0{,}600}{0{,}400}=0{,}900\\,\\mathrm{atm}$, coincide con (b).",
        "common_errors": [
          "Olvidar que $P_T=P_0(1+\\alpha)$ solo es válida porque $V$ y $T$ son constantes (a $V$ y $T$ constantes, la presión es proporcional a los moles totales).",
          "Confundir $P_0$ (presión inicial de reactivo puro) con $P_T$ (presión total en el equilibrio) al sustituir en la fórmula de $\\alpha$."
        ],
        "provenance": "SOURCE_DERIVED"
      }
    ],
    "exam_questions": ['''

if n == 1:
    data = data.replace(anchor, new_tail, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
