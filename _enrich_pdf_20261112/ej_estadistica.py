# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'Ejercicios de Estadistica.pdf'
para bundles/eso_matematicas__mat_estadistica_descriptiva.json"""
import math
from fractions import Fraction as F

L2 = "02_Tablas_de_frecuencia_y_gráficos.json"
L3 = "03_Medidas_de_centralización_y_posición.json"
L4 = "04_Medidas_de_dispersión.json"
L5 = "05_Dispersión_relativa_caja_y_valores_atípicos.json"

EX = {
L2: [
 {"id":"EX-1202-P1","type":"CONTEXT","objective_ids":["LO-1202-1","LO-1202-2"],
  "concept_ids":["C-1202-1","C-1202-2"],"difficulty":4,
  "statement":"En un reconocimiento médico se ha pesado, en kilogramos, a $30$ niños: $30,\\ 32,\\ 27,\\ 25,\\ 33,\\ 34,\\ 32,\\ 32,\\ 25,\\ 40,\\ 33,\\ 35,\\ 36,\\ 30,\\ 33,\\ 35,\\ 34,\\ 37,\\ 32,\\ 37,\\ 35,\\ 34,\\ 30,\\ 28,\\ 29,\\ 32,\\ 31,\\ 33,\\ 29,\\ 34$. a) Agrupa los datos en intervalos de amplitud $3$ empezando en $24{,}5$ y construye la tabla con frecuencias absolutas y relativas. b) Explica por qué conviene empezar en $24{,}5$ y no en $25$. c) ¿Barras o histograma?",
  "hints":["Los intervalos son $[24{,}5;27{,}5)$, $[27{,}5;30{,}5)$, y así hasta cubrir el dato mayor, que es $40$.",
           "Fíjate en si algún peso cae exactamente sobre un extremo de intervalo."],
  "answer":"a) Frecuencias $3,\\ 6,\\ 10,\\ 8,\\ 2,\\ 1$ (total $30$); relativas $0{,}10$; $0{,}20$; $0{,}3\\overline{3}$; $0{,}2\\overline{6}$; $0{,}0\\overline{6}$; $0{,}0\\overline{3}$. b) Porque así ningún dato entero cae en una frontera y las marcas de clase salen enteras ($26,29,32,35,38,41$). c) Histograma.",
  "full_solution":"a) Con amplitud $3$ desde $24{,}5$ los intervalos son $[24{,}5;27{,}5)$, $[27{,}5;30{,}5)$, $[30{,}5;33{,}5)$, $[33{,}5;36{,}5)$, $[36{,}5;39{,}5)$ y $[39{,}5;42{,}5)$, que cubren desde el peso menor ($25$) hasta el mayor ($40$). Contando: en el primero caen $25,25,27$, o sea $3$ niños; en el segundo $28,29,29,30,30,30$, es decir $6$; en el tercero $31$ y cinco $32$ y cuatro $33$, en total $10$; en el cuarto cuatro $34$, tres $35$ y un $36$, en total $8$; en el quinto los dos $37$, o sea $2$; y en el sexto el $40$, o sea $1$. La suma es $3+6+10+8+2+1=30$, el total de niños, lo que valida el recuento. Las frecuencias relativas se obtienen dividiendo entre $30$: $0{,}10$; $0{,}20$; $0{,}3\\overline{3}$; $0{,}2\\overline{6}$; $0{,}0\\overline{6}$; $0{,}0\\overline{3}$, y suman $1$. b) Si se empezara en $25$ los intervalos serían $[25,28)$, $[28,31)$\\ldots y los pesos $25$, $28$, $31$, $34$, $37$ y $40$ caerían justo en una frontera: habría que decidir a qué clase van y es fácil equivocarse. Empezando en $24{,}5$ ningún dato (todos enteros) coincide con un extremo, y además las marcas de clase son los enteros $26$, $29$, $32$, $35$, $38$ y $41$, cómodas para calcular después la media. c) Al tratarse de una variable cuantitativa continua agrupada en intervalos, el gráfico adecuado es el histograma, con las barras pegadas entre sí, porque el eje horizontal representa una escala continua.",
  "common_errors":["Elegir intervalos con extremos enteros y contar dos veces (o ninguna) los datos que caen en la frontera: por eso los extremos se desplazan medio kilo.",
                   "Representar los datos agrupados con un diagrama de barras separadas: las barras separadas son para variables cualitativas o cuantitativas discretas, no para intervalos."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1202-P2","type":"CONTEXT","objective_ids":["LO-1202-1","LO-1202-3"],
  "concept_ids":["C-1202-1","C-1202-2"],"difficulty":4,
  "statement":"Se han anotado las edades de $30$ personas: $3,\\ 25,\\ 30,\\ 5,\\ 7,\\ 18,\\ 25,\\ 23,\\ 35,\\ 43,\\ 28,\\ 17,\\ 15,\\ 12,\\ 8,\\ 4,\\ 9,\\ 37,\\ 32,\\ 41,\\ 36,\\ 28,\\ 28,\\ 15,\\ 18,\\ 20,\\ 19,\\ 27,\\ 25,\\ 40$. a) Agrúpalas en las clases $0$-$4$, $5$-$9$, $10$-$14$, $15$-$19$, $20$-$24$, $25$-$29$, $30$-$34$, $35$-$39$, $40$-$44$ y da la frecuencia absoluta y la acumulada de cada una. b) ¿Cuál es la amplitud real de cada clase y cuál su marca de clase? c) ¿Cuántas personas tienen menos de $20$ años?",
  "hints":["Una clase como $0$-$4$ contiene las edades $0,1,2,3,4$: eso son cinco valores enteros.",
           "La frecuencia acumulada de una clase es la suma de su frecuencia y de todas las anteriores."],
  "answer":"a) $2,\\ 4,\\ 1,\\ 6,\\ 2,\\ 7,\\ 2,\\ 3,\\ 3$; acumuladas $2,\\ 6,\\ 7,\\ 13,\\ 15,\\ 22,\\ 24,\\ 27,\\ 30$. b) Amplitud $5$; marcas $2,\\ 7,\\ 12,\\ 17,\\ 22,\\ 27,\\ 32,\\ 37,\\ 42$. c) $13$ personas.",
  "full_solution":"a) Contando en cada clase: en $0$-$4$ están $3$ y $4$, o sea $2$ personas; en $5$-$9$ están $5,7,8,9$, o sea $4$; en $10$-$14$ está $12$, o sea $1$; en $15$-$19$ están $15,15,17,18,18,19$, o sea $6$; en $20$-$24$ están $20$ y $23$, o sea $2$; en $25$-$29$ están $25,25,25,27,28,28,28$, o sea $7$; en $30$-$34$ están $30$ y $32$, o sea $2$; en $35$-$39$ están $35,36,37$, o sea $3$; y en $40$-$44$ están $40,41,43$, o sea $3$. Total: $2+4+1+6+2+7+2+3+3=30$, correcto. Las frecuencias acumuladas se van sumando: $2$, $6$, $7$, $13$, $15$, $22$, $24$, $27$ y $30$; la última debe coincidir con el total, y lo hace. b) Aunque la clase se escriba $0$-$4$, al tratarse de edades enteras contiene cinco valores, así que la amplitud real es $5$: el intervalo continuo equivalente es $[-0{,}5;\\,4{,}5)$. La marca de clase es el punto medio: $\\dfrac{-0{,}5+4{,}5}{2}=2$, y de la misma forma salen $7,12,17,22,27,32,37,42$. c) Tener menos de $20$ años es estar en las cuatro primeras clases, cuya frecuencia acumulada es $13$: hay $13$ personas.",
  "common_errors":["Decir que la amplitud de la clase $0$-$4$ es $4$ (restando los extremos escritos): con datos enteros la clase abarca cinco valores y su amplitud real es $5$.",
                   "Calcular la marca de clase de $0$-$4$ como $\\dfrac{0+4}{2}=2$ por casualidad acertando, pero aplicar el mismo criterio a clases desplazadas y equivocarse: la marca es el centro del intervalo continuo."],
  "provenance":"SOURCE_DERIVED"},
],

L3: [
 {"id":"EX-1203-P1","type":"CONTEXT","objective_ids":["LO-1203-1","LO-1203-3"],
  "concept_ids":["C-1203-1"],"difficulty":4,
  "statement":"La tabla recoge edades agrupadas: $[0,5)$ con $3$ personas, $[5,10)$ con $9$, $[10,15)$ con $12$, $[15,20)$ con $9$, $[20,25)$ con $15$ y $[25,30)$ con $2$. a) Calcula la edad media. b) ¿Qué porcentaje tiene menos de $15$ años?",
  "hints":["Con datos agrupados se usa la marca de clase de cada intervalo como valor representativo.",
           "La media ponderada es $\\overline{x}=\\dfrac{\\sum f_ix_i}{N}$, con $N$ el total de personas."],
  "answer":"a) $\\overline{x}=\\dfrac{775}{50}=15{,}5$ años. b) $48\\%$.",
  "full_solution":"a) Primero se calculan las marcas de clase, que son los puntos medios de cada intervalo: $2{,}5$; $7{,}5$; $12{,}5$; $17{,}5$; $22{,}5$ y $27{,}5$. El total de personas es $N=3+9+12+9+15+2=50$. Ahora se multiplica cada marca por su frecuencia y se suma: $3\\cdot 2{,}5=7{,}5$; $9\\cdot 7{,}5=67{,}5$; $12\\cdot 12{,}5=150$; $9\\cdot 17{,}5=157{,}5$; $15\\cdot 22{,}5=337{,}5$; $2\\cdot 27{,}5=55$. La suma es $7{,}5+67{,}5+150+157{,}5+337{,}5+55=775$, de modo que $\\overline{x}=\\dfrac{775}{50}=15{,}5$ años. b) Tener menos de $15$ años significa estar en los tres primeros intervalos, cuyas frecuencias suman $3+9+12=24$ personas. El porcentaje es $\\dfrac{24}{50}\\cdot 100=48\\%$. Nota importante: la media calculada así es aproximada, porque se supone que dentro de cada intervalo los datos se reparten alrededor de la marca de clase; con los datos originales el valor podría variar ligeramente.",
  "common_errors":["Promediar las seis marcas de clase sin ponderar por las frecuencias, lo que daría $15$ en lugar de $15{,}5$ y trataría igual al intervalo de $2$ personas y al de $15$.",
                   "Usar el extremo inferior del intervalo (por ejemplo $0$, $5$, $10$\\ldots) en lugar de la marca de clase, lo que rebaja la media en media amplitud."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1203-P2","type":"REASONING","objective_ids":["LO-1203-1","LO-1203-2"],
  "concept_ids":["C-1203-1","C-1203-2"],"difficulty":4,
  "statement":"Las notas de un examen se reparten así: nota $1$: $1$ alumno; $2$: $1$; $3$: $2$; $4$: $2$; $5$: $6$; $6$: $4$; $7$: $5$; $8$: $3$; $9$: $3$; $10$: $2$. a) Calcula la nota media y la moda. b) ¿Qué porcentaje de alumnos está por encima de la media? Un alumno dice que, por definición de media, debe ser el $50\\%$: comprueba si es cierto.",
  "hints":["No olvides ponderar cada nota por el número de alumnos que la tiene.",
           "Cuenta exactamente cuántos alumnos superan la media y divide entre el total."],
  "answer":"a) $\\overline{x}=\\dfrac{177}{29}\\approx 6{,}10$ y moda $=5$. b) $13$ de $29$ alumnos, es decir, $\\approx 44{,}83\\%$: no es el $50\\%$.",
  "full_solution":"a) El total de alumnos es $N=1+1+2+2+6+4+5+3+3+2=29$. La suma ponderada de las notas es $1\\cdot 1+2\\cdot 1+3\\cdot 2+4\\cdot 2+5\\cdot 6+6\\cdot 4+7\\cdot 5+8\\cdot 3+9\\cdot 3+10\\cdot 2=1+2+6+8+30+24+35+24+27+20=177$. Por tanto $\\overline{x}=\\dfrac{177}{29}\\approx 6{,}103$. La moda es la nota más repetida, que es el $5$ (con $6$ alumnos). b) Estar por encima de la media significa tener más de $6{,}103$, es decir, notas de $7$ en adelante: $5+3+3+2=13$ alumnos. El porcentaje es $\\dfrac{13}{29}\\cdot 100\\approx 44{,}83\\%$, que no es el $50\\%$. La afirmación del alumno confunde la media con la mediana: la mediana (el alumno que ocupa el lugar $15$ al ordenar las $29$ notas) sí deja la mitad por encima y la mitad por debajo, y aquí vale $6$. La media, en cambio, es un reparto equitativo del total y no tiene por qué dejar la mitad de los datos a cada lado; de hecho, con distribuciones asimétricas rara vez lo hace.",
  "common_errors":["Calcular la media como el promedio de los diez valores de nota ($1$ a $10$), que daría $5{,}5$, sin ponderar por el número de alumnos.",
                   "Suponer que la media siempre deja el $50\\%$ de los datos por encima: esa propiedad es de la mediana, no de la media."],
  "provenance":"SOURCE_DERIVED"},
],

L4: [
 {"id":"EX-1204-P1","type":"CONTEXT","objective_ids":["LO-1204-2","LO-1204-1"],
  "concept_ids":["C-1204-2","C-1204-1"],"difficulty":4,
  "statement":"Se pregunta a los alumnos de un autobús escolar por el tiempo, en minutos, que tardan en llegar de casa a la parada: $[0,5)$: $20$ alumnos; $[5,10)$: $13$; $[10,15)$: $18$; $[15,20)$: $5$; $[20,25)$: $4$. a) Calcula la media y la desviación típica. b) ¿Qué porcentaje tarda más de $10$ minutos?",
  "hints":["Usa las marcas de clase $2{,}5$; $7{,}5$; $12{,}5$; $17{,}5$ y $22{,}5$.",
           "Para la varianza resulta cómoda la fórmula $\\sigma^{2}=\\dfrac{\\sum f_ix_i^{2}}{N}-\\overline{x}^{2}$."],
  "answer":"a) $\\overline{x}=\\dfrac{550}{60}\\approx 9{,}17$ min y $\\sigma\\approx 6{,}03$ min. b) $45\\%$.",
  "full_solution":"a) El total es $N=20+13+18+5+4=60$ alumnos. Con las marcas de clase $2{,}5$; $7{,}5$; $12{,}5$; $17{,}5$ y $22{,}5$, la suma ponderada es $20\\cdot 2{,}5+13\\cdot 7{,}5+18\\cdot 12{,}5+5\\cdot 17{,}5+4\\cdot 22{,}5=50+97{,}5+225+87{,}5+90=550$, luego $\\overline{x}=\\dfrac{550}{60}=9{,}1\\overline{6}$ minutos, aproximadamente $9{,}17$. Para la desviación típica se calcula $\\sum f_ix_i^{2}=20\\cdot 6{,}25+13\\cdot 56{,}25+18\\cdot 156{,}25+5\\cdot 306{,}25+4\\cdot 506{,}25=125+731{,}25+2812{,}5+1531{,}25+2025=7225$. Entonces $\\sigma^{2}=\\dfrac{7225}{60}-\\left(9{,}1\\overline{6}\\right)^{2}=120{,}4167-84{,}0278=36{,}3889$, y $\\sigma=\\sqrt{36{,}3889}\\approx 6{,}03$ minutos. b) Tardar más de $10$ minutos corresponde a los tres últimos intervalos: $18+5+4=27$ alumnos, es decir, $\\dfrac{27}{60}\\cdot 100=45\\%$. Observa que $\\sigma$ es grande comparada con la media: los tiempos están muy repartidos, desde casi nada hasta más de $20$ minutos.",
  "common_errors":["Sumar las desviaciones respecto a la media sin elevarlas al cuadrado: esa suma siempre da cero, porque las desviaciones positivas y negativas se compensan.",
                   "Olvidar restar $\\overline{x}^{2}$ al usar la fórmula abreviada, o restar $\\overline{x}$ en lugar de su cuadrado."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1204-P2","type":"REASONING","objective_ids":["LO-1204-2","LO-1204-3"],
  "concept_ids":["C-1204-2"],"difficulty":5,
  "statement":"Con la misma distribución de notas de antes (nota $1$: $1$ alumno; $2$: $1$; $3$: $2$; $4$: $2$; $5$: $6$; $6$: $4$; $7$: $5$; $8$: $3$; $9$: $3$; $10$: $2$, con media $\\overline{x}=\\dfrac{177}{29}\\approx 6{,}103$): a) Calcula la desviación típica. b) ¿Qué porcentaje de alumnos tiene una nota dentro del intervalo $\\left(\\overline{x}-\\sigma,\\ \\overline{x}+\\sigma\\right)$?",
  "hints":["Calcula primero $\\sum f_ix_i^{2}$ y aplica $\\sigma^{2}=\\dfrac{\\sum f_ix_i^{2}}{N}-\\overline{x}^{2}$.",
           "Con $\\sigma$ ya hallada, averigua qué notas enteras caen dentro del intervalo y suma sus frecuencias."],
  "answer":"a) $\\sigma^{2}\\approx 5{,}127$ y $\\sigma\\approx 2{,}264$. b) El intervalo es aproximadamente $(3{,}84;\\ 8{,}37)$, que contiene las notas $4$ a $8$: $20$ alumnos de $29$, es decir, $\\approx 68{,}97\\%$.",
  "full_solution":"a) Se calcula $\\sum f_ix_i^{2}=1\\cdot 1+1\\cdot 4+2\\cdot 9+2\\cdot 16+6\\cdot 25+4\\cdot 36+5\\cdot 49+3\\cdot 64+3\\cdot 81+2\\cdot 100=1+4+18+32+150+144+245+192+243+200=1229$. Con $N=29$ y $\\overline{x}=\\dfrac{177}{29}\\approx 6{,}1034$, la varianza es $\\sigma^{2}=\\dfrac{1229}{29}-\\overline{x}^{2}\\approx 42{,}3793-37{,}2521=5{,}1272$, y la desviación típica $\\sigma=\\sqrt{5{,}1272}\\approx 2{,}264$ puntos. b) El intervalo es $\\left(6{,}1034-2{,}2644;\\ 6{,}1034+2{,}2644\\right)=(3{,}839;\\ 8{,}368)$. Las notas enteras que caen dentro son $4$, $5$, $6$, $7$ y $8$, con frecuencias $2+6+4+5+3=20$ alumnos. El porcentaje es $\\dfrac{20}{29}\\cdot 100\\approx 68{,}97\\%$. Es interesante que salga tan cerca del $68\\%$ que predice la regla empírica para distribuciones aproximadamente simétricas; pero conviene recordar que esa regla es solo orientativa y que aquí el porcentaje se ha obtenido contando alumnos, no aplicando la regla.",
  "common_errors":["Incluir la nota $3$ en el recuento porque 'está casi en $3{,}84$': hay que comparar cada valor con el extremo calculado, no redondear el intervalo.",
                   "Dar la varianza como respuesta cuando se pide la desviación típica: $\\sigma$ es la raíz cuadrada de $\\sigma^{2}$ y se mide en las mismas unidades que los datos."],
  "provenance":"SOURCE_DERIVED"},
],

L5: [
 {"id":"EX-1205-P1","type":"CONTEXT","objective_ids":["LO-1205-1"],
  "concept_ids":["C-1205-1"],"difficulty":4,
  "statement":"El peso medio de la especie animal $A$ es de $21{,}3$ kg con desviación típica $2{,}5$ kg; en la especie $B$ el peso medio es $125$ kg con desviación típica $13$ kg. Calcula el coeficiente de variación de cada una y decide cuál presenta mayor variación relativa en los pesos. ¿Coincide con la que tiene mayor desviación típica?",
  "hints":["El coeficiente de variación es $CV=\\dfrac{\\sigma}{\\overline{x}}$, y suele expresarse en porcentaje.",
           "Compara los dos porcentajes, no las desviaciones típicas en kilogramos."],
  "answer":"$CV_A\\approx 11{,}74\\%$ y $CV_B=10{,}4\\%$: la especie $A$ tiene mayor variación relativa, aunque su desviación típica ($2{,}5$ kg) sea mucho menor que la de $B$ ($13$ kg).",
  "full_solution":"Para la especie $A$: $CV_A=\\dfrac{2{,}5}{21{,}3}\\approx 0{,}1174$, es decir, un $11{,}74\\%$. Para la especie $B$: $CV_B=\\dfrac{13}{125}=0{,}104$, es decir, un $10{,}4\\%$. Como $11{,}74\\%>10{,}4\\%$, la especie $A$ tiene mayor variación relativa: sus pesos se dispersan más en proporción a su tamaño típico. Y no, no coincide con la de mayor desviación típica: $B$ tiene $\\sigma=13$ kg frente a los $2{,}5$ kg de $A$, pero esos $13$ kg son poco para animales que pesan $125$ kg de media, mientras que $2{,}5$ kg son mucho para animales de $21{,}3$ kg. Esto es justo para lo que sirve el coeficiente de variación: al ser un cociente entre dos cantidades con las mismas unidades, es adimensional y permite comparar dispersiones de conjuntos con medias (o incluso unidades) muy distintas.",
  "common_errors":["Concluir que $B$ es más dispersa porque su desviación típica es mayor: en valor absoluto lo es, pero la dispersión relativa se mide con $CV=\\dfrac{\\sigma}{\\overline{x}}$.",
                   "Dar el coeficiente de variación con unidades (por ejemplo $0{,}1174$ kg): es un cociente entre dos cantidades en kilogramos, así que las unidades se cancelan."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-1205-P2","type":"REASONING","objective_ids":["LO-1205-1"],
  "concept_ids":["C-1205-1"],"difficulty":4,
  "statement":"En la clase $A$ la nota media de un examen fue $5{,}5$ con desviación típica $2{,}1$; en la clase $B$, la media fue $7{,}3$ con desviación típica $2{,}6$. a) ¿Qué clase tiene mayor dispersión absoluta? b) Calcula el coeficiente de variación de cada una y di qué clase tiene mayor dispersión relativa. c) Explica por qué las dos respuestas no coinciden.",
  "hints":["La dispersión absoluta se mide con $\\sigma$; la relativa, con $CV=\\dfrac{\\sigma}{\\overline{x}}$.",
           "Calcula los dos cocientes antes de responder a c)."],
  "answer":"a) La clase $B$ ($\\sigma=2{,}6>2{,}1$). b) $CV_A\\approx 38{,}18\\%$ y $CV_B\\approx 35{,}62\\%$: mayor dispersión relativa en $A$. c) Porque $B$ parte de una media más alta, y las mismas décimas de desviación 'pesan' menos sobre una media mayor.",
  "full_solution":"a) En valor absoluto, la clase $B$ está más dispersa, porque $\\sigma_B=2{,}6$ puntos es mayor que $\\sigma_A=2{,}1$ puntos. b) Los coeficientes de variación son $CV_A=\\dfrac{2{,}1}{5{,}5}\\approx 0{,}3818$, es decir, un $38{,}18\\%$, y $CV_B=\\dfrac{2{,}6}{7{,}3}\\approx 0{,}3562$, es decir, un $35{,}62\\%$. Como $38{,}18\\%>35{,}62\\%$, la mayor dispersión relativa corresponde a la clase $A$. c) Las respuestas se invierten porque las dos clases no tienen la misma media. En la clase $A$ los $2{,}1$ puntos de desviación se comparan con una media de $5{,}5$, y suponen más de un tercio de ella; en la clase $B$ los $2{,}6$ puntos se comparan con una media de $7{,}3$, y suponen una fracción menor. Conclusión práctica: comparar desviaciones típicas directamente solo es legítimo cuando las medias son parecidas; en cuanto difieren, hay que usar el coeficiente de variación.",
  "common_errors":["Responder que la clase $B$ es más dispersa en los dos sentidos: con medias distintas, la dispersión absoluta y la relativa pueden ordenarse al contrario.",
                   "Calcular $CV$ como $\\dfrac{\\overline{x}}{\\sigma}$ (media entre desviación): el coeficiente de variación es la desviación típica dividida entre la media."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    # ---------- L02 P1 pesos
    pesos = [30,32,27,25,33,34,32,32,25,40,33,35,36,30,33,35,34,37,32,37,
             35,34,30,28,29,32,31,33,29,34]
    assert len(pesos) == 30 and min(pesos) == 25 and max(pesos) == 40
    bords = [24.5 + 3*i for i in range(7)]
    fr = [len([p for p in pesos if lo <= p < hi]) for lo, hi in zip(bords, bords[1:])]
    assert fr == [3, 6, 10, 8, 2, 1] and sum(fr) == 30
    marcas = [(lo+hi)/2 for lo, hi in zip(bords, bords[1:])]
    assert marcas == [26.0, 29.0, 32.0, 35.0, 38.0, 41.0]
    assert not any(abs(p-b) < 1e-9 for p in pesos for b in bords)
    rel = [F(f, 30) for f in fr]
    assert rel == [F(1, 10), F(1, 5), F(1, 3), F(4, 15), F(1, 15), F(1, 30)]
    assert sum(rel) == 1
    assert ic(float(rel[0]), 0.10) and ic(float(rel[1]), 0.20)
    # frontera entera si se empezara en 25
    b25 = [25 + 3*i for i in range(6)]
    assert sorted(set(p for p in pesos if p in b25)) == [25, 28, 31, 34, 37, 40]
    # ---------- L02 P2 edades
    ed = [3,25,30,5,7,18,25,23,35,43,28,17,15,12,8,4,9,37,32,41,
          36,28,28,15,18,20,19,27,25,40]
    assert len(ed) == 30
    cl = [(0,4),(5,9),(10,14),(15,19),(20,24),(25,29),(30,34),(35,39),(40,44)]
    fr2 = [len([e for e in ed if lo <= e <= hi]) for lo, hi in cl]
    assert fr2 == [2, 4, 1, 6, 2, 7, 2, 3, 3] and sum(fr2) == 30
    acum, s = [], 0
    for f in fr2:
        s += f; acum.append(s)
    assert acum == [2, 6, 7, 13, 15, 22, 24, 27, 30]
    assert [(lo-0.5 + hi+0.5)/2 for lo, hi in cl] == [2,7,12,17,22,27,32,37,42]
    assert all((hi+0.5)-(lo-0.5) == 5 for lo, hi in cl)
    assert acum[3] == 13 == len([e for e in ed if e < 20])
    # ---------- L03 P1 edades agrupadas
    f3 = [3, 9, 12, 9, 15, 2]; x3 = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5]
    N = sum(f3); assert N == 50
    S = sum(f*x for f, x in zip(f3, x3)); assert ic(S, 775.0)
    assert [f*x for f, x in zip(f3, x3)] == [7.5, 67.5, 150.0, 157.5, 337.5, 55.0]
    media = S/N; assert ic(media, 15.5)
    assert sum(f3[:3]) == 24 and ic(24/50*100, 48)
    assert ic(sum(x3)/6, 15.0)     # error: promediar marcas sin ponderar
    # ---------- L03 P2 / L04 P2 notas
    notas = list(range(1, 11)); fn = [1, 1, 2, 2, 6, 4, 5, 3, 3, 2]
    Nn = sum(fn); assert Nn == 29
    Sn = sum(f*x for f, x in zip(fn, notas)); assert Sn == 177
    assert [f*x for f, x in zip(fn, notas)] == [1, 2, 6, 8, 30, 24, 35, 24, 27, 20]
    mn = Sn/Nn; assert ic(mn, 177/29) and round(mn, 3) == 6.103
    assert fn[notas.index(5)] == max(fn)      # moda = 5
    arriba = sum(f for f, x in zip(fn, notas) if x > mn)
    assert arriba == 13 and round(arriba/Nn*100, 2) == 44.83
    # mediana: dato en posicion 15 de 29
    datos = [x for f, x in zip(fn, notas) for _ in range(f)]
    assert len(datos) == 29 and datos[14] == 6
    assert ic(sum(notas)/10, 5.5)             # error: promediar notas sin ponderar
    S2n = sum(f*x*x for f, x in zip(fn, notas)); assert S2n == 1229
    assert [f*x*x for f, x in zip(fn, notas)] == [1, 4, 18, 32, 150, 144, 245, 192, 243, 200]
    varn = S2n/Nn - mn**2
    assert round(S2n/Nn, 4) == 42.3793 and round(mn**2, 4) == 37.2521
    assert round(varn, 4) == 5.1272, varn
    sdn = math.sqrt(varn); assert round(sdn, 3) == 2.264, sdn
    lo, hi = mn - sdn, mn + sdn
    assert round(lo, 3) == 3.839 and round(hi, 3) == 8.368, (lo, hi)
    dentro = [x for x in notas if lo < x < hi]
    assert dentro == [4, 5, 6, 7, 8]
    fd = sum(f for f, x in zip(fn, notas) if lo < x < hi)
    assert fd == 20 and round(fd/Nn*100, 2) == 68.97
    assert not (lo < 3)
    # ---------- L04 P1 autobus
    f4 = [20, 13, 18, 5, 4]; x4 = [2.5, 7.5, 12.5, 17.5, 22.5]
    N4 = sum(f4); assert N4 == 60
    S4 = sum(f*x for f, x in zip(f4, x4)); assert ic(S4, 550.0)
    assert [f*x for f, x in zip(f4, x4)] == [50.0, 97.5, 225.0, 87.5, 90.0]
    m4 = S4/N4; assert ic(m4, 550/60) and round(m4, 2) == 9.17
    S24 = sum(f*x*x for f, x in zip(f4, x4)); assert ic(S24, 7225.0)
    assert [f*x*x for f, x in zip(f4, x4)] == [125.0, 731.25, 2812.5, 1531.25, 2025.0]
    v4 = S24/N4 - m4**2
    assert round(S24/N4, 4) == 120.4167 and round(m4**2, 4) == 84.0278
    assert round(v4, 4) == 36.3889, v4
    s4 = math.sqrt(v4); assert round(s4, 2) == 6.03, s4
    assert sum(f4[2:]) == 27 and ic(27/60*100, 45)
    # ---------- L05 P1 especies
    cva, cvb = 2.5/21.3, 13/125
    assert round(cva*100, 2) == 11.74 and round(cvb*100, 2) == 10.40
    assert cva > cvb and 13 > 2.5
    # ---------- L05 P2 clases
    ca, cb = 2.1/5.5, 2.6/7.3
    assert round(ca*100, 2) == 38.18 and round(cb*100, 2) == 35.62
    assert 2.6 > 2.1 and ca > cb
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
