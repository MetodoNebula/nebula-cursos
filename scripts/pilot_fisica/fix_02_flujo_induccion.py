# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["12_El_flujo_magnético_y_qué_induce_corriente.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}\n!=\n{old!r}"
    container[key] = new

# 1. keywords[4].definition
set_exact(l["keywords"][4], "definition",
    "Movimiento de un cuerpo respecto de otro. En la inducción es lo único que cuenta: da igual que se mueva el imán o la espira.",
    "Movimiento de un cuerpo respecto de otro. Para el caso concreto de un imán y una espira (sin que nada más cambie), es lo que determina la fem inducida: da igual que se mueva el imán o la espira. No es necesario para inducir corriente en general: un circuito en reposo cuyo campo varía con el tiempo (como en un transformador) también induce corriente sin que nada se desplace; lo único imprescindible siempre es que el flujo $\\Phi_B$ varíe.")

# 2. objectives[5].statement
set_exact(l["objectives"][5], "statement",
    "Reconocer, en la observación de que solo cuenta el movimiento relativo, una afirmación sobre qué observadores ven la misma física.",
    "Reconocer que, en el caso particular del imán y la espira, la observación de que solo cuenta el movimiento relativo es una afirmación sobre qué observadores ven la misma física (fem de movimiento) — sin que esto generalice a toda la inducción: un circuito en reposo con un campo que varía en el tiempo también induce corriente sin que nada se mueva.")

# 3. theory_blocks[7].body: prepend scoping paragraph
old_tb7 = l["theory_blocks"][7]["body"]
assert old_tb7.startswith("Vuelve a la primera observación de Faraday")
scope_prefix = (
    "Esta observación de Faraday —que solo importa el movimiento relativo— es válida en el caso "
    "concreto del imán y la espira, cuando lo que cambia es su posición relativa. **No es la ley "
    "general de la inducción**: esa es $\\mathrm d\\Phi_B/\\mathrm dt\\neq0$. Un circuito completamente "
    "en reposo, atravesado por un campo que varía en el tiempo (como en el ejercicio de la bobina con "
    "$B(t)$ decreciente de esta misma lección, o en un transformador), induce corriente sin que nada se "
    "mueva. Dicho esto, dentro del caso imán-espira la observación es exacta y merece la pena analizarla "
    "porque conecta con la relatividad especial:\n\n"
)
l["theory_blocks"][7]["body"] = scope_prefix + old_tb7

# 4. mcq[2].explanation
set_exact(l["mcq"][2], "explanation",
    "La observación original de Faraday es inequívoca: la corriente aparece solo mientras hay movimiento relativo y cesa en cuanto este cesa. Con el imán quieto el flujo no varía, y sin variación de flujo no hay corriente inducida por intenso que sea el campo.",
    "La ley general de la inducción es: se induce corriente si y solo si el flujo varía ($\\mathrm d\\Phi_B/\\mathrm dt\\neq0$). En este montaje, con el imán inmóvil dentro de la espira, el flujo es grande pero constante en el tiempo, así que no varía y no hay corriente inducida, por intenso que sea el campo. (En el caso particular de un imán y una espira sin más, la única forma de que el flujo varíe es el movimiento relativo entre ambos; pero esto no es universal: un circuito que no se mueve y cuyo campo cambia con el tiempo —como un transformador— también induce corriente sin que nada se desplace.)")

# 5. summary.key_points[0]
set_exact(l["summary"], "key_points", l["summary"]["key_points"], l["summary"]["key_points"])  # no-op sanity
kp = l["summary"]["key_points"]
old_kp0 = "La corriente inducida aparece **solo mientras hay movimiento relativo** y cesa cuando este cesa; su intensidad depende de **lo rápido** que sea."
assert kp[0] == old_kp0
kp[0] = ("Lo que induce corriente es que el flujo **varíe** ($\\mathrm d\\Phi_B/\\mathrm dt\\neq0$); su intensidad "
         "depende de **lo rápido** que varíe. En el caso particular de un imán y una espira, el flujo solo varía "
         "si hay movimiento relativo entre ellos — pero un circuito en reposo con un campo que cambia en el "
         "tiempo (un transformador) también induce corriente sin que nada se mueva.")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P0 electromagnetismo/12 (flujo/induccion) corregido y propagado.")
