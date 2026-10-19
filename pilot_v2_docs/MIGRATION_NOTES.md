# Migration Notes — eso_matematicas Pilot v2

## Pasos para desplegar

1. **Copiar bundles** de `pilot/eso_matematicas_v2/bundles/` → `Nebula_Cursos_Web/bundles/`
2. **Actualizar catalog.json** — añadir unidad foundations (id: mat_foundations, order: 0)
3. **Copiar archivos de evaluación** (unit_checkpoints, diagnostic, exam_mode) a la raíz del curso
4. **Cifrar**:
   ```cmd
   cd E:\gpt_testing\Nebula_GPT_Cowork\Nebula_Cursos_Web
   set NEBULA_PASS=Nebula123!
   node cifrar.js
   ```
5. **Verificar** en https://metodonebula.github.io/nebula-cursos/

## Rollback
Originales preservados en `bundles_original/`. Copiar de vuelta, eliminar foundations y eval, re-cifrar.
