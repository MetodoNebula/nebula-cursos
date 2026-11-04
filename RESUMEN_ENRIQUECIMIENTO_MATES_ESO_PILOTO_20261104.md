# Enriquecimiento Matemáticas ESO/Bach — PILOTO (unidad `mat_funciones_representacion`)

**Fecha:** 2026-11-04 · **Backup:** `bundles/_backup_mat_enrich_20261104_002419/` (21 bundles + catalog, intacto)
**Alcance de esta fase:** solo la unidad piloto, dentro de `Nebula_Cursos_Web/bundles/eso_matematicas__mat_funciones_representacion.json`. Selectividad y GCSE no se tocan.

## 1 · Figuras (todas en TikZ, validadas)
- **33 figuras** de la unidad: las 33 compilan desde su fuente `tikz` con un preámbulo unificado reconstruido (motor `nebula_figures.tex` + estilos `_fig_build` + estilos huérfanos `nbdotA/nbdotV/nbaxisbase/nbaux/nbsym/nbtangent` reconstruidos por uso).
- **Puerta automática texto-texto** (`check_overlap.py` sobre el PDF): 0 colisiones en las 33.
- **Revisión visual** (render a PNG, hojas de contacto): **4 figuras** con solape texto-línea / texto-gráfica que la puerta automática NO detecta —
  - `diag_004`: "eje de simetría" montada sobre la línea discontinua y pisando la fórmula.
  - `AS-0705-2`: etiqueta larga "(3,6) no pertenece a la gráfica" cruzando la recta.
  - `AS-0705-3`: etiqueta de asíntota "x=0" amontonada con el eje/ticks.
  - `AS-0706-4`: "dominio empieza en x=3" pisando los números del eje X.
- Las 4 se **corrigieron** (reubicación de etiqueta a zona vacía + conector fino), se re-renderizaron, pasan la puerta y se re-inspeccionaron a tamaño real. Se regeneró su **SVG de producción** (pipeline dvisvgm + remapeo de color web + marcador `data-nebula-fig='cool'` + rect de fondo) y se reinyectó `tikz`+`svg` en el bundle.

## 2 · Ejercicios nuevos
- **41 ejercicios nuevos** (6–8 por lección), `provenance: SOURCE_DERIVED`, repartidos en dificultad y dirigidos a los **fallos conceptuales** de cada lección (imagen vs preimagen, dominio/recorrido intercambiados, corte con X usando f(0), máximo como x en vez de y, par/impar comprobado con un solo valor, f(x−a) hacia la izquierda, −f(x) vs f(−x), salto vs hueco, rama equivocada en funciones a trozos, parte entera de negativos, radicando ≥ 0…).
- Cada ejercicio: enunciado, `hints`, `answer`, `full_solution` **paso a paso autocontenida** y `common_errors`.
- **Todos los números validados con Python** (assert) antes de inyectar.
- Distribución de dificultad del piloto tras el enriquecimiento: d1=12, d2=49, d3=18, d4=12 → **dif≥3 = 33%** (antes ≈6%).

## 3 · Integridad
- El bundle carga como JSON; ids únicos; `objective_ids` y `concept_ids` válidos por lección; sin `$` desbalanceado; sin soluciones vacías.
- `catalog.json` regenerado con `scripts/rebuild_catalog.py`.
- Solo se modificaron el bundle piloto y `catalog.json`.

## 4 · Pendiente de publicación
- La web sirve la versión **cifrada** (`cifrado/*.bin`). Para publicar hay que ejecutar `node cifrar.js` (o `publicar.bat`) con la contraseña del curso — paso que corresponde al propietario.

## 5 · Herramientas de trabajo (reutilizables para el resto de unidades)
- `_mat_enrich_20261104_002419/valid_preamble.tex` — preámbulo unificado de validación.
- `_mat_enrich_20261104_002419/validate.py` — compila + puerta de solapes + PNG, reanudable.
- `_mat_enrich_20261104_002419/gensvg.py` — regenera SVG de producción desde TikZ.
- `_mat_enrich_20261104_002419/ejercicios/*.py` — ejercicios con validación numérica.
