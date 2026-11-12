# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'problemas-de-proporcionalidad.pdf'
para bundles/eso_matematicas__mat_proporcionalidad_financiera.json"""
import math
from fractions import Fraction as F

L1 = "01_Razones_y_proporcionalidad_directa.json"
L2 = "02_Proporcionalidad_inversa.json"

EX = {
L1: [
 {"id":"EX-0301-P1","type":"CONTEXT","objective_ids":["LO-0301-3","LO-0301-2"],
  "concept_ids":["C-0301-2"],"difficulty":3,
  "statement":"Un obrero gana $350$ euros a la semana. ¿Cuánto ganará en $45$ días, trabajando al mismo ritmo?",
  "hints":["Antes de plantear la proporción, las dos cantidades de tiempo deben estar en la misma unidad.",
           "Una semana son $7$ días, así que puedes calcular primero lo que gana en un día."],
  "answer":"$2250$ euros.",
  "full_solution":"El error más fácil aquí es comparar semanas con días. Primero se igualan las unidades: $1$ semana $=7$ días, así que el dato es «$350$ euros por cada $7$ días». La relación es directamente proporcional, porque a más días trabajados, más dinero. La constante de proporcionalidad es lo que gana al día: $k=\\dfrac{350}{7}=50$ euros/día. Con ella, en $45$ días gana $50\\cdot 45=2250$ euros. También puede plantearse la proporción $\\dfrac{350}{7}=\\dfrac{x}{45}$, de donde $7x=350\\cdot 45=15\\,750$ y $x=\\dfrac{15\\,750}{7}=2250$ euros. Comprobación: $2250:45=50$ euros al día, el mismo ritmo que al principio.",
  "common_errors":["Plantear $\\dfrac{350}{1}=\\dfrac{x}{45}$ tomando la semana como si fuera un día, lo que da $15\\,750$ euros, siete veces más de lo real.",
                   "Dividir $45$ entre $7$ y quedarse con $6$ semanas, perdiendo los $3$ días sobrantes."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0301-P2","type":"CONTEXT","objective_ids":["LO-0301-3","LO-0301-2"],
  "concept_ids":["C-0301-2"],"difficulty":3,
  "statement":"Un kilogramo de jamón cuesta $7{,}25$ euros. ¿Cuántos gramos de jamón se pueden comprar con $5$ euros? Da el resultado redondeado al gramo y explica por qué no tiene sentido dar todos los decimales.",
  "hints":["Pasa el kilogramo a gramos: $1$ kg $=1000$ g.",
           "Plantea $\\dfrac{1000}{7{,}25}=\\dfrac{x}{5}$."],
  "answer":"Unos $690$ g (exactamente $689{,}655\\ldots$ g).",
  "full_solution":"Se igualan las unidades de peso: $1$ kg son $1000$ g, así que el dato es «$1000$ g cuestan $7{,}25$ euros». A menos dinero, menos jamón: la relación es directamente proporcional. Planteando la proporción $\\dfrac{1000}{7{,}25}=\\dfrac{x}{5}$ se obtiene $7{,}25\\,x=1000\\cdot 5=5000$, de donde $x=\\dfrac{5000}{7{,}25}=689{,}6551\\ldots$ gramos. Redondeando al gramo, unos $690$ g. No tiene sentido escribir $689{,}6551724$ g porque una báscula de charcutería no distingue milésimas de gramo, y porque el dato de partida ($7{,}25$ euros) solo tiene tres cifras significativas: el resultado no puede ser más preciso que los datos. Comprobación: $690$ g a $7{,}25$ euros el kilo cuestan $0{,}690\\cdot 7{,}25=5{,}0025$ euros, prácticamente los $5$ euros disponibles.",
  "common_errors":["Plantear la proporción con $1$ kg y $5$ euros y dar $0{,}69$ como respuesta en gramos, cuando $0{,}69$ es el resultado en kilogramos.",
                   "Invertir la proporción y calcular $\\dfrac{7{,}25\\cdot 5}{1000}$, que da $0{,}036$, un número sin sentido en este contexto."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0301-P3","type":"CONTEXT","objective_ids":["LO-0301-3"],
  "concept_ids":["C-0301-2"],"difficulty":4,
  "statement":"En una copistería, $5$ fotocopias cuestan $40$ céntimos. ¿Cuántas fotocopias se pueden hacer con $8$ euros? Comprueba antes de calcular que el resultado debe ser bastante mayor que $5$.",
  "hints":["Los $40$ céntimos y los $8$ euros deben estar en la misma unidad monetaria.",
           "$40$ céntimos son $0{,}40$ euros."],
  "answer":"$100$ fotocopias.",
  "full_solution":"Como $8$ euros es mucho más que lo que cuestan $5$ fotocopias, el resultado tiene que ser bastante mayor que $5$: esa estimación previa sirve para detectar errores. Para calcularlo hay que poner las dos cantidades de dinero en la misma unidad: $40$ céntimos $=0{,}40$ euros. La relación es directa (más dinero, más fotocopias), así que $\\dfrac{5}{0{,}40}=\\dfrac{x}{8}$, de donde $0{,}40\\,x=5\\cdot 8=40$ y $x=\\dfrac{40}{0{,}40}=100$ fotocopias. Otra vía: cada fotocopia cuesta $0{,}40:5=0{,}08$ euros, y $8:0{,}08=100$. Comprobación: $100$ fotocopias a $0{,}08$ euros son exactamente $8$ euros.",
  "common_errors":["Mezclar unidades y plantear $\\dfrac{5}{40}=\\dfrac{x}{8}$, lo que da $x=1$ fotocopia: un resultado absurdo que la estimación previa habría descartado.",
                   "Pasar los $8$ euros a céntimos pero dejar los $40$ céntimos como euros, duplicando el error de unidades."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0301-P4","type":"CONTEXT","objective_ids":["LO-0301-3","LO-0301-2"],
  "concept_ids":["C-0301-2"],"difficulty":4,
  "statement":"Cada día, en $2$ horas y $10$ minutos de lectura se avanzan $25$ páginas de un libro. Si el libro tiene $275$ páginas, ¿cuánto tiempo total hará falta? Expresa el resultado en horas y minutos.",
  "hints":["Pasa $2$ h $10$ min a minutos antes de plantear la proporción.",
           "Al final, divide los minutos entre $60$ para obtener horas y minutos; el resto son los minutos."],
  "answer":"$1430$ minutos, es decir, $23$ horas y $50$ minutos.",
  "full_solution":"Primero se expresa el tiempo en una sola unidad: $2$ h $=2\\cdot 60=120$ min, y sumando los $10$ min queda $130$ minutos para $25$ páginas. A más páginas, más tiempo: la relación es directa. Planteando $\\dfrac{25}{130}=\\dfrac{275}{x}$ se obtiene $25x=130\\cdot 275=35\\,750$ y $x=\\dfrac{35\\,750}{25}=1430$ minutos. (Más rápido: $275:25=11$ sesiones de $130$ min, y $11\\cdot 130=1430$ min.) Para pasarlo a horas y minutos se divide entre $60$: $1430:60$ da cociente $23$ y resto $50$, porque $23\\cdot 60=1380$ y $1430-1380=50$. Por tanto hacen falta $23$ horas y $50$ minutos.",
  "common_errors":["Escribir el resultado como $23{,}83$ horas y leerlo como «$23$ h y $83$ min»: la parte decimal de las horas no son minutos, hay que multiplicarla por $60$.",
                   "Plantear la proporción con «$2{,}10$ horas» en lugar de $130$ minutos: $2$ h $10$ min son $2{,}1\\overline{6}$ horas, no $2{,}10$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0301-P5","type":"CONTEXT","objective_ids":["LO-0301-2","LO-0301-3"],
  "concept_ids":["C-0301-2"],"difficulty":3,
  "statement":"Una máquina fabrica $400$ tornillos en $5$ horas, a ritmo constante. a) ¿Cuántos tornillos fabrica en $1$ hora y $45$ minutos? b) ¿Cuánto tarda en fabricar $1000$ tornillos? Expresa el tiempo en horas y minutos.",
  "hints":["Calcula primero la constante de proporcionalidad: tornillos por hora.",
           "$1$ h $45$ min son $1{,}75$ horas, porque $45$ min son $\\dfrac{45}{60}=0{,}75$ h."],
  "answer":"a) $140$ tornillos. b) $12{,}5$ horas, es decir, $12$ horas y $30$ minutos.",
  "full_solution":"La constante de proporcionalidad es el ritmo de la máquina: $k=\\dfrac{400}{5}=80$ tornillos por hora. a) $1$ hora y $45$ minutos son $1+\\dfrac{45}{60}=1{,}75$ horas, así que fabrica $80\\cdot 1{,}75=140$ tornillos. b) Para $1000$ tornillos, $t=\\dfrac{1000}{80}=12{,}5$ horas. La parte decimal se convierte multiplicando por $60$: $0{,}5\\cdot 60=30$ minutos, de modo que son $12$ horas y $30$ minutos. Comprobación de b) con una proporción: $\\dfrac{400}{5}=\\dfrac{1000}{t}$ da $400t=5000$ y $t=12{,}5$ horas, el mismo resultado.",
  "common_errors":["Tomar $1$ h $45$ min como $1{,}45$ horas: los minutos hay que dividirlos entre $60$, y $45$ min son $0{,}75$ h.",
                   "Leer $12{,}5$ horas como «$12$ h y $5$ min» en lugar de $12$ h y $30$ min."],
  "provenance":"SOURCE_DERIVED"},
],

L2: [
 {"id":"EX-0302-P1","type":"CONTEXT","objective_ids":["LO-0302-2","LO-0302-3"],
  "concept_ids":["C-0302-2","C-0302-1"],"difficulty":3,
  "statement":"Un granjero tiene pienso para alimentar a sus $12$ vacas durante $45$ días. Si compra $3$ vacas más, ¿cuántos días le durará el mismo pienso?",
  "hints":["Cuidado: el segundo dato no es $3$, sino el número total de vacas después de la compra.",
           "Antes de calcular, decide si el resultado debe ser mayor o menor que $45$ días."],
  "answer":"$36$ días.",
  "full_solution":"Lo primero es leer bien el enunciado: el granjero no pasa a tener $3$ vacas, sino $12+3=15$ vacas. La relación entre número de vacas y días que dura una cantidad fija de pienso es inversamente proporcional, porque el producto «vacas por días» es constante: es la cantidad total de raciones. Como hay más vacas, el pienso durará menos de $45$ días, así que ya se sabe que el resultado tiene que ser menor que $45$. El producto constante es $12\\cdot 45=540$ raciones, de modo que con $15$ vacas se tiene $15\\cdot x=540$ y $x=\\dfrac{540}{15}=36$ días. Comprobación: $15\\cdot 36=540$, el mismo total de raciones.",
  "common_errors":["Usar $3$ como número de vacas y obtener $180$ días: el enunciado dice «$3$ vacas más», así que el total es $15$.",
                   "Plantear la proporción directa $\\dfrac{12}{45}=\\dfrac{15}{x}$, que daría $56{,}25$ días, es decir, más tiempo con más vacas: imposible."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0302-P2","type":"CONTEXT","objective_ids":["LO-0302-1","LO-0302-2"],
  "concept_ids":["C-0302-1","C-0302-2"],"difficulty":3,
  "statement":"Tres amigos ponen $7{,}50$ euros cada uno para comprar un regalo. Si al final participan dos amigos más, ¿cuánto debe poner cada uno? Indica también cuál es la magnitud que permanece constante.",
  "hints":["El precio del regalo no cambia: es el producto «número de amigos por aportación de cada uno».",
           "Participan $3+2=5$ amigos, no $2$."],
  "answer":"$4{,}50$ euros cada uno. La magnitud constante es el precio del regalo, $22{,}50$ euros.",
  "full_solution":"La cantidad que no cambia es el precio del regalo: $3\\cdot 7{,}50=22{,}50$ euros. Ese producto constante es precisamente la señal de que las magnitudes «número de amigos» y «aportación de cada uno» son inversamente proporcionales. Con dos amigos más participan $3+2=5$ personas, así que $5\\cdot x=22{,}50$ y $x=\\dfrac{22{,}50}{5}=4{,}50$ euros. Como hay más gente para pagar lo mismo, cada uno paga menos que antes, lo que confirma el sentido del resultado. Comprobación: $5\\cdot 4{,}50=22{,}50$ euros, el precio del regalo.",
  "common_errors":["Tomar $2$ como número de amigos y obtener $11{,}25$ euros: hay que sumar los nuevos a los que ya estaban.",
                   "Dividir $7{,}50$ entre $5$ y dar $1{,}50$ euros: lo que se reparte entre los cinco es el precio total, no la aportación de uno solo."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0302-P3","type":"CONTEXT","objective_ids":["LO-0302-2"],
  "concept_ids":["C-0302-2","C-0302-1"],"difficulty":4,
  "statement":"Un camión que carga $3000$ kg necesita $15$ viajes para transportar una mercancía. ¿Cuántos viajes necesitará otro camión que carga $4{,}5$ toneladas para transportar la misma mercancía?",
  "hints":["Las dos cargas deben expresarse en la misma unidad: $1$ tonelada $=1000$ kg.",
           "Si cada viaje lleva más carga, el número de viajes debe bajar."],
  "answer":"$10$ viajes.",
  "full_solution":"Primero se igualan las unidades: $3000$ kg $=3$ toneladas. La mercancía total es fija, y es el producto «carga por viaje $\\times$ número de viajes»: $3\\cdot 15=45$ toneladas. Eso confirma que las dos magnitudes son inversamente proporcionales. Para el segundo camión, $4{,}5\\cdot x=45$, de donde $x=\\dfrac{45}{4{,}5}=10$ viajes. El resultado es menor que $15$, como debía ser, porque el segundo camión lleva más carga en cada viaje. Comprobación: $4{,}5\\cdot 10=45$ toneladas, la misma mercancía.",
  "common_errors":["Comparar $3000$ con $4{,}5$ sin convertir las unidades, lo que daría $10\\,000$ viajes.",
                   "Plantear la proporción directa y obtener $22{,}5$ viajes: un camión más grande no puede necesitar más viajes."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0302-P4","type":"CONTEXT","objective_ids":["LO-0302-2","LO-0302-3"],
  "concept_ids":["C-0302-2"],"difficulty":4,
  "statement":"Un coche que va a $72$ km/h tarda $3$ horas y $15$ minutos en hacer un recorrido. ¿Cuánto tardará otro coche en el mismo recorrido si va a $90$ km/h? Expresa el resultado en horas y minutos.",
  "hints":["Pasa $3$ h $15$ min a minutos antes de plantear nada.",
           "A más velocidad, menos tiempo: el resultado debe ser menor que $195$ minutos."],
  "answer":"$156$ minutos, es decir, $2$ horas y $36$ minutos.",
  "full_solution":"Se expresa el tiempo en minutos: $3$ h $=180$ min, y sumando $15$ min son $195$ minutos. A velocidad constante, la distancia es el producto «velocidad por tiempo», y aquí la distancia es la misma para los dos coches, así que velocidad y tiempo son inversamente proporcionales. Como el segundo coche va más rápido, tardará menos de $195$ minutos. Igualando los productos: $72\\cdot 195=90\\cdot x$, es decir, $14\\,040=90x$ y $x=\\dfrac{14\\,040}{90}=156$ minutos. Pasando a horas y minutos: $156:60$ da cociente $2$ y resto $36$, luego $2$ horas y $36$ minutos. Comprobación: la distancia es $72\\cdot\\dfrac{195}{60}=234$ km y también $90\\cdot\\dfrac{156}{60}=234$ km.",
  "common_errors":["Usar $3{,}15$ horas en lugar de $3{,}25$ horas (o de $195$ minutos): $15$ minutos son un cuarto de hora, es decir, $0{,}25$ h.",
                   "Dar la respuesta como $2{,}6$ horas y leerla como $2$ h $6$ min, cuando $0{,}6$ h son $36$ minutos."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0302-P5","type":"REASONING","objective_ids":["LO-0302-3","LO-0302-2"],
  "concept_ids":["C-0302-1","C-0302-2"],"difficulty":3,
  "statement":"Un depósito lleno tarda $24$ minutos en vaciarse abriendo $5$ desagües iguales. Queremos que se vacíe en $15$ minutos. a) Antes de calcular, razona si hará falta abrir más o menos de $5$ desagües. b) Calcula cuántos desagües hay que abrir.",
  "hints":["Piensa qué magnitud es fija: el volumen del depósito.",
           "El producto «número de desagües por tiempo» se mantiene constante."],
  "answer":"a) Más de $5$, porque se quiere vaciar en menos tiempo. b) $8$ desagües.",
  "full_solution":"a) El depósito es el mismo, así que para vaciarlo en menos tiempo hay que sacar agua más rápido, y eso exige más desagües: la respuesta será mayor que $5$. Anticipar el sentido del resultado es la mejor forma de descubrir si la proporción se ha planteado al revés. b) Las magnitudes «número de desagües» y «tiempo de vaciado» son inversamente proporcionales, porque su producto es el volumen total expresado en «desagües-minuto»: $5\\cdot 24=120$. Para que el tiempo sea $15$ minutos: $x\\cdot 15=120$, de donde $x=\\dfrac{120}{15}=8$ desagües. El resultado es mayor que $5$, como se había previsto. Comprobación: $8\\cdot 15=120$, el mismo producto constante.",
  "common_errors":["Plantear la proporción directa $\\dfrac{5}{24}=\\dfrac{x}{15}$, que da $x\\approx 3{,}1$ desagües: menos desagües no pueden vaciar el depósito más rápido.",
                   "Restar los tiempos y pensar que, al bajar $9$ minutos, hay que añadir $9$ desagües: la relación es multiplicativa, no aditiva."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-0302-P6","type":"CONTEXT","objective_ids":["LO-0302-2","LO-0302-3"],
  "concept_ids":["C-0302-2"],"difficulty":4,
  "statement":"Cuatro albañiles tardan $18$ días en arreglar un tejado. Quiero que el tejado esté acabado en $12$ días. ¿Cuántos albañiles tengo que contratar además de los cuatro que ya tengo?",
  "hints":["Calcula primero cuántos albañiles hacen falta en total y después responde a lo que se pregunta.",
           "El producto «albañiles por días» es el trabajo total."],
  "answer":"Hacen falta $6$ albañiles en total, así que hay que contratar $2$ más.",
  "full_solution":"El trabajo total, medido en jornadas de trabajo, es constante: $4\\cdot 18=72$ jornadas. Las magnitudes «número de albañiles» y «días» son inversamente proporcionales. Para acabar en $12$ días hacen falta $x$ albañiles con $x\\cdot 12=72$, de donde $x=\\dfrac{72}{12}=6$ albañiles en total. Pero la pregunta no es cuántos albañiles hacen falta, sino cuántos hay que contratar además de los que ya hay: $6-4=2$ albañiles nuevos. Comprobación: $6\\cdot 12=72$ jornadas, el mismo trabajo total.",
  "common_errors":["Responder $6$ cuando se pregunta cuántos hay que contratar: $6$ es el total necesario, y los nuevos son $6-4=2$.",
                   "Plantear la proporción directa y obtener $\\dfrac{4\\cdot 12}{18}\\approx 2{,}7$ albañiles, es decir, menos personal para acabar antes."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    # L01 P1 obrero
    assert F(350, 7) == 50 and 50*45 == 2250
    assert 350*45 == 15750 and F(15750, 7) == 2250
    assert ic(2250/45, 50)
    # L01 P2 jamon
    x = 1000*5/7.25
    assert ic(x, 689.6551724137931, rel_tol=1e-12)
    assert round(x) == 690 and round(x, 3) == 689.655
    assert ic(0.690*7.25, 5.0025)
    assert ic(7.25*5/1000, 0.036250)
    # L01 P3 fotocopias
    assert ic(5*8/0.40, 100) and ic(0.40/5, 0.08) and ic(8/0.08, 100)
    assert ic(100*0.08, 8)
    assert ic(5*8/40, 1)          # el error de unidades
    # L01 P4 lectura
    assert 2*60 + 10 == 130
    assert 130*275 == 35750 and F(35750, 25) == 1430
    assert 275//25 == 11 and 11*130 == 1430
    assert divmod(1430, 60) == (23, 50) and 23*60 == 1380 and 1430-1380 == 50
    assert ic(1430/60, 23.8333333333, rel_tol=1e-9)
    assert ic(2+10/60, 2.1666666667, rel_tol=1e-9)
    # L01 P5 tornillos
    assert F(400, 5) == 80
    assert ic(1+45/60, 1.75) and ic(80*1.75, 140)
    assert ic(1000/80, 12.5) and ic(0.5*60, 30)
    assert ic(5*1000/400, 12.5)
    # L02 P1 vacas
    assert 12+3 == 15 and 12*45 == 540 and F(540, 15) == 36
    assert 15*36 == 540
    assert ic(12*45/3, 180)                # error: usar 3
    assert ic(45*15/12, 56.25)             # error: proporcion directa
    # L02 P2 regalo
    assert ic(3*7.50, 22.50) and ic(22.50/5, 4.50) and 3+2 == 5
    assert ic(5*4.50, 22.50)
    assert ic(22.50/2, 11.25)              # error: usar 2
    assert ic(7.50/5, 1.50)                # error tipico
    # L02 P3 camion
    assert ic(3000/1000, 3) and 3*15 == 45 and ic(45/4.5, 10)
    assert ic(4.5*10, 45)
    assert ic(3000*15/4.5, 10000)          # error de unidades
    assert ic(4.5*15/3, 22.5)              # error: directa
    # L02 P4 coche
    assert 3*60 + 15 == 195
    assert 72*195 == 14040 and F(14040, 90) == 156
    assert divmod(156, 60) == (2, 36)
    assert ic(72*195/60, 234) and ic(90*156/60, 234)
    assert ic(3+15/60, 3.25) and ic(156/60, 2.6)
    # L02 P5 desagues
    assert 5*24 == 120 and F(120, 15) == 8 and 8*15 == 120
    assert 8 > 5
    assert ic(5*15/24, 3.125)              # error: directa
    # L02 P6 albaniles
    assert 4*18 == 72 and F(72, 12) == 6 and 6-4 == 2 and 6*12 == 72
    assert ic(4*12/18, 2.6666666667, rel_tol=1e-9)
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
