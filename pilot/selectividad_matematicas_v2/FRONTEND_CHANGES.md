# FRONTEND_CHANGES.md — selectividad_matematicas

No se ha modificado `index.html`. La migración es aditiva (ver SCHEMA_MIGRATION.md)
y el reorden es de datos (orden del array `theory_blocks`), así que el visor actual
renderiza sin cambios: esencial primero y la ampliación al final con su separador.
Las 4 rutas, los checkpoints, el diagnóstico y el Exam Mode existen como datos; que
el alumno los navegue requeriría vistas de UI nuevas (igual que en física), fuera
del alcance de 'reordenar sin tocar el frontend'.

Pendiente de coordinación: añadir la unidad nueva **Fundamentos** (6 microlecciones)
y su entrada a `catalog.json` — lo hace el agente principal, no este piloto.
