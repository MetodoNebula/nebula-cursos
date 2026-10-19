# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__relatividad.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["05_La_energía_en_reposo_E_0mc2.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

set_exact(l["keywords"][6], "definition",
    "Energía mínima necesaria para que un proceso pueda ocurrir. En la creación de un par vale $2mc^{2}$: por debajo, el proceso es imposible.",
    "Energía mínima necesaria para que un proceso pueda ocurrir. En la creación de un par vale aproximadamente $2mc^{2}$ (umbral ideal, despreciando la pequeña energía cinética que se lleva el núcleo de retroceso): por debajo de ese valor, el proceso es imposible.")

set_exact(l["flashcards"][8], "back",
    "$E_{\\text{umbral}}=2m c^{2}$ (dos partículas, no una). Para el par electrón-positrón, $1{,}64\\cdot10^{-13}$ J $=1{,}02$ MeV. Por debajo, el proceso **no ocurre**.",
    "$E_{\\text{umbral}}\\approx 2m c^{2}$ (dos partículas, no una; valor ideal que desprecia la pequeña energía cinética de retroceso del núcleo). Para el par electrón-positrón, $\\approx1{,}64\\cdot10^{-13}$ J $=1{,}02$ MeV. Por debajo, el proceso **no ocurre**.")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P2 relatividad/05 (umbral produccion de pares, etiquetado en keywords/flashcards; theory_blocks ya era correcto).")
