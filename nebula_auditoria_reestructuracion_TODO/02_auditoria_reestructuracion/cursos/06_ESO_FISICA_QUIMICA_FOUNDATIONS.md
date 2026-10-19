# Auditoría de reestructuración — ESO — Física y Química (Foundations / versión standalone)

**Curso ID:** `eso_fisicaquimica`  
**Unidades actuales:** 4  
**Lecciones actuales:** 19  
**Palabras pedagógicas aproximadas:** 26,456  
**Mediana de palabras/hora declarada:** ~857  
**Documento maestro obligatorio:** `../00_MASTER_IMPLEMENTATION_SPEC.md`

> Este documento está escrito como **especificación de ejecución** para un agente. No es una propuesta opcional ni una lista de ideas. Las acciones P0/P1 son obligatorias; las decisiones estructurales definen el estado objetivo del curso.

---

## 1. Veredicto y objetivo del rediseño

El curso debe permitir cuatro recorridos sobre una fuente canónica: **desde cero**, **estándar**, **excelencia** y **repaso rápido**. El agente debe conservar el contenido técnicamente útil, corregir el ledger semántico y reestructurar navegación/práctica para reducir carga cognitiva y mejorar transferencia.

No se debe medir éxito por "cantidad de texto conservado" sino por: corrección, trazabilidad, claridad, dominio y capacidad de recuperar prerrequisitos.

---

## 2. Inventario actual y acción por unidad

| Unidad actual | Lecciones | Palabras aprox. | Acción de arquitectura |
|---|---:|---:|---|
| `U-ESO-01` | 4 | 6.053 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-03` | 5 | 6.900 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-04` | 5 | 6.596 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `U-ESO-02` | 5 | 6.907 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations científicas** — Pregunta/hipótesis/evidencia, SI, conversiones, incertidumbre, tablas y gráficas.
2. **01 Materia y modelo de partículas** — Masa/volumen/densidad -> partículas -> temperatura/cambios de estado -> curvas de calentamiento.
3. **02 Sustancias, mezclas y disoluciones** — Clasificación -> separación -> soluto/disolvente -> concentración -> diseño experimental.
4. **03 Estructura atómica básica** — Partículas subatómicas -> Z/A/isótopos -> iones -> modelos atómicos -> tabla/estructura al alcance.
5. **04 Checkpoint de Foundations** — Evaluación acumulativa que decide si el alumno puede saltar recuperación al entrar en 4.º ESO/Bachillerato.


### Función recomendada de este corpus
Convertirlo en **Foundations de Física y Química**, no mantenerlo como una copia paralela de FQ completo. Debe ser corto, extremadamente claro y reutilizable como recuperación desde cursos posteriores.

- La prioridad es comprensión de medición, partículas, mezclas y átomo.
- Evitar fórmulas que todavía no se puedan interpretar; si aparecen Q=mcΔT o Q=mL, deben ser opcionales/extension si la unidad pretende ser realmente básica.
- Los summaries actuales deben regenerarse completamente si contienen boilerplate/truncado.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U-ESO-02 / lesson_03` | Cambios de estado: "absorber calor => aumenta Ec" contradice meseta a T constante. | Reescribir en tres fases: antes cambia Ec/T; durante cambio T constante y cambia energía potencial/configuración; después vuelve a cambiar Ec/T. | Teoría, summary y MCQ coinciden. |
| P0 | `corpus / versionado` | Duplica 19 lecciones con fq_completo y divergen. | Convertir a fuente canónica: uno de los dos deja de ser copia editable. Usar canonical_lesson_id + variant/config o generación derivada. | No existen dos bodies independientes con mismo canonical_lesson_id. |
| P1 | `summaries` | Boilerplate repetitivo y campos truncados como "Una curva T vs." o "1.". | Regenerar summary desde core_claims/assumptions/formulae/mistakes. Añadir lint de truncado. | Ningún summary contiene fragmentos incompletos o boilerplate genérico como idea principal. |
| P2 | `U-ESO-02 / curvas de calentamiento` | "Mesetas perfectamente horizontales" como afirmación experimental. | Decir horizontal en modelo ideal/aproximadamente horizontal en experimento con sustancia pura bajo condiciones controladas. | Claim etiquetado MODEL. |
| P3 | `MCQ corpus` | 228 distractores sin why_wrong. | No rellenar mecánicamente todos: completar prioritariamente distractores que representan misconceptions; permitir omission para distractores triviales con regla documentada. | 100% de distractores conceptuales tienen feedback útil. |


### Regla de propagación
Cada corrección de esta tabla debe aplicarse a **todas** las representaciones afectadas: objective, theory/core claim, formula, worked example, guided exercise, MCQ, flashcard, misconception, hint y summary. Corregir solo el párrafo principal no cierra el issue.

---

## 5. Cambios pedagógicos obligatorios por lección

Para cada lección actual, el agente debe ejecutar este procedimiento:

1. Identificar 1–4 **objetivos atómicos**. Si hay más, dividir.
2. Declarar prerrequisitos como concept IDs, no como texto libre únicamente.
3. Extraer claims canónicos y asignar `EXACT/MODEL/APPROXIMATION/HEURISTIC/EXAM_CONVENTION/SPECIAL_CASE`.
4. Crear una entrada intuitiva o problema motivador de máximo 1 bloque.
5. Mantener una capa `CORE` que permita comprender la idea sin ampliaciones.
6. Añadir `STANDARD` con variaciones y decisiones de método.
7. Añadir `ADVANCED` solo cuando aumenta comprensión/transferencia; no como relleno.
8. Garantizar worked example -> faded example -> práctica independiente para skills procedimentales.
9. Etiquetar ejercicios L1–L5 y skills.
10. Crear misconception check con al menos el error más probable.
11. Regenerar summary desde knowledge_model.
12. Añadir checkpoint al final de cada grupo coherente de 2–5 microlecciones.

### Regla de salida para el alumno con poca base
Nunca debe ser necesario abandonar la plataforma para recuperar un prerrequisito fundamental. Si el concepto previo no existe, crear microlección Foundation reutilizable.

### Regla para excelencia
La ruta Advanced debe contener al menos uno de estos elementos cuando tenga sentido: condición de validez, contraejemplo, comparación de modelos, problema de transferencia, demostración útil o interpretación profunda. No basta con "hacer la misma cuenta con números más feos".

---

## 6. Lecciones que requieren fragmentación/poolización prioritaria

- No hay flags automáticos de longitud extrema. Aun así, dividir cualquier lección que exceda el objetivo de estudio real tras medir interacción/práctica.

### Regla de fragmentación
Una microlección nueva debe tener un objetivo reconocible y poder completarse de forma independiente. No dividir por número de páginas de manera arbitraria. Un buen corte suele ocurrir entre:
- intuición y formalismo;
- dos técnicas distintas;
- definición y aplicación compleja;
- aprendizaje y banco de práctica.

---

## 7. QA estructural detectado

| Severidad | Tipo | Cantidad |
|---|---|---:|
| low | `wrong_option_no_explanation` | 228 |

**Nota:** el CSV de QA del curso contiene las filas exactas. No inflar el documento con 228 distractores repetitivos.


Archivo con todas las filas exactas: `../qa/eso_fisicaquimica_structural_issues.csv`.

---

## 8. Diseño de evaluación del curso

### Diagnóstico inicial
Construir 12–25 ítems que cubran prerrequisitos y skills troncales. No usarlo para poner una etiqueta global al alumno. La salida es un mapa de fortalezas/lagunas.

### Checkpoint de unidad
- 20–30% reconocimiento/comprensión;
- 40–50% aplicación;
- 20–30% transferencia/selección de método;
- al menos un misconception item si el tema tiene error típico fuerte.

Los porcentajes son guía de diseño, ajustables al tipo de asignatura; no deben forzar preguntas artificiales.

### Exam Mode
No incluir hints iniciales. Tras la entrega, clasificar cada fallo por skill y ofrecer enlace de recuperación exacto. Los simulacros no sustituyen los checkpoints de aprendizaje.

---

## 9. Reglas de UI/contenido adaptativo

La lección debe poder renderizar:

- `start_from_zero`: muestra prerequisites, intuición, ejemplos completos y hints.
- `standard`: comprime foundations, muestra Core+Standard y ejercicios L2–L4.
- `excellence`: permite quick-check y salta repetición; muestra condiciones, contraejemplos, L4–L5.
- `quick_review`: summary + 3–6 preguntas; si falla, redirige a bloques concretos.

La ruta es **por unidad/skill**, no una configuración permanente del usuario.

---

## 10. Reglas de migración de ejercicios

- Conservar ejercicios válidos aunque la lección se divida.
- Moverlos a un pool global de curso o unidad si no pertenecen a una única microlección.
- Etiquetar `skills`, `difficulty`, `conceptual_depth`, `cognitive_level`, `official_track` si aplica y `source`.
- Si varios ejercicios son clones numéricos, conservar algunos representativos y parametrizar/generar variantes en vez de obligar a recorrer todos.
- En cada sesión, seleccionar un conjunto pequeño y diverso. Los bancos completos siguen accesibles como práctica adicional.

---

## 11. Definition of Done específica

Este curso no se marca `release_ready` hasta que:

1. todos los P0 de este documento estén cerrados y verificados;
2. todos los P1 estén corregidos o documentados con decisión explícita;
3. no existan referencias/IDs rotos del CSV QA;
4. toda lección ordinaria tenga al menos un ejemplo resuelto o justificación explícita del tipo de lección;
5. los Exercise Banks estén tipados como pools;
6. las macro-lecciones señaladas estén divididas o exista una justificación de interacción que demuestre duración real aceptable;
7. las reglas absolutas estén etiquetadas/condicionadas;
8. summary y assessment no contradigan theory;
9. exista diagnóstico + checkpoints + Exam Mode;
10. sea posible completar el curso por las cuatro rutas sin duplicar cuerpos de conocimiento.


## Reglas de implementación para el agente

1. **Preservar contenido útil**: no reescribir por estilo si ya es correcto y claro. Corregir, atomizar y etiquetar antes que regenerar indiscriminadamente.
2. **No introducir contenido fuera del syllabus por defecto**: una ampliación puede existir, pero debe ir a `ADVANCED` o a una banda curricular separada.
3. **No ocultar contenido obligatorio por la ruta del alumno**: la ruta cambia apoyo/profundidad, no el alcance oficial.
4. **No duplicar conocimiento**: teoría, resumen y preguntas deben referenciar claims canónicos.
5. **Trazabilidad**: toda nueva microlección debe guardar `derived_from` con unidad/lección original.
6. **Orden de corrección**: P0 -> P1 -> estructura -> P2/P3 -> estética.
7. **No borrar ejercicios válidos**: migrarlos a pools y etiquetarlos por skill/dificultad.
8. **Validación antes de commit/release**: schema, referencias, cálculos, semantic lint y render.


---

## 12. Orden exacto de ejecución recomendado

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=eso_fisicaquimica`.
2. Resolver el CSV `qa/eso_fisicaquimica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
