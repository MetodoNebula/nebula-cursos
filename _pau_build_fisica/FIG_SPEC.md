# FIG_SPEC — Figuras TikZ para el banco PAU Física (centralizadas, validadas)

Generas figuras SVG canónicas del proyecto para una lista de ejercicios, usando EL BUILDER
DEL PROYECTO (latex + dvisvgm) y VALIDÁNDOLAS visualmente (sin solapes). Todo en el PC del
usuario vía device_bash; el rasterizado de revisión se hace en el contenedor (Bash + Read).

## ENTRADA
Tu fichero de grupo: `_pau_build_fisica/_figgroups/<GRP>.json` = lista de ejercicios con
{id, flagged, source, block, title, statement, knowns, full_solution, answer, figure_suggestion}.
Carpeta de exámenes PDF (en el PC): `$HOME/mnt/Nebula_GPT_Cowork/selectividad_fisica_examenes/`.

## PASO 0 — Si flagged=true: RECUPERA LOS DATOS REALES DE LA FIGURA
El texto se extrajo con pdftotext y PERDIÓ datos que solo están en una figura (posiciones de
cargas, ángulos, distancias, lecturas de gráficas). Para cada ejercicio flagged:
1. Localiza el PDF por su `source` (comunidad+convocatoria+año) en la carpeta de exámenes.
   Convocatorias: Junio→06, Julio→07, Septiembre→09, Modelo→mo, Coincidentes→coi,
   Ordinaria→ord, Extraordinaria→ext, "Reserva A/B"→reservaa/reservab. Valencia="valencia",
   Madrid="madrid", Cantabria="cantabria", Murcia="murcia", Andalucía="andalucia".
2. Stage el PDF al contenedor (device_stage_files) y rasteriza páginas:
   container Bash: `pdftoppm -r 200 -png <pdf> /tmp/<id>pg` ; luego Read las PNG para VER la figura.
3. Lee los valores reales (posiciones, cargas con signo, ángulos, distancias, escalas de gráfica).
4. Si difieren de los del texto (que eran reconstruidos), CORRIGE el ejercicio: statement,
   knowns, full_solution y answer con los números REALES, reverificando con python3. Quita del
   enunciado/common_errors las notas de "reconstruido/representativo" que ya no apliquen.
   Si la figura confirma lo que ya había, no cambies el texto.
Devuelve las correcciones (ver SALIDA). Si no hay PDF localizable o la figura no es legible, deja
el texto como está y anótalo.

## PASO 1 — DISEÑA LA FIGURA (TikZ)
Dibuja SOLO lo que aporta (una figura por ejercicio que la necesite). Usa el preámbulo del
builder (ya cargado por compile_figs.py). Macros/estilos/colores disponibles:
- Colores: NebulaNavy (#0B1F3A, trazo principal/texto), NebulaError (morado, vector/fuerza/campo E),
  NebulaCheck (verde, segundo vector/campo B), NebulaAmber (ámbar, destacados), NebulaMuted (gris, auxiliares).
- Estilos: nbline (navy grueso), nbdash (navy discontinuo), nbaxis (eje con flecha),
  nbvec (flecha morada gruesa), nbvecb (flecha verde gruesa). `>=Stealth`.
- Gráficas de ejes (fotoeléctrico Ec-f, desintegración N(t), energía de enlace/nucleón, x-t del MAS):
  usa la macro `\nbfuncplotlab{xmin}{xmax}{ymin}{ymax}{xtick}{ytick}{$xlabel$}{$ylabel$}{<cuerpo pgfplots>}`
  (envuelve un axis listo; dentro usa \addplot[...]{...}; \node, \draw con `axis cs:`).
REGLAS DE ESTILO:
- Fondo claro (el post() pone #f6f8fb). Dibuja en navy/teal/morado/ámbar sobre claro; texto oscuro legible.
- Tamaño compacto: la web limita el SVG a 520×300 px. Mantén la figura pequeña (p.ej. 8–11 cm de ancho TikZ).
- Etiquetas con \footnotesize o \scriptsize. Usa unidades con $...$ y \text{}.
- CERO SOLAPES: texto con texto, texto con línea/flecha/curva, o etiquetas que se montan. Separa
  etiquetas de los trazos (anchors, desplazamientos). Las puntas de flecha no deben pisar texto.

## PASO 2 — COMPILA (en el PC)
Escribe un spec JSON = lista de {id, prefix, title, tikz} y compílalo:
  device_bash: cd .../_pau_build_fisica && python3 compile_figs.py MI_spec.json svgs/<GRP>_raw.json
  (prefix = id en minúsculas, p.ej. "pau-fis-opt-005"; title = breve, para <title> del SVG).
Si algún id sale en FAIL, corrige el TikZ y recompila (puedes usarlo incremental: añade 'merge' como 3er arg).

## PASO 3 — VALIDA VISUALMENTE (rasteriza y MIRA)
Para cada SVG producido:
  device_bash (python): vuelca cada svg a svgs/png_src/<id>.svg
  device_stage_files los .svg al contenedor
  container Bash: `rsvg-convert -z 2 <staged.svg> -o /tmp/<id>.png`
  Read /tmp/<id>.png  → inspecciona: ¿solapes texto-texto o texto-línea? ¿etiquetas legibles?
  Si hay solape o se ve mal, AJUSTA el TikZ (mueve etiquetas, cambia anchors, separa trazos) y repite
  PASO 2–3 hasta que quede LIMPIO. No entregues una figura con solapes.

## SALIDA (dos ficheros, escritura atómica con python)
1. `_pau_build_fisica/svgs/<GRP>_final.json` = {id: svg_string}  (solo los SVG ya validados y limpios)
2. `_pau_build_fisica/corrections/<GRP>.json` = {id: {caption, statement?, knowns?, full_solution?, answer?}}
   - caption: pie de figura breve en español (obligatorio para cada id con figura).
   - statement/knowns/full_solution/answer: SOLO si corregiste datos reales (si no, omítelos).
Reporta: nº de figuras validadas, nº de ejercicios con datos corregidos, y cualquier id sin figura (con motivo).

## CALIDAD
Figura exacta al problema (geometría, signos de carga, sentido de vectores, orientación de rayos).
Mejor pocas figuras impecables que muchas con solapes. Español en todas las etiquetas.
