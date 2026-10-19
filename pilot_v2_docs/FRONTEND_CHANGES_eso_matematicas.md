# Frontend Changes — eso_matematicas Pilot v2

## Cambios que SÍ afectan al frontend
1. **137 SVGs** añadidos como `assets[type:"svg"]` — el frontend ya los renderiza
2. **Nuevo bundle**: `eso_matematicas__foundations.json` — requiere entrada en `catalog.json`
3. **Correcciones** en `theory_blocks[].content`, `mcq` opciones/respuestas

## Cambios que NO afectan al frontend
- `schema_v2`: campo aditivo, ignorado
- Archivos de evaluación (unit_checkpoints, diagnostic, exam_mode): no consumidos aún

## catalog.json
Añadir solo la unidad foundations al curso `eso_matematicas`. **NO alterar otros proyectos.**
