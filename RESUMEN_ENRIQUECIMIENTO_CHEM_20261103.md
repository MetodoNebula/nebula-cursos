# Resumen de enriquecimiento — GCSE Química (exercises[])

**Fecha:** 2026-11-03 02:29  ·  **Backup:** `bundles/_backup_chem_enrich_20261103_014749/` (14 bundles, intacto)

## Ejercicios añadidos por unidad (autoría propia, provenance SOURCE_DERIVED, type STANDARD)

| Unidad | Ejerc. totales | Nuevos | d4 | d5 | Figuras |
|---|---:|---:|---:|---:|---:|
| U00_Foundations | 42 | 6 | 6 | 0 | 0 |
| U01_States_of_Matter | 44 | 5 | 5 | 0 | 0 |
| U02_Atoms_Elements_and_Bonding | 56 | 6 | 6 | 0 | 0 |
| U03_Formulas_and_Amounts | 60 | 13 | 10 | 3 | 0 |
| U04_Electrochemistry | 47 | 8 | 7 | 1 | 0 |
| U05_Chemical_Energetics | 35 | 9 | 7 | 2 | 1 |
| U06_Chemical_Reactions | 37 | 6 | 6 | 0 | 0 |
| U07_Acids_Bases_and_Salts | 47 | 9 | 6 | 3 | 0 |
| U08_The_Periodic_Table | 37 | 5 | 5 | 0 | 0 |
| U09_Metals | 46 | 6 | 5 | 1 | 0 |
| U10_Environmental_Chemistry | 50 | 5 | 4 | 1 | 0 |
| U11_Organic_Chemistry | 65 | 7 | 5 | 2 | 0 |
| U12_Experimental_Methods_and_Analysis | 52 | 8 | 5 | 3 | 0 |
| U13_Revision_and_Exam_Practice | 7 | 4 | 2 | 2 | 0 |
| **TOTAL** | **625** | **97** | **79** | **18** | **1** |

## Resultado
- **97 ejercicios nuevos** de dificultad alta (79× d4, 18× d5), todos con solución impecable paso a paso, `hints`, `answer`, `full_solution` y `common_errors`.
- **Cada valor numérico validado con Python** (masas molares, moles, g/dm³, mol/dm³, rendimiento %, pureza, volúmenes de gas 24 dm³/mol, estequiometría, reactivo limitante, ΔH de enlaces, electrólisis, Faraday cualitativo, fórmula empírica/molecular, agua de cristalización) antes de inyectar; `assert` + `math.isclose`.
- **Distribución de dificultad final:** d1=132, d2=345, d3=50, **d4=80, d5=18** → difícil(≥4) = **98 (15,7%)**, frente a 1 (0,2%) inicial.
- **Soluciones auditadas:** 12 soluciones existentes 'finas' (sólo verificación 'Check:') reescritas a desarrollo autocontenido paso a paso; 3 ejercicios de U05 con `difficulty` ausente corregidos. Sin `$` desbalanceado, sin soluciones vacías, sin remisiones tipo 'as in the previous'.
- **1 figura nueva validada** (perfil de energía de reacción exotérmica, U05) construida con el builder TikZ→SVG del proyecto, canónica (`data-nebula-svg`), e inspeccionada a tamaño real: sin solape texto-texto ni texto-línea.
- **Integridad:** los 14 bundles cargan como JSON; ids únicos; `objective_ids` válidos por lección; `concept_ids` no se usa en el curso (no inventado). `catalog.json` regenerado con el script del proyecto (9 cursos, química = 625 ejercicios).

## Observación (fuera de alcance, no modificado)
- Varios ejercicios **originales** usan `type` `TRANSFER`/`CHALLENGE` y algunos SVG originales usan un marcador distinto a `data-nebula-svg`. No se han tocado (son contenido previo); los ejercicios nuevos usan siempre `type:"STANDARD"` como se pidió. Nota: el `catalog.json` de la raíz estaba roto (resto de una sesión previa, formato de un solo curso) y el script lo ha reparado a la estructura completa de 9 cursos.

No se ha modificado nada fuera de `exercises[]` (salvo regenerar `catalog.json` y añadir el reporte).