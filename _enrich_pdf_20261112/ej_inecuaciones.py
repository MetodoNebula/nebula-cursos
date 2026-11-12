# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'inecuaciones.pdf' (20 ejercicios de inecuaciones, 4 ESO)
para bundles/eso_matematicas__mat_sistemas_inecuaciones.json"""
import math
from fractions import Fraction as F

L4 = "04_Inecuaciones_e_intervalos.json"
L5 = "05_Inecuaciones_de_segundo_grado.json"

EX = {
L4: [
 {"id":"EX-0604-P1","type":"STANDARD","objective_ids":["LO-0604-1","LO-0604-2"],
  "concept_ids":["C-0604-01","C-0604-02"],"difficulty":4,
  "statement":"Resuelve $\\dfrac{x-1}{2}-\\dfrac{x-4}{3}<1$ quitando primero los denominadores, y expresa la solución en notación de intervalos.",
  "hints":["Multiplica los dos miembros por el mínimo común múltiplo de $2$ y $3$, que es $6$: al ser positivo, el sentido de la desigualdad no cambia.",
           "Cuidado con el paréntesis del segundo numerador: al multiplicar por $-2$ hay que cambiar los dos signos."],
  "answer":"$x<1$, es decir, $(-\\infty,1)$.",
  "full_solution":"El mínimo común múltiplo de los denominadores es $6$. Multiplicando los dos miembros por $6$ (número positivo, así que la desigualdad conserva el sentido): $6\\cdot\\dfrac{x-1}{2}-6\\cdot\\dfrac{x-4}{3}<6\\cdot 1$, es decir, $3(x-1)-2(x-4)<6$. Se desarrollan los paréntesis con cuidado del signo: $3x-3-2x+8<6$. Reduciendo, $x+5<6$, de donde $x<1$. En notación de intervalos, la solución es $(-\\infty,1)$, con paréntesis en el $1$ porque la desigualdad es estricta y ese valor no se incluye. Comprobación: con $x=0$ el primer miembro vale $\\dfrac{-1}{2}-\\dfrac{-4}{3}=-0{,}5+1{,}3\\overline{3}=0{,}8\\overline{3}<1$, cierto; con $x=2$ vale $\\dfrac{1}{2}-\\dfrac{-2}{3}=0{,}5+0{,}6\\overline{6}=1{,}1\\overline{6}$, que no es menor que $1$, como debe ser.",
  "common_errors":["Multiplicar por $6$ solo los términos con denominador y dejar el $1$ del segundo miembro sin multiplicar.",
                   "Escribir $3x-3-2x-8<6$: al multiplicar $-\\dfrac{x-4}{3}$ por $6$ se obtiene $-2(x-4)=-2x+8$, con el signo del $-4$ cambiado."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0604-P2","type":"STANDARD","objective_ids":["LO-0604-1","LO-0604-2"],
  "concept_ids":["C-0604-01","C-0604-02"],"difficulty":5,
  "statement":"Resuelve $\\dfrac{5x-2}{3}-\\dfrac{x-8}{4}>\\dfrac{x+14}{2}-2$ y expresa la solución en notación de intervalos.",
  "hints":["El mínimo común múltiplo de $3$, $4$ y $2$ es $12$.",
           "No olvides multiplicar también el $-2$ del segundo miembro por $12$."],
  "answer":"$x>4$, es decir, $(4,+\\infty)$.",
  "full_solution":"El mínimo común múltiplo de $3$, $4$ y $2$ es $12$. Multiplicando todo por $12$ (positivo, el sentido se mantiene): $4(5x-2)-3(x-8)>6(x+14)-24$. Se desarrollan los paréntesis: $20x-8-3x+24>6x+84-24$. Reduciendo cada miembro: $17x+16>6x+60$. Se pasan las $x$ a un lado y los números al otro: $17x-6x>60-16$, es decir, $11x>44$, y dividiendo entre $11$ (positivo) queda $x>4$. En intervalos, $(4,+\\infty)$. Comprobación con $x=5$: el primer miembro vale $\\dfrac{23}{3}-\\dfrac{-3}{4}=7{,}6\\overline{6}+0{,}75=8{,}41\\overline{6}$ y el segundo $\\dfrac{19}{2}-2=7{,}5$; en efecto $8{,}41\\overline{6}>7{,}5$. Con $x=4$ los dos miembros valen exactamente $7$, así que el $4$ no pertenece a la solución.",
  "common_errors":["Multiplicar por $12$ el término $-2$ y escribir $-2$ en vez de $-24$: todos los términos de los dos miembros se multiplican.",
                   "Dividir al final entre $11$ e invertir el sentido de la desigualdad: solo se invierte al multiplicar o dividir por un número negativo."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0604-P3","type":"REASONING","objective_ids":["LO-0604-1","LO-0604-2"],
  "concept_ids":["C-0604-01","C-0604-02"],"difficulty":4,
  "statement":"Resuelve las dos inecuaciones siguientes y describe su conjunto solución: a) $12(x+2)+5<3(4x+1)+3$; b) $5(x-2)-4(2x+1)<-3x+3$. ¿Qué tienen en común y en qué se diferencian?",
  "hints":["Desarrolla los paréntesis y reduce: en los dos casos los términos en $x$ desaparecen.",
           "Cuando queda una desigualdad solo con números, hay que decidir si es verdadera o falsa."],
  "answer":"a) No tiene solución ($\\varnothing$), porque se reduce a $29<6$, que es falso. b) La cumplen todos los números reales ($\\mathbb{R}$), porque se reduce a $-14<3$, que es verdadero.",
  "full_solution":"a) Se desarrollan los dos miembros: $12x+24+5<12x+3+3$, es decir, $12x+29<12x+6$. Restando $12x$ en los dos miembros desaparece la incógnita y queda $29<6$, una desigualdad numérica falsa. Como no depende de $x$, no hay ningún valor que la cumpla: el conjunto solución es el conjunto vacío, $\\varnothing$. b) Se desarrolla igual: $5x-10-8x-4<-3x+3$, es decir, $-3x-14<-3x+3$. Sumando $3x$ en los dos miembros desaparece de nuevo la incógnita y queda $-14<3$, que es verdadera. Al no depender de $x$, se cumple para cualquier valor: el conjunto solución es $\\mathbb{R}$, todos los números reales. Lo que tienen en común es que los coeficientes de $x$ coinciden en los dos miembros, y por eso la incógnita se cancela; lo que las diferencia es que la desigualdad numérica resultante es falsa en el primer caso y verdadera en el segundo. Conviene no confundir estas dos situaciones con un error de cálculo: que la $x$ desaparezca es un resultado legítimo.",
  "common_errors":["Pensar que si la $x$ desaparece se ha cometido un error y volver atrás: puede ocurrir, y entonces la respuesta es $\\varnothing$ o $\\mathbb{R}$ según sea falsa o verdadera la desigualdad numérica.",
                   "Escribir $x=0$ como solución cuando la incógnita se cancela: el resultado es un conjunto (vacío o todo $\\mathbb{R}$), no un valor concreto."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0604-P4","type":"CONTEXT","objective_ids":["LO-0604-1","LO-0604-2"],
  "concept_ids":["C-0604-01"],"difficulty":5,
  "statement":"Una editorial ofrece a un vendedor dos contratos: (A) $25\\,000$ euros fijos más un $10\\%$ del precio de cada libro vendido; (B) un $30\\%$ del precio de cada libro vendido, sin fijo. El precio de cada libro es de $35$ euros. ¿A partir de cuántos libros vendidos le conviene más la opción B? Una solución publicada afirma que la respuesta es $3571$ libros: comprueba si es correcta.",
  "hints":["Calcula primero cuánto cobra por libro con cada contrato: el $10\\%$ y el $30\\%$ de $35$ euros.",
           "Al resolver la inecuación saldrá un número con decimales; piensa qué entero es el primero que la cumple."],
  "answer":"Hay que vender al menos $3572$ libros. La solución publicada ($3571$) es incorrecta: con $3571$ libros la opción B todavía no supera a la A.",
  "full_solution":"Con el contrato A, por cada libro cobra el $10\\%$ de $35$ euros, es decir, $3{,}50$ euros, más el fijo: si vende $n$ libros, $A(n)=25\\,000+3{,}5n$. Con el contrato B cobra el $30\\%$ de $35$, es decir, $10{,}50$ euros por libro y nada fijo: $B(n)=10{,}5n$. Que B sea más beneficiosa significa $B(n)>A(n)$, es decir, $10{,}5n>25\\,000+3{,}5n$. Restando $3{,}5n$: $7n>25\\,000$, y dividiendo entre $7$ (positivo): $n>\\dfrac{25\\,000}{7}=3571{,}428\\ldots$ Como $n$ es un número entero de libros, el primero que cumple la desigualdad estricta es $n=3572$. Comprobación: con $n=3571$, $A=25\\,000+12\\,498{,}5=37\\,498{,}5$ euros y $B=37\\,495{,}5$ euros, así que B es todavía peor (por $3$ euros); con $n=3572$, $A=37\\,502$ euros y $B=37\\,506$ euros, y ahora sí B es mejor. La solución publicada se queda en la parte entera de $3571{,}43$ sin comprobar la desigualdad, y por eso falla.",
  "common_errors":["Truncar el resultado $3571{,}43$ a $3571$: cuando la incógnita cuenta objetos y la desigualdad es estricta, hay que tomar el siguiente entero y comprobarlo.",
                   "Aplicar el $10\\%$ y el $30\\%$ a los $25\\,000$ euros en lugar de al precio del libro."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0604-P5","type":"CONTEXT","objective_ids":["LO-0604-1","LO-0604-3","LO-0604-2"],
  "concept_ids":["C-0604-01","C-0604-03","C-0604-02"],"difficulty":5,
  "statement":"El índice de masa corporal se define como $\\mathrm{IMC}=\\dfrac{\\text{peso en kg}}{(\\text{estatura en m})^{2}}$, y se considera peso normal cuando el IMC está entre $18{,}5$ y $24{,}9$. Para una persona de $1{,}89$ m de estatura: a) halla los pesos exactos que delimitan el peso normal; b) da el intervalo con dos decimales de modo que los dos extremos sigan siendo peso normal, y justifica el redondeo que eliges en cada extremo.",
  "hints":["Plantea la doble desigualdad $18{,}5\\le\\dfrac{p}{1{,}89^{2}}\\le 24{,}9$ y multiplica los tres miembros por $1{,}89^{2}$, que es positivo.",
           "Al redondear un extremo de un intervalo, comprueba siempre que el valor redondeado sigue cumpliendo la condición."],
  "answer":"a) $66{,}08385\\le p\\le 88{,}94529$ kg. b) $[66{,}09;\\ 88{,}94]$: el extremo inferior se redondea hacia arriba y el superior hacia abajo.",
  "full_solution":"a) Si $p$ es el peso en kilogramos, la condición de peso normal es la doble desigualdad $18{,}5\\le\\dfrac{p}{1{,}89^{2}}\\le 24{,}9$. Se calcula $1{,}89^{2}=3{,}5721$ y se multiplican los tres miembros por ese numero, que es positivo y por tanto no altera los sentidos: $18{,}5\\cdot 3{,}5721\\le p\\le 24{,}9\\cdot 3{,}5721$, es decir, $66{,}08385\\le p\\le 88{,}94529$ kilogramos. b) Al pasar a dos decimales hay que elegir el redondeo con cuidado, porque un redondeo automático puede sacar el valor del intervalo. En el extremo superior, la regla habitual redondearía $88{,}94529$ a $88{,}95$, pero $\\dfrac{88{,}95}{3{,}5721}=24{,}9013$, que ya supera $24{,}9$: hay que redondear hacia abajo, a $88{,}94$ kg, cuyo IMC es $24{,}8985$ y sí cumple la condición. En el extremo inferior ocurre lo simétrico: $66{,}08$ daría un IMC de $18{,}4989$, algo por debajo del mínimo, así que hay que redondear hacia arriba, a $66{,}09$ kg, con IMC $18{,}5017$. El intervalo pedido es, por tanto, $[66{,}09;\\ 88{,}94]$, y el peso máximo con dos decimales que sigue considerándose normal es $88{,}94$ kg.",
  "common_errors":["Dividir entre $1{,}89$ en lugar de entre su cuadrado: en la fórmula la estatura aparece elevada al cuadrado.",
                   "Redondear los extremos con la regla automática sin comprobarlos: $88{,}95$ kg parece el redondeo correcto de $88{,}94529$, pero su IMC ya pasa de $24{,}9$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0604-P6","type":"STANDARD","objective_ids":["LO-0604-1","LO-0604-2"],
  "concept_ids":["C-0604-01","C-0604-02"],"difficulty":4,
  "statement":"Resuelve $\\dfrac{x}{2}+\\dfrac{x+1}{7}>x-2$ y expresa la solución en notación de intervalos.",
  "hints":["El mínimo común múltiplo de $2$ y $7$ es $14$.",
           "Al final, al pasar los términos en $x$ a un lado, decide con cuidado el sentido de la desigualdad."],
  "answer":"$x<6$, es decir, $(-\\infty,6)$.",
  "full_solution":"Se multiplican los dos miembros por $14$, el mínimo común múltiplo de $2$ y $7$ (número positivo, el sentido se conserva): $7x+2(x+1)>14(x-2)$. Desarrollando: $7x+2x+2>14x-28$, es decir, $9x+2>14x-28$. Se agrupan los términos: $2+28>14x-9x$, o sea, $30>5x$, y dividiendo entre $5$ queda $6>x$, es decir, $x<6$. En notación de intervalos, $(-\\infty,6)$. Una alternativa es pasar las $x$ al primer miembro: $9x-14x>-28-2$ da $-5x>-30$, y al dividir entre $-5$ (negativo) hay que invertir el sentido, obteniendo igualmente $x<6$: las dos vías coinciden, y la segunda recuerda cuándo se invierte la desigualdad. Comprobación con $x=0$: $0+\\dfrac{1}{7}=0{,}1428>-2$, cierto; con $x=6$ los dos miembros valen $4$, luego el $6$ no pertenece a la solución.",
  "common_errors":["Multiplicar por $14$ y escribir $7x+2x+2>14x-2$, olvidando que el $-2$ del segundo miembro también se multiplica por $14$.",
                   "Llegar a $-5x>-30$ y dividir entre $-5$ sin invertir el sentido, dando $x>6$, que es justo el conjunto contrario."],
  "provenance":"SOURCE_DERIVED"},
],

L5: [
 {"id":"EX-0605-P1","type":"STANDARD","objective_ids":["LO-0605-1","LO-0605-2"],
  "concept_ids":["C-0605-01","C-0605-02"],"difficulty":4,
  "statement":"Resuelve $3x^{2}-10x+7\\ge 0$ y expresa la solución en notación de intervalos.",
  "hints":["Halla primero las raíces con la fórmula general; no son ambas enteras.",
           "El coeficiente principal es positivo, así que la parábola abre hacia arriba."],
  "answer":"$x\\in\\left(-\\infty,1\\right]\\cup\\left[\\dfrac{7}{3},+\\infty\\right)$",
  "full_solution":"Se buscan las raíces de $3x^{2}-10x+7=0$ con la fórmula general: $x=\\dfrac{10\\pm\\sqrt{100-4\\cdot 3\\cdot 7}}{6}=\\dfrac{10\\pm\\sqrt{100-84}}{6}=\\dfrac{10\\pm 4}{6}$, que da $x=\\dfrac{14}{6}=\\dfrac{7}{3}$ y $x=\\dfrac{6}{6}=1$. Como el coeficiente principal $3$ es positivo, la parábola abre hacia arriba: es positiva fuera del intervalo entre las raíces y negativa dentro. Se confirma con números de prueba: en $x=0$, $3\\cdot 0-0+7=7>0$; en $x=2$, $12-20+7=-1<0$; en $x=3$, $27-30+7=4>0$. Como la desigualdad es $\\ge$, las raíces se incluyen. La solución es $x\\in\\left(-\\infty,1\\right]\\cup\\left[\\dfrac{7}{3},+\\infty\\right)$, con corchetes en $1$ y en $\\dfrac{7}{3}$ porque en esos puntos la expresión vale exactamente $0$ y el cero cumple $\\ge 0$.",
  "common_errors":["Dar como solución el intervalo entre las raíces: con coeficiente principal positivo, la expresión es negativa dentro y positiva fuera.",
                   "Dividir mal en la fórmula general y usar $2$ en vez de $2a=6$ como denominador, obteniendo raíces falsas."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0605-P2","type":"STANDARD","objective_ids":["LO-0605-1","LO-0605-2"],
  "concept_ids":["C-0605-01","C-0605-02"],"difficulty":4,
  "statement":"Resuelve $6x^{2}-5x-6<0$ y expresa la solución en notación de intervalos.",
  "hints":["Usa la fórmula general: el discriminante es un cuadrado perfecto.",
           "Con coeficiente principal positivo y desigualdad $<0$, la solución es el intervalo entre las raíces."],
  "answer":"$x\\in\\left(-\\dfrac{2}{3},\\dfrac{3}{2}\\right)$",
  "full_solution":"Las raíces de $6x^{2}-5x-6=0$ son $x=\\dfrac{5\\pm\\sqrt{25+4\\cdot 6\\cdot 6}}{12}=\\dfrac{5\\pm\\sqrt{169}}{12}=\\dfrac{5\\pm 13}{12}$, es decir, $x=\\dfrac{18}{12}=\\dfrac{3}{2}$ y $x=\\dfrac{-8}{12}=-\\dfrac{2}{3}$. El coeficiente principal $6$ es positivo, luego la parábola abre hacia arriba y la expresión es negativa justo entre las dos raíces. Comprobación con un número de prueba interior, $x=0$: $6\\cdot 0-0-6=-6<0$, correcto; y con uno exterior, $x=2$: $24-10-6=8>0$. Como la desigualdad es estricta, los extremos no se incluyen: la solución es $x\\in\\left(-\\dfrac{2}{3},\\dfrac{3}{2}\\right)$. Puede comprobarse también factorizando: $6x^{2}-5x-6=(3x+2)(2x-3)$, producto que es negativo cuando los dos factores tienen signos distintos, lo que ocurre exactamente en ese intervalo.",
  "common_errors":["Ordenar mal los extremos y escribir $\\left(\\dfrac{3}{2},-\\dfrac{2}{3}\\right)$: en un intervalo el extremo menor va siempre primero.",
                   "Tomar el discriminante como $25-144$ por confundir el signo de $c=-6$: aquí $-4ac=-4\\cdot 6\\cdot(-6)=+144$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0605-P3","type":"STANDARD","objective_ids":["LO-0605-1","LO-0605-3"],
  "concept_ids":["C-0605-01","C-0605-02"],"difficulty":4,
  "statement":"Resuelve $-2x^{2}+5x+3>0$. Presta atención al signo del coeficiente principal y expresa la solución en notación de intervalos.",
  "hints":["Puedes multiplicar los dos miembros por $-1$ para que el coeficiente principal sea positivo, pero entonces hay que invertir el sentido de la desigualdad.",
           "Si no cambias el signo, recuerda que una parábola con coeficiente principal negativo abre hacia abajo y es positiva entre sus raíces."],
  "answer":"$x\\in\\left(-\\dfrac{1}{2},3\\right)$",
  "full_solution":"Conviene dejar el coeficiente principal positivo. Multiplicando los dos miembros por $-1$ hay que invertir el sentido: $2x^{2}-5x-3<0$. Las raíces son $x=\\dfrac{5\\pm\\sqrt{25+4\\cdot 2\\cdot 3}}{4}=\\dfrac{5\\pm\\sqrt{49}}{4}=\\dfrac{5\\pm 7}{4}$, es decir, $x=3$ y $x=-\\dfrac{1}{2}$. Con coeficiente principal positivo y desigualdad $<0$, la solución es el intervalo entre las raíces: $x\\in\\left(-\\dfrac{1}{2},3\\right)$. El mismo resultado se obtiene sin cambiar el signo: la parábola $y=-2x^{2}+5x+3$ abre hacia abajo (coeficiente $-2$), así que está por encima del eje $X$ precisamente entre sus dos raíces, que son las mismas. Comprobación en la expresión original con $x=0$: $3>0$, cierto; con $x=4$: $-32+20+3=-9$, que no es positivo, así que el $4$ queda fuera, como corresponde.",
  "common_errors":["Multiplicar por $-1$ y no invertir el sentido de la desigualdad, lo que da el conjunto complementario.",
                   "Aplicar la regla 'solución fuera de las raíces' sin mirar el signo del coeficiente principal: con la parábola abierta hacia abajo la expresión es positiva dentro."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0605-P4","type":"REASONING","objective_ids":["LO-0605-1","LO-0605-2","LO-0605-3"],
  "concept_ids":["C-0605-02","C-0605-01"],"difficulty":5,
  "statement":"La expresión $x^{2}-4x+4$ tiene una raíz doble. Resuelve las cuatro inecuaciones $x^{2}-4x+4>0$, $x^{2}-4x+4\\ge 0$, $x^{2}-4x+4<0$ y $x^{2}-4x+4\\le 0$, y explica con la parábola por qué salen soluciones tan distintas.",
  "hints":["Factoriza: $x^{2}-4x+4=(x-2)^{2}$, y piensa qué signos puede tomar un cuadrado.",
           "La parábola es tangente al eje $X$ en $x=2$: solo lo toca en un punto y el resto está por encima."],
  "answer":"$>0$: $\\mathbb{R}\\setminus\\{2\\}$. $\\ge 0$: $\\mathbb{R}$. $<0$: $\\varnothing$. $\\le 0$: solo $x=2$.",
  "full_solution":"La expresión es un cuadrado perfecto: $x^{2}-4x+4=(x-2)^{2}$, con raíz doble $x=2$ (su discriminante es $16-16=0$). Un cuadrado de un número real nunca es negativo, y vale $0$ únicamente cuando lo que se eleva al cuadrado es $0$, es decir, cuando $x=2$. Con eso se resuelven las cuatro inecuaciones. Para $(x-2)^{2}>0$ hay que excluir el único punto donde vale cero: la solución es todos los reales menos el $2$, $\\mathbb{R}\\setminus\\{2\\}$, que en intervalos se escribe $(-\\infty,2)\\cup(2,+\\infty)$. Para $(x-2)^{2}\\ge 0$ se cumple siempre, incluido el $2$: la solución es $\\mathbb{R}$. Para $(x-2)^{2}<0$ no hay ningún número real que lo cumpla: la solución es $\\varnothing$. Y para $(x-2)^{2}\\le 0$ solo sirve el valor que la anula: la solución es el único punto $x=2$. Geométricamente, la parábola $y=(x-2)^{2}$ abre hacia arriba y es tangente al eje $X$ en $x=2$: toca el eje en ese punto y está estrictamente por encima en todos los demás. Por eso la raíz doble produce estos cuatro casos extremos, en los que la solución es todo, casi todo, nada o un solo punto.",
  "common_errors":["Dar $(-\\infty,2)\\cup(2,+\\infty)$ también para $\\ge 0$: con la desigualdad no estricta el punto de tangencia sí se incluye, y la solución es todo $\\mathbb{R}$.",
                   "Responder $x=2$ para $(x-2)^{2}<0$ confundiendo 'menor o igual' con 'menor': con desigualdad estricta no hay solución."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0605-P5","type":"REASONING","objective_ids":["LO-0605-2","LO-0605-3"],
  "concept_ids":["C-0605-01","C-0605-02"],"difficulty":3,
  "statement":"Resuelve, razonando con la parábola o con el signo de un cuadrado: a) $x^{2}<9$; b) $x^{2}<-9$; c) $x^{2}+16\\ge 0$.",
  "hints":["En a) pasa el $9$ al primer miembro y factoriza como diferencia de cuadrados.",
           "En b) y c) piensa qué valores puede tomar $x^{2}$ para cualquier número real."],
  "answer":"a) $x\\in(-3,3)$. b) No tiene solución, $\\varnothing$. c) Todos los reales, $\\mathbb{R}$.",
  "full_solution":"a) Se pasa todo a un miembro: $x^{2}-9<0$, es decir, $(x-3)(x+3)<0$. El producto de dos factores es negativo cuando tienen signos distintos, lo que ocurre entre las raíces $-3$ y $3$. La solución es $x\\in(-3,3)$, con extremos abiertos porque en $-3$ y $3$ la expresión vale $0$ y no cumple $<0$. Un error típico es escribir $x<3$ a secas 'extrayendo la raíz': eso deja fuera la condición $x>-3$, y por ejemplo $x=-5$ cumpliría $x<3$ pero $(-5)^{2}=25$ no es menor que $9$. b) Para cualquier número real, $x^{2}\\ge 0$, así que nunca puede ser menor que $-9$: la inecuación no tiene solución, $\\varnothing$. c) De nuevo $x^{2}\\ge 0$, luego $x^{2}+16\\ge 16>0$ para todo $x$: la desigualdad se cumple siempre y la solución es $\\mathbb{R}$. En los dos últimos apartados la parábola correspondiente no corta al eje $X$ (discriminantes negativos), y por eso la expresión mantiene el mismo signo en todo el dominio.",
  "common_errors":["Resolver $x^{2}<9$ como $x<3$, olvidando los valores negativos: la solución correcta es $-3<x<3$.",
                   "Dar $x=\\pm 3$ como solución de una inecuación: las raíces son las fronteras del conjunto solución, no el conjunto solución."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    xs = [F(k, 4) for k in range(-80, 81)]
    # ---------- L04 P1
    f = lambda x: F(x-1, 2) - F(x-4, 3)
    for x in xs:
        assert (f(x) < 1) == (x < 1), x
    for x in xs:
        assert 6*f(x) == 3*(x-1) - 2*(x-4) == x + 5
    assert f(0) == F(5, 6) and ic(float(f(0)), 0.8333333333, rel_tol=1e-9)
    assert f(2) == F(7, 6) and ic(float(f(2)), 1.1666666667, rel_tol=1e-9)
    # ---------- L04 P2
    lhs = lambda x: F(5*x-2, 3) - F(x-8, 4)
    rhs = lambda x: F(x+14, 2) - 2
    for x in xs:
        assert (lhs(x) > rhs(x)) == (x > 4), x
        assert 12*lhs(x) == 4*(5*x-2) - 3*(x-8) == 17*x + 16
        assert 12*rhs(x) == 6*(x+14) - 24 == 6*x + 60
    assert lhs(5) == F(23, 3) + F(3, 4) == F(101, 12) and rhs(5) == F(15, 2)
    assert round(float(lhs(5)), 5) == 8.41667 and float(rhs(5)) == 7.5
    assert lhs(4) == 7 == rhs(4)
    # ---------- L04 P3
    for x in xs:
        a_l, a_r = 12*(x+2)+5, 3*(4*x+1)+3
        assert a_l == 12*x + 29 and a_r == 12*x + 6
        assert not (a_l < a_r)                     # sin solucion
        b_l, b_r = 5*(x-2)-4*(2*x+1), -3*x+3
        assert b_l == -3*x - 14 and b_r == -3*x + 3
        assert b_l < b_r                           # todo R
    # ---------- L04 P4 editorial
    A = lambda n: 25000 + F(35, 10)*n
    B = lambda n: F(105, 10)*n
    assert F(35, 100)*10 == F(35, 10) and F(30, 100)*35 == F(105, 10)
    assert F(25000, 7) == F(25000, 7)
    assert ic(25000/7, 3571.4285714285716, rel_tol=1e-12)
    assert not (B(3571) > A(3571)) and B(3572) > A(3572)
    assert A(3571) == F(374985, 10) and B(3571) == F(374955, 10)
    assert float(A(3571)) == 37498.5 and float(B(3571)) == 37495.5
    assert A(3572) == 37502 and B(3572) == 37506
    assert float(A(3571) - B(3571)) == 3.0
    # ---------- L04 P5 IMC
    h2 = 1.89**2; assert ic(h2, 3.5721, rel_tol=1e-12)
    lo, hi = 18.5*h2, 24.9*h2
    assert round(lo, 5) == 66.08385 and round(hi, 5) == 88.94529, (lo, hi)
    assert round(88.95/h2, 4) == 24.9013 and 88.95/h2 > 24.9
    assert round(88.94/h2, 4) == 24.8985 and 18.5 <= 88.94/h2 <= 24.9
    assert round(66.08/h2, 4) == 18.4989 and 66.08/h2 < 18.5
    assert round(66.09/h2, 4) == 18.5017 and 18.5 <= 66.09/h2 <= 24.9
    # ---------- L04 P6
    g = lambda x: F(x, 2) + F(x+1, 7)
    for x in xs:
        assert (g(x) > x - 2) == (x < 6), x
        assert 14*g(x) == 7*x + 2*(x+1) == 9*x + 2
        assert 14*(x-2) == 14*x - 28
    assert g(0) == F(1, 7) and round(float(g(0)), 4) == 0.1429
    assert g(6) == 4 == 6 - 2
    # ---------- L05 P1
    q1 = lambda x: 3*x*x - 10*x + 7
    assert 100 - 4*3*7 == 16 and math.isqrt(16) == 4
    assert F(10+4, 6) == F(7, 3) and F(10-4, 6) == 1
    assert q1(1) == 0 and q1(F(7, 3)) == 0
    for x in xs:
        assert (q1(x) >= 0) == (x <= 1 or x >= F(7, 3)), x
    assert q1(0) == 7 and q1(2) == -1 and q1(3) == 4
    # ---------- L05 P2
    q2 = lambda x: 6*x*x - 5*x - 6
    assert 25 + 4*6*6 == 169 and math.isqrt(169) == 13
    assert F(5+13, 12) == F(3, 2) and F(5-13, 12) == F(-2, 3)
    for x in xs:
        assert (q2(x) < 0) == (F(-2, 3) < x < F(3, 2)), x
        assert q2(x) == (3*x+2)*(2*x-3)
    assert q2(0) == -6 and q2(2) == 8
    # ---------- L05 P3
    q3 = lambda x: -2*x*x + 5*x + 3
    assert 25 + 4*2*3 == 49 and math.isqrt(49) == 7
    assert F(5+7, 4) == 3 and F(5-7, 4) == F(-1, 2)
    for x in xs:
        assert (q3(x) > 0) == (F(-1, 2) < x < 3), x
        assert (q3(x) > 0) == (2*x*x - 5*x - 3 < 0)
    assert q3(0) == 3 and q3(4) == -9
    # ---------- L05 P4 raiz doble
    q4 = lambda x: x*x - 4*x + 4
    assert 16 - 4*4 == 0
    for x in xs:
        assert q4(x) == (x-2)**2 >= 0
        assert (q4(x) > 0) == (x != 2)
        assert q4(x) >= 0
        assert not (q4(x) < 0)
        assert (q4(x) <= 0) == (x == 2)
    assert q4(2) == 0
    # ---------- L05 P5
    for x in xs:
        assert (x*x < 9) == (-3 < x < 3), x
        assert (x*x - 9 < 0) == ((x-3)*(x+3) < 0)
        assert not (x*x < -9)
        assert x*x + 16 >= 16
    assert F(-5)**2 == 25 and not (25 < 9) and (F(-5) < 3)
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
