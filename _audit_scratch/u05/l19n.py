# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"stem": "Para $2\\,H_2O_2(l)\\rightleftharpoons 2\\,H_2O(l)+O_2(g)$, la expresión correcta de Kc es:",
        "options": [
          {
            "key": "A",
            "text": "$K_c=\\dfrac{[H_2O]^2[O_2]}{[H_2O_2]^2}$",
            "misconception_id": "MIS-Q05-19-1",
            "why_wrong": "Trata H2O2 y H2O como si estuvieran en disolución diluida, cuando aquí son líquidos puros y deben tacharse."
          },
          {
            "key": "B",
            "text": "$K_c=[H_2O]^2[O_2]$",
            "misconception_id": "MIS-Q05-19-1",
            "why_wrong": "Incluye H2O, que aquí es líquido puro (no un disolvente de fondo en disolución diluida) y debe tacharse igual que H2O2."
          },
          {
            "key": "C",
            "text": "$K_c=\\dfrac{[O_2]}{[H_2O_2]^2}$",
            "misconception_id": "MIS-Q05-19-1",
            "why_wrong": "H2O2 es líquido puro en esta reacción y no debe aparecer en el denominador."
          },
          {
            "key": "D",
            "text": "$K_c=[O_2]$",
            "misconception_id": null,
            "why_wrong": null
          }
        ],
        "correct": "D",
        "explanation": "H2O2(l) y H2O(l) son líquidos puros en esta reacción (no disolventes de fondo) y se tachan; solo queda el gas O2.",'''

new = r'''"stem": "Para $Br_2(l)\\rightleftharpoons Br_2(g)$, la expresión correcta de Kc es:",
        "options": [
          {
            "key": "A",
            "text": "$K_c=\\dfrac{[Br_2(g)]}{[Br_2(l)]}$",
            "misconception_id": "MIS-Q05-19-1",
            "why_wrong": "Trata $Br_2(l)$ como si estuviera en disolución diluida, cuando aquí es un líquido puro y debe tacharse."
          },
          {
            "key": "B",
            "text": "$K_c=[Br_2(l)]$",
            "misconception_id": "MIS-Q05-19-1",
            "why_wrong": "Incluye el líquido puro $Br_2(l)$, que debe tacharse, y omite el gas $Br_2(g)$, que es la única especie que debe aparecer en $K_c$."
          },
          {
            "key": "C",
            "text": "$K_c=[Br_2(g)]^2$",
            "misconception_id": null,
            "why_wrong": "El coeficiente estequiométrico de $Br_2(g)$ en esta ecuación ajustada es 1, no 2."
          },
          {
            "key": "D",
            "text": "$K_c=[Br_2(g)]$",
            "misconception_id": null,
            "why_wrong": null
          }
        ],
        "correct": "D",
        "explanation": "$Br_2(l)$ es un líquido puro en esta reacción y se tacha; solo queda el gas $Br_2(g)$, con coeficiente 1.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
