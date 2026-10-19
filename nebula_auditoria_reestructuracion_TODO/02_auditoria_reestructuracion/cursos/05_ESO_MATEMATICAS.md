# Auditoría de reestructuración — ESO — Matemáticas

**Curso ID:** `eso_matematicas`  
**Unidades actuales:** 20  
**Lecciones actuales:** 122  
**Palabras pedagógicas aproximadas:** 600,680  
**Mediana de palabras/hora declarada:** ~4,681  
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
| `mat_trigonometria` | 9 | 51.460 | D ESO CORE / EXTENSION — triángulo rectángulo en Core; circunferencia/identidades/ec. trigonométricas según profundidad. |
| `mat_potencias_raices` | 5 | 25.973 | A FOUNDATIONS / ESO CORE — mantener. graduando radicales avanzados y racionalización según nivel. |
| `mat_numeros_operaciones` | 7 | 34.526 | A FOUNDATIONS — base numérica; obligatoria para alumnos con lagunas y reutilizable como recuperación. |
| `mat_probabilidad` | 7 | 28.218 | E ESO CORE / EXTENSION — sucesos. árboles y Laplace; combinatoria avanzada se etiqueta Extension. |
| `mat_algebra_polinomios` | 5 | 26.346 | B ESO CORE — álgebra y polinomios. |
| `mat_ecuaciones` | 5 | 29.100 | B ESO CORE — progresión 1º/2º grado -> factorizables -> racionales/radicales; partes exponencial/log pueden requerir EXTENSION. |
| `mat_familias_funciones` | 7 | 30.613 | C ESO CORE — lineales/cuadráticas/inversa; exponenciales/log según banda y profundidad. |
| `mat_distribuciones` | 4 | 20.073 | F/G REVIEW — clasificar lesson a lesson; binomial/normal/aproximación pueden ser puente a Bachillerato. |
| `mat_geometria_metrica` | 8 | 39.810 | D ESO CORE — métrica. semejanza. Pitágoras y escalas. |
| `mat_sucesiones` | 6 | 28.277 | F ESO EXTENSION — conservar como ampliación/puente si excede el núcleo de la ruta elegida. |
| `mat_limites_continuidad` | 5 | 26.460 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_proporcionalidad_financiera` | 5 | 24.613 | A FOUNDATIONS / ESO CORE — porcentajes e interés con problemas contextualizados. |
| `mat_geometria_analitica` | 7 | 28.026 | D ESO CORE / EXTENSION — plano cartesiano. vectores y rectas; clasificar partes avanzadas. |
| `mat_funciones_representacion` | 6 | 30.549 | C ESO CORE — lectura. dominio. crecimiento y transformaciones al nivel de etapa. |
| `mat_estadistica_descriptiva` | 5 | 29.670 | E ESO CORE — descripción y lectura crítica. |
| `mat_derivadas` | 7 | 32.582 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_estadistica_bidimensional` | 7 | 31.673 | F ESO EXTENSION — nube/correlación/regresión básica; corregir P0 y evitar sobreformalización. |
| `mat_sistemas_inecuaciones` | 7 | 39.499 | B ESO CORE — etiquetar extensiones como sistemas no lineales/Gauss si exceden la ruta base. |
| `mat_complejos` | 5 | 23.491 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |
| `mat_conicas` | 5 | 19.721 | G BACH_BRIDGE — fuera de ruta ESO por defecto. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **A Foundations** — Números y operaciones -> potencias/raíces -> proporcionalidad/porcentajes -> lenguaje algebraico. Ruta de recuperación y también inicio para alumnos con poca base.
2. **B ESO Core — Álgebra** — Polinomios -> ecuaciones -> sistemas/inecuaciones con progresión de dificultad.
3. **C ESO Core — Funciones** — Concepto/representación -> lineales/cuadráticas/proporcionalidad inversa -> transformaciones y lectura gráfica.
4. **D ESO Core — Geometría** — Métrica -> semejanza/Pitágoras -> analítica básica -> trigonometría de triángulos y aplicaciones.
5. **E ESO Core — Estadística y probabilidad** — Descriptiva -> probabilidad -> tablas/árboles -> lectura crítica de datos.
6. **F ESO Extension** — Sucesiones, estadística bidimensional/regresión básica, combinatoria y ampliaciones que sí se quieran ofrecer a altas capacidades.
7. **G Bachillerato Bridge** — Complejos, cónicas, límites, derivadas y contenidos de distribución/normal que excedan el núcleo ESO. Nunca en ruta ESO por defecto.


### Regla estructural principal de ESO Matemáticas
El mayor cambio no es de redacción, sino de **taxonomía**. El agente debe añadir `curriculum_band` a todas las unidades/lecciones y reconstruir la navegación. Un alumno que elija ESO Core no debe ver complejos, cónicas, límites o derivadas como continuación obligatoria.

### Regla de accesibilidad
- Cada lección Core debe poder resolverse con prerrequisitos enlazados dentro de Foundations.
- Evitar introducir formalismo de Bachillerato para explicar un concepto ESO si existe una explicación gráfica/intuitiva suficiente.
- La ruta Excellence puede abrir contenido F/G, pero debe indicar claramente "ampliación" o "puente a Bachillerato".


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `mat_estadistica_bidimensional / 03_Regresión_lineal_básica_interpretar_y_predecir / mcq[1]` | 1,1·3+3,2 se calcula como 6,7; correcto 6,5; residuo 0,5 y ninguna opción lo ofrece. | Cambiar datos/opciones para que exista una única respuesta correcta. Si se conservan datos, respuesta=0,5. | Evaluador numérico confirma opción y explicación. |
| P1 | `catálogo completo` | Mezcla ESO core con complejos, cónicas, límites, derivadas y normal/binomial avanzada como una secuencia homogénea. | Separar curriculum_band: ESO_FOUNDATION, ESO_CORE, ESO_EXTENSION y BACH_BRIDGE. La ruta por defecto nunca incluye BACH_BRIDGE. | Un alumno "ESO" no recibe contenido Bachillerato salvo elección/diagnóstico explícito. |
| P1 | `funciones / inversa` | Algoritmo intercambiar x/y sin comprobar inyectividad. | Comprobar one-to-one/injectiva o restringir dominio antes de construir inversa. | Ejemplos incluyen una función que requiere restricción de dominio. |
| P2 | `estadística descriptiva / cuartiles` | Una convención de cuartiles presentada como única. | Declarar convención del curso/examen/calculadora. | Los resultados se interpretan según convención declarada. |
| P2 | `estadística bidimensional / R²` | 0<=R²<=1 universal. | Acotar a OLS estándar con intercepto; nota Advanced sobre modelos sin intercepto. | Claim no universal. |
| P1 | `mat_ecuaciones / 05_Ecuaciones_exponenciales_y_logarítmicas_básicas` | 7 IDs duplicados dentro de la lección. | Regenerar IDs deterministas únicos y actualizar referencias. | Validador unique IDs pasa sin colisiones. |


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
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | TH-0505-5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-6 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | WE-0505-7 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S5 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S6 x2 |
| `eso_matematicas__mat_ecuaciones` | `05_Ecuaciones_exponenciales_y_logarítmicas_básicas.json` | medium | `duplicate_id_within_lesson` | EX-0505-S7 x2 |


Archivo con todas las filas exactas: `../qa/eso_matematicas_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=eso_matematicas`.
2. Resolver el CSV `qa/eso_matematicas_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
