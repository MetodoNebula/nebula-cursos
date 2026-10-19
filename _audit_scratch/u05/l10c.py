import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []
edits.append(("H4_theory0_body",
"En la lección anterior se vio que, para $\\text{A}\\rightleftharpoons\\text{B}$, en el equilibrio $[\\text{B}]_{\\text{eq}}/[\\text{A}]_{\\text{eq}}=k_+/k_-$, un cociente constante a una temperatura dada. Para una reacción general con varios reactivos y productos, y con coeficientes estequiométricos distintos de 1, existe un cociente análogo, llamado **constante de equilibrio Kc**, que generaliza esa misma idea.",
"En la lección anterior se vio que, para $\\text{A}\\rightleftharpoons\\text{B}$ **elemental**, en el equilibrio $[\\text{B}]_{\\text{eq}}/[\\text{A}]_{\\text{eq}}=k_+/k_-$, un cociente constante a una temperatura dada. Para una reacción general con varios reactivos y productos, y con coeficientes estequiométricos distintos de 1, existe un cociente análogo, llamado **constante de equilibrio Kc**, que generaliza esa misma idea: para una reacción cualquiera (elemental o no), Kc se escribe siempre con los coeficientes de la ecuación ajustada, aunque su justificación general ya no es la igualdad de velocidades elementales, sino un argumento termodinámico."
))

ok = apply(edits)
print("DONE", ok)
