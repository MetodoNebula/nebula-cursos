# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"answer": "(c) $\\approx0{,}227$ g de $PbSO_4$",
        "full_solution": "(a) $V_{total}=500$ mL; $[Pb^{2+}]=\\dfrac{0{,}0030\\times250}{500}=1{,}5\\times10^{-3}$ M; por simetría, $[SO_4^{2-}]=1{,}5\\times10^{-3}$ M también. (b) $Q_i=(1{,}5\\times10^{-3})^2=2{,}25\\times10^{-6}$. Como $Q_i\\gg K_{sp}=1{,}6\\times10^{-8}$, precipita. (c) Moles iniciales de cada ion: $n=1{,}5\\times10^{-3}\\times0{,}500=7{,}5\\times10^{-4}$ mol (iguales, reacción 1:1 sin exceso). Prácticamente todo precipita como $PbSO_4$: $m=7{,}5\\times10^{-4}\\times303{,}3=0{,}227$ g.",
        "mark_scheme": [
          "1 punto por la dilución correcta en (a)",
          "1 punto por el cálculo y comparación de Qi en (b)",
          "2 puntos por el balance de moles y la masa final en (c), aceptando la pequeña cantidad residual en disolución según Ksp como redondeo despreciable"
        ],'''

new = r'''"answer": "(a) $[Pb^{2+}]=[SO_4^{2-}]=1{,}5\\times10^{-3}$ M. (b) $Q_i=2{,}25\\times10^{-6}>K_{sp}=1{,}6\\times10^{-8}$: precipita. (c) Máximo $0{,}227$ g (≈0,208 g teniendo en cuenta lo que queda disuelto en el equilibrio).",
        "full_solution": "(a) $V_{total}=500$ mL; $[Pb^{2+}]=\\dfrac{0{,}0030\\times250}{500}=1{,}5\\times10^{-3}$ M; por simetría, $[SO_4^{2-}]=1{,}5\\times10^{-3}$ M también.\n\n(b) $Q_i=(1{,}5\\times10^{-3})^2=2{,}25\\times10^{-6}$. Como $Q_i\\gg K_{sp}=1{,}6\\times10^{-8}$, precipita.\n\n(c) Moles iniciales de cada ion: $n=1{,}5\\times10^{-3}\\times0{,}500=7{,}5\\times10^{-4}$ mol (iguales, reacción 1:1 sin exceso). Si precipitara todo, $m=7{,}5\\times10^{-4}\\times303{,}3=0{,}227$ g: esto es la cota superior teórica.\n\nComprobación: en el equilibrio quedan disueltos $[Pb^{2+}]=[SO_4^{2-}]=\\sqrt{K_{sp}}=\\sqrt{1{,}6\\times10^{-8}}=1{,}26\\times10^{-4}$ M ⟹ $6{,}3\\times10^{-5}$ mol en los 500 mL (un $8{,}4\\,\\%$ del total, nada despreciable con este $K_{sp}$ y estas concentraciones). Precipitan realmente $7{,}5\\times10^{-4}-6{,}3\\times10^{-5}=6{,}87\\times10^{-4}$ mol $=0{,}208$ g. El valor $0{,}227$ g es solo el máximo teórico.",
        "mark_scheme": [
          "Para la puntuación completa debes: diluir correctamente al volumen total (1 p), calcular $Q_i$ y compararlo con $K_{sp}$ (1 p), y hacer el balance de moles con el reactivo limitante y la masa (2 p)."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
