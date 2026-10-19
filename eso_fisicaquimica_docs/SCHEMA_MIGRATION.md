# Schema Migration — eso_fisicaquimica

## Fecha: 2026-10-19

## Resumen

- **Prefijo canónico:** `ESOFYQ`
- **Formato:** `ESOFYQ::<unit_id>::<lesson_slug>`
- **Total canonical IDs:** 19
- **Duplicados:** 0

## IDs canónicos

| Unidad | Lección | canonical_lesson_id | Ruta DESDE_CERO | Ruta EXCELLENCE | Ruta FAST_REVIEW |
|---|---|---|---|---|---|
| U-ESO-01 | Pregunta-hipótesis-evidencia | `ESOFYQ::U-ESO-01::01_metodo_cientifico` | ✓ | — | ✓ |
| U-ESO-01 | El SI y las conversiones de unidades | `ESOFYQ::U-ESO-01::02_si_conversiones` | ✓ | — | — |
| U-ESO-01 | Incertidumbre y resolución | `ESOFYQ::U-ESO-01::03_incertidumbre` | ✓ | ✓ | — |
| U-ESO-01 | Tablas y gráficas | `ESOFYQ::U-ESO-01::04_tablas_graficas` | ✓ | ✓ | — |
| U-ESO-02 | Masa-volumen-densidad | `ESOFYQ::U-ESO-02::01_masa_volumen_densidad` | ✓ | — | ✓ |
| U-ESO-02 | Modelo de partículas | `ESOFYQ::U-ESO-02::02_modelo_particulas` | ✓ | — | — |
| U-ESO-02 | Cambios de estado | `ESOFYQ::U-ESO-02::03_cambios_estado` | ✓ | — | — |
| U-ESO-02 | Temperatura y equilibrio | `ESOFYQ::U-ESO-02::04_temperatura_equilibrio` | ✓ | — | — |
| U-ESO-02 | Curvas de calentamiento | `ESOFYQ::U-ESO-02::05_curvas_calentamiento` | ✓ | ✓ | — |
| U-ESO-03 | Sustancia frente a mezcla | `ESOFYQ::U-ESO-03::01_sustancia_mezcla` | ✓ | — | ✓ |
| U-ESO-03 | Separación por propiedades | `ESOFYQ::U-ESO-03::02_separacion_propiedades` | ✓ | — | — |
| U-ESO-03 | Soluto y disolvente | `ESOFYQ::U-ESO-03::03_soluto_disolvente` | ✓ | — | — |
| U-ESO-03 | Concentración básica | `ESOFYQ::U-ESO-03::04_concentracion_basica` | ✓ | — | — |
| U-ESO-03 | Diseño de separación | `ESOFYQ::U-ESO-03::05_diseno_separacion` | ✓ | ✓ | — |
| U-ESO-04 | Partículas subatómicas | `ESOFYQ::U-ESO-04::01_particulas_subatomicas` | ✓ | — | ✓ |
| U-ESO-04 | Z, A e isótopos | `ESOFYQ::U-ESO-04::02_Z_A_isotopos` | ✓ | — | — |
| U-ESO-04 | Iones | `ESOFYQ::U-ESO-04::03_iones` | ✓ | — | — |
| U-ESO-04 | Modelos atómicos | `ESOFYQ::U-ESO-04::04_modelos_atomicos` | ✓ | ✓ | — |
| U-ESO-04 | Familias periódicas | `ESOFYQ::U-ESO-04::05_familias_periodicas` | ✓ | — | — |

## Rutas recomendadas

- **DESDE_CERO**: Todas las lecciones (curso introductorio)
- **STANDARD**: Todas las lecciones
- **EXCELLENCE**: 5 lecciones con contenido ADVANCED/ENRICHMENT significativo
- **FAST_REVIEW**: 4 lecciones (1 resumen por unidad)

## Origen

Bundles forkeados de `fq_completo__U-ESO-*.json` el 2026-10-19.
Los bundles originales `eso_fisicaquimica__*.json` (formato antiguo, sin scope) siguen existiendo como referencia.
