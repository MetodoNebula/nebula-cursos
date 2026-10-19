# FRONTEND_CHANGES.md — selectividad_fisica (piloto v2)

## Resumen

**No se ha modificado `index.html` ni ningún otro fichero del frontend.**
La migración a `schema_v2` es puramente aditiva (ver `SCHEMA_MIGRATION.md`),
así que el parser actual —que indexa los bundles por nombre de campo plano
(`theory_blocks`, `objectives`, `exercises`, `mcq`, `summary`...)— sigue
funcionando exactamente igual: simplemente nunca lee la clave `schema_v2`
que ahora acompaña a cada lección, igual que ya ignoraba otros campos de
metadato (`provenance`, `concept_ids`, etc.) que no usa para renderizar.

Verificación: `grep -c "schema_v2" index.html` → `0` referencias. El HTML no
necesita saber que la clave existe.

## Cuándo SÍ haría falta tocar el frontend

Las rutas pedagógicas (`DESDE_CERO/STANDARD/EXCELLENCE/FAST_REVIEW`), los
checkpoints y el Exam Mode están ahora representados como datos en
`schema_v2.learning_design.recommended_routes` y en los ficheros nuevos de
Fase 6 (`unit_checkpoints.json`, `exam_mode.json`, `diagnostic.json`), pero
**la interfaz actual no tiene ningún control para que el alumno elija una
ruta**: muestra la lección entera, de un tirón, igual que siempre.

Para que las 4 rutas sean navegables de verdad por un alumno (y no solo
"existan en el JSON"), hace falta como mínimo:

1. Un selector de ruta (al entrar al curso o por unidad) que filtre, dentro
   de cada lección, qué bloques de `schema_v2.presentation.*` y qué piezas de
   `schema_v2.practice.items` se muestran, usando `route_visibility` /
   `recommended_routes`.
2. Una pantalla de diagnóstico inicial que lea `diagnostic.json` y proponga
   una ruta por defecto según el vector de habilidades del alumno.
3. Una pantalla de checkpoint que lea `unit_checkpoints.json` y muestre
   `needs_support/ready/mastered` tras cada bloque de lecciones.
4. Un modo de examen separado que lea `exam_mode.json` (topic/mixed/timed/
   mock) y reduzca el scaffolding (oculte hints, pida la respuesta antes de
   mostrar `full_solution`).

Esto es trabajo de frontend genuino (nuevas vistas de UI, no solo datos) y
queda fuera del alcance de este piloto, que es de contenido y estructura de
datos. Se documenta aquí explícitamente como la before/after real: **los
datos para las 4 rutas, los checkpoints y el Exam Mode ya existen y son
consistentes (ver QA_REPORT.md); lo que falta para que el alumno las use es
la capa de interfaz que las consuma.**

## Comprobación de que el visor actual sigue funcionando con los bundles del piloto

Ver Fase 8 / `MIGRATION_NOTES.md`: se sirvió `index.html` con
`python -m http.server` apuntando a los bundles del piloto (sustituyendo
temporalmente los de `bundles/`) y se verificó que selectividad_fisica carga,
lista sus 8 unidades y abre lecciones sin errores de consola relacionados con
el nuevo campo `schema_v2`.
