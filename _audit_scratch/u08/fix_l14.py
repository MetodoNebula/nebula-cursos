import io, sys

BS = chr(92) * 2  # exactly two literal backslash characters, matching on-disk convention

path = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
data = open(path, encoding='utf-8').read()

key_start = '"14_Reacciones_de_adición.json"'
key_end = '"15_Regla_de_Markovnikov.json"'
i0 = data.find(key_start)
i1 = data.find(key_end)
assert i0 != -1 and i1 != -1 and i0 < i1
seg = data[i0:i1]

edits = []

edits.append((
"se rompe uno de los enlaces π del doble enlace, liberando dos electrones",
"se rompe el enlace π del doble enlace (o, si se parte de un triple enlace, uno de sus dos enlaces π), liberando dos electrones",
"L14-F5"
))

edits.append((
"Las cuatro parten del mismo doble enlace y las cuatro acaban con los dos carbonos unidos por un enlace simple; lo único que cambia es qué entra en cada carbono y qué condiciones hacen falta para que la reacción ocurra.",
"Las cuatro parten del mismo doble enlace y las cuatro acaban con los dos carbonos unidos por un enlace simple; lo único que cambia es qué entra en cada carbono y qué condiciones hacen falta para que la reacción ocurra."
+ chr(10)+chr(10) +
f"Por convención, en las ecuaciones de química orgánica se suelen omitir los estados de agregación (la mayoría de estos compuestos sencillos son gases o líquidos a temperatura ambiente); cuando convenga indicarlos explícitamente, puede escribirse, por ejemplo, CH$_2$=CH$_2$(g) + H$_2$(g) ${BS}xrightarrow{{{BS}text{{Pt}}}}$ CH$_3$-CH$_3$(g).",
"L14-F10"
))

edits.append((
"La **hidrohalogenación** suele escribirse en éter como disolvente; HCl, HBr y HI reaccionan todos de forma parecida.",
"La **hidrohalogenación** no necesita condiciones especiales (no requiere catalizador ni un disolvente determinado); los tres haluros de hidrógeno reaccionan de forma parecida, con reactividad HI > HBr > HCl.",
"L14-F11"
))

edits.append((
f">C=C< + H-X ${BS}xrightarrow{{{BS}text{{éter}}}}$ >C(H)-C(X)<",
">C=C< + H-X $" + chr(92) + "longrightarrow$ >C(H)-C(X)<",
"L14-coherence-table"
))

edits.append((
"Es la reacción clásica de 'decoloración del agua de bromo': el Br$_2$, de color pardo, desaparece al adicionarse, y por eso se usa como ensayo cualitativo para detectar un doble enlace.",
"Es la reacción clásica de 'decoloración de una disolución de bromo' (aquí, Br$_2$ en CCl$_4$; en agua de bromo propiamente dicha el producto principal sería distinto, una bromohidrina, por la presencia de agua): el Br$_2$, de color pardo, desaparece al adicionarse, y por eso se usa como ensayo cualitativo para detectar un doble enlace.",
"L14-F6-worked0"
))

edits.append((
"Un alqueno decolora el agua de bromo sin necesidad de luz, dando un único producto.",
"Un alqueno decolora una disolución de Br$_2$ en CCl$_4$ sin necesidad de luz, dando un único producto.",
"L14-F6-mcq2"
))

alkyne_new = (
"Por ejemplo, el etino (acetileno), HC" + chr(8801) + "CH, reacciona con Br$_2$ en dos etapas sucesivas: "
"HC" + chr(8801) + "CH + Br$_2$ " + chr(8594) + " CHBr=CHBr (1,2-dibromoeteno, con un solo doble enlace ya); "
"y, con un segundo Br$_2$, CHBr=CHBr + Br$_2$ " + chr(8594) + " CHBr$_2$-CHBr$_2$ (1,1,2,2-tetrabromoetano, "
"totalmente saturado, con los cuatro átomos de halógeno). Con H$_2$ ocurre lo mismo por etapas: "
f"HC{chr(8801)}CH + H$_2$ ${BS}xrightarrow{{{BS}text{{Pt}}}}$ CH$_2$=CH$_2$ (hidrogenación parcial: queda un alqueno) "
f"y, si se añade más H$_2$, CH$_2$=CH$_2$ + H$_2$ ${BS}xrightarrow{{{BS}text{{Pt}}}}$ CH$_3$-CH$_3$ (hidrogenación total: queda ya el alcano)."
)
edits.append((
"Por ejemplo, con exceso de Br$_2$ un alquino acaba totalmente saturado con cuatro átomos de halógeno.",
alkyne_new,
"L14-F7"
))

insaturacion_new = (
f" Una herramienta auxiliar relacionada es el **grado de insaturación**: para un hidrocarburo de fórmula C$_x$H$_y$ "
f"(sin halógenos ni heteroátomos), se calcula como $x+1-{BS}frac{{y}}{{2}}$, y cuenta cuántas 'unidades de insaturación' "
"tiene la molécula, donde cada doble enlace o cada anillo aporta 1 unidad y cada triple enlace aporta 2. Por ejemplo, "
"el buta-1,3-dieno, C$_4$H$_6$, tiene grado de insaturación $4+1-6/2=2$, que coincide con sus dos dobles enlaces. "
"Cada hidrogenación catalítica añade un H$_2$ y reduce este grado en una unidad, hasta llegar a 0 en el alcano "
"(o cicloalcano) completamente saturado."
)
edits.append((
alkyne_new,
alkyne_new + chr(10) + chr(10) + insaturacion_new.strip(),
"L14-F4-append"
))

edits.append((
"Fórmula del grado de insaturación de un hidrocarburo C_xH_y, y su relación con la hidrogenación",
"Fórmula del grado de insaturación de un hidrocarburo C$_x$H$_y$, y su relación con la hidrogenación",
"L14-F9"
))

edits.append((
'        "why": "El error se detecta al contrastar el resultado con las condiciones y relaciones del problema.",\n        "how_to_avoid": "Mirar primero el sustrato: si tiene un enlace múltiple, es adición; si está saturado, solo puede ser sustitución.",',
'        "why": "Se clasifica la reacción fijándose solo en el reactivo (X$_2$) en vez de en lo que le ocurre al sustrato (si está saturado o tiene un enlace múltiple).",\n        "how_to_avoid": "Mirar primero el sustrato: si tiene un enlace múltiple, es adición; si está saturado, solo puede ser sustitución.",',
"L14-F8"
))

edits.append((
"así que hacen falta 2 mol de H$_2$ por mol de C$_5$H$_8$ para obtener el alcano saturado C$_5$H$_{12}$ (pentano).",
"así que hacen falta 2 mol de H$_2$ por mol de C$_5$H$_8$ para obtener un alcano de fórmula C$_5$H$_{12}$. El enunciado no fija el esqueleto de los dos dobles enlaces, así que solo puede afirmarse con seguridad esa fórmula molecular: sería pentano si la cadena es lineal (p. ej. a partir del penta-1,3-dieno), pero 2-metilbutano si el esqueleto es ramificado como el del isopreno (2-metilbuta-1,3-dieno).",
"L14-F1"
))

old_g0_tail = (
    '"answer": "(a) CH$_3$-CHCl-CHCl-CH$_3$ (2,3-diclorobutano). (b) CH$_3$-CH$_2$-CHI-CH$_3$ (2-yodobutano).",\n'
    '        "common_errors": [\n'
    '          "En (b), dibujar dos productos distintos como si hubiera ambigüedad, sin darse cuenta de que por simetría ambos \'caminos\' llevan al mismo compuesto."\n'
    '        ],\n'
    '        "provenance": "SOURCE_DERIVED"\n'
    '      },\n'
    '      {\n'
    '        "id": "EX-Q08-14-G2",'
)
new_full_sol = (
    f'"full_solution": "(a) CH$_3$-CH=CH-CH$_3$ + Cl$_2$ ${BS}xrightarrow{{{BS}text{{CCl}}_4}}$ CH$_3$-CHCl-CHCl-CH$_3$ '
    "(2,3-diclorobutano). Comprobación del ajuste: 4 C, 8 H y 2 Cl a cada lado. (b) CH$_3$-CH=CH-CH$_3$ + HI "
    + chr(8594) + ' CH$_3$-CH$_2$-CHI-CH$_3$ (2-yodobutano). Comprobación: 4 C, 9 H y 1 I a cada lado. '
    "En los dos casos, al ser el but-2-eno un alqueno simétrico (los dos carbonos del doble enlace son equivalentes), "
    'no importa en qué carbono entra cada átomo del reactivo: solo hay un producto posible."'
)
new_g0_tail = (
    '"answer": "(a) CH$_3$-CHCl-CHCl-CH$_3$ (2,3-diclorobutano). (b) CH$_3$-CH$_2$-CHI-CH$_3$ (2-yodobutano).",\n'
    '        "common_errors": [\n'
    '          "En (b), dibujar dos productos distintos como si hubiera ambigüedad, sin darse cuenta de que por simetría ambos \'caminos\' llevan al mismo compuesto."\n'
    '        ],\n'
    '        "provenance": "SOURCE_DERIVED",\n'
    '        ' + new_full_sol + '\n'
    '      },\n'
    '      {\n'
    '        "id": "EX-Q08-14-G2",'
)
edits.append((old_g0_tail, new_g0_tail, "L14-F2"))

edits.append((
"Procedimiento: El anillo no se rompe: la adición solo afecta a los dos carbonos del doble enlace, estén en cadena abierta o en un ciclo. Añade un Br a cada uno de esos dos carbonos del anillo. Conclusión: 1,2-dibromociclohexano, C$_6$H$_{10}$Br$_2$.",
f"(a) C$_6$H$_{{10}}$ (ciclohexeno) + Br$_2$ ${BS}xrightarrow{{{BS}text{{CCl}}_4}}$ C$_6$H$_{{10}}$Br$_2$ (1,2-dibromociclohexano). (b) Comprobación del ajuste: 6 C, 10 H y 2 Br a cada lado. El anillo no se rompe: la adición solo afecta a los dos carbonos que forman el doble enlace dentro del ciclo; el resto del anillo permanece intacto.",
"L14-F3"
))

ok = True
for old, new, label in edits:
    c = seg.count(old)
    if c != 1:
        print(f"FAIL [{label}] count={c}")
        ok = False
    else:
        seg = seg.replace(old, new, 1)
        print(f"OK [{label}]")

if not ok:
    print("ABORTED")
    sys.exit(1)

data2 = data[:i0] + seg + data[i1:]
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(data2)
print("ALL EDITS APPLIED")
