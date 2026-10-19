# -*- coding: utf-8 -*-
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web/pilot/selectividad_fisica_v2")
fp = os.path.join(BASE, "selectividad_fisica__cuantica.json")
d = json.load(open(fp, encoding="utf-8"))
l = d["06_Indeterminación_y_la_nueva_mecánica_cuántica.json"]

def set_exact(container, key, old, new):
    cur = container[key]
    assert cur == old, f"MISMATCH at {key}:\n{cur!r}"
    container[key] = new

# 1) objectives[1]
set_exact(l["objectives"][1], "statement",
    "Decidir, mediante el criterio dimensional (que el producto tenga dimensiones de J$\\cdot$s), si un par de magnitudes está sujeto al principio.",
    "Usar el criterio dimensional (que el producto tenga dimensiones de J$\\cdot$s) como filtro **necesario pero no suficiente** para descartar pares no conjugados, y reconocer los pares realmente conjugados de este curso (posición-momento en la misma dirección, energía-tiempo, ángulo-momento angular) sin generalizar a cualquier par que pase el filtro dimensional.")

# 2) worked_examples[2]
we = l["worked_examples"][2]
set_exact(we, "statement",
    "Sin memorizar ninguna lista, decide cuáles de estos pares de magnitudes están sujetos al principio de indeterminación: **(a)** fuerza y tiempo; **(b)** momento angular y ángulo; **(c)** energía y posición. Usa el criterio dimensional.",
    "Decide cuáles de estos pares de magnitudes están sujetos al principio de indeterminación: **(a)** fuerza y tiempo; **(b)** momento angular y ángulo; **(c)** energía y posición. Usa el criterio dimensional como filtro para descartar, y comprueba además si el par superviviente es uno de los pares conjugados estudiados en el curso.")
set_exact(we, "knowns", we["knowns"],
    ["El criterio dimensional (filtro necesario, no suficiente): si el producto NO tiene dimensiones de J$\\cdot$s, el par seguro que no está sujeto al principio",
     "Los pares conjugados estudiados en el curso: posición-momento (misma dirección), energía-tiempo, ángulo-momento angular"])
rs = we["reasoning"]
old_r0 = "El criterio es puramente dimensional, de modo que el procedimiento es siempre el mismo: escribir las dimensiones de cada magnitud, multiplicarlas y comparar con J$\\cdot$s."
assert rs[0] == old_r0
rs[0] = ("El criterio dimensional sirve para **descartar**: si el producto no tiene dimensiones de J$\\cdot$s, el par no "
         "está sujeto al principio, sin excepción. Pero que sí las tenga NO basta para afirmar que están sujetos: hace falta "
         "además que sean uno de los pares conjugados realmente estudiados.")
old_rb = ("**(b)** El momento angular tiene las mismas dimensiones que $mvr$: $\\mathrm{kg\\,m\\,s^{-1}\\cdot m} = "
          "\\mathrm{kg\\,m^2\\,s^{-1}} = \\mathrm{J\\cdot s}$. Y el ángulo es adimensional, de modo que el producto sigue "
          "teniendo dimensiones de J$\\cdot$s. **Sí cumple el criterio.**")
assert old_rb in rs
idx = rs.index(old_rb)
rs[idx] = old_rb.replace("**Sí cumple el criterio.**",
    "**Pasa el filtro dimensional** — y, además, ángulo y momento angular son precisamente uno de los pares conjugados "
    "del curso (el análogo rotacional de posición-momento), así que **sí** está sujeto al principio. La razón última no "
    "es la coincidencia dimensional, sino que ambas magnitudes son variables canónicamente conjugadas.")
old_interp = we["interpretation"]
assert old_interp.startswith("El criterio dimensional convierte una lista")
we["interpretation"] = old_interp + (" Aun así, el filtro dimensional por sí solo no demuestra la conjugación: $x$ y "
    "$p_y$ (posición y momento en direcciones distintas) también tienen producto con dimensiones de J$\\cdot$s y, sin "
    "embargo, son compatibles. Lo decisivo es ser un par canónicamente conjugado, no solo tener las dimensiones correctas.")
set_exact(we, "solution",
    "**(a)** No. **(b)** Sí. **(c)** No.\n\nSolo (b) tiene un producto con dimensiones de J$\\cdot$s.",
    "**(a)** No. **(b)** Sí. **(c)** No.\n\n(a) y (c) se descartan ya por el filtro dimensional (no dan J$\\cdot$s). (b) pasa el filtro dimensional Y es un par conjugado estudiado (ángulo-momento angular): por eso, y no solo por la dimensión, está sujeto al principio.")

# 3) mcq[5]
mcq = l["mcq"][5]
set_exact(mcq, "stem",
    "Usando el criterio dimensional, ¿cuál de estos pares de magnitudes está sujeto al principio de indeterminación?",
    "¿Cuál de estos pares de magnitudes está sujeto al principio de indeterminación (dimensión de J$\\cdot$s Y par conjugado reconocido)?")
set_exact(mcq, "explanation",
    "El criterio es que el producto tenga las dimensiones de la constante de Planck, J$\\cdot$s. El momento angular tiene las mismas dimensiones que $mvr$, es decir $\\mathrm{kg\\,m^2\\,s^{-1}} = \\mathrm{J\\cdot s}$, y el ángulo es adimensional: el producto cumple el criterio. No es casualidad que la magnitud con las dimensiones de $h$ sea precisamente la que Bohr cuantizó en múltiplos de $h/2\\pi$.",
    "El filtro dimensional descarta A, B y D (sus productos no dan J$\\cdot$s). El momento angular y el ángulo sí dan J$\\cdot$s ($\\mathrm{kg\\,m^2\\,s^{-1}}$), pero eso solo los deja como candidatos: lo que confirma que están sujetos al principio es que, además, son el par conjugado rotacional estudiado en el curso (análogo a posición-momento). El filtro dimensional nunca basta por sí solo para afirmar conjugación: $x$ y $p_y$, por ejemplo, también dan J$\\cdot$s y son compatibles.")

# 4) flashcards[2]
set_exact(l["flashcards"][2], "back",
    "Criterio dimensional: lo está si **el producto tiene dimensiones de J$\\cdot$s**, las de la constante de Planck. $[x][p] = \\mathrm{J\\cdot s}$ ✓; $[E][t] = \\mathrm{J\\cdot s}$ ✓; $[F][t] = \\mathrm{kg\\,m\\,s^{-1}}$ ✗. No hay que memorizar ninguna lista.",
    "El criterio dimensional es un filtro **necesario, no suficiente**: si el producto NO tiene dimensiones de J$\\cdot$s (como $[F][t]=\\mathrm{kg\\,m\\,s^{-1}}$ ✗), el par seguro que no está sujeto. Si SÍ las tiene ($[x][p]=\\mathrm{J\\cdot s}$, $[E][t]=\\mathrm{J\\cdot s}$, $[L][\\theta]=\\mathrm{J\\cdot s}$), hay que comprobar además que sea un par conjugado reconocido — no basta con la dimensión (p. ej. $x$ y $p_y$ también dan J$\\cdot$s y son compatibles).")

# 5) summary.key_points[0]
kp = l["summary"]["key_points"]
old_kp0 = ("**El principio:** $\\Delta x\\cdot\\Delta p \\ge h/4\\pi$ y $\\Delta E\\cdot\\Delta t \\ge h/4\\pi$, con "
           "$h/4\\pi = \\hbar/2 = 5{,}3\\cdot10^{-35}$ J$\\cdot$s. Es una cota inferior, acota un **producto**, y el "
           "criterio para saber qué pares cumple es dimensional: que el producto tenga dimensiones de J$\\cdot$s.")
assert kp[0] == old_kp0
kp[0] = old_kp0.replace(
    "y el criterio para saber qué pares cumple es dimensional: que el producto tenga dimensiones de J$\\cdot$s.",
    "el criterio dimensional (producto con dimensiones de J$\\cdot$s) descarta pares que no cumplen, pero no basta por sí "
    "solo para afirmar que un par sí está sujeto: hace falta que además sea un par canónicamente conjugado (posición-"
    "momento en la misma dirección, energía-tiempo, ángulo-momento angular).")

json.dump(d, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK: P0 cuantica/06 (criterio dimensional) corregido: ahora filtro necesario no suficiente, propagado.")
