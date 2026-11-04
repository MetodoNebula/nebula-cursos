# Brief — enriquecimiento de UNA unidad de Matemáticas ESO/Bach

Trabajas SOLO sobre tu bundle: `bundles/eso_matematicas__<UNIDAD>.json` (en el equipo,
bajo `$HOME/mnt/Nebula_GPT_Cowork/Nebula_Cursos_Web/`). NO toques otros bundles,
ni `catalog.json`, ni Selectividad/GCSE. Ejecuta TODO con `device_bash` (LaTeX está
en el equipo del usuario, no en el contenedor). Límite ~110 s por llamada: usa los
scripts reanudables en tandas.

Toolkit (ruta `_mat_enrich_shared/`, relativa a Nebula_Cursos_Web):
- `regen_svgs.py <bundle> [N]`   regenera el SVG de producción de N figuras desde su TikZ (paleta casa + margen amplio). Reanudable. Úsalo hasta cubrir todas.
- `figrender.py <bundle> <outdir> [N]`  compila + puerta de solapes texto-texto + PNG. Reanudable.
- `mksheets.py <outdir>`  hojas de contacto por lección en <outdir>/sheets/.
- `injfig.py <bundle> <fixes.json>`  {id: tikz_nuevo} → regenera SVG e inyecta.
- `inject_exercises.py <bundle> <modulo.py>`  inyecta ejercicios con comprobaciones.
Referencia de oro ya terminada: `bundles/eso_matematicas__mat_funciones_representacion.json`.

## FIGURAS
1. `python3 _mat_enrich_shared/regen_svgs.py <bundle> 8` repetido hasta `regeneradas == total`.
   Si alguna figura falla al compilar (lo verás en figrender), NO la inventes: anota el
   macro/símbolo no definido y repórtalo; sigue con el resto.
2. `figrender.py <bundle> <outdir> 8` repetido hasta procesar todas. Mira `overlaps_auto`.
3. `mksheets.py <outdir>`; sube las hojas con device_stage_files y MÍRALAS (Read).
   Busca: solape texto-texto, texto-línea, texto-curva, rótulo fuera del área, puntos sin
   etiqueta clara. (El PNG que ves usa el mismo preámbulo que el SVG publicado: es fiel.)
4. Para cada figura con defecto: edita SU TikZ moviendo la etiqueta a zona vacía (usa
   anchor, y un conector fino `\draw[gray!55,thin]` si ayuda). Guarda {id: tikz_nuevo} en
   un fixes.json y aplica `injfig.py <bundle> fixes.json`. Re-renderiza y re-mira hasta que quede limpio.
5. Al final, TODAS las figuras deben tener su SVG regenerado (paso 1) aunque no tuvieran defecto.

## EJERCICIOS (6–8 nuevos por lección)
Para cada lección del bundle, lee: `objectives` (ids LO-...), `misconceptions`,
`common_mistakes`, y los `concept_ids` ya usados en sus `exercises`/`keywords`.
Escribe 6–8 ejercicios NUEVOS que:
- Cubran dificultad VARIADA (mezcla d2, d3 y d4; algún d2 de refuerzo; evita que todo sea fácil).
- Estén DIRIGIDOS a los fallos conceptuales de esa lección (uno por misconception al menos).
- Tengan: `id` único (p.ej. `EX-<nnnn>-N1`…), `type` STANDARD/REASONING/CONTEXT,
  `objective_ids` (válidos de la lección), `concept_ids` (válidos de la lección),
  `difficulty` (int), `statement`, `hints` (1–2), `answer` (breve),
  `full_solution` (desarrollo PASO A PASO autocontenido, en prosa, sin `\n`),
  `common_errors` (1–2, atacando la misconception), `provenance":"SOURCE_DERIVED"`.
- LaTeX con `$...$` balanceado. Español. Separador decimal con coma: `$2{,}5$`.
Escribe todo en un módulo Python `ej_<unidad>.py` con `EX={ "<clave_leccion>":[ {...}, ... ] }`
y una función `val()` con asserts que VALIDAN CADA NÚMERO (p.ej. raíces, imágenes, dominios).
Ejecuta `val()` y corrige hasta que pase. Luego `inject_exercises.py <bundle> ej_<unidad>.py`
(hace más comprobaciones: ids únicos, objective/concept válidos, $ balanceado, provenance).

## INTEGRIDAD + INFORME
- Verifica que el bundle carga como JSON tras todo.
- Informe final (texto, conciso): nº figuras regeneradas; figuras corregidas por solape (ids y
  qué era); nº ejercicios nuevos por lección y reparto de dificultad; cualquier figura que no
  compiló (con el macro faltante); confirmación de que val() pasó y la inyección fue OK.
NO regeneres catalog.json (lo hace el orquestador al final). NO cifres nada.
