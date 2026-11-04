# Auditoría — Ejercicios de selectividad (PAU) · Matemáticas II

**Curso:** `selectividad_matematicas` (label «Matemáticas II»)
**Fecha:** 2026-11-04
**Alcance:** nueva lección «Ejercicios de selectividad (PAU)» (id `LPAU`) en cada bloque del curso.

## Resultado

- **400 problemas** de Selectividad/EBAU resueltos paso a paso (planteamiento → desarrollo completo → resultado), repartidos en **12 lecciones LPAU** (una por bloque con contenido PAU).
- **172 figuras** compiladas con el builder del proyecto (`bundles/_fix_work/nebula_build.py`): LaTeX/TikZ → `dvisvgm` → SVG canónico `data-nebula-svg`, paleta Nebula sobre tarjeta clara.
- Catálogo regenerado (`rebuild_catalog.py`: **0 avisos**, 9 cursos intactos). `selectividad_matematicas` pasa de 107 a **119 lecciones**.

| Bloque | Problemas | Figuras |
|---|---|---|
| derivadas | 53 | 36 |
| determinantes | 8 | 0 |
| distribuciones | 26 | 20 |
| geometría métrica | 54 | 16 |
| integrales | 57 | 33 |
| límites | 18 | 7 |
| matrices | 37 | 0 |
| probabilidad | 49 | 31 |
| rectas y planos | 32 | 14 |
| representación | 13 | 13 |
| sistemas | 49 | 0 |
| vectores | 4 | 2 |
| **TOTAL** | **400** | **172** |

> `fundamentos` no recibe lección LPAU: ningún problema de los 54 exámenes es «repaso puro» sin tema PAU específico (criterio del encargo).

## Motor (idéntico al de Química/Física)

1. **Extracción + dedup.** 56 PDF → `pdftotext -layout` (todos con texto real, ninguno escaneado). Deduplicados a **54 exámenes** (descartadas las 2 versiones sin resolver `Aragón_2026-Ordinaria` y `Asturias_2026-Ordinaria`, que tienen su `_Resuelto_`). 11 comunidades, 2024–2026.
2. **Idioma.** En exámenes bilingües (Cataluña, Valencia, País Vasco) se usó solo el español; los exámenes íntegramente en valenciano/catalán se tradujeron al castellano. Coma decimal española dentro de `$...$`.
3. **Parseo + clasificación + formato** por comunidad (11 subagentes en paralelo con una FORMAT_SPEC común): cada problema → `exam_question` con `statement`, `knowns`, `full_solution` (apartados **(a)**,**(b)**…, bloques `$$...$$`), `answer`, `common_errors`, `mark_scheme`, `marks`, `provenance`, `source`, `assets`.
4. **Verificación.** Cada resultado no trivial se comprobó con Python (sympy/numpy): derivadas, integrales, límites, sistemas, determinantes, inversas, autovalores, probabilidades, binomial/normal.
5. **Figuras** (centralizado, 6 subagentes de parámetros + compilación propia): gráficas de función con `pgfplots` (cortes, extremos, asíntotas v/h/oblicuas, rectas tangentes), áreas sombreadas bajo/entre curvas, campanas normales con cola sombreada, árboles de probabilidad, diagramas de Venn y esquemas 3D (plano, recta, distancia, simétrico, tetraedro, vectores). Rasterizadas y revisadas para **cero solapamiento**.
6. **Ensamblado atómico** (`tmp + os.replace`) en los 13 bundles y en `catalog.json` (recurso compartido por los 9 cursos; se preservó la estructura `{projects:[...]}`). Copia de seguridad previa en `_pau_build_mat/backup_*`.

## Auditoría de calidad

- **Figuras — sin cuadros blancos ni solapes.** El fondo de todas las etiquetas se igualó a la tarjeta (`NebulaBG`) y se quitó el fondo de los rótulos de ejes (se veían como recuadros sobre regiones sombreadas). Las curvas con asíntota vertical se parten en ramas (sin «tapa» horizontal). Se revisó cada figura rasterizada; se descartaron **8 esquemas 3D** de «punto simétrico respecto a un plano» por amontonamiento de etiquetas (mejor sin figura que con solape) — el desarrollo escrito es autosuficiente en esos casos.
- **MathJax lint.** Render de los **4418 campos** (statement + full_solution + answer + knowns + common_errors + mark_scheme) en Chromium headless con el MathJax y la configuración exactos del proyecto: **0 `mjx-merror`, 0 errores de consola**.
- **Estructura.** Todos los bundles y `catalog.json` cargan; `{projects:[...]}` intacto con los 9 cursos; las 12 entradas LPAU del catálogo apuntan al bundle/bkey correctos y sus recuentos coinciden.
- **Contenido.** Muestra de 10 problemas de 7 bloques revisada y **re-verificada con sympy** (límites, determinantes, sistemas con parámetro, probabilidad condicionada, área entre curvas, distancia punto-plano, binomial): todos correctos. El desarrollo es paso a paso, nombra los teoremas (Rouché-Frobenius, Barrow, Bayes), y los `common_errors`/`mark_scheme` son específicos del problema (no genéricos).

### Erratas de solucionarios oficiales detectadas y corregidas (ejemplos)
Los subagentes corrigieron y anotaron en `common_errors` varios deslices de las hojas oficiales/autor, usando el valor verificado:
- Valencia 2024-Extra P1: determinante real $k^2-k-18$ (la clave SUV decía otra cosa).
- Andalucía 2025-Extra: producto mixto $-9$ (la hoja ponía $-7$).
- Cantabria 2026-Ord: $X=A^{-1}MA^{-1}$ (la clave usaba $A^{-1}MA$).
- Aragón 2024-Extra: área del triángulo $=\sqrt6$ (la hoja ponía $6$).
- País Vasco 2025-Ext: superficie $108\pi$ (se había perdido el $\pi$).
- Navarra 2024-Ord: constante del plano $K=16$ para la distancia pedida.

## Notas de publicación
- Los bundles y `catalog.json` se escribieron **en claro** (modo `localhost`/`PLAIN` del sitio). Para la web publicada hay que regenerar los cifrados (`cifrar.js` → `cifrado/*.bin`) con el flujo habitual (`publicar.bat`).
- Carpeta de trabajo conservada en `_pau_build_mat/` (textos, specs de figuras, SVG, scripts, backups). No se borró nada.

---

## Adenda (2026-11-04, tarde) — legibilidad y consistencia entre cursos

**Soluciones más espaciadas.** A petición del usuario (las soluciones iban muy cargadas), se reformateó el `full_solution` para que cada paso del razonamiento sea un párrafo propio (un apartado denso como «(4.2.1)» pasa de un bloque a 4 pasos con aire entre ellos). La transformación es **no destructiva**: solo inserta saltos de párrafo —se verificó que no cambia ningún carácter no-blanco y que los `$` siguen balanceados— y respeta intactos los bloques `$$...$$`, listas y tablas.

- **Matemáticas II (Ciencias):** 361/400 soluciones reespaciadas.
- **Matemáticas CCSS:** 156/426 soluciones reespaciadas (copia de seguridad en `_pau_build_mat/backup_ccss_*`).
- Re-lint MathJax tras el cambio: **0 `mjx-merror`, 0 errores de consola** en ambos cursos (4418 + 4719 campos). Catálogo regenerado: 0 avisos, 9 cursos.

**Comprobación de solapamiento con CCSS.** Los 54 exámenes de este trabajo son de **2.º Bachillerato de Ciencias** (`2oBachCC`); sus problemas (p. ej. el área bajo $y=\cos(\pi x/9)+2$, Valencia 2026) **no aparecen** en el curso `selectividad_matematicas_ccss`, que tiene su propia colección PAU a partir de los exámenes de Matemáticas Aplicadas (otra convocatoria/pista). No hay duplicación entre cursos.

**Extensión a Física y Química (misma mejora de espaciado).**
- **Física Selectividad:** 144/425 soluciones reespaciadas (copia en `_pau_build_mat/backup_selectividad_fisica_*`).
- **Química Selectividad:** 258/360 soluciones reespaciadas (copia en `_pau_build_mat/backup_selectividad_quimica_*`).
- Re-lint MathJax tras el cambio: **0 `mjx-merror`, 0 errores de consola** en ambos (3939 + 2842 campos). Catálogo: 0 avisos, 9 cursos.

En total, la mejora de legibilidad se aplicó a los **4 cursos de selectividad** (Matemáticas II, Matemáticas CCSS, Física y Química), de forma no destructiva y validada en todos.
