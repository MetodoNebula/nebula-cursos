# Banco PAU — Matemáticas Aplicadas a las CCSS II · Informe de construcción

Curso `selectividad_matematicas_ccss`. Se ha añadido en cada bloque una lección nueva
**"Ejercicios de selectividad (PAU)"** (id `LPAU`, bkey `99_Ejercicios_de_selectividad_PAU.json`)
con problemas reales de EBAU/Selectividad resueltos paso a paso, con figuras validadas.

## Fuentes
59 exámenes (PDF, todos "Resuelto") de 13 comunidades: Andalucía, Aragón, Asturias,
Castilla-La Mancha, Castilla y León, Cataluña, Galicia, La Rioja, Madrid, Murcia, Navarra,
País Vasco y Comunidad Valenciana. Enunciados en gallego/catalán/valenciano/euskera traducidos
al español; copias bilingües deduplicadas a una sola en español.

## Problemas por bloque (exam_questions / figuras)
| Bloque | Ejercicios | Figuras |
|---|---:|---:|
| Fundamentos | 2 | 0 |
| Matrices | 39 | 0 |
| Sistemas de ecuaciones | 40 | 0 |
| Límites y continuidad | 21 | 12 |
| Derivadas | 61 | 26 |
| Representación de funciones | 25 | 23 |
| Integrales | 30 | 26 |
| Probabilidad | 88 | 62 |
| Programación lineal | 51 | 51 |
| Estadística bidimensional | 0 (sin lección) | 0 |
| Muestreo e inferencia | 69 | 9 |
| **TOTAL** | **426** | **209** |

**Estadística bidimensional**: ninguno de los 59 exámenes incluye covarianza/correlación/regresión
(ese tema no entra en la EBAU de CCSS II de estas comunidades), por lo que ese bloque no tiene
lección PAU. Los 10 bloques restantes sí la tienen.

## Figuras
Generadas con el builder del proyecto (`bundles/_fix_work/nebula_build.py`: LaTeX + dvisvgm →
SVG `data-nebula-svg`, paleta Nebula sobre tarjeta clara) y compiladas en el ordenador. Tipos:
región factible (PL), gráfica de función con asíntotas/cortes/tangente, área sombreada,
campana normal con IC, árbol de probabilidad, tabla de contingencia y diagrama de Venn.
Auditadas una a una (rasterizadas y revisadas): **sin recuadros blancos en los rótulos y sin
solapes texto-texto ni texto-línea**; 0 figuras fuera de tamaño; 209/209 SVG XML válidos.

## Validación
- **Lint MathJax** (mathjax del proyecto en Chromium headless, misma config) sobre los 426
  ejercicios ensamblados: **0 `mjx-merror`, 0 errores de consola** (3825 campos renderizados).
- **Estructura**: los 10 bundles cargan y tienen su lección LPAU con el nº correcto de
  exam_questions y figuras; `catalog.json` intacto con los **9 cursos**; `rebuild_catalog.py`
  terminó con **0 avisos**.
- **Auditoría de contenido independiente** (6 revisores, verificación con sympy/numpy/scipy):
  **los 426 resultados finales son correctos**. 0 defectos critical; 4 major + 12 minor,
  **todos corregidos** (ver abajo). 2 notas de clasificación en "fundamentos" (son problemas de
  patrones/sucesiones; están correctamente fuera de matrices/sistemas) sin cambio necesario.

## Correcciones aplicadas tras la auditoría
- PROB-029: `P(A∪D)` → `P(A∩D)` en el enunciado (coherencia con la solución).
- PROB-035 (datos oficiales incoherentes): reescrita como ejercicio de **detección de
  incoherencias** (se demuestra que los datos son imposibles) en lugar de dar un 0,22 imposible.
- MAT-008 y MAT-033 (apartados ilegibles en la extracción de exámenes de Valencia): recortados a
  los apartados verificables y autosuficientes (matriz normal x=2; |AB−2I₃|=30, invertible).
- DER-029: carácter de control en el título → `\frac` restaurado.
- LIM-005: evaluación de la rama correcta f(−1)=3.
- PL-001: prosa de edición depurada; PL-048/049: añadidas las soluciones enteras óptimas que faltaban.
- REP-018: signo del límite infinito corregido (−∞); REP-014: descripción de monotonía corregida.
- INT-030: aclarada la premisa a>0 por apartados.
- SIS-002: enunciado truncado completado; SIS-015: relato matricial dimensionalmente imposible sustituido.

## Publicación
El contenido está en los bundles y en `catalog.json` en claro (la web en localhost ya lo muestra).
Para publicarlo en la web cifrada, ejecuta `publicar.bat` como siempre (pide la contraseña,
re-cifra con `cifrar.js` y hace push). Copia de seguridad previa en `_pau_build_ccss/backup_<fecha>/`.
