# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"reasoning": [
          "Se identifica si el anión de cada sal es base conjugada de un ácido débil o no.",
          "Para CaCO3: el H+ añadido reacciona con CO3^2-, consumiéndolo.",
          "Para AgCl: el H+ no reacciona de forma apreciable con Cl-, porque HCl es un ácido fuerte."
        ],
        "solution": "La solubilidad de $CaCO_3$ **aumenta** al bajar el pH; la de $AgCl$ **no cambia** apreciablemente.",
        "interpretation": "$CO_3^{2-}$ es base conjugada de un ácido débil (el ácido carbónico), así que el $H^+$ añadido lo consume, desplazando el equilibrio de solubilidad hacia disolver más $CaCO_3$. $Cl^-$, en cambio, es la base conjugada de HCl, un ácido fuerte que está totalmente disociado: el $H^+$ no tiene ninguna tendencia a recombinarse con $Cl^-$, así que el pH no afecta a la solubilidad de AgCl.",
        "common_mistake": "Aplicar el mismo razonamiento del efecto de pH a cualquier sal, sin comprobar primero si su anión es o no la base conjugada de un ácido débil.",'''

new = r'''"reasoning": [
          "Se identifica si el anión de cada sal es base conjugada de un ácido débil o no.",
          "Para $CaCO_3$: el $H^+$ añadido reacciona con $CO_3^{2-}$, consumiéndolo.",
          "Para $AgCl$: el $H^+$ no reacciona de forma apreciable con $Cl^-$, porque $HCl$ es un ácido fuerte; pero el $HCl$ sí aporta $Cl^-$ al medio, y $Cl^-$ es precisamente el ion común de $AgCl$."
        ],
        "solution": "La solubilidad de $CaCO_3$ **aumenta** al bajar el pH. La de $AgCl$ **disminuye**, pero no por el pH en sí: es un efecto de ion común, porque el $HCl$ aporta $Cl^-$.",
        "interpretation": "$CO_3^{2-}$ es base conjugada de un ácido débil (el ácido carbónico), así que el $H^+$ añadido lo consume, desplazando el equilibrio de solubilidad hacia disolver más $CaCO_3$. $Cl^-$, en cambio, es la base conjugada de $HCl$, un ácido fuerte totalmente disociado: el $H^+$ no tiene ninguna tendencia a recombinarse con $Cl^-$, así que el pH en sí no afecta a la solubilidad de $AgCl$. Sin embargo, el $HCl$ añadido sí aporta $Cl^-$ a la disolución, y $Cl^-$ es el ion común de $AgCl$: por efecto de ion común, la solubilidad de $AgCl$ disminuye (p. ej., con $HCl$ $0{,}10$ M, $s'\\approx1{,}8\\times10^{-9}$ M, muy por debajo de $s=1{,}34\\times10^{-5}$ M en agua pura). La causa no es el pH, sino el anión añadido junto con el ácido.",
        "common_mistake": "Concluir que «el pH no afecta a $AgCl$» y, de ahí, que nada cambia: el pH en sí no afecta, pero el $HCl$ sí reduce la solubilidad de $AgCl$ por efecto de ion común (aportar $Cl^-$), no por el $H^+$.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
