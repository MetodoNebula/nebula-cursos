# Changelog — Auditoría v2

## [2026-10-19] Auditoría v2 — Matemáticas II + Matemáticas CCSS

### Correcciones ALTA/CONCEPTO (P0)

- **mat_derivadas L01** (Mates II): Corregida afirmación incorrecta sobre cociente incremental tendiendo a infinito en caso de discontinuidad. El comportamiento puede ser divergente u oscilatorio.
- **mat_derivadas L10** (Mates II): Corregida definición de punto de inflexión que presentaba $f''=0$ como condición necesaria universal. Añadida mención a puntos donde $f''$ no existe.
- **mat_limites L03** (Mates II): Corregida misma sobresimplificación del cociente incremental en contexto de propiedades de límites.
- **mat_derivadas L08** (CCSS): Misma corrección de punto de inflexión que en Mates II.
- **mat_muestreo_inferencia L01** (CCSS): Corregida afirmación que sobrestimaba lo que garantiza la selección aleatoria respecto a la representatividad.

### Correcciones MEDIA/EDITORIAL (P1)

- **162 marcadores "la idea correspondiente"** sustituidos por misconceptions concretas derivadas del campo `mistake` de cada `common_mistake`.
  - Mates II: 76 instancias (mat_derivadas: 33, mat_probabilidad: 27, mat_representacion: 12, mat_determinantes: 4)
  - CCSS: 86 instancias (mat_derivadas: 30, mat_matrices: 18, mat_sistemas: 17, mat_programacion_lineal: 12, mat_integrales: 9)

### Correcciones MEDIA/ESTRUCTURA (P1)

- **115 ejercicios guiados** con menos de 2 pistas recibieron una segunda pista progresiva con andamiaje contextual.
  - Mates II: 73 ejercicios (10 bundles afectados)
  - CCSS: 42 ejercicios (7 bundles afectados)

### Validación

- 21 bundles × 7 gates = **147/147 PASS** (100%)
- 0 errores de JSON, 0 IDs duplicados, 0 MEZCLA, 0 MCQ inválidos, 0 SVG mal formados, 0 campos vacíos
