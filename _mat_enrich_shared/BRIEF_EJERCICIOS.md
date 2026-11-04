# Brief — redactar EJERCICIOS para UNA unidad de Matemáticas ESO/Bach

LAS FIGURAS YA ESTÁN HECHAS. No toques figuras, ni `svg`, ni `tikz`. SOLO añades
ejercicios al array `exercises[]` de cada lección de TU bundle. No toques otros bundles,
ni catalog.json, ni Selectividad/GCSE. Ejecuta todo con `device_bash`.

Tu bundle: `bundles/eso_matematicas__<UNIDAD>.json` (en `$HOME/mnt/Nebula_GPT_Cowork/Nebula_Cursos_Web/`).

## Referencia de ORO (imítala en calidad y estilo)
`bundles/eso_matematicas__mat_funciones_representacion.json` — mira sus ejercicios con id
`EX-07xx-Nk` (provenance SOURCE_DERIVED): enunciado claro, 1-2 `hints`, `answer` breve,
`full_solution` en PROSA paso a paso autocontenida, `common_errors` que atacan una
misconception concreta. Ese es el nivel que debes alcanzar.

## Qué añadir: 6–8 ejercicios NUEVOS por lección
Para CADA lección del bundle, primero LEE: `objectives` (ids LO-...), `misconceptions`,
`common_mistakes`, `worked_examples`, y los `concept_ids` usados en sus `exercises`/`keywords`.
Luego redacta 6–8 ejercicios nuevos que:
- Tengan dificultad VARIADA y bien repartida (mezcla d2, d3 y d4; evita que todo sea fácil; puedes incluir 1 d5 de reto).
- Estén DIRIGIDOS a los fallos conceptuales de ESA lección: al menos uno por cada misconception listada. El enunciado debe tender una "trampa" donde el alumno con ese error falla.
- NO sean genéricos ni de relleno: cada uno aporta algo (un caso nuevo, una variante, un contexto real, una trampa distinta). Nada de clonar el mismo ejercicio cambiando números.
- Campos: `id` único (patrón `EX-<nnnn>-N1`, `N2`…, usando el código de la lección), `type` (STANDARD/REASONING/CONTEXT), `objective_ids` (VÁLIDOS de la lección), `concept_ids` (VÁLIDOS de la lección), `difficulty` (int 2–5), `statement`, `hints` (1–2), `answer` (breve), `full_solution` (desarrollo PASO A PASO en prosa, autocontenido, que un alumno pueda seguir sin ayuda; NADA de "se deja como ejercicio" ni "como en el ejemplo anterior"; sin `\n`), `common_errors` (1–2 atacando la misconception), `provenance":"SOURCE_DERIVED"`.
- LaTeX con `$...$` balanceado. Español. Separador decimal coma: `$2{,}5$`.

## Validación OBLIGATORIA
Escribe todo en un módulo Python `ej_<unidad>.py` con:
  EX = { "<clave_leccion_exacta>": [ {ejercicio}, ... ], ... }
  def val():  # asserts que comprueban CADA número que afirmas (raíces, imágenes, dominios, áreas, porcentajes, probabilidades, derivadas…). Usa math; usa assert y math.isclose para decimales.
Ejecuta `python3 -c "import ej_<unidad> as m; m.val(); print('OK')"` y corrige hasta que pase.
Luego inyecta: `python3 _mat_enrich_shared/inject_exercises.py bundles/eso_matematicas__<UNIDAD>.json ej_<unidad>.py`
(ese script revalida: ids únicos, objective/concept válidos, $ balanceado, provenance, solución no trivial; si falla, corrige y reintenta).

## Informe final (conciso)
- nº ejercicios nuevos por lección y reparto de dificultad (d2/d3/d4/d5).
- confirmación de que val() pasó y la inyección fue OK (el bundle carga como JSON).
- 1 ejemplo de un ejercicio "trampa conceptual" que hayas escrito (id + una línea).
NO regeneres catalog.json. NO cifres. NO toques figuras.
