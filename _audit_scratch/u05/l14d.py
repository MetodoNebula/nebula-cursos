# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"body": "Si se añade un reactivo (o se retira un producto), su concentración en el denominador —o numerador— de $Q$ cambia bruscamente, de modo que $Q$ deja de coincidir con $K_c$. En concreto:\n\n- **Añadir reactivo** (o quitar producto): $Q$ baja por debajo de $K_c$ ⟹ el sistema avanza hacia productos.\n- **Añadir producto** (o quitar reactivo): $Q$ sube por encima de $K_c$ ⟹ el sistema avanza hacia reactivos.\n\nEn ambos casos, una vez alcanzado el nuevo equilibrio, $K_c$ sigue valiendo exactamente lo mismo: lo único que cambió fueron las concentraciones de equilibrio, no la constante.",'''

new = r'''"body": "Si se añade un reactivo (o se retira un producto), su concentración en el denominador —o numerador— de $Q$ cambia bruscamente, de modo que $Q$ deja de coincidir con $K_c$. En concreto:\n\n- **Añadir reactivo** (o quitar producto): $Q$ baja por debajo de $K_c$ ⟹ el sistema avanza hacia productos.\n- **Añadir producto** (o quitar reactivo): $Q$ sube por encima de $K_c$ ⟹ el sistema avanza hacia reactivos.\n- **Añadir o quitar un sólido o líquido puro** (p. ej. $CaCO_3(s)$ en $CaCO_3(s)\\rightleftharpoons CaO(s)+CO_2(g)$) no desplaza el equilibrio en absoluto: los sólidos y líquidos puros no figuran en la expresión de $Q$ ni de $K_c$.\n- **La oposición es solo parcial**: en el nuevo equilibrio, la especie que se añadió sigue estando en mayor concentración que antes de añadirla (nunca vuelve del todo al valor inicial); ver el ejemplo numérico de esta lección.\n\nEn todos los casos (salvo sólidos y líquidos puros), una vez alcanzado el nuevo equilibrio, $K_c$ sigue valiendo exactamente lo mismo: lo único que cambió fueron las concentraciones de equilibrio, no la constante.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
