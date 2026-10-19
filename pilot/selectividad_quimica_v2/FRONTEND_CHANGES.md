# FRONTEND_CHANGES.md — selectividad_quimica

**No se ha modificado `index.html` ni el frontend.** La migración es aditiva (ver SCHEMA_MIGRATION) y el reordenado esencial-primero actúa sobre el **orden del array** `theory_blocks` (lo que el visor ya renderiza), no sobre el motor.

Para que las 4 rutas, los checkpoints y el Exam Mode sean navegables por el alumno hace falta una capa de UI (selector de ruta, pantalla de diagnóstico/checkpoint, modo examen) que consuma `schema_v2`, `unit_checkpoints.json`, `diagnostic.json` y `exam_mode.json`. Los **datos** ya existen y están validados; falta la interfaz.

El módulo nuevo **00 Foundations** (`selectividad_quimica__U00_Fundamentos.json`) requiere que el **coordinador añada la unidad al `catalog.json`** para que aparezca en el visor (este fork no toca catalog.json, compartido con otros cursos).
