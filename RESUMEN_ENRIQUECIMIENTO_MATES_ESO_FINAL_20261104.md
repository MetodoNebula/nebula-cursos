# Enriquecimiento de Matemáticas ESO/Bachillerato — Informe final

**Curso:** `eso_matematicas` (Nebula_Cursos_Web) · **Fecha:** 2026-11-04
**Alcance respetado:** solo los 21 bundles `eso_matematicas__*.json`. No se tocó Selectividad, GCSE, FQ ni ningún otro curso. `catalog.json` solo se regeneró al final (conteos); su estructura de 9 cursos quedó intacta.

---

## 1. Qué se ha hecho

### Figuras (todas en TikZ, validadas)
- **324 figuras** en las 21 unidades, **regeneradas desde su fuente TikZ** con un preámbulo unificado y la paleta de la casa (curvas verdes, ejes azul marino, puntos ámbar/violeta).
- Se corrigió la causa de los **cuadros blancos**: las etiquetas del borde caían fuera del rectángulo de fondo. Ahora todas las SVG se generan con **margen amplio y fondo completo** → sin cuadros blancos en el texto.
- Revisión visual rasterizando las SVG **reales publicadas** (no el render de TikZ), para que lo auditado sea exactamente lo que verá el alumno. Se detectaron y arreglaron **5 figuras con solapes** texto-texto/texto-línea; el resto quedó limpio.

### Ejercicios (nuevos, desarrollados, dirigidos a errores conceptuales)
- **926 ejercicios nuevos añadidos** (delta real frente al backup), **0 eliminados**: trabajo aditivo, no se perdió nada del contenido previo.
- Reparto por unidad (añadidos):

| Unidad | +Ej | Unidad | +Ej |
|---|---|---|---|
| foundations | 49 | geometria_analitica | 52 |
| algebra_polinomios | 37 | geometria_metrica | 56 |
| complejos | 35 | limites_continuidad | 39 |
| conicas | 35 | numeros_operaciones | 49 |
| derivadas | 56 | potencias_raices | 35 |
| distribuciones | 28 | probabilidad | 55 |
| ecuaciones | 37 | proporcionalidad_financiera | 35 |
| estadistica_bidimensional | 49 | sistemas_inecuaciones | 49 |
| estadistica_descriptiva | 35 | sucesiones | 42 |
| familias_funciones | 49 | trigonometria | 63 |
| funciones_representacion | 41 | **TOTAL** | **926** |

- Cada ejercicio incluye: enunciado, **`full_solution` en prosa paso a paso** (razona cada paso, con comprobación final), `answer`, `hints`, `common_errors` y metadatos (`objective_ids`, `concept_ids`, `difficulty`, `type`). `provenance: SOURCE_DERIVED`.
- **Dificultad variada** (d2–d5) y **cada lección cubre sus misconceptions**: el campo `common_errors` apunta a la trampa concreta. Ejemplos:
  - *Covarianzas no comparables entre escalas* (solo `r` es adimensional).
  - *Atípico ≠ erróneo*: antes de borrar el 95 del hospital hay que comprobar si es error o dato real.
  - *Sistema 3×3 donde fila₃ = fila₁+fila₂* → compatible indeterminado, no solución única.
  - *z⁴=16*: por qué solo k=0..3 (k=4 repite la dirección de k=0).
  - *Enteros consecutivos*: plantear x+(x+1)+(x+2), no x+x+x.

---

## 2. Auditoría (los tres criterios pedidos)

**(a) Figuras sin cuadros blancos ni solapes** — OK
324/324 figuras regeneradas; margen y fondo corregidos; 5 solapes arreglados; revisión visual sobre las SVG reales. El conteo de assets es idéntico al backup (324/324): **ningún agente de ejercicios tocó una sola figura**.

**(b) Contenido pedagógico, paso a paso** — OK
Lectura profunda de una muestra estratificada: los **2 ejercicios de mayor dificultad de cada unidad (42 en total)**, donde más probable es que se escondan errores. Se verificó la **matemática de los 42 a mano/Python**: todas correctas, con solución desarrollada y comprobación. Además, cada agente validó **cada número con asserts de Python** antes de inyectar, y las unidades complejos, potencias y números se auditaron en profundidad aparte.

**(c) No genérico ni relleno** — OK
Los ejercicios son contextualizados (silo cilindro+cono, examen tipo test binomial, estanque elíptico, elevación de un edificio con dos ángulos) y cada uno ataca un error conceptual nombrado, no variaciones triviales.

**Integridad (21 bundles):** todos cargan como JSON · ids únicos (sin duplicados) · `objective_ids`/`concept_ids` válidos · `$` balanceados · soluciones >=60 car. (única excepción: `EX-1203-S1`, un ejercicio **preexistente** trivial pero correcto, no añadido por este trabajo).

---

## 3. Qué queda por hacer (tú)

El único paso pendiente es **publicar cifrando con tu contraseña**:

    node cifrar.js      (o)      publicar.bat

Esto regenera los `cifrado/*.bin` que lee la web. No puedo hacerlo yo porque requiere el secreto.

---

## 4. Notas

- **Backup de rollback:** `bundles/_backup_mat_enrich_20261104_002419/` conserva los 21 bundles + catalog.json previos. Bórralo cuando estés conforme.
- **Toolkit reutilizable** en `_mat_enrich_shared/` (regenerar figuras, inyectar más ejercicios, auditar): `regen_svgs.py`, `inject_exercises.py`, `figrender.py`, `audit_final.py`, `valid_preamble.tex`, etc.
- Los ficheros de trabajo (`ej_*.py`, cachés `.regen.json`, scratch) ya se eliminaron.
