# AUDIT_REPORT_v2 — Química (Selectividad)

**Fecha**: 2026-10-19  
**Curso**: selectividad_quimica  
**Lecciones**: 133 | **Bundles**: 10  
**Resultado global**: ✅ **0 ERRORES — Todos los gates pasan al 100%**

---

## Resumen ejecutivo

Auditoría programática y editorial completa de los 10 bundles del piloto v2. Se encontraron y corrigieron **3 errores ALTA** (full_solution faltante), **28 campos id faltantes**, y se añadieron **53 hints progresivos** a ejercicios guiados. Tras las correcciones, los 7 gates de validación pasan sin excepciones.

---

## Fase 1 — Backlog / semantic_change_ledger

| Hallazgo | Severidad | Estado |
|---|---|---|
| U07-L03 guided_exercises[0]: falta `full_solution` | P0 | ✅ FIXED |
| U08-L10 guided_exercises[1]: falta `full_solution` | P0 | ✅ FIXED |
| U08-L11 guided_exercises[0]: falta `full_solution` | P0 | ✅ FIXED |
| U08-L14 "producto único" sin matiz estereoquímico | P1 | ✅ VERIFIED (ya corregido en pilot v2) |
| U07 todas las lecciones (L01–L14): 28 ejercicios sin campo `id` | P1 | ✅ FIXED |

**Nuevos hallazgos P0/P1/P2**: 0.  
Los 17 ítems del ledger original fueron verificados como correctamente aplicados.

### Verificación epistémica

- EXAM_CONVENTION: verificado en H₂SO₄, estado estándar, convenciones PAU ✅
- APPROXIMATION: verificado en ΔH constante con T, gases ideales ✅
- MODEL: verificado en orbital/función de onda, enlaces σ/π ✅
- No se encontraron nuevas convenciones PAU presentadas como hechos universales.

---

## Fase 2 — scope + essential-first

| Métrica | Valor | Estado |
|---|---|---|
| Theory blocks totales | 660 | ✅ |
| CORE | 650 | ✅ |
| ADVANCED | 10 | ✅ |
| Sin scope | 0 | ✅ |
| MEZCLA (CORE después de ADVANCED) | 0 | ✅ |

Los 10 bloques ADVANCED son genuinamente de ampliación (no pertenecen al currículo PAU base).  
No se encontraron bloques CORE que deberían ser ADVANCED.

---

## Fase 3 — schema_v2

| Métrica | Valor | Estado |
|---|---|---|
| canonical_lesson_id únicos | 133 | ✅ |
| Duplicados | 0 | ✅ |
| Formato SELQUI::unit::slug | 133/133 | ✅ |
| Rutas recomendadas | DESDE_CERO, STANDARD, EXCELLENCE, FAST_REVIEW | ✅ |

---

## Fase 4 — Foundations (U00)

| Métrica | Valor | Estado |
|---|---|---|
| Micro-lecciones | 6 | ✅ |
| SVGs | 3 | ✅ |
| MCQ con distractores y why_wrong | ✅ | ✅ |
| Dificultad creciente | ✅ | ✅ |

Las 6 micro-lecciones cubren: formulación, mol, proporcionalidad/factores, notación científica, logaritmos pH, lectura de gráficas.

---

## Fase 5 — Evaluación

| Componente | Conteo | Estado |
|---|---|---|
| unit_checkpoints | 45 preguntas, 10 unidades | ✅ |
| diagnostic | 22 ítems, 14 ejes | ✅ |
| exam_mode | 220+ preguntas | ✅ |

---

## Fase 6 — Diagramas

| Métrica | Valor | Estado |
|---|---|---|
| SVGs totales | 104 | ✅ |
| XML válido | 104/104 | ✅ |
| Colores fuera de paleta Nebula | 31 SVGs (warning) | ⚠️ P2 |

Los 31 SVGs con colores fuera de paleta son funcionales y legibles. Los colores extra se usan para:
- Escalas de pH (arcoíris) en F05
- Diagramas de orbitales (rojo/azul convencional) en U02
- Diagramas de enlace (paleta extendida para claridad) en U03
- Perfiles energéticos (grises auxiliares) en U04/U05

**Recomendación**: Mantener como P2 — los colores extra mejoran la comprensión visual sin conflicto con la identidad Nebula.

---

## Correcciones aplicadas en esta auditoría

### ALTA (P0) — 3 correcciones
1. **U07-L03** (`03_Ajuste_por_ion-electrón_en_medio_ácido`): Añadido `full_solution` al ejercicio guiado 1 (ajuste de semirreacción Sn²⁺→Sn⁴⁺).
2. **U08-L10** (`10_Isomería_de_posición`): Añadido `full_solution` al ejercicio guiado 2 (comparación de tres pares de isómeros).
3. **U08-L11** (`11_Isomería_de_función`): Añadido `full_solution` al ejercicio guiado 1 (butanal vs butanona).

### MEDIA (P1) — 81 correcciones
4. **U07 L01–L14**: Añadidos 28 campos `id` (formato `EX-Q07-NN-GN`) a todos los ejercicios guiados que carecían de él.
5. **U00–U08**: Añadidos 53 hints progresivos (segundo hint) a ejercicios guiados que solo tenían 1. Distribución:
   - U00: 1 ejercicio
   - U01: 1 ejercicio
   - U02: 2 ejercicios
   - U03: 10 ejercicios
   - U04: 7 ejercicios
   - U05: 20 ejercicios
   - U06: 8 ejercicios
   - U08: 4 ejercicios

### VERIFICADO (ya corregido)
6. **U08-L14**: El matiz estereoquímico sobre "producto único" ya estaba incluido en el pilot v2.
7. **LaTeX delimiters** (U02-L07, U05-L02, U07-L14, U08-L21): Sin problemas detectados — falsos positivos del informe editorial.

---

## Estadísticas finales post-auditoría

| Métrica | Antes | Después |
|---|---|---|
| Errores GATE | 3 | 0 |
| Ejercicios ≥2 hints | 206 | 259 |
| Ejercicios 1 hint | 53 | 0 |
| Ejercicios sin full_solution | 3 | 0 |
| Ejercicios sin id | 28 | 0 |
| SVGs XML inválido | 0 | 0 |
| MEZCLA | 0 | 0 |
| canonical_lesson_id duplicados | 0 | 0 |
