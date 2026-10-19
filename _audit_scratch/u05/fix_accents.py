PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old_title = "Moles totales, fracciones molares y Kp en funcion de alfa y P_T"
new_title = "Moles totales, fracciones molares y Kp en función de alfa y P_T"
n1 = data.count(old_title)
print("title count:", n1)

old_body_frag = "conviene expresar tambien los moles totales en el equilibrio y, a partir de ellos, Kp directamente en funcion de alfa y de la presion total P_T, sin pasar por Kc."
new_body_frag = "conviene expresar también los moles totales en el equilibrio y, a partir de ellos, Kp directamente en función de alfa y de la presión total P_T, sin pasar por Kc."
n2 = data.count(old_body_frag)
print("body frag count:", n2)

old_frag2 = "Ejemplo numerico: para"
new_frag2 = "Ejemplo numérico: para"
n3 = data.count(old_frag2)
print("frag2 count:", n3)

old_frag3 = "Esta relacion tambien permite el camino inverso: si se mide experimentalmente la presion total final"
new_frag3 = "Esta relación también permite el camino inverso: si se mide experimentalmente la presión total final"
n4 = data.count(old_frag3)
print("frag3 count:", n4)

old_frag4 = "constantes que partia de una presion inicial"
new_frag4 = "constantes que partía de una presión inicial"
n5 = data.count(old_frag4)
print("frag4 count:", n5)

if n1==1 and n2==1 and n3==1 and n4==1 and n5==1:
    data = data.replace(old_title, new_title, 1)
    data = data.replace(old_body_frag, new_body_frag, 1)
    data = data.replace(old_frag2, new_frag2, 1)
    data = data.replace(old_frag3, new_frag3, 1)
    data = data.replace(old_frag4, new_frag4, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
