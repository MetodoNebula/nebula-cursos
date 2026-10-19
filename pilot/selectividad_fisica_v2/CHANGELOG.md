# CHANGELOG.md — selectividad_fisica (piloto v2)

Resumen cronológico de las 7 commits de este piloto (ver `git log` en la
rama `main` para el detalle completo de cada una).

## Fase 0 — Inventario
`fix/selectividad_fisica/fase0-inventario`
- `original/selectividad_fisica/` congelado (copia exacta, nunca editada).
- `AUDIT_BEFORE.md` generado con inventario real (76 lecciones, 5888
  piezas, metodología de recuento documentada).

## Fase 1 — Backlog obligatorio (semantic_change_ledger)
`fix/selectividad_fisica/p0-p1-p2`
- **P0** resueltos: inducción presentada como dependiente de movimiento
  relativo (electromagnetismo, L12); criterio dimensional usado como
  condición suficiente para pares conjugados (cuántica, L06).
- **P1** resueltos: rozamiento "siempre negativo" (campo_gravitatorio);
  potencial magnético negado globalmente (electromagnetismo, L06);
  polarización de dieléctricos en sentido contrario a E
  (electromagnetismo); energía de enlace Fe-56 como máximo exacto en vez
  de región Fe-Ni (nuclear, L02).
- **P2** resueltos: solenoide "uniforme en todo el interior"
  (electromagnetismo); isocronía del MAS sin distinguir de oscilación
  general (mas, L01); g máxima en superficie sin etiquetar modelo de
  Tierra homogénea (campo_gravitatorio, L04); índice de refracción n≥1
  sin acotar a medios ordinarios (óptica, L02); energía de la onda
  estacionaria con "el nodo no puede hacer trabajo" como razón principal
  en vez de superposición (ondas, L11); de Broglie λ=h/mv en vez de h/p y
  umbral de producción de pares sin marcar MODEL/APPROX
  (cuántica/relatividad).
- 9 items verificados como ya resueltos en el contenido actual (herencia
  de una revisión previa no registrada en el propio ledger): tercera ley
  de Kepler, introducción a relatividad general, equivalencia local,
  tiempo propio, decibelios, intensidad-amplitud, nodos/antinodos en
  tubos, idealizaciones de óptica geométrica, estabilidad nuclear
  Z>83/Pb-208, caída libre.

## Fase 2+3 — QA numérico y migración a schema_v2
`qa+refactor/selectividad_fisica/...`
- Verificador numérico propio (`numeric_qa.py`): 0 discrepancias reales.
- `schema_v2` añadido de forma aditiva a las 76 lecciones (luego 88),
  sin tocar ningún campo plano que usa `index.html`.

## Fase 4 — Atomización
`refactor/selectividad_fisica/atomic-lessons`
- Las 6 lecciones del backlog oficial (`structural_issues.csv`) divididas
  en 12, conservando el 100% de sus piezas (verificado automáticamente).

## Fase 5 — Fundamentos y grafo de conocimiento
`feat/selectividad_fisica/foundations-knowledge-graph`
- 6 microlecciones de remediación just-in-time.
- `KNOWLEDGE_GRAPH.json`: 88 nodos, 156 aristas.

## Fase 6 — Checkpoints, diagnóstico, Exam Mode
`feat/selectividad_fisica/checkpoints-diagnostico-exam-mode`
- 31 checkpoints, diagnóstico de 22 items/14 ejes, módulo "PAU integrada".

## Fase 7 — QA estructural y corrección de una regresión propia
`fix+qa/selectividad_fisica/...`
- `structural_qa.py` detectó 72 `objective_ids` rotos introducidos por la
  propia atomización de la Fase 4 (al repartir `objectives[]` entre las
  dos partes de cada lección dividida). Corregido dando a ambas partes la
  unión completa de los objetivos originales. 0 roturas tras el fix.

## Fase 8 — Release
`feat/selectividad_fisica/release`
- `catalog.json` y `bundles/` regenerados para selectividad_fisica (76→88
  lecciones, 5888→6047 piezas), sin tocar ningún otro curso. Verificado
  con servidor local (HTTP 200 + JSON válido en `index.html`,
  `catalog.json` y los bundles).

## Fase 9 — Deliverables finales (este commit)
- `AUDIT_AFTER.md`, `PILOT_COMPARISON.md`, `CHANGELOG.md` (este fichero).

## Auditoría v2 — 2026-10-19

Auditoría independiente de 6 fases sobre el curso completo (88 lecciones,
9 bundles, 3 ficheros de evaluación, 241 SVGs).

### Correcciones aplicadas

- **P0 — Nuclear Z>83→Z>82**: 28 instancias de `Z>83` reemplazadas por
  `Z>82` en todo el bundle `selectividad_fisica__nuclear.json` (10
  lecciones). El Bi-209 (Z=83) es alfa-inestable; el último elemento
  verdaderamente estable es Pb (Z=82).
- **P1 — Cuántica fracciones ambiguas**: 2 expresiones con barra `/` en
  `exercises[0].full_solution` de L02 (efecto fotoeléctrico) sustituidas
  por `\dfrac{}{}` para eliminar ambigüedad de precedencia.
- **P1 — Relatividad conservación del momento**: Añadida nota en
  `flashcards[9].back` de L05 (E₀=mc²) aclarando que un fotón aislado
  no puede crear un par e⁺e⁻ sin un tercer cuerpo que absorba el retroceso.

### Verificaciones completadas (0 nuevos P0/P1)

- Escaneo profundo de física en las 88 lecciones: 0 errores.
- scope + 0 MEZCLA: 731 bloques verificados, 0 violaciones.
- schema_v2: 88 canonical IDs únicos, rutas a nivel de bloque, content_version.
- Fundamentos: 6 micro-lecciones auditadas, sin errores.
- Evaluación: diagnostic (22 items/14 ejes), checkpoints (31),
  exam_mode (173+10+2+2) — 0 referencias rotas.
- SVGs: 241 válidos, 87/88 cobertura.
- Gates: 100% PASS.

### Hallazgos P2 (5, no bloqueantes)

Documentados en `AUDIT_REPORT_v2.md`.
