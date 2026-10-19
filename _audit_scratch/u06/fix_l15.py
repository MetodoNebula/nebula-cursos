import json

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U06_Acido_Base.json"
with open(path, encoding="utf-8") as f:
    raw = f.read()
data = json.loads(raw)
key = "15_Ácidos_y_bases_en_productos_industria_y_medioambiente.json"
l = data[key]

fixes = []

# H1
fixes.append((l["mcq"][0]["options"][0]["why_wrong"],
"Divide un pH entre el otro (6/3 = 2) en vez de deshacer el logaritmo; el pH no es una magnitud proporcional que se pueda dividir así."
))

# H3 theory1
new_theory1 = ("Muchos productos de limpieza indican en su etiqueta la concentración del componente activo (por ejemplo, 'disolución de hidróxido de sodio al X %' o, de forma más directa, una concentración molar). Cuando el dato es un porcentaje en masa y una densidad, la concentración molar se obtiene con $c=\\dfrac{\\%\\cdot\\rho\\cdot10}{M}$ (con $\\rho$ en g/mL y $M$ en g/mol): por ejemplo, un salfumán de HCl al 35 % con $\\rho=1{,}18$ g/mL tiene $c=\\dfrac{35\\cdot1{,}18\\cdot10}{36{,}46}=11{,}3$ M.\n\n"
"A partir de la concentración, el procedimiento es el mismo que para cualquier ácido o base **fuerte**:\n\n"
"$$[\\mathrm{OH^-}]=C,\\qquad \\mathrm{pOH}=-\\log[\\mathrm{OH^-}],\\qquad \\mathrm{pH}=14{,}00-\\mathrm{pOH}.$$\n\n"
"No todos los productos domésticos son fuertes: el vinagre (ácido acético, $K_a=1{,}8\\times10^{-5}$) y el amoniaco doméstico (base débil, $K_b=1{,}8\\times10^{-5}$) son ácidos/bases débiles, y su pH se calcula con las herramientas de las lecciones de ácidos y bases débiles, no con $[\\mathrm{H^+}]=C$ directamente: un vinagre 0,83 M de CH$_3$COOH tiene $\\alpha\\approx\\sqrt{K_a/c_0}$ y $\\mathrm{pH}\\approx2{,}41$, muy distinto de lo que daría tratarlo como fuerte.\n\n"
"Lo mismo ocurre al revés, para un producto fuerte: a partir del pH indicado o medido, se puede obtener la concentración de ácido o de base que contiene, deshaciendo el logaritmo.")
fixes.append((l["theory_blocks"][1]["body"], new_theory1))

# H2 theory4
new_theory4 = ("El agua de lluvia disuelve CO$_2$ atmosférico y forma ácido carbónico, lo que le da de forma **natural** un pH ligeramente ácido, en torno a 5,6: $\\mathrm{CO_2}(g)+\\mathrm{H_2O}(l)\\rightleftharpoons \\mathrm{H_2CO_3}(aq)$. Cuando la combustión de carbón o de derivados del petróleo libera óxidos de azufre y de nitrógeno, estos se disuelven también en el agua de las nubes y forman ácidos más fuertes:\n\n"
"$$\\mathrm{SO_2}(g)+\\mathrm{H_2O}(l)\\rightarrow \\mathrm{H_2SO_3}(aq)\\qquad 2\\,\\mathrm{SO_2}(g)+\\mathrm{O_2}(g)\\rightarrow 2\\,\\mathrm{SO_3}(g)\\qquad \\mathrm{SO_3}(g)+\\mathrm{H_2O}(l)\\rightarrow \\mathrm{H_2SO_4}(aq)$$\n"
"$$3\\,\\mathrm{NO_2}(g)+\\mathrm{H_2O}(l)\\rightarrow 2\\,\\mathrm{HNO_3}(aq)+\\mathrm{NO}(g)$$\n\n"
"que bajan el pH de la lluvia considerablemente por debajo de ese valor natural.\n\n"
"Las consecuencias (acidificación de lagos y suelos, corrosión de construcciones de mármol y caliza, que es carbonato de calcio y reacciona con el exceso de ácido: $\\mathrm{CaCO_3}(s)+2\\,\\mathrm{H^+}(aq)\\rightarrow \\mathrm{Ca^{2+}}(aq)+\\mathrm{CO_2}(g)+\\mathrm{H_2O}(l)$) son, en el fondo, el mismo tipo de razonamiento ácido-base ya estudiado: una disolución más ácida reacciona con una base (el carbonato) de forma más intensa.")
fixes.append((l["theory_blocks"][4]["body"], new_theory4))

# H5
fixes.append((l["keywords"][3]["definition"],
"Base débil o poco soluble (Mg(OH)$_2$, Al(OH)$_3$, CaCO$_3$, NaHCO$_3$) que neutraliza el exceso de HCl del estómago."
))

# H6
fixes.append((l["exercises"][1]["statement"],
l["exercises"][1]["statement"].replace("Un lago recibe un vertido", "Un estanque recibe un vertido")
))

# H7
fixes.append((l["challenge_questions"][0]["statement"],
"Un depósito contiene 300 L de un residuo con pH 2,00 (supuesto ácido fuerte monoprótico). Se dispone de disoluciones de NaOH 2,0 M para neutralizarlo. **(a)** Calcula el volumen de NaOH 2,0 M necesario. **(b)** Si solo se añaden dos tercios del volumen calculado en (a), calcula el pH resultante y comenta si está más próximo a 2 o a 7."
))

# H8
fixes.append((l["exam_questions"][1]["full_solution"],
"La reacción ajustada es $2\\,\\mathrm{H_3PO_4}(aq)+3\\,\\mathrm{Ca(OH)_2}(s)\\rightarrow \\mathrm{Ca_3(PO_4)_2}(s)+6\\,\\mathrm{H_2O}(l)$ (neutralización completa de los tres protones). $V=2{,}0$ m$^3$ $=2000$ L (el volumen total que se vierte cada día). $n(\\mathrm{H_{3}PO_{4}})=0{,}0040\\cdot2000=8{,}0$ mol. Como el H$_3$PO$_4$ es triprótico, aporta $3\\cdot8{,}0=24$ mol de H$^+$. Cada mol de Ca(OH)$_2$ aporta 2 moles de OH$^-$, así que $n(\\mathrm{Ca(OH)_{2}})=24/2=12$ mol. Masa $=12\\cdot74{,}09=889$ g $\\approx0{,}89$ kg/día."
))

# H9a WE1 reasoning[1]
fixes.append((l["worked_examples"][1]["reasoning"][1],
l["worked_examples"][1]["reasoning"][1].replace(
"$\\mathrm{Ca(OH)_{2}}+\\mathrm{H_{2}SO_{4}}\\rightarrow \\mathrm{CaSO_{4}}+2\\,\\mathrm{H_{2}O}$",
"$\\mathrm{Ca(OH)_{2}}(s)+\\mathrm{H_{2}SO_{4}}(aq)\\rightarrow \\mathrm{CaSO_{4}}(s)+2\\,\\mathrm{H_{2}O}(l)$"
)
))

# H9b WE3 reasoning[1]
fixes.append((l["worked_examples"][3]["reasoning"][1],
l["worked_examples"][3]["reasoning"][1].replace(
"$\\mathrm{Mg(OH)_{2}}+2\\,\\mathrm{HCl}\\rightarrow \\mathrm{MgCl_{2}}+2\\,\\mathrm{H_{2}O}$",
"$\\mathrm{Mg(OH)_{2}}(s)+2\\,\\mathrm{HCl}(aq)\\rightarrow \\mathrm{MgCl_{2}}(aq)+2\\,\\mathrm{H_{2}O}(l)$"
)
))

# H9c guided1 full_solution
fixes.append((l["guided_exercises"][1]["full_solution"],
l["guided_exercises"][1]["full_solution"].replace(
"$\\mathrm{NaOH}+\\mathrm{HNO_{3}}\\rightarrow\\mathrm{NaNO_{3}}+\\mathrm{H_{2}O}$",
"$\\mathrm{NaOH}(s)+\\mathrm{HNO_{3}}(aq)\\rightarrow\\mathrm{NaNO_{3}}(aq)+\\mathrm{H_{2}O}(l)$"
)
))

# H10 WE2 interpretation
fixes.append((l["worked_examples"][2]["interpretation"],
"El ácido gástrico está unas 4 veces más concentrado en H$^+$ que el zumo de limón, no un 35 % más, que es lo que saldría al dividir 2,3/1,7 tratando la escala como lineal. Una diferencia de pH de solo 0,6 unidades ya corresponde a un factor notable en concentración."
))

# H13 WE3 statement
fixes.append((l["worked_examples"][3]["statement"],
l["worked_examples"][3]["statement"].replace(
"Un comprimido de antiácido (leche de magnesia) contiene 400 mg de Mg(OH)$_2$",
"Un comprimido antiácido de hidróxido de magnesio contiene 400 mg de Mg(OH)$_2$"
)
))

# render fail flashcards[4].back
fixes.append((l["flashcards"][4]["back"],
"No: es un factor $10^{2}=100$ en $[\\mathrm{H^+}]$, no un factor 2. El pH es una escala logarítmica."
))

print("planned:", len(fixes))
applied = 0
skipped = []
for old, new in fixes:
    old_j = json.dumps(old, ensure_ascii=False)
    new_j = json.dumps(new, ensure_ascii=False)
    n = raw.count(old_j)
    if n == 1:
        raw = raw.replace(old_j, new_j, 1)
        applied += 1
    else:
        skipped.append((n, old_j[:90]))

print("applied:", applied, "of", len(fixes))
for n, s in skipped:
    print("SKIP", n, s)

with open(path, "w", encoding="utf-8") as f:
    f.write(raw)
print("DONE")
