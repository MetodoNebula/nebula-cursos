# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'tema_2.pdf' (Potencias, raices y logaritmos)
para bundles/eso_matematicas__mat_potencias_raices.json"""
import math
from fractions import Fraction as F

L1 = "01_Potencias_y_sus_propiedades.json"
L2 = "02_Raíces_y_radicales.json"
L3 = "03_Notación_científica_y_orden_de_magnitud.json"
L4 = "04_Operaciones_avanzadas_con_radicales_y_racionalización.json"
L5 = "05_Logaritmos_y_propiedades_operativas.json"

EX = {
L1: [
 {"id":"EX-02-01-P1","type":"STANDARD","objective_ids":["LO-02-01-2","LO-02-01-4"],
  "concept_ids":["C-02-02","C-02-01"],"difficulty":4,
  "statement":"Simplifica $\\dfrac{2^{3}\\cdot 4^{5}\\cdot 3^{4}}{(-9)^{2}\\cdot 6^{3}}$ descomponiendo antes todas las bases en factores primos, y da el resultado como una fracción irreducible.",
  "hints":["Escribe $4=2^2$, $9=3^2$ y $6=2\\cdot 3$ antes de aplicar ninguna propiedad.",
           "Fíjate en que el exponente $2$ de $(-9)^{2}$ es par: el resultado de esa potencia es positivo."],
  "answer":"$\\dfrac{2^{10}}{3^{3}}=\\dfrac{1024}{27}$",
  "full_solution":"Primero se pasa todo a bases primas. En el numerador, $4^{5}=(2^{2})^{5}=2^{10}$, luego el numerador es $2^{3}\\cdot 2^{10}\\cdot 3^{4}=2^{13}\\cdot 3^{4}$. En el denominador, $(-9)^{2}=(-1)^{2}\\cdot 9^{2}=+81=3^{4}$ (el exponente es par, así que el signo menos desaparece) y $6^{3}=(2\\cdot 3)^{3}=2^{3}\\cdot 3^{3}$; por tanto el denominador es $3^{4}\\cdot 2^{3}\\cdot 3^{3}=2^{3}\\cdot 3^{7}$. Ahora se divide base a base: $\\dfrac{2^{13}\\cdot 3^{4}}{2^{3}\\cdot 3^{7}}=2^{13-3}\\cdot 3^{4-7}=2^{10}\\cdot 3^{-3}=\\dfrac{2^{10}}{3^{3}}=\\dfrac{1024}{27}$. Comprobación con valores: el numerador vale $8\\cdot 1024\\cdot 81=663552$ y el denominador $81\\cdot 216=17496$, y en efecto $663552:17496=\\dfrac{1024}{27}$.",
  "common_errors":["Escribir $(-9)^{2}=-81$ y arrastrar un signo negativo que no existe: con exponente par el resultado es positivo.",
                   "Intentar dividir $4^{5}$ entre $6^{3}$ restando exponentes sin descomponer: las propiedades del cociente solo se aplican a potencias de la misma base."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-01-P2","type":"STANDARD","objective_ids":["LO-02-01-2","LO-02-01-4"],
  "concept_ids":["C-02-02","C-02-01"],"difficulty":4,
  "statement":"Simplifica $\\dfrac{5^{2}\\cdot 15^{3}\\cdot 3^{2}}{(-25)^{2}\\cdot 30^{2}}$ y da el resultado como fracción irreducible.",
  "hints":["$15=3\\cdot 5$, $25=5^{2}$ y $30=2\\cdot 3\\cdot 5$.",
           "Agrupa al final las potencias de $2$, de $3$ y de $5$ por separado."],
  "answer":"$\\dfrac{3^{3}}{2^{2}\\cdot 5}=\\dfrac{27}{20}$",
  "full_solution":"Se descompone cada base. Numerador: $15^{3}=(3\\cdot 5)^{3}=3^{3}\\cdot 5^{3}$, así que queda $5^{2}\\cdot 3^{3}\\cdot 5^{3}\\cdot 3^{2}=3^{5}\\cdot 5^{5}$. Denominador: $(-25)^{2}=25^{2}=(5^{2})^{2}=5^{4}$ (exponente par, signo positivo) y $30^{2}=(2\\cdot 3\\cdot 5)^{2}=2^{2}\\cdot 3^{2}\\cdot 5^{2}$, luego el denominador es $2^{2}\\cdot 3^{2}\\cdot 5^{6}$. Dividiendo base a base: $\\dfrac{3^{5}\\cdot 5^{5}}{2^{2}\\cdot 3^{2}\\cdot 5^{6}}=\\dfrac{3^{5-2}\\cdot 5^{5-6}}{2^{2}}=\\dfrac{3^{3}\\cdot 5^{-1}}{2^{2}}=\\dfrac{27}{4\\cdot 5}=\\dfrac{27}{20}$. Comprobación: numerador $25\\cdot 3375\\cdot 9=759375$, denominador $625\\cdot 900=562500$, y $759375:562500=1{,}35=\\dfrac{27}{20}$.",
  "common_errors":["Dejar $5^{-1}$ en el numerador como si fuera un $-5$, en lugar de llevarlo al denominador como $\\dfrac{1}{5}$.",
                   "Olvidar elevar el $2$ y el $3$ de $30$ al cuadrado: $(2\\cdot 3\\cdot 5)^{2}$ eleva los tres factores, no solo el $5$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-01-P3","type":"CONTEXT","objective_ids":["LO-02-01-1","LO-02-01-2"],
  "concept_ids":["C-02-01","C-02-02"],"difficulty":4,
  "statement":"Una hoja de papel tiene $0{,}01$ mm de grosor. Cada vez que se dobla por la mitad, el grosor se duplica, de modo que tras $n$ dobleces el grosor es $0{,}01\\cdot 2^{n}$ mm. a) ¿Qué grosor tiene tras $10$ dobleces? b) ¿Y tras $30$ dobleces, expresado en kilómetros? c) ¿Cuántos dobleces hacen falta para superar $1$ metro de grosor?",
  "hints":["Duplicar $n$ veces es multiplicar por $2^{n}$, no multiplicar por $n$.",
           "En el apartado c), $1$ m son $1000$ mm: hay que buscar el primer $n$ natural con $2^{n}>100000$."],
  "answer":"a) $10{,}24$ mm. b) $0{,}01\\cdot 2^{30}=10\\,737\\,418{,}24$ mm $\\approx 10{,}74$ km. c) $17$ dobleces.",
  "full_solution":"a) Con $n=10$: $0{,}01\\cdot 2^{10}=0{,}01\\cdot 1024=10{,}24$ mm, es decir, poco más de un centímetro. b) Con $n=30$: $2^{30}=1\\,073\\,741\\,824$, luego el grosor es $0{,}01\\cdot 1\\,073\\,741\\,824=10\\,737\\,418{,}24$ mm. Para pasar a kilómetros se divide entre $10^{6}$ (porque $1$ km $=10^{6}$ mm): $10\\,737\\,418{,}24:10^{6}=10{,}73741824$ km, unos $10{,}7$ km, más alto que el Everest. c) Hay que resolver $0{,}01\\cdot 2^{n}>1000$, es decir, $2^{n}>100\\,000$. Como $2^{16}=65\\,536$ (insuficiente) y $2^{17}=131\\,072$ (suficiente), el primer valor que cumple la condición es $n=17$: con $17$ dobleces el grosor es $0{,}01\\cdot 131\\,072=1310{,}72$ mm, algo más de $1$ metro.",
  "common_errors":["Multiplicar por el número de dobleces en lugar de duplicar: con $30$ dobleces el grosor no es $0{,}01\\cdot 30=0{,}3$ mm, sino $0{,}01\\cdot 2^{30}$.",
                   "En el apartado c), dar $n=16$ porque $2^{16}$ 'se parece' a $100\\,000$: hay que comprobar la desigualdad, y $65\\,536$ no supera $100\\,000$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-01-P4","type":"REASONING","objective_ids":["LO-02-01-1"],
  "concept_ids":["C-02-01"],"difficulty":3,
  "statement":"Se dice que $1729$ es el número natural más pequeño que se puede escribir como suma de dos cubos de dos maneras distintas. Comprueba que $1729=10^{3}+9^{3}$ y que también $1729=12^{3}+1^{3}$. Después decide si es cierto que $10^{3}+9^{3}=(10+9)^{3}$.",
  "hints":["Calcula por separado cada cubo y suma; no hay ninguna propiedad que permita sumar cubos agrupando las bases.",
           "Para la última pregunta basta calcular $19^{3}$ y comparar."],
  "answer":"$10^{3}+9^{3}=1000+729=1729$ y $12^{3}+1^{3}=1728+1=1729$. Es falso que $10^{3}+9^{3}=(10+9)^{3}$, porque $19^{3}=6859\\neq 1729$.",
  "full_solution":"Se calculan los cubos uno a uno. $10^{3}=10\\cdot 10\\cdot 10=1000$ y $9^{3}=9\\cdot 9\\cdot 9=729$; su suma es $1000+729=1729$. Por otro lado, $12^{3}=12\\cdot 12\\cdot 12=1728$ y $1^{3}=1$; su suma es $1728+1=1729$. Las dos descomposiciones dan el mismo número, así que la afirmación se cumple. En cambio, $(10+9)^{3}=19^{3}=19\\cdot 19\\cdot 19=6859$, que no es $1729$: la potencia no se reparte sobre una suma, solo sobre un producto o un cociente. Es decir, $(a+b)^{3}\\neq a^{3}+b^{3}$ en general.",
  "common_errors":["Creer que $(a+b)^{n}=a^{n}+b^{n}$: la potencia solo se distribuye sobre productos y cocientes, nunca sobre sumas.",
                   "Calcular $12^{3}$ como $12\\cdot 3=36$, multiplicando la base por el exponente en lugar de multiplicar la base por sí misma tres veces."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-01-P5","type":"STANDARD","objective_ids":["LO-02-01-1","LO-02-01-3"],
  "concept_ids":["C-02-03","C-02-01"],"difficulty":3,
  "statement":"Calcula $\\left(-\\dfrac{2}{5}\\right)^{-2}$ y $\\left(-\\dfrac{2}{5}\\right)^{-3}$, dando los resultados como fracciones, y explica por qué uno sale positivo y el otro negativo.",
  "hints":["Un exponente negativo invierte la fracción: $\\left(\\dfrac{a}{b}\\right)^{-n}=\\left(\\dfrac{b}{a}\\right)^{n}$.",
           "El signo del resultado lo decide la paridad del exponente, no el signo del exponente."],
  "answer":"$\\left(-\\dfrac{2}{5}\\right)^{-2}=\\dfrac{25}{4}$ y $\\left(-\\dfrac{2}{5}\\right)^{-3}=-\\dfrac{125}{8}$.",
  "full_solution":"El exponente negativo significa invertir la base: $\\left(-\\dfrac{2}{5}\\right)^{-2}=\\left(-\\dfrac{5}{2}\\right)^{2}=\\dfrac{(-5)^{2}}{2^{2}}=\\dfrac{25}{4}$, que es positivo porque el exponente $2$ es par y los dos factores negativos se compensan. De la misma forma, $\\left(-\\dfrac{2}{5}\\right)^{-3}=\\left(-\\dfrac{5}{2}\\right)^{3}=\\dfrac{(-5)^{3}}{2^{3}}=\\dfrac{-125}{8}=-\\dfrac{125}{8}$, que es negativo porque el exponente $3$ es impar y queda un factor negativo sin pareja. En resumen: el exponente negativo solo invierte la fracción, y el signo final lo decide si el exponente es par (positivo) o impar (negativo).",
  "common_errors":["Pensar que un exponente negativo hace negativo el resultado: $\\left(-\\dfrac{2}{5}\\right)^{-2}$ es positivo, y vale $\\dfrac{25}{4}$, no $-\\dfrac{25}{4}$.",
                   "Invertir la fracción y además cambiarle el signo, obteniendo $\\dfrac{5}{2}$ en lugar de $-\\dfrac{5}{2}$: el signo de la base no se toca."],
  "provenance":"SOURCE_DERIVED"},
],

L2: [
 {"id":"EX-02-02-P1","type":"STANDARD","objective_ids":["LO-02-02-1","LO-02-02-4"],
  "concept_ids":["C-02-04"],"difficulty":3,
  "statement":"Calcula, si existe en los números reales: a) $\\sqrt[5]{243}$; b) $\\sqrt[4]{-16}$; c) $\\sqrt[3]{3^{9}}$.",
  "hints":["Busca en cada caso qué número elevado al índice da el radicando.",
           "Para c) usa que $\\sqrt[n]{a^{m}}=a^{m/n}$ cuando el índice divide al exponente."],
  "answer":"a) $3$. b) No existe en los reales. c) $27$.",
  "full_solution":"a) Hay que encontrar el número cuya quinta potencia es $243$. Probando: $3^{5}=3\\cdot 3\\cdot 3\\cdot 3\\cdot 3=243$, luego $\\sqrt[5]{243}=3$. b) El índice $4$ es par, y cualquier número real elevado a una potencia par da un resultado positivo o cero; por tanto no hay ningún número real cuya cuarta potencia sea $-16$, y la raíz no existe en los reales. (En cambio $\\sqrt[5]{-32}$ sí existe y vale $-2$, porque el índice es impar.) c) Como el índice $3$ divide al exponente $9$, se puede escribir $\\sqrt[3]{3^{9}}=3^{9/3}=3^{3}=27$. Comprobación: $27^{3}=19683$ y también $3^{9}=19683$.",
  "common_errors":["Dividir el radicando entre el índice: $\\sqrt[5]{243}$ no es $243:5$, sino el número que elevado a $5$ da $243$.",
                   "Dar $\\sqrt[4]{-16}=-2$: $(-2)^{4}=+16$, no $-16$; con índice par y radicando negativo no hay solución real."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-02-P2","type":"CONTEXT","objective_ids":["LO-02-02-1","LO-02-02-4"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"Un cubo tiene un volumen de $2$ metros cúbicos. Calcula su arista y su superficie total, dejando los resultados en forma de radical, y da después el valor aproximado de la superficie con dos decimales.",
  "hints":["De $V=a^{3}$ se despeja $a=\\sqrt[3]{V}$.",
           "La superficie total de un cubo es $S=6a^{2}$, y $\\left(\\sqrt[3]{2}\\right)^{2}=\\sqrt[3]{4}$."],
  "answer":"Arista $a=\\sqrt[3]{2}$ m; superficie $S=6\\sqrt[3]{4}\\ \\text{m}^{2}\\approx 9{,}52\\ \\text{m}^{2}$.",
  "full_solution":"El volumen de un cubo de arista $a$ es $V=a^{3}$. Si $V=2$, entonces $a^{3}=2$ y por tanto $a=\\sqrt[3]{2}$ metros (que no es un número entero: vale aproximadamente $1{,}26$ m). La superficie total son las seis caras cuadradas, $S=6a^{2}$. Ahora $a^{2}=\\left(\\sqrt[3]{2}\\right)^{2}=2^{2/3}=\\sqrt[3]{2^{2}}=\\sqrt[3]{4}$, de modo que $S=6\\sqrt[3]{4}$ metros cuadrados. Para el valor aproximado, $\\sqrt[3]{4}\\approx 1{,}5874$, luego $S\\approx 6\\cdot 1{,}5874=9{,}5244$, es decir, unos $9{,}52$ metros cuadrados.",
  "common_errors":["Elevar al cuadrado el radicando en lugar del radical: $\\left(\\sqrt[3]{2}\\right)^{2}=\\sqrt[3]{4}$, no $\\sqrt[3]{2^{3}}=2$.",
                   "Tomar la arista como $2:3$ al despejar de $a^{3}=2$: hay que extraer la raíz cúbica, no dividir por el exponente."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-02-P3","type":"REASONING","objective_ids":["LO-02-02-4","LO-02-02-2"],
  "concept_ids":["C-02-04"],"difficulty":3,
  "statement":"Escribe tres radicales distintos equivalentes a $\\sqrt[7]{3^{4}}$ y explica qué operación permite generarlos.",
  "hints":["Pasa el radical a potencia de exponente fraccionario: $\\sqrt[7]{3^{4}}=3^{4/7}$.",
           "Una fracción no cambia de valor si se multiplican numerador y denominador por el mismo número."],
  "answer":"Por ejemplo $\\sqrt[14]{3^{8}}$, $\\sqrt[21]{3^{12}}$ y $\\sqrt[28]{3^{16}}$, todos iguales a $3^{4/7}$.",
  "full_solution":"Se escribe el radical como potencia de exponente fraccionario: $\\sqrt[7]{3^{4}}=3^{4/7}$. La clave es que la fracción $\\dfrac{4}{7}$ admite infinitas formas equivalentes: $\\dfrac{4}{7}=\\dfrac{8}{14}=\\dfrac{12}{21}=\\dfrac{16}{28}$. Volviendo a escribir cada una como radical se obtiene $3^{8/14}=\\sqrt[14]{3^{8}}$, $3^{12/21}=\\sqrt[21]{3^{12}}$ y $3^{16/28}=\\sqrt[28]{3^{16}}$. La operación que los genera es multiplicar índice y exponente por el mismo número natural, y por eso el valor no cambia: todos valen aproximadamente $1{,}8734$.",
  "common_errors":["Multiplicar solo el índice (o solo el exponente): $\\sqrt[14]{3^{4}}$ no es igual a $\\sqrt[7]{3^{4}}$, porque $\\dfrac{4}{14}\\neq\\dfrac{4}{7}$.",
                   "Sumar el mismo número a índice y exponente en lugar de multiplicar: $\\dfrac{4+7}{7+7}=\\dfrac{11}{14}$ no es $\\dfrac{4}{7}$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-02-P4","type":"STANDARD","objective_ids":["LO-02-02-1","LO-02-02-4"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"Calcula $\\sqrt{\\sqrt[3]{729}}$ y $\\sqrt[3]{\\sqrt{729}}$. ¿Coinciden? Enuncia la regla que lo explica.",
  "hints":["Resuelve primero la raíz interior en cada caso.",
           "Escribe las dos expresiones como potencias de exponente fraccionario y compara los exponentes."],
  "answer":"Las dos valen $3$. La regla es $\\sqrt[m]{\\sqrt[n]{a}}=\\sqrt[m\\cdot n]{a}$, y el producto de los índices no depende del orden.",
  "full_solution":"En el primer caso, $\\sqrt[3]{729}=9$ porque $9^{3}=729$, y después $\\sqrt{9}=3$. En el segundo, $\\sqrt{729}=27$ porque $27^{2}=729$, y después $\\sqrt[3]{27}=3$. Los dos resultados coinciden y valen $3$. La explicación se ve mejor con exponentes fraccionarios: $\\sqrt{\\sqrt[3]{729}}=\\left(729^{1/3}\\right)^{1/2}=729^{1/6}$ y $\\sqrt[3]{\\sqrt{729}}=\\left(729^{1/2}\\right)^{1/3}=729^{1/6}$. En ambos casos los exponentes se multiplican y dan $\\dfrac{1}{6}$, de modo que una raíz de otra raíz es una sola raíz de índice el producto de los índices: $\\sqrt[m]{\\sqrt[n]{a}}=\\sqrt[m\\cdot n]{a}$. Y efectivamente $3^{6}=729$.",
  "common_errors":["Sumar los índices y calcular $\\sqrt[5]{729}$: en una raíz de otra raíz los índices se multiplican, no se suman.",
                   "Suponer que cambiar el orden de las raíces cambia el resultado: al multiplicarse los índices, el orden es indiferente."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-02-P5","type":"CONTEXT","objective_ids":["LO-02-02-1"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"Dos depósitos cúbicos de agua tienen volúmenes de $1728$ y $4096$ metros cúbicos. a) Calcula la arista de cada uno. b) Halla la razón entre las aristas y la razón entre los volúmenes, y comprueba qué relación hay entre ambas.",
  "hints":["La arista se obtiene con la raíz cúbica del volumen.",
           "Compara la razón de volúmenes con el cubo de la razón de aristas."],
  "answer":"a) $\\sqrt[3]{1728}=12$ m y $\\sqrt[3]{4096}=16$ m. b) Razón de aristas $\\dfrac{12}{16}=\\dfrac{3}{4}$; razón de volúmenes $\\dfrac{1728}{4096}=\\dfrac{27}{64}=\\left(\\dfrac{3}{4}\\right)^{3}$.",
  "full_solution":"a) Como el volumen de un cubo es $V=a^{3}$, la arista es $a=\\sqrt[3]{V}$. Para el primero, $12^{3}=1728$, luego $a_{1}=12$ m. Para el segundo, $16^{3}=4096$, luego $a_{2}=16$ m. b) La razón de las aristas es $\\dfrac{12}{16}$, que simplificando entre $4$ da $\\dfrac{3}{4}$. La razón de los volúmenes es $\\dfrac{1728}{4096}$; simplificando entre $64$ queda $\\dfrac{27}{64}$. Y se observa que $\\left(\\dfrac{3}{4}\\right)^{3}=\\dfrac{3^{3}}{4^{3}}=\\dfrac{27}{64}$, es decir, la razón de volúmenes es el cubo de la razón de las aristas. Tiene sentido: al multiplicar una longitud por un factor $k$, el volumen se multiplica por $k^{3}$.",
  "common_errors":["Suponer que si las aristas están en razón $\\dfrac{3}{4}$, los volúmenes también están en razón $\\dfrac{3}{4}$: en volúmenes la razón se eleva al cubo.",
                   "Calcular la arista dividiendo el volumen entre $3$ en lugar de extraer la raíz cúbica."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-02-P6","type":"CONTEXT","objective_ids":["LO-02-02-1","LO-02-02-4"],
  "concept_ids":["C-02-04"],"difficulty":5,
  "statement":"El diámetro de un balón, medido en centímetros, es un número entero. Se sabe que su volumen está entre $13$ y $17$ decímetros cúbicos. Usando $V=\\dfrac{4}{3}\\pi r^{3}$, averigua qué valores enteros puede tomar el diámetro.",
  "hints":["Pasa primero los volúmenes a centímetros cúbicos: $1$ dm$^{3}=1000$ cm$^{3}$.",
           "Despeja $r=\\sqrt[3]{\\dfrac{3V}{4\\pi}}$ y recuerda que el diámetro es $d=2r$."],
  "answer":"$d$ puede ser $30$ cm o $31$ cm (los extremos dan $d\\approx 29{,}17$ cm y $d\\approx 31{,}90$ cm).",
  "full_solution":"Primero se igualan unidades: $13$ dm$^{3}=13\\,000$ cm$^{3}$ y $17$ dm$^{3}=17\\,000$ cm$^{3}$. De $V=\\dfrac{4}{3}\\pi r^{3}$ se despeja $r^{3}=\\dfrac{3V}{4\\pi}$, es decir, $r=\\sqrt[3]{\\dfrac{3V}{4\\pi}}$, y el diámetro es $d=2r=2\\sqrt[3]{\\dfrac{3V}{4\\pi}}$. Para $V=13\\,000$: $\\dfrac{3\\cdot 13000}{4\\pi}=\\dfrac{39000}{12{,}566}\\approx 3103{,}5$, cuya raíz cúbica es $\\approx 14{,}59$, luego $d\\approx 29{,}17$ cm. Para $V=17\\,000$: $\\dfrac{51000}{12{,}566}\\approx 4058{,}5$, cuya raíz cúbica es $\\approx 15{,}95$, luego $d\\approx 31{,}90$ cm. Por tanto el diámetro está entre $29{,}17$ y $31{,}90$ cm, y los únicos enteros en ese intervalo son $30$ y $31$ centímetros.",
  "common_errors":["Trabajar con $13$ y $17$ directamente en centímetros cúbicos sin convertir los decímetros cúbicos, lo que da un balón de apenas $2{,}9$ cm.",
                   "Dar el radio como respuesta cuando se pregunta el diámetro: hay que duplicar el valor obtenido con la raíz cúbica."],
  "provenance":"SOURCE_DERIVED"},
],

L3: [
 {"id":"EX-02-03-P1","type":"STANDARD","objective_ids":["LO-02-03-1","LO-02-03-4"],
  "concept_ids":["C-02-07","C-02-06"],"difficulty":3,
  "statement":"Indica el orden de magnitud de cada medida: a) masa del protón, $1{,}67\\cdot 10^{-27}$ kg; b) radio medio del Sol, $6{,}96\\cdot 10^{8}$ m; c) tamaño de un virus, $0{,}000\\,000\\,000\\,235$ m; d) radio medio de la órbita terrestre, $1{,}496\\cdot 10^{11}$ m.",
  "hints":["El orden de magnitud es el exponente de $10$ cuando el número está correctamente escrito en notación científica (mantisa entre $1$ y $10$).",
           "En c) cuenta con cuidado los ceros: hay nueve ceros tras la coma antes del $2$."],
  "answer":"a) $-27$. b) $8$. c) $-10$. d) $11$.",
  "full_solution":"El orden de magnitud de una cantidad es el exponente de la potencia de $10$ en su notación científica. a) $1{,}67\\cdot 10^{-27}$ ya está en notación científica y su mantisa $1{,}67$ está entre $1$ y $10$, así que el orden de magnitud es $-27$. b) Igual razonamiento: el orden es $8$. c) Hay que escribir primero el número en notación científica. En $0{,}000\\,000\\,000\\,235$ la primera cifra significativa es el $2$, que ocupa el décimo lugar tras la coma, así que el número es $2{,}35\\cdot 10^{-10}$ y el orden de magnitud es $-10$. d) La mantisa $1{,}496$ está entre $1$ y $10$, luego el orden es $11$. Observa que el orden de magnitud permite comparar de un golpe: el virus y el protón son increíblemente pequeños, pero el protón lo es $10^{17}$ veces más.",
  "common_errors":["Contar los nueve ceros de $0{,}000\\,000\\,000\\,235$ y dar $-9$: el exponente lo marca la posición de la primera cifra significativa, que es la décima.",
                   "Confundir el orden de magnitud con la mantisa y responder $1{,}67$ o $2{,}35$ en lugar del exponente."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-03-P2","type":"CONTEXT","objective_ids":["LO-02-03-1","LO-02-03-3"],
  "concept_ids":["C-02-06","C-02-07"],"difficulty":4,
  "statement":"Usando que mega $=10^{6}$, kilo $=10^{3}$, deci $=10^{-1}$, micro $=10^{-6}$, nano $=10^{-9}$, pico $=10^{-12}$ y giga $=10^{9}$, expresa en notación científica y en la unidad indicada: a) $3$ picoculombios en microculombios; b) $6000$ nanosegundos en milisegundos (mili $=10^{-3}$); c) $0{,}01$ gigagramos en decigramos.",
  "hints":["Pasa primero a la unidad base (culombios, segundos, gramos) y luego divide por el factor de la unidad pedida.",
           "Comprueba al final que la mantisa queda entre $1$ y $10$."],
  "answer":"a) $3\\cdot 10^{-6}\\ \\mu$C. b) $6\\cdot 10^{-3}$ ms. c) $10^{8}$ dg.",
  "full_solution":"a) $3$ picoculombios son $3\\cdot 10^{-12}$ C. Como $1\\ \\mu$C $=10^{-6}$ C, se divide: $\\dfrac{3\\cdot 10^{-12}}{10^{-6}}=3\\cdot 10^{-12+6}=3\\cdot 10^{-6}$ microculombios. b) $6000$ nanosegundos son $6000\\cdot 10^{-9}=6\\cdot 10^{-6}$ s. Dividiendo entre $10^{-3}$ s (un milisegundo): $\\dfrac{6\\cdot 10^{-6}}{10^{-3}}=6\\cdot 10^{-3}$ milisegundos. c) $0{,}01$ gigagramos son $0{,}01\\cdot 10^{9}=10^{-2}\\cdot 10^{9}=10^{7}$ g. Un decigramo es $10^{-1}$ g, así que $\\dfrac{10^{7}}{10^{-1}}=10^{7+1}=10^{8}$ decigramos. En los tres casos la mantisa final está entre $1$ y $10$, así que la notación científica es correcta.",
  "common_errors":["Multiplicar cuando hay que dividir al cambiar de unidad: para pasar de culombios a microculombios se divide entre $10^{-6}$, lo que equivale a multiplicar por $10^{6}$.",
                   "Dejar la respuesta como $6000\\cdot 10^{-9}$ o $0{,}01\\cdot 10^{9}$: eso no es notación científica, porque la mantisa debe estar entre $1$ y $10$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-03-P3","type":"CONTEXT","objective_ids":["LO-02-03-1","LO-02-03-3","LO-02-03-4"],
  "concept_ids":["C-02-06","C-02-07"],"difficulty":5,
  "statement":"Según la leyenda, el inventor del ajedrez pidió $1$ grano de trigo por la primera casilla, $2$ por la segunda, $4$ por la tercera, y así duplicando hasta la casilla $64$; el total es $2^{64}-1=18\\,446\\,744\\,073\\,709\\,551\\,615$ granos. a) Escribe esa cantidad en notación científica (cuatro cifras en la mantisa) e indica su orden de magnitud. b) Si en un kilogramo hay unos $6000$ granos, calcula la masa total en kilogramos y en toneladas, en notación científica.",
  "hints":["Para el orden de magnitud cuenta las cifras del número: si tiene $20$ cifras, el exponente es $19$.",
           "En b) divide la mantisa y resta los exponentes; $1$ tonelada son $10^{3}$ kg."],
  "answer":"a) $\\approx 1{,}845\\cdot 10^{19}$ granos; orden de magnitud $19$. b) $\\approx 3{,}07\\cdot 10^{15}$ kg $\\approx 3{,}07\\cdot 10^{12}$ toneladas.",
  "full_solution":"a) El número $18\\,446\\,744\\,073\\,709\\,551\\,615$ tiene $20$ cifras, así que al correr la coma detrás de la primera cifra hay que compensar con $10^{19}$: queda $1{,}8446744\\ldots\\cdot 10^{19}$, es decir, unos $1{,}845\\cdot 10^{19}$ granos. El orden de magnitud es, por tanto, $19$. b) Si $6000$ granos pesan $1$ kg, la masa total es $\\dfrac{1{,}845\\cdot 10^{19}}{6\\cdot 10^{3}}$ kg. Se divide la mantisa, $1{,}845:6=0{,}3075$, y se restan los exponentes, $19-3=16$: queda $0{,}3075\\cdot 10^{16}$, que normalizado es $3{,}075\\cdot 10^{15}$ kg, unos $3{,}07\\cdot 10^{15}$ kilogramos. Para pasar a toneladas se divide entre $10^{3}$: $3{,}075\\cdot 10^{15}:10^{3}=3{,}075\\cdot 10^{12}$, es decir, más de tres billones de toneladas, muchísimo más que la producción mundial de trigo de un año.",
  "common_errors":["Dar orden de magnitud $20$ porque el número tiene $20$ cifras: un número de $20$ cifras está entre $10^{19}$ y $10^{20}$, así que su orden es $19$.",
                   "Dejar $0{,}3075\\cdot 10^{16}$ como resultado final: hay que normalizar la mantisa a un valor entre $1$ y $10$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-03-P4","type":"CONTEXT","objective_ids":["LO-02-03-1","LO-02-03-3"],
  "concept_ids":["C-02-06"],"difficulty":3,
  "statement":"Una quiniela de $15$ partidos admite $3^{15}$ columnas sencillas distintas. Si cada columna costara $0{,}80$ euros, ¿cuánto habría que gastar para rellenarlas todas? Da el resultado en euros y también en notación científica.",
  "hints":["Calcula primero $3^{15}$ y después multiplica por $0{,}80$.",
           "Para la notación científica, mueve la coma hasta dejar una sola cifra entera."],
  "answer":"$3^{15}=14\\,348\\,907$ columnas; coste $11\\,479\\,125{,}60$ euros $=1{,}147912560\\cdot 10^{7}$ euros (unos $11{,}5$ millones).",
  "full_solution":"Cada partido admite tres resultados ($1$, $X$ o $2$), y hay $15$ partidos independientes, así que el número de columnas es $3^{15}$. Calculándolo por pasos: $3^{5}=243$, $3^{10}=243^{2}=59\\,049$ y $3^{15}=3^{10}\\cdot 3^{5}=59\\,049\\cdot 243=14\\,348\\,907$ columnas. El coste total es $14\\,348\\,907\\cdot 0{,}80=11\\,479\\,125{,}60$ euros. Para escribirlo en notación científica se corre la coma siete lugares a la izquierda: $1{,}14791256\\cdot 10^{7}$ euros, es decir, del orden de $10^{7}$, unos once millones y medio de euros.",
  "common_errors":["Calcular $15^{3}$ en lugar de $3^{15}$: la base es el número de resultados posibles y el exponente el número de partidos.",
                   "Escribir el coste como $11{,}4791256\\cdot 10^{6}$ y llamarlo notación científica correcta: la mantisa debe tener una sola cifra entera, luego es $1{,}14791256\\cdot 10^{7}$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-03-P5","type":"CONTEXT","objective_ids":["LO-02-03-3"],
  "concept_ids":["C-02-06"],"difficulty":3,
  "statement":"En una muestra hay $5{,}23\\cdot 10^{6}$ bacterias y cada una pesa $2{,}5\\cdot 10^{-10}$ gramos. Calcula el peso total de la muestra en notación científica y exprésalo también en miligramos.",
  "hints":["Multiplica las mantisas y suma los exponentes.",
           "Comprueba si hay que normalizar la mantisa; $1$ g $=10^{3}$ mg."],
  "answer":"$1{,}3075\\cdot 10^{-3}$ g, es decir, $1{,}3075$ mg.",
  "full_solution":"Se multiplica el número de bacterias por el peso de cada una: $\\left(5{,}23\\cdot 10^{6}\\right)\\cdot\\left(2{,}5\\cdot 10^{-10}\\right)$. Las mantisas se multiplican, $5{,}23\\cdot 2{,}5=13{,}075$, y los exponentes se suman, $6+(-10)=-4$, lo que da $13{,}075\\cdot 10^{-4}$. Esa mantisa es mayor que $10$, así que hay que normalizar: $13{,}075\\cdot 10^{-4}=1{,}3075\\cdot 10^{-3}$ gramos. Como $1$ gramo son $10^{3}$ miligramos, el peso es $1{,}3075\\cdot 10^{-3}\\cdot 10^{3}=1{,}3075$ mg: poco más de un miligramo para más de cinco millones de bacterias.",
  "common_errors":["Sumar las mantisas o multiplicar los exponentes: al multiplicar potencias de la misma base los exponentes se suman, y las mantisas se multiplican.",
                   "Dar $13{,}075\\cdot 10^{-4}$ como resultado final sin normalizar la mantisa a un valor entre $1$ y $10$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-03-P6","type":"REASONING","objective_ids":["LO-02-03-4","LO-02-03-1"],
  "concept_ids":["C-02-07"],"difficulty":5,
  "statement":"Un alumno dice haber calculado el cuadrado de un número de seis cifras y da como resultado $816\\,302\\,041$. Sin usar calculadora, razona por qué ese resultado es imposible, usando únicamente el orden de magnitud. ¿Cuántas cifras puede tener el cuadrado de un número de seis cifras?",
  "hints":["Un número de seis cifras está entre $100\\,000=10^{5}$ y $1\\,000\\,000=10^{6}$.",
           "Eleva al cuadrado los dos extremos del intervalo y mira entre qué potencias de $10$ cae el resultado."],
  "answer":"El cuadrado de un número de seis cifras está entre $10^{10}$ y $10^{12}$, así que tiene $11$ o $12$ cifras. $816\\,302\\,041$ solo tiene $9$, luego es imposible.",
  "full_solution":"Si un número $n$ tiene seis cifras, entonces $10^{5}\\le n<10^{6}$. Elevando al cuadrado toda la desigualdad (todos los números son positivos, así que el sentido se mantiene): $\\left(10^{5}\\right)^{2}\\le n^{2}<\\left(10^{6}\\right)^{2}$, es decir, $10^{10}\\le n^{2}<10^{12}$. Un número mayor o igual que $10^{10}$ tiene al menos $11$ cifras, y uno menor que $10^{12}$ tiene como máximo $12$; por tanto el cuadrado debe tener $11$ o $12$ cifras. El resultado propuesto, $816\\,302\\,041$, tiene solo $9$ cifras, es decir, es del orden de $10^{8}$: queda muy por debajo del mínimo posible $10^{10}$, así que el alumno se ha equivocado con seguridad. De hecho, $816\\,302\\,041=28\\,571^{2}$, el cuadrado de un número de cinco cifras.",
  "common_errors":["Pensar que el cuadrado de un número de seis cifras tiene doce cifras siempre: puede tener once, porque elevar al cuadrado duplica el exponente pero no garantiza llegar a la siguiente potencia de diez.",
                   "Elevar al cuadrado solo el número de cifras ($6^{2}=36$) en lugar de acotar el número mismo entre potencias de $10$."],
  "provenance":"SOURCE_DERIVED"},
],

L4: [
 {"id":"EX-02-04-P1","type":"STANDARD","objective_ids":["LO-02-04-1","LO-02-04-4"],
  "concept_ids":["C-02-04","C-02-05"],"difficulty":4,
  "statement":"Ordena de menor a mayor los radicales $\\sqrt{7^{3}}$, $\\sqrt[3]{7^{5}}$ y $\\sqrt[4]{7^{5}}$, reduciéndolos antes a índice común.",
  "hints":["Calcula el mínimo común múltiplo de los índices $2$, $3$ y $4$.",
           "Con el mismo índice y la misma base, el mayor radical es el que tiene mayor exponente en el radicando."],
  "answer":"$\\sqrt[4]{7^{5}}<\\sqrt{7^{3}}<\\sqrt[3]{7^{5}}$",
  "full_solution":"El mínimo común múltiplo de $2$, $3$ y $4$ es $12$, así que se pasan los tres a índice $12$ multiplicando índice y exponente por el factor que corresponda. Para $\\sqrt{7^{3}}$ hay que multiplicar por $6$: $\\sqrt{7^{3}}=\\sqrt[12]{7^{18}}$. Para $\\sqrt[3]{7^{5}}$ hay que multiplicar por $4$: $\\sqrt[3]{7^{5}}=\\sqrt[12]{7^{20}}$. Para $\\sqrt[4]{7^{5}}$ hay que multiplicar por $3$: $\\sqrt[4]{7^{5}}=\\sqrt[12]{7^{15}}$. Ahora los tres tienen el mismo índice y la misma base, así que basta comparar los exponentes $15<18<20$. Por tanto $\\sqrt[12]{7^{15}}<\\sqrt[12]{7^{18}}<\\sqrt[12]{7^{20}}$, es decir, $\\sqrt[4]{7^{5}}<\\sqrt{7^{3}}<\\sqrt[3]{7^{5}}$. Comprobación con decimales: $7^{5/4}\\approx 11{,}39$, $7^{3/2}\\approx 18{,}52$ y $7^{5/3}\\approx 25{,}62$.",
  "common_errors":["Ordenar mirando solo el índice (y decir que a mayor índice menor valor) sin tener en cuenta el exponente del radicando.",
                   "Multiplicar solo el índice al reducir a índice común: hay que multiplicar índice y exponente por el mismo número para no cambiar el valor."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-04-P2","type":"STANDARD","objective_ids":["LO-02-04-1","LO-02-04-4"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"Ordena de menor a mayor $\\sqrt[8]{2^{13}}$, $\\sqrt[10]{2^{17}}$ y $\\sqrt[16]{2^{23}}$.",
  "hints":["Pasa cada radical a potencia de exponente fraccionario de base $2$.",
           "Con la misma base mayor que $1$, el mayor número es el que tiene mayor exponente: compara las fracciones."],
  "answer":"$\\sqrt[16]{2^{23}}<\\sqrt[8]{2^{13}}<\\sqrt[10]{2^{17}}$",
  "full_solution":"Se escriben los tres como potencias de base $2$: $\\sqrt[8]{2^{13}}=2^{13/8}$, $\\sqrt[10]{2^{17}}=2^{17/10}$ y $\\sqrt[16]{2^{23}}=2^{23/16}$. Como la base $2$ es mayor que $1$, la función exponencial es creciente y basta ordenar los exponentes. Pasándolos a decimal: $\\dfrac{13}{8}=1{,}625$, $\\dfrac{17}{10}=1{,}7$ y $\\dfrac{23}{16}=1{,}4375$. Luego $1{,}4375<1{,}625<1{,}7$ y el orden es $2^{23/16}<2^{13/8}<2^{17/10}$, es decir, $\\sqrt[16]{2^{23}}<\\sqrt[8]{2^{13}}<\\sqrt[10]{2^{17}}$. Comprobando los valores: $2{,}709$, $3{,}084$ y $3{,}249$ respectivamente.",
  "common_errors":["Comparar directamente los radicandos ($2^{13}$, $2^{17}$, $2^{23}$) olvidando que los índices son distintos.",
                   "Reducir a índice común equivocadamente: si se prefiere ese camino, el mínimo común múltiplo de $8$, $10$ y $16$ es $80$, y hay que escalar cada exponente con el mismo factor que el índice."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-04-P3","type":"CONTEXT","objective_ids":["LO-02-04-4"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"Halla una fórmula que dé el volumen de un cubo a partir de su superficie total $S$, y aplícala a un cubo de superficie total $150\\ \\text{cm}^{2}$.",
  "hints":["De $S=6a^{2}$ despeja la arista $a$.",
           "Después sustituye en $V=a^{3}$ y escribe el resultado con un exponente fraccionario o con un radical."],
  "answer":"$V=\\left(\\dfrac{S}{6}\\right)^{3/2}=\\sqrt{\\left(\\dfrac{S}{6}\\right)^{3}}$; para $S=150\\ \\text{cm}^{2}$, $V=125\\ \\text{cm}^{3}$.",
  "full_solution":"La superficie total de un cubo de arista $a$ son sus seis caras: $S=6a^{2}$. Despejando, $a^{2}=\\dfrac{S}{6}$ y por tanto $a=\\sqrt{\\dfrac{S}{6}}$. El volumen es $V=a^{3}=\\left(\\sqrt{\\dfrac{S}{6}}\\right)^{3}=\\left(\\dfrac{S}{6}\\right)^{3/2}$, que también puede escribirse como $\\sqrt{\\left(\\dfrac{S}{6}\\right)^{3}}$. Aplicándolo a $S=150$: primero $\\dfrac{150}{6}=25$, luego $a=\\sqrt{25}=5$ cm, y el volumen es $V=25^{3/2}=5^{3}=125$ centímetros cúbicos. Comprobación: un cubo de arista $5$ cm tiene superficie $6\\cdot 5^{2}=150\\ \\text{cm}^{2}$ y volumen $125\\ \\text{cm}^{3}$.",
  "common_errors":["Escribir $V=\\left(\\dfrac{S}{6}\\right)^{3}$ olvidando que la arista es la raíz cuadrada de $\\dfrac{S}{6}$, no $\\dfrac{S}{6}$.",
                   "Dividir la superficie entre $6$ al final en lugar de al principio, o dividir el volumen entre $6$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-04-P4","type":"REASONING","objective_ids":["LO-02-04-4","LO-02-04-3"],
  "concept_ids":["C-02-04"],"difficulty":4,
  "statement":"En la igualdad $(a-x)^{2}+b^{2}=c^{2}$ despeja $x$. Indica qué condición deben cumplir $b$ y $c$ para que exista solución real y comprueba el resultado con $a=10$, $b=6$ y $c=10$.",
  "hints":["Aísla primero el cuadrado $(a-x)^{2}$ y después extrae la raíz cuadrada, sin olvidar el doble signo.",
           "Una raíz cuadrada real exige radicando mayor o igual que cero."],
  "answer":"$x=a\\mp\\sqrt{c^{2}-b^{2}}$, con la condición $c^{2}\\ge b^{2}$. Para $a=10$, $b=6$, $c=10$: $x=2$ o $x=18$.",
  "full_solution":"Se aísla el cuadrado pasando $b^{2}$ al otro miembro: $(a-x)^{2}=c^{2}-b^{2}$. Al extraer la raíz cuadrada aparecen dos posibilidades, porque dos números opuestos tienen el mismo cuadrado: $a-x=\\pm\\sqrt{c^{2}-b^{2}}$. Despejando $x$: $x=a\\mp\\sqrt{c^{2}-b^{2}}$, es decir, las dos soluciones $x=a-\\sqrt{c^{2}-b^{2}}$ y $x=a+\\sqrt{c^{2}-b^{2}}$. Para que la raíz exista en los reales hace falta $c^{2}-b^{2}\\ge 0$, o sea $c^{2}\\ge b^{2}$ (con $b,c>0$, basta $c\\ge b$). Con $a=10$, $b=6$ y $c=10$: $c^{2}-b^{2}=100-36=64$ y $\\sqrt{64}=8$, luego $x=10-8=2$ o $x=10+8=18$. Comprobación con $x=2$: $(10-2)^{2}+6^{2}=64+36=100=10^{2}$, correcto; y con $x=18$: $(10-18)^{2}+36=64+36=100$, también correcto.",
  "common_errors":["Perder una de las dos soluciones al extraer la raíz cuadrada: $(a-x)^{2}=k$ da $a-x=+\\sqrt{k}$ y $a-x=-\\sqrt{k}$.",
                   "Escribir $\\sqrt{c^{2}-b^{2}}=c-b$: la raíz no se reparte sobre una resta, y con $c=10$, $b=6$ daría $4$ en lugar de $8$."],
  "provenance":"SOURCE_DERIVED"},
],

L5: [
 {"id":"EX-02-05-P1","type":"CONTEXT","objective_ids":["LO-02-05-4","LO-02-05-3"],
  "concept_ids":["C-02-10","C-02-09"],"difficulty":4,
  "statement":"El nivel de presión sonora en decibelios se calcula con $N=20\\log\\dfrac{p}{2\\cdot 10^{-5}}$, donde $p$ es la presión del sonido en pascales. a) Calcula el nivel de música a mucha potencia, con $p=6{,}4$ Pa. b) Calcula el de un martillo neumático, con $p=1{,}1$ Pa. c) ¿Qué presión corresponde a $120$ dB, el umbral de dolor?",
  "hints":["Divide primero $p$ entre $2\\cdot 10^{-5}$ y después aplica el logaritmo decimal.",
           "En c) hay que deshacer el logaritmo: si $20\\log k=120$, entonces $\\log k=6$ y $k=10^{6}$."],
  "answer":"a) $\\approx 110{,}1$ dB. b) $\\approx 94{,}8$ dB. c) $p=20$ Pa.",
  "full_solution":"a) Se calcula el cociente: $\\dfrac{6{,}4}{2\\cdot 10^{-5}}=\\dfrac{6{,}4}{0{,}00002}=320\\,000$. Su logaritmo decimal es $\\log 320\\,000\\approx 5{,}5052$, y multiplicando por $20$ queda $N\\approx 110{,}10$ dB. b) Ahora $\\dfrac{1{,}1}{2\\cdot 10^{-5}}=55\\,000$, cuyo logaritmo es $\\log 55\\,000\\approx 4{,}7404$; multiplicando por $20$, $N\\approx 94{,}81$ dB. Observa que la presión del martillo es casi seis veces menor que la de la música, pero el nivel en decibelios solo baja unos $15$ dB: la escala es logarítmica. c) Si $N=120$, entonces $20\\log\\dfrac{p}{2\\cdot 10^{-5}}=120$, luego $\\log\\dfrac{p}{2\\cdot 10^{-5}}=6$ y por tanto $\\dfrac{p}{2\\cdot 10^{-5}}=10^{6}$. Despejando, $p=2\\cdot 10^{-5}\\cdot 10^{6}=2\\cdot 10=20$ pascales.",
  "common_errors":["Aplicar el logaritmo a $p$ sin dividir antes entre la presión de referencia $2\\cdot 10^{-5}$.",
                   "En c) dividir $120$ entre $20$ y tomar directamente $p=6$: el $6$ es el logaritmo del cociente, así que hay que deshacer el logaritmo con $10^{6}$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-05-P2","type":"CONTEXT","objective_ids":["LO-02-05-4","LO-02-05-3"],
  "concept_ids":["C-02-10","C-02-09"],"difficulty":4,
  "statement":"El pH de una disolución es $\\mathrm{pH}=-\\log[H^{+}]$, con la concentración en mol/L. Calcula el pH (con una cifra decimal) de la lejía, con $[H^{+}]=1{,}26\\cdot 10^{-13}$; del agua de mar, con $[H^{+}]=10^{-8}$; de la leche, con $[H^{+}]=3{,}16\\cdot 10^{-7}$; y del vinagre, con $[H^{+}]=1{,}26\\cdot 10^{-3}$. Después ordena las cuatro disoluciones de más ácida a menos ácida. (Usa $\\log 1{,}26\\approx 0{,}100$ y $\\log 3{,}16\\approx 0{,}500$.)",
  "hints":["Aplica la propiedad del producto: $-\\log(m\\cdot 10^{-n})=n-\\log m$.",
           "Más ácido significa más concentración de $H^{+}$, y por tanto pH más bajo."],
  "answer":"Lejía $12{,}9$; agua de mar $8{,}0$; leche $6{,}5$; vinagre $2{,}9$. De más ácida a menos ácida: vinagre, leche, agua de mar, lejía.",
  "full_solution":"Se usa que $-\\log\\left(m\\cdot 10^{-n}\\right)=-\\log m-\\log 10^{-n}=n-\\log m$. Lejía: $\\mathrm{pH}=13-\\log 1{,}26\\approx 13-0{,}100=12{,}9$. Agua de mar: $\\mathrm{pH}=-\\log 10^{-8}=8$ exactamente. Leche: $\\mathrm{pH}=7-\\log 3{,}16\\approx 7-0{,}500=6{,}5$. Vinagre: $\\mathrm{pH}=3-\\log 1{,}26\\approx 3-0{,}100=2{,}9$. Para ordenar por acidez hay que recordar que el pH lleva un signo menos delante: a mayor concentración de iones hidrógeno, menor pH, y más ácida es la disolución. La concentración mayor es la del vinagre ($1{,}26\\cdot 10^{-3}$) y la menor la de la lejía ($1{,}26\\cdot 10^{-13}$), así que de más ácida a menos ácida el orden es vinagre ($2{,}9$), leche ($6{,}5$), agua de mar ($8{,}0$) y lejía ($12{,}9$). Las dos primeras son ácidas (pH menor que $7$) y las dos últimas básicas.",
  "common_errors":["Ordenar pensando que a mayor pH mayor acidez: el signo menos de la definición invierte el orden, y la disolución más ácida es la de pH más bajo.",
                   "Calcular $-\\log\\left(1{,}26\\cdot 10^{-13}\\right)$ como $13+\\log 1{,}26$: el logaritmo de la mantisa se resta, porque $-\\log(m\\cdot 10^{-n})=n-\\log m$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-05-P3","type":"REASONING","objective_ids":["LO-02-05-3","LO-02-05-4"],
  "concept_ids":["C-02-10","C-02-09"],"difficulty":5,
  "statement":"Un cultivo de microorganismos crece un $84\\%$ a la semana, de modo que $P=P_{0}\\cdot 1{,}84^{t}$ con $t$ en semanas. a) Halla el factor de crecimiento diario $b$, es decir, el número que cumple $b^{7}=1{,}84$, con cuatro decimales, e indica el porcentaje diario. b) Un libro afirma que ese factor diario es $1{,}097$. Comprueba, elevando a la séptima, que no puede ser correcto. c) ¿Cuántos microorganismos habrá tras $2$ semanas si $P_{0}=1000$?",
  "hints":["Para a) usa logaritmos: de $b^{7}=1{,}84$ se obtiene $\\log b=\\dfrac{\\log 1{,}84}{7}$.",
           "Para b) basta calcular $1{,}097^{7}$ y comparar con $1{,}84$."],
  "answer":"a) $b\\approx 1{,}0910$, un $9{,}10\\%$ diario. b) $1{,}097^{7}\\approx 1{,}9118\\neq 1{,}84$, así que $1{,}097$ es demasiado grande. c) $1000\\cdot 1{,}84^{2}=3385{,}6$, unos $3386$ microorganismos.",
  "full_solution":"a) Una semana son $7$ días, y multiplicar siete veces por el factor diario $b$ debe equivaler a multiplicar por $1{,}84$: $b^{7}=1{,}84$. Tomando logaritmos decimales en los dos miembros, $7\\log b=\\log 1{,}84$, de donde $\\log b=\\dfrac{\\log 1{,}84}{7}\\approx\\dfrac{0{,}264818}{7}\\approx 0{,}0378312$ y por tanto $b\\approx 10^{0{,}0378312}\\approx 1{,}0910$. El crecimiento diario es, pues, de un $9{,}10\\%$ aproximadamente. b) Si el factor diario fuera $1{,}097$, en una semana el cultivo se multiplicaría por $1{,}097^{7}$. Calculándolo: $1{,}097^{2}\\approx 1{,}2034$, $1{,}097^{4}\\approx 1{,}4482$ y $1{,}097^{7}=1{,}097^{4}\\cdot 1{,}097^{2}\\cdot 1{,}097\\approx 1{,}9118$. Eso sería un crecimiento semanal del $91{,}2\\%$, no del $84\\%$, así que el valor $1{,}097$ es incorrecto; el correcto es $1{,}0910$. c) Con el modelo semanal, $P=1000\\cdot 1{,}84^{2}=1000\\cdot 3{,}3856=3385{,}6$, es decir, unos $3386$ microorganismos. Con el factor diario correcto se llega a lo mismo: $1000\\cdot 1{,}0910^{14}\\approx 3385$, mientras que con el erróneo $1{,}097$ saldrían unos $3655$, casi $270$ de más.",
  "common_errors":["Dividir el porcentaje entre $7$ y decir que el crecimiento diario es del $12\\%$: los porcentajes de crecimiento se componen multiplicando factores, no sumando.",
                   "Calcular $1{,}84:7=0{,}2629$ como factor diario, confundiendo la raíz séptima con la división entre $7$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-05-P4","type":"CONTEXT","objective_ids":["LO-02-05-1","LO-02-05-4"],
  "concept_ids":["C-02-09","C-02-10"],"difficulty":4,
  "statement":"Una especie duplica su población cada año. Si parte de $100$ individuos, ¿cuántos años enteros pasarán hasta que la población supere el millón? (Usa $\\log 2\\approx 0{,}30103$.)",
  "hints":["Plantea $100\\cdot 2^{t}>1\\,000\\,000$ y simplifica antes de tomar logaritmos.",
           "El resultado de la ecuación no será entero: piensa si hay que redondear hacia arriba o hacia abajo."],
  "answer":"$t>\\dfrac{4}{\\log 2}\\approx 13{,}29$, así que hacen falta $14$ años.",
  "full_solution":"La población al cabo de $t$ años es $100\\cdot 2^{t}$, y se quiere que supere el millón: $100\\cdot 2^{t}>1\\,000\\,000$. Dividiendo los dos miembros entre $100$ queda $2^{t}>10\\,000$. Tomando logaritmos decimales (la función logaritmo es creciente, así que la desigualdad se conserva): $t\\log 2>\\log 10\\,000=4$, de donde $t>\\dfrac{4}{\\log 2}\\approx\\dfrac{4}{0{,}30103}\\approx 13{,}2877$. Como el tiempo se cuenta en años enteros y la condición es estricta, el primer año que cumple la condición es $t=14$. Comprobación: a los $13$ años la población es $100\\cdot 2^{13}=100\\cdot 8192=819\\,200$, que todavía no llega al millón; a los $14$ años es $100\\cdot 2^{14}=100\\cdot 16\\,384=1\\,638\\,400$, que ya lo supera.",
  "common_errors":["Redondear $13{,}29$ a $13$ años: a los $13$ años la población es $819\\,200$ y aún no supera el millón, así que hay que redondear hacia arriba.",
                   "Olvidar dividir entre $100$ y plantear $2^{t}>1\\,000\\,000$, lo que daría unos $20$ años."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-02-05-P5","type":"STANDARD","objective_ids":["LO-02-05-3"],
  "concept_ids":["C-02-10"],"difficulty":4,
  "statement":"Sabiendo únicamente que $\\log 2\\approx 0{,}30103$, calcula $\\log 40$ y $\\log\\dfrac{5}{4}$ sin usar calculadora.",
  "hints":["Escribe $40=4\\cdot 10=2^{2}\\cdot 10$ y usa que $\\log 10=1$.",
           "Para el segundo, sustituye $5$ por $\\dfrac{10}{2}$ para que todo quede en función de $\\log 2$ y $\\log 10$."],
  "answer":"$\\log 40\\approx 1{,}60206$ y $\\log\\dfrac{5}{4}\\approx 0{,}09691$.",
  "full_solution":"Para el primero se descompone el argumento en factores cuyos logaritmos se conocen: $40=2^{2}\\cdot 10$. Aplicando la propiedad del producto y la de la potencia, $\\log 40=\\log 2^{2}+\\log 10=2\\log 2+1\\approx 2\\cdot 0{,}30103+1=1{,}60206$. Para el segundo conviene reescribir el $5$: como $5=\\dfrac{10}{2}$ y $4=2^{2}$, se tiene $\\dfrac{5}{4}=\\dfrac{10}{2\\cdot 2^{2}}=\\dfrac{10}{2^{3}}$. Entonces, por la propiedad del cociente, $\\log\\dfrac{5}{4}=\\log 10-\\log 2^{3}=1-3\\log 2\\approx 1-3\\cdot 0{,}30103=1-0{,}90309=0{,}09691$. El resultado es positivo y muy pequeño, lo que tiene sentido porque $\\dfrac{5}{4}=1{,}25$ está algo por encima de $1$ y $\\log 1=0$.",
  "common_errors":["Escribir $\\log 40=\\log 4+\\log 10$ y después $\\log 4=4\\log 2$ en lugar de $2\\log 2$: el exponente que sale fuera es el de la potencia, y $4=2^{2}$.",
                   "Calcular $\\log\\dfrac{5}{4}$ como $\\dfrac{\\log 5}{\\log 4}$: el logaritmo de un cociente es la resta de logaritmos, no el cociente de logaritmos."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    # ---- L01 P1
    num = 2**3 * 4**5 * 3**4; den = (-9)**2 * 6**3
    assert num == 663552 and den == 17496
    assert F(num, den) == F(1024, 27) == F(2**10, 3**3)
    # ---- L01 P2
    num = 5**2 * 15**3 * 3**2; den = (-25)**2 * 30**2
    assert num == 759375 and den == 562500
    assert F(num, den) == F(27, 20)
    assert ic(num/den, 1.35)
    # ---- L01 P3 papel
    assert 2**10 == 1024 and ic(0.01*2**10, 10.24)
    assert 2**30 == 1073741824
    assert ic(0.01*2**30, 10737418.24)
    assert ic(0.01*2**30/1e6, 10.73741824)
    assert 2**16 == 65536 and 2**17 == 131072
    assert 2**16 <= 100000 < 2**17            # primer n con 2^n>100000 es 17
    assert ic(0.01*2**17, 1310.72) and 0.01*2**17 > 1000 and 0.01*2**16 < 1000
    # ---- L01 P4 Ramanujan
    assert 10**3 + 9**3 == 1729 == 12**3 + 1**3
    assert 10**3 == 1000 and 9**3 == 729 and 12**3 == 1728
    assert 19**3 == 6859 != 1729
    # ---- L01 P5
    assert F(-2, 5)**-2 == F(25, 4)
    assert F(-2, 5)**-3 == F(-125, 8)
    assert F(-5, 2)**2 == F(25, 4) and F(-5, 2)**3 == F(-125, 8)
    # ---- L02 P1
    assert 3**5 == 243
    assert (-2)**4 == 16            # por eso 4a raiz de -16 no existe
    assert 3**9 == 19683 == 27**3
    assert (-2)**5 == -32
    # ---- L02 P2 cubo V=2
    a = 2**(1/3); assert ic(a, 1.2599210499, rel_tol=1e-9)
    assert ic(a**2, 4**(1/3), rel_tol=1e-12)
    assert ic(4**(1/3), 1.5874010520, rel_tol=1e-9)
    assert ic(6*4**(1/3), 9.5244063118, rel_tol=1e-9)
    assert round(6*4**(1/3), 2) == 9.52
    # ---- L02 P3 radicales equivalentes
    assert F(4, 7) == F(8, 14) == F(12, 21) == F(16, 28)
    assert round(3**(4/7), 4) == 1.8734
    assert not ic(F(4, 14), F(4, 7))
    assert F(11, 14) != F(4, 7)
    # ---- L02 P4 raiz de raiz
    assert 9**3 == 729 and 27**2 == 729 and 3**6 == 729
    assert ic((729**(1/3))**0.5, 3.0, rel_tol=1e-12)
    assert ic((729**0.5)**(1/3), 3.0, rel_tol=1e-12)
    assert ic(729**(1/6), 3.0, rel_tol=1e-12)
    # ---- L02 P5 depositos
    assert 12**3 == 1728 and 16**3 == 4096
    assert F(12, 16) == F(3, 4)
    assert F(1728, 4096) == F(27, 64) == F(3, 4)**3
    # ---- L02 P6 balon
    def diam(V): return 2*(3*V/(4*math.pi))**(1/3)
    d1, d2 = diam(13000), diam(17000)
    assert round(d1, 3) == 29.173, d1
    assert round(d2, 3) == 31.902, d2
    assert [n for n in range(1, 100) if d1 < n < d2] == [30, 31]
    assert round(3*13000/(4*math.pi), 1) == 3103.5
    assert round((3*13000/(4*math.pi))**(1/3), 2) == 14.59
    assert round(3*17000/(4*math.pi), 1) == 4058.5
    assert round((3*17000/(4*math.pi))**(1/3), 2) == 15.95
    # ---- L03 P1 orden de magnitud
    assert f"{0.000000000235:.2e}" == "2.35e-10"
    assert len("000000000") == 9      # nueve ceros tras la coma
    for x, o in [(1.67e-27, -27), (6.96e8, 8), (2.35e-10, -10), (1.496e11, 11)]:
        assert math.floor(math.log10(abs(x))) == o, (x, o)
    # ---- L03 P2 prefijos
    assert ic(3e-12/1e-6, 3e-6)
    assert ic(6000*1e-9, 6e-6) and ic(6e-6/1e-3, 6e-3)
    assert ic(0.01*1e9, 1e7) and ic(1e7/1e-1, 1e8)
    # ---- L03 P3 ajedrez
    T = 2**64 - 1
    assert T == 18446744073709551615
    assert len(str(T)) == 20 and math.floor(math.log10(T)) == 19
    assert ic(T/1e19, 1.8446744073709552, rel_tol=1e-12)
    assert round(T/1e19, 3) == 1.845
    kg = T/6000
    assert ic(kg, 3.0744573456182694e15, rel_tol=1e-9), kg
    assert round(kg/1e15, 2) == 3.07
    assert round(kg/1000/1e12, 2) == 3.07     # toneladas
    assert ic(1.845/6, 0.3075)
    assert sum(2**i for i in range(64)) == 2**64 - 1
    # ---- L03 P4 quiniela
    assert 3**15 == 14348907 and 3**5 == 243 and 3**10 == 59049
    assert 59049*243 == 14348907
    assert ic(14348907*0.80, 11479125.6)
    assert round(14348907*0.8/1e7, 8) == 1.14791256
    assert 15**3 == 3375    # el error tipico
    # ---- L03 P5 bacterias
    assert ic(5.23*2.5, 13.075)
    assert ic(5.23e6*2.5e-10, 1.3075e-3, rel_tol=1e-12)
    assert ic(1.3075e-3*1e3, 1.3075)
    # ---- L03 P6 cifras del cuadrado
    assert 10**10 <= (10**5)**2 and (10**6)**2 == 10**12
    assert len(str(816302041)) == 9
    assert 816302041 == 28571**2 and len(str(28571)) == 5
    for n in (100000, 999999, 123456):
        assert 11 <= len(str(n*n)) <= 12
    assert len(str(123456**2)) == 11 and 123456**2 == 15241383936
    assert 999999**2 == 999998000001 and len(str(999999**2)) == 12
    # ---- L04 P1 ordenar 7
    assert ic(7**1.5, 18.5202591775, rel_tol=1e-9)
    assert round(7**(5/3), 5) == 25.61514
    assert round(7**(5/4), 5) == 11.38604
    assert 7**(5/4) < 7**1.5 < 7**(5/3)
    assert F(3, 2) == F(18, 12) and F(5, 3) == F(20, 12) and F(5, 4) == F(15, 12)
    assert math.lcm(2, 3, 4) == 12
    assert round(7**(5/4), 2) == 11.39 and round(7**1.5, 2) == 18.52 and round(7**(5/3), 2) == 25.62
    # ---- L04 P2 ordenar 2
    assert ic(13/8, 1.625) and ic(17/10, 1.7) and ic(23/16, 1.4375)
    assert 2**(23/16) < 2**(13/8) < 2**(17/10)
    assert round(2**(23/16), 3) == 2.709 and round(2**(13/8), 3) == 3.084 and round(2**(17/10), 3) == 3.249
    assert math.lcm(8, 10, 16) == 80
    # ---- L04 P3 cubo S->V
    assert ic(150/6, 25) and ic(math.sqrt(25), 5) and 5**3 == 125
    assert ic((150/6)**1.5, 125)
    assert 6*5**2 == 150
    # ---- L04 P4 despejar x
    a, b, c = 10, 6, 10
    r = math.sqrt(c**2 - b**2); assert ic(r, 8)
    for x in (a - r, a + r):
        assert ic((a - x)**2 + b**2, c**2)
    assert ic(a - r, 2) and ic(a + r, 18)
    assert c - b == 4 != 8        # el error tipico
    # ---- L05 P1 decibelios
    def N(p): return 20*math.log10(p/2e-5)
    assert ic(6.4/2e-5, 320000)
    assert ic(math.log10(320000), 5.5051499783, rel_tol=1e-9)
    assert round(N(6.4), 2) == 110.10
    assert ic(1.1/2e-5, 55000)
    assert ic(math.log10(55000), 4.7403626895, rel_tol=1e-9)
    assert round(N(1.1), 2) == 94.81
    assert ic(2e-5*1e6, 20) and ic(N(20), 120)
    # ---- L05 P2 pH
    def pH(h): return -math.log10(h)
    assert round(math.log10(1.26), 3) == 0.1 and round(math.log10(3.16), 3) == 0.5
    assert round(pH(1.26e-13), 1) == 12.9
    assert ic(pH(1e-8), 8.0)
    assert round(pH(3.16e-7), 1) == 6.5
    assert round(pH(1.26e-3), 1) == 2.9
    conc = {"vinagre": 1.26e-3, "leche": 3.16e-7, "mar": 1e-8, "lejia": 1.26e-13}
    assert sorted(conc, key=lambda k: -conc[k]) == ["vinagre", "leche", "mar", "lejia"]
    assert sorted(conc, key=lambda k: pH(conc[k])) == ["vinagre", "leche", "mar", "lejia"]
    # ---- L05 P3 crecimiento
    assert ic(math.log10(1.84), 0.2648178230, rel_tol=1e-9)
    assert ic(math.log10(1.84)/7, 0.0378311176, rel_tol=1e-8)
    b7 = 1.84**(1/7)
    assert ic(b7, 10**(math.log10(1.84)/7), rel_tol=1e-12)
    assert round(b7, 4) == 1.0910, b7
    assert round((b7 - 1)*100, 2) == 9.10
    assert round(1.097**7, 4) == 1.9118, 1.097**7
    assert not ic(1.097**7, 1.84, rel_tol=1e-3)
    assert round((1.097**7 - 1)*100, 1) == 91.2
    assert round(1.097**2, 4) == 1.2034 and round(1.097**4, 4) == 1.4482
    assert ic(1.84**2, 3.3856)
    assert ic(1000*1.84**2, 3385.6)
    assert round(1000*b7**14) == 3386 or round(1000*b7**14) == 3385
    assert 3380 < 1000*b7**14 < 3390
    assert 3650 < 1000*1.097**14 < 3660
    assert round(1000*1.097**14 - 1000*1.84**2) == 270 or 265 < 1000*1.097**14-3385.6 < 275
    assert ic(1.84/7, 0.2628571428, rel_tol=1e-8)
    # ---- L05 P4 duplicacion
    assert ic(4/0.30103, 13.2877123, rel_tol=1e-7)
    assert 2**13 == 8192 and 100*8192 == 819200 < 1000000
    assert 2**14 == 16384 and 100*16384 == 1638400 > 1000000
    assert math.ceil(4/math.log10(2)) == 14
    # ---- L05 P5 logaritmos
    assert ic(2*0.30103 + 1, 1.60206)
    assert ic(math.log10(40), 1.6020599913, rel_tol=1e-9)
    assert ic(1 - 3*0.30103, 0.09691)
    assert ic(math.log10(5/4), 0.0969100130, rel_tol=1e-9)
    assert ic(F(5, 4), F(10, 8)) and 2*2**2 == 8 == 2**3
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
