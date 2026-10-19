# Auditoría v2 — Matemáticas II (Selectividad)

**Fecha:** 19 de octubre de 2026  
**Alcance:** 13 bundles `selectividad_matematicas__*.json`, 107 lecciones  
**Tipo:** Corrección automatizada a partir de auditoría experta

---

## Resumen ejecutivo

| Categoría | Hallazgos | Corregidos | Estado |
|---|---|---|---|
| ALTA/CONCEPTO | 3 | 3 | ✅ FIXED |
| MEDIA/EDITORIAL | 76 | 76 | ✅ FIXED |
| MEDIA/ESTRUCTURA | 73 | 73 | ✅ FIXED |
| **Total** | **152** | **152** | **100% FIXED** |

Validación: 7 gates × 13 bundles = **91/91 PASS**

---

## Fase 1 — Correcciones ALTA/CONCEPTO

### Fix 1: Cociente incremental y discontinuidad (mat_derivadas L01)

- **Severidad:** ALTA
- **Ubicación:** `theory_blocks[2].body`
- **Error:** Afirmaba que si $f$ no es continua en $a$, el cociente incremental tiende a $\pm\infty$
- **Corrección:** Sustituido por: "Si $f$ no es continua en $a$, $f$ no es derivable en $a$. El cociente incremental no posee entonces un límite finito común; su comportamiento puede ser divergente u oscilatorio."
- **Estado:** FIXED ✅

### Fix 2: Puntos de inflexión (mat_derivadas L10)

- **Severidad:** ALTA
- **Ubicación:** `summary.key_points[1]`
- **Error:** Presentaba $f''(x_0)=0$ como condición necesaria universal para puntos de inflexión
- **Corrección:** Redefinido como "punto en el que cambia la concavidad", añadiendo que hay que estudiar puntos donde $f''$ no existe
- **Estado:** FIXED ✅

### Fix 3: Cociente incremental en límites (mat_limites L03)

- **Severidad:** ALTA
- **Ubicación:** `theory_blocks[4].body`
- **Error:** Misma sobresimplificación del cociente incremental en el contexto de propiedades de límites
- **Corrección:** Reformulado para distinguir correctamente los casos y añadir la observación general sobre discontinuidad y derivabilidad
- **Estado:** FIXED ✅

---

## Fase 2 — Correcciones MEDIA/EDITORIAL

**76 marcadores "la idea correspondiente"** sustituidos por la misconception concreta asociada a cada error frecuente.

| Bundle | Instancias |
|---|---|
| mat_derivadas | 33 |
| mat_probabilidad | 27 |
| mat_representacion | 12 |
| mat_determinantes | 4 |

Cada marcador se reemplazó con texto diagnóstico derivado del campo `mistake` correspondiente, formulado como la creencia errónea subyacente.

---

## Fase 3 — Correcciones MEDIA/ESTRUCTURA

**73 ejercicios guiados** con menos de 2 pistas recibieron una segunda pista progresiva.

| Bundle | Ejercicios corregidos |
|---|---|
| mat_derivadas | 22 |
| mat_limites | 11 |
| mat_integrales | 10 |
| mat_geometria_metrica | 8 |
| mat_representacion | 7 |
| mat_vectores | 6 |
| mat_rectas_planos | 5 |
| mat_sistemas | 3 |
| mat_probabilidad | 1 |

Las pistas añadidas proporcionan andamiaje progresivo: desde la orientación conceptual hasta el paso operativo concreto, sin revelar la respuesta.

---

## Validación

Todos los 13 bundles pasan los 7 gates:
1. ✅ JSON válido
2. ✅ canonical_lesson_id únicos
3. ✅ 0 MEZCLA (ningún CORE después de ADVANCED)
4. ✅ MCQ correct key presente en options
5. ✅ SVG XML válido
6. ✅ Campos obligatorios (title, theory_blocks, objectives)
7. ✅ Integridad estructural preservada
