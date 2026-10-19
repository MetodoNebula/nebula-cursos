import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

old = '"(a) El -COOH aporta un H donador y dos oxígenos aceptores, más puntos de anclaje que el único -OH de un alcohol. (b) Aunque la disociación es parcial, los iones H3O+ y CH3COO- que sí se forman transportan la corriente."'
new = '"(a) El -COOH aporta un H donador y dos oxígenos aceptores, más puntos de anclaje que el único -OH de un alcohol. (b) El 1-butanol tiene un único -OH (un donador y un aceptor) y una cadena apolar de 4 C que ya pesa frente al grupo polar; el ácido etanoico tiene un -COOH (un donador y dos oxígenos aceptores) y solo un CH3 apolar: por eso el ácido es miscible y el butanol solo parcialmente soluble (unos 7,7 g/100 g de agua)."'
rep(old, new, 1, "F1 answer")

old_a = "Un alcohol como el propan-1-ol solo dispone de un oxígeno con un par de electrones libres y un H donador. Con más puntos de anclaje para el enlace de hidrógeno con el agua, el ácido se solvata mejor y resulta, de hecho, incluso más soluble que un alcohol de masa parecida."
new_a = "El 1-butanol del enunciado solo dispone de un oxígeno (un H donador y un par de electrones libres aceptor): un único punto doble de anclaje frente a los tres del -COOH (un donador y dos aceptores). Con más puntos de anclaje para el enlace de hidrógeno con el agua, el ácido etanoico se solvata por completo y es miscible en cualquier proporción."
rep(old_a, new_a, 1, "F2a full_solution(a)")

old_b = "(b) Ser un ácido débil significa que el equilibrio CH3COOH + H2O ⇌ CH3COO- + H3O+ está desplazado mayoritariamente hacia la izquierda, pero no completamente: una fracción, aunque pequeña, de moléculas sí se disocia. Los iones H3O+ y CH3COO- resultantes, al estar libres en disolución, pueden moverse bajo un campo eléctrico y transportar carga, lo que hace que la disolución conduzca la corriente, aunque mucho menos que la de un ácido fuerte a la misma concentración, donde la disociación es prácticamente total."
new_b = "(b) El 1-butanol, CH3-CH2-CH2-CH2-OH, tiene un único grupo -OH (un H donador y un O aceptor) sosteniendo una cadena apolar de 4 carbonos; esa cadena apolar rompe la red de enlaces de hidrógeno del agua sin aportar ningún anclaje que lo compense, por lo que domina sobre el único -OH polar. El ácido etanoico, CH3-COOH, tiene en cambio un -COOH con tres puntos de anclaje (un donador y dos aceptores) y solo un grupo -CH3 apolar: la parte polar domina con claridad, de ahí la miscibilidad total frente a la solubilidad limitada del butanol (unos 7,7 g/100 g de agua). A partir de cadenas de 4-5 carbonos, como ya se vio en la serie de los alcoholes, la parte apolar empieza a predominar sobre un único grupo -OH o -COOH, reduciendo la solubilidad en agua."
rep(old_b, new_b, 1, "F2b full_solution(b)")

old_ms = '''"mark_scheme": [
          "1 punto por identificar los dos oxígenos del -COOH como punto extra de anclaje frente al -OH del alcohol",
          "1 punto por relacionar conductividad con presencia de iones libres, no con la cantidad total de ácido",
          "1 punto por mencionar explícitamente que la disociación es parcial, propia de un ácido débil"
        ],'''
new_ms = '''"mark_scheme": [
          "1 punto por identificar los dos oxígenos aceptores y el H donador del -COOH como puntos de anclaje extra frente al -OH del alcohol (a)",
          "1 punto por indicar que el 1-butanol solo tiene un -OH, con un único donador y un único aceptor (b)",
          "1 punto por relacionar la cadena apolar de 4 carbonos del butanol con su menor solubilidad frente a la miscibilidad total del ácido (b)"
        ],'''
rep(old_ms, new_ms, 1, "F3 mark_scheme")

old_ce = '"En (b), afirmar que un ácido débil \'no conduce la corriente\', confundiendo disociación parcial con ausencia total de iones."'
new_ce = '"En (b), pensar que, al tener los dos un solo grupo -OH o -COOH, alcohol y ácido deberían disolverse igual, sin contar la diferencia en el número de puntos de anclaje ni el peso añadido por la cadena apolar del butanol."'
rep(old_ce, new_ce, 1, "F3b common_errors")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE A")
