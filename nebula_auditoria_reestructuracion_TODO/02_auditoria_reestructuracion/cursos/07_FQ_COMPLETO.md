# Auditoría de reestructuración — Física y Química — corpus completo ESO / 4.º ESO / 1.º Bachillerato

**Curso ID:** `fq_completo`  
**Unidades actuales:** 22  
**Lecciones actuales:** 143  
**Palabras pedagógicas aproximadas:** 501,685  
**Mediana de palabras/hora declarada:** ~2,250  
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
| `U-4Q-03` | 6 | 18.220 | RUTA 4ESO Química. |
| `U-ESO-04` | 5 | 18.179 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-B1F-03` | 8 | 20.310 | RUTA 1Bach Física. |
| `U-B1Q-01` | 7 | 23.139 | RUTA 1Bach Química. |
| `U-B1F-01` | 8 | 28.897 | RUTA 1Bach Física. |
| `U-ESO-01` | 4 | 17.149 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-B1Q-03` | 8 | 25.790 | RUTA 1Bach Química. |
| `U-4F-01` | 6 | 27.280 | RUTA 4ESO Física. |
| `U-4Q-02` | 7 | 21.962 | RUTA 4ESO Química. |
| `U-ESO-02` | 5 | 17.533 | NO DUPLICAR: referenciar lección canónica de Foundations. |
| `U-4Q-04` | 8 | 36.473 | RUTA 4ESO Química. |
| `U-4Q-06` | 6 | 17.734 | RUTA 4ESO Química. |
| `U-4F-03` | 5 | 18.890 | RUTA 4ESO Física. |
| `U-4F-04` | 7 | 24.385 | RUTA 4ESO Física. |
| `U-4Q-05` | 5 | 13.214 | RUTA 4ESO Química. |
| `U-4Q-01` | 6 | 30.818 | RUTA 4ESO Química. |
| `U-B1Q-05` | 7 | 24.399 | RUTA 1Bach Química. |
| `U-4F-02` | 7 | 26.175 | RUTA 4ESO Física. |
| `U-B1Q-04` | 8 | 24.588 | RUTA 1Bach Química. |
| `U-B1F-02` | 8 | 22.056 | RUTA 1Bach Física. |
| `U-B1Q-02` | 7 | 26.937 | RUTA 1Bach Química. |
| `U-ESO-03` | 5 | 17.557 | NO DUPLICAR: referenciar lección canónica de Foundations. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Shared Foundations** — Referenciar de forma canónica U-ESO-01..04; no copiar.
2. **Ruta 4.º ESO Física** — U-4F-01 movimiento -> U-4F-02 fuerzas -> U-4F-03 presión/fluidos -> U-4F-04 energía/calor.
3. **Ruta 4.º ESO Química** — U-4Q-01 enlace -> U-4Q-02 formulación/oxidación -> U-4Q-03 orgánica básica -> U-4Q-04 reacciones -> U-4Q-05 mol -> U-4Q-06 disoluciones/gases.
4. **Ruta 1.º Bach Física** — U-B1F-01 cinemática/vectorial -> U-B1F-02 dinámica -> U-B1F-03 trabajo/energía.
5. **Ruta 1.º Bach Química** — U-B1Q-01 estructura/periodicidad -> U-B1Q-02 enlace -> U-B1Q-03 mol/gases -> U-B1Q-04 estequiometría -> U-B1Q-05 orgánica.
6. **Exam/competency adapters** — Cada ruta tiene sus checkpoints y bancos; el meta-corpus no se presenta al alumno como una lista única de 143 lecciones.


### Regla estructural principal de FQ completo
No exponer "FQ completo" como un curso lineal. Debe ser un **content graph/meta-corpus** del que se construyen rutas por etapa. El alumno elige/recibe una ruta (Foundations, 4ESO Física, 4ESO Química, 1Bach Física, 1Bach Química), y las dependencias cruzadas se resuelven por prerequisitos.

- `U-ESO-*` se comparte por referencia con el curso Foundations.
- Un cambio en una lección canónica debe reflejarse en todas las rutas automáticamente.
- Si se pretende vender cada ruta como "curso completo" de etapa, ejecutar además auditoría de cobertura contra el syllabus oficial correspondiente; este documento solo garantiza reestructuración del contenido existente.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U-B1Q-04 / lesson_01` | Al menos dos opciones correctas contienen why_wrong. | Validar opción correcta: why_wrong nulo y why_correct compatible. | Schema CI bloquea cualquier correct_option_marked_wrong. |
| P0 | `U-ESO-*` | Duplica contenido de eso_fisicaquimica. | Usar misma fuente canónica compartida; este corpus referencia/compone Foundations, no copia. | Hashes/bodies canónicos únicos. |
| P2 | `U-B1Q-02 / polaridad/enlace` | Umbrales Δχ 0,4 y 1,7 como fronteras físicas exactas. | Etiquetar regla orientativa del curso. | Claim HEURISTIC. |
| P2 | `U-4Q-01 / enlace iónico` | Transferencia completa metal->no metal como definición universal. | Presentar como modelo introductorio de formación de iones/red. | Claim MODEL. |
| P2 | `enlace / orden` | "Más pares compartidos => siempre más corto y fuerte". | Acotar a comparación del mismo par de átomos/orden de enlace comparable. | No universal. |
| P2 | `energía / eficiencia` | 0<eta<1 siempre. | Permitir eta=0 en límite conceptual y <=1. | Fórmula/rango matemático correcto. |
| P2 | `mecánica / rozamiento` | Rozamiento siempre resta energía. | Mismo alcance que Selectividad Física: modelo típico superficie fija. | No universal. |
| P2 | `summary layer` | Resúmenes genéricos "se entiende relacionando...". | Regenerar resúmenes específicos desde claims. | Cada summary identifica 3-6 ideas específicas de esa lección. |


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

| Unidad | Lección | Severidad | Tipo | Detalle |
|---|---|---|---|---|
| `fq_completo__U-B1Q-04` | `lesson_01.json` | medium | `correct_option_marked_wrong` | MC-L01-01 A: Es la mitad de 44,0 g; resulta de dividir mal la proporción o de un error de cálculo con n=0,250 mol en lugar de 0,500. |
| `fq_completo__U-B1Q-04` | `lesson_01.json` | medium | `correct_option_marked_wrong` | MC-L01-02 B: Correcta: n(H₂)=4,0/2,0=2,0 mol; proporción 2:1 → n(O₂)=1,0 mol; m(O₂)=1,0·32,0=32,0 g. |


Archivo con todas las filas exactas: `../qa/fq_completo_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=fq_completo`.
2. Resolver el CSV `qa/fq_completo_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
