# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

# H5a: WE-Q05-12-1 solution -> markdown table
edits.append(("H5_WE0", r'''"solution": "$x=n_0\\alpha=0{,}0300\\cdot0{,}600=0{,}0180$ mol. Tabla (mol): $N_2O_4$: inicial $0{,}0300$, cambio $-0{,}0180$, equilibrio $0{,}0120$. $NO_2$: inicial $0$, cambio $+0{,}0360$, equilibrio $0{,}0360$. $[N_2O_4]_{eq}=0{,}0120/5{,}00=0{,}00240$ M; $[NO_2]_{eq}=0{,}0360/5{,}00=0{,}00720$ M.",''',
r'''"solution": "$x=n_0\\alpha=0{,}0300\\cdot0{,}600=0{,}0180$ mol.\n\n| | $N_2O_4$ | $NO_2$ |\n|---|---|---|\n| Inicial (mol) | $0{,}0300$ | $0$ |\n| Cambio (mol) | $-0{,}0180$ | $+0{,}0360$ |\n| Equilibrio (mol) | $0{,}0120$ | $0{,}0360$ |\n\n$[N_2O_4]_{eq}=0{,}0120/5{,}00=0{,}00240$ M; $[NO_2]_{eq}=0{,}0360/5{,}00=0{,}00720$ M.",'''
))

# H5b: EX-Q05-12-S1 full_solution -> markdown table
edits.append(("H5_EX0", r'''"full_solution": "Moles de $SO_3$ disociados $=0{,}0400\\cdot0{,}250=0{,}0100$ mol; con coeficiente 2, el avance es $x=0{,}0100/2=0{,}00500$ mol. Equilibrio (mol): $SO_3=0{,}0300$; $SO_2=2x=0{,}0100$; $O_2=x=0{,}00500$. Concentraciones ($V=3{,}00$ L): $[SO_3]=0{,}0100$ M; $[SO_2]=0{,}00333$ M; $[O_2]=0{,}00167$ M. $K_c=\\dfrac{[SO_2]^2[O_2]}{[SO_3]^2}=\\dfrac{0{,}00333^2\\cdot0{,}00167}{0{,}0100^2}=1{,}85\\cdot10^{-4}$ mol/L.",''',
r'''"full_solution": "Moles de $SO_3$ disociados $=0{,}0400\\cdot0{,}250=0{,}0100$ mol; con coeficiente 2, el avance es $x=0{,}0100/2=0{,}00500$ mol.\n\n| | $SO_3$ | $SO_2$ | $O_2$ |\n|---|---|---|---|\n| Inicial (mol) | $0{,}0400$ | $0$ | $0$ |\n| Cambio (mol) | $-0{,}0100$ | $+0{,}0100$ | $+0{,}00500$ |\n| Equilibrio (mol) | $0{,}0300$ | $0{,}0100$ | $0{,}00500$ |\n\nConcentraciones ($V=3{,}00$ L): $[SO_3]=0{,}0100$ M; $[SO_2]=0{,}00333$ M; $[O_2]=0{,}00167$ M. $K_c=\\dfrac{[SO_2]^2[O_2]}{[SO_3]^2}=\\dfrac{0{,}00333^2\\cdot0{,}00167}{0{,}0100^2}=1{,}85\\cdot10^{-4}$ mol/L.",'''
))

# H5c: EX-Q05-12-EXAM1 full_solution -> markdown table
edits.append(("H5_EQ0", r'''"full_solution": "$c_0(NOCl)=0{,}0600/2{,}50=0{,}0240$ M. (a) $x=[Cl_2]_{eq}=5{,}00\\cdot10^{-3}$ M (coeficiente 1). Como el coeficiente de $NOCl$ es 2, su cambio es $-2x$, y $\\alpha=2x/c_0=2\\cdot5{,}00\\cdot10^{-3}/0{,}0240=0{,}417$. Equilibrio: $[NOCl]=0{,}0140$ M; $[NO]=0{,}0100$ M; $[Cl_2]=5{,}00\\cdot10^{-3}$ M. (b) $K_c=\\dfrac{[NO]^2[Cl_2]}{[NOCl]^2}=\\dfrac{0{,}0100^2\\cdot5{,}00\\cdot10^{-3}}{0{,}0140^2}=2{,}55\\cdot10^{-3}$ mol/L. (c) $\\Delta n=(2+1)-2=1$; $RT=28{,}7$ atm·L/mol; $K_p=K_c\\cdot RT=0{,}0732$ atm.",''',
r'''"full_solution": "$c_0(NOCl)=0{,}0600/2{,}50=0{,}0240$ M.\n\n| | $NOCl$ | $NO$ | $Cl_2$ |\n|---|---|---|---|\n| Inicial (M) | $0{,}0240$ | $0$ | $0$ |\n| Cambio (M) | $-2x$ | $+2x$ | $+x$ |\n| Equilibrio (M) | $0{,}0140$ | $0{,}0100$ | $5{,}00\\cdot10^{-3}$ |\n\n(a) $x=[Cl_2]_{eq}=5{,}00\\cdot10^{-3}$ M (coeficiente 1). Como el coeficiente de $NOCl$ es 2, su cambio es $-2x$, y $\\alpha=2x/c_0=2\\cdot5{,}00\\cdot10^{-3}/0{,}0240=0{,}417$. (b) $K_c=\\dfrac{[NO]^2[Cl_2]}{[NOCl]^2}=\\dfrac{0{,}0100^2\\cdot5{,}00\\cdot10^{-3}}{0{,}0140^2}=2{,}55\\cdot10^{-3}$ mol/L. (c) $\\Delta n=(2+1)-2=1$; $RT=28{,}7$ atm·L/mol; $K_p=K_c\\cdot RT=0{,}0732$ atm.",'''
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
