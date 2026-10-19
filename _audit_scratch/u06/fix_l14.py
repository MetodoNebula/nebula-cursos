import json, io

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U06_Acido_Base.json"
with open(path, encoding="utf-8") as f:
    raw = f.read()
data = json.loads(raw)
key = "14_Indicadores_curvas_de_valoración_y_elección_del_punto.json"
l = data[key]

fixes = []

# H1
fixes.append((l["theory_blocks"][2]["assets"][0]["caption"],
"Curva de valoración de 25,00 mL de HCl 0,100 M con NaOH 0,100 M (puntos calculados). El salto es tan brusco que entre 24,99 y 25,01 mL (0,02 mL de diferencia) el pH pasa de 4,70 a 9,30, y entre 24,90 y 25,10 mL (0,20 mL, unas cuatro gotas) pasa de 3,70 a 10,30. Las bandas sombreadas marcan los intervalos de viraje del naranja de metilo (3,1-4,4) y de la fenolftaleína (8,2-10,0): ambos caen dentro del salto."
))

# H2 + H4 + H9 (theory_blocks[3].body)
new_tb3 = ("Un indicador ácido-base es, él mismo, un ácido (o una base) débil orgánico, HIn, cuya forma ácida y su base conjugada In$^-$ tienen colores distintos: "
"$\\mathrm{HIn}(aq)+\\mathrm{H_2O}(l)\\rightleftharpoons \\mathrm{In^-}(aq)+\\mathrm{H_3O^+}(aq)$, con $K_{In}=\\dfrac{[\\mathrm{In^-}][\\mathrm{H_3O^+}]}{[\\mathrm{HIn}]}$, de donde "
"$\\mathrm{pH}=pK_{In}+\\log_{10}\\!\\left(\\dfrac{[\\mathrm{In^-}]}{[\\mathrm{HIn}]}\\right)$. El ojo humano solo percibe el color de una de las dos formas cuando esta está, aproximadamente, 10 veces en exceso sobre la otra, "
"así que el color vira en un intervalo de pH de, aproximadamente, $pK_{In}\\pm1$. Algunos indicadores habituales: naranja de metilo (viraje 3,1-4,4, rojo→amarillo), rojo de metilo (4,4-6,2, rojo→amarillo), "
"azul de bromotimol (6,0-7,6, amarillo→azul) y fenolftaleína (8,2-10,0, incolora→rosa).\n\n"
"El indicador correcto es aquel cuyo intervalo de viraje cae dentro (o muy cerca) del tramo casi vertical de la curva, idealmente con $pK_{In}$ próximo al pH de equivalencia; el punto de equivalencia no tiene por qué estar en el centro exacto de ese intervalo. "
"Si el salto es muy pronunciado y ancho —como en ácido fuerte-base fuerte—, casi cualquier indicador con viraje dentro de ese tramo sirve, porque el error de volumen que introduce es minúsculo.\n\n"
"Si en cambio el salto es más estrecho o está desplazado (como se verá a continuación para ácido débil-base fuerte o al revés), la elección deja de ser indiferente: un indicador fuera de sitio puede dar un error de valoración grande.")
fixes.append((l["theory_blocks"][3]["body"], new_tb3))

# part of H4: relabel the AS-Q06-14-2 caption text (SVG image itself not regenerated)
fixes.append((l["theory_blocks"][3]["assets"][0]["caption"],
"El cruce de las formas ácida (HIn) y básica (In$^-$) del indicador ocurre en pH$=pK_{In}$, una propiedad del propio indicador, no el punto de equivalencia de la valoración. El intervalo de viraje (aproximadamente $pK_{In}\\pm1$) debe caer dentro del salto de pH de la valoración para que el punto final observado se acerque al punto de equivalencia real. (Nota: esta figura esquemática usa las etiquetas antiguas «salto»/«equivalencia» en el cruce; léanse como «pH = $pK_{In}$».)"
))

# H5 (theory_blocks[4].body) - insert new paragraph about curve shape before final paragraph
old_tb4 = l["theory_blocks"][4]["body"]
anchor = "Esto no es un caso aparte sin relación con lo anterior"
idx = old_tb4.find(anchor)
new_paragraph = ("Además del pH de equivalencia, la forma entera de la curva cambia respecto al caso fuerte-fuerte. En una valoración de ácido débil con base fuerte (p. ej. ácido acético 0,100 M con NaOH 0,100 M): el pH inicial es más alto (2,87, el de un ácido débil, no el de uno fuerte); antes de la equivalencia se forma una zona de disolución reguladora, con $\\mathrm{pH}=pK_a+\\log_{10}(n_{\\mathrm{A^-}}/n_{\\mathrm{HA}})$; en el volumen de semiequivalencia ($V=V_{eq}/2$, aquí 12,50 mL) ese cociente vale 1 y $\\mathrm{pH}=pK_a$ exactamente (4,74); y el salto final es más corto y está desplazado hacia pH básicos (de pH$\\approx$7,1 a pH$\\approx$10,3 entre 24,90 y 25,10 mL, en vez de 3,70 a 10,30 como en fuerte-fuerte). Por ejemplo, el volumen al que el pH vale 4,4 (el límite del naranja de metilo) se obtiene despejando $V$ en $4{,}4=4{,}74+\\log_{10}\\!\\left(\\dfrac{V}{25{,}00-V}\\right)$, lo que da $V\\approx7{,}8$ mL, muy lejos de los 25,00 mL de la equivalencia real.\n\n")
assert idx != -1, "anchor not found in theory_blocks[4]"
new_tb4 = old_tb4[:idx] + new_paragraph + old_tb4[idx:]
fixes.append((old_tb4, new_tb4))

# H6
fixes.append((l["common_mistakes"][0]["why"],
"Con un buen indicador (y, sobre todo, en la valoración fuerte-fuerte de los primeros ejemplos) ambos volúmenes coinciden casi exactamente, y se acaba generalizando que son lo mismo."
))
fixes.append((l["common_mistakes"][1]["why"],
"La primera valoración que se estudia es fuerte-fuerte, con pH de equivalencia 7,00, y esa igualdad se generaliza sin comprobar si el ácido o la base de partida son débiles."
))

# H7
fixes.append((l["worked_examples"][3]["reasoning"][1],
"Todo el ácido acético se ha convertido en acetato: la disolución resultante es, sencillamente, acetato de sodio en agua, y hay que tratar su hidrólisis como en la lección «Hidrólisis de sales»: el acetato es una base débil con $K_b=K_w/K_a$."
))

# H8 + H14
fixes.append((l["guided_exercises"][1]["full_solution"],
"(a) En la equivalencia, $V_{\\text{ácido}}=25{,}00$ mL y $[\\mathrm{NH_{4}^+}]=2{,}50\\cdot10^{-3}/0{,}05000=0{,}0500$ M. $K_a=1{,}0\\cdot10^{-14}/1{,}8\\cdot10^{-5}=5{,}56\\cdot10^{-10}$. $[\\mathrm{H^+}]=\\sqrt{5{,}56\\cdot10^{-10}\\cdot0{,}0500}=5{,}27\\cdot10^{-6}$ M, $\\mathrm{pH}=5{,}28$.\n\n(b) De los dos, el naranja de metilo. Su intervalo (3,1-4,4) queda algo por debajo del pH de equivalencia (5,28), pero dentro del salto: el pH 4,4 se alcanza con solo ~0,02 mL de HCl en exceso sobre los 25,00 mL de equivalencia, un error despreciable. La fenolftaleína, en cambio, deja de verse rosa a pH 8,2, que se alcanza ya a ~22,98 mL (2 mL antes de la equivalencia, un error del 8 %): viraría mucho antes de llegar a la equivalencia real, porque aquí el pH parte de un valor alto y baja."
))
fixes.append((l["guided_exercises"][1]["answer"],
"(a) $\\mathrm{pH}=5{,}28$. (b) Naranja de metilo: vira con solo ~0,02 mL de exceso de HCl; la fenolftaleína daría un error del 8 %."
))

# H10
fixes.append((l["worked_examples"][2]["reasoning"][2],
"El salto de pH entre estos dos volúmenes tan próximos va a ser enorme porque el exceso cambia de naturaleza: pasa de ser $1{,}0\\times10^{-6}$ mol de H$^+$ a ser $1{,}0\\times10^{-6}$ mol de OH$^-$, con lo que $[\\mathrm{H^+}]$ cambia de unos $2\\times10^{-5}$ M a unos $5\\times10^{-10}$ M, más de cuatro órdenes de magnitud, es decir, más de cuatro unidades de pH."
))

# H11
fixes.append((l["summary"]["formulas"][0],
"a\\,n_{\\text{ácido}}=b\\,n_{\\text{base}}\\ \\text{(en la equivalencia; }a,b=\\text{H}^+/\\text{OH}^-\\text{ por fórmula; si ambos son 1, }n_{\\text{ácido}}=n_{\\text{base}}\\text{)}"
))

# H12
fixes.append((l["exercises"][1]["hints"][0],
"El error relativo se calcula, en valor absoluto, como $\\dfrac{|V_{\\text{punto final erróneo}}-V_{\\text{equivalencia}}|}{V_{\\text{equivalencia}}}\\times100$ (aquí el indicador vira antes de la equivalencia, así que es un error «por defecto»)."
))

# H15
fixes.append((l["misconceptions"][0]["related_exercises"],
"el ejercicio 3 (equivalencia frente a punto final) y el reto"
))

# H17 + plantilla mark_scheme exam0
fixes.append((l["exam_questions"][0]["mark_scheme"],
["Para el punto de (a) debes decir que el punto de equivalencia es un cálculo estequiométrico (moles de H$^+$ = moles de OH$^-$), no basta con decir «verdadera».",
 "Para el punto de (b) debes explicar que, cerca de la equivalencia, basta una gota para cambiar mucho el pH; decir solo «falsa» no es suficiente.",
 "Para el punto de (c) debes mencionar la hidrólisis de la sal resultante para dar el punto completo, no basta con decir «falsa».",
 "Para el punto de (d) debes decir que solo en fuerte-fuerte el pH de equivalencia es 7, y que en los demás casos hay que calcularlo antes de elegir el indicador."]
))

# H17 mark_scheme exam1
fixes.append((l["exam_questions"][1]["mark_scheme"],
["Para los 2 puntos del pH debes plantear la hidrólisis del $\\mathrm{NH_4^+}$ y dar el resultado numérico, no solo el valor final.",
 "Para el punto del indicador debes identificar el rojo de metilo, no el naranja de metilo ni la fenolftaleína.",
 "Para el último punto debes justificar comparando los tres intervalos de viraje con el pH de equivalencia calculado, no basta con nombrar el indicador."]
))

# H3
fixes.append((l["objectives"][1]["statement"],
"Interpretar una curva de valoración pH frente a volumen añadido: su forma de 'S', el salto brusco de pH cerca de la equivalencia y las zonas más planas antes y después (por exceso de ácido o de base; solo en valoraciones de ácido o base débil la zona previa a la equivalencia es, además, una disolución reguladora)."
))

print("planned fixes:", len(fixes))

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
        skipped.append((n, old_j[:80]))

print("applied:", applied, "of", len(fixes))
for n, s in skipped:
    print("SKIP occurrences=", n, s)

with open(path, "w", encoding="utf-8") as f:
    f.write(raw)
print("DONE")
