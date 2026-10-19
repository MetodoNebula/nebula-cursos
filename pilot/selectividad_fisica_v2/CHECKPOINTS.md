# CHECKPOINTS.md — selectividad_fisica (piloto v2)

## Qué se construyó (Fase 6)

Tres ficheros nuevos, puramente aditivos y por **referencia** a ids de
piezas que ya existían (ningún contenido se duplica):

- `unit_checkpoints.json`: 31 checkpoints, agrupando las lecciones de cada
  una de las 8 unidades de contenido en bloques de hasta 3 lecciones
  consecutivas. Cada checkpoint referencia los MCQ de dificultad ≤3 y el
  ejercicio más sencillo de cada lección del bloque. 0 checkpoints vacíos.
- `diagnostic.json`: diagnóstico inicial de 22 items (dentro del rango
  12-25 pedido) sobre 14 ejes de habilidad: los 6 microtemas de Fundamentos
  (vectores, trigonometría, despeje algebraico, notación científica/SI,
  lectura de gráficas, conservación de la energía) y las 8 unidades de
  contenido. Cada eje usa `diagnostic_items` ya existentes en las
  lecciones correspondientes.
- `exam_mode.json`: el módulo "PAU integrada" —
  - `topic_questions`: las `exam_questions` de cada unidad, agrupadas por
    tema (173 preguntas en total, repartidas en las 8 unidades).
  - `mixed_questions`: una muestra de 10 preguntas de varias unidades.
  - `timed_questions`: las 173 preguntas con un tiempo estimado (2 min por
    punto de `marks`, convención estándar de la PAU).
  - `partial_mock_exams`: dos parciales por bloque temático (mecánica:
    campo gravitatorio+MAS+ondas; física moderna: electromagnetismo+
    óptica+relatividad+cuántica+nuclear).
  - `full_mock_exams`: dos exámenes completos muestreando las 8 unidades,
    como la estructura real de la prueba.
  - `scaffolding_policy`: en Exam Mode no se muestran `hints` ni
    `full_solution` hasta que el alumno entrega respuesta (reduce el
    andamiaje, como pide el encargo para esta capa).

## Validación de integridad referencial

`scripts/pilot_fisica/validate_checkpoints_exammode.py` comprueba que cada
referencia (`ref_lesson` + `item_id`) de los tres ficheros apunta a una
lección y una pieza que existen de verdad en los bundles del piloto.

**Resultado: 0 referencias rotas** en los 31 checkpoints + 22 items de
diagnóstico + 173+10+2+2 referencias de Exam Mode.

## Umbral needs_support / ready / mastered

Declarado explícitamente (no inferido de datos de alumnos reales, que no
existen en este piloto): `<60%` correcto → `needs_support`; `60-85%` →
`ready`; `>85%` → `mastered`. Queda documentado aquí para que quien
implemente la UI del checkpoint (ver `FRONTEND_CHANGES.md`) use el mismo
criterio.

## Qué falta para que esto sea usable por un alumno

Igual que las 4 rutas pedagógicas, estos tres ficheros son **datos**
correctos y validados; la interfaz actual (`index.html`) no tiene pantallas
para el diagnóstico, los checkpoints ni el Exam Mode. Ver
`FRONTEND_CHANGES.md` para el detalle de qué vistas de UI harían falta.
