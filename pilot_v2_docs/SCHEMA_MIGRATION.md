# Schema Migration — schema_v2

## Descripción
`schema_v2` es un bloque **ADITIVO** añadido a cada lección. No modifica ningún campo existente del frontend.

## Campos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `canonical_lesson_id` | string | ID único `ESOMAT::<unit>::<slug>` |
| `recommended_routes` | string[] | DESDE_CERO, STANDARD, EXCELLENCE |
| `epistemic_type` | string | DEFINITION, LAW, MODEL, etc. |
| `prerequisites_canonical` | string[] | IDs de prerequisitos |
| `estimated_mastery_time_min` | number | Tiempo estimado en minutos |
| `is_bachillerato` | boolean | Contenido de Bachillerato |
| `scope_summary` | object | Conteo CORE/ADVANCED/ENRICHMENT/EXTENSION |

## Impacto frontend: NINGUNO
## Rollback: Eliminar campo `schema_v2` de cada lección.
