# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''El cociente $P_i'/P_i=\\dfrac{n_{total,gas,inicial}}{n_{total,gas,inicial}+n_{inerte}}$, un factor menor que 1 que diluye por igual todas las presiones parciales reactivas. Sustituyendo en Q, se obtiene $Q_{nuevo}=K\\cdot\\phi^{\\Delta n}=K\\cdot f^{-\\Delta n}$, la misma forma funcional que la hallada en el reto de la lección anterior para una expansión de volumen por un factor f, confirmando que el gas inerte a P constante es formalmente una expansión encubierta.",'''

new = r'''El cociente $P_i'/P_i=\\dfrac{n_{total,gas,inicial}}{n_{total,gas,inicial}+n_{inerte}}=\\phi$, un factor menor que 1 que diluye por igual todas las presiones parciales reactivas, es decir, $P_i'=\\phi P_i$ para cada especie. Sustituyendo en $Q$: $Q_{nuevo}=\\dfrac{(\\phi P_C)^c(\\phi P_D)^d}{(\\phi P_A)^a(\\phi P_B)^b}=\\dfrac{P_C^cP_D^d}{P_A^aP_B^b}\\cdot\\phi^{(c+d)-(a+b)}=K\\phi^{\\Delta n}$. Por otro lado, por $PV=nRT$ a $P$ y $T$ constantes, el volumen es proporcional a los moles totales, así que $V'/V=\\dfrac{n_{tot}+n_{inerte}}{n_{tot}}=1/\\phi=f$: el factor de expansión real del volumen es precisamente $f=1/\\phi$. Sustituyendo: $Q_{nuevo}=K\\phi^{\\Delta n}=K\\left(\\dfrac{1}{f}\\right)^{\\Delta n}=K\\cdot f^{-\\Delta n}$, la misma forma funcional que la hallada en el reto de la lección anterior para una expansión de volumen por un factor f, confirmando que el gas inerte a P constante es formalmente una expansión encubierta.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
