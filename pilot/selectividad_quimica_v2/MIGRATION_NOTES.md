# MIGRATION_NOTES.md — selectividad_quimica

## Escritura en disco
- 10 bundles (U00 + 9) a `pilot/selectividad_quimica_v2/` y a `bundles/`.
- Datos: `KNOWLEDGE_GRAPH.json`, `unit_checkpoints.json`, `diagnostic.json`, `exam_mode.json` y deliverables a `pilot/selectividad_quimica_v2/`.
- Originales congelados en `original/selectividad_quimica/` (rollback).
- **catalog.json NO modificado** (lo gestiona el coordinador): debe añadir la unidad `U00_Fundamentos` y, si se desea, actualizar títulos.

## NEEDS_HUMAN_REVIEW / trabajo de continuación
1. **División de navegación de U08_Organica (27 lecc) y U05_Equilibrio (19 lecc)** recomendada por la auditoría: es un cambio a nivel de catálogo (nuevas unidades de navegación) que no se ejecuta aquí para no romper el catálogo compartido. Decisión de arquitectura pendiente.
2. **Backlog de diagramas:** 38 lecciones de contenido con ≥4 bloques siguen sin figura. Se añadieron 6 de alto valor (perfil energético, mapa de Gibbs, valoración, reactivo limitante, pila, equilibrio dinámico). Prioridad siguiente sugerida: gases ideales (U01/04), disoluciones/dilución (U01/05,11), configuración electrónica (U02/06), Kp-Kc y tablas ICE (U05/11,12), estructuras orgánicas (U08/02-07).
3. Añadir U00 al catálogo para que Foundations sea visible.
