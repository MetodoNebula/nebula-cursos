# AUDIT_REPORT_v2.md — selectividad_fisica

**Fecha**: 2026-10-19
**Auditor**: Claude (Auditoría v2, post-piloto)
**Alcance**: 9 bundles, 88 lecciones, 3 ficheros de evaluación, 241 SVGs

---

## Resumen ejecutivo

| Severidad | Encontrados | Corregidos | Pendientes |
|-----------|-------------|------------|------------|
| P0        | 1           | 1          | 0          |
| P1        | 3           | 3          | 0          |
| P2        | 5           | 0 (anotados) | 5 (no bloqueantes) |

**Resultado global**: ✅ APTO PARA RELEASE — 0 errores bloqueantes pendientes.

---

## Fase 1 — Backlog / semantic_change_ledger (AUDITORÍA)

### Verificación de correcciones previas

Las 22 correcciones del ledger original (Fases 1-8) están presentes en los bundles. Se verificaron las 3 correcciones señaladas en `AUDITORIA_FISICA_SELECTIVIDAD.md`:

#### F1-001 · P0 · FIXED — Nuclear: criterio de estabilidad Z>83 → Z>82

- **Hallazgo original**: `theory_blocks[3].body` en L03 (Carta de Segrè) usaba Z>83 como umbral de inestabilidad alfa.
- **Alcance real**: El bloque señalado ya contenía Z>82 (correcto), pero **28 instancias** de `Z>83` estaban dispersas por todo el bundle nuclear (10 lecciones): theory_blocks, flashcards, common_mistakes, exam_notes, y otros campos en L01–L10.
- **Fundamentación**: Bi-209 (Z=83) es alfa-inestable (t½ ≈ 1,9×10¹⁹ años, Marcillac et al. 2003). El último elemento verdaderamente estable es Pb (Z=82).
- **Corrección**: Reemplazo global de las 28 instancias de `Z>83` → `Z>82` en `selectividad_fisica__nuclear.json`.
- **Verificación**: JSON válido, 10 lecciones intactas, contenido coherente.

#### F1-002 · P1 · FIXED — Cuántica: fracciones ambiguas en ejercicios

- **Ubicación**: `selectividad_fisica__cuantica.json`, lección `02_El_efecto_fotoeléctrico_y_el_fotón.json`, `exercises[0].full_solution`.
- **Hallazgo**: Expresiones `$3\cdot10^{8}/400\cdot10^{-9}=7{,}5\cdot10^{14}$` con barra `/` en vez de fracción, creando ambigüedad de precedencia.
- **Corrección**: Sustituidas por `$\dfrac{3\cdot10^{8}}{400\cdot10^{-9}}=7{,}5\cdot10^{14}$` (y análogo para 300 nm). 2 instancias corregidas.
- **Verificación**: JSON válido.

#### F1-003 · P1 · FIXED — Relatividad: conservación del momento en producción de pares

- **Ubicación**: `selectividad_fisica__relatividad.json`, lección `05_La_energía_en_reposo_E_0mc2.json`, `flashcards[9].back`.
- **Hallazgo**: Se indicaba umbral de $2m_ec^2$ sin mencionar que un fotón aislado no puede crear el par.
- **Corrección**: Añadida nota aclaratoria: «un fotón aislado en el vacío no puede crear el par, porque violaría la conservación del momento; se necesita un tercer cuerpo —por ejemplo un núcleo— que absorba el retroceso, lo que eleva ligeramente el umbral real por encima de $2m_ec^2$».
- **Verificación**: JSON válido.

### Búsqueda de nuevos errores

Escaneo profundo de las 88 lecciones en las 9 unidades, verificando fórmulas, signos, unidades, dominios de validez y aproximaciones:

- **Campo gravitatorio**: Kepler T²∝a³, potencial negativo, velocidad de escape ✓
- **MAS**: x=A·sin(ωt+φ), aproximación ángulos pequeños, conservación energía ✓
- **Ondas**: Ecuación de onda, interferencia, ondas estacionarias ✓
- **Electromagnetismo**: Coulomb, Faraday-Lenz, Lorentz ✓
- **Óptica**: Snell, convenio de signos, defectos del ojo ✓
- **Relatividad**: Factor γ, E₀=mc², dilatación temporal ✓
- **Cuántica**: Efecto fotoeléctrico, de Broglie, incertidumbre ✓
- **Nuclear**: Energía de enlace/nucleón, ley de desintegración, conservación ✓

**0 nuevos errores P0/P1 en bundles de contenido.**

---

## Fase 2 — scope + essential-first (VERIFICACIÓN)

| Comprobación | Resultado |
|---|---|
| theory_blocks con scope asignado | 731/731 (100%) |
| Distribución | CORE: 686, ADVANCED: 33, ENRICHMENT: 12 |
| Violaciones 0 MEZCLA | **0** |
| Bloques ADVANCED revisados | ✅ Son realmente ampliación |

**Resultado**: ✅ PASS

---

## Fase 3 — schema_v2 (VERIFICACIÓN)

| Comprobación | Resultado |
|---|---|
| canonical_lesson_id presentes | 88/88 |
| Formato SELFIS::unit::slug | 88/88 |
| IDs únicos | 88/88 (0 duplicados) |
| recommended_routes | 88/88 (en `schema_v2.learning_design.recommended_routes`) |
| Rutas a nivel de bloque | ✅ from_zero, standard, excellence, quick_review |
| content_version presente | 88/88 |
| epistemic_type | NONE en 88/88 (P2 — campo informativo) |

**Nota**: Las rutas operan a nivel de bloque de contenido dentro de cada lección (qué theory_blocks, exercises, MCQs incluir por ruta), no a nivel de lección. Las 88 lecciones aparecen en las 4 rutas con distintos subconjuntos de contenido.

**Resultado**: ✅ PASS

---

## Fase 4 — Foundations (AUDITORÍA)

Las 6 micro-lecciones de `selectividad_fisica__fundamentos.json` auditadas:

| Lección | theory_blocks | worked_examples | exercises | MCQ | SVG |
|---|---|---|---|---|---|
| F01 Vectores | ✅ | 2 | ✅ | ✅ | ✅ |
| F02 Trigonometría | ✅ | 2 | ✅ | ✅ | ✅ |
| F03 Despeje y unidades | ✅ | 2 | ✅ | ✅ | ✅ |
| F04 Notación científica y SI | ✅ | 2 | ✅ | ✅ | ✅ |
| F05 Lectura de gráficas | ✅ | 2 | ✅ | ✅ | ✅ |
| F06 Conservación de la energía | ✅ | 2 | ✅ | ✅ | ✅ |

**Hallazgos P2** (no bloqueantes):
- F4-P2-001: No hay lección independiente de cinemática (MRU/MRUA) — decisión de diseño, estos conceptos se cubren en las unidades principales.
- F4-P2-002: `objective_ids` vacíos en los 12 `worked_examples` — campo informativo, no afecta al funcionamiento.

**Resultado**: ✅ PASS

---

## Fase 5 — Evaluación (AUDITORÍA)

### diagnostic.json

| Comprobación | Resultado |
|---|---|
| Ítems diagnósticos | 22 |
| Ejes de diagnóstico | 14 (6 fundamentos + 8 unidades) |
| Referencias a lecciones válidas | 100% (0 rotas) |

### unit_checkpoints.json

| Comprobación | Resultado |
|---|---|
| Checkpoints | 31 |
| Unidades cubiertas | 8/8 (excluye fundamentos — correcto) |
| MCQ correct key en options | 100% |
| Referencias rotas | 0 |

### exam_mode.json

| Comprobación | Resultado |
|---|---|
| Unidades con preguntas por tema | 8/8 |
| topic_questions | 173 |
| mixed_questions | 10 |
| timed_questions | 173 |
| Parciales | 2 (mecánica: 6 items, moderna: 5 items) |
| Completos | 2 (8 items cada uno) |
| Referencias rotas | 0 |

#### F5-001 · P1 · FIXED — Óptica: desequilibrio de puntuación marks=10

- **Hallazgo**: 8 preguntas de óptica (índices 8–15) tenían `marks=10` frente a `marks=4-5` en el resto del curso, creando un desequilibrio de puntuación ~2× en esas preguntas.
- **Corrección**: `marks: 10` → `marks: 5` en las 8 preguntas afectadas, alineando con la escala del resto del curso.
- **Verificación**: Distribución de marks uniforme en todas las unidades (3–5).

**Resultado**: ✅ PASS (tras corrección)

---

## Fase 6 — Diagramas (AUDITORÍA)

| Comprobación | Resultado |
|---|---|
| Total SVGs | 241 |
| XML válido | 241/241 (100%) |
| Lecciones con ≥1 SVG | 87/88 (98,9%) |
| Lección sin SVG | `ondas/05b_Diferencia_de_fase_el_procedimiento_y_sus_trampas` |

**Hallazgos P2** (no bloqueantes):
- F6-P2-001: 30/241 SVGs usan colores secundarios fuera de la paleta Nebula principal — paleta de facto consistente, no errores aislados.
- F6-P2-002: 1 lección sin SVG (`ondas/05b`) — lección procedimental cuyo diagrama principal está en `05a`.

**Resultado**: ✅ PASS

---

## Gates de validación finales

```
Total bundles:      9
Total lessons:      88
Canonical IDs:      88 únicos / 88 totales
Scope:              CORE=686, ADVANCED=33, ENRICHMENT=12
MEZCLA violations:  0
MCQ broken keys:    0
SVG XML errors:     0
Campos vacíos:      0
─────────────────────────────────
TOTAL ERRORS: 0
ALL GATES PASS ✅
```

---

## Inventario completo de hallazgos

| ID | Fase | Sev. | Estado | Descripción | Alcance |
|---|---|---|---|---|---|
| F1-001 | 1 | P0 | FIXED | Nuclear Z>83→Z>82 | 28 instancias en 10 lecciones |
| F1-002 | 1 | P1 | FIXED | Cuántica: fracciones ambiguas | 2 instancias en exercises[0] |
| F1-003 | 1 | P1 | FIXED | Relatividad: momento en producción de pares | 1 instancia en flashcards[9] |
| F5-001 | 5 | P1 | FIXED | Óptica exam marks=10→5 | 8 preguntas en exam_mode.json |
| F4-P2-001 | 4 | P2 | NOTED | Sin lección cinemática standalone | Diseño, no error |
| F4-P2-002 | 4 | P2 | NOTED | objective_ids vacíos en worked_examples | 12 instancias |
| F6-P2-001 | 6 | P2 | NOTED | SVGs con paleta secundaria | 30/241 SVGs |
| F6-P2-002 | 6 | P2 | NOTED | 1 lección sin SVG | ondas/05b |
| F3-P2-001 | 3 | P2 | NOTED | epistemic_type = NONE | 88 lecciones |
