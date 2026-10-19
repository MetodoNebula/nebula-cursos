import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("REF_prereq0",
"Conocer el equilibrio dinámico y la relación $[\\text{B}]_{\\text{eq}}/[\\text{A}]_{\\text{eq}}=k_+/k_-$ para la reacción sencilla $\\text{A}\\rightleftharpoons\\text{B}$ (lección el apartado correspondiente).",
"Conocer el equilibrio dinámico y la relación $[\\text{B}]_{\\text{eq}}/[\\text{A}]_{\\text{eq}}=k_+/k_-$ para la reacción sencilla $\\text{A}\\rightleftharpoons\\text{B}$ (lección 9: Equilibrio químico dinámico)."
))
edits.append(("REF_prereq1",
"Deducir unidades a partir de un orden total y operar con potencias de exponente entero, incluido el exponente 0 (lección el apartado correspondiente).",
"Deducir unidades a partir de un orden total y operar con potencias de exponente entero, incluido el exponente 0 (lección 6: Unidades de la constante de velocidad k)."
))
edits.append(("REF_diag1_cwa0",
"Confunde el exponente 0 con un valor nulo, un error que se repite de el apartado correspondiente y que aquí afecta a cómo se simplifica Kc cuando Δn=0.",
"Confunde el exponente 0 con un valor nulo, un error que se repite de la lección 6 (Unidades de la constante de velocidad k) y que aquí afecta a cómo se simplifica Kc cuando Δn=0."
))
edits.append(("REF_fc2_back",
"Kc: siempre los coeficientes estequiométricos (propiedad del equilibrio). Ley de velocidad: órdenes experimentales, que solo coinciden con los coeficientes si la reacción es elemental (el apartado correspondiente).",
"Kc: siempre los coeficientes estequiométricos (propiedad del equilibrio). Ley de velocidad: órdenes experimentales, que solo coinciden con los coeficientes si la reacción es elemental (lección 4: Ley de velocidad)."
))
edits.append(("REF_fc10_back",
"Es la generalización del cociente $k_+/k_-$ (lección el apartado correspondiente, para A⇌B) a una reacción con varios reactivos y productos y coeficientes estequiométricos distintos de 1.",
"Es la generalización del cociente $k_+/k_-$ (lección 9: Equilibrio químico dinámico, para A⇌B) a una reacción con varios reactivos y productos y coeficientes estequiométricos distintos de 1."
))
edits.append(("REF_misc0_why",
"Se traslada directamente la estructura de la ley de velocidad (donde los exponentes son experimentales, el apartado correspondiente/el apartado correspondiente) a la expresión de Kc, sin darse cuenta de que son conceptos distintos con reglas distintas.",
"Se traslada directamente la estructura de la ley de velocidad (donde los exponentes son experimentales, lección 4: Ley de velocidad) a la expresión de Kc, sin darse cuenta de que son conceptos distintos con reglas distintas."
))
edits.append(("REF_misc0_correct",
"Los exponentes de la expresión de Kc son, siempre y sin excepción, los **coeficientes estequiométricos** de la ecuación ajustada (a diferencia de los órdenes de la ley de velocidad, que son experimentales y pueden no coincidir con ellos, como se vio en el apartado correspondiente). Para escribir Kc no se necesita ningún dato experimental de cinética: basta con la ecuación ajustada.",
"Los exponentes de la expresión de Kc son, siempre y sin excepción, los **coeficientes estequiométricos** de la ecuación ajustada (a diferencia de los órdenes de la ley de velocidad, que son experimentales y pueden no coincidir con ellos, como se vio en la lección 4, Ley de velocidad). Para escribir Kc no se necesita ningún dato experimental de cinética: basta con la ecuación ajustada."
))
edits.append(("REF_misc1_why",
"Se repite, para Kc, la misma confusión que con las unidades de k (el apartado correspondiente): asociar 'constante' con 'unidades fijas'.",
"Se repite, para Kc, la misma confusión que con las unidades de k (lección 6: Unidades de la constante de velocidad k): asociar 'constante' con 'unidades fijas'."
))
edits.append(("REF_cm0_why",
"Se traslada la estructura de la ley de velocidad (el apartado correspondiente/el apartado correspondiente), donde los exponentes son experimentales, a la expresión de Kc, que tiene una regla distinta.",
"Se traslada la estructura de la ley de velocidad (lección 4: Ley de velocidad), donde los exponentes son experimentales, a la expresión de Kc, que tiene una regla distinta."
))
edits.append(("REF_cm1_why",
"Se repite, para Kc, la misma confusión que con las unidades de k (el apartado correspondiente).",
"Se repite, para Kc, la misma confusión que con las unidades de k (lección 6: Unidades de la constante de velocidad k)."
))

# Fallos de renderizado
edits.append(("RENDER_misc0_incorrect",
"«Los exponentes de la expresión de Kc son los órdenes de la ley de velocidad, igual que en la ley de velocidad v=k[A]^m[B]^n.»",
"«Los exponentes de la expresión de Kc son los órdenes de la ley de velocidad, igual que en la ley de velocidad $v=k[\\text{A}]^m[\\text{B}]^n$.»"
))
edits.append(("RENDER_summary_wtr",
"invertir la ecuación da 1/Kc, multiplicar los coeficientes por n da Kc^n, y sumar dos ecuaciones da el producto de sus constantes.",
"invertir la ecuación da $1/K_c$, multiplicar los coeficientes por $n$ da $K_c^{\\,n}$, y sumar dos ecuaciones da el producto de sus constantes."
))

ok = apply(edits)
print("DONE", ok)
