# CHANGELOG.md — selectividad_quimica (piloto v2) — 2026-10-19

## Fase 1 — Backlog del semantic_change_ledger (17/17)
- **P0** U09/04: redondeo inconsistente (27,6 vs 27,56 → 2,44). Corregido conservando cifras de guarda + nota de redondeo.
- **P1** U06: H₂SO₄ (2 H⁺ marcado como convención PAU/aproximación con Ka2 en el summary); neutralización (Brønsted como definición general + contraejemplo NH₃+HCl sin agua); equivalencia (equivalentes en vez de «moles ácido = moles base» en L14).
- **P1** U04: estado estándar redefinido (1 bar IUPAC moderno; 1 atm = EXAM_CONVENTION; tablas a 298,15 K) en teoría, keyword, flashcard, objetivo, summary y MCQ.
- **P1** U05: derivación K=k₊/k₋ acotada a etapa elemental (ya lo estaba; reforzado el caveat para reacciones globales).
- **P1** U08: cis/trans — añadida distinción E/Z (dobles enlaces, CIP) frente a cis/trans (ciclos).
- **P2** U04: Qp=ΔH, ΔH=ΔU+Δn_gRT (gas ideal, sistema cerrado, trabajo pV), T=ΔH/ΔS (aproximación con ΔH,ΔS constantes).
- **P2** U05: unidades de Kc — nota Advanced sobre actividades y K termodinámica adimensional.
- **P2** U08: enantiómeros («en entorno aquiral»), halogenación («único» = producto constitucional; estereoisómeros posibles), CCl₄ (nota de seguridad/histórica).
- **P2** U03: enlace de hidrógeno reformulado como tendencia en especies comparables (no superlativo universal).
- **P2** U02: orbital = función de onda (|ψ|² densidad de probabilidad); Madelung marcada MODEL/HEURÍSTICO con más excepciones que Cr/Cu.

## Fase 2 — scope + esencial-primero
- Añadido `scope` a los 660 bloques (química no lo tenía): {'CORE': 650, 'ADVANCED': 10}. 5 lecciones reordenadas (ampliación al final con separador). 0 lecciones con avanzado antes de lo esencial.

## Fase 3 — schema_v2 (canonical SELQUI) en las 133 lecciones, rutas DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW.

## Fase 4 — Módulo 00 Foundations (6 microlecciones): formulación, mol, proporcionalidad/factores, notación científica y cifras, logaritmos para pH, lectura de gráficas. Con 3 diagramas nuevos.

## Fase 5 — Evaluación: 45 checkpoints, diagnóstico 22 ítems/14 ejes, Exam Mode (220 preguntas por tema + mixtas + cronometradas + 2 parciales + 2 completos).

## Fase 6 — Diagramas: 6 nuevos (perfil energético, mapa de Gibbs, curva de valoración, reactivo limitante, pila galvánica, equilibrio dinámico) en lecciones de cálculo sin figura. Total 103.

## Auditoría v2 (2026-10-19) — Validación programática + correcciones

### ALTA (P0) — 3 correcciones
- **U07-L03** `03_Ajuste_por_ion-electrón_en_medio_ácido`: añadido `full_solution` al ejercicio guiado 1.
- **U08-L10** `10_Isomería_de_posición`: añadido `full_solution` al ejercicio guiado 2.
- **U08-L11** `11_Isomería_de_función`: añadido `full_solution` al ejercicio guiado 1.

### MEDIA (P1) — 81 correcciones
- **U07 L01–L14**: añadidos 28 campos `id` (formato EX-Q07-NN-GN) a ejercicios guiados sin él.
- **U00–U08**: añadidos 53 hints progresivos (2º hint) a ejercicios guiados con solo 1 hint.

### VERIFICADO (sin cambio necesario)
- U08-L14 "producto único" → matiz estereoquímico ya presente en pilot v2.
- LaTeX delimiters (U02-L07, U05-L02, U07-L14, U08-L21) → sin problemas detectados.

### Resultado post-auditoría
- **0 errores** en los 7 gates de validación.
- **259/259 ejercicios** con ≥2 hints, full_solution e id.
- 104 SVGs XML válido, 0 MEZCLA, 133 canonical IDs únicos.
