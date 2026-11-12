# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'EJERCICIOS_DE_FRACCIONES_ALGEBRAICAS.pdf'
para bundles/eso_matematicas__mat_algebra_polinomios.json"""
from fractions import Fraction as F

L3 = "03_Identidades_notables.json"
L4 = "04_Factorización_y_divisibilidad_de_polinomios.json"
L5 = "05_División_general_y_fracciones_algebraicas.json"

EX = {
L3: [
 {"id":"EX-04-03-P1","type":"STANDARD","objective_ids":["LO-04-03-1","LO-04-03-2"],
  "concept_ids":["C-04-03-2","C-04-03-1"],"difficulty":4,
  "statement":"Opera y simplifica $\\left(x-\\dfrac{1}{x^{2}}\\right)\\left(x+\\dfrac{1}{x^{2}}\\right)$, dejando el resultado como una sola fracción. Indica para qué valores de $x$ tiene sentido la expresión.",
  "hints":["Fíjate en la estructura: es una suma por diferencia de los mismos dos términos.",
           "$\\left(\\dfrac{1}{x^{2}}\\right)^{2}=\\dfrac{1}{x^{4}}$."],
  "answer":"$x^{2}-\\dfrac{1}{x^{4}}=\\dfrac{x^{6}-1}{x^{4}}$, con $x\\neq 0$.",
  "full_solution":"La expresión tiene la forma $(a-b)(a+b)$ con $a=x$ y $b=\\dfrac{1}{x^{2}}$, así que se puede aplicar la identidad de la suma por diferencia: $(a-b)(a+b)=a^{2}-b^{2}$. Por tanto el producto vale $x^{2}-\\left(\\dfrac{1}{x^{2}}\\right)^{2}=x^{2}-\\dfrac{1}{x^{4}}$. Para dejarlo como una sola fracción se toma $x^{4}$ como denominador común: $x^{2}=\\dfrac{x^{6}}{x^{4}}$, de modo que el resultado es $\\dfrac{x^{6}}{x^{4}}-\\dfrac{1}{x^{4}}=\\dfrac{x^{6}-1}{x^{4}}$. La expresión solo tiene sentido si $x\\neq 0$, porque con $x=0$ los denominadores se anulan. Comprobación con $x=2$: el producto original es $\\left(2-\\dfrac{1}{4}\\right)\\left(2+\\dfrac{1}{4}\\right)=\\dfrac{7}{4}\\cdot\\dfrac{9}{4}=\\dfrac{63}{16}$, y la fórmula da $\\dfrac{2^{6}-1}{2^{4}}=\\dfrac{63}{16}$, el mismo valor.",
  "common_errors":["Elevar al cuadrado solo el denominador y escribir $\\dfrac{1}{x^{4}}$ como $\\dfrac{1}{x^{2}}$, o dejar $b^{2}=\\dfrac{1}{x^{2}}$ sin elevar.",
                   "Desarrollar los cuatro productos y perder algún término cruzado, cuando la identidad notable permite hacerlo en un paso: los términos cruzados se cancelan entre sí."],
  "provenance":"SOURCE_DERIVED"},
],

L4: [
 {"id":"EX-0404-P1","type":"STANDARD","objective_ids":["LO-04-04-1","LO-04-04-2","LO-04-04-4"],
  "concept_ids":["C-04-04-1","C-04-04-2","C-04-04-3"],"difficulty":5,
  "statement":"Factoriza por completo los dos polinomios $A(x)=2x^{3}+10x^{2}+16x+8$ y $B(x)=4x^{3}+8x^{2}-4x-8$, sacando primero factor común y aplicando después Ruffini.",
  "hints":["Saca el factor numérico común de cada polinomio antes de buscar raíces: así los coeficientes son más pequeños.",
           "Prueba como raíces los divisores del término independiente; en los dos casos $x=-2$ funciona."],
  "answer":"$A(x)=2(x+2)^{2}(x+1)$ y $B(x)=4(x+2)(x+1)(x-1)$.",
  "full_solution":"Para $A(x)$ se extrae el factor común $2$: $A(x)=2(x^{3}+5x^{2}+8x+4)$. Se buscan raíces entre los divisores de $4$; probando $x=-2$: $(-2)^{3}+5\\cdot 4+8\\cdot(-2)+4=-8+20-16+4=0$, así que $-2$ es raíz. Aplicando Ruffini con $-2$ a los coeficientes $1,5,8,4$ se obtiene el cociente $x^{2}+3x+2$ y resto $0$. Ese trinomio se factoriza como $(x+1)(x+2)$, porque sus raíces son $-1$ y $-2$. Por tanto $A(x)=2(x+2)(x+1)(x+2)=2(x+2)^{2}(x+1)$. Comprobación desarrollando: $(x+2)^{2}(x+1)=(x^{2}+4x+4)(x+1)=x^{3}+5x^{2}+8x+4$, correcto. Para $B(x)$ se extrae el factor común $4$: $B(x)=4(x^{3}+2x^{2}-x-2)$. Probando $x=-2$: $-8+8+2-2=0$, es raíz. Ruffini con $-2$ sobre $1,2,-1,-2$ da el cociente $x^{2}+0x-1=x^{2}-1$ y resto $0$. Y $x^{2}-1$ es una diferencia de cuadrados: $(x-1)(x+1)$. Luego $B(x)=4(x+2)(x-1)(x+1)$. Observa que el factor $2$ de $A$ y el $4$ de $B$ no son raíces: son factores numéricos que no aportan ningún valor que anule el polinomio.",
  "common_errors":["Colocar $+2$ en la esquina de la tabla de Ruffini al dividir entre $x+2$: hay que usar la raíz, que es $-2$.",
                   "Dejar $A(x)=2(x+2)(x^{2}+3x+2)$ como factorización final: el trinomio todavía se puede descomponer, y la factorización completa llega hasta factores de primer grado."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0404-P2","type":"STANDARD","objective_ids":["LO-04-04-3","LO-04-04-4","LO-04-04-2"],
  "concept_ids":["C-04-04-2","C-04-04-3"],"difficulty":4,
  "statement":"Factoriza por completo $P(x)=x^{3}+3x^{2}-16x-48$ buscando una raíz entera entre los divisores del término independiente.",
  "hints":["Los candidatos a raíz entera son los divisores de $48$: $\\pm 1,\\pm 2,\\pm 3,\\pm 4,\\pm 6,\\dots$",
           "Comprueba $x=4$ sustituyendo en el polinomio antes de montar la tabla de Ruffini."],
  "answer":"$P(x)=(x-4)(x+4)(x+3)$.",
  "full_solution":"Se prueban divisores de $48$. Con $x=4$: $4^{3}+3\\cdot 4^{2}-16\\cdot 4-48=64+48-64-48=0$, así que $4$ es raíz y $(x-4)$ es factor. Se aplica Ruffini con $4$ a los coeficientes $1,\\ 3,\\ -16,\\ -48$: se baja el $1$; $1\\cdot 4=4$ y $3+4=7$; $7\\cdot 4=28$ y $-16+28=12$; $12\\cdot 4=48$ y $-48+48=0$, resto cero como debía. El cociente es $x^{2}+7x+12$, que se factoriza buscando dos números que sumen $7$ y multipliquen $12$: son $3$ y $4$, luego $x^{2}+7x+12=(x+3)(x+4)$. Por tanto $P(x)=(x-4)(x+3)(x+4)$, y las raíces son $4$, $-3$ y $-4$. Comprobación: el producto de las raíces cambiado de signo debe dar el término independiente, y en efecto $4\\cdot(-3)\\cdot(-4)=48$, cuyo opuesto es $-48$.",
  "common_errors":["Buscar raíces entre números que no dividen al término independiente: si $P$ tiene una raíz entera, esa raíz divide necesariamente a $-48$.",
                   "Usar $-4$ en la tabla de Ruffini para el factor $(x-4)$: el número que se coloca es la raíz, es decir, $4$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0404-P3","type":"REASONING","objective_ids":["LO-04-04-1","LO-04-04-2"],
  "concept_ids":["C-04-04-1","C-04-04-2"],"difficulty":4,
  "statement":"Factoriza por completo en los números reales $x^{5}-x$ y explica por qué el factor $x^{2}+1$ no se puede descomponer más.",
  "hints":["Empieza sacando factor común $x$ y después aplica dos veces la diferencia de cuadrados.",
           "¿Hay algún número real cuyo cuadrado sea $-1$?"],
  "answer":"$x^{5}-x=x(x-1)(x+1)(x^{2}+1)$. El factor $x^{2}+1$ no tiene raíces reales, así que no se descompone en factores reales de primer grado.",
  "full_solution":"Primero se saca factor común $x$: $x^{5}-x=x(x^{4}-1)$. Ahora $x^{4}-1$ es una diferencia de cuadrados, porque $x^{4}=(x^{2})^{2}$ y $1=1^{2}$: $x^{4}-1=(x^{2}-1)(x^{2}+1)$. El primer paréntesis es otra diferencia de cuadrados: $x^{2}-1=(x-1)(x+1)$. Juntando todo, $x^{5}-x=x(x-1)(x+1)(x^{2}+1)$. El factor $x^{2}+1$ no se puede descomponer en factores reales porque no tiene raíces reales: para cualquier número real $x$ se cumple $x^{2}\\ge 0$, luego $x^{2}+1\\ge 1>0$ y nunca se anula. Un error frecuente es escribir $x^{2}+1=(x+1)(x+1)$, pero al desarrollar eso da $x^{2}+2x+1$, que no es lo mismo. Comprobación de la factorización con $x=2$: $2^{5}-2=30$, y $2\\cdot 1\\cdot 3\\cdot 5=30$, correcto.",
  "common_errors":["Factorizar $x^{2}+1$ como $(x+1)^{2}$ o como $(x+1)(x-1)$: lo primero da $x^{2}+2x+1$ y lo segundo $x^{2}-1$; solo la diferencia de cuadrados se factoriza.",
                   "Olvidar el factor común $x$ y perder la raíz $x=0$, dejando la factorización incompleta."],
  "provenance":"SOURCE_DERIVED"},
],

L5: [
 {"id":"EX-0405-P1","type":"STANDARD","objective_ids":["LO-04-05-2","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":5,
  "statement":"Simplifica $\\dfrac{2x^{3}+10x^{2}+16x+8}{4x^{3}+8x^{2}-4x-8}$ e indica todas las restricciones de la fracción original.",
  "hints":["Factoriza numerador y denominador por completo antes de cancelar nada.",
           "Las restricciones las marcan los factores del denominador original, incluso los que después se cancelan."],
  "answer":"$\\dfrac{x+2}{2(x-1)}=\\dfrac{x+2}{2x-2}$, con $x\\neq -2$, $x\\neq -1$ y $x\\neq 1$.",
  "full_solution":"Se factorizan los dos polinomios. El numerador: $2x^{3}+10x^{2}+16x+8=2(x^{3}+5x^{2}+8x+4)$, y como $x=-2$ es raíz, Ruffini da $2(x+2)(x^{2}+3x+2)=2(x+2)(x+2)(x+1)=2(x+2)^{2}(x+1)$. El denominador: $4x^{3}+8x^{2}-4x-8=4(x^{3}+2x^{2}-x-2)$, y con la raíz $x=-2$ Ruffini da $4(x+2)(x^{2}-1)=4(x+2)(x-1)(x+1)$. La fracción queda $\\dfrac{2(x+2)^{2}(x+1)}{4(x+2)(x-1)(x+1)}$. Ahora sí se pueden cancelar factores comunes: un $(x+2)$, el factor $(x+1)$ completo, y el $2$ con el $4$ dejando un $2$ en el denominador. El resultado es $\\dfrac{x+2}{2(x-1)}$, es decir, $\\dfrac{x+2}{2x-2}$. Las restricciones se leen en el denominador ORIGINAL, cuyos factores son $(x+2)$, $(x-1)$ y $(x+1)$: por tanto $x\\neq -2$, $x\\neq 1$ y $x\\neq -1$. Las dos últimas restricciones son fáciles de olvidar porque esos factores desaparecen al simplificar, pero la fracción de partida no existe en esos valores. Comprobación con $x=3$: la fracción original vale $\\dfrac{54+90+48+8}{108+72-12-8}=\\dfrac{200}{160}=1{,}25$, y la simplificada $\\dfrac{5}{4}=1{,}25$.",
  "common_errors":["Cancelar términos sueltos (por ejemplo los $x^{3}$ o los $8$) en lugar de factores completos: solo se cancela lo que multiplica a todo.",
                   "Dar como únicas restricciones las del denominador simplificado ($x\\neq 1$), olvidando $x\\neq -2$ y $x\\neq -1$, que vienen de factores cancelados."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P2","type":"STANDARD","objective_ids":["LO-04-05-4","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":4,
  "statement":"Calcula y simplifica $\\dfrac{2x+4}{x+4}-\\dfrac{2x-14}{x-5}$ e indica las restricciones. El resultado puede sorprenderte.",
  "hints":["El mínimo común múltiplo de los denominadores es $(x+4)(x-5)$.",
           "Al desarrollar los dos numeradores, fíjate en qué pasa con los términos en $x^{2}$ y en $x$."],
  "answer":"$\\dfrac{36}{(x+4)(x-5)}=\\dfrac{36}{x^{2}-x-20}$, con $x\\neq -4$ y $x\\neq 5$.",
  "full_solution":"Los denominadores $x+4$ y $x-5$ no tienen factores comunes, así que el mínimo común múltiplo es su producto, $(x+4)(x-5)$. Se escriben las dos fracciones con ese denominador: $\\dfrac{(2x+4)(x-5)}{(x+4)(x-5)}-\\dfrac{(2x-14)(x+4)}{(x+4)(x-5)}$. Se desarrollan los numeradores con cuidado: $(2x+4)(x-5)=2x^{2}-10x+4x-20=2x^{2}-6x-20$, y $(2x-14)(x+4)=2x^{2}+8x-14x-56=2x^{2}-6x-56$. Al restar, los términos en $x^{2}$ se cancelan y también los términos en $x$: $\\left(2x^{2}-6x-20\\right)-\\left(2x^{2}-6x-56\\right)=-20+56=36$. Queda, por tanto, $\\dfrac{36}{(x+4)(x-5)}$, que desarrollando el denominador es $\\dfrac{36}{x^{2}-x-20}$. Es llamativo que el numerador sea una constante: las partes variables se compensan exactamente. Las restricciones son $x\\neq -4$ y $x\\neq 5$. Comprobación con $x=0$: la expresión original vale $\\dfrac{4}{4}-\\dfrac{-14}{-5}=1-2{,}8=-1{,}8$, y la simplificada $\\dfrac{36}{-20}=-1{,}8$.",
  "common_errors":["Restar solo el primer término del segundo numerador y olvidar cambiar el signo del resto: hay que restar el paréntesis completo.",
                   "Cancelar la $x$ del numerador con la del denominador después de operar: $36$ es una constante y no hay nada que cancelar."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P3","type":"STANDARD","objective_ids":["LO-04-05-4","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":4,
  "statement":"Opera y simplifica $1+\\dfrac{1}{2x-1}-\\dfrac{2x}{4x^{2}-1}$, indicando las restricciones.",
  "hints":["Factoriza $4x^{2}-1$ como diferencia de cuadrados para hallar el mínimo común múltiplo.",
           "El $1$ también hay que escribirlo con el denominador común."],
  "answer":"$\\dfrac{4x^{2}}{4x^{2}-1}$, con $x\\neq\\dfrac{1}{2}$ y $x\\neq -\\dfrac{1}{2}$.",
  "full_solution":"Primero se factoriza el denominador mayor: $4x^{2}-1=(2x)^{2}-1^{2}=(2x-1)(2x+1)$. El mínimo común múltiplo de $1$, $2x-1$ y $(2x-1)(2x+1)$ es $(2x-1)(2x+1)$. Se escriben los tres sumandos con ese denominador: el $1$ se convierte en $\\dfrac{(2x-1)(2x+1)}{(2x-1)(2x+1)}=\\dfrac{4x^{2}-1}{4x^{2}-1}$; la segunda fracción, multiplicando arriba y abajo por $(2x+1)$, queda $\\dfrac{2x+1}{4x^{2}-1}$; y la tercera ya tiene ese denominador. Sumando los numeradores: $\\left(4x^{2}-1\\right)+\\left(2x+1\\right)-2x=4x^{2}-1+2x+1-2x=4x^{2}$. El resultado es $\\dfrac{4x^{2}}{4x^{2}-1}$, que no se simplifica más porque $4x^{2}$ y $4x^{2}-1$ no comparten factores. Las restricciones vienen de $2x-1=0$ y $2x+1=0$: $x\\neq\\dfrac{1}{2}$ y $x\\neq-\\dfrac{1}{2}$. Comprobación con $x=1$: la expresión original vale $1+1-\\dfrac{2}{3}=\\dfrac{4}{3}$, y la simplificada $\\dfrac{4}{3}$.",
  "common_errors":["Olvidar escribir el $1$ con el denominador común y sumar solo las dos fracciones.",
                   "Simplificar $\\dfrac{4x^{2}}{4x^{2}-1}$ cancelando los $4x^{2}$ y dar $\\dfrac{1}{-1}=-1$: el $-1$ del denominador es un sumando, no un factor."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P4","type":"STANDARD","objective_ids":["LO-04-05-4","LO-04-05-2","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":5,
  "statement":"Calcula y simplifica $\\dfrac{1}{x^{2}-x}+\\dfrac{2x-1}{x-1}-\\dfrac{3x-1}{x}$, indicando las restricciones.",
  "hints":["Factoriza $x^{2}-x=x(x-1)$: ese es ya el mínimo común múltiplo de los tres denominadores.",
           "Al final, saca factor común en el numerador para ver si se puede simplificar."],
  "answer":"$\\dfrac{3-x}{x-1}$, con $x\\neq 0$ y $x\\neq 1$.",
  "full_solution":"Se factoriza el primer denominador: $x^{2}-x=x(x-1)$. Los otros dos son $x-1$ y $x$, así que el mínimo común múltiplo de los tres es $x(x-1)$. Se reescriben las tres fracciones: la primera ya lo tiene; la segunda se multiplica arriba y abajo por $x$, dando $\\dfrac{x(2x-1)}{x(x-1)}=\\dfrac{2x^{2}-x}{x(x-1)}$; la tercera se multiplica por $(x-1)$, dando $\\dfrac{(3x-1)(x-1)}{x(x-1)}=\\dfrac{3x^{2}-4x+1}{x(x-1)}$. Ahora se opera el numerador, restando la tercera: $1+\\left(2x^{2}-x\\right)-\\left(3x^{2}-4x+1\\right)=1+2x^{2}-x-3x^{2}+4x-1=-x^{2}+3x$. La fracción es $\\dfrac{-x^{2}+3x}{x(x-1)}$. Sacando factor común $x$ en el numerador: $\\dfrac{x(-x+3)}{x(x-1)}$, y cancelando el factor $x$ queda $\\dfrac{3-x}{x-1}$. Las restricciones son $x\\neq 0$ y $x\\neq 1$, y la de $x\\neq 0$ sigue siendo necesaria aunque ese factor se haya cancelado. Comprobación con $x=2$: la expresión original vale $\\dfrac{1}{2}+\\dfrac{3}{1}-\\dfrac{5}{2}=1$, y la simplificada $\\dfrac{3-2}{2-1}=1$.",
  "common_errors":["Restar la última fracción sin cambiar el signo de todos sus términos: hay que restar $(3x^{2}-4x+1)$ completo, lo que incluye $+4x$ y $-1$.",
                   "Cancelar la $x$ del numerador $-x^{2}+3x$ con la del denominador antes de sacar factor común: hasta que no esté factorizado no se puede cancelar nada."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P5","type":"STANDARD","objective_ids":["LO-04-05-4","LO-04-05-2","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":5,
  "statement":"Calcula y simplifica $\\dfrac{x^{2}-6x+9}{x^{2}+2x-15}:\\dfrac{2x-10}{x^{2}-25}$, indicando las restricciones.",
  "hints":["Dividir es multiplicar por la fracción inversa: invierte la segunda y factoriza todo.",
           "$x^{2}-6x+9$ es un cuadrado perfecto y $x^{2}-25$ una diferencia de cuadrados."],
  "answer":"$\\dfrac{x-3}{2}$, con $x\\neq -5$, $x\\neq 3$ y $x\\neq 5$.",
  "full_solution":"Dividir fracciones es multiplicar por la inversa: $\\dfrac{x^{2}-6x+9}{x^{2}+2x-15}\\cdot\\dfrac{x^{2}-25}{2x-10}$. Ahora se factoriza cada pieza: $x^{2}-6x+9=(x-3)^{2}$ (cuadrado perfecto); $x^{2}+2x-15=(x+5)(x-3)$, porque sus raíces son $-5$ y $3$; $x^{2}-25=(x-5)(x+5)$ (diferencia de cuadrados); y $2x-10=2(x-5)$. El producto queda $\\dfrac{(x-3)^{2}(x-5)(x+5)}{(x+5)(x-3)\\cdot 2(x-5)}$. Se cancelan $(x+5)$, $(x-5)$ y un factor $(x-3)$, y queda $\\dfrac{x-3}{2}$. Las restricciones proceden de todo lo que no puede anularse: los denominadores originales $x^{2}+2x-15$ (luego $x\\neq -5$ y $x\\neq 3$) y $x^{2}-25$ (luego $x\\neq 5$ y $x\\neq -5$), y además el divisor $2x-10$ no puede ser cero (de nuevo $x\\neq 5$), porque no se puede dividir entre cero. En total: $x\\neq -5$, $x\\neq 3$, $x\\neq 5$. Comprobación con $x=4$: la primera fracción vale $\\dfrac{16-24+9}{16+8-15}=\\dfrac{1}{9}$, la segunda $\\dfrac{8-10}{16-25}=\\dfrac{-2}{-9}=\\dfrac{2}{9}$, y su cociente $\\dfrac{1/9}{2/9}=\\dfrac{1}{2}$, que coincide con $\\dfrac{4-3}{2}$.",
  "common_errors":["Invertir la primera fracción en lugar de la segunda al convertir la división en producto.",
                   "Olvidar la restricción que viene del numerador del divisor: si $2x-10=0$ la segunda fracción vale $0$ y la división no está definida."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P6","type":"STANDARD","objective_ids":["LO-04-05-4","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":5,
  "statement":"Opera y simplifica $\\dfrac{x-2}{2x}-\\dfrac{1-3x}{3x^{2}}+\\dfrac{2x^{2}+3}{6x^{4}}$, indicando las restricciones.",
  "hints":["El mínimo común múltiplo de $2x$, $3x^{2}$ y $6x^{4}$ es $6x^{4}$: fíjate tanto en los números como en los exponentes.",
           "Al reescribir cada fracción, multiplica numerador y denominador por lo que falta para llegar a $6x^{4}$."],
  "answer":"$\\dfrac{x^{4}+1}{2x^{4}}$, con $x\\neq 0$.",
  "full_solution":"El mínimo común múltiplo de los denominadores es $6x^{4}$: entre los coeficientes $2$, $3$ y $6$ el mcm es $6$, y entre $x$, $x^{2}$ y $x^{4}$ es $x^{4}$. Se reescriben las tres fracciones. La primera se multiplica arriba y abajo por $3x^{3}$: $\\dfrac{3x^{3}(x-2)}{6x^{4}}=\\dfrac{3x^{4}-6x^{3}}{6x^{4}}$. La segunda por $2x^{2}$: $\\dfrac{2x^{2}(1-3x)}{6x^{4}}=\\dfrac{2x^{2}-6x^{3}}{6x^{4}}$, y entra restando. La tercera ya tiene el denominador. Sumando los numeradores con sus signos: $\\left(3x^{4}-6x^{3}\\right)-\\left(2x^{2}-6x^{3}\\right)+\\left(2x^{2}+3\\right)=3x^{4}-6x^{3}-2x^{2}+6x^{3}+2x^{2}+3=3x^{4}+3$. La fracción es $\\dfrac{3x^{4}+3}{6x^{4}}$, y sacando factor común $3$ en el numerador queda $\\dfrac{3\\left(x^{4}+1\\right)}{6x^{4}}=\\dfrac{x^{4}+1}{2x^{4}}$. La única restricción es $x\\neq 0$. Comprobación con $x=1$: la expresión original vale $-\\dfrac{1}{2}-\\dfrac{-2}{3}+\\dfrac{5}{6}=-\\dfrac{1}{2}+\\dfrac{2}{3}+\\dfrac{5}{6}=1$, y la simplificada $\\dfrac{2}{2}=1$.",
  "common_errors":["Tomar como denominador común el producto $2x\\cdot 3x^{2}\\cdot 6x^{4}=36x^{7}$: funciona, pero complica mucho las cuentas; el mínimo común múltiplo es $6x^{4}$.",
                   "Cancelar los $x^{4}$ de $\\dfrac{x^{4}+1}{2x^{4}}$ y dar $\\dfrac{1}{2}$: en el numerador $x^{4}$ es un sumando, no un factor."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0405-P7","type":"STANDARD","objective_ids":["LO-04-05-2","LO-04-05-3"],
  "concept_ids":["C-04-05-2"],"difficulty":3,
  "statement":"Simplifica $\\dfrac{x^{3}-49x}{x^{4}-7x^{3}}$ e indica las restricciones.",
  "hints":["Saca factor común en el numerador y en el denominador.",
           "Después aplica la diferencia de cuadrados a $x^{2}-49$."],
  "answer":"$\\dfrac{x+7}{x^{2}}$, con $x\\neq 0$ y $x\\neq 7$.",
  "full_solution":"En el numerador se saca factor común $x$: $x^{3}-49x=x\\left(x^{2}-49\\right)$, y $x^{2}-49$ es una diferencia de cuadrados, $(x-7)(x+7)$, así que el numerador es $x(x-7)(x+7)$. En el denominador se saca factor común $x^{3}$: $x^{4}-7x^{3}=x^{3}(x-7)$. La fracción queda $\\dfrac{x(x-7)(x+7)}{x^{3}(x-7)}$. Se cancela el factor $(x-7)$ y se simplifica $\\dfrac{x}{x^{3}}=\\dfrac{1}{x^{2}}$, con lo que el resultado es $\\dfrac{x+7}{x^{2}}$. Las restricciones vienen del denominador original $x^{3}(x-7)$: $x\\neq 0$ y $x\\neq 7$; la segunda hay que escribirla aunque el factor $(x-7)$ se haya cancelado. Comprobación con $x=1$: la fracción original vale $\\dfrac{1-49}{1-7}=\\dfrac{-48}{-6}=8$, y la simplificada $\\dfrac{1+7}{1}=8$.",
  "common_errors":["Cancelar la $x$ del numerador con una sola del denominador y dejar $\\dfrac{x+7}{x^{3}}$: hay que restar exponentes, $\\dfrac{x}{x^{3}}=\\dfrac{1}{x^{2}}$.",
                   "Dar solo $x\\neq 0$ como restricción: el factor $(x-7)$ estaba en el denominador de partida, así que $x=7$ también queda excluido."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    from fractions import Fraction as Fr
    # --- L03 P1
    for x in (Fr(2), Fr(3), Fr(-1), Fr(1, 2), Fr(5)):
        lhs = (x - Fr(1, 1)/x**2) * (x + Fr(1, 1)/x**2)
        assert lhs == x**2 - Fr(1, 1)/x**4 == (x**6 - 1)/x**4, x
    x = Fr(2)
    assert (x - Fr(1, 4))*(x + Fr(1, 4)) == Fr(7, 4)*Fr(9, 4) == Fr(63, 16)
    assert Fr(2**6 - 1, 2**4) == Fr(63, 16)

    # --- polinomios como listas de coeficientes (grado descendente)
    def ev(c, x):
        r = Fr(0)
        for a in c: r = r*x + a
        return r
    A = [2, 10, 16, 8]
    B = [4, 8, -4, -8]
    P = [1, 3, -16, -48]
    testvals = [Fr(k) for k in (-7, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 7, 11)] + [Fr(1, 2), Fr(-3, 5)]
    # --- L04 P1
    for x in testvals:
        assert ev(A, x) == 2*(x+2)**2*(x+1)
        assert ev(B, x) == 4*(x+2)*(x+1)*(x-1)
    assert ev(A, Fr(-2)) == 0 and ev(B, Fr(-2)) == 0
    assert ev([1, 5, 8, 4], Fr(-2)) == 0
    assert ev([1, 2, -1, -2], Fr(-2)) == 0
    for x in testvals:
        assert (x+2)**2*(x+1) == ev([1, 5, 8, 4], x)
    # --- L04 P2
    for x in testvals:
        assert ev(P, x) == (x-4)*(x+4)*(x+3)
        assert ev([1, 7, 12], x) == (x+3)*(x+4)
    assert ev(P, Fr(4)) == 0 and 4**3 + 3*16 - 64 - 48 == 0
    # tabla de Ruffini con 4 sobre 1,3,-16,-48
    co, acc = [1], 1
    for a in (3, -16, -48):
        acc = acc*4 + a; co.append(acc)
    assert co == [1, 7, 12, 0]
    assert 4*(-3)*(-4) == 48
    # --- L04 P3
    for x in testvals:
        assert x**5 - x == x*(x-1)*(x+1)*(x**2+1)
    assert 2**5 - 2 == 30 == 2*1*3*5
    for x in testvals:
        assert x**2 + 1 > 0
        assert (x+1)**2 == x**2 + 2*x + 1
    # --- L05 P1
    def f1(x): return (2*x**3 + 10*x**2 + 16*x + 8) / (4*x**3 + 8*x**2 - 4*x - 8)
    for x in testvals:
        if x in (Fr(-2), Fr(-1), Fr(1)): continue
        assert f1(x) == (x+2)/(2*(x-1)), x
    assert f1(Fr(3)) == Fr(200, 160) == Fr(5, 4)
    assert 2*27 + 10*9 + 16*3 + 8 == 200 and 4*27 + 8*9 - 12 - 8 == 160
    # --- L05 P2
    def f2(x): return (2*x+4)/(x+4) - (2*x-14)/(x-5)
    for x in testvals:
        if x in (Fr(-4), Fr(5)): continue
        assert f2(x) == 36/((x+4)*(x-5)) == 36/(x**2 - x - 20), x
    assert f2(Fr(0)) == Fr(-9, 5) and Fr(36, -20) == Fr(-9, 5)
    # desarrollos
    for x in testvals:
        assert (2*x+4)*(x-5) == 2*x**2 - 6*x - 20
        assert (2*x-14)*(x+4) == 2*x**2 - 6*x - 56
    # --- L05 P3
    def f3(x): return 1 + 1/(2*x-1) - (2*x)/(4*x**2-1)
    for x in testvals:
        if x in (Fr(1, 2), Fr(-1, 2)): continue
        assert f3(x) == (4*x**2)/(4*x**2-1), x
    assert f3(Fr(1)) == Fr(4, 3)
    # --- L05 P4
    def f4(x): return 1/(x**2-x) + (2*x-1)/(x-1) - (3*x-1)/x
    for x in testvals:
        if x in (Fr(0), Fr(1)): continue
        assert f4(x) == (3-x)/(x-1), x
    assert f4(Fr(2)) == 1
    for x in testvals:
        assert (3*x-1)*(x-1) == 3*x**2 - 4*x + 1
        assert 1 + (2*x**2 - x) - (3*x**2 - 4*x + 1) == -x**2 + 3*x
    # --- L05 P5
    def f5(x): return ((x**2-6*x+9)/(x**2+2*x-15)) / ((2*x-10)/(x**2-25))
    for x in testvals:
        if x in (Fr(-5), Fr(3), Fr(5)): continue
        assert f5(x) == (x-3)/2, x
    assert f5(Fr(4)) == Fr(1, 2)
    assert (16-24+9) == 1 and (16+8-15) == 9 and (8-10) == -2 and (16-25) == -9
    for x in testvals:
        assert x**2 - 6*x + 9 == (x-3)**2
        assert x**2 + 2*x - 15 == (x+5)*(x-3)
        assert x**2 - 25 == (x-5)*(x+5)
    # --- L05 P6
    def f6(x): return (x-2)/(2*x) - (1-3*x)/(3*x**2) + (2*x**2+3)/(6*x**4)
    for x in testvals:
        if x == 0: continue
        assert f6(x) == (x**4+1)/(2*x**4), x
    assert f6(Fr(1)) == 1
    for x in testvals:
        assert 3*x**3*(x-2) == 3*x**4 - 6*x**3
        assert 2*x**2*(1-3*x) == 2*x**2 - 6*x**3
        assert (3*x**4 - 6*x**3) - (2*x**2 - 6*x**3) + (2*x**2 + 3) == 3*x**4 + 3
    assert Fr(-1, 2) + Fr(2, 3) + Fr(5, 6) == 1
    # --- L05 P7
    def f7(x): return (x**3 - 49*x)/(x**4 - 7*x**3)
    for x in testvals:
        if x in (Fr(0), Fr(7)): continue
        assert f7(x) == (x+7)/x**2, x
    assert f7(Fr(1)) == 8 and Fr(-48, -6) == 8
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
