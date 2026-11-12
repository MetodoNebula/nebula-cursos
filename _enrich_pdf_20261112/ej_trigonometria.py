# -*- coding: utf-8 -*-
"""Ejercicios derivados de 'trigonometria.pdf' (81 ejercicios, 4 ESO) y
'7-trigonometria.pdf' para eso_matematicas__mat_trigonometria.json"""
import math
from fractions import Fraction as F

L2 = "02_Resolución_de_triángulos_rectángulos.json"
L3 = "03_Aplicaciones_de_trigonometría.json"
L5 = "05_Relaciones_trigonométricas_fundamentales.json"

EX = {
L2: [
 {"id":"EX-10-02-P1","type":"CONTEXT","objective_ids":["LO-10-02-1","LO-10-02-2"],
  "concept_ids":["C-10-03"],"difficulty":4,
  "statement":"Las diagonales de un rombo miden $12$ cm y $8$ cm. Calcula sus cuatro ángulos y exprésalos en grados, minutos y segundos.",
  "hints":["Las diagonales de un rombo se cortan perpendicularmente en su punto medio, formando cuatro triángulos rectángulos de catetos $6$ y $4$.",
           "Cada diagonal es bisectriz de los ángulos del rombo: el triángulo te da la MITAD del ángulo."],
  "answer":"Dos ángulos de $112^\\circ\\,37'\\,11{,}5''$ (aproximadamente $112^\\circ\\,37'$) y dos de $67^\\circ\\,22'\\,48{,}5''$ (aproximadamente $67^\\circ\\,23'$).",
  "full_solution":"Las diagonales de un rombo son perpendiculares y se cortan en su punto medio, así que lo dividen en cuatro triángulos rectángulos iguales cuyos catetos son las semidiagonales: $\\dfrac{12}{2}=6$ cm y $\\dfrac{8}{2}=4$ cm. En uno de esos triángulos, el ángulo que tiene como cateto opuesto el $6$ y como contiguo el $4$ cumple $\\tan\\theta=\\dfrac{6}{4}=1{,}5$, de donde $\\theta=\\arctan 1{,}5\\approx 56{,}30993^\\circ$. Pero $\\theta$ es solo la mitad del ángulo del rombo, porque la diagonal lo biseca; el ángulo completo es $2\\theta\\approx 112{,}61986^\\circ$. Para pasarlo a grados, minutos y segundos: la parte entera son $112^\\circ$; la parte decimal, $0{,}61986\\cdot 60=37{,}19$ minutos, luego $37'$; y $0{,}19\\cdot 60\\approx 11{,}5$ segundos. Es decir, $112^\\circ\\,37'\\,11{,}5''$. Los otros dos ángulos son suplementarios (los ángulos consecutivos de un rombo suman $180^\\circ$): $180^\\circ-112{,}61986^\\circ=67{,}38014^\\circ$, que en el sistema sexagesimal es $67^\\circ\\,22'\\,48{,}5''$, aproximadamente $67^\\circ\\,23'$. Comprobación: $112{,}61986+67{,}38014=180$, y los cuatro ángulos suman $2(112{,}61986+67{,}38014)=360^\\circ$.",
  "common_errors":["Dar $56{,}31^\\circ$ como ángulo del rombo: el triángulo rectángulo contiene la mitad del ángulo, porque la diagonal actúa de bisectriz.",
                   "Leer $112{,}62^\\circ$ como $112^\\circ\\,62'$: la parte decimal del grado hay que multiplicarla por $60$ para obtener los minutos, y $0{,}62\\cdot 60\\approx 37$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-02-P2","type":"STANDARD","objective_ids":["LO-10-02-1","LO-10-02-2"],
  "concept_ids":["C-10-03"],"difficulty":4,
  "statement":"Resuelve, sin calculadora, el triángulo rectángulo en $A$ cuyos catetos miden $b=\\sqrt{3}$ y $c=1$ (es decir, halla la hipotenusa $a$ y los ángulos $B$ y $C$) y calcula su área.",
  "hints":["Usa el teorema de Pitágoras para la hipotenusa; el resultado es exacto.",
           "Recuerda los valores exactos: $\\tan 60^\\circ=\\sqrt{3}$ y $\\tan 30^\\circ=\\dfrac{1}{\\sqrt{3}}$."],
  "answer":"$a=2$, $B=60^\\circ$, $C=30^\\circ$ y área $=\\dfrac{\\sqrt{3}}{2}\\approx 0{,}866$ unidades cuadradas.",
  "full_solution":"Como el ángulo recto está en $A$, los catetos son $b$ y $c$ y la hipotenusa es $a$. Por el teorema de Pitágoras, $a^{2}=b^{2}+c^{2}=\\left(\\sqrt{3}\\right)^{2}+1^{2}=3+1=4$, luego $a=2$ exactamente. Para el ángulo $B$, su cateto opuesto es $b=\\sqrt{3}$ y el contiguo $c=1$, así que $\\tan B=\\dfrac{\\sqrt{3}}{1}=\\sqrt{3}$, y el ángulo agudo cuya tangente es $\\sqrt{3}$ es $B=60^\\circ$. El tercer ángulo sale sin más cálculo, porque los dos agudos de un triángulo rectángulo son complementarios: $C=90^\\circ-60^\\circ=30^\\circ$. Se puede comprobar con otra razón: $\\sin C=\\dfrac{c}{a}=\\dfrac{1}{2}$, y en efecto $\\sin 30^\\circ=\\dfrac{1}{2}$. El área de un triángulo rectángulo es el semiproducto de los catetos: $S=\\dfrac{b\\cdot c}{2}=\\dfrac{\\sqrt{3}\\cdot 1}{2}=\\dfrac{\\sqrt{3}}{2}\\approx 0{,}866$.",
  "common_errors":["Usar la hipotenusa como uno de los catetos en el área: el semiproducto que da el área es el de los dos catetos, no el de un cateto por la hipotenusa.",
                   "Calcular $C$ con una nueva razón trigonométrica y arrastrar errores de redondeo, cuando basta con $C=90^\\circ-B$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-02-P3","type":"CONTEXT","objective_ids":["LO-10-02-1","LO-10-02-2"],
  "concept_ids":["C-10-03"],"difficulty":4,
  "statement":"Las dos ramas de un compás miden $11{,}5$ cm cada una. Si las puntas distan $6{,}25$ cm, ¿qué ángulo forman las ramas? Da el resultado en grados y minutos.",
  "hints":["El compás abierto forma un triángulo isósceles; traza la altura desde el vértice para partirlo en dos triángulos rectángulos iguales.",
           "En cada mitad, el cateto opuesto al semiángulo es $\\dfrac{6{,}25}{2}$ y la hipotenusa es $11{,}5$."],
  "answer":"Aproximadamente $31{,}54^\\circ$, es decir, $31^\\circ\\,32'$.",
  "full_solution":"Las dos ramas iguales y la distancia entre las puntas forman un triángulo isósceles de lados $11{,}5$, $11{,}5$ y $6{,}25$ cm. La altura trazada desde el vértice (la articulación del compás) es también bisectriz del ángulo buscado y mediatriz del lado desigual, de modo que parte el triángulo en dos triángulos rectángulos iguales. En cada uno de ellos, llamando $\\theta$ al semiángulo, el cateto opuesto es $\\dfrac{6{,}25}{2}=3{,}125$ cm y la hipotenusa es $11{,}5$ cm, así que $\\sin\\theta=\\dfrac{3{,}125}{11{,}5}\\approx 0{,}271739$ y $\\theta\\approx 15{,}76778^\\circ$. El ángulo que forman las ramas es el doble: $2\\theta\\approx 31{,}53556^\\circ$. Pasándolo a minutos: $0{,}53556\\cdot 60\\approx 32{,}1$, luego el ángulo es aproximadamente $31^\\circ\\,32'$. Comprobación: con un ángulo de $31{,}53556^\\circ$ entre ramas de $11{,}5$ cm, la distancia entre puntas es $2\\cdot 11{,}5\\cdot\\sin\\left(15{,}76778^\\circ\\right)=6{,}25$ cm, el dato de partida.",
  "common_errors":["Usar el seno con el lado completo de $6{,}25$ cm y la hipotenusa de $11{,}5$ cm: en el triángulo rectángulo el cateto es la MITAD del lado desigual.",
                   "Olvidar duplicar el semiángulo y responder $15{,}77^\\circ$."],
  "provenance":"SOURCE_DERIVED"},
],

L3: [
 {"id":"EX-10-03-P1","type":"CONTEXT","objective_ids":["LO-10-03-1"],
  "concept_ids":["C-10-05"],"difficulty":4,
  "statement":"En un tramo de carretera la pendiente es del $6\\%$, lo que significa que se asciende $6$ m por cada $100$ m medidos en horizontal. Un ciclista recorre $1$ km de carretera. a) ¿Qué ángulo forma la carretera con la horizontal? b) ¿Cuánto asciende realmente el ciclista, si ese kilómetro es la distancia recorrida sobre el asfalto? c) ¿Cuánto habría ascendido si el kilómetro fuese el avance horizontal?",
  "hints":["La pendiente en tanto por ciento es $100\\tan\\alpha$, no el ángulo ni el seno.",
           "En b) el kilómetro es la hipotenusa del triángulo; en c) es el cateto horizontal."],
  "answer":"a) $\\alpha=\\arctan 0{,}06\\approx 3{,}4336^\\circ$. b) $1000\\sin\\alpha\\approx 59{,}9$ m. c) $1000\\cdot 0{,}06=60$ m exactos.",
  "full_solution":"a) Una pendiente del $6\\%$ significa que el cociente entre el desnivel y el avance horizontal es $\\dfrac{6}{100}=0{,}06$. Ese cociente es precisamente la tangente del ángulo de inclinación, así que $\\tan\\alpha=0{,}06$ y $\\alpha=\\arctan 0{,}06\\approx 3{,}4336^\\circ$: una cuesta que en el mapa parece suave. b) Si el kilómetro recorrido se mide sobre el asfalto, ese kilómetro es la hipotenusa, y el desnivel es el cateto opuesto: desnivel $=1000\\cdot\\sin\\left(3{,}4336^\\circ\\right)\\approx 1000\\cdot 0{,}059892=59{,}89$ m, es decir, unos $59{,}9$ metros. c) Si el kilómetro fuese el avance horizontal, el desnivel sería el cateto opuesto obtenido con la tangente: $1000\\cdot\\tan\\alpha=1000\\cdot 0{,}06=60$ m exactos. La diferencia entre los dos casos es de apenas $11$ centímetros, porque con ángulos tan pequeños el seno y la tangente casi coinciden; pero conviene saber cuál es cuál, porque con pendientes grandes la diferencia sí importa: al $30\\%$, por ejemplo, serían $287{,}3$ m frente a $300$ m.",
  "common_errors":["Interpretar el $6\\%$ como que el ángulo mide $6^\\circ$: el porcentaje es la tangente multiplicada por $100$, y aquí el ángulo es de solo $3{,}43^\\circ$.",
                   "Multiplicar el kilómetro recorrido sobre el asfalto directamente por $0{,}06$: eso vale cuando el kilómetro es horizontal, porque la tangente relaciona el desnivel con el cateto horizontal, no con la hipotenusa."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-03-P2","type":"CONTEXT","objective_ids":["LO-10-03-1"],
  "concept_ids":["C-10-05"],"difficulty":5,
  "statement":"Un pentágono regular está inscrito en una circunferencia de radio $10$ cm. Calcula la longitud de su lado, su apotema y su área, con cuatro decimales.",
  "hints":["Une el centro con dos vértices consecutivos: el ángulo central es $\\dfrac{360^\\circ}{5}$, y la apotema lo divide en dos mitades iguales.",
           "En el triángulo rectángulo resultante, la hipotenusa es el radio y el semiángulo central es $36^\\circ$."],
  "answer":"Lado $\\approx 11{,}7557$ cm, apotema $\\approx 8{,}0902$ cm y área $\\approx 237{,}7641\\ \\text{cm}^{2}$.",
  "full_solution":"Al unir el centro con dos vértices consecutivos se obtiene un triángulo isósceles cuyo ángulo central mide $\\dfrac{360^\\circ}{5}=72^\\circ$ y cuyos lados iguales son el radio, $10$ cm. La apotema es la altura de ese triángulo sobre el lado del pentágono, y al ser también bisectriz y mediatriz lo divide en dos triángulos rectángulos con semiángulo central $\\dfrac{72^\\circ}{2}=36^\\circ$, hipotenusa $10$ cm, cateto opuesto igual a la mitad del lado y cateto contiguo igual a la apotema. Entonces la mitad del lado es $10\\sin 36^\\circ\\approx 5{,}8779$, luego el lado completo es $2\\cdot 10\\sin 36^\\circ\\approx 11{,}7557$ cm. La apotema es $10\\cos 36^\\circ\\approx 8{,}0902$ cm. El área de un polígono regular es $\\dfrac{\\text{perímetro}\\cdot\\text{apotema}}{2}$: el perímetro es $5\\cdot 11{,}7557=58{,}7785$ cm, así que $S=\\dfrac{58{,}7785\\cdot 8{,}0902}{2}\\approx 237{,}7641\\ \\text{cm}^{2}$. Comprobación con otra vía: el área también es cinco veces el área de uno de los triángulos centrales, $5\\cdot\\dfrac{1}{2}\\cdot 10^{2}\\cdot\\sin 72^\\circ\\approx 237{,}7641$, el mismo valor.",
  "common_errors":["Usar el ángulo central completo ($72^\\circ$) en el triángulo rectángulo: la apotema lo parte por la mitad, así que el ángulo que interviene es $36^\\circ$.",
                   "Tomar el radio como apotema: el radio llega a un vértice y la apotema al punto medio de un lado, y aquí valen $10$ y $8{,}09$ cm respectivamente."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-03-P3","type":"CONTEXT","objective_ids":["LO-10-03-1"],
  "concept_ids":["C-10-05"],"difficulty":5,
  "statement":"Calcula la apotema y el área de un decágono regular de $20$ cm de lado, con cuatro decimales.",
  "hints":["El ángulo central es $\\dfrac{360^\\circ}{10}=36^\\circ$, y la apotema lo divide en dos ángulos de $18^\\circ$.",
           "Ahora el dato conocido es el cateto opuesto (la mitad del lado), así que conviene usar la tangente."],
  "answer":"Apotema $\\approx 30{,}7768$ cm y área $\\approx 3077{,}6835\\ \\text{cm}^{2}$.",
  "full_solution":"El ángulo central del decágono es $\\dfrac{360^\\circ}{10}=36^\\circ$, y la apotema lo divide en dos ángulos de $18^\\circ$. En el triángulo rectángulo que forman la apotema, la mitad del lado y el radio, el cateto opuesto al ángulo de $18^\\circ$ es $\\dfrac{20}{2}=10$ cm y el cateto contiguo es la apotema $ap$. Por tanto $\\tan 18^\\circ=\\dfrac{10}{ap}$, de donde $ap=\\dfrac{10}{\\tan 18^\\circ}\\approx\\dfrac{10}{0{,}324920}\\approx 30{,}7768$ cm. El perímetro es $10\\cdot 20=200$ cm, así que el área es $S=\\dfrac{200\\cdot 30{,}7768}{2}\\approx 3077{,}6835\\ \\text{cm}^{2}$. Observa que la apotema es bastante mayor que el lado: en un polígono de muchos lados el centro queda lejos de cada lado, y el decágono se parece ya bastante a un círculo (un círculo de la misma área tendría radio $\\approx 31{,}3$ cm, muy cerca de la apotema).",
  "common_errors":["Usar el seno en lugar de la tangente: el dato conocido es un cateto (la mitad del lado) y la incógnita es el otro cateto (la apotema), no la hipotenusa.",
                   "Calcular el área como $\\dfrac{\\text{lado}\\cdot\\text{apotema}}{2}$: en la fórmula aparece el perímetro completo, que aquí es $200$ cm."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-03-P4","type":"CONTEXT","objective_ids":["LO-10-03-1"],
  "concept_ids":["C-10-05"],"difficulty":4,
  "statement":"Determina la superficie de un hexágono regular inscrito en una circunferencia de $9$ cm de radio, con cuatro decimales, y comprueba el resultado por un segundo camino.",
  "hints":["En el hexágono regular el lado coincide con el radio: compruébalo mirando el ángulo central.",
           "La apotema es $9\\cos 30^\\circ$."],
  "answer":"$S\\approx 210{,}4442\\ \\text{cm}^{2}$ (que es $\\dfrac{3\\sqrt{3}}{2}\\cdot 9^{2}$).",
  "full_solution":"El ángulo central del hexágono es $\\dfrac{360^\\circ}{6}=60^\\circ$, así que cada triángulo centro-vértice-vértice tiene un ángulo de $60^\\circ$ entre dos lados iguales (los radios): es equilátero, y por eso el lado del hexágono coincide con el radio, $9$ cm. La apotema es la altura de ese triángulo equilátero: con el semiángulo central de $30^\\circ$, $ap=9\\cos 30^\\circ=9\\cdot\\dfrac{\\sqrt{3}}{2}\\approx 7{,}7942$ cm. El perímetro es $6\\cdot 9=54$ cm, luego $S=\\dfrac{54\\cdot 7{,}7942}{2}\\approx 210{,}4442\\ \\text{cm}^{2}$. Segundo camino: el hexágono son seis triángulos equiláteros de lado $9$, y el área de un triángulo equilátero de lado $\\ell$ es $\\dfrac{\\sqrt{3}}{4}\\ell^{2}$, así que $S=6\\cdot\\dfrac{\\sqrt{3}}{4}\\cdot 81=\\dfrac{3\\sqrt{3}}{2}\\cdot 81\\approx 210{,}4442\\ \\text{cm}^{2}$, el mismo valor, lo que confirma el cálculo.",
  "common_errors":["Suponer que el lado del hexágono es distinto del radio sin comprobar el ángulo central: en el hexágono regular (y solo en él) coinciden.",
                   "Confundir apotema y radio al aplicar la fórmula del área, lo que daría $\\dfrac{54\\cdot 9}{2}=243\\ \\text{cm}^{2}$, un valor demasiado grande."],
  "provenance":"SOURCE_DERIVED"},
],

L5: [
 {"id":"EX-10-05-P1","type":"REASONING","objective_ids":["LO-10-05-1"],
  "concept_ids":["C-10-08"],"difficulty":4,
  "statement":"¿Puede existir un ángulo tal que $\\sin\\alpha=\\dfrac{1}{5}$ y $\\cos\\alpha=\\dfrac{3}{5}$? Justifícalo sin calculadora y, si la respuesta es que no, corrige el valor del coseno suponiendo que el seno es correcto y el ángulo es agudo.",
  "hints":["Comprueba si esos dos valores cumplen la identidad fundamental $\\sin^{2}\\alpha+\\cos^{2}\\alpha=1$.",
           "Si el seno es correcto, el coseno sale de $\\cos\\alpha=\\sqrt{1-\\sin^{2}\\alpha}$ (positivo, al ser el ángulo agudo)."],
  "answer":"No puede existir: $\\left(\\dfrac{1}{5}\\right)^{2}+\\left(\\dfrac{3}{5}\\right)^{2}=\\dfrac{10}{25}=0{,}4\\neq 1$. Con $\\sin\\alpha=\\dfrac{1}{5}$, el coseno debe ser $\\cos\\alpha=\\dfrac{2\\sqrt{6}}{5}\\approx 0{,}9798$.",
  "full_solution":"El seno y el coseno de un mismo ángulo no son independientes: tienen que cumplir la identidad fundamental $\\sin^{2}\\alpha+\\cos^{2}\\alpha=1$. Se comprueba con los valores propuestos: $\\left(\\dfrac{1}{5}\\right)^{2}+\\left(\\dfrac{3}{5}\\right)^{2}=\\dfrac{1}{25}+\\dfrac{9}{25}=\\dfrac{10}{25}=\\dfrac{2}{5}=0{,}4$, que no es $1$. Por tanto no existe ningún ángulo con esas dos razones a la vez. Si el dato fiable es $\\sin\\alpha=\\dfrac{1}{5}$, el coseno queda determinado salvo el signo: $\\cos^{2}\\alpha=1-\\dfrac{1}{25}=\\dfrac{24}{25}$, luego $\\cos\\alpha=\\pm\\dfrac{\\sqrt{24}}{5}=\\pm\\dfrac{2\\sqrt{6}}{5}$. Como el ángulo es agudo, el coseno es positivo: $\\cos\\alpha=\\dfrac{2\\sqrt{6}}{5}\\approx 0{,}9798$. Tiene sentido: un seno tan pequeño corresponde a un ángulo pequeño (unos $11{,}5^\\circ$), cuyo coseno debe estar muy cerca de $1$.",
  "common_errors":["Comprobar la identidad sumando las razones en lugar de sus cuadrados: $\\dfrac{1}{5}+\\dfrac{3}{5}=\\dfrac{4}{5}$ no dice nada, la identidad es con los cuadrados.",
                   "Dar $\\sqrt{\\dfrac{24}{25}}$ como $\\dfrac{24}{5}$ o como $\\dfrac{12}{5}$: la raíz del numerador es $\\sqrt{24}=2\\sqrt{6}$, no $24:2$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-05-P2","type":"REASONING","objective_ids":["LO-10-05-1","LO-10-05-2"],
  "concept_ids":["C-10-08"],"difficulty":5,
  "statement":"¿Puede existir un ángulo agudo tal que su tangente y su coseno sean iguales? Plantea la ecuación con la identidad fundamental, resuélvela y da el valor del ángulo con cuatro decimales.",
  "hints":["Escribe $\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}$ e iguala a $\\cos\\alpha$; después sustituye $\\cos^{2}\\alpha$ por $1-\\sin^{2}\\alpha$.",
           "Llegarás a una ecuación de segundo grado en $\\sin\\alpha$: descarta la raíz negativa, porque el ángulo es agudo."],
  "answer":"Sí existe: $\\sin\\alpha=\\dfrac{-1+\\sqrt{5}}{2}\\approx 0{,}6180$, de donde $\\alpha\\approx 38{,}1727^\\circ$, y entonces $\\tan\\alpha=\\cos\\alpha\\approx 0{,}7862$.",
  "full_solution":"La condición es $\\tan\\alpha=\\cos\\alpha$. Escribiendo la tangente como cociente, $\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\cos\\alpha$, y multiplicando por $\\cos\\alpha$ (que no es cero en un ángulo agudo): $\\sin\\alpha=\\cos^{2}\\alpha$. Ahora se usa la identidad fundamental para dejar todo en función del seno: $\\cos^{2}\\alpha=1-\\sin^{2}\\alpha$, de modo que $\\sin\\alpha=1-\\sin^{2}\\alpha$, es decir, $\\sin^{2}\\alpha+\\sin\\alpha-1=0$. Llamando $s=\\sin\\alpha$, se resuelve $s^{2}+s-1=0$ con la fórmula general: $s=\\dfrac{-1\\pm\\sqrt{1+4}}{2}=\\dfrac{-1\\pm\\sqrt{5}}{2}$. La raíz con el signo menos es $\\approx -1{,}618$, imposible para un seno (que vive entre $-1$ y $1$) y además negativa; la válida es $s=\\dfrac{-1+\\sqrt{5}}{2}\\approx 0{,}6180$. El ángulo es $\\alpha=\\arcsin 0{,}6180\\approx 38{,}1727^\\circ$. Comprobación: $\\cos\\left(38{,}1727^\\circ\\right)\\approx 0{,}78615$ y $\\tan\\left(38{,}1727^\\circ\\right)\\approx 0{,}78615$: en efecto coinciden. Curiosidad: el valor $\\dfrac{-1+\\sqrt{5}}{2}$ es el inverso de la razón áurea.",
  "common_errors":["Responder que no existe porque 'la tangente crece sin límite y el coseno no pasa de $1$': eso solo descarta los ángulos grandes; para ángulos pequeños la tangente es pequeña y el cruce se produce.",
                   "Quedarse con la raíz $\\dfrac{-1-\\sqrt{5}}{2}\\approx -1{,}618$: ningún seno puede valer menos que $-1$."],
  "provenance":"SOURCE_DERIVED"},

 {"id":"EX-10-05-P3","type":"STANDARD","objective_ids":["LO-10-05-1","LO-10-05-2"],
  "concept_ids":["C-10-08"],"difficulty":4,
  "statement":"De un ángulo agudo $\\alpha$ se sabe que su cotangente vale $2$. Halla $\\tan\\alpha$, $\\cos\\alpha$ y $\\sin\\alpha$ mediante identidades, sin usar la calculadora, y deja los resultados con el denominador racionalizado.",
  "hints":["La cotangente es la inversa de la tangente: $\\cot\\alpha=\\dfrac{1}{\\tan\\alpha}$.",
           "Usa $1+\\tan^{2}\\alpha=\\dfrac{1}{\\cos^{2}\\alpha}$ y después $\\sin\\alpha=\\tan\\alpha\\cdot\\cos\\alpha$."],
  "answer":"$\\tan\\alpha=\\dfrac{1}{2}$, $\\cos\\alpha=\\dfrac{2\\sqrt{5}}{5}\\approx 0{,}8944$ y $\\sin\\alpha=\\dfrac{\\sqrt{5}}{5}\\approx 0{,}4472$.",
  "full_solution":"La cotangente es la inversa de la tangente, así que de $\\cot\\alpha=2$ se obtiene $\\tan\\alpha=\\dfrac{1}{2}$. Para el coseno se usa la identidad $1+\\tan^{2}\\alpha=\\dfrac{1}{\\cos^{2}\\alpha}$: sustituyendo, $1+\\dfrac{1}{4}=\\dfrac{5}{4}=\\dfrac{1}{\\cos^{2}\\alpha}$, de donde $\\cos^{2}\\alpha=\\dfrac{4}{5}$ y, al ser el ángulo agudo (coseno positivo), $\\cos\\alpha=\\sqrt{\\dfrac{4}{5}}=\\dfrac{2}{\\sqrt{5}}=\\dfrac{2\\sqrt{5}}{5}\\approx 0{,}8944$. El seno se obtiene de la definición de la tangente: $\\sin\\alpha=\\tan\\alpha\\cdot\\cos\\alpha=\\dfrac{1}{2}\\cdot\\dfrac{2}{\\sqrt{5}}=\\dfrac{1}{\\sqrt{5}}=\\dfrac{\\sqrt{5}}{5}\\approx 0{,}4472$. Comprobación con la identidad fundamental: $\\sin^{2}\\alpha+\\cos^{2}\\alpha=\\dfrac{1}{5}+\\dfrac{4}{5}=1$, correcto. Y en efecto $\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\dfrac{1/\\sqrt{5}}{2/\\sqrt{5}}=\\dfrac{1}{2}=\\tan\\alpha$.",
  "common_errors":["Tomar $\\tan\\alpha=2$ confundiendo la cotangente con la tangente: la cotangente es su inversa, así que $\\tan\\alpha=\\dfrac{1}{2}$.",
                   "Despejar $\\cos\\alpha$ de $\\dfrac{5}{4}=\\dfrac{1}{\\cos^{2}\\alpha}$ y escribir $\\cos^{2}\\alpha=\\dfrac{5}{4}$: hay que invertir la fracción, y $\\cos^{2}\\alpha=\\dfrac{4}{5}$, menor que $1$ como corresponde."],
  "provenance":"SOURCE_DERIVED"},
],
}


def val():
    ic = math.isclose
    d, r = math.degrees, math.radians
    def dms(x):
        g = int(x); mm = (x - g)*60; m = int(mm); s = (mm - m)*60
        return g, m, round(s, 1)
    # ---------- L02 P1 rombo
    th = d(math.atan(6/4)); assert round(th, 5) == 56.30993, th
    ang = 2*th; assert round(ang, 5) == 112.61986, ang
    assert dms(ang) == (112, 37, 11.5), dms(ang)
    other = 180 - ang; assert round(other, 5) == 67.38014
    assert dms(other) == (67, 22, 48.5), dms(other)
    assert ic(ang + other, 180) and ic(2*(ang + other), 360)
    assert ic(round(0.61986*60, 2), 37.19)
    # ---------- L02 P2 triangulo exacto
    b, c = math.sqrt(3), 1.0
    a = math.hypot(b, c); assert ic(a, 2.0, rel_tol=1e-12)
    assert ic(3 + 1, 4)
    assert ic(d(math.atan(b/c)), 60.0, rel_tol=1e-12)
    assert ic(90 - 60, 30)
    assert ic(math.sin(r(30)), 0.5, abs_tol=1e-12) and ic(c/a, 0.5)
    assert ic(b*c/2, math.sqrt(3)/2) and round(math.sqrt(3)/2, 3) == 0.866
    # ---------- L02 P3 compas
    sn = 3.125/11.5; assert round(sn, 6) == 0.271739, sn
    th3 = d(math.asin(sn)); assert round(th3, 5) == 15.76778, th3
    ang3 = 2*th3; assert round(ang3, 5) == 31.53556, ang3
    assert dms(ang3)[:2] == (31, 32), dms(ang3)
    assert ic(2*11.5*math.sin(r(th3)), 6.25, rel_tol=1e-9)
    assert round(0.53556*60, 1) == 32.1
    # ---------- L03 P1 pendiente
    al = d(math.atan(0.06)); assert round(al, 4) == 3.4336, al
    asc = 1000*math.sin(r(al)); assert round(asc, 2) == 59.89, asc
    assert round(asc, 1) == 59.9
    assert ic(1000*0.06, 60)
    assert round(60 - asc, 2) == 0.11
    al30 = math.atan(0.30); assert round(1000*math.sin(al30), 1) == 287.3
    assert round(math.sin(r(al)), 6) == 0.059892
    # ---------- L03 P2 pentagono
    lado = 2*10*math.sin(r(36)); assert round(lado, 4) == 11.7557, lado
    assert round(10*math.sin(r(36)), 4) == 5.8779
    ap = 10*math.cos(r(36)); assert round(ap, 4) == 8.0902, ap
    per = 5*lado; assert round(per, 4) == 58.7785, per
    S = per*ap/2; assert round(S, 4) == 237.7641, S
    S2 = 5*0.5*100*math.sin(r(72)); assert ic(S, S2, rel_tol=1e-12)
    assert round(S2, 4) == 237.7641
    assert 360//5 == 72 and 72//2 == 36
    # ---------- L03 P3 decagono
    assert 360//10 == 36 and 36//2 == 18
    t18 = math.tan(r(18)); assert round(t18, 6) == 0.32492, t18
    ap10 = 10/t18; assert round(ap10, 4) == 30.7768, ap10
    S10 = 200*ap10/2; assert round(S10, 4) == 3077.6835, S10
    rc = math.sqrt(S10/math.pi); assert round(rc, 1) == 31.3, rc
    assert ap10 > 20
    # ---------- L03 P4 hexagono
    assert 360//6 == 60
    ap6 = 9*math.cos(r(30)); assert round(ap6, 4) == 7.7942, ap6
    assert ic(ap6, 9*math.sqrt(3)/2, rel_tol=1e-12)
    S6 = 54*ap6/2; assert round(S6, 4) == 210.4442, S6
    S6b = 6*math.sqrt(3)/4*81; assert ic(S6, S6b, rel_tol=1e-12)
    assert ic(S6b, 3*math.sqrt(3)/2*81, rel_tol=1e-12)
    assert ic(54*9/2, 243)
    # ---------- L05 P1
    assert F(1, 5)**2 + F(3, 5)**2 == F(10, 25) == F(2, 5)
    assert ic(float(F(2, 5)), 0.4) and F(2, 5) != 1
    assert 1 - F(1, 25) == F(24, 25)
    assert ic(math.sqrt(24)/5, 2*math.sqrt(6)/5, rel_tol=1e-12)
    assert round(2*math.sqrt(6)/5, 4) == 0.9798
    assert round(d(math.asin(0.2)), 1) == 11.5
    assert F(1, 5) + F(3, 5) == F(4, 5)
    # ---------- L05 P2
    s = (-1 + math.sqrt(5))/2
    assert round(s, 4) == 0.618
    assert ic(s*s + s - 1, 0, abs_tol=1e-15)
    a2 = d(math.asin(s)); assert round(a2, 4) == 38.1727, a2
    assert ic(math.cos(r(a2)), math.tan(r(a2)), rel_tol=1e-12)
    assert round(math.cos(r(a2)), 5) == 0.78615
    assert round(math.tan(r(a2)), 5) == 0.78615
    assert round(math.cos(r(a2)), 4) == 0.7862
    s_bad = (-1 - math.sqrt(5))/2
    assert round(s_bad, 3) == -1.618 and s_bad < -1
    assert ic(1 + 4, 5)
    # ---------- L05 P3
    tg = F(1, 2)
    assert 1 + tg**2 == F(5, 4)
    cos2 = F(4, 5); assert cos2 == 1/F(5, 4)
    cosa = 2/math.sqrt(5); assert ic(cosa, 2*math.sqrt(5)/5, rel_tol=1e-12)
    assert round(cosa, 4) == 0.8944
    sina = 0.5*cosa; assert ic(sina, 1/math.sqrt(5), rel_tol=1e-12)
    assert ic(sina, math.sqrt(5)/5, rel_tol=1e-12) and round(sina, 4) == 0.4472
    assert ic(sina**2 + cosa**2, 1.0, rel_tol=1e-12)
    assert F(1, 5) + F(4, 5) == 1
    assert ic(sina/cosa, 0.5, rel_tol=1e-12)
    print("val() OK  ->", sum(len(v) for v in EX.values()), "ejercicios")
