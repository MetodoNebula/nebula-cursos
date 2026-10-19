# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''En cambio, para sales con anión neutro (que no reacciona con $H^+$, como $Cl^-$, $Br^-$ o $SO_4^{2-}$), el pH no tiene este efecto sobre la solubilidad.",'''
new = r'''En cambio, para sales cuyo anión es la base conjugada de un ácido fuerte ($Cl^-$, $Br^-$, $I^-$, $NO_3^-$), el pH no tiene este efecto sobre la solubilidad. El caso de $SO_4^{2-}$ es intermedio: es la base conjugada de $HSO_4^-$, un ácido débil pero no muy débil ($K_a\\approx10^{-2}$), así que la solubilidad de sulfatos como $BaSO_4$ aumenta algo en medio muy ácido, aunque mucho menos que en carbonatos o fosfatos.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
