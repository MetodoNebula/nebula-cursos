# MIGRATION_NOTES.md — selectividad_fisica (piloto v2 → release)

## Qué hace `scripts/pilot_fisica/release_catalog.py` (Fase 8)

1. Lee las 9 unidades validadas de `pilot/selectividad_fisica_v2/`
   (`fundamentos` + las 8 originales, ya con las correcciones de Fase 1,
   `schema_v2` de Fase 3, atomización de Fase 4 y referencias arregladas
   de Fase 7).
2. Copia cada bundle a `bundles/selectividad_fisica__<unidad>.json`,
   **sin tocar los bundles de ningún otro curso** (verificado: el resto de
   `projects` en `catalog.json` queda exactamente igual, comprobado
   comparando antes/después).
3. Regenera la entrada `"selectividad_fisica"` de `catalog.json`: unidades,
   lecciones (con `n` secuencial, título, dificultad, duración y el conteo
   real de piezas de cada lección) y los totales del curso.

`catalog.json` y `bundles/` **no están versionados en git** — así lo marca
`.gitignore` ("Contenido en claro: en la web solo va la version cifrada").
Es exactamente el mismo patrón que ya seguía el resto del proyecto (el
contenido en claro se sirve en local o se cifra con `cifrar.js` para
publicar); por eso el script vive en `scripts/pilot_fisica/` (versionado)
pero su salida no se commitea.

## Antes / después en `catalog.json`

| | Antes (original) | Después (piloto) |
|---|---|---|
| Unidades | 8 | 9 (+ `fundamentos`) |
| Lecciones | 76 | 88 (+6 Fundamentos, +6 de atomizar 6 lecciones en 12) |
| Piezas totales | 5 888 | 6 047 |

El incremento de piezas no es relleno: son las piezas nuevas que exige el
encargo (microlecciones de Fundamentos con su propio `worked_example`,
`exercises`, `mcq`...) más una pieza nueva de teoría (`TH-06-9`, nota
Advanced sobre potencial vector añadida en la Fase 1) y los `objectives`
duplicados deliberadamente entre las dos partes de cada lección atomizada
(fix de Fase 7, documentado en `QA_REPORT.md`).

## Verificación del frontend (Fase 8)

Sin modificar `index.html`:

```
python3 -m http.server 8899   # en la raíz del proyecto
curl http://localhost:8899/index.html      -> 200
curl http://localhost:8899/catalog.json    -> 200, JSON valido, 9 proyectos,
                                               selectividad_fisica con 9 unidades
curl http://localhost:8899/bundles/selectividad_fisica__fundamentos.json
                                            -> 200, JSON valido, 6 lecciones
```

El modo `PLAIN` de `index.html` (activo en `localhost`/`127.0.0.1`) lee los
bundles sin descifrar, que es como se comprobó esto.

**Limitación declarada:** esta sesión no tuvo un navegador/automatizador
disponible en la máquina del usuario (no había Playwright/Chromium en el
shell remoto), así que la verificación fue a nivel HTTP + JSON (respuesta
200, JSON parseable, estructura esperada), no una comprobación visual de
consola del navegador. Para una verificación completa se recomienda abrir
`http://localhost:8899/?cifrado` (o sin el parámetro, en modo plano) en un
navegador real y confirmar que el curso "Física" carga sus 9 unidades y
abre lecciones sin errores de consola — es el paso que un humano con
acceso a un navegador en esa máquina puede completar en un minuto.

## Cómo volver atrás (rollback)

`original/selectividad_fisica/` contiene las 8 unidades **exactamente**
como estaban antes de empezar este piloto (congeladas en la Fase 0, nunca
tocadas). Para revertir: copiar esos 8 ficheros de vuelta a `bundles/` y
restaurar la entrada `selectividad_fisica` de `catalog.json` desde el
historial de git (el commit previo a `fix/selectividad_fisica/fase0-...`)
o desde una copia de seguridad de `catalog.json` tomada antes de ejecutar
`release_catalog.py`.
