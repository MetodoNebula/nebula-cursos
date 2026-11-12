# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'limites_continuidad.pdf' (Tema 11, Matemáticas I)
para bundles/eso_matematicas__mat_limites_continuidad.json"""
import math
from fractions import Fraction as F

L3 = "03_Cálculo_de_límites_e_indeterminaciones.json"
L4 = "04_Asíntotas_y_ramas_infinitas.json"

EX = {
L3: [
 {"id":"EX-8A03-P1","type":"STANDARD","objective_ids":["LO-8A03-2","LO-8A03-5"],
  "concept_ids":["C-8A03-02","C-8A03-01"],"difficulty":5,
  "statement":"Calcula $\\lim\\limits_{x\\to -1}\\dfrac{3x^{2}+x-2}{x^{3}+x^{2}-x-1}$. Si el límite no existe, explica por qué y da los límites laterales.",
  "hints":["Al sustituir sale $\\dfrac{0}{0}$: factoriza numerador y denominador. En el denominador agrupa: $x^{2}(x+1)-(x+1)$.",
           "Tras simplificar un factor $(x+1)$ quedará algo de la forma $\\dfrac{k}{0}$ con $k\\neq 0$: eso obliga a estudiar los laterales."],
  "answer":"El límite no existe: $\\lim\\limits_{x\\to -1^{-}}=-\\infty$ y $\\lim\\limits_{x\\to -1^{+}}=+\\infty$.",
  "full_solution":"Al sustituir $x=-1$ el numerador vale $3-1-2=0$ y el denominador $-1+1+1-1=0$: es la indeterminación $\\dfrac{0}{0}$, así que hay que factorizar. El numerador es $3x^{2}+x-2=(x+1)(3x-2)$ (sus raíces son $-1$ y $\\dfrac{2}{3}$). El denominador se factoriza agrupando: $x^{3}+x^{2}-x-1=x^{2}(x+1)-(x+1)=(x+1)(x^{2}-1)=(x+1)^{2}(x-1)$. Simplificando un factor $(x+1)$, el límite queda $\\lim\\limits_{x\\to -1}\\dfrac{3x-2}{(x+1)(x-1)}$. Ahora, al sustituir, el numerador tiende a $-5$ (distinto de cero) y el denominador a $0$: no es una indeterminación, sino un cociente de la forma $\\dfrac{-5}{0}$, que obliga a estudiar el signo del denominador por cada lado. Si $x\\to -1^{-}$ (por ejemplo $x=-1{,}01$), entonces $(x+1)<0$ y $(x-1)<0$, así que su producto es positivo y pequeño: $\\dfrac{-5}{0^{+}}=-\\infty$. Si $x\\to -1^{+}$ (por ejemplo $x=-0{,}99$), entonces $(x+1)>0$ y $(x-1)<0$, el producto es negativo y pequeño: $\\dfrac{-5}{0^{-}}=+\\infty$. Como los dos laterales son distintos, el límite no existe. Comprobación numérica: en $x=-1{,}001$ la función vale aproximadamente $-2500{,}2$, y en $x=-0{,}999$ aproximadamente $+2499{,}7$.",
  "common_errors":["Dar $0$ como resultado en cuanto aparece $\\dfrac{0}{0}$: esa forma no es un valor, solo indica que hay que transformar la expresión.",
                   "Tras simplificar, escribir que el límite es $\\infty$ sin signo ni estudio lateral: aquí los dos lados dan infinitos de signo distinto y el límite no existe."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-8A03-P2","type":"STANDARD","objective_ids":["LO-8A03-3","LO-8A03-5"],
  "concept_ids":["C-8A03-02"],"difficulty":5,
  "statement":"Calcula $\\lim\\limits_{x\\to 0}\\dfrac{\\sqrt{2x+4}-2}{\\sqrt{x+1}-1}$ racionalizando.",
  "hints":["Hay una raíz en el numerador y otra en el denominador: hay que multiplicar por los dos conjugados a la vez.",
           "Multiplica numerador y denominador por $\\left(\\sqrt{2x+4}+2\\right)\\left(\\sqrt{x+1}+1\\right)$."],
  "answer":"$1$",
  "full_solution":"Al sustituir $x=0$ se obtiene $\\dfrac{\\sqrt{4}-2}{\\sqrt{1}-1}=\\dfrac{0}{0}$, indeterminación. Como hay raíces arriba y abajo, se multiplica numerador y denominador por los dos conjugados: $\\left(\\sqrt{2x+4}+2\\right)$ y $\\left(\\sqrt{x+1}+1\\right)$. El numerador se convierte en $\\left(\\sqrt{2x+4}-2\\right)\\left(\\sqrt{2x+4}+2\\right)=(2x+4)-4=2x$, y el denominador en $\\left(\\sqrt{x+1}-1\\right)\\left(\\sqrt{x+1}+1\\right)=(x+1)-1=x$. Pero hay que arrastrar los factores que se han introducido en el otro lado, de modo que la expresión queda $\\dfrac{2x\\left(\\sqrt{x+1}+1\\right)}{x\\left(\\sqrt{2x+4}+2\\right)}$. Ahora sí se puede simplificar la $x$ (que es lo que causaba la indeterminación): $\\dfrac{2\\left(\\sqrt{x+1}+1\\right)}{\\sqrt{2x+4}+2}$. Sustituyendo $x=0$: $\\dfrac{2(1+1)}{2+2}=\\dfrac{4}{4}=1$. Comprobación numérica: para $x=0{,}001$ la expresión original vale aproximadamente $1{,}000125$, muy cerca de $1$.",
  "common_errors":["Racionalizar solo el numerador: queda $\\dfrac{2x}{\\left(\\sqrt{x+1}-1\\right)\\left(\\sqrt{2x+4}+2\\right)}$, que sigue siendo $\\dfrac{0}{0}$; hay que eliminar las dos raíces.",
                   "Escribir $\\sqrt{2x+4}=\\sqrt{2x}+2$: la raíz no se reparte sobre una suma."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-8A03-P3","type":"REASONING","objective_ids":["LO-8A03-2","LO-8A03-5"],
  "concept_ids":["C-8A03-02","C-8A03-01"],"difficulty":5,
  "statement":"Calcula $\\lim\\limits_{x\\to 2}\\dfrac{2x^{2}-x-10}{x^{3}-3x^{2}+4}$ y compáralo con el límite del ejercicio anterior en $x=-1$. En uno de los dos casos el límite no existe y en el otro vale $-\\infty$: explica qué detalle de la factorización marca la diferencia.",
  "hints":["Factoriza: $2x^{2}-x-10=(2x-5)(x+2)$ y $x^{3}-3x^{2}+4=(x+1)(x-2)^{2}$.",
           "Fíjate en si el factor que anula el denominador aparece elevado a una potencia par o impar."],
  "answer":"$\\lim\\limits_{x\\to 2}\\dfrac{2x^{2}-x-10}{x^{3}-3x^{2}+4}=-\\infty$ (los dos laterales coinciden). La diferencia está en la paridad del exponente del factor que anula el denominador: $(x-2)^{2}$ no cambia de signo, mientras que $(x+1)^{1}$ sí.",
  "full_solution":"Al sustituir $x=2$: el numerador vale $8-2-10=-4$ y el denominador $8-12+4=0$. No es $\\dfrac{0}{0}$, sino $\\dfrac{-4}{0}$, así que hay que estudiar el signo del denominador. Para verlo se factoriza: $2x^{2}-x-10=(2x-5)(x+2)$, y $x^{3}-3x^{2}+4=(x+1)(x-2)^{2}$ (se encuentra la raíz $x=-1$ y se aplica Ruffini, quedando $x^{2}-4x+4=(x-2)^{2}$). La función es, por tanto, $\\dfrac{(2x-5)(x+2)}{(x+1)(x-2)^{2}}$. Cerca de $x=2$, el numerador tiende a $(-1)\\cdot 4=-4$, el factor $(x+1)$ tiende a $3>0$ y el factor $(x-2)^{2}$ tiende a $0$ siendo SIEMPRE positivo, porque es un cuadrado. Así que el denominador tiende a $0^{+}$ por los dos lados y el cociente tiende a $\\dfrac{-4}{0^{+}}=-\\infty$ tanto por la izquierda como por la derecha: el límite existe y vale $-\\infty$. En el caso anterior, en cambio, el denominador contenía el factor $(x+1)$ con exponente $1$, que es negativo a la izquierda de $-1$ y positivo a la derecha; por eso los dos laterales salían con signos opuestos y el límite no existía. La regla práctica: si el factor que anula el denominador tiene exponente par, el signo no cambia y los dos laterales coinciden; si lo tiene impar, el signo cambia y hay que comprobar si el límite existe. Comprobación numérica: en $x=1{,}999$ la función vale aproximadamente $-1\\,336\\,111$ y en $x=2{,}001$ aproximadamente $-1\\,330\\,556$: negativa y enorme por los dos lados.",
  "common_errors":["Afirmar que, siempre que el denominador se anula, el límite no existe: con un factor de exponente par los dos laterales pueden coincidir y el límite es $+\\infty$ o $-\\infty$.",
                   "Dar la respuesta como $\\infty$ sin signo: el signo lo determina el del numerador combinado con el del denominador."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-8A03-P4","type":"STANDARD","objective_ids":["LO-8A03-5","LO-8A03-2"],
  "concept_ids":["C-8A03-02"],"difficulty":5,
  "statement":"Calcula $\\lim\\limits_{x\\to 2}\\left(\\dfrac{3x-2}{x^{2}-2x+4}\\right)^{\\frac{x}{x-2}}$. Comprueba primero que se trata de la indeterminación $1^{\\infty}$.",
  "hints":["Sustituye $x=2$ en la base y en el exponente antes de nada.",
           "Para $1^{\\infty}$ se usa $\\lim f^{g}=e^{\\lim (f-1)\\cdot g}$; calcula $f(x)-1$ con denominador común y simplifica el factor $(x-2)$."],
  "answer":"$e^{1/2}=\\sqrt{e}\\approx 1{,}6487$",
  "full_solution":"Primero se identifica la indeterminación. Al sustituir $x=2$, la base vale $\\dfrac{3\\cdot 2-2}{4-4+4}=\\dfrac{4}{4}=1$ y el exponente $\\dfrac{2}{0}$ tiende a infinito: es la forma $1^{\\infty}$, que es indeterminada. Se aplica la fórmula $\\lim f(x)^{g(x)}=e^{L}$ con $L=\\lim\\left(f(x)-1\\right)g(x)$. Se calcula $f(x)-1=\\dfrac{3x-2}{x^{2}-2x+4}-1=\\dfrac{3x-2-\\left(x^{2}-2x+4\\right)}{x^{2}-2x+4}=\\dfrac{-x^{2}+5x-6}{x^{2}-2x+4}$. El numerador se factoriza: $-x^{2}+5x-6=-\\left(x^{2}-5x+6\\right)=-(x-2)(x-3)$. Por tanto $\\left(f(x)-1\\right)g(x)=\\dfrac{-(x-2)(x-3)}{x^{2}-2x+4}\\cdot\\dfrac{x}{x-2}=\\dfrac{-x(x-3)}{x^{2}-2x+4}$, donde ya se ha simplificado el factor $(x-2)$ que producía la indeterminación. Sustituyendo $x=2$: $L=\\dfrac{-2\\cdot(-1)}{4}=\\dfrac{2}{4}=\\dfrac{1}{2}$. El límite es, pues, $e^{1/2}=\\sqrt{e}\\approx 1{,}6487$. Comprobación numérica: para $x=2{,}001$ la expresión vale aproximadamente $1{,}6478$.",
  "common_errors":["Concluir que el límite es $1$ porque la base tiende a $1$: $1^{\\infty}$ es una forma indeterminada, no vale $1$.",
                   "Olvidar el $-1$ de la fórmula y calcular $e^{\\lim f\\cdot g}$ en lugar de $e^{\\lim (f-1)g}$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-8A03-P5","type":"STANDARD","objective_ids":["LO-8A03-4","LO-8A03-5"],
  "concept_ids":["C-8A03-03","C-8A03-02"],"difficulty":4,
  "statement":"Calcula $\\lim\\limits_{x\\to +\\infty}\\left(\\dfrac{2x+3}{2x-1}\\right)^{x}$.",
  "hints":["Comprueba a qué tiende la base cuando $x\\to +\\infty$: numerador y denominador tienen el mismo grado.",
           "De nuevo es $1^{\\infty}$: usa $e^{\\lim (f-1)\\cdot g}$ y recuerda que $\\lim\\limits_{x\\to+\\infty}\\dfrac{4x}{2x-1}=2$."],
  "answer":"$e^{2}\\approx 7{,}389$",
  "full_solution":"La base es un cociente de polinomios del mismo grado, así que tiende al cociente de los coeficientes principales: $\\dfrac{2}{2}=1$. El exponente tiende a $+\\infty$, de modo que la forma es $1^{\\infty}$, indeterminada. Se aplica $\\lim f^{g}=e^{L}$ con $L=\\lim\\left(f-1\\right)g$. Se calcula $f(x)-1=\\dfrac{2x+3}{2x-1}-1=\\dfrac{(2x+3)-(2x-1)}{2x-1}=\\dfrac{4}{2x-1}$. Entonces $\\left(f(x)-1\\right)g(x)=\\dfrac{4}{2x-1}\\cdot x=\\dfrac{4x}{2x-1}$, cuyo límite cuando $x\\to +\\infty$ es $\\dfrac{4}{2}=2$ (mismo grado arriba y abajo). Por tanto el límite buscado es $e^{2}\\approx 7{,}389$. Comprobación numérica: para $x=1000$ la expresión vale aproximadamente $7{,}3817$, y para $x=100\\,000$ aproximadamente $7{,}38898$, acercándose a $e^{2}$.",
  "common_errors":["Decir que el límite es $1$ porque la base tiende a $1$, o que es $+\\infty$ porque el exponente tiende a infinito: ninguna de las dos lecturas vale en una indeterminación $1^{\\infty}$.",
                   "Calcular $f-1$ restando solo los términos independientes y obtener $\\dfrac{3+1}{2x-1}$ por casualidad bien, pero fallar en otros casos: hay que restar el denominador completo."],
  "provenance":"SOURCE_DERIVED"},
],

L4: [
 {"id":"EX-8A04-P1","type":"REASONING","objective_ids":["LO-8A04-1","LO-8A04-3"],
  "concept_ids":["C-8A04-01","C-8A04-04"],"difficulty":5,
  "statement":"Halla las asíntotas verticales de $f(x)=\\dfrac{2x+1}{x^{2}-1}$ y de $g(x)=\\dfrac{1}{x^{2}-2x+1}$, y estudia en cada caso la posición de la curva respecto a ellas calculando los límites laterales. ¿Por qué en una de las dos funciones la curva se va hacia el mismo lado por la izquierda y por la derecha?",
  "hints":["Factoriza los denominadores: $x^{2}-1=(x-1)(x+1)$ y $x^{2}-2x+1=(x-1)^{2}$.",
           "Para cada lateral, mira el signo del numerador y el de cada factor del denominador."],
  "answer":"$f$: asíntotas $x=-1$ y $x=1$, con $\\lim_{x\\to-1^{-}}f=-\\infty$, $\\lim_{x\\to-1^{+}}f=+\\infty$, $\\lim_{x\\to1^{-}}f=-\\infty$, $\\lim_{x\\to1^{+}}f=+\\infty$. $g$: única asíntota $x=1$, con $+\\infty$ por los dos lados, porque $(x-1)^{2}$ es siempre positivo.",
  "full_solution":"Para $f$ se anula el denominador en $x^{2}-1=0$, es decir, $x=-1$ y $x=1$, y en ninguno de los dos se anula el numerador ($2x+1$ vale $-1$ y $3$), así que las dos son asíntotas verticales. Escribiendo $f(x)=\\dfrac{2x+1}{(x-1)(x+1)}$ se estudian los laterales. En $x\\to -1^{-}$: el numerador tiende a $-1$, $(x-1)$ es negativo y $(x+1)$ es negativo y pequeño, luego el denominador es $0^{+}$ y $f\\to\\dfrac{-1}{0^{+}}=-\\infty$. En $x\\to -1^{+}$: $(x+1)$ pasa a ser positivo, el denominador es $0^{-}$ y $f\\to +\\infty$. En $x\\to 1^{-}$: el numerador tiende a $3$, $(x+1)$ es positivo y $(x-1)$ negativo y pequeño, luego el denominador es $0^{-}$ y $f\\to -\\infty$. En $x\\to 1^{+}$: el denominador es $0^{+}$ y $f\\to +\\infty$. Para $g$, el denominador es $x^{2}-2x+1=(x-1)^{2}$, que se anula solo en $x=1$: hay una única asíntota vertical. Y como $(x-1)^{2}$ es un cuadrado, es positivo a los dos lados de $1$, así que $g(x)=\\dfrac{1}{(x-1)^{2}}\\to\\dfrac{1}{0^{+}}=+\\infty$ tanto por la izquierda como por la derecha: la curva sube por los dos lados. Esa es la diferencia: cuando el factor que anula el denominador está elevado a una potencia par, no cambia de signo al cruzar el punto, y las dos ramas van en la misma dirección. Comprobación: $g(0{,}99)=g(1{,}01)=10\\,000$ exactamente, por simetría.",
  "common_errors":["Dar $x=1$ y $x=-1$ como asíntotas de $g$ confundiendo $x^{2}-2x+1$ con $x^{2}-1$: el primero es un cuadrado perfecto y solo tiene la raíz $x=1$.",
                   "Suponer que en toda asíntota vertical una rama sube y la otra baja: eso ocurre con exponente impar, no con exponente par."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    rats = [F(k, 7) for k in range(-60, 61)]
    # ---------- L03 P1
    num = lambda x: 3*x*x + x - 2
    den = lambda x: x**3 + x*x - x - 1
    for x in rats:
        assert num(x) == (x+1)*(3*x-2)
        assert den(x) == (x+1)**2*(x-1)
    assert num(F(-1)) == 0 and den(F(-1)) == 0
    assert num(F(2, 3)) == 0
    assert 3*(-1)-2 == -5
    f1 = lambda x: (3*x*x + x - 2)/(x**3 + x*x - x - 1)
    a, b = f1(-1.001), f1(-0.999)
    assert a < -2000 and b > 2000, (a, b)
    assert round(a) == -2500, a
    assert round(b) == 2500, b
    for t in (1e-3, 1e-4, 1e-5):
        assert f1(-1 - t) < 0 and f1(-1 + t) > 0
        assert abs(f1(-1 - t)) > 1/t and abs(f1(-1 + t)) > 1/t
    # ---------- L03 P2
    f2 = lambda x: (math.sqrt(2*x+4) - 2)/(math.sqrt(x+1) - 1)
    assert round(f2(0.001), 6) == 1.000125, f2(0.001)
    for t in (1e-2, 1e-4, 1e-6):
        assert ic(f2(t), 1.0, abs_tol=5e-2*t**0 if t > 1e-3 else 1e-4)
    assert ic(f2(1e-8), 1.0, abs_tol=1e-6)
    g2 = lambda x: (2*(math.sqrt(x+1)+1))/(math.sqrt(2*x+4)+2)
    for t in (0.5, 0.1, 1e-3):
        assert ic(f2(t), g2(t), rel_tol=1e-9)
    assert ic(g2(0), 1.0)
    # ---------- L03 P3
    n3 = lambda x: 2*x*x - x - 10
    d3 = lambda x: x**3 - 3*x*x + 4
    for x in rats:
        assert n3(x) == (2*x-5)*(x+2)
        assert d3(x) == (x+1)*(x-2)**2
    assert n3(F(2)) == -4 and d3(F(2)) == 0
    assert 8 - 2 - 10 == -4 and 8 - 12 + 4 == 0
    f3 = lambda x: n3(x)/d3(x)
    l, r = f3(1.999), f3(2.001)
    assert l < 0 and r < 0
    assert round(l) == -1336111, l
    assert round(r) == -1330556, r
    for t in (1e-3, 1e-4, 1e-5):
        assert f3(2-t) < 0 and f3(2+t) < 0
    assert (2*2-5)*(2+2) == -4 and (2+1) == 3
    # ---------- L03 P4
    base = lambda x: (3*x-2)/(x*x - 2*x + 4)
    expo = lambda x: x/(x-2)
    assert ic(base(2), 1.0)
    f4 = lambda x: base(x)**expo(x)
    assert round(f4(2.001), 4) == 1.6478, f4(2.001)
    assert ic(f4(2.000001), math.sqrt(math.e), rel_tol=1e-5)
    assert ic(f4(1.999999), math.sqrt(math.e), rel_tol=1e-5)
    assert round(math.sqrt(math.e), 4) == 1.6487
    for x in rats:
        if x == 2: continue
        assert base(x) - 1 == (-x*x + 5*x - 6)/(x*x - 2*x + 4)
        assert -x*x + 5*x - 6 == -(x-2)*(x-3)
        assert (base(x)-1)*expo(x) == (-x*(x-3))/(x*x - 2*x + 4)
    assert F(-2*(2-3), 4) == F(1, 2)
    # ---------- L03 P5
    f5 = lambda x: ((2*x+3)/(2*x-1))**x
    assert round(f5(1000), 4) == 7.3817, f5(1000)
    assert round(f5(100000), 5) == 7.38898, f5(100000)
    assert round(math.e**2, 3) == 7.389
    for x in rats:
        if x == F(1, 2): continue
        assert F(2*x+3, 2*x-1) - 1 == F(4, 2*x-1)
        assert (F(2*x+3, 2*x-1) - 1)*x == F(4*x, 2*x-1)
    assert ic(f5(1e7), math.e**2, rel_tol=1e-6)
    # ---------- L04 P1
    ff = lambda x: (2*x+1)/(x*x-1)
    for x in rats:
        if x in (F(1), F(-1)): continue
        assert ff(x) == F(2*x+1, (x-1)*(x+1))
    assert 2*(-1)+1 == -1 and 2*1+1 == 3
    for t in (1e-2, 1e-4, 1e-6):
        assert ff(-1-t) < 0 and abs(ff(-1-t)) > 1/(3*t)
        assert ff(-1+t) > 0 and abs(ff(-1+t)) > 1/(3*t)
        assert ff(1-t) < 0 and abs(ff(1-t)) > 1/(3*t)
        assert ff(1+t) > 0 and abs(ff(1+t)) > 1/(3*t)
    gg = lambda x: 1/(x*x - 2*x + 1)
    for x in rats:
        if x == 1: continue
        assert gg(x) == F(1, (x-1)**2) and gg(x) > 0
    assert gg(F(99, 100)) == 10000 == gg(F(101, 100))
    for t in (1e-2, 1e-4):
        assert gg(1-t) > 0 and gg(1+t) > 0 and ic(gg(1-t), gg(1+t), rel_tol=1e-5)
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
