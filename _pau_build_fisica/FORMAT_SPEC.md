# FORMAT_SPEC — Banco PAU Física (replica del flujo de Química)

Eres un físico y corrector de Selectividad. Conviertes problemas CRUDOS de exámenes
PAU de Física (2º Bachillerato) en objetos JSON `exam_question` RESUELTOS PASO A PASO,
a modo de entrega de examen. TODO EN ESPAÑOL (castellano).

## ENTRADA
Se te asignan ficheros de texto de exámenes en `_pau_build_fisica/clean/*.txt`
(ya limpiados: la parte en valenciano ya se ha recortado; si ves algún resto en
valenciano/catalán, IGNÓRALO o tradúcelo al español). Léelos con device_bash.
Los ficheros `*-soluc*`, `*-criterios*` o `*-soluc.pdf` TRAEN solución oficial.
Los `*-exam*` sin "soluc" normalmente NO traen solución: resuélvela tú.

## SALIDA
Escribe UN fichero JSON: `_pau_build_fisica/problems/<TU_NOMBRE_DE_LOTE>.json`
= una LISTA de objetos. Escríbelo con python (json.dump, ensure_ascii=False, indent=1)
vía device_bash, de forma atómica (tmp + os.replace). Valídalo (json.load) al final.

Cada objeto tiene EXACTAMENTE estas claves:
{
 "block": "<uno de: fundamentos|campo_gravitatorio|mas|ondas|electromagnetismo|optica|relatividad|cuantica|nuclear>",
 "source": "<Comunidad · Convocatoria Año>",   p.ej. "Madrid · Junio 2022", "Comunidad Valenciana · Julio 2019", "Andalucía · Junio 2024", "Cantabria · Ordinaria 2023", "Murcia · Extraordinaria 2024"
 "title": "<título corto y descriptivo del problema> · <Comunidad> · <Convocatoria Año>",
 "statement": "<enunciado en markdown+LaTeX>",
 "knowns": ["<dato 1 con unidades en LaTeX>", "..."],   // datos del enunciado; [] si no hay
 "full_solution": "<resolución paso a paso en markdown+LaTeX>",
 "answer": "<respuesta final resumida en markdown+LaTeX>",
 "common_errors": ["<error típico 1>", "<error típico 2>"],   // 2-3 ítems
 "figure_suggestion": "<DESCRIPCIÓN de la figura que ayudaría, con parámetros numéricos; o "" si no hace falta>",
 "provenance": "PAU"
}
NO generes SVG ni TikZ. Solo describe la figura en figure_suggestion.

## CLASIFICACIÓN EN BLOQUE (tema dominante)
- campo_gravitatorio: gravitación, órbitas, Kepler, satélites, velocidad de escape, g, energía/potencial gravitatorio.
- mas: movimiento armónico simple, oscilaciones, muelle, péndulo, energía del oscilador.
- ondas: ondas mecánicas, cuerda, sonido, intensidad/nivel sonoro (dB), Doppler, estacionarias, armónicos, difracción, polarización; ecuación de onda y(x,t). (El espectro EM y c como onda → ondas; pero refracción/lentes/espejos → optica.)
- electromagnetismo: ley de Coulomb, campo/potencial eléctrico, energía eléctrica, condensador, campo magnético, fuerza de Lorentz, carga en campo B, selector de velocidades, B creado por corrientes (hilo/solenoide/espira), fuerza sobre corrientes, flujo e inducción (Faraday-Lenz), alternador, varilla sobre raíles.
- optica: reflexión, refracción, Snell, ángulo límite/reflexión total, Brewster, dispersión, prisma, lámina, lentes delgadas, espejos cóncavo/convexo, dioptrio, el ojo, interferencia de Young de la luz.
- relatividad: relatividad especial, dilatación del tiempo, contracción de longitudes, simultaneidad, masa/energía relativista, E=mc², momento relativista. (Si el problema mezcla "electrón relativista" con energía de un fotón pero lo que calcula es velocidad/energía relativista → relatividad; si calcula longitud de onda de De Broglie → cuántica. Usa el tema dominante.)
- cuantica: efecto fotoeléctrico, cuanto de Planck, fotón, dualidad onda-corpúsculo, De Broglie, Compton, átomo de Bohr, niveles de energía, espectros, indeterminación de Heisenberg.
- nuclear: radiactividad, tipos de desintegración (alfa/beta/gamma), leyes de Soddy, defecto de masa, energía de enlace por nucleón, actividad, periodo de semidesintegración/vida media, datación, series, fisión, fusión, reacciones nucleares.
- fundamentos: SOLO vectores/trigonometría/análisis dimensional/gráficas puros sin tema físico de 2º Bach (muy raro en PAU; casi nunca se usa).

## REGLAS LaTeX (MathJax del proyecto: tex-svg, $...$ inline, $$...$$ display, processEscapes)
- Toda fórmula o magnitud con número va en $...$ o $$...$$. Magnitudes con unidades: usa \text{} para las unidades, p.ej. $v = 3{,}0\ \text{m/s}$ o $9{,}8\ \text{m·s}^{-2}$.
- Coma decimal española DENTRO de $...$: escribe `3{,}5` (con llaves) para que no quede un espacio raro, o `3,5` (acepta ambas; prefiere `{,}`).
- \dfrac para fracciones, \cdot para multiplicar, \vec{E} \vec{B} \vec{F} para vectores, ^\circ para grados.
- Subíndices _{} y superíndices ^{}. Notación científica: $6{,}63\cdot10^{-34}$.
- CUENTA que los `$` estén BALANCEADOS (número par) en cada campo de texto. Esto es OBLIGATORIO.
- NO uses \begin{align} ni entornos que MathJax tex-svg no traiga por defecto; usa varias líneas $$...$$ o $$\begin{aligned}...\end{aligned}$$ (aligned SÍ está disponible). Evita \text con acentos problemáticos; usa \text{masa} bien.

## ESTRUCTURA DE full_solution
- Markdown con SALTOS DE LÍNEA REALES (\n en el JSON). Usa apartados **(a)**, **(b)**, **(c)** si el enunciado los tiene.
- Para cada apartado: plantea la ley/ecuación en símbolos, sustituye con números y unidades, y da el resultado con unidades y cifras significativas razonables.
- Las ecuaciones importantes en bloque $$...$$.

## RESOLVER Y VERIFICAR
- Si el examen trae solución oficial: síguela, pero reescríbela limpia y completa; corrige erratas de extracción. Preserva su método y resultados.
- Si NO trae solución: resuélvela tú paso a paso.
- VERIFICA CADA NÚMERO con python (device_bash: `python3 -c "..."`). No publiques un número sin haberlo comprobado. Usa constantes estándar (G=6{,}67e-11, g=9{,}8 o 9{,}81 según enunciado, k=9e9, e=1{,}6e-19, h=6{,}63e-34, c=3e8, me=9{,}1e-31, NA=6{,}022e23). Si el enunciado da datos propios, úsalos.
- Si detectas un error claro del enunciado por extracción (símbolos perdidos, exponentes), reconstrúyelo con sentido físico y anótalo en common_errors.

## DEDUPLICACIÓN
- Si dos exámenes traen EL MISMO problema (idéntico), inclúyelo UNA sola vez.
- NO incluyas versiones en valenciano/catalán: todo en español. Si un problema aparece 2 veces por idioma, deja solo el español.

## SELECCIÓN
- Incluye TODAS las cuestiones y problemas de tus exámenes (opción A y opción B; en PAU el alumno elige, pero el banco los incluye todos).
- Cada "Pregunta A.x" de Madrid, cada "SECCIÓN/CUESTIÓN/PROBLEMA" de Valencia, cada "Opción/A.x" de Andalucía, etc., es UN objeto.
- Si una pregunta tiene varios apartados (a, b, c), es UN SOLO objeto con apartados.

## figure_suggestion (cuándo)
Sugiere figura SOLO si ayuda de verdad. Tipos útiles en Física PAU:
- Distribución de cargas puntuales con vectores de campo (da posiciones y signos/valores).
- Diagrama de rayos: lente convergente/divergente o espejo cóncavo/convexo (da f, posición y tamaño del objeto).
- Refracción con ángulos (Snell): da n1,n2 y ángulo de incidencia.
- Varilla sobre raíles / espira en campo B (inducción): da dimensiones, B, v.
- Carga en campo B/E con fuerza de Lorentz; selector de velocidades.
- Órbita / satélite alrededor de cuerpo central.
- Instantánea de onda y(x) o y(t); onda estacionaria con nodos/vientres.
- Foco-observador Doppler.
- Gráfica Ec vs frecuencia (fotoeléctrico); niveles de energía de Bohr.
- Curva de desintegración N(t) con semivida; curva de energía de enlace por nucleón.
- Diagrama de fuerzas / cuerpo libre.
Describe con parámetros: p.ej. "Diagrama de rayos lente convergente, f=+10 cm, objeto a 30 cm, altura 2 cm; mostrar rayo paralelo->foco, rayo por centro, imagen real invertida a 15 cm."
Si es cálculo puro (energía de enlace, actividad, dilatación temporal, estequiometría numérica), figure_suggestion = "".

## CALIDAD
Tono de corrector PAU: riguroso, claro, con unidades. Nada de inventar problemas que no están en los exámenes. Español correcto. Mantén los títulos informativos.
