# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__cuantica.json")
d = json.load(open(fp, encoding="utf-8"))
l5 = d["05_Dualidad_onda-corpúsculo_Compton_y_de_Broglie.json"]
l6 = d["06_Indeterminación_y_la_nueva_mecánica_cuántica.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

# objectives[3]: lead with h/p, mark h/mv as non-relativistic substitution
set_exact(l5["objectives"][3], "statement",
    "Aplicar la hipótesis de de Broglie $\\lambda = h/mv$ en problemas directos e inversos, incluidos los de electrones acelerados por una diferencia de potencial.",
    "Aplicar la hipótesis de de Broglie $\\lambda = h/p$ (con $p=mv$ como aproximación no relativista, válida para $v\\ll c$) en problemas directos e inversos, incluidos los de electrones acelerados por una diferencia de potencial.")

# keywords[2]: lead with h/p
set_exact(l5["keywords"][2], "definition",
    "Onda asociada a toda partícula en movimiento, de longitud $\\lambda = h/mv$. No es una trayectoria: describe dónde es probable encontrar a la partícula.",
    "Onda asociada a toda partícula en movimiento, de longitud $\\lambda = h/p$ (fórmula canónica; $p=mv$ solo como aproximación no relativista, $v\\ll c$). No es una trayectoria: describe dónde es probable encontrar a la partícula.")

# theory_blocks[3]: extend the existing clarifying note with the non-relativistic caveat
old_note = ("> **Dos nombres para la misma magnitud.** En $\\lambda = h/mv$, el producto $mv$ es el momento lineal. "
            "Conviene escribir la fórmula como $\\lambda = h/p$ y recordar que, según el objeto, ese $p$ se calcula "
            "de una manera o de otra: $mv$ si tiene masa, $E/c$ si es un fotón.")
assert old_note in l5["theory_blocks"][3]["body"]
new_note = old_note + ("\n>\n> **La fórmula canónica es $\\lambda=h/p$.** $p=mv$ es la expresión del momento lineal "
    "**no relativista** ($v\\ll c$), que es la que sirve en todos los problemas de este curso. Si alguna vez una "
    "partícula se acercase a la velocidad de la luz, habría que usar el momento relativista; eso queda fuera de "
    "este curso, pero conviene saber que $p=mv$ no es la definición de $p$, es un caso particular de ella.")
l5["theory_blocks"][3]["body"] = l5["theory_blocks"][3]["body"].replace(old_note, new_note)

# theory_blocks[9]: first sentence mentions "la masa que va en lambda=h/mv"; add scope reminder at end
old_tb9_start = "**La masa que va en $\\lambda = h/mv$ es la de la partícula del problema.**"
assert l5["theory_blocks"][9]["body"].startswith(old_tb9_start)
l5["theory_blocks"][9]["body"] += ("\n\n**Recordatorio de alcance:** $\\lambda=h/mv$ es $\\lambda=h/p$ con $p=mv$ "
    "no relativista. Para los electrones, protones y neutrones de este curso, acelerados por diferencias de "
    "potencial de laboratorio, $v\\ll c$ y la aproximación es excelente.")

# summary.key_points[2]: already writes lambda=h/p=h/mv together; add the non-relativistic note
kp = l5["summary"]["key_points"]
old_kp2 = ("**La hipótesis de de Broglie:** toda partícula en movimiento lleva asociada una onda de longitud "
           "$\\lambda = h/p = h/mv$. Para la energía cinética, $\\lambda = h/\\sqrt{2mE_c}$; para un electrón acelerado, "
           "$\\lambda(\\mathrm{nm}) \\approx 1{,}23/\\sqrt{V}$.")
assert kp[2] == old_kp2
kp[2] = old_kp2.replace(
    "de longitud $\\lambda = h/p = h/mv$.",
    "de longitud $\\lambda = h/p$ (fórmula canónica), con $p=mv$ como aproximación no relativista $v\\ll c$.")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P2 cuantica/de_Broglie corregido (canonica h/p, mv marcado como aproximacion).")
