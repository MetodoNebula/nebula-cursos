# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__electromagnetismo.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["10_El_campo_magnético_creado_por_corrientes.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

# objectives[4]
set_exact(l["objectives"][4], "statement",
    "Calcular el campo en el interior de un solenoide, justificando que es **uniforme en todo el interior** y que solo en los extremos cae a la mitad.",
    "Calcular el campo en el interior de un solenoide largo, justificando que es **aproximadamente uniforme en todo el interior lejos de los extremos** (modelo de solenoide largo e ideal) y que en los propios extremos cae a la mitad.")

# theory_blocks[5]: title stays; body: add condition after the boxed formula sentence; caption: scope it
tb5 = l["theory_blocks"][5]
old_caption = ("Corte longitudinal de un solenoide. Dentro, las líneas son paralelas y **equidistantes**: el campo es "
               "uniforme en todo el interior, incluido el centro. En los extremos se abren y su densidad se reduce a la mitad, "
               "que es lo único que allí cambia.")
assert tb5["assets"][0]["caption"] == old_caption
tb5["assets"][0]["caption"] = ("Corte longitudinal de un solenoide largo. Dentro, lejos de los extremos, las líneas son "
    "casi paralelas y equidistantes: el campo es aproximadamente uniforme en todo el interior, incluido el centro (modelo "
    "de solenoide largo, L≫R). En los extremos se abren y su densidad se reduce a la mitad, que es lo que allí cambia de forma apreciable.")

old_b5_marker = "donde $n$ es el **número de espiras por unida"
assert old_b5_marker in tb5["body"]
# add a scope sentence right before the error-note that typically follows; safest: append at end of body
tb5["body"] = tb5["body"] + ("\n\nEsta fórmula es un **modelo** (aproximación) válido para un solenoide **largo** "
    "($L\\gg R$) y lejos de sus extremos: es entonces cuando el campo es prácticamente uniforme en el interior. "
    "En un solenoide corto o grueso, o cerca de los extremos, el campo real varía con la posición y hay que usar "
    "la expresión completa de la espira/bobina finita.")

# theory_blocks[6]
tb6 = l["theory_blocks"][6]
old_b6 = ("Error frecuente que conviene anticipar: aplicar el factor $\\tfrac12$ al **centro** del solenoide. El centro "
          "pertenece al **interior**, y en todo el interior de un solenoide largo el campo vale $B=\\mu nI$ y es uniforme; "
          "$\\tfrac12$ corresponde únicamente a los **extremos**, por la razón geométrica del")
assert tb6["body"].startswith(old_b6)
tb6["body"] = tb6["body"].replace(
    "y en todo el interior de un solenoide largo el campo vale $B=\\mu nI$ y es uniforme;",
    "y en todo el interior de un solenoide largo (lejos de los extremos) el campo vale aproximadamente $B=\\mu nI$ y es "
    "prácticamente uniforme;")
old_cap6 = ("Campo en el eje de un solenoide finito, calculado con la expresión exacta. La meseta llega hasta el borde y "
            "vale $0{,}999\\,\\mu nI$ en el centro; solo en el extremo el campo cae a $0{,}500\\,\\mu nI$, la mitad. Fuera, se desploma.")
assert tb6["assets"][0]["caption"] == old_cap6
tb6["assets"][0]["caption"] = old_cap6 + (" Nótese que incluso en el centro el valor exacto ($0{,}999\\,\\mu nI$) es solo "
    "muy próximo a $\\mu nI$, no idéntico: $B=\\mu nI$ es el límite de solenoide infinitamente largo, una aproximación "
    "excelente para $L\\gg R$, no un valor exacto en un solenoide real.")

# flashcards[5].back
old_fc5 = "$$B=\\frac{\\mu NI}{L}=\\mu\\,n\\,I\\qquad n=\\frac{N}{L}$$ **Uniforme en todo el interior**: no aparece ni la posición ni el radio del solenoide. Fuera, prácticamente nulo."
assert l["flashcards"][5]["back"] == old_fc5
l["flashcards"][5]["back"] = ("$$B=\\frac{\\mu NI}{L}=\\mu\\,n\\,I\\qquad n=\\frac{N}{L}$$ Modelo de solenoide **largo**: "
    "**aproximadamente uniforme en todo el interior**, lejos de los extremos; no aparece ni la posición ni el radio. Fuera, prácticamente nulo.")

# misconceptions[0].correct_model
old_mc = l["misconceptions"][0]["correct_model"]
assert old_mc.startswith("En **todo** el interior de un solenoide largo el campo vale $B=\\mu nI=\\dfrac{\\mu NI}{L}$ y es uniforme.")
l["misconceptions"][0]["correct_model"] = old_mc.replace(
    "En **todo** el interior de un solenoide largo el campo vale $B=\\mu nI=\\dfrac{\\mu NI}{L}$ y es uniforme.",
    "En **todo** el interior de un solenoide largo (lejos de los extremos) el campo vale aproximadamente $B=\\mu nI=\\dfrac{\\mu NI}{L}$ y es prácticamente uniforme (modelo de solenoide largo e ideal).")

# exam_questions[0].full_solution part (b)
eq_fs = l["exam_questions"][0]["full_solution"]
marker = "**(b) Falsa.** En **todo** el interior de un solenoide largo el"
assert marker in eq_fs
l["exam_questions"][0]["full_solution"] = eq_fs.replace(
    "**(b) Falsa.** En **todo** el interior de un solenoide largo el",
    "**(b) Falsa.** En **todo** el interior de un solenoide largo (lejos de los extremos) el")

# summary
old_kp4 = "**Solenoide**: $B=\\mu nI$, **uniforme en todo el interior** y casi nulo fuera. El factor $\\tfrac12$ corresponde **solo a los extremos**, donde se ve media bobina."
assert l["summary"]["key_points"][4] == old_kp4
l["summary"]["key_points"][4] = ("**Solenoide largo (modelo)**: $B=\\mu nI$, **aproximadamente uniforme en todo el "
    "interior** lejos de los extremos, y casi nulo fuera. El factor $\\tfrac12$ corresponde **solo a los extremos**, "
    "donde se ve media bobina.")

old_wtr = l["summary"]["what_to_remember_if_nothing_else"]
assert old_wtr == "Una corriente crea campo; el de un hilo cae como $1/r$ y gira a su alrededor; y el de un solenoide es uniforme en **todo** el interior, con la mitad solo en los extremos."
l["summary"]["what_to_remember_if_nothing_else"] = ("Una corriente crea campo; el de un hilo cae como $1/r$ y gira a su "
    "alrededor; y el de un solenoide largo es aproximadamente uniforme en **todo** el interior lejos de los extremos, "
    "con la mitad solo en los propios extremos.")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P2 electromagnetismo/solenoide corregido (modelo/aproximacion con condiciones).")
