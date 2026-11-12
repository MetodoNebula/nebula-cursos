# Enriquecimiento de Matemáticas ESO con los PDFs de `ejercicios_Mates_ESOResueltos`

**Curso:** `eso_matematicas` · **Fecha:** 2026-11-12
**Fuentes:** los 12 PDFs de `ejercicios_Mates_ESOResueltos/` (11 iniciales + `estadistica_combinatoria_probabilidad_nebula.pdf`).
**Alcance:** 11 unidades de `eso_matematicas`. No se ha tocado Selectividad, GCSE, IB ni FQ.

---

## 1. Qué se ha añadido

**115 ejercicios nuevos**, 0 eliminados (trabajo aditivo). Todos con `provenance: SOURCE_DERIVED`,
enunciado, 1–2 `hints`, `answer` breve, `full_solution` en prosa paso a paso con comprobación final,
y `common_errors` apuntando a una trampa concreta.

| Unidad | PDF de origen | +Ej |
|---|---|---|
| mat_potencias_raices | tema_2.pdf | 26 |
| mat_sucesiones | ejercicios_de_sucesiones_resueltos.pdf + hoja-08-sucesiones-pend-3eso.pdf | 17 |
| mat_algebra_polinomios | EJERCICIOS_DE_FRACCIONES_ALGEBRAICAS.pdf | 11 |
| mat_sistemas_inecuaciones | inecuaciones.pdf | 11 |
| mat_proporcionalidad_financiera | problemas-de-proporcionalidad.pdf | 11 |
| mat_trigonometria | trigonometria.pdf + 7-trigonometria.pdf | 10 |
| mat_estadistica_descriptiva | Ejercicios de Estadistica.pdf + PDF Nebula | 10 |
| mat_complejos | 7_complejos.pdf | 6 |
| mat_limites_continuidad | limites_continuidad.pdf | 6 |
| mat_probabilidad | PDF Nebula | 4 |
| mat_estadistica_bidimensional | PDF Nebula | 3 |
| **TOTAL** | | **115** |

Reparto de dificultad: **d3 = 17, d4 = 64, d5 = 34** (todos de nivel medio-alto: se eligieron
técnicas y trampas que NO estaban ya cubiertas en el curso).

### Huecos que cubren (lo que no había antes)
- **Potencias/raíces:** prefijos del SI encadenados, orden de magnitud por número de cifras,
  cuántas cifras tiene el cuadrado de un número de 6 cifras, ajedrez ($2^{64}-1$), papel doblado,
  radicales equivalentes, raíz de raíz, ordenar radicales de distinto índice, decibelios, pH y ordenación
  por acidez, factor de crecimiento diario a partir del semanal.
- **Sucesiones:** recurrencia tipo Fibonacci con otros valores iniciales, pertenencia de un número a
  una sucesión, PA con diferencia negativa y término lejano, lados en PA, «¿cuántos términos sumar
  para obtener S?» (ecuación de 2.º grado), PG con razón negativa, PG con $r^4=16$ (**dos soluciones**).
- **Álgebra:** factorización doble con Ruffini, fracciones algebraicas con mcm de tres denominadores,
  restricciones del dominio incluidas las de factores que se cancelan.
- **Inecuaciones:** con denominadores, casos degenerados ($\varnothing$ y $\mathbb{R}$),
  raíz doble con los cuatro signos, IMC con redondeo de extremos de intervalo.
- **Proporcionalidad:** unidades distintas antes de plantear la proporción, conversión sexagesimal
  del resultado, trampa de «3 vacas más» y de «¿cuántos hay que contratar?».
- **Trigonometría:** grados-minutos-segundos, polígonos regulares (apotema y área), pendiente en %
  (tangente, no ángulo), $\tan\alpha=\cos\alpha$, coherencia de $\sin$ y $\cos$.
- **Límites:** $0/0$ que deja $k/0$ (laterales y existencia), doble racionalización,
  multiplicidad par vs impar del factor que anula el denominador, **indeterminación $1^\infty$** (no existía).
- **Complejos:** potencias de $i$ con exponente negativo, ecuación de grado 4 en $\mathbb{C}$,
  sistema con dos pares de soluciones reales, propiedades del conjugado.
- **Estadística y probabilidad (PDF Nebula):** cuartiles y moda por intervalos con frecuencias
  acumuladas, CV con datos agrupados, $r$ y recta de regresión con la fórmula de las sumas,
  interpolación vs extrapolación, combinaciones vs variaciones con papeletas, $P(A\cup B)$ en un
  espacio de combinaciones, Bayes con $P(V|H)$ frente a $P(H|V)$.

---

## 2. Validación (sin margen de error)

**(a) Matemática — doble verificación independiente.**
1. Durante la redacción, cada número se comprobó con `assert` en Python (`_enrich_pdf_20261112/ej_*.py`,
   función `val()`), usando `fractions.Fraction` para lo exacto.
2. Después, una **segunda pasada independiente con sympy** (`verify_sympy.py` y `verify_sympy2.py`)
   vuelve a deducir cada resultado desde el enunciado con otro método (factorización simbólica,
   `solveset`, `limit`, mínimos cuadrados simbólicos, `binomial`): **138 comprobaciones, todas correctas.**

**(b) Integridad de los bundles** (`audit2.py`): 0 problemas. Todos cargan como JSON; ids únicos;
`objective_ids` y `concept_ids` válidos en cada lección; `$` y llaves balanceados; sin saltos de línea;
ninguna solución corta; todos con hints y errores frecuentes; **ningún ejercicio previo alterado ni reordenado**.

**(c) Figuras** (`figcheck.py`): las **112 figuras** de las unidades tocadas se validaron una a una
(XML correcto, `viewBox`, rectángulo de fondo completo, marcador `data-nebula-fig`, ningún elemento
fuera del lienzo) → 0 problemas, y **ninguna fue modificada por el trabajo de ejercicios** (hash
idéntico al backup). Además se rasterizaron y revisaron visualmente 27 figuras (las de mayor carga
de texto de cada unidad).

### Defecto de figuras encontrado y corregido
La macro `\nbdotb` colocaba su etiqueta a `below=5pt`, **la misma altura que los números de las marcas**
de `\nbnumline` (`below=3pt`), de modo que se solapaban. Afectaba a **5 figuras** de todo el curso:

| Figura | Unidad | Solape |
|---|---|---|
| `AS-8A01-2` | mat_limites_continuidad | «$x=2$: excluido del dominio» sobre las marcas 1, 2 y 3 |
| `AS-02-03-1` | mat_potencias_raices | $10^{-6}$ sobre $-6$ y $10^{9}$ sobre $9$ |
| `AS-1303-1` | mat_estadistica_bidimensional | $x=1$ sobre la marca 1 y $x=5$ sobre la 5 |
| `AS-0101-1` | mat_numeros_operaciones | $-7$, $-5$, $-2$ sobre sus marcas |
| `AS-0101-2` | mat_numeros_operaciones | $-12$ sobre su marca |

Corregido en `_mat_enrich_shared/nebula_figures.tex` (`below=16pt`) y regeneradas las 5 figuras con el
pipeline de siempre (`svcgen.py`), que reproduce byte a byte las figuras no afectadas. Verificado
visualmente: los solapes han desaparecido. Copias en `_enrich_pdf_20261112/_figuras_auditadas/`.

### Erratas detectadas en las fuentes (no se han propagado)
- `tema_2.pdf` (2.95): da $1{,}097$ como factor de crecimiento diario para un $84\%$ semanal.
  Lo correcto es $\sqrt[7]{1{,}84}\approx 1{,}0910$; con $1{,}097$ el crecimiento semanal sería del $91{,}2\%$.
  El ejercicio `EX-02-05-P3` usa el valor correcto y pide al alumno detectar el error.
- `inecuaciones.pdf` (ej. 10): da $3571$ libros; la desigualdad $7n>25\,000$ exige $n\ge 3572$.
  `EX-0604-P4` pide comprobarlo.
- PDF de Nebula (1.3): $CV$ redondeado a $52{,}54\%$; el valor correcto es $52{,}535\% \to 52{,}53\%$.
  `EX-1205-P3` usa $52{,}53\%$.
- `problemas-de-proporcionalidad.pdf` (ej. 17): la frase de solución está copiada del ejercicio 16.

---

## 3. Pendiente (tú)

Publicar cifrando con tu contraseña: `node cifrar.js` (o `publicar.bat`). No puedo hacerlo yo.

## 4. Notas

- **Backups de rollback:** `bundles/_backup_pdf_enrich_20261112/` (9 unidades + catalog) y
  `bundles/_backup_pdf_enrich_20261112b/` (probabilidad, bidimensional, descriptiva).
  `catalog.json.bak_pdfenrich_20261112`. Bórralos cuando estés conforme.
- `catalog.json` regenerado con `scripts/rebuild_catalog.py`: 11 cursos, 0 avisos.
  `eso_matematicas`: 129 lecciones, 2166 ejercicios.
- Herramientas de este trabajo en `_enrich_pdf_20261112/`: módulos `ej_*.py` (ejercicios + validación),
  `audit2.py` (integridad), `figcheck.py` (figuras), `verify_sympy*.py` (verificación independiente),
  `spec.py` (volcado de objetivos/conceptos por unidad).
