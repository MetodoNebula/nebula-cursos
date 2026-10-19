# Auditoría de reestructuración — Cambridge GCSE/IGCSE — Physics

**Curso ID:** `gcse_ciencias_phys`  
**Unidades actuales:** 10  
**Lecciones actuales:** 62  
**Palabras pedagógicas aproximadas:** 310,944  
**Mediana de palabras/hora declarada:** ~3,252  
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
| `U06_Waves_Light_and_Sound` | 8 | 39.500 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U09_Space_Physics` | 4 | 18.904 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U05_Thermal_Physics` | 7 | 44.859 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U08_Nuclear_Physics` | 6 | 22.839 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U07_Electricity_and_Magnetism` | 13 | 75.705 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U04_Energy_Work_and_Power` | 6 | 26.787 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U10_Revision_and_Exam_Practice` | 1 | 6.930 | CONVERTIR en Exam Mode/pool; no mantener como una lección lineal. |
| `U03_Forces_and_Pressure` | 7 | 28.842 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U01_Measurement_and_Motion` | 6 | 32.420 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |
| `U02_Mass_Weight_and_Density` | 4 | 14.158 | CONSERVAR módulo; convertir cualquier Exercise Bank interno en pool y mantener track oficial separado de ruta pedagógica. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Units, standard form, rearranging equations, graphs and basic vector/scalar language; diagnostic-driven.
2. **01 Measurement and Motion** — Keep U01 but enforce velocity-time vs speed-time distinction.
3. **02 Mass, Weight and Density** — Keep U02; move Exercise Bank to pool.
4. **03 Forces and Pressure** — Keep U03; integrate vector/resultant and model conditions.
5. **04 Energy, Work and Power** — Keep U04; fix stored-energy balance.
6. **05 Thermal Physics** — Keep U05; fix phase-change contradiction.
7. **06 Waves, Light and Sound** — Keep U06; fix wave definition/refraction wording and add longitudinal-friendly definitions.
8. **07 Electricity and Magnetism** — Keep U07; separate changing flux principle from AC exam rule.
9. **08 Nuclear Physics** — Keep U08.
10. **09 Space Physics** — Keep U09; circular vs elliptical orbit scope.
11. **10 Revision / Exam Mode** — U10 becomes exercise pool + generated mixed papers, not a one-lesson unit.


### Reglas pedagógicas específicas de GCSE/IGCSE Physics
- Mantener `official_track` (Core/Extended si aplica) separado de `learning_route`.
- Reforzar command words y mark-scheme language en Exam Mode, no contaminar la explicación conceptual con frases memorizadas sin comprensión.
- Cada practical/graph skill debe aparecer primero guiado y después en pregunta donde el alumno interpreta datos.
- Exercise Banks pasan a pools etiquetados por syllabus code, skill, track y difficulty.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `U05_Thermal_Physics / 03_Melting_boiling_and_evaporation` | Durante meseta se dice que partículas "slow down", contradiciendo T constante. | Tres fases antes/durante/después; durante el cambio no cambia Ec media/T idealmente. | Theory, challenge y summary son consistentes. |
| P1 | `U06_Waves_Light_and_Sound / 01_Wave_quantities_and_types` | Definición de wave exige medium y excluye EM waves. | Definir wave como disturbance/oscillation transferring energy without net matter transport; mechanical waves need medium, EM do not. | MCQ no exige medium para toda wave. |
| P1 | `U01_Measurement_and_Motion / graphs` | Speed-time usado donde se razona aceleración firmada/direccional. | Usar velocity-time cuando el signo/dirección importa; speed-time solo para rapidez. | Los gráficos tienen etiqueta coherente con la magnitud. |
| P1 | `U04_Energy_Work_and_Power` | Balance "energy leaving always equals entered" omite stored energy. | Usar energy in = useful out + wasted out + change in stored energy. | Problemas con acumulación de energía funcionan. |
| P2 | `U09_Space_Physics / orbit` | Gravedad perpendicular al movimiento y speed constante para toda órbita. | Acotar a circular orbit. | Elíptica puede variar speed. |
| P2 | `U06 / wave definitions` | Amplitude/wavelength definidas con vertical/horizontal del dibujo. | Definiciones físicas independientes de la orientación del dibujo y válidas para longitudinales. | Se pueden aplicar a longitudinal waves. |
| P2 | `U06 / refraction` | "denser medium" ambiguo. | Usar optically denser / higher refractive index. | Terminología óptica precisa. |
| P2 | `U06/EM spectrum` | Radio/microwaves "do not harm". | Decir non-ionising, pero alta intensidad puede causar thermal damage. | No se equipara non-ionising con harmless. |
| P2 | `U07 / transformer` | Transformer works with AC, not DC como absoluto. | Explicar que necesita changing magnetic flux; steady DC no mantiene emf, transients/pulses sí varían flujo. | Regla de examen y principio físico ambos presentes. |


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
| `gcse_ciencias_phys__U06_Waves_Light_and_Sound` | `08_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U05_Thermal_Physics` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U08_Nuclear_Physics` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U07_Electricity_and_Magnetism` | `13_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U04_Energy_Work_and_Power` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U10_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U10_Revision_and_Exam_Practice` | `01_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_practice` |  |
| `gcse_ciencias_phys__U03_Forces_and_Pressure` | `07_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U01_Measurement_and_Motion` | `06_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |
| `gcse_ciencias_phys__U02_Mass_Weight_and_Density` | `04_Exercise_Bank_Cambridge_IGCSE.json` | medium | `no_worked_examples` |  |


Archivo con todas las filas exactas: `../qa/gcse_ciencias_phys_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=gcse_ciencias_phys`.
2. Resolver el CSV `qa/gcse_ciencias_phys_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
