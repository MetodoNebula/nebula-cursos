PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

# H7a: theory_blocks[4].body
edits.append(("H7_theory4_body",
'''Un detalle importante, y poco intuitivo a primera vista: la composición final de un equilibrio **no depende de cómo se llegue a él**. Si se parte de una situación inicial, se altera hasta un primer equilibrio, y luego se altera de nuevo hasta un segundo equilibrio, el resultado final es el mismo que si se aplicaran ambas alteraciones juntas desde el principio, sin pasar por el equilibrio intermedio.\\n\\nEsto da libertad a la hora de plantear una tabla ICE con varias perturbaciones sucesivas: se puede calcular todo de una vez, sin necesidad de resolver un equilibrio intermedio paso a paso, siempre que el estado final sea el mismo.''',
'''Un detalle importante, y poco intuitivo a primera vista: el estado de equilibrio final solo depende de la temperatura, del volumen (o presión) finales y de las cantidades totales de cada sustancia introducidas en el sistema, nunca del orden o del camino por el que se llega a él.\\n\\nPor eso, si a un equilibrio ya establecido se le añade más reactivo y se deja alcanzar un nuevo equilibrio, el resultado es idéntico al que se obtendría planteando una única tabla ICE con todo lo añadido (lo inicial más lo añadido después) como fila «Inicial», sin resolver primero el equilibrio intermedio. Ejemplo: se parte de $0{,}0300$ mol de $\\\\text{N}_2\\\\text{O}_4$ en $1{,}00$ L; tras alcanzar el equilibrio, se añaden $0{,}0200$ mol más de $\\\\text{N}_2\\\\text{O}_4$ al mismo recipiente y se deja re-equilibrar. El resultado final es exactamente el mismo que si se hubiera planteado una sola tabla ICE partiendo de $0{,}0300+0{,}0200=0{,}0500$ mol de $\\\\text{N}_2\\\\text{O}_4$ desde el principio.'''
))

# H7b: FC-Q05-12-10 back
edits.append(("H7_FC10_back",
"No: la composición final de un equilibrio no depende de cómo se llegue (directamente o pasando por un equilibrio intermedio), siempre que las condiciones finales sean las mismas.",
"No: el equilibrio final solo depende de T, V (o P) y de las cantidades totales introducidas, no del camino. Por ejemplo, añadir reactivo en dos tandas sucesivas (dejando re-equilibrar entre medias) da el mismo resultado final que añadir de una vez la suma de ambas cantidades."
))

# H9: worked_examples[2].solution despeje
edits.append(("H9_WE2_despeje",
"De $7{,}07=\\\\dfrac{2x}{0{,}100-x}$ se despeja $x=0{,}0780$ M.",
"De $7{,}07=\\\\dfrac{2x}{0{,}100-x}\\\\Rightarrow7{,}07(0{,}100-x)=2x\\\\Rightarrow0{,}707=9{,}07\\\\,x\\\\Rightarrow x=0{,}0780$ M (valor comprobado: $0{,}07795$)."
))

results = []
ok_all = True
for label, old, new in edits:
    n = data.count(old)
    results.append((label, n))
    if n == 1:
        data = data.replace(old, new, 1)
    else:
        ok_all = False

for lb, cnt in results:
    print(lb, cnt)

if ok_all:
    open(PATH, "w", encoding="utf-8").write(data)
    print("ALL WRITTEN")
else:
    print("ABORT")
