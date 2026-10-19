# Auditoría de reestructuración — Cambridge GCSE/IGCSE — Chemistry

**Curso ID:** `gcse_ciencias_chem`  
**Unidades actuales:** 13  
**Lecciones actuales:** 70  
**Palabras pedagógicas aproximadas:** 356,803  
**Mediana de palabras/hora declarada:** ~3,339  
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
| `U04_Electrochemistry` | 5 | 25.620 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U11_Organic_Chemistry` | 8 | 31.016 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U07_Acids_Bases_and_Salts` | 5 | 36.750 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U08_The_Periodic_Table` | 5 | 22.482 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U03_Formulas_and_Amounts` | 6 | 28.468 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U10_Environmental_Chemistry` | 5 | 28.831 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U12_Experimental_Methods_and_Analysis` | 7 | 41.219 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U09_Metals` | 6 | 31.478 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U01_States_of_Matter` | 6 | 29.659 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U05_Chemical_Energetics` | 4 | 14.532 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U13_Revision_and_Exam_Practice` | 1 | 10.914 | CONVERTIR en Exam Mode/pool; no mantener como una lección lineal. |
| `U02_Atoms_Elements_and_Bonding` | 7 | 29.059 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U06_Chemical_Reactions` | 5 | 26.775 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Particle model vocabulary, formulae, balancing, units, proportional reasoning and practical measurement.
2. **01 States of Matter** — Keep U01; ensure model/experiment distinction.
3. **02 Atoms, Elements and Bonding** — Keep U02.
4. **03 Formulae and Amounts** — Keep U03; worked-example ladder for mole/ratio.
5. **04 Electrochemistry** — Keep U04.
6. **05 Chemical Energetics** — Keep U05; definition vs calorimeter evidence.
7. **06 Chemical Reactions** — Keep U06.
8. **07 Acids, Bases and Salts** — Keep U07; broaden base definition and scope pH/neutralisation claims.
9. **08 Periodic Table** — Keep U08.
10. **09 Metals** — Keep U09.
11. **10 Environmental Chemistry** — Keep U10.
12. **11 Organic Chemistry** — Keep U11; split long sequences if a lesson exceeds atomic target.
13. **12 Experimental Methods and Analysis** — Keep U12 and use it as cross-link target from all practical claims.
14. **13 Revision / Exam Mode** — U13 becomes tagged pool and mixed-paper generator, not ordinary lesson.


### Reglas pedagógicas específicas de GCSE/IGCSE Chemistry
- Mantener `official_track` separado de profundidad del alumno.
- Al pasar del modelo de partículas a enlace/reacción, usar representaciones múltiples: partículas/iones -> fórmula -> ecuación -> observación macroscópica.
- Practical methods deben enlazarse desde las unidades conceptuales; no quedar aislados en U12.
- Todos los Exercise Banks son pools, no lecciones ordinarias.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `U07_Acids_Bases_and_Salts` | Base definida como cualquier metal oxide/hydroxide. | Decir common bases include metal oxides/hydroxides; definición del nivel debe incluir bases como NH3. | NH3 no contradice la definición. |
| P2 | `U07 / pH` | pH 0-14 como límite universal. | Etiquetar rango típico para aqueous dilute solutions near room temperature. | No se presenta como límite físico absoluto. |
| P2 | `U07 / neutralisation` | Neutralisation always salt + water. | Acotar a acid + hydroxide/oxide; no todas las bases generan agua. | Ejemplo NH3 no rompe la regla. |
| P2 | `U05_Chemical_Energetics` | Exo/endo decidido solo por observed ΔT. | Definir por energy transfer/enthalpy; ΔT es evidencia experimental bajo condiciones controladas y puede sufrir heat loss. | Teoría distingue definición y observación. |


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
| `gcse_ciencias_chem__U04_Electrochemistry` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U11_Organic_Chemistry` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U07_Acids_Bases_and_Salts` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U08_The_Periodic_Table` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U03_Formulas_and_Amounts` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U10_Environmental_Chemistry` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U12_Experimental_Methods_and_Analysis` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U09_Metals` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U01_States_of_Matter` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U05_Chemical_Energetics` | `04_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U13_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U13_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_practice` |  |
| `gcse_ciencias_chem__U02_Atoms_Elements_and_Bonding` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_chem__U06_Chemical_Reactions` | `05_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |


Archivo con todas las filas exactas: `../qa/gcse_ciencias_chem_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=gcse_ciencias_chem`.
2. Resolver el CSV `qa/gcse_ciencias_chem_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
