# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H3_fullsol", r'''"full_solution": "Sea $Q=\\dfrac{P_C^{c}P_D^{d}}{P_A^{a}P_B^{b}}$ en el equilibrio, con $Q=K$. Si $V\\to fV$ a $T$ y moles constantes, cada presión parcial pasa de $P_i$ a $P_i/f$. Sustituyendo: $Q_{nuevo}=K\\cdot f^{-\\Delta n}$, puesto que $\\Delta n=(c+d)-(a+b)$. Comprobación numérica: $\\Delta n=1$, $f=0{,}5$: $Q_{nuevo}=K_p\\cdot 0{,}5^{-1}=0{,}150\\cdot2=0{,}300$, exactamente el valor hallado en el ejemplo anterior.",''',
r'''"full_solution": "Sea $Q=\\dfrac{P_C^{c}P_D^{d}}{P_A^{a}P_B^{b}}$ en el equilibrio, con $Q=K$. Si $V\\to fV$ a $T$ y moles constantes, cada presión parcial pasa de $P_i$ a $P_i/f$. Sustituyendo: $Q_{nuevo}=\\dfrac{(P_C/f)^{c}(P_D/f)^{d}}{(P_A/f)^{a}(P_B/f)^{b}}=\\dfrac{P_C^{c}P_D^{d}}{P_A^{a}P_B^{b}}\\cdot\\dfrac{f^{-(c+d)}}{f^{-(a+b)}}=K\\cdot f^{-[(c+d)-(a+b)]}=K\\cdot f^{-\\Delta n}$, puesto que $\\Delta n=(c+d)-(a+b)$. Si $f<1$ (se comprime) y $\\Delta n>0$ (más moles de gas en productos), entonces $f^{-\\Delta n}>1$ y $Q_{nuevo}>K$: el sistema avanza hacia reactivos, el lado con menos moles de gas, confirmando la regla de presión/volumen. Comprobación numérica: $\\Delta n=1$, $f=0{,}5$: $Q_{nuevo}=K_p\\cdot 0{,}5^{-1}=0{,}150\\cdot2=0{,}300$, exactamente el valor hallado en el ejemplo anterior.",'''
))

edits.append(("H8_commonerrors", r'''"common_errors": [
          "Olvidar el signo negativo del exponente, obteniendo f^(+Δn) en vez de f^(-Δn), lo que invertiría la predicción del sentido del desplazamiento."
        ],''',
r'''"common_errors": [
          "Olvidar el signo negativo del exponente, obteniendo $f^{+\\Delta n}$ en vez de $f^{-\\Delta n}$, lo que invertiría la predicción del sentido del desplazamiento."
        ],'''
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
