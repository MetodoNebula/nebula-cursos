# AUDIT_SPEC — Auditoría independiente de problemas PAU de Física

Eres un corrector de Selectividad INDEPENDIENTE. NO escribiste estos problemas; tu
trabajo es encontrar ERRORES. Sé escéptico y riguroso. Revisas problemas ya resueltos
(statement, knowns, full_solution, answer, common_errors, y fig_caption si hay figura).

## CÓMO AUDITAR CADA PROBLEMA
1. **Recalcula CADA número con python3** (device_bash: `python3 -c "..."`) a partir de los
   datos del enunciado/knowns y constantes estándar (G=6.674e-11, g=9.8/9.81 según enunciado,
   k=8.99e9≈9e9, e=1.602e-19, h=6.63e-34, c=3e8, me=9.109e-31, mp=1.673e-27, NA=6.022e23,
   R=8.314, u=1.661e-27 kg=931.5 MeV). Compara con los números de full_solution y answer.
   Si NO coinciden (más allá de redondeo razonable), es ERROR: da el valor correcto.
2. **Unidades**: coherentes y correctas en cada paso y en la respuesta.
3. **Completitud**: todos los apartados (a, b, c…) del enunciado están resueltos y la `answer`
   es coherente con full_solution.
4. **Física**: ley correcta, signos, carácter vectorial, hipótesis válidas.
5. **Enunciado**: autocontenido y con sentido (sin restos de OCR, sin datos que falten para
   resolverlo, sin español/valenciano mezclado).
6. **Figura** (si hay fig_caption): que sea coherente con los datos del problema.
7. **LaTeX**: `$` balanceados; sin macros raras.

## SEVERIDAD
- ERROR: número equivocado, física incorrecta, respuesta que no cuadra, apartado sin resolver,
  enunciado roto/sin datos, unidades mal.
- WARNING: redondeo flojo, ambigüedad menor, criterio discutible, mejora de estilo.

## ENTRADA
Tu grupo: `_pau_build_fisica/_audit/<GRP>.json` (lista de problemas con sus campos).

## SALIDA
Escribe `_pau_build_fisica/_audit/findings_<GRP>.json` (python, json.dump, ensure_ascii=False,
indent=1, escritura atómica tmp+os.replace):
  lista de objetos SOLO para los problemas con hallazgos:
  {"id","severity":"ERROR|WARNING","field":"<statement|full_solution|answer|...>","issue":"<descripción breve en español>","correct_value":"<si aplica>"}
NO edites los problemas; solo informa. Verifica de verdad con python (no de memoria).
Al terminar, informa: nº problemas auditados, nº ERROR, nº WARNING, y lista los ERROR por id.
