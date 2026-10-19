# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["06_El_campo_magnético_un_campo_sin_fuentes.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

# 1) objectives[3]: scope to "para una carga puntual en movimiento"
set_exact(l["objectives"][3], "statement",
    "Enumerar las cuatro ausencias que se siguen de no haber monopolos: no hay ley de Coulomb magnética, ni energía potencial magnética, ni potencial magnético, ni fuerza conservativa.",
    "Enumerar las cuatro ausencias que se siguen de no haber monopolos, para una carga puntual en movimiento: no hay ley de Coulomb magnética, ni energía potencial magnética, ni potencial escalar análogo al eléctrico, ni fuerza conservativa en ese sentido (nota Advanced: sí existe un potencial vector A, y una energía U=-mu·B para un dipolo magnético en un campo externo).")

# 2) theory_blocks[5].body: tighten point 3 wording to make the point-charge scope explicit (already decent, add one clause)
old3 = ("3. **No hay potencial magnético**: ningún escalar $V_m$ que se pueda calcular en un punto y después sumar "
        "como se suman los potenciales eléctricos. Tampoco hay, por tanto, superficies equipotenciales magnéticas.")
new3 = ("3. **No hay potencial magnético escalar de posición, para una carga puntual en movimiento**: ningún escalar "
        "$V_m(\\vec r)$ que se pueda calcular en un punto y después sumar como se suman los potenciales eléctricos. "
        "Tampoco hay, por tanto, superficies equipotenciales magnéticas para esa carga. (Esto no quiere decir que no "
        "exista ningún objeto matemático asociado a $\\vec B$: en el nivel Advanced se introduce el potencial vector "
        "$\\vec A$, y un dipolo magnético —no una carga puntual— sí tiene una energía potencial bien definida.)")
assert old3 in l["theory_blocks"][5]["body"]
l["theory_blocks"][5]["body"] = l["theory_blocks"][5]["body"].replace(old3, new3)

# 3) Add new ADVANCED theory_block with the vector potential / dipole note
new_block = {
    "id": "TH-06-9",
    "type": "advanced",
    "title": "Nota avanzada: el potencial vector A y la energía de un dipolo magnético",
    "scope": "ADVANCED",
    "body": (
        "Las cuatro ausencias de más arriba se referían siempre a **una carga puntual en movimiento**: para "
        "esa carga no hay ningún escalar de posición del que $\\vec B$ se derive por gradiente, igual que $\\vec E=-\\vec\\nabla V$. "
        "Eso es exacto y es lo que hay que saber para Selectividad. Pero conviene no llevarlo más allá de donde vale, "
        "porque hay dos construcciones reales que a veces se confunden con \"el potencial magnético que no existía\":\n\n"
        "- **El potencial vector $\\vec A$.** Se puede escribir $\\vec B=\\vec\\nabla\\times\\vec A$ (en vez de "
        "$\\vec E=-\\vec\\nabla V$). $\\vec A$ es un campo vectorial, no un escalar, y no da la energía de una carga "
        "sumando números: sigue haciendo falta álgebra vectorial. No es un contraejemplo a las cuatro ausencias; es "
        "la herramienta matemática avanzada con la que de verdad se trabaja $\\vec B$ en electrodinámica, fuera del "
        "alcance de este curso.\n"
        "- **La energía de un dipolo magnético.** Un dipolo (una espira con corriente, un imán pequeño), caracterizado "
        "por su momento magnético $\\vec\\mu$, sí tiene una energía potencial bien definida en un campo externo uniforme: "
        "$$U=-\\vec\\mu\\cdot\\vec B$$ Esto **no contradice** las cuatro ausencias: $\\vec\\mu$ no es una carga magnética "
        "aislada, sino la propiedad de un sistema extendido (una espira, un imán), y $U$ aquí describe la energía de "
        "**orientación** del dipolo (como un $U=-\\vec p\\cdot\\vec E$ para un dipolo eléctrico), no la energía de una "
        "carga puntual que se desplaza en el campo.\n\n"
        "Conclusión para examen: si preguntan por una carga puntual, las cuatro ausencias son la respuesta correcta "
        "y completa. Si aparece un dipolo o una espira en un campo externo, $U=-\\vec\\mu\\cdot\\vec B$ es la magnitud "
        "relevante, y no es una excepción a la regla anterior sino una magnitud distinta."
    ),
    "concept_ids": ["C-EM-19"],
    "objective_ids": ["LO-06-4"],
    "provenance": "GENERATED_EXPLANATION",
}
l["theory_blocks"].append(new_block)

# 4) misconceptions[0].correct_model: add pointer to the advanced note
old_cm = l["misconceptions"][0]["correct_model"]
assert old_cm.endswith("El campo magnético se maneja siempre con vectores, nunca con un escalar que se sume.")
l["misconceptions"][0]["correct_model"] = old_cm + (
    " Esto se refiere a una carga puntual; un dipolo magnético (una espira, un imán) sí tiene una energía de "
    "orientación $U=-\\vec\\mu\\cdot\\vec B$ en un campo externo (nota Advanced), que no es un potencial escalar de "
    "posición y no contradice lo anterior."
)

# 5) exam_notes[4]: soften absolute phrasing
old_en4 = l["exam_notes"][4]
assert old_en4 == "Si en un enunciado aparece la expresión «carga magnética» o «potencial magnético», o bien el enunciado está mal, o bien es una pregunta trampa que espera que se señale que no existen."
l["exam_notes"][4] = ("Si en un enunciado de Selectividad aparece la expresión «carga magnética» o «potencial magnético "
    "de una carga puntual», o bien el enunciado está mal, o bien es una pregunta trampa que espera que se señale que "
    "no existen. (Si en cambio aparece la energía de un dipolo/espira en un campo externo, $U=-\\vec\\mu\\cdot\\vec B$ "
    "es una magnitud distinta y perfectamente real; ver nota Advanced.)")

# 6) summary fields
old_big = l["summary"]["big_idea"]
assert old_big.startswith("No existe la carga magnética")
l["summary"]["big_idea"] = old_big + (" (Nivel Advanced: una carga puntual no tiene potencial escalar, pero un dipolo "
    "magnético sí tiene una energía de orientación bien definida, U=-mu·B, en un campo externo.)")

kp = l["summary"]["key_points"]
old_kp3 = "**Las cuatro ausencias**: no hay ley de Coulomb magnética, ni energía potencial magnética, ni potencial magnético, ni fuerza conservativa. Dos causas: las dos primeras, por no existir la carga magnética; las otras dos, porque la fuerza magnética depende de la velocidad."
assert kp[3] == old_kp3
kp[3] = old_kp3 + " (Todo esto para una carga puntual; un dipolo sí tiene energía de orientación U=-mu·B — nota Advanced.)"

old_wtr = l["summary"]["what_to_remember_if_nothing_else"]
assert old_wtr == "No hay carga magnética (por eso las líneas de $\\vec B$ son cerradas) y la fuerza magnética depende de la velocidad (por eso no hay potencial magnético ni fuerza conservativa): a partir de aquí ya no estás haciendo gravitación con otras letras."
l["summary"]["what_to_remember_if_nothing_else"] = old_wtr.replace(
    "no hay potencial magnético ni fuerza conservativa", "no hay potencial escalar ni fuerza conservativa para una carga puntual")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P1 electromagnetismo/06 (potencial magnetico) corregido + nota Advanced anadida.")
