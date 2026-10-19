# Auditoría v2 — Matemáticas CCSS (Selectividad)

**Fecha:** 19 de octubre de 2026  
**Alcance:** 9 bundles `selectividad_matematicas_ccss__*.json`, 66 lecciones  
**Tipo:** Corrección automatizada a partir de auditoría experta

---

## Resumen ejecutivo

| Categoría | Hallazgos | Corregidos | Estado |
|---|---|---|---|
| ALTA/CONCEPTO | 2 | 2 | ✅ FIXED |
| MEDIA/EDITORIAL | 86 | 86 | ✅ FIXED |
| MEDIA/ESTRUCTURA | 42 | 42 | ✅ FIXED |
| **Total** | **130** | **130** | **100% FIXED** |

Validación: 7 gates × 9 bundles = **63/63 PASS**

---

## Fase 1 — Correcciones ALTA/CONCEPTO

### Fix 4: Puntos de inflexión (mat_derivadas L08)

- **Severidad:** ALTA
- **Ubicación:** `summary.key_points[1]`
- **Error:** Presentaba $f''(x_0)=0$ como condición necesaria universal para puntos de inflexión
- **Corrección:** Redefinido como "punto en el que cambia la concavidad", con indicación de estudiar también puntos donde $f''$ no existe
- **Estado:** FIXED ✅

### Fix 5: Representatividad muestral (mat_muestreo_inferencia L01)

- **Severidad:** ALTA
- **Ubicación:** `summary.key_points[2]`
- **Error:** Afirmaba que "la aleatoriedad en la selección decide si la muestra representa a la población"
- **Corrección:** Sustituido por formulación que reconoce que la aleatoriedad favorece una selección sin sesgo pero la representatividad depende también del marco, la no respuesta y la variabilidad aleatoria
- **Estado:** FIXED ✅

---

## Fase 2 — Correcciones MEDIA/EDITORIAL

**86 marcadores "la idea correspondiente"** sustituidos por misconceptions concretas.

| Bundle | Instancias |
|---|---|
| mat_derivadas | 30 |
| mat_matrices | 18 |
| mat_sistemas | 17 |
| mat_programacion_lineal | 12 |
| mat_integrales | 9 |

---

## Fase 3 — Correcciones MEDIA/ESTRUCTURA

**42 ejercicios guiados** con menos de 2 pistas recibieron una segunda pista progresiva.

| Bundle | Ejercicios corregidos |
|---|---|
| mat_derivadas | 18 |
| mat_limites | 9 |
| mat_integrales | 8 |
| mat_representacion | 4 |
| mat_probabilidad | 1 |
| mat_programacion_lineal | 1 |
| mat_sistemas | 1 |

---

## Fase 4 — Recomendación sobre módulo Foundations

El curso CCSS no dispone de un módulo de fundamentos separado (a diferencia de Mates II). **Se recomienda crear uno** con las siguientes micro-lecciones:

1. **Ecuaciones y sistemas 2x2** — prerrequisito para mat_sistemas y mat_programacion_lineal
2. **Funciones elementales** — prerrequisito para mat_limites, mat_derivadas, mat_representacion
3. **Proporcionalidad y porcentajes** — prerrequisito para mat_probabilidad y mat_muestreo_inferencia
4. **Combinatoria básica** — factorial, combinaciones para probabilidad
5. **Lectura de gráficas y tablas** — prerrequisito transversal

Esta recomendación requiere aprobación del usuario antes de implementarse.

---

## Validación

Todos los 9 bundles pasan los 7 gates:
1. ✅ JSON válido
2. ✅ canonical_lesson_id únicos
3. ✅ 0 MEZCLA
4. ✅ MCQ correct key presente
5. ✅ SVG XML válido
6. ✅ Campos obligatorios presentes
7. ✅ Integridad estructural preservada
