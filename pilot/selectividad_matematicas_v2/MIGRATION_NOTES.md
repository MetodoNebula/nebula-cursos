# MIGRATION_NOTES.md — selectividad_matematicas

- Originales congelados en `original/selectividad_matematicas/` (rollback).
- Bundles corregidos/reordenados escritos en `pilot/selectividad_matematicas_v2/`
  y en `bundles/` (lo que lee el visor).
- `structural_issues.csv` vacío: **sin atomización** (ninguna lección excedía el
  objetivo tras la medición del paquete de auditoría).
- **No** se tocó `catalog.json`: el agente principal regenerará la entrada del
  curso y añadirá la unidad Fundamentos. Las 12 unidades de contenido no cambian
  de número de lecciones, así que sus entradas siguen siendo válidas.
