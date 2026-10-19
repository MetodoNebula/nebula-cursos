# SCHEMA_MIGRATION.md — selectividad_fisica (piloto v2)

## Decisión arquitectónica: migración aditiva, no sustitutiva

`index.html` (el visor real, 146 KB de JS) lee cada lección accediendo
directamente a nombres de campo planos: `theory_blocks`, `objectives`,
`exercises`, `mcq`, `summary`, etc. No existe una capa de parseo intermedia:
el JS indexa el objeto JSON tal cual llega del bundle.

Por tanto, migrar al `target_lesson_schema.example.json` **sustituyendo**
esos campos habría roto el frontend de producción sin reescribirlo. Se optó
por la alternativa explícitamente permitida por el encargo
("Mantén compatibilidad con el frontend cuando sea razonable. Si el schema
cambia, adapta parser o introduce compatibilidad"):

> Se añade una clave nueva, `schema_v2`, a cada lección, con la forma de
> `target_lesson_schema.example.json`. **Ningún campo plano existente se
> modifica de nombre, de tipo ni se elimina.** `schema_v2` convive con ellos.

Verificación: `grep -c "schema_v2" index.html` → 0. El parser actual ignora
la clave nueva igual que ignora cualquier campo que no busque explícitamente,
así que el frontend sigue funcionando sin cambios (ver `FRONTEND_CHANGES.md`).

## Qué contiene schema_v2 y de dónde sale cada campo

El generador es `scripts/pilot_fisica/build_schema_v2.py`, ejecutado una vez
sobre las 76 lecciones de las 8 unidades. Reglas de derivación:

- `canonical_lesson_id`: `"SELFIS::<unidad>::<id>"` — el campo `id` (p. ej.
  `"L01"`) ya era único **dentro** de cada unidad (verificado en
  `AUDIT_BEFORE.md`); con el prefijo de unidad queda único en todo el curso.
- `learning_design.estimated_*_minutes`: a partir de `estimated_length`
  ("1,5 h" → 90 min), con CORE = 60 %, STANDARD = 100 %, ADVANCED = 150 % del
  tiempo declarado. Es una heurística declarada, no una medición.
- `learning_design.recommended_routes`: los cuatro arrays
  (`from_zero/standard/excellence/quick_review`) se construyen agrupando los
  IDs que **ya existían** en cada contenedor (`theory_blocks`,
  `worked_examples`, `guided_exercises`, `exercises`, `mcq`,
  `diagnostic_items`, `exam_questions`, `challenge_questions`), usando los
  campos `scope` (`CORE`/`ADVANCED`) y `difficulty` (1-5) que la mayoría de
  piezas ya llevaba de una revisión previa del curso:
  - `from_zero`: piezas CORE, no avanzadas, dificultad ≤ 2, + diagnóstico.
  - `standard`: piezas CORE, dificultad ≤ 3.
  - `excellence`: todas las piezas, CORE y ADVANCED, toda dificultad,
    `exam_questions` y `challenge_questions` incluidas.
  - `quick_review`: bloques de tipo `connection`/`caveat` (las síntesis y
    advertencias, no la explicación completa) + `exam_questions` +
    `challenge_questions` + piezas de dificultad ≥ 4. Es la ruta de "solo
    repaso": sin reexplicación del concepto, directa a práctica de examen.
- `objectives`: copia de `objectives[]`; `required_for_mastery` = `true`
  salvo que el objetivo tenga `scope == "ADVANCED"`.
- `knowledge_model.core_claims` / `formulae`: uno por cada
  `summary.key_points[]` / `summary.formulas[]`. `epistemic_type` por defecto
  `"MODEL"` (criterio conservador: en Física de Selectividad casi toda
  fórmula y afirmación lleva condiciones de validez implícitas). Para las 22
  afirmaciones del `semantic_change_ledger` auditadas una a una en la Fase 1,
  se asigna el `epistemic_type` exacto decidido entonces (ver
  `EPISTEMIC_OVERRIDES` en el script): p. ej. de Broglie λ=h/p → `EXACT`;
  B=μnI del solenoide largo → `APPROXIMATION`; criterio dimensional →
  `HEURISTIC`; rozamiento siempre negativo → `SPECIAL_CASE`.
  **Clasificación pendiente declarada:** una taxonomía claim-a-claim
  exhaustiva de las ~2 000 afirmaciones del curso que no pasaron por el
  backlog auditado queda fuera del alcance de este piloto por volumen; se
  documenta aquí como trabajo de continuación, con el criterio por defecto
  "MODEL" actuando como salvaguarda (nunca se infla una aproximación a ley
  universal por omisión).
- `knowledge_model.common_mistakes`: copia de `misconceptions[]`.
- `knowledge_model.exam_conventions`: copia de `exam_notes[]`.
- `presentation.*`: los `theory_blocks` se reparten por `type`/`scope`
  (`intuition` → `intuition_blocks`; `ADVANCED` → `advanced_blocks`;
  `connection`/`caveat` → `standard_blocks`; resto CORE → `core_blocks`).
  `worked_examples` → `worked_examples`; **`guided_exercises` →
  `faded_examples`** (ya llevan `hints` y resolución parcial escalonada, que
  es exactamente la definición de faded example pedida en el encargo);
  `diagnostic_items` → `micro_checks`.
- `practice.items`: unión de `exercises` + `guided_exercises` +
  `challenge_questions`, con `route_visibility` recalculada por
  `difficulty` (L1-L2→todas las rutas; L3→standard+; L4-L5→excellence +
  quick_review). El campo `difficulty` (1-5) que ya traían las piezas
  implementa directamente la taxonomía L1-L5 pedida en el encargo:
  reconocimiento/aplicación directa/combinación/nivel Selectividad/
  transferencia.
- `practice.checkpoint_item_ids`: se deja vacío a nivel de lección a
  propósito; los checkpoints son una construcción **por unidad** (varias
  lecciones), implementada en Fase 6 (`CHECKPOINTS.md`/`unit_checkpoints.json`),
  no un campo derivable lección a lección.
- `qa.validated_semantics` = `true` (Fase 1 completada y commiteada).
  `qa.validated_numerics` = `true` (Fase 2: verificador numérico propio,
  0 discrepancias reales tras descartar falsos positivos — ver
  `QA_REPORT.md`). `qa.validated_render` queda en `false` hasta la
  comprobación de Fase 8 (arranque del servidor local, ver
  `FRONTEND_CHANGES.md`); se actualizará entonces.

## Validación de la migración

`scripts/pilot_fisica/validate_schema_v2.py`:
- 76/76 lecciones con `schema_v2`.
- 76 `canonical_lesson_id` únicos, 0 duplicados.
- JSON válido en los 8 bundles tras la migración.
- Todas las rutas (`from_zero/standard/excellence/quick_review`) son listas
  bien formadas en las 76 lecciones.

## Qué NO cambia

Ningún campo plano (`id`, `title`, `objectives`, `theory_blocks`,
`exercises`, `mcq`, `summary`, etc.) se ha renombrado, movido ni eliminado.
`original/selectividad_fisica/` permanece intacto como antes de esta fase.
