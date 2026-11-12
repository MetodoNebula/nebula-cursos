# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'estadistica_combinatoria_probabilidad_nebula.pdf'
(material propio de Método Nebula). Tres bundles: estadística descriptiva,
estadística bidimensional y probabilidad."""
import math
from fractions import Fraction as F

EX_DESC = {
"03_Medidas_de_centralización_y_posición.json": [
 {"id":"EX-1203-P3","type":"CONTEXT","objective_ids":["LO-1203-3","LO-1203-2"],
  "concept_ids":["C-1203-2","C-1203-3"],"difficulty":4,
  "statement":"En un parque de atracciones se registra el tiempo de espera, en minutos, de $40$ visitantes: $[0,10)$: $6$ personas; $[10,20)$: $12$; $[20,30)$: $10$; $[30,40)$: $8$; $[40,50]$: $4$. a) ¿Qué porcentaje espera $20$ minutos o más? b) Localiza los intervalos donde caen $Q_1$, $Q_2$ y $Q_3$ usando las frecuencias acumuladas, y da la marca de clase de cada uno. c) ¿Cuál es el intervalo modal y su marca de clase?",
  "hints":["Construye la columna de frecuencias acumuladas $N_i$ antes de buscar nada.",
           "Los cuartiles se localizan en las posiciones $\\dfrac{N}{4}$, $\\dfrac{N}{2}$ y $\\dfrac{3N}{4}$; aquí $N=40$."],
  "answer":"a) $\\dfrac{22}{40}\\cdot 100=55\\%$. b) $Q_1$ en $[10,20)$, marca $15$; $Q_2$ en $[20,30)$, marca $25$; $Q_3$ en $[30,40)$, marca $35$. c) Intervalo modal $[10,20)$, marca $15$.",
  "full_solution":"Primero se construyen las frecuencias acumuladas: $6$; $6+12=18$; $18+10=28$; $28+8=36$; $36+4=40$. a) Esperar $20$ minutos o más significa caer en los tres últimos intervalos: $10+8+4=22$ visitantes de $40$, es decir, $\\dfrac{22}{40}\\cdot 100=55\\%$. Comprobación: los otros $18$ son el $45\\%$, y $45+55=100$. b) Las posiciones de los cuartiles son $\\dfrac{40}{4}=10$, $\\dfrac{40}{2}=20$ y $\\dfrac{3\\cdot 40}{4}=30$. La posición $10$ cae en el segundo intervalo, porque la acumulada pasa de $6$ a $18$: $Q_1$ está en $[10,20)$, cuya marca de clase es $\\dfrac{10+20}{2}=15$. La posición $20$ cae en el tercero, porque la acumulada pasa de $18$ a $28$: $Q_2$ está en $[20,30)$, marca $25$. La posición $30$ cae en el cuarto, porque la acumulada pasa de $28$ a $36$: $Q_3$ está en $[30,40)$, marca $35$. c) El intervalo modal es el de mayor frecuencia, que es $[10,20)$ con $12$ visitantes; su marca de clase es $15$. Conviene recordar que $15$, $25$ y $35$ son marcas de clase de los intervalos donde caen los cuartiles, no los cuartiles exactos: estos se obtendrían interpolando dentro del intervalo.",
  "common_errors":["Buscar el cuartil en el intervalo cuya frecuencia acumulada coincide exactamente con la posición, en lugar del primero que la alcanza o la supera.",
                   "Dar como moda la frecuencia $12$ en vez del intervalo $[10,20)$ (o su marca $15$): la moda es un valor de la variable, no una frecuencia."],
  "provenance":"SOURCE_DERIVED"},
],
"05_Dispersión_relativa_caja_y_valores_atípicos.json": [
 {"id":"EX-1205-P3","type":"CONTEXT","objective_ids":["LO-1205-1"],
  "concept_ids":["C-1205-1"],"difficulty":5,
  "statement":"Con la misma distribución de tiempos de espera ($[0,10)$: $6$; $[10,20)$: $12$; $[20,30)$: $10$; $[30,40)$: $8$; $[40,50]$: $4$; en total $40$ visitantes), calcula la media, la desviación típica y el coeficiente de variación, e interpreta el resultado.",
  "hints":["Usa las marcas de clase $5$, $15$, $25$, $35$ y $45$, y calcula $\\sum n_ix_i$ y $\\sum n_ix_i^{2}$.",
           "$\\sigma=\\sqrt{\\dfrac{\\sum n_ix_i^{2}}{N}-\\overline{x}^{2}}$ y $CV=\\dfrac{\\sigma}{\\overline{x}}\\cdot 100$."],
  "answer":"$\\overline{x}=\\dfrac{920}{40}=23$ min; $\\sigma=\\sqrt{146}\\approx 12{,}08$ min; $CV\\approx 52{,}53\\%$: dispersión relativa alta.",
  "full_solution":"Las marcas de clase son $5$, $15$, $25$, $35$ y $45$. Los productos $n_ix_i$ valen $30$, $180$, $250$, $280$ y $180$, cuya suma es $920$; por tanto $\\overline{x}=\\dfrac{920}{40}=23$ minutos. Los productos $n_ix_i^{2}$ valen $6\\cdot 25=150$, $12\\cdot 225=2700$, $10\\cdot 625=6250$, $8\\cdot 1225=9800$ y $4\\cdot 2025=8100$, cuya suma es $27\\,000$. Entonces $\\sigma^{2}=\\dfrac{27\\,000}{40}-23^{2}=675-529=146$ y $\\sigma=\\sqrt{146}\\approx 12{,}083$ minutos. El coeficiente de variación es $CV=\\dfrac{12{,}083}{23}\\cdot 100\\approx 52{,}53\\%$ (más exactamente, $52{,}535\\%$). Interpretación: la desviación típica supone más de la mitad de la media, lo que indica una dispersión relativa alta: los tiempos de espera no están concentrados alrededor de los $23$ minutos, sino repartidos entre casi cero y casi una hora. Al tratarse de datos agrupados, estos valores son estimaciones, porque se supone que dentro de cada intervalo los datos se sitúan en la marca de clase.",
  "common_errors":["Calcular $\\sigma^{2}$ como $\\dfrac{\\sum n_ix_i^{2}}{N}-\\overline{x}$ en lugar de restar $\\overline{x}^{2}$: hay que restar el cuadrado de la media.",
                   "Dar el coeficiente de variación en minutos: es un cociente entre dos cantidades en minutos, así que es adimensional y se expresa en porcentaje."],
  "provenance":"SOURCE_DERIVED"},
],
}

EX_BID = {
"05_Covarianza_y_coeficiente_de_correlación_lineal.json": [
 {"id":"EX-1305-P1","type":"CONTEXT","objective_ids":["LO-1305-2","LO-1305-3"],
  "concept_ids":["C-1305-2","C-1305-1"],"difficulty":5,
  "statement":"Se estudia en $5$ alumnos la relación entre las horas diarias de uso del móvil ($x$) y las horas de sueño ($y$): $(1,9)$, $(2,8)$, $(4,7)$, $(5,7)$, $(8,5)$. Sabiendo que $\\sum x=20$, $\\sum y=36$, $\\sum xy=128$, $\\sum x^{2}=110$ y $\\sum y^{2}=268$, calcula el coeficiente de correlación lineal con la fórmula $r=\\dfrac{n\\sum xy-\\left(\\sum x\\right)\\left(\\sum y\\right)}{\\sqrt{\\left[n\\sum x^{2}-\\left(\\sum x\\right)^{2}\\right]\\left[n\\sum y^{2}-\\left(\\sum y\\right)^{2}\\right]}}$ e interprétalo.",
  "hints":["Sustituye con cuidado: $n=5$, y el numerador puede salir negativo.",
           "Calcula por separado los dos corchetes del denominador antes de multiplicarlos."],
  "answer":"$r=\\dfrac{-80}{\\sqrt{6600}}\\approx -0{,}985$: correlación lineal negativa muy fuerte.",
  "full_solution":"Se sustituyen los datos con $n=5$. Numerador: $5\\cdot 128-20\\cdot 36=640-720=-80$, negativo, lo que ya anticipa una relación decreciente. Primer corchete del denominador: $5\\cdot 110-20^{2}=550-400=150$. Segundo corchete: $5\\cdot 268-36^{2}=1340-1296=44$. Su producto es $150\\cdot 44=6600$ y su raíz $\\sqrt{6600}\\approx 81{,}24$. Por tanto $r=\\dfrac{-80}{81{,}24}\\approx -0{,}985$. Como $r$ está muy cerca de $-1$, la correlación lineal es negativa y muy fuerte: entre estos cinco alumnos, los que dedican más horas al móvil tienden a dormir menos, y los puntos se sitúan casi sobre una recta descendente. Conviene añadir una advertencia: correlación no es causalidad. Estos datos no demuestran que el móvil cause dormir menos; podría haber una tercera variable (por ejemplo, acostarse tarde) que influya en las dos.",
  "common_errors":["Dar un valor de $r$ fuera del intervalo $[-1,1]$: si eso ocurre, el error suele estar en haber olvidado alguna de las multiplicaciones por $n$ en el denominador.",
                   "Interpretar $r\\approx -0{,}985$ como una correlación débil por ser negativa: el signo indica el sentido y el valor absoluto la intensidad, que aquí es casi máxima."],
  "provenance":"SOURCE_DERIVED"},
],
"06_Recta_de_regresión_predicción_y_causalidad.json": [
 {"id":"EX-1306-P1","type":"CONTEXT","objective_ids":["LO-1306-1"],
  "concept_ids":["C-1306-1"],"difficulty":5,
  "statement":"Con los mismos $5$ alumnos (uso del móvil $x$ y horas de sueño $y$; $\\sum x=20$, $\\sum y=36$, $\\sum xy=128$, $\\sum x^{2}=110$, $n=5$), halla la recta de regresión de $y$ sobre $x$ usando $b=\\dfrac{n\\sum xy-\\left(\\sum x\\right)\\left(\\sum y\\right)}{n\\sum x^{2}-\\left(\\sum x\\right)^{2}}$ y $a=\\overline{y}-b\\,\\overline{x}$, y explica qué significa la pendiente.",
  "hints":["Calcula primero las medias $\\overline{x}$ e $\\overline{y}$.",
           "Deja $b$ como fracción exacta para que $a$ salga sin errores de redondeo."],
  "answer":"$b=-\\dfrac{8}{15}\\approx -0{,}5333$ y $a=\\dfrac{28}{3}\\approx 9{,}3333$, luego $\\hat{y}=9{,}3333-0{,}5333x$.",
  "full_solution":"Las medias son $\\overline{x}=\\dfrac{20}{5}=4$ y $\\overline{y}=\\dfrac{36}{5}=7{,}2$. La pendiente es $b=\\dfrac{5\\cdot 128-20\\cdot 36}{5\\cdot 110-20^{2}}=\\dfrac{640-720}{550-400}=\\dfrac{-80}{150}=-\\dfrac{8}{15}\\approx -0{,}5333$. La ordenada en el origen es $a=\\overline{y}-b\\,\\overline{x}=7{,}2-\\left(-\\dfrac{8}{15}\\right)\\cdot 4=7{,}2+\\dfrac{32}{15}=\\dfrac{108}{15}+\\dfrac{32}{15}=\\dfrac{140}{15}=\\dfrac{28}{3}\\approx 9{,}3333$. La recta es, por tanto, $\\hat{y}=\\dfrac{28}{3}-\\dfrac{8}{15}x\\approx 9{,}3333-0{,}5333x$. La pendiente negativa significa que, según este modelo, cada hora diaria adicional de móvil se asocia con unas $0{,}5333$ horas menos de sueño previsto, es decir, unos $32$ minutos menos. Comprobación: la recta debe pasar por el punto $\\left(\\overline{x},\\overline{y}\\right)=(4;\\,7{,}2)$, y en efecto $\\dfrac{28}{3}-\\dfrac{8}{15}\\cdot 4=\\dfrac{140-32}{15}=\\dfrac{108}{15}=7{,}2$.",
  "common_errors":["Restar mal en $a=\\overline{y}-b\\,\\overline{x}$ cuando $b$ es negativa: restar un número negativo equivale a sumarlo, así que $a$ sale mayor que $\\overline{y}$.",
                   "Usar $\\sum y^{2}$ en el denominador de $b$: en la pendiente de $y$ sobre $x$ solo interviene la dispersión de $x$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1306-P2","type":"CONTEXT","objective_ids":["LO-1306-2","LO-1306-3","LO-1306-4"],
  "concept_ids":["C-1306-2","C-1306-3","C-1306-4"],"difficulty":5,
  "statement":"Con la recta $\\hat{y}=\\dfrac{28}{3}-\\dfrac{8}{15}x$ (horas de sueño según horas de móvil), ajustada con datos de $x$ entre $1$ y $8$ y con $r\\approx -0{,}985$: a) estima las horas de sueño de un alumno que usa el móvil $6$ horas al día y expresa el resultado en horas y minutos; b) valora la fiabilidad de esa estimación; c) ¿demuestra este modelo que el móvil causa dormir menos?",
  "hints":["Sustituye $x=6$ manteniendo las fracciones y pasa a decimal solo al final.",
           "Para los minutos, multiplica la parte decimal de las horas por $60$."],
  "answer":"a) $\\hat{y}(6)=\\dfrac{92}{15}\\approx 6{,}13$ horas, es decir, $6$ horas y $8$ minutos. b) Es una interpolación ($6$ está dentro de $[1,8]$) con $r$ muy próximo a $-1$, así que es razonable, aunque solo hay $5$ datos. c) No: la correlación no prueba causalidad.",
  "full_solution":"a) Se sustituye $x=6$ en la recta: $\\hat{y}(6)=\\dfrac{28}{3}-\\dfrac{8}{15}\\cdot 6=\\dfrac{28}{3}-\\dfrac{48}{15}=\\dfrac{28}{3}-\\dfrac{16}{5}=\\dfrac{140-48}{15}=\\dfrac{92}{15}\\approx 6{,}1333$ horas. La parte decimal son $0{,}1333\\cdot 60\\approx 8$ minutos, de modo que la estimación es de $6$ horas y $8$ minutos de sueño. b) La fiabilidad es razonable por dos motivos: el valor $x=6$ está dentro del rango de los datos observados, $[1,8]$, así que se trata de una interpolación y no de una extrapolación; y el coeficiente $r\\approx -0{,}985$ indica que los puntos se ajustan muy bien a la recta. Sin embargo, la muestra es de solo cinco alumnos, lo que limita la validez de la conclusión fuera de ese grupo. c) No. Que dos variables estén muy correlacionadas no demuestra que una cause la otra: podría haber una variable oculta (por ejemplo, acostarse tarde por otros motivos) que explique las dos, o incluso invertirse el sentido (dormir poco deja más tiempo despierto para usar el móvil). Para hablar de causa haría falta un diseño experimental, no solo datos observacionales.",
  "common_errors":["Leer $6{,}13$ horas como «$6$ horas y $13$ minutos»: la parte decimal hay que multiplicarla por $60$, y $0{,}13$ h son unos $8$ minutos.",
                   "Usar la recta para estimar, por ejemplo, $x=15$ horas de móvil: eso es extrapolar fuera del rango de los datos y el modelo deja de ser fiable (daría incluso horas de sueño negativas)."],
  "provenance":"SOURCE_DERIVED"},
],
}

EX_PROB = {
"04_Combinatoria_básica.json": [
 {"id":"EX-1404-P1","type":"REASONING","objective_ids":["LO-1404-2","LO-1404-3","LO-1404-4"],
  "concept_ids":["C-1404-1","C-1404-2"],"difficulty":4,
  "statement":"Hay $8$ papeletas numeradas del $1$ al $8$. a) Si se sacan $2$ a la vez (sin reemplazamiento), ¿cuántos resultados distintos hay? b) ¿Y si se extraen una detrás de otra, teniendo en cuenta el orden? c) Explica la relación entre los dos números.",
  "hints":["Pregúntate si $\\{3,5\\}$ y $\\{5,3\\}$ son el mismo resultado en cada apartado.",
           "Combinaciones cuando el orden no importa; variaciones cuando sí importa."],
  "answer":"a) $\\binom{8}{2}=28$. b) $V_{8,2}=8\\cdot 7=56$. c) $56=28\\cdot 2$, porque cada pareja admite $2$ órdenes.",
  "full_solution":"a) Si las dos papeletas se sacan a la vez, el orden no distingue resultados: $\\{3,5\\}$ y $\\{5,3\\}$ son la misma extracción. Se usan combinaciones: $\\binom{8}{2}=\\dfrac{8!}{2!\\,(8-2)!}=\\dfrac{8\\cdot 7}{2\\cdot 1}=28$ resultados distintos. b) Si se extraen una detrás de otra y se anota el orden, $(3,5)$ y $(5,3)$ son resultados distintos. Se usan variaciones sin repetición: $V_{8,2}=8\\cdot 7=56$, porque la primera papeleta puede ser cualquiera de las $8$ y, una vez retirada, quedan $7$ para la segunda. c) La relación es $56=28\\cdot 2$: cada pareja sin orden se corresponde con exactamente $2$ secuencias ordenadas (la pareja y su inversa), así que al dividir las $56$ secuencias entre $2$ se recuperan las $28$ parejas. En general, $\\binom{n}{k}=\\dfrac{V_{n,k}}{k!}$.",
  "common_errors":["Usar variaciones cuando las extracciones son simultáneas: si se sacan a la vez no hay un «primero» y un «segundo», así que el orden no cuenta.",
                   "Calcular $8^{2}=64$ aplicando el principio multiplicativo sin descontar la repetición: no hay reemplazamiento, así que la segunda papeleta solo puede ser una de las $7$ restantes."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1404-P2","type":"CONTEXT","objective_ids":["LO-1404-4","LO-1404-3"],
  "concept_ids":["C-1404-2","C-1404-1"],"difficulty":4,
  "statement":"De las $8$ papeletas numeradas del $1$ al $8$ se sacan $2$ a la vez. a) Calcula la probabilidad de obtener exactamente las papeletas $3$ y $5$. b) Si en cambio se extraen ordenadamente, calcula la probabilidad de sacar primero el $3$ y después el $5$. c) ¿Por qué el segundo resultado es la mitad del primero?",
  "hints":["En a) aplica la regla de Laplace sobre las $\\binom{8}{2}=28$ parejas equiprobables.",
           "En b) multiplica la probabilidad de cada etapa: la segunda se calcula sobre las $7$ papeletas que quedan."],
  "answer":"a) $\\dfrac{1}{28}\\approx 3{,}57\\%$. b) $\\dfrac{1}{8}\\cdot\\dfrac{1}{7}=\\dfrac{1}{56}\\approx 1{,}79\\%$. c) Porque $\\{3,5\\}$ admite dos secuencias, $(3,5)$ y $(5,3)$, y en b) solo vale una.",
  "full_solution":"a) Al sacarlas a la vez, los $28$ resultados posibles (las $\\binom{8}{2}$ parejas) son equiprobables y solo uno es favorable, la pareja $\\{3,5\\}$. Por la regla de Laplace, $P=\\dfrac{1}{28}\\approx 0{,}0357$, es decir, un $3{,}57\\%$. b) Con extracción ordenada se multiplican las probabilidades de las dos etapas: la probabilidad de que la primera papeleta sea el $3$ es $\\dfrac{1}{8}$; una vez retirado el $3$, quedan $7$ papeletas y la probabilidad de que la segunda sea el $5$ es $\\dfrac{1}{7}$. Por tanto $P(3\\to 5)=\\dfrac{1}{8}\\cdot\\dfrac{1}{7}=\\dfrac{1}{56}\\approx 0{,}0179$, un $1{,}79\\%$. c) El suceso del apartado a), «salen el $3$ y el $5$», se realiza mediante dos secuencias ordenadas distintas: $(3,5)$ y $(5,3)$, cada una con probabilidad $\\dfrac{1}{56}$. Sumándolas se obtiene $\\dfrac{2}{56}=\\dfrac{1}{28}$, que es justo el resultado de a). Por eso exigir además un orden concreto divide la probabilidad entre $2$.",
  "common_errors":["Calcular $P(3\\to 5)=\\dfrac{1}{8}\\cdot\\dfrac{1}{8}$: sin reemplazamiento, en la segunda extracción quedan $7$ papeletas, no $8$.",
                   "Pensar que el apartado a) y el b) deben dar lo mismo porque «salen las mismas papeletas»: en b) se impone además un orden, lo que reduce los casos favorables a la mitad."],
  "provenance":"SOURCE_DERIVED"},
],
"02_Operaciones_con_sucesos_y_regla_de_Laplace.json": [
 {"id":"EX-1402-P1","type":"CONTEXT","objective_ids":["LO-1402-1","LO-1402-2","LO-1402-3"],
  "concept_ids":["C-1402-1","C-1402-2","C-1402-3"],"difficulty":5,
  "statement":"De $8$ papeletas numeradas del $1$ al $8$ se sacan $2$ a la vez, de modo que hay $\\binom{8}{2}=28$ parejas equiprobables. Sea $A=$«las dos papeletas son pares» y $B=$«una de las papeletas es el $8$». a) Enumera los elementos de $A$ y calcula $P(A)$. b) Enumera los de $B$ y calcula $P(B)$. c) Halla $A\\cap B$ y $P(A\\cap B)$. d) Calcula $P(A\\cup B)$.",
  "hints":["Los pares entre $1$ y $8$ son $2$, $4$, $6$ y $8$: las parejas de $A$ son $\\binom{4}{2}$.",
           "Usa $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$ y pregúntate por qué hay que restar algo."],
  "answer":"a) $A=\\{\\{2,4\\},\\{2,6\\},\\{2,8\\},\\{4,6\\},\\{4,8\\},\\{6,8\\}\\}$, $P(A)=\\dfrac{6}{28}=\\dfrac{3}{14}\\approx 21{,}43\\%$. b) $B$ tiene $7$ parejas, $P(B)=\\dfrac{7}{28}=\\dfrac{1}{4}$. c) $A\\cap B=\\{\\{2,8\\},\\{4,8\\},\\{6,8\\}\\}$, $P(A\\cap B)=\\dfrac{3}{28}$. d) $P(A\\cup B)=\\dfrac{10}{28}=\\dfrac{5}{14}\\approx 35{,}71\\%$.",
  "full_solution":"a) Los números pares del $1$ al $8$ son $2$, $4$, $6$ y $8$, y las parejas que se pueden formar con ellos son $\\binom{4}{2}=6$: $\\{2,4\\}$, $\\{2,6\\}$, $\\{2,8\\}$, $\\{4,6\\}$, $\\{4,8\\}$ y $\\{6,8\\}$. Por Laplace, $P(A)=\\dfrac{6}{28}=\\dfrac{3}{14}\\approx 0{,}2143$, un $21{,}43\\%$. b) El suceso $B$ reúne todas las parejas que contienen el $8$: la otra papeleta puede ser cualquiera de las $7$ restantes, así que $B=\\{\\{1,8\\},\\{2,8\\},\\{3,8\\},\\{4,8\\},\\{5,8\\},\\{6,8\\},\\{7,8\\}\\}$ y $P(B)=\\dfrac{7}{28}=\\dfrac{1}{4}=25\\%$. c) La intersección exige las dos condiciones a la vez: dos papeletas pares y que una sea el $8$. Eso deja $\\{2,8\\}$, $\\{4,8\\}$ y $\\{6,8\\}$, luego $P(A\\cap B)=\\dfrac{3}{28}$. d) Con la regla de la adición, $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)=\\dfrac{6}{28}+\\dfrac{7}{28}-\\dfrac{3}{28}=\\dfrac{10}{28}=\\dfrac{5}{14}\\approx 0{,}3571$, un $35{,}71\\%$. Hay que restar la intersección porque las tres parejas $\\{2,8\\}$, $\\{4,8\\}$ y $\\{6,8\\}$ se han contado dos veces, una en $A$ y otra en $B$. Comprobación por recuento directo: la unión está formada por $6+7-3=10$ parejas distintas.",
  "common_errors":["Sumar $P(A)+P(B)=\\dfrac{13}{28}$ sin restar la intersección: los sucesos no son incompatibles y tres parejas se contarían dos veces.",
                   "Incluir en $B$ la pareja $\\{8,8\\}$: no hay reemplazamiento, así que las dos papeletas son distintas."],
  "provenance":"SOURCE_DERIVED"},
],
"06_Teorema_de_Bayes_básico.json": [
 {"id":"EX-1406-P1","type":"CONTEXT","objective_ids":["LO-1406-1","LO-1406-2","LO-1406-3"],
  "concept_ids":["C-1406-1","C-1406-2","C-1406-3"],"difficulty":5,
  "statement":"Un creador publica vídeos de baile ($B$, el $70\\%$) y de humor ($H$, el $30\\%$). Se hace viral el $10\\%$ de los de baile y el $20\\%$ de los de humor. a) Calcula la probabilidad de que un vídeo sea de baile y no se haga viral. b) ¿Qué porcentaje del total de vídeos se hace viral? c) Si un vídeo se ha hecho viral, ¿cuál es la probabilidad de que sea de humor? d) Explica por qué c) no es el $20\\%$.",
  "hints":["Organiza los datos en un árbol: $P(V\\mid B)=0{,}10$ y $P(V\\mid H)=0{,}20$, y los complementos $0{,}90$ y $0{,}80$.",
           "Para c) usa el teorema de Bayes: $P(H\\mid V)=\\dfrac{P(H)P(V\\mid H)}{P(V)}$."],
  "answer":"a) $0{,}70\\cdot 0{,}90=0{,}63$, un $63\\%$. b) $P(V)=0{,}13$, un $13\\%$. c) $P(H\\mid V)=\\dfrac{0{,}06}{0{,}13}=\\dfrac{6}{13}\\approx 46{,}15\\%$. d) Porque $P(V\\mid H)$ y $P(H\\mid V)$ condicionan sobre conjuntos distintos.",
  "full_solution":"El árbol tiene dos ramas iniciales, $P(B)=0{,}70$ y $P(H)=0{,}30$, y de cada una salen «viral» y «no viral». Los cuatro caminos son: baile y viral, $0{,}70\\cdot 0{,}10=0{,}07$; baile y no viral, $0{,}70\\cdot 0{,}90=0{,}63$; humor y viral, $0{,}30\\cdot 0{,}20=0{,}06$; humor y no viral, $0{,}30\\cdot 0{,}80=0{,}24$. Suman $1$, lo que valida el árbol. a) La probabilidad pedida es el segundo camino: $P(B\\cap\\overline{V})=0{,}63$, es decir, el $63\\%$ de todos los vídeos. b) Un vídeo viral puede venir de baile o de humor, y esos dos caminos son incompatibles, así que por la probabilidad total $P(V)=0{,}07+0{,}06=0{,}13$, un $13\\%$. c) Ahora se sabe que el vídeo es viral y se pregunta por su origen; es una probabilidad a posteriori y se usa Bayes: $P(H\\mid V)=\\dfrac{P(H)P(V\\mid H)}{P(V)}=\\dfrac{0{,}30\\cdot 0{,}20}{0{,}13}=\\dfrac{0{,}06}{0{,}13}=\\dfrac{6}{13}\\approx 0{,}4615$, un $46{,}15\\%$. d) El $20\\%$ es $P(V\\mid H)$: de cada $100$ vídeos de humor, $20$ se hacen virales. Lo que se pide en c) es $P(H\\mid V)$: de cada $100$ vídeos virales, unos $46$ son de humor. Son preguntas distintas porque el conjunto sobre el que se condiciona cambia: en un caso son los vídeos de humor y en el otro los vídeos virales. Resulta llamativo que, aunque solo el $30\\%$ de los vídeos sean de humor, casi la mitad de los virales lo sean: es consecuencia de que su tasa de viralización dobla a la del baile.",
  "common_errors":["Responder $20\\%$ en el apartado c) confundiendo $P(H\\mid V)$ con $P(V\\mid H)$: la barra indica qué información se da por conocida.",
                   "Calcular $P(V)$ como $0{,}10+0{,}20=0{,}30$ sin ponderar por $P(B)$ y $P(H)$: hay muchos más vídeos de baile, así que su tasa pesa más en el total."],
  "provenance":"SOURCE_DERIVED"},
],
}

# el inyector espera un unico dict EX por bundle; se elige segun variable de entorno
import os
_which = os.environ.get("NEB_BUNDLE", "")
EX = {"desc": EX_DESC, "bid": EX_BID, "prob": EX_PROB}.get(_which, {})


def val():
    ic = math.isclose
    # ---------- descriptiva: tiempos de espera
    ni = [6, 12, 10, 8, 4]; xi = [5, 15, 25, 35, 45]
    N = sum(ni); assert N == 40
    Ni = [sum(ni[:k+1]) for k in range(5)]
    assert Ni == [6, 18, 28, 36, 40]
    assert sum(ni[2:]) == 22 and F(22, 40)*100 == 55
    assert sum(ni[:2]) == 18 and F(18, 40)*100 == 45
    pos = [F(N, 4), F(N, 2), F(3*N, 4)]; assert pos == [10, 20, 30]
    def intervalo(p):
        for k, acc in enumerate(Ni):
            if acc >= p: return k
    assert [intervalo(p) for p in pos] == [1, 2, 3]
    assert [xi[intervalo(p)] for p in pos] == [15, 25, 35]
    assert ni.index(max(ni)) == 1 and xi[1] == 15 and max(ni) == 12
    assert [(0+10)/2, (10+20)/2, (20+30)/2, (30+40)/2, (40+50)/2] == [5, 15, 25, 35, 45]
    S1 = sum(n*x for n, x in zip(ni, xi)); assert S1 == 920
    assert [n*x for n, x in zip(ni, xi)] == [30, 180, 250, 280, 180]
    media = F(S1, N); assert media == 23
    S2 = sum(n*x*x for n, x in zip(ni, xi)); assert S2 == 27000
    assert [n*x*x for n, x in zip(ni, xi)] == [150, 2700, 6250, 9800, 8100]
    var = F(S2, N) - media**2; assert var == 146 and F(S2, N) == 675 and media**2 == 529
    sd = math.sqrt(146); assert round(sd, 3) == 12.083, sd
    cv = sd/23*100; assert round(cv, 2) == 52.53 and round(cv, 3) == 52.535, cv
    # ---------- bidimensional
    xs = [1, 2, 4, 5, 8]; ys = [9, 8, 7, 7, 5]
    n = len(xs); assert n == 5
    assert sum(xs) == 20 and sum(ys) == 36
    assert sum(a*b for a, b in zip(xs, ys)) == 128
    assert sum(a*a for a in xs) == 110 and sum(b*b for b in ys) == 268
    assert [a*b for a, b in zip(xs, ys)] == [9, 16, 28, 35, 40]
    assert [a*a for a in xs] == [1, 4, 16, 25, 64]
    assert [b*b for b in ys] == [81, 64, 49, 49, 25]
    numr = n*128 - 20*36; assert numr == -80
    c1 = n*110 - 20**2; c2 = n*268 - 36**2
    assert c1 == 150 and c2 == 44 and c1*c2 == 6600
    r = numr/math.sqrt(6600); assert round(r, 3) == -0.985, r
    assert round(math.sqrt(6600), 2) == 81.24
    assert -1 <= r <= 1
    b = F(numr, c1); assert b == F(-8, 15) and round(float(b), 4) == -0.5333
    mx, my = F(20, 5), F(36, 5); assert mx == 4 and my == F(36, 5)
    a = my - b*mx; assert a == F(28, 3) and round(float(a), 4) == 9.3333
    assert my + F(32, 15) == F(140, 15) == F(28, 3)
    assert a + b*mx == my                       # la recta pasa por (x̄, ȳ)
    yh = a + b*6; assert yh == F(92, 15) and round(float(yh), 4) == 6.1333
    assert F(28, 3) - F(48, 15) == F(92, 15) and F(48, 15) == F(16, 5)
    assert round((float(yh) - 6)*60) == 8
    assert round(float(-b)*60) == 32            # 0,5333 h ~ 32 min
    assert 1 <= 6 <= 8                          # interpolacion
    # comprobacion independiente con minimos cuadrados directos
    mxf, myf = sum(xs)/n, sum(ys)/n
    sxy = sum((p-mxf)*(q-myf) for p, q in zip(xs, ys))
    sxx = sum((p-mxf)**2 for p in xs)
    syy = sum((q-myf)**2 for q in ys)
    assert ic(sxy/sxx, float(b), rel_tol=1e-12)
    assert ic(myf - (sxy/sxx)*mxf, float(a), rel_tol=1e-12)
    assert ic(sxy/math.sqrt(sxx*syy), r, rel_tol=1e-12)
    # extrapolacion absurda
    assert float(a + b*20) < 0
    # ---------- probabilidad: papeletas
    comb = math.comb(8, 2); assert comb == 28 and 8*7 == 56 and 56//2 == 28
    assert math.perm(8, 2) == 56 and math.comb(8, 2) == math.perm(8, 2)//math.factorial(2)
    assert F(1, 28) and round(float(F(1, 28))*100, 2) == 3.57
    assert F(1, 8)*F(1, 7) == F(1, 56) and round(float(F(1, 56))*100, 2) == 1.79
    assert 2*F(1, 56) == F(1, 28)
    pares = [2, 4, 6, 8]
    import itertools
    todas = list(itertools.combinations(range(1, 9), 2)); assert len(todas) == 28
    A = [p for p in todas if all(v % 2 == 0 for v in p)]
    B = [p for p in todas if 8 in p]
    AB = [p for p in todas if p in A and p in B]
    AuB = [p for p in todas if p in A or p in B]
    assert len(A) == 6 == math.comb(4, 2) and sorted(A) == [(2,4),(2,6),(2,8),(4,6),(4,8),(6,8)]
    assert len(B) == 7 and sorted(B) == [(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8)]
    assert len(AB) == 3 and sorted(AB) == [(2,8),(4,8),(6,8)]
    assert len(AuB) == 10 == 6+7-3
    assert F(6, 28) == F(3, 14) and round(float(F(3, 14))*100, 2) == 21.43
    assert F(7, 28) == F(1, 4)
    assert F(6, 28)+F(7, 28)-F(3, 28) == F(10, 28) == F(5, 14)
    assert round(float(F(5, 14))*100, 2) == 35.71
    assert F(6, 28)+F(7, 28) == F(13, 28)
    # ---------- probabilidad: videos
    PB, PH = F(70, 100), F(30, 100)
    PVB, PVH = F(10, 100), F(20, 100)
    assert PB + PH == 1
    caminos = [PB*PVB, PB*(1-PVB), PH*PVH, PH*(1-PVH)]
    assert caminos == [F(7, 100), F(63, 100), F(6, 100), F(24, 100)]
    assert sum(caminos) == 1
    PV = PB*PVB + PH*PVH; assert PV == F(13, 100)
    assert F(7, 100)+F(6, 100) == F(13, 100)
    PHV = PH*PVH/PV; assert PHV == F(6, 13)
    assert round(float(PHV)*100, 2) == 46.15
    assert PHV != PVH
    assert PVB + F(90, 100) == 1 and PVH + F(80, 100) == 1
    assert PVB + PVH == F(30, 100)   # el error tipico
    print("val() OK")
