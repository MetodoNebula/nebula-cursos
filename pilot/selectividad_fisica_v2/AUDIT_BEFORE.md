# AUDIT_BEFORE — Selectividad Física (curso `selectividad_fisica`)

Generado automáticamente a partir del corpus **original** (`original/selectividad_fisica/`, copia congelada de `bundles/selectividad_fisica__*.json`, sin modificar) mediante `scripts/pilot_fisica/inventory.py` y `scripts/pilot_fisica/semantic_lint.py`. Cifras cruzadas con `catalog.json` y con los documentos de auditoría obligatorios (`00_MASTER_IMPLEMENTATION_SPEC.md`, `02_auditoria_reestructuracion/cursos/01_SELECTIVIDAD_FISICA.md`, `semantic_change_ledger.csv`, `qa_por_curso/selectividad_fisica_structural_issues.csv`).

## 1. Estructura actual

| Unidad | Lecciones | Palabras (auditoría previa) | Palabras (recuento propio, solo prosa) |
|---|---:|---:|---:|
| campo_gravitatorio | 9 | 135.040 | 158.943 |
| mas | 7 | 94.259 | 145.699 |
| ondas | 12 | 166.360 | 179.335 |
| electromagnetismo | 14 | 186.440 | 228.079 |
| optica | 11 | 149.374 | 252.517 |
| relatividad | 7 | 100.537 | 143.517 |
| cuantica | 6 | 85.328 | 102.059 |
| nuclear | 10 | 127.701 | 142.712 |
| **Total** | **76** | **1.045.039** | **1.534.900 (ver nota)** |

> Nota metodológica: la columna "auditoría previa" reproduce las cifras ya certificadas en `02_auditoria_reestructuracion/cursos/01_SELECTIVIDAD_FISICA.md` (coinciden exactamente, 1.045.039 en total). La columna "recuento propio" usa una metodología distinta y más amplia (todas las cadenas de texto narrativo en `objectives/theory_blocks/keywords/worked_examples/guided_exercises/exercises/exam_questions/challenge_questions/mcq/flashcards/misconceptions/common_mistakes/exam_notes/summary`, excluyendo expresiones LaTeX entre `$...$` y marcado Markdown). Se incluye como señal adicional de inventario, no sustituye a la cifra oficial. Con cualquiera de los dos métodos el curso es muy extenso y varias lecciones superan el ritmo de estudio razonable (ver §3).

**Piezas por tipo** (coincide exactamente con `catalog.json.projects[selectividad_fisica].total.por_tipo`, lo que valida el script de inventario):

| Tipo | Nº |
|---|---:|
| objectives | 483 |
| prerequisites | 307 |
| diagnostic_items | 200 |
| theory_blocks | 702 |
| keywords | 705 |
| worked_examples | 321 |
| guided_exercises | 180 |
| exercises | 311 |
| exam_questions | 173 |
| challenge_questions | 65 |
| mcq | 533 |
| flashcards | 779 |
| misconceptions | 190 |
| common_mistakes | 457 |
| exam_notes | 482 |
| **Total piezas** | **5.888** |

Cada lección actual ya trae: objectives, prerequisites (texto, sin concept-graph formal), diagnostic_items, theory_blocks (tipados `intuition/core/...` con campo `scope`), keywords, worked_examples, guided_exercises, exercises, exam_questions, challenge_questions, mcq, flashcards, misconceptions, common_mistakes, exam_notes y summary (`big_idea`, `key_points`, `formulas`, `what_to_remember_if_nothing_else`). Es decir: el contenido pedagógico de base es rico y en su mayoría reutilizable — el problema no es ausencia de material sino: (a) errores/absolutismos científicos puntuales, (b) ausencia de arquitectura de rutas adaptativas y de grafo de prerrequisitos formal, (c) algunas lecciones demasiado largas, y (d) schema plano sin `canonical_lesson_id`/`epistemic_type`/rutas.

## 2. Backlog obligatorio de corrección científica (semantic_change_ledger.csv, `course=selectividad_fisica`)

22 filas: **P0 = 2, P1 = 6, P2 = 14**.

- P0 (2): inducción electromagnética presentada con movimiento relativo como condición necesaria (`electromagnetismo/12`); criterio dimensional usado como condición suficiente de pares conjugados (`cuantica/06`).
- P1 (6): rozamiento "siempre" trabajo negativo (`campo_gravitatorio`); negación global de potencial/energía potencial magnética (`electromagnetismo/06`); polarización dieléctrica descrita siempre en sentido contrario a E (`electromagnetismo` dieléctricos); motivación incorrecta de la necesidad de la RG (`relatividad` intro GR); máximo de energía de enlace atribuido en exclusiva a Fe-56 (`nuclear`); regla Z>83 inconsistente con estabilidad estricta (`nuclear`).
- P2 (14): Kepler T²/a³ solo con r; a=g sin caída libre explícita; g máxima como EXACT en vez de MODEL; MAS ideal generalizado a toda oscilación; solenoide "uniforme en todo el interior"; I∝A² mal acotado; "los decibelios no se suman" sin explicar por qué; estacionarias sin superposición como razón; nodos/antinodos sin magnitud; idealizaciones ópticas sin etiqueta de modelo; "localmente" ausente en equivalencia; tiempo propio mal definido; producción de pares sin marcar MODEL/APPROX; λ=h/mv presentada como fórmula fundamental en vez de λ=h/p.

Todas se tratan como backlog obligatorio, no como sugerencias (Fase 1 de este piloto).

## 3. QA estructural detectado (`qa_por_curso/selectividad_fisica_structural_issues.csv`)

6 lecciones / 7 filas requieren fragmentación o poolización prioritaria:

| Unidad | Lección | Severidad | Palabras |
|---|---|---|---:|
| ondas | 05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json | medium (content_overload) | 13.830 |
| ondas | 11_Ondas_estacionarias_la_onda_que_no_viaja.json | high (very_long_lesson) | 18.306 |
| optica | 03_El_ángulo_límite_y_la_reflexión_total.json | medium (content_overload) | 13.725 |
| campo_gravitatorio | 02_La_ley_de_gravitación_universal.json | medium + high | 18.070 |
| cuantica | 06_Indeterminación_y_la_nueva_mecánica_cuántica.json | medium (content_overload) | 14.633 |
| electromagnetismo | 05_El_potencial_eléctrico_sumar_sin_vectores.json | high (very_long_lesson) | 20.190 |

Esta lista (del CSV oficial) es la que gobierna la Fase 4 de atomización. El recuento propio (§1) detecta además otras ~38 lecciones por encima de 9.000 palabras/hora con la metodología amplia; se documentan en `scripts/pilot_fisica/inventory_BEFORE.json` como señal adicional, pero **no** se tratan como backlog obligatorio de fragmentación porque el criterio oficial del curso es el CSV citado — fragmentar más allá de lo indicado no está en el mandato y violaría la regla de "no reescribir por estilo si ya es correcto y claro".

## 4. Duplicados

- IDs de lección (`id`, p.ej. `L01`): únicos dentro de cada unidad (son identificadores por unidad, no por curso — se resuelve con `canonical_lesson_id` global en Fase 3).
- Contenido duplicado (hash de título + cuerpos de theory_blocks): **0 grupos** duplicados detectados entre las 76 lecciones.

## 5. Precisión científica — temas de riesgo (Master §14 + auditoría de curso)

Revisados específicamente por el ledger: inducción electromagnética, flujo magnético, condiciones de aplicación de fórmulas (B=μnI solenoide, I∝A², λ=h/p), física cuántica (indeterminación, producción de pares), relatividad (equivalencia, tiempo propio, motivación GR), rozamiento, aproximaciones, signos, unidades, vectores, conservación de energía, interpretación gráfica (nodos/antinodos). Todos estos puntos están cubiertos por el backlog de §2; no se han encontrado en esta fase errores científicos adicionales no documentados por el ledger (se revisará de nuevo durante la extracción de `knowledge_model` en Fase 3, lección por lección).

## 6. Lint semántico de palabras absolutas (recuento bruto, antes de corregir)

Script `semantic_lint.py` sobre todo el texto narrativo de las 76 lecciones:

| Término | Ocurrencias |
|---|---:|
| solo / sólo | 2.322 |
| siempre | 1.323 |
| exactamente | 988 |
| cualquier | 529 |
| nunca | 521 |
| por definición | 33 |
| garantiza | 29 |
| toda partícula | 15 |
| en todos los casos | 14 |
| todo cuerpo | 7 |
| jamás | 6 |
| **Total** | **5.787** |

**Interpretación:** la inmensa mayoría son usos discursivos inocuos ("solo necesitas", "no siempre es fácil ver que…", "cualquier duda"), no afirmaciones científicas absolutas. Revisar 5.787 ocurrencias palabra por palabra no es la vía que exige el Master Spec: la resolución real (§5 del Master) es que cada `core_claim`/`formula` canónico extraído en `knowledge_model` lleve su `epistemic_type` (`EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`) y sus `conditions`. Esa extracción (Fase 3) es el mecanismo que cierra el lint de forma escalable; los 22 casos del ledger (que sí son afirmaciones absolutas científicamente problemáticas) se corrigen textualmente en Fase 1. El recuento bruto queda guardado en `scripts/pilot_fisica/semantic_lint_BEFORE.json` para trazabilidad y para repetir el lint después de la migración (`semantic_lint_AFTER.json`) y confirmar que ningún claim de alto riesgo quedó sin condiciones.

## 7. Prerrequisitos

Cada lección ya declara `prerequisites[]` (texto + `id` tipo `P-F08`), pero son prerrequisitos de **skill** (álgebra, notación científica, vectores…) sin un grafo formal de `prerequisite_concept_ids` entre lecciones del curso ni microlecciones Foundation reutilizables a las que enlazar cuando el alumno falla el diagnóstico. Esto se construye en Fase 5 (módulo 00 Foundations) y Fase 3 (añadir `prerequisite_concept_ids` resolubles en `learning_design`).

## 8. Summaries, flashcards, MCQ, soluciones, feedback

- **Summaries**: 76/76 lecciones tienen `summary.{big_idea,key_points,formulas,what_to_remember_if_nothing_else}`. Correcto en estructura; el contenido debe regenerarse donde el ledger corrige un claim que el summary también afirmaba (propagación, Fase 1).
- **Flashcards**: 779, todas con `front/back/concept_id/difficulty`. Ninguna detectada (en esta fase) convirtiendo una aproximación en ley de forma que contradiga el ledger fuera de los casos ya listados; se revisa en Fase 1 al propagar cada corrección.
- **MCQ**: 533, con `options[].{key,text,why_wrong}`, `correct`, `explanation`. Validación estructural completa (una opción correcta, `why_wrong` solo en incorrectas, referencia a `objective_id`/`concept_id` existente) se ejecuta en Fase 7 (QA automatizado) sobre las 533 preguntas, no solo sobre una muestra.
- **Soluciones**: `worked_examples`, `guided_exercises`, `exercises`, `exam_questions`, `challenge_questions` (321+180+311+173+65 = 1.050 piezas) incluyen `solution`/`full_solution`. La verificación numérica automática (recálculo de cadenas `a = b·c` con notación decimal española) es la Fase 2 de este piloto; sustituye al archivo `equality_mismatches_candidates.csv` (87 candidatos para esta asignatura), que se ha inspeccionado y contiene mayoritariamente falsos positivos del parser original (p.ej. confunde la letra "E" o "e" con el número de Euler, o no reconoce "sen"/`\dfrac` correctamente) — se reemplaza por un verificador propio más fiel a la notación real del curso.
- **Feedback**: `common_errors`/`common_mistakes`/`misconceptions` presentes y no genéricos ("Incorrecto") en el muestreo realizado; validación sistemática en Fase 7.

## 9. Duración declarada

`estimated_length` por lección oscila 1–2,5 h (la mayoría 1,5–2 h). Bajo el modelo objetivo (Core 15–25 min, Standard 25–40 min, Advanced +15–25 min) casi ninguna lección actual cabe en una sola sesión Core; esto es esperado porque el corpus actual mezcla CORE+STANDARD+ADVANCED en una sola lección lineal — exactamente lo que la arquitectura de rutas (Fase 3) y la atomización (Fase 4) deben resolver, no evidencia de otro problema adicional.

## 10. Problemas de secuencia

La secuencia de unidades ya declarada en `02_auditoria_reestructuracion/cursos/01_SELECTIVIDAD_FISICA.md` §3 (gravitatorio → MAS → ondas → electromagnetismo → óptica → relatividad → cuántica → nuclear) es la que usa el curso actual en `catalog.json.units[]`; no se detectan saltos de prerrequisito graves dentro de cada unidad (cada lección declara prerequisites coherentes con la anterior). Falta: (a) módulo 00 Foundations explícito, (b) módulo 09 PAU integrada, (c) checkpoints explícitos entre grupos de lecciones — los tres se añaden en Fases 5–6.

## 11. Conclusión de la Fase 0

El curso **no** necesita reescritura masiva de contenido: necesita (1) cerrar 22 correcciones científicas puntuales con propagación completa, (2) migrar a un schema canónico con `epistemic_type`/rutas sin romper el frontend actual, (3) atomizar 6 lecciones, (4) añadir Foundations/checkpoints/Exam Mode, (5) QA automatizado real (estructura + numérico) en sustitución de los candidatos ruidosos existentes. Se procede a Fase 1 sobre `pilot/selectividad_fisica_v2/`.
