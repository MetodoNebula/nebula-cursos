# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"statement": "Para el equilibrio $NH_4Cl(s)\\rightleftharpoons NH_3(g)+HCl(g)$: (a) escribe la expresión de Kc. (b) escribe la expresión de Kp. (c) calcula Δn para el efecto de presión. (d) explica, en una frase, por qué este equilibrio es formalmente análogo a un Ksp aunque no se trate de iones en disolución.",
        "answer": "(a) $K_c=[NH_3][HCl]$. (b) $K_p=P(NH_3)P(HCl)$. (c) $\\Delta n=2-0=+2$. (d) Es análogo porque también es un sólido en equilibrio con las especies que produce al descomponerse, y el sólido se tacha igual que en Ksp.",
        "full_solution": "(a) NH4Cl es sólido, se tacha; quedan los dos gases: $K_c=[NH_3][HCl]$. (b) Igual con presiones parciales: $K_p=P(NH_3)P(HCl)$. (c) Solo cuentan los gases: productos, 1+1=2 moles de gas; reactivos, 0 (NH4Cl es sólido). $\\Delta n=2-0=+2$. (d) Aunque aquí los productos son gases y en Ksp son iones en disolución, la lógica es idéntica: un sólido puro se descompone en otras especies, y ese sólido no aparece en la constante; Ksp es simplemente el caso en que esas «otras especies» son iones acuosos en vez de gases.",
        "mark_scheme": [
          "1 punto por (a)",
          "1 punto por (b)",
          "1 punto por (c)",
          "1 punto por (d), exigiendo mencionar explícitamente que el sólido se tacha en ambos casos"
        ],
        "common_errors": [
          "En (a) y (b), incluir NH4Cl(s) en la expresión.",
          "En (c), olvidar filtrar el sólido antes de contar moles de gas."
        ],'''

new = r'''"statement": "Para el equilibrio $\\mathrm{NH_4Cl(s)\\rightleftharpoons NH_3(g)+HCl(g)}$:\n\n(a) Escribe la expresión de $K_c$.\n\n(b) Escribe la expresión de $K_p$.\n\n(c) Calcula $\\Delta n$ para el efecto de presión.\n\n(d) Explica, en una frase, por qué este equilibrio es formalmente análogo a un $K_{sp}$ aunque no se trate de iones en disolución.\n\n(e) Si a $340\\,^{\\circ}\\mathrm{C}$ la presión total en el equilibrio es $0{,}20\\,\\mathrm{atm}$, calcula $K_p$ y $K_c$ ($R=0{,}082\\,\\mathrm{atm\\,L\\,mol^{-1}\\,K^{-1}}$).",
        "answer": "(a) $K_c=[\\mathrm{NH_3}][\\mathrm{HCl}]$. (b) $K_p=p_{\\mathrm{NH_3}}\\,p_{\\mathrm{HCl}}$. (c) $\\Delta n=2-0=+2$. (d) Es análogo porque también es un sólido en equilibrio con las especies que produce al descomponerse, y el sólido se tacha igual que en $K_{sp}$. (e) $p_{\\mathrm{NH_3}}=p_{\\mathrm{HCl}}=0{,}10$ atm; $K_p=0{,}010\\,\\mathrm{atm^2}$; $K_c=K_p/(RT)^2\\approx3{,}9\\times10^{-6}\\,\\mathrm{mol^2\\,L^{-2}}$.",
        "full_solution": "(a) $\\mathrm{NH_4Cl}$ es sólido, se tacha; quedan los dos gases: $K_c=[\\mathrm{NH_3}][\\mathrm{HCl}]$.\n\n(b) Igual con presiones parciales: $K_p=p_{\\mathrm{NH_3}}\\,p_{\\mathrm{HCl}}$.\n\n(c) Solo cuentan los gases: productos, $1+1=2$ moles de gas; reactivos, 0 ($\\mathrm{NH_4Cl}$ es sólido). $\\Delta n=2-0=+2$.\n\n(d) Aunque aquí los productos son gases y en $K_{sp}$ son iones en disolución, la lógica es idéntica: un sólido puro se descompone en otras especies, y ese sólido no aparece en la constante; $K_{sp}$ es simplemente el caso en que esas «otras especies» son iones acuosos en vez de gases.\n\n(e) Como se forman $\\mathrm{NH_3}$ y $\\mathrm{HCl}$ en proporción 1:1 a partir de un sólido puro, $p_{\\mathrm{NH_3}}=p_{\\mathrm{HCl}}=P_{total}/2=0{,}20/2=0{,}10$ atm. $K_p=p_{\\mathrm{NH_3}}\\,p_{\\mathrm{HCl}}=0{,}10\\times0{,}10=0{,}010\\,\\mathrm{atm^2}$. Con $T=340+273=613$ K: $RT=0{,}082\\times613=50{,}3\\,\\mathrm{atm\\,L\\,mol^{-1}}$. $K_c=\\dfrac{K_p}{(RT)^{\\Delta n}}=\\dfrac{0{,}010}{50{,}3^2}=3{,}9\\times10^{-6}\\,\\mathrm{mol^2\\,L^{-2}}$.",
        "mark_scheme": [
          "(a) 1 punto: escribe la expresión sin $\\mathrm{NH_4Cl(s)}$.",
          "(b) 1 punto: $K_p$ con presiones parciales, sin el sólido.",
          "(c) 1 punto: $\\Delta n$ contando solo los gases.",
          "(d) 1 punto: para la puntuación completa debes indicar que en ambos casos un sólido puro está en equilibrio con las especies que produce y que el sólido no aparece en la constante.",
          "(e) 2 puntos: 1 por obtener correctamente las presiones parciales a partir de la presión total, y 1 por el cálculo de $K_c$ a partir de $K_p$."
        ],
        "common_errors": [
          "En (a) y (b), incluir $\\mathrm{NH_4Cl(s)}$ en la expresión.",
          "En (c), olvidar filtrar el sólido antes de contar moles de gas.",
          "En (e), usar $P_{total}$ directamente como $p_{\\mathrm{NH_3}}$ o $p_{\\mathrm{HCl}}$ en vez de dividirla entre 2."
        ],'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
