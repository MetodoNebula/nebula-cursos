# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__campo_gravitatorio.json")
d = json.load(open(fp, encoding="utf-8"))

l05 = d["05_Fuerzas_conservativas_y_energía_potencial_gravitatoria.json"]
l07 = d["07_Conservación_de_la_energía_mecánica_en_el_campo.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

# lesson 05: keywords[7]
old_kw = "Fuerza no conservativa que se opone siempre al desplazamiento, como el rozamiento; su trabajo es negativo en ambos sentidos y no admite energía potencial asociada."
assert l05["keywords"][7]["definition"] == old_kw
l05["keywords"][7]["definition"] = old_kw.replace(
    "que se opone siempre al desplazamiento, como el rozamiento",
    "que se opone al desplazamiento cuando desliza sobre una superficie fija, como el rozamiento cinético en el modelo habitual de este curso (si la superficie también se mueve, como en una cinta transportadora, el rozamiento estático puede llegar a realizar trabajo positivo)")

# lesson 07: objectives[2]
set_exact(l07["objectives"][2], "statement",
    "Aplicar $\\Delta E_m=W_{nc}$ cuando hay fuerzas disipativas y justificar que el trabajo del rozamiento es **siempre negativo**, de modo que $E_m$ solo puede disminuir.",
    "Aplicar $\\Delta E_m=W_{nc}$ cuando hay fuerzas disipativas y justificar que, para un cuerpo que desliza sobre una superficie fija (el modelo habitual de este curso), el trabajo del rozamiento es **siempre negativo**, de modo que $E_m$ solo puede disminuir.")

# lesson 07: summary.key_points[3]
kp = l07["summary"]["key_points"]
old_kp3 = "**$W_{nc}$ del rozamiento es siempre negativo** ($\\cos 180^\\circ=-1$), luego $E_m$ **solo puede disminuir**. Un $\\Delta E_m>0$ con rozamiento es un error de signo, no un descubrimiento."
assert kp[3] == old_kp3
kp[3] = old_kp3.replace(
    "**$W_{nc}$ del rozamiento es siempre negativo**",
    "**Sobre una superficie fija (el modelo de este curso), $W_{nc}$ del rozamiento es siempre negativo**")

# lesson 07: flashcards[3]
fc = l07["flashcards"][3]
old_fc_back = "Porque se opone al desplazamiento: el ángulo es $180^\\circ$ y $W_{nc}=-F_R\\Delta r<0$. Luego **con rozamiento $E_m$ solo puede disminuir**; si sale $\\Delta E_m>0$, hay un error de signo."
assert fc["back"] == old_fc_back
fc["back"] = old_fc_back + (" (Esto supone que la superficie está fija; si ella también se mueve —una cinta "
    "transportadora— el rozamiento estático puede llegar a hacer trabajo positivo, pero eso no ocurre en los "
    "problemas de esta unidad.)")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P1 campo_gravitatorio/rozamiento -- headline summary/flashcard/objective ahora condicionados (el contraejemplo cinta transportadora ya estaba en theory_blocks[4]).")
