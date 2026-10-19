# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H5_fc_a", r'''"back": "Cuando el anión de la sal es la base conjugada de un ácido débil (CO3²⁻, F⁻, S²⁻, OH⁻...). Si el anión es de un ácido fuerte (Cl⁻, SO4²⁻...), el pH no tiene ese efecto.",''',
r'''"back": "Cuando el anión de la sal es la base conjugada de un ácido débil (CO3²⁻, F⁻, S²⁻, OH⁻...). Si el anión es de un ácido fuerte (Cl⁻, Br⁻, I⁻, NO3⁻), el pH no tiene ese efecto. SO4²⁻ es un caso intermedio: su ácido conjugado (HSO4⁻) es débil pero no muy débil, así que hay un efecto, aunque pequeño salvo en medio muy ácido.",'''
))

edits.append(("H5_fc_b", r'''"back": "No: solo a las sales con anión básico (base conjugada de un ácido débil). Para sales como AgCl o BaSO4, el pH no tiene un efecto apreciable.",''',
r'''"back": "No: solo a las sales con anión básico (base conjugada de un ácido débil). Para sales como AgCl, el pH no tiene efecto; en BaSO4 el efecto existe pero es pequeño, porque SO4²⁻ es una base débil, aunque no tan débil como CO3²⁻ o F⁻.",'''
))

edits.append(("H5_misc", r'''"why_it_appears": "Se generaliza el caso de sales con anión neutro (como Cl⁻ o SO4²⁻, que no reaccionan con H+) a todas las sales, sin distinguir si el anión es básico.",''',
r'''"why_it_appears": "Se generaliza el caso de sales con anión de ácido fuerte (como Cl⁻, que no reacciona de forma apreciable con H+) a todas las sales, sin distinguir si el anión es básico (CO3²⁻, F⁻) o solo ligeramente básico (SO4²⁻, con efecto pequeño).",'''
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
