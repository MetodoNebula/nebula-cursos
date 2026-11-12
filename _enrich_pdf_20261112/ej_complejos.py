# -*- coding: utf-8 -*-
"""Ejercicios derivados de '7_complejos.pdf' (64 ejercicios de números complejos)
para bundles/eso_matematicas__mat_complejos.json"""
import math
from fractions import Fraction as F

L1 = "01_Necesidad_de_los_complejos_y_unidad_imaginaria.json"
L2 = "02_Forma_binómica_y_operaciones.json"

EX = {
L1: [
 {"id":"EX-02B01-P1","type":"STANDARD","objective_ids":["LO-02B01-3"],
  "concept_ids":["C-02B-02"],"difficulty":4,
  "statement":"Calcula, usando la periodicidad de las potencias de la unidad imaginaria: a) $i^{723}$; b) $i^{6254}$; c) $i^{-17}$; d) $i^{-527}$.",
  "hints":["Las potencias de $i$ se repiten con periodo $4$: $i^{1}=i$, $i^{2}=-1$, $i^{3}=-i$, $i^{4}=1$.",
           "Para un exponente negativo, usa $i^{-n}=\\dfrac{1}{i^{n}}$, o bien suma un múltiplo de $4$ al exponente hasta hacerlo positivo."],
  "answer":"a) $-i$. b) $-1$. c) $-i$. d) $i$.",
  "full_solution":"Las potencias de $i$ forman un ciclo de longitud $4$, así que basta mirar el resto de dividir el exponente entre $4$: resto $0\\to 1$, resto $1\\to i$, resto $2\\to -1$, resto $3\\to -i$. a) $723=4\\cdot 180+3$, resto $3$, luego $i^{723}=-i$. b) $6254=4\\cdot 1563+2$, resto $2$, luego $i^{6254}=-1$. c) Para los exponentes negativos conviene sumar múltiplos de $4$ hasta llegar a un exponente positivo, porque $i^{4}=1$ y multiplicar por $1$ no cambia nada: $i^{-17}=i^{-17+20}=i^{3}=-i$. (También puede verse así: $i^{-17}=\\dfrac{1}{i^{17}}=\\dfrac{1}{i}$, y $\\dfrac{1}{i}=\\dfrac{i}{i^{2}}=\\dfrac{i}{-1}=-i$.) d) $i^{-527}=i^{-527+528}=i^{1}=i$, ya que $528=4\\cdot 132$. Comprobación del criterio en los negativos: el resto de $-17$ al dividir entre $4$ es $3$ (porque $-17=4\\cdot(-5)+3$) y el de $-527$ es $1$ (porque $-527=4\\cdot(-132)+1$), lo que coincide con los resultados obtenidos.",
  "common_errors":["Multiplicar la base por el exponente, como en $i^{723}=723i$: el exponente indica cuántas veces se multiplica $i$ por sí misma.",
                   "Tratar el exponente negativo cambiando el signo del resultado ($i^{-17}=-i^{17}$ por casualidad acierta aquí, pero $i^{-2}=-1$ y $-i^{2}=+1$ no coinciden): hay que pasar por $i^{-n}=\\dfrac{1}{i^{n}}$ o sumar múltiplos de $4$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02B01-P2","type":"STANDARD","objective_ids":["LO-02B01-1"],
  "concept_ids":["C-02B-01","C-02B-02"],"difficulty":5,
  "statement":"Resuelve en $\\mathbb{C}$ la ecuación $x^{4}-3x^{3}-2x^{2}+10x-12=0$, buscando primero las raíces enteras con Ruffini.",
  "hints":["Prueba divisores de $12$: $x=-2$ y $x=3$ son raíces.",
           "Tras dos pasos de Ruffini queda una ecuación de segundo grado con discriminante negativo."],
  "answer":"$x=-2$, $x=3$, $x=1+i$ y $x=1-i$.",
  "full_solution":"Los candidatos a raíz entera son los divisores de $12$. Probando $x=-2$: $16+24-8-20-12=0$, es raíz. Ruffini con $-2$ sobre los coeficientes $1,\\,-3,\\,-2,\\,10,\\,-12$ da el cociente $x^{3}-5x^{2}+8x-6$ y resto $0$. Se busca otra raíz entre los divisores de $6$; probando $x=3$: $27-45+24-6=0$, también es raíz. Ruffini con $3$ sobre $1,\\,-5,\\,8,\\,-6$ da el cociente $x^{2}-2x+2$ y resto $0$. Queda por resolver $x^{2}-2x+2=0$: el discriminante es $4-8=-4$, negativo, así que no hay raíces reales, pero sí complejas: $x=\\dfrac{2\\pm\\sqrt{-4}}{2}=\\dfrac{2\\pm 2i}{2}=1\\pm i$. Las cuatro soluciones son, por tanto, $-2$, $3$, $1+i$ y $1-i$. Comprobación de una de las complejas: si $x=1+i$, entonces $x^{2}=(1+i)^{2}=1+2i+i^{2}=2i$, y $x^{2}-2x+2=2i-2(1+i)+2=2i-2-2i+2=0$, correcto. Observa que las dos raíces complejas son conjugadas: eso siempre ocurre cuando el polinomio tiene coeficientes reales.",
  "common_errors":["Dar por terminada la ecuación con las dos raíces enteras: un polinomio de grado $4$ tiene cuatro raíces en $\\mathbb{C}$ contando multiplicidades.",
                   "Escribir $\\sqrt{-4}=-2$: la raíz de un número negativo es imaginaria, $\\sqrt{-4}=2i$."],
  "provenance":"SOURCE_DERIVED"},
],

L2: [
 {"id":"EX-02B02-P1","type":"REASONING","objective_ids":["LO-02B02-2","LO-02B02-1"],
  "concept_ids":["C-02B-03"],"difficulty":5,
  "statement":"Halla todos los pares de números reales $a$ y $b$ que cumplen $(a+i)(b-3i)=7-11i$.",
  "hints":["Desarrolla el producto y agrupa parte real y parte imaginaria; dos complejos son iguales si coinciden ambas partes.",
           "Obtendrás un sistema; al sustituir aparecerá una ecuación de segundo grado, así que puede haber dos soluciones."],
  "answer":"Dos pares: $a=4$ con $b=1$, y $a=-\\dfrac{1}{3}$ con $b=-12$.",
  "full_solution":"Se desarrolla el producto: $(a+i)(b-3i)=ab-3ai+bi-3i^{2}=ab+3+(b-3a)i$, usando que $-3i^{2}=+3$. Dos números complejos son iguales cuando coinciden su parte real y su parte imaginaria, de modo que se obtiene el sistema $ab+3=7$ y $b-3a=-11$, es decir, $ab=4$ y $b=3a-11$. Sustituyendo la segunda en la primera: $a(3a-11)=4$, o sea, $3a^{2}-11a-4=0$. Con la fórmula general, $a=\\dfrac{11\\pm\\sqrt{121+48}}{6}=\\dfrac{11\\pm\\sqrt{169}}{6}=\\dfrac{11\\pm 13}{6}$, lo que da $a=4$ y $a=-\\dfrac{1}{3}$. Para cada valor se calcula $b=3a-11$: si $a=4$, entonces $b=12-11=1$; si $a=-\\dfrac{1}{3}$, entonces $b=-1-11=-12$. Comprobación del primer par: $(4+i)(1-3i)=4-12i+i-3i^{2}=4-11i+3=7-11i$, correcto. Y del segundo: $\\left(-\\dfrac{1}{3}+i\\right)(-12-3i)=4+i-12i-3i^{2}=4-11i+3=7-11i$, también correcto. Las dos soluciones son válidas: el enunciado no pide números enteros.",
  "common_errors":["Olvidar que $-3i^{2}=+3$ y plantear la parte real como $ab$ en lugar de $ab+3$.",
                   "Quedarse solo con la solución entera $a=4$, $b=1$: la ecuación de segundo grado tiene dos raíces reales y ambas dan un par válido."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02B02-P2","type":"REASONING","objective_ids":["LO-02B02-2","LO-02B02-4"],
  "concept_ids":["C-02B-04","C-02B-03"],"difficulty":4,
  "statement":"Sea $z=a+bi$ con $a,b$ reales. Razona en general: a) ¿cómo es siempre el producto de dos complejos conjugados? b) ¿qué complejos cumplen que su opuesto coincide con su conjugado? c) ¿qué tipo de número se obtiene al calcular $z+\\overline{z}$ y al calcular $z-\\overline{z}$?",
  "hints":["Desarrolla $(a+bi)(a-bi)$ aplicando la suma por diferencia y sustituye $i^{2}=-1$.",
           "En b) escribe la condición $-z=\\overline{z}$ componente a componente."],
  "answer":"a) Siempre un número real mayor o igual que cero: $z\\overline{z}=a^{2}+b^{2}=|z|^{2}$. b) Los imaginarios puros (los de parte real nula), como $5i$ o $-2i$, y también el $0$. c) $z+\\overline{z}=2a$ es real, y $z-\\overline{z}=2bi$ es imaginario puro.",
  "full_solution":"a) $z\\overline{z}=(a+bi)(a-bi)$, que es una suma por diferencia: $a^{2}-(bi)^{2}=a^{2}-b^{2}i^{2}=a^{2}+b^{2}$. El resultado no tiene parte imaginaria, así que es real, y al ser suma de dos cuadrados es mayor o igual que cero (vale $0$ solo si $z=0$). De hecho coincide con $|z|^{2}$. Por ejemplo, $(2+5i)(2-5i)=4+25=29$. b) La condición $-z=\\overline{z}$ se escribe $-a-bi=a-bi$. Igualando partes reales, $-a=a$, luego $a=0$; igualando partes imaginarias, $-b=-b$, que se cumple siempre. Por tanto los números buscados son los de parte real nula, es decir, los imaginarios puros: $z=bi$. Comprobación con $z=5i$: su opuesto es $-5i$ y su conjugado también $-5i$. c) $z+\\overline{z}=(a+bi)+(a-bi)=2a$, que es un número real (se cancela la parte imaginaria); y $z-\\overline{z}=(a+bi)-(a-bi)=2bi$, que es imaginario puro (se cancela la parte real). Esto da dos fórmulas útiles: $\\operatorname{Re}(z)=\\dfrac{z+\\overline{z}}{2}$ y $\\operatorname{Im}(z)=\\dfrac{z-\\overline{z}}{2i}$.",
  "common_errors":["Decir que el producto de conjugados es $a^{2}-b^{2}$: al sustituir $i^{2}=-1$ el signo cambia y queda $a^{2}+b^{2}$.",
                   "Confundir opuesto y conjugado: el opuesto cambia el signo de las dos partes, $-z=-a-bi$, y el conjugado solo el de la imaginaria, $\\overline{z}=a-bi$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02B02-P3","type":"REASONING","objective_ids":["LO-02B02-3","LO-02B02-2"],
  "concept_ids":["C-02B-04","C-02B-03"],"difficulty":5,
  "statement":"a) Comprueba que, para cualquier número real $a$ se cumple $\\dfrac{1+ai}{a-i}=i$. b) Calcula el inverso de $-2+i$ en forma binómica.",
  "hints":["En a) basta multiplicar $i$ por el denominador y comprobar que se obtiene el numerador.",
           "En b) el inverso es $\\dfrac{1}{-2+i}$: multiplica numerador y denominador por el conjugado del denominador."],
  "answer":"a) Sí: $i(a-i)=ai-i^{2}=1+ai$, luego el cociente vale $i$ para todo $a$ real. b) $\\dfrac{1}{-2+i}=-\\dfrac{2}{5}-\\dfrac{1}{5}i$.",
  "full_solution":"a) La forma más rápida de comprobar una igualdad entre cocientes es multiplicar en cruz. Hay que ver si $1+ai=i\\cdot(a-i)$. Desarrollando el segundo miembro: $i(a-i)=ai-i^{2}=ai+1=1+ai$, que es exactamente el numerador. Por tanto $\\dfrac{1+ai}{a-i}=i$ para cualquier valor real de $a$ (el denominador $a-i$ nunca es cero, porque su parte imaginaria es $-1$). Es un resultado llamativo: una familia infinita de cocientes distintos que siempre da el mismo valor. b) El inverso de $z=-2+i$ es $\\dfrac{1}{-2+i}$. Se multiplica numerador y denominador por el conjugado $-2-i$: $\\dfrac{1}{-2+i}\\cdot\\dfrac{-2-i}{-2-i}=\\dfrac{-2-i}{(-2)^{2}+1^{2}}=\\dfrac{-2-i}{5}=-\\dfrac{2}{5}-\\dfrac{1}{5}i$. Comprobación: $(-2+i)\\left(-\\dfrac{2}{5}-\\dfrac{1}{5}i\\right)=\\dfrac{4}{5}+\\dfrac{2}{5}i-\\dfrac{2}{5}i-\\dfrac{1}{5}i^{2}=\\dfrac{4}{5}+\\dfrac{1}{5}=1$, como debe ser.",
  "common_errors":["Multiplicar por el propio denominador en lugar de por su conjugado: $(-2+i)(-2+i)$ sigue teniendo parte imaginaria y no elimina la $i$ del denominador.",
                   "Calcular el denominador como $(-2)^{2}-1^{2}=3$: al multiplicar un complejo por su conjugado se obtiene $a^{2}+b^{2}$, aquí $4+1=5$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02B02-P4","type":"STANDARD","objective_ids":["LO-02B02-3","LO-02B02-2"],
  "concept_ids":["C-02B-04","C-02B-03"],"difficulty":4,
  "statement":"Calcula $\\dfrac{-555-555i}{-1+3i}$ y da el resultado en forma binómica. Sugerencia: simplifica antes de dividir.",
  "hints":["Saca factor común $-555$ en el numerador: $-555-555i=-555(1+i)$.",
           "Después multiplica numerador y denominador por el conjugado del denominador, $-1-3i$."],
  "answer":"$-111+222i$",
  "full_solution":"Conviene sacar factor común en el numerador para trabajar con números pequeños: $-555-555i=-555(1+i)$, de modo que el cociente es $-555\\cdot\\dfrac{1+i}{-1+3i}$. Se multiplica numerador y denominador por el conjugado del denominador, $-1-3i$. El denominador se convierte en $(-1)^{2}+3^{2}=1+9=10$. El numerador es $(1+i)(-1-3i)=-1-3i-i-3i^{2}=-1-4i+3=2-4i$. Así, $\\dfrac{1+i}{-1+3i}=\\dfrac{2-4i}{10}=\\dfrac{1-2i}{5}$, y multiplicando por $-555$: $-555\\cdot\\dfrac{1-2i}{5}=-111(1-2i)=-111+222i$. Comprobación: $(-111+222i)(-1+3i)=111-333i-222i+666i^{2}=111-555i-666=-555-555i$, el numerador original.",
  "common_errors":["Dividir parte real entre parte real y parte imaginaria entre parte imaginaria ($\\dfrac{-555}{-1}$ y $\\dfrac{-555}{3}$): la división de complejos exige multiplicar por el conjugado del denominador.",
                   "Usar como conjugado de $-1+3i$ el número $1-3i$ (cambiando los dos signos): el conjugado solo cambia el signo de la parte imaginaria, y es $-1-3i$."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    # ---------- L01 P1 potencias de i
    cycle = {0: 1, 1: 1j, 2: -1, 3: -1j}
    for n, want in ((723, -1j), (6254, -1), (-17, -1j), (-527, 1j)):
        assert cycle[n % 4] == want, (n, n % 4)
    assert 723 % 4 == 3 and 723 == 4*180 + 3
    assert 6254 % 4 == 2 and 6254 == 4*1563 + 2
    assert -17 % 4 == 3 and -17 == 4*(-5) + 3 and -17 + 20 == 3
    assert -527 % 4 == 1 and -527 == 4*(-132) + 1 and -527 + 528 == 1 and 528 == 4*132
    assert abs((1j)**723 - (-1j)) < 1e-9
    assert abs((1j)**(-17) - (-1j)) < 1e-9
    assert abs((1j)**(-527) - 1j) < 1e-9
    assert (1j)**(-2) == -1 and -(1j**2) == 1
    # ---------- L01 P2 ecuacion cuartica
    P = lambda x: x**4 - 3*x**3 - 2*x**2 + 10*x - 12
    assert P(-2) == 0 and P(3) == 0
    assert 16 + 24 - 8 - 20 - 12 == 0
    co, acc = [1], 1
    for a in (-3, -2, 10, -12):
        acc = acc*(-2) + a; co.append(acc)
    assert co == [1, -5, 8, -6, 0], co
    Q = lambda x: x**3 - 5*x**2 + 8*x - 6
    assert Q(3) == 0 and 27 - 45 + 24 - 6 == 0
    co2, acc = [1], 1
    for a in (-5, 8, -6):
        acc = acc*3 + a; co2.append(acc)
    assert co2 == [1, -2, 2, 0], co2
    assert 4 - 8 == -4
    for z in (1 + 1j, 1 - 1j):
        assert abs(z**2 - 2*z + 2) < 1e-12
        assert abs(P(z)) < 1e-9, z
    assert (1 + 1j)**2 == 2j
    for x in (-2, 3):
        assert P(x) == 0
    # factorizacion completa
    for t in [F(k, 5) for k in range(-30, 31)]:
        x = complex(t)
        assert abs(P(x) - (x + 2)*(x - 3)*(x*x - 2*x + 2)) < 1e-6, t
    # ---------- L02 P1
    def prod(a, b): return (a + 1j)*(b - 3j)
    for a, b in ((4, 1), (F(-1, 3), -12)):
        z = prod(complex(a), complex(b))
        assert abs(z - (7 - 11j)) < 1e-12, (a, b, z)
    assert 121 + 48 == 169 and math.isqrt(169) == 13
    assert F(11 + 13, 6) == 4 and F(11 - 13, 6) == F(-1, 3)
    for a in (F(4), F(-1, 3)):
        b = 3*a - 11
        assert a*b == 4
    assert 3*4 - 11 == 1 and 3*F(-1, 3) - 11 == -12
    # ---------- L02 P2 conjugados
    for a in (-3, 0, 2, 5):
        for b in (-4, 0, 1, 5):
            z = complex(a, b)
            assert (z*z.conjugate()).imag == 0
            assert ic((z*z.conjugate()).real, a*a + b*b)
            assert ic(abs(z)**2, a*a + b*b, rel_tol=1e-12)
            assert (z + z.conjugate()) == complex(2*a, 0)
            assert (z - z.conjugate()) == complex(0, 2*b)
            assert ((-z) == z.conjugate()) == (a == 0)
    assert (2 + 5j)*(2 - 5j) == 29
    assert -(5j) == (5j).conjugate() == -5j
    # ---------- L02 P3
    for a in (-5, -1, 0, 1, 2.5, 7):
        assert abs((1 + a*1j)/(a - 1j) - 1j) < 1e-12, a
        assert abs(1j*(a - 1j) - (1 + a*1j)) < 1e-12
    inv = 1/(-2 + 1j)
    assert abs(inv - (-0.4 - 0.2j)) < 1e-12, inv
    assert ic(-2/5, -0.4) and ic(-1/5, -0.2)
    assert (-2)**2 + 1**2 == 5
    assert abs((-2 + 1j)*(-0.4 - 0.2j) - 1) < 1e-12
    # ---------- L02 P4
    z = (-555 - 555j)/(-1 + 3j)
    assert abs(z - (-111 + 222j)) < 1e-9, z
    assert (1 + 1j)*(-1 - 3j) == 2 - 4j
    assert (-1)**2 + 3**2 == 10
    assert abs((2 - 4j)/10 - (1 - 2j)/5) < 1e-15
    assert abs(-555*((1 - 2j)/5) - (-111 + 222j)) < 1e-9
    assert (-111 + 222j)*(-1 + 3j) == -555 - 555j
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
