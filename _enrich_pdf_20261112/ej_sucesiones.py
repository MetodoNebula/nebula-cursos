# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'ejercicios_de_sucesiones_resueltos.pdf' y
'hoja-08-sucesiones-pend-3eso.pdf' para eso_matematicas__mat_sucesiones.json"""
import math
from fractions import Fraction as F

L1 = "01_Sucesiones_y_término_general.json"
L2 = "02_Progresiones_aritméticas.json"
L3 = "03_Progresiones_geométricas.json"
L4 = "04_Comportamiento_de_sucesiones_monotonía_y_acotación.json"
L6 = "06_Límite_de_sucesiones_y_número_e.json"

EX = {
L1: [
 {"id":"EX-7B01-P1","type":"STANDARD","objective_ids":["LO-7B01-2"],
  "concept_ids":["C-7B01-2","C-7B01-1"],"difficulty":3,
  "statement":"Escribe los ocho primeros términos de la sucesión definida por $a_1=2$, $a_2=3$ y $a_n=a_{n-1}+a_{n-2}$ para $n\\ge 3$. Compárala con la sucesión de Fibonacci ($1,1,2,3,5,\\dots$): ¿qué tienen en común y en qué se diferencian?",
  "hints":["Cada término nuevo es la suma de los dos anteriores; necesitas tener los dos de antes antes de calcular el siguiente.",
           "Fíjate en que la regla de recurrencia es la misma en las dos sucesiones; lo que cambia son los dos primeros términos."],
  "answer":"$2,\\ 3,\\ 5,\\ 8,\\ 13,\\ 21,\\ 34,\\ 55$. Comparten la misma regla de recurrencia que Fibonacci, pero arrancan de otros valores iniciales.",
  "full_solution":"Se aplica la regla paso a paso. Los dos primeros están dados: $a_1=2$ y $a_2=3$. Después, $a_3=a_2+a_1=3+2=5$; $a_4=a_3+a_2=5+3=8$; $a_5=a_4+a_3=8+5=13$; $a_6=a_5+a_4=13+8=21$; $a_7=a_6+a_5=21+13=34$; $a_8=a_7+a_6=34+21=55$. La sucesión es, por tanto, $2,3,5,8,13,21,34,55$. Comparada con Fibonacci ($1,1,2,3,5,8,13,21,\\dots$), la regla de formación es idéntica, $a_n=a_{n-1}+a_{n-2}$, pero los valores iniciales son distintos. Curiosamente, a partir del tercer término esta sucesión coincide con Fibonacci desplazada: $5,8,13,21,34,55$ son términos de Fibonacci, porque $2$ y $3$ ya eran términos consecutivos de Fibonacci. Esto muestra que una regla de recurrencia sola no determina la sucesión: hacen falta también los valores iniciales.",
  "common_errors":["Intentar calcular $a_8$ sustituyendo $n=8$ en alguna fórmula: una sucesión recurrente obliga a recorrer todos los términos anteriores.",
                   "Sumar el término anterior y la posición ($a_n=a_{n-1}+n$) en lugar de los dos términos anteriores."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B01-P2","type":"STANDARD","objective_ids":["LO-7B01-3","LO-7B01-2"],
  "concept_ids":["C-7B01-1"],"difficulty":4,
  "statement":"Halla un término general para cada sucesión: a) $\\dfrac{1}{2},\\ \\dfrac{4}{3},\\ \\dfrac{9}{4},\\ \\dfrac{16}{5},\\dots$; b) $\\dfrac{2}{4},\\ \\dfrac{5}{6},\\ \\dfrac{10}{8},\\ \\dfrac{17}{10},\\dots$ (no simplifiques las fracciones: la pista está en los numeradores y denominadores tal como aparecen).",
  "hints":["Estudia por separado el patrón de los numeradores y el de los denominadores.",
           "En b) los numeradores son $2,5,10,17$: mira cuánto les falta a $1,4,9,16$."],
  "answer":"a) $a_n=\\dfrac{n^{2}}{n+1}$. b) $a_n=\\dfrac{n^{2}+1}{2n+2}$.",
  "full_solution":"a) Los numeradores son $1,4,9,16$, que son los cuadrados $1^{2},2^{2},3^{2},4^{2}$: el numerador es $n^{2}$. Los denominadores son $2,3,4,5$, es decir, la posición más uno: $n+1$. Por tanto $a_n=\\dfrac{n^{2}}{n+1}$. Comprobación: $a_1=\\dfrac{1}{2}$, $a_2=\\dfrac{4}{3}$, $a_3=\\dfrac{9}{4}$, $a_4=\\dfrac{16}{5}$, como se pedía. b) Los numeradores son $2,5,10,17$. Restando uno a cada uno queda $1,4,9,16$, de nuevo los cuadrados, así que el numerador es $n^{2}+1$. Los denominadores son $4,6,8,10$, que van de dos en dos empezando en $4$: son $2n+2$. Luego $a_n=\\dfrac{n^{2}+1}{2n+2}$. Comprobación: $a_1=\\dfrac{2}{4}$, $a_2=\\dfrac{5}{6}$, $a_3=\\dfrac{10}{8}$ y $a_4=\\dfrac{17}{10}$, exactamente los términos dados.",
  "common_errors":["Simplificar primero las fracciones ($\\dfrac{2}{4}=\\dfrac{1}{2}$, $\\dfrac{10}{8}=\\dfrac{5}{4}$) y perder así el patrón de los denominadores.",
                   "Dar los denominadores de b) como $2n$ en lugar de $2n+2$: para $n=1$ eso daría $2$, no $4$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B01-P3","type":"REASONING","objective_ids":["LO-7B01-1","LO-7B01-2"],
  "concept_ids":["C-7B01-1"],"difficulty":5,
  "statement":"Se tienen tres sucesiones: $\\{a_n\\}=7,\\,13,\\,19,\\,25,\\dots$; $b_n=4n+3$; $c_n=n^{2}+2$. Decide a cuál o cuáles de ellas pertenece cada uno de los números $531$, $27$ y $1201$, justificando cada respuesta.",
  "hints":["Halla primero el término general de la primera sucesión; va de $6$ en $6$ empezando en $7$.",
           "Un número pertenece a la sucesión si al resolver la ecuación correspondiente sale una posición $n$ natural."],
  "answer":"$531$ pertenece a $\\{b_n\\}$ (posición $132$) y a $\\{c_n\\}$ (posición $23$). $27$ pertenece a $\\{b_n\\}$ ($n=6$) y a $\\{c_n\\}$ ($n=5$). $1201$ pertenece solo a $\\{a_n\\}$ ($n=200$).",
  "full_solution":"La primera sucesión avanza de $6$ en $6$ desde $7$, así que su término general es $a_n=7+6(n-1)=6n+1$. Ahora se comprueba cada número resolviendo las tres ecuaciones y aceptando solo soluciones naturales. Para $531$: $6n+1=531$ da $n=\\dfrac{530}{6}=88{,}33\\ldots$, que no es natural, así que no pertenece a $\\{a_n\\}$; $4n+3=531$ da $n=\\dfrac{528}{4}=132$, natural, así que sí pertenece a $\\{b_n\\}$; $n^{2}+2=531$ da $n^{2}=529$ y $n=23$, natural, así que también pertenece a $\\{c_n\\}$. Para $27$: $6n+1=27$ da $n=\\dfrac{26}{6}$, no natural; $4n+3=27$ da $n=6$, sí; $n^{2}+2=27$ da $n^{2}=25$ y $n=5$, sí. Para $1201$: $6n+1=1201$ da $n=200$, sí; $4n+3=1201$ da $n=\\dfrac{1198}{4}=299{,}5$, no; $n^{2}+2=1201$ da $n^{2}=1199$, y como $34^{2}=1156$ y $35^{2}=1225$, no hay ningún natural cuyo cuadrado sea $1199$, así que no pertenece. En resumen, pertenecer a una sucesión no es parecerse a sus términos: es que la posición que resulta sea un número natural.",
  "common_errors":["Aceptar como válida una posición decimal (por ejemplo $n=299{,}5$): las posiciones de una sucesión son números naturales.",
                   "Concluir que $1199$ es un cuadrado porque su raíz, $34{,}6$, 'está cerca' de un entero: hay que comprobar con los cuadrados exactos de alrededor."],
  "provenance":"SOURCE_DERIVED"},
],

L2: [
 {"id":"EX-7B02-P1","type":"STANDARD","objective_ids":["LO-7B02-2","LO-7B02-1"],
  "concept_ids":["C-7B02-1"],"difficulty":4,
  "statement":"De una progresión aritmética se sabe que $a_4=12$ y $a_7=6$. Halla la diferencia $d$, el primer término $a_1$, el término general y el valor de $a_{175}$.",
  "hints":["Entre $a_4$ y $a_7$ hay tres saltos de diferencia, no siete.",
           "La diferencia puede ser negativa: aquí la progresión decrece."],
  "answer":"$d=-2$, $a_1=18$, $a_n=20-2n$ y $a_{175}=-330$.",
  "full_solution":"De $a_4$ a $a_7$ se dan $7-4=3$ saltos, así que $a_7=a_4+3d$. Sustituyendo: $6=12+3d$, de donde $3d=-6$ y $d=-2$. La diferencia es negativa, lo que indica que la progresión es decreciente. Para el primer término se retrocede tres saltos desde $a_4$: $a_1=a_4-3d=12-3\\cdot(-2)=12+6=18$. El término general es $a_n=a_1+(n-1)d=18+(n-1)(-2)=18-2n+2=20-2n$. Comprobación: $a_4=20-8=12$ y $a_7=20-14=6$, correcto. Finalmente, $a_{175}=20-2\\cdot 175=20-350=-330$.",
  "common_errors":["Usar $a_7=a_4+7d$ y obtener $d=-\\dfrac{6}{7}$: el número de saltos entre dos términos es la diferencia de sus posiciones.",
                   "Escribir $a_n=a_1+nd$ en lugar de $a_n=a_1+(n-1)d$, lo que desplaza toda la progresión un lugar."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B02-P2","type":"CONTEXT","objective_ids":["LO-7B02-2","LO-7B02-3"],
  "concept_ids":["C-7B02-1","C-7B02-2"],"difficulty":4,
  "statement":"Los cuatro lados de un cuadrilátero están en progresión aritmética de diferencia $6$ cm. Si el perímetro mide $52$ cm, calcula la longitud de cada lado.",
  "hints":["Llama $a$ al lado menor y escribe los otros tres en función de $a$ y de la diferencia.",
           "El perímetro es la suma de los cuatro lados."],
  "answer":"$4$ cm, $10$ cm, $16$ cm y $22$ cm.",
  "full_solution":"Si el lado menor mide $a$, los cuatro lados son $a$, $a+6$, $a+12$ y $a+18$. El perímetro es su suma: $a+(a+6)+(a+12)+(a+18)=4a+36$. Igualando al dato, $4a+36=52$, de donde $4a=16$ y $a=4$ cm. Los lados son entonces $4$, $4+6=10$, $4+12=16$ y $4+18=22$ centímetros. Comprobación: $4+10+16+22=52$ cm, y la diferencia entre lados consecutivos es $6$ en los tres casos. (También podía usarse la fórmula de la suma: $S_4=\\dfrac{4}{2}(a_1+a_4)=2(a+a+18)=4a+36$, el mismo resultado.)",
  "common_errors":["Plantear los lados como $a$, $a+6$, $a+6$, $a+6$: en una progresión aritmética cada lado supera al anterior en $6$, así que los incrementos se acumulan.",
                   "Dividir directamente $52$ entre $4$ y dar $13$ cm para todos los lados, lo que ignora que los lados son distintos."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B02-P3","type":"REASONING","objective_ids":["LO-7B02-3","LO-7B02-2"],
  "concept_ids":["C-7B02-2","C-7B02-1"],"difficulty":5,
  "statement":"¿Cuántos términos hay que sumar de la progresión aritmética $7,\\ 10,\\ 13,\\dots$ para obtener $282$?",
  "hints":["Escribe $a_n$ en función de $n$ y sustitúyelo en $S_n=\\dfrac{n(a_1+a_n)}{2}$.",
           "Obtendrás una ecuación de segundo grado en $n$: descarta la solución que no sea un natural."],
  "answer":"$n=12$ términos.",
  "full_solution":"El primer término es $a_1=7$ y la diferencia $d=3$, así que $a_n=7+3(n-1)=3n+4$. La suma de los $n$ primeros términos es $S_n=\\dfrac{n(a_1+a_n)}{2}=\\dfrac{n(7+3n+4)}{2}=\\dfrac{n(3n+11)}{2}$. Igualando a $282$: $\\dfrac{n(3n+11)}{2}=282$, es decir, $3n^{2}+11n=564$, o bien $3n^{2}+11n-564=0$. Aplicando la fórmula general, $n=\\dfrac{-11\\pm\\sqrt{121+4\\cdot 3\\cdot 564}}{6}=\\dfrac{-11\\pm\\sqrt{6889}}{6}=\\dfrac{-11\\pm 83}{6}$. Las dos soluciones son $n=\\dfrac{72}{6}=12$ y $n=\\dfrac{-94}{6}=-15{,}67$. La segunda se descarta porque el número de términos sumados tiene que ser un natural. Comprobación: $a_{12}=3\\cdot 12+4=40$ y $S_{12}=\\dfrac{12(7+40)}{2}=6\\cdot 47=282$, correcto.",
  "common_errors":["Quedarse con la solución negativa o dar las dos como válidas: $n$ cuenta términos, así que debe ser un natural positivo.",
                   "Confundir en la fórmula $S_n=\\dfrac{n(a_1+a_n)}{2}$ el número de términos $n$ con el valor del último término $a_n$, y escribir $\\dfrac{n(7+n)}{2}$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B02-P4","type":"REASONING","objective_ids":["LO-7B02-3","LO-7B02-2"],
  "concept_ids":["C-7B02-2","C-7B02-1"],"difficulty":4,
  "statement":"En una progresión aritmética, la suma de los diez primeros términos vale $530$ y el primer término es $8$. Calcula el término décimo y la diferencia.",
  "hints":["Usa $S_{10}=\\dfrac{10(a_1+a_{10})}{2}$ y despeja $a_{10}$.",
           "Después, de $a_{10}=a_1+9d$ sale la diferencia."],
  "answer":"$a_{10}=98$ y $d=10$.",
  "full_solution":"La fórmula de la suma da $S_{10}=\\dfrac{10(a_1+a_{10})}{2}=5(a_1+a_{10})$. Sustituyendo los datos: $530=5(8+a_{10})$, de donde $8+a_{10}=\\dfrac{530}{5}=106$ y por tanto $a_{10}=106-8=98$. Para la diferencia se usa que de $a_1$ a $a_{10}$ hay nueve saltos: $a_{10}=a_1+9d$, es decir, $98=8+9d$, luego $9d=90$ y $d=10$. Comprobación: la progresión es $8,18,28,\\dots,98$, su suma es $\\dfrac{10(8+98)}{2}=5\\cdot 106=530$, como decía el enunciado.",
  "common_errors":["Dividir $530$ entre $10$ y tomar $53$ como término décimo: $53$ es la media de los términos, no el último.",
                   "Calcular la diferencia como $\\dfrac{98-8}{10}=9$: entre el primero y el décimo hay nueve intervalos, no diez."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B02-P5","type":"STANDARD","objective_ids":["LO-7B02-3"],
  "concept_ids":["C-7B02-2","C-7B02-1"],"difficulty":4,
  "statement":"a) Calcula la suma $5+10+15+\\cdots+95+100$. b) Calcula la suma de los $23$ primeros términos de la progresión aritmética $6,\\ \\dfrac{19}{3},\\ \\dfrac{20}{3},\\dots$, dando el resultado como fracción.",
  "hints":["En a) averigua primero cuántos términos hay: son los múltiplos de $5$ desde $5$ hasta $100$.",
           "En b) la diferencia es $\\dfrac{19}{3}-6=\\dfrac{1}{3}$."],
  "answer":"a) $1050$. b) $\\dfrac{667}{3}\\approx 222{,}33$.",
  "full_solution":"a) Los términos son los múltiplos de $5$ desde $5$ hasta $100$, así que hay $\\dfrac{100}{5}=20$ términos, con $a_1=5$ y $a_{20}=100$. La suma es $S_{20}=\\dfrac{20(5+100)}{2}=10\\cdot 105=1050$. b) La diferencia es $d=\\dfrac{19}{3}-6=\\dfrac{19-18}{3}=\\dfrac{1}{3}$, y se confirma con el tercer término: $\\dfrac{19}{3}+\\dfrac{1}{3}=\\dfrac{20}{3}$. El término $23$ es $a_{23}=6+22\\cdot\\dfrac{1}{3}=6+\\dfrac{22}{3}=\\dfrac{18+22}{3}=\\dfrac{40}{3}$. Entonces $S_{23}=\\dfrac{23\\left(6+\\dfrac{40}{3}\\right)}{2}=\\dfrac{23\\cdot\\dfrac{58}{3}}{2}=\\dfrac{1334}{6}=\\dfrac{667}{3}$, que en decimal es $222{,}3\\overline{3}$.",
  "common_errors":["En a) contar $100$ términos (o $96$) en lugar de $20$: hay que dividir entre la diferencia, porque los términos van de $5$ en $5$.",
                   "En b) tomar $d=\\dfrac{19}{3}$ en vez de restar: la diferencia es lo que hay que sumar al término anterior, no el término siguiente."],
  "provenance":"SOURCE_DERIVED"},
],

L3: [
 {"id":"EX-7B03-P1","type":"STANDARD","objective_ids":["LO-7B03-2","LO-7B03-1"],
  "concept_ids":["C-7B03-1"],"difficulty":4,
  "statement":"El primer término de una progresión geométrica es $\\dfrac{27}{4}$ y el cuarto es $-\\dfrac{1}{4}$. Halla la razón y el término general.",
  "hints":["De $a_1$ a $a_4$ hay tres saltos: $a_4=a_1\\cdot r^{3}$.",
           "Un cubo negativo tiene raíz cúbica negativa, y la raíz cúbica es única."],
  "answer":"$r=-\\dfrac{1}{3}$ y $a_n=\\dfrac{27}{4}\\left(-\\dfrac{1}{3}\\right)^{n-1}$.",
  "full_solution":"En una progresión geométrica, $a_4=a_1\\cdot r^{3}$. Sustituyendo los datos: $-\\dfrac{1}{4}=\\dfrac{27}{4}\\cdot r^{3}$, de donde $r^{3}=-\\dfrac{1}{4}\\cdot\\dfrac{4}{27}=-\\dfrac{1}{27}$. La raíz cúbica de un número negativo es negativa y única, así que $r=\\sqrt[3]{-\\dfrac{1}{27}}=-\\dfrac{1}{3}$. El término general es $a_n=a_1r^{n-1}=\\dfrac{27}{4}\\left(-\\dfrac{1}{3}\\right)^{n-1}$. Comprobación: $a_2=\\dfrac{27}{4}\\cdot\\left(-\\dfrac{1}{3}\\right)=-\\dfrac{9}{4}$, $a_3=\\dfrac{3}{4}$ y $a_4=-\\dfrac{1}{4}$, el dato de partida. Observa que los signos alternan, señal inequívoca de razón negativa.",
  "common_errors":["Hallar la razón restando o dividiendo términos no consecutivos sin tener en cuenta el número de saltos: de $a_1$ a $a_4$ hay tres, así que lo que se obtiene es $r^{3}$, no $r$.",
                   "Dar $r=\\dfrac{1}{3}$ y escribir el signo 'a mano': con razón positiva todos los términos tendrían el signo de $a_1$, y aquí hay términos negativos."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B03-P2","type":"REASONING","objective_ids":["LO-7B03-1","LO-7B03-2"],
  "concept_ids":["C-7B03-1"],"difficulty":5,
  "statement":"De una progresión geométrica se sabe que $a_3=12$ y $a_7=192$. Calcula su razón y su décimo término. Atención: hay más de una progresión posible.",
  "hints":["De $a_3$ a $a_7$ hay cuatro saltos: $a_7=a_3\\cdot r^{4}$.",
           "Una potencia de exponente par tiene dos raíces reales opuestas."],
  "answer":"$r=2$ o $r=-2$; en ambos casos $a_1=3$, y $a_{10}=1536$ si $r=2$, o $a_{10}=-1536$ si $r=-2$.",
  "full_solution":"De $a_3$ a $a_7$ hay $7-3=4$ saltos, luego $a_7=a_3\\cdot r^{4}$: $192=12\\,r^{4}$, de donde $r^{4}=\\dfrac{192}{12}=16$. Como el exponente es par, hay dos razones reales posibles: $r=2$ y $r=-2$, porque $2^{4}=16$ y $(-2)^{4}=16$. El primer término se obtiene retrocediendo dos saltos desde $a_3$: $a_1=\\dfrac{a_3}{r^{2}}=\\dfrac{12}{4}=3$ en los dos casos, porque $r^{2}=4$ tanto con $2$ como con $-2$. Para el décimo término, $a_{10}=a_1r^{9}$. Si $r=2$: $a_{10}=3\\cdot 2^{9}=3\\cdot 512=1536$. Si $r=-2$: $a_{10}=3\\cdot(-2)^{9}=3\\cdot(-512)=-1536$, porque el exponente $9$ es impar. Comprobación con $r=-2$: la progresión es $3,-6,12,-24,48,-96,192,\\dots$, y efectivamente $a_3=12$ y $a_7=192$. Hay por tanto dos soluciones válidas, y conviene darlas las dos.",
  "common_errors":["Quedarse solo con $r=2$: al despejar de una potencia de exponente par aparecen dos razones opuestas, y las dos generan progresiones que cumplen los datos.",
                   "Suponer que con $r=-2$ el término $a_7$ sería negativo: el exponente que interviene es $r^{6}$, par, así que $a_7$ sale positivo."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B03-P3","type":"CONTEXT","objective_ids":["LO-7B03-3","LO-7B03-2"],
  "concept_ids":["C-7B03-1","C-7B03-2"],"difficulty":4,
  "statement":"En un cultivo hay inicialmente $10$ bacterias que se reproducen por bipartición cada $30$ minutos. ¿Cuántas bacterias habrá al cabo de $12$ horas?",
  "hints":["Cuenta cuántos periodos de $30$ minutos caben en $12$ horas.",
           "Cada periodo multiplica la población por $2$."],
  "answer":"$10\\cdot 2^{24}=167\\,772\\,160$ bacterias.",
  "full_solution":"En una hora hay dos periodos de $30$ minutos, así que en $12$ horas hay $12\\cdot 2=24$ periodos. Cada bipartición duplica la población, de modo que la población se multiplica por $2$ veinticuatro veces: $P=10\\cdot 2^{24}$. Calculando, $2^{10}=1024$, $2^{20}=1024^{2}=1\\,048\\,576$ y $2^{24}=2^{20}\\cdot 2^{4}=1\\,048\\,576\\cdot 16=16\\,777\\,216$. Por tanto $P=10\\cdot 16\\,777\\,216=167\\,772\\,160$ bacterias, es decir, del orden de $1{,}7\\cdot 10^{8}$. Si se modela como progresión geométrica con $a_1=10$ (la población inicial, en el instante $0$), la población tras $24$ biparticiones es el término $a_{25}=10\\cdot 2^{24}$: hay que tener cuidado con si el índice cuenta periodos transcurridos o lugares de la progresión.",
  "common_errors":["Usar $12$ como número de duplicaciones en lugar de $24$: el periodo es de media hora, así que hay dos por hora.",
                   "Multiplicar por $24$ en lugar de duplicar $24$ veces, dando $240$ bacterias: el crecimiento es multiplicativo, no aditivo."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B03-P4","type":"STANDARD","objective_ids":["LO-7B03-2"],
  "concept_ids":["C-7B03-1","C-7B03-2"],"difficulty":4,
  "statement":"En una progresión geométrica, el segundo término es $4$ y el quinto es $32$. Halla la razón, el primer término y la suma de los diez primeros términos.",
  "hints":["De $a_2$ a $a_5$ hay tres saltos, así que lo que se obtiene al dividir es $r^{3}$.",
           "Usa $S_n=a_1\\dfrac{r^{n}-1}{r-1}$, válida cuando $r\\neq 1$."],
  "answer":"$r=2$, $a_1=2$ y $S_{10}=2046$.",
  "full_solution":"De $a_2$ a $a_5$ hay $5-2=3$ saltos, luego $a_5=a_2\\cdot r^{3}$: $32=4r^{3}$, de donde $r^{3}=8$ y, como la raíz cúbica es única, $r=2$. El primer término es $a_1=\\dfrac{a_2}{r}=\\dfrac{4}{2}=2$. Para la suma, al ser $r=2\\neq 1$, se puede usar $S_{10}=a_1\\dfrac{r^{10}-1}{r-1}=2\\cdot\\dfrac{2^{10}-1}{2-1}=2\\cdot\\dfrac{1024-1}{1}=2\\cdot 1023=2046$. Comprobación sumando directamente: $2+4+8+16+32+64+128+256+512+1024=2046$, correcto.",
  "common_errors":["Dividir $32$ entre $4$ y tomar $8$ como razón: ese cociente es $r^{3}$, porque entre el segundo y el quinto término hay tres saltos.",
                   "Aplicar la fórmula de la suma con $n=10$ pero poniendo $a_2$ en lugar de $a_1$, lo que da un término de más y otro de menos."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B03-P5","type":"STANDARD","objective_ids":["LO-7B03-1","LO-7B03-2"],
  "concept_ids":["C-7B03-2","C-7B03-1"],"difficulty":3,
  "statement":"Halla la suma de los ocho primeros términos de la progresión geométrica $\\dfrac{1}{4},\\ \\dfrac{1}{2},\\ 1,\\dots$, dando el resultado como fracción y como decimal.",
  "hints":["Halla la razón dividiendo un término entre el anterior, no restándolos.",
           "Como $r>1$, la suma crece: conviene usar $S_n=a_1\\dfrac{r^{n}-1}{r-1}$."],
  "answer":"$S_8=\\dfrac{255}{4}=63{,}75$.",
  "full_solution":"La razón se obtiene dividiendo: $r=\\dfrac{1/2}{1/4}=2$, y se confirma con el siguiente par, $\\dfrac{1}{1/2}=2$. Con $a_1=\\dfrac{1}{4}$ y $r=2$, la suma de los ocho primeros términos es $S_8=a_1\\dfrac{r^{8}-1}{r-1}=\\dfrac{1}{4}\\cdot\\dfrac{2^{8}-1}{2-1}=\\dfrac{1}{4}\\cdot\\dfrac{256-1}{1}=\\dfrac{255}{4}$, es decir, $63{,}75$. Comprobación sumando los ocho términos: $\\dfrac{1}{4}+\\dfrac{1}{2}+1+2+4+8+16+32=63{,}75$, correcto.",
  "common_errors":["Hallar la razón restando términos consecutivos ($\\dfrac{1}{2}-\\dfrac{1}{4}=\\dfrac{1}{4}$): en una progresión geométrica la razón es un cociente.",
                   "Tomar $a_1=1$ porque es 'el término entero' y perder los dos primeros términos de la suma."],
  "provenance":"SOURCE_DERIVED"},
],

L4: [
 {"id":"EX-7B04-P1","type":"REASONING","objective_ids":["LO-7B04-1","LO-7B04-2","LO-7B04-3"],
  "concept_ids":["C-7B04-1","C-7B04-2","C-7B04-3"],"difficulty":4,
  "statement":"Una sucesión se define por recurrencia como $b_1=-1$ y $b_n=3b_{n-1}+2$. a) Calcula sus cinco primeros términos. b) Clasifícala en cuanto a monotonía, acotación y convergencia, y explica por qué el factor $3$ de la recurrencia no la hace crecer.",
  "hints":["Calcula $b_2$ con cuidado antes de sacar conclusiones sobre el crecimiento.",
           "Si todos los términos son iguales, ¿qué cotas tiene la sucesión y hacia dónde tiende?"],
  "answer":"a) $-1,\\ -1,\\ -1,\\ -1,\\ -1$: es la sucesión constante $-1$. b) Es monótona (constante, no estrictamente creciente ni decreciente), está acotada (toda cota $\\ge -1$ por arriba y $\\le -1$ por abajo sirve) y converge a $-1$.",
  "full_solution":"a) Se aplica la regla: $b_2=3\\cdot(-1)+2=-3+2=-1$. Como $b_2$ vuelve a ser $-1$, el cálculo siguiente es idéntico: $b_3=3\\cdot(-1)+2=-1$, y lo mismo $b_4$ y $b_5$. La sucesión es, por tanto, constante e igual a $-1$. El valor $-1$ es un punto fijo de la recurrencia: resolviendo $x=3x+2$ se obtiene $-2x=2$, es decir, $x=-1$, justo el valor inicial, y por eso la sucesión no se mueve. b) Al ser constante, se cumple $b_{n+1}=b_n$ para todo $n$: es monótona en sentido amplio (a la vez creciente y decreciente en sentido no estricto), pero no es estrictamente creciente ni estrictamente decreciente. Está acotada, porque todos sus términos valen $-1$: por ejemplo, $-1$ es a la vez cota inferior y cota superior. Y converge a $-1$, ya que la distancia de cada término a $-1$ es cero. El factor $3$ no la hace crecer porque multiplica un número negativo y el $+2$ compensa exactamente la diferencia; si el valor inicial fuera, por ejemplo, $b_1=0$, la sucesión sería $0,2,8,26,\\dots$ y sí crecería sin límite.",
  "common_errors":["Deducir del factor $3$ que la sucesión crece sin calcular ningún término: el comportamiento de una recurrencia depende también del valor inicial.",
                   "Afirmar que una sucesión constante no es monótona ni convergente: es monótona en sentido amplio y converge a su propio valor."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B04-P2","type":"REASONING","objective_ids":["LO-7B04-1","LO-7B04-2"],
  "concept_ids":["C-7B04-1","C-7B04-2"],"difficulty":4,
  "statement":"Considera la sucesión $b_n=\\dfrac{2n-1}{n+1}$. a) Calcula $b_1$, $b_2$, $b_3$ y $b_{22}$. b) Demuestra que es creciente comparando $b_{n+1}$ con $b_n$, en lugar de mirar solo los primeros términos. c) ¿Está acotada superiormente?",
  "hints":["Para b) escribe $b_n=2-\\dfrac{3}{n+1}$ reorganizando la fracción.",
           "Si $\\dfrac{3}{n+1}$ disminuye al crecer $n$, ¿qué le pasa a $2-\\dfrac{3}{n+1}$?"],
  "answer":"a) $b_1=\\dfrac{1}{2}$, $b_2=1$, $b_3=\\dfrac{5}{4}$, $b_{22}=\\dfrac{43}{23}$. b) $b_n=2-\\dfrac{3}{n+1}$ y $\\dfrac{3}{n+1}$ decrece, así que $b_n$ crece. c) Sí: está acotada superiormente por $2$ (nunca lo alcanza).",
  "full_solution":"a) Sustituyendo: $b_1=\\dfrac{2-1}{2}=\\dfrac{1}{2}$; $b_2=\\dfrac{4-1}{3}=1$; $b_3=\\dfrac{6-1}{4}=\\dfrac{5}{4}$; y $b_{22}=\\dfrac{2\\cdot 22-1}{22+1}=\\dfrac{43}{23}\\approx 1{,}8696$. b) Mirar unos pocos términos no demuestra nada; conviene transformar la fórmula. Dividiendo, $\\dfrac{2n-1}{n+1}=\\dfrac{2(n+1)-3}{n+1}=2-\\dfrac{3}{n+1}$. Al aumentar $n$, el denominador $n+1$ crece, luego la fracción $\\dfrac{3}{n+1}$ disminuye, y al restar una cantidad cada vez menor el resultado aumenta: $b_{n+1}>b_n$ para todo $n$. La sucesión es, por tanto, estrictamente creciente. c) De la expresión $b_n=2-\\dfrac{3}{n+1}$ se ve que siempre se resta algo positivo, así que $b_n<2$ para todo $n$: el número $2$ es cota superior y la sucesión nunca lo alcanza, aunque se acerca tanto como se quiera. Por abajo está acotada por $b_1=\\dfrac{1}{2}$, al ser creciente.",
  "common_errors":["Concluir que es creciente solo porque los primeros términos aumentan: hay sucesiones que empiezan creciendo y luego cambian, así que hace falta comparar $b_{n+1}$ con $b_n$ en general.",
                   "Pensar que si está acotada por $2$ debe alcanzar el valor $2$ en algún término: una cota superior no tiene por qué ser un valor de la sucesión."],
  "provenance":"SOURCE_DERIVED"},
],

L6: [
 {"id":"EX-7B06-P1","type":"STANDARD","objective_ids":["LO-7B06-1","LO-7B06-2"],
  "concept_ids":["C-7B06-1","C-7B06-2"],"difficulty":4,
  "statement":"Calcula los límites de las sucesiones $a_n=\\dfrac{2n-1}{n+1}$, $b_n=\\dfrac{n^{2}+1}{2n+2}$ y $c_n=n^{2}-1$, comparando en cada caso los grados del numerador y del denominador.",
  "hints":["Compara el grado del numerador con el del denominador: si son iguales, el límite es el cociente de los coeficientes principales.",
           "Si el numerador tiene grado mayor, la sucesión diverge."],
  "answer":"$\\lim a_n=2$; $\\lim b_n=+\\infty$; $\\lim c_n=+\\infty$.",
  "full_solution":"Para $a_n=\\dfrac{2n-1}{n+1}$, numerador y denominador tienen el mismo grado ($1$), así que el límite es el cociente de los coeficientes principales: $\\dfrac{2}{1}=2$. Se ve también escribiendo $a_n=2-\\dfrac{3}{n+1}$: el término que se resta tiende a cero, y queda $2$. Para $b_n=\\dfrac{n^{2}+1}{2n+2}$, el numerador tiene grado $2$ y el denominador grado $1$: el numerador crece mucho más deprisa, así que la sucesión diverge y $\\lim b_n=+\\infty$. Se puede confirmar dividiendo todo entre $n$: $b_n=\\dfrac{n+\\frac{1}{n}}{2+\\frac{2}{n}}$, cuyo numerador crece sin tope mientras el denominador tiende a $2$. Para $c_n=n^{2}-1$ no hay denominador: al crecer $n$, el valor crece sin límite, luego $\\lim c_n=+\\infty$. Comprobación numérica: $a_{1000}\\approx 1{,}997$, $b_{1000}\\approx 499{,}50$ y $c_{1000}=999\\,999$.",
  "common_errors":["Decir que $b_n$ tiende a $\\dfrac{1}{2}$ mirando solo los coeficientes $1$ y $2$ sin comparar antes los grados: el criterio del cociente de coeficientes solo vale cuando los grados coinciden.",
                   "Escribir $\\dfrac{\\infty}{\\infty}=1$: el infinito no es un número y ese cociente es una indeterminación que hay que resolver comparando grados."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-7B06-P2","type":"REASONING","objective_ids":["LO-7B06-1","LO-7B06-2"],
  "concept_ids":["C-7B06-1","C-7B06-2"],"difficulty":4,
  "statement":"La sucesión $a_n=\\dfrac{n^{2}}{n+1}$ tiene como primeros términos $\\dfrac{1}{2},\\ \\dfrac{4}{3},\\ \\dfrac{9}{4},\\ \\dfrac{16}{5},\\dots$. Un alumno dice que, como los términos son fracciones cada vez 'menos grandes' en el denominador comparado con el numerador, el límite será $1$. Calcula el límite real y explica el error.",
  "hints":["Compara el grado del numerador con el del denominador.",
           "Calcula algún término lejano, como $a_{100}$, para contrastar la conjetura."],
  "answer":"$\\lim a_n=+\\infty$: la sucesión diverge. El error es suponer que una sucesión de fracciones tiene que tender a un número finito.",
  "full_solution":"El numerador $n^{2}$ tiene grado $2$ y el denominador $n+1$ tiene grado $1$. Cuando el grado del numerador es mayor, la sucesión diverge: $\\lim\\dfrac{n^{2}}{n+1}=+\\infty$. Para verlo con detalle se divide numerador y denominador entre $n$: $a_n=\\dfrac{n}{1+\\frac{1}{n}}$, donde el denominador tiende a $1$ mientras el numerador crece sin tope, de modo que el cociente crece sin tope. También puede escribirse $a_n=n-1+\\dfrac{1}{n+1}$, que es prácticamente $n-1$ para $n$ grande. El error del alumno es razonar sobre el 'aspecto' de las fracciones en vez de comparar el ritmo de crecimiento: una sucesión de fracciones puede perfectamente tender a infinito si el numerador crece más deprisa. Un contraste numérico lo deja claro: $a_{10}=\\dfrac{100}{11}\\approx 9{,}09$ y $a_{100}=\\dfrac{10\\,000}{101}\\approx 99{,}01$, muy lejos de $1$ y creciendo.",
  "common_errors":["Suponer que cualquier sucesión formada por fracciones converge a un número finito: lo que decide es la comparación de grados.",
                   "Simplificar $\\dfrac{n^{2}}{n+1}$ como $\\dfrac{n^{2}}{n}=n$ 'quitando el $1$': no se puede eliminar un sumando del denominador, aunque el resultado del límite coincida por casualidad."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    # ---- L01 P1 fib variante
    b = [2, 3]
    while len(b) < 8: b.append(b[-1] + b[-2])
    assert b == [2, 3, 5, 8, 13, 21, 34, 55]
    fib = [1, 1]
    while len(fib) < 10: fib.append(fib[-1] + fib[-2])
    assert fib == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert all(x in fib for x in b)
    # ---- L01 P2 terminos generales
    assert [F(n*n, n+1) for n in (1, 2, 3, 4)] == [F(1, 2), F(4, 3), F(9, 4), F(16, 5)]
    for n, (p, q) in zip((1, 2, 3, 4), ((2, 4), (5, 6), (10, 8), (17, 10))):
        assert n*n + 1 == p and 2*n + 2 == q
    # ---- L01 P3 pertenencia
    def pos_lin(val, a, b):            # a*n+b = val  -> n
        return F(val - b, a)
    assert pos_lin(531, 6, 1) == F(530, 6) and not pos_lin(531, 6, 1).denominator == 1
    assert pos_lin(531, 4, 3) == 132
    assert 23*23 + 2 == 531
    assert pos_lin(27, 6, 1) == F(26, 6) and F(26, 6).denominator != 1
    assert pos_lin(27, 4, 3) == 6
    assert 5*5 + 2 == 27
    assert pos_lin(1201, 6, 1) == 200
    assert pos_lin(1201, 4, 3) == F(1198, 4) == F(599, 2)
    assert ic(float(F(1198, 4)), 299.5)
    assert 34**2 == 1156 and 35**2 == 1225 and not (1156 < 1199 < 1225 and math.isqrt(1199)**2 == 1199)
    assert math.isqrt(1199) == 34 and 34**2 != 1199
    assert [7 + 6*(n-1) for n in (1, 2, 3, 4)] == [7, 13, 19, 25]
    # ---- L02 P1
    d = F(6 - 12, 3); assert d == -2
    a1 = 12 - 3*d; assert a1 == 18
    gen = lambda n: 20 - 2*n
    assert gen(1) == 18 and gen(4) == 12 and gen(7) == 6 and gen(175) == -330
    assert F(6-12, 7) == F(-6, 7)
    # ---- L02 P2 cuadrilatero
    a = F(52 - 36, 4); assert a == 4
    lados = [a, a+6, a+12, a+18]; assert lados == [4, 10, 16, 22] and sum(lados) == 52
    assert 4*a + 36 == 52
    # ---- L02 P3 cuantos terminos
    S = lambda n: F(n*(3*n + 11), 2)
    assert S(12) == 282
    disc = 11**2 + 4*3*564; assert disc == 6889 and math.isqrt(disc) == 83
    assert F(-11 + 83, 6) == 12 and F(-11 - 83, 6) == F(-94, 6)
    assert ic(float(F(-94, 6)), -15.666666666666666)
    assert 3*12 + 4 == 40 and F(12*(7+40), 2) == 282
    # ---- L02 P4 S10=530
    a10 = F(530, 5) - 8; assert a10 == 98
    assert F(10*(8 + 98), 2) == 530
    dd = F(98 - 8, 9); assert dd == 10
    assert F(98-8, 10) == 9     # error tipico
    # ---- L02 P5
    assert 100//5 == 20 and F(20*(5+100), 2) == 1050
    d2 = F(19, 3) - 6; assert d2 == F(1, 3)
    assert F(19, 3) + F(1, 3) == F(20, 3)
    a23 = 6 + 22*F(1, 3); assert a23 == F(40, 3)
    S23 = F(23*(6 + F(40, 3)), 2); assert S23 == F(667, 3)
    assert ic(float(S23), 222.33333333333334, rel_tol=1e-12)
    assert F(1334, 6) == F(667, 3)
    # ---- L03 P1
    r = F(-1, 4) / F(27, 4); assert r == F(-1, 27)
    assert F(-1, 3)**3 == F(-1, 27)
    g = lambda n: F(27, 4) * F(-1, 3)**(n-1)
    assert g(1) == F(27, 4) and g(2) == F(-9, 4) and g(3) == F(3, 4) and g(4) == F(-1, 4)
    # ---- L03 P2 dos razones
    assert F(192, 12) == 16 and 2**4 == 16 and (-2)**4 == 16
    for rr in (2, -2):
        assert F(12, rr**2) == 3
        a1b = 3
        assert a1b * rr**2 == 12 and a1b * rr**6 == 192
    assert 3 * 2**9 == 1536 and 3 * (-2)**9 == -1536 and 2**9 == 512
    assert [3*(-2)**(n-1) for n in range(1, 8)] == [3, -6, 12, -24, 48, -96, 192]
    # ---- L03 P3 bacterias
    assert 12*2 == 24
    assert 2**10 == 1024 and 1024**2 == 2**20 == 1048576
    assert 2**24 == 1048576*16 == 16777216
    assert 10*2**24 == 167772160
    assert ic(167772160/1e8, 1.6777216)
    # ---- L03 P4
    assert F(32, 4) == 8 and 2**3 == 8
    assert F(4, 2) == 2
    S10 = 2 * (2**10 - 1) // (2 - 1); assert S10 == 2046
    assert sum(2*2**k for k in range(10)) == 2046
    # ---- L03 P5
    assert F(1, 2) / F(1, 4) == 2 and F(1, 1) / F(1, 2) == 2
    S8 = F(1, 4) * (2**8 - 1); assert S8 == F(255, 4) and ic(float(S8), 63.75)
    assert sum(F(1, 4)*2**k for k in range(8)) == F(255, 4)
    assert F(1, 2) - F(1, 4) == F(1, 4)
    # ---- L04 P1 recurrencia constante
    bb = [-1]
    for _ in range(4): bb.append(3*bb[-1] + 2)
    assert bb == [-1, -1, -1, -1, -1]
    assert F(2, -2) == -1          # punto fijo x=3x+2 -> x=-1
    cc = [0]
    for _ in range(3): cc.append(3*cc[-1] + 2)
    assert cc == [0, 2, 8, 26]
    # ---- L04 P2 / L06 P1 (2n-1)/(n+1)
    f = lambda n: F(2*n - 1, n + 1)
    assert f(1) == F(1, 2) and f(2) == 1 and f(3) == F(5, 4) and f(22) == F(43, 23)
    assert ic(float(f(22)), 1.8695652173913044, rel_tol=1e-12)
    for n in range(1, 60):
        assert f(n) == 2 - F(3, n + 1)
        assert f(n + 1) > f(n)
        assert f(n) < 2
    assert round(float(f(1000)), 3) == 1.997
    # ---- L06 P1 b_n y c_n
    g2 = lambda n: F(n*n + 1, 2*n + 2)
    assert g2(1) == F(2, 4) and g2(1000) == F(1000001, 2002)
    assert round(float(g2(1000)), 2) == 499.5, float(g2(1000))
    assert 1000**2 - 1 == 999999
    # ---- L06 P2 n^2/(n+1)
    h = lambda n: F(n*n, n + 1)
    assert h(10) == F(100, 11) and round(float(h(10)), 2) == 9.09
    assert h(100) == F(10000, 101) and round(float(h(100)), 2) == 99.01
    for n in range(1, 50):
        assert h(n) == n - 1 + F(1, n + 1)
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
