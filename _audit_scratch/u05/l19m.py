# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"statement": "«Caza del error»: un compañero escribe, para $2\\,H_2O_2(l)\\rightleftharpoons 2\\,H_2O(l)+O_2(g)$, la expresión $K_c=\\dfrac{[H_2O]^2[O_2]}{[H_2O_2]^2}$. Indica el error y corrígelo.",
        "knowns": [
          "H2O2: líquido puro",
          "H2O: líquido puro",
          "O2: gas"
        ],
        "unknowns": [
          "Expresión correcta de Kc"
        ],
        "reasoning": [
          "Se identifica que tanto H2O2 como H2O están en fase líquida pura (no son solutos en disolución acuosa diluida en este contexto, son los líquidos puros de la propia reacción).",
          "Se tachan ambos líquidos puros.",
          "Solo queda el gas O2."
        ],
        "solution": "$K_c=[O_2]$",
        "interpretation": "El error del compañero fue tratar H2O2(l) y H2O(l) como si estuvieran en disolución diluida (ac), incluyéndolos en Kc, cuando en esta reacción ambos son líquidos puros (la propia descomposición del agua oxigenada) y deben tacharse igual que un sólido puro.",
        "common_mistake": "Asumir que, como el agua suele aparecer en disoluciones acuosas, siempre hay que incluirla en Kc, sin comprobar si en esta reacción concreta es un líquido puro (reactivo o producto en sí mismo) y no un disolvente de fondo.",'''

new = r'''"statement": "«Caza del error»: un compañero escribe, para $Br_2(l)\\rightleftharpoons Br_2(g)$, la expresión $K_c=\\dfrac{[Br_2(g)]}{[Br_2(l)]}$. Indica el error y corrígelo.",
        "knowns": [
          "$Br_2(l)$: líquido puro",
          "$Br_2(g)$: gas"
        ],
        "unknowns": [
          "Expresión correcta de Kc"
        ],
        "reasoning": [
          "Se identifica que $Br_2(l)$ es un líquido puro (no un soluto disuelto en otro disolvente), mientras que $Br_2(g)$ es la especie gaseosa.",
          "Se tacha el líquido puro $Br_2(l)$.",
          "Solo queda el gas $Br_2(g)$."
        ],
        "solution": "$K_c=[Br_2(g)]$ (o, en presiones parciales, $K_p=p_{Br_2}$).",
        "interpretation": "El error del compañero fue incluir $Br_2(l)$ en el denominador de $K_c$, como si su concentración pudiera variar. Al ser un líquido puro, se tacha exactamente igual que un sólido puro, y solo queda la especie gaseosa: $K_c=[Br_2(g)]$. Esto es, de hecho, la presión de vapor del bromo líquido a esa temperatura expresada como constante de equilibrio.",
        "common_mistake": "Pensar que, como hay dos fases de la misma sustancia (líquida y gaseosa), ambas deben entrar en Kc; solo entra la fase cuya concentración puede variar libremente (el gas), nunca el líquido puro.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
