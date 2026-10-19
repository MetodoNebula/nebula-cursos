import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

BS = chr(92)*2
NL = chr(92) + 'n'

# F4: theory_blocks[3].body — expand acidity block (Ka/pKa, resonance, phenol, amines)
old = "Los ácidos carboxílicos son mucho más ácidos que los alcoholes porque su base conjugada, el ion carboxilato, estabiliza la carga negativa por resonancia entre dos oxígenos; en un alcóxido la carga queda localizada en uno solo. Con $pK_a" + BS + "approx4{,}8$ para el ácido acético y $pK_a" + BS + "approx16$ para el etanol, la razón de constantes es $10^{16-4{,}8}" + BS + "approx1{,}6" + BS + "cdot10^{11}$."

new_lines = [
"Los ácidos carboxílicos son mucho más ácidos que los alcoholes porque su base conjugada, el ion carboxilato, estabiliza la carga negativa por resonancia entre dos oxígenos; en un alcóxido la carga queda localizada en uno solo.",
"",
"La fuerza de un ácido se mide con su constante de acidez $K_a$ (equilibrio $R" + BS + "text{-COOH}+H_2O" + BS + "rightleftharpoons R" + BS + "text{-COO}^-+H_3O^+$): cuanto mayor es $K_a$, más desplazado está el equilibrio hacia la derecha y más fuerte es el ácido. Por comodidad se usa $" + BS + "mathrm{p}K_a=-" + BS + "log K_a$, de modo que un $pK_a$ MENOR corresponde a un ácido MÁS fuerte. Con $pK_a" + BS + "approx4{,}8$ para el ácido acético y $pK_a" + BS + "approx16$ para el etanol, la razón de constantes es $K_a(" + BS + "text{ácido})/K_a(" + BS + "text{etanol})=10^{16-4{,}8}" + BS + "approx1{,}6" + BS + "cdot10^{11}$: el ácido acético es más de cien mil millones de veces más fuerte que el etanol como ácido.",
"",
"La razón estructural es la resonancia: en el ion carboxilato, $CH_3COO^-$, la carga negativa se reparte a partes iguales entre los dos oxígenos (dos estructuras resonantes equivalentes), lo que lo estabiliza mucho. En el ion etóxido, $CH_3CH_2O^-$, no hay ningún segundo átomo con el que compartir la carga: queda fija sobre un único oxígeno, mucho menos estable.",
"",
"El fenol, con un $-OH$ unido directamente a un anillo aromático, queda en un punto intermedio ($pK_a" + BS + "approx10$): su base conjugada, el ion fenóxido, puede deslocalizar parcialmente la carga hacia el anillo, pero de forma menos simétrica y eficaz que el carboxilato. Por eso el fenol es más ácido que un alcohol alifático, pero mucho menos que un ácido carboxílico.",
"",
"Las aminas, en cambio, no son ácidas por ese -NH: son BÁSICAS, porque el nitrógeno conserva un par de electrones libre capaz de aceptar un protón: $R" + BS + "text{-}NH_2+H_2O" + BS + "rightleftharpoons R" + BS + "text{-}NH_3^++OH^-$. Esa es la propiedad química característica de las aminas, igual que la acidez lo es de los ácidos carboxílicos y el fenol.",
]
new = NL.join(new_lines)
rep(old, new, 1, "F4 theory_blocks[3] expansion")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE C")
