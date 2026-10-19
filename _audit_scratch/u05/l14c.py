# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''el factor de dilución se cancela exactamente entre numerador y denominador.\n\nIgual que con la concentración, $K_p$ (o $K_c$) no cambia por comprimir o expandir: solo cambia la posición del equilibrio.",'''

new = r'''el factor de dilución se cancela exactamente entre numerador y denominador.\n\nIgual que con la concentración, $K_p$ (o $K_c$) no cambia por comprimir o expandir: solo cambia la posición del equilibrio.\n\n¿Por qué ocurre esto? Si el volumen pasa a $V/2$ (se comprime a la mitad) a $T$ y moles constantes, cada presión parcial se duplica, así que $Q_p$ pasa a valer $K_p\\cdot2^{\\Delta n}$ justo después del cambio. Si $\\Delta n>0$ (más moles de gas en productos), $2^{\\Delta n}>1$ y $Q_p>K_p$: el sistema avanza hacia reactivos, el lado con menos moles de gas. Si $\\Delta n<0$, ocurre lo contrario y avanza hacia productos. (El reto final de esta lección demuestra esta relación en general, para cualquier factor $f$.)\n\nOjo: esta regla se refiere a cambiar el volumen del recipiente. Añadir un gas inerte a volumen constante también sube la presión total, pero no desplaza el equilibrio, porque no cambia ninguna presión parcial ni ninguna concentración (se verá en la siguiente lección).",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
