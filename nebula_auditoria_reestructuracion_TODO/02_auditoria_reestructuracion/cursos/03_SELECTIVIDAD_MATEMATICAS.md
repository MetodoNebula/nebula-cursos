# Auditoría de reestructuración — Selectividad / PAU — Matemáticas II

**Curso ID:** `selectividad_matematicas`  
**Unidades actuales:** 12  
**Lecciones actuales:** 101  
**Palabras pedagógicas aproximadas:** 544,496  
**Mediana de palabras/hora declarada:** ~3,487  
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
| `mat_limites` | 8 | 42.218 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_distribuciones` | 7 | 26.623 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_determinantes` | 6 | 61.584 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_vectores` | 7 | 37.017 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_integrales` | 12 | 36.968 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_probabilidad` | 10 | 45.808 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_rectas_planos` | 8 | 47.838 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_sistemas` | 7 | 47.708 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_matrices` | 7 | 73.005 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_geometria_metrica` | 7 | 37.120 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_representacion` | 11 | 40.210 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mat_derivadas` | 11 | 48.397 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Álgebra, ecuaciones, trigonometría básica, notación, funciones y manipulación simbólica; recuperación opcional.
2. **01 Cálculo I — Límites y continuidad** — Límite -> laterales -> operaciones -> infinito -> indeterminaciones -> continuidad -> asíntotas.
3. **02 Cálculo II — Derivadas** — Definición/tasa -> reglas -> tangente -> monotonicidad/extremos -> concavidad/inflexión -> optimización.
4. **03 Representación de funciones** — Integrar dominio, límites, derivadas, asíntotas y croquis; problemas de decisión, no solo checklist mecánico.
5. **04 Integración** — Primitivas -> técnicas -> integral definida -> áreas -> aplicaciones.
6. **05 Álgebra lineal** — Matrices -> determinantes -> rango/inversa -> sistemas -> discusión de parámetros.
7. **06 Geometría vectorial y afín** — Vectores -> rectas/planos -> posiciones -> producto escalar/vectorial -> distancias/ángulos/proyecciones.
8. **07 Probabilidad y distribuciones** — Sucesos -> condicionada/independencia -> Bayes/árboles -> variables/distribuciones -> problemas mixtos.
9. **08 PAU integrada** — Sets mixtos y simulacros por perfil de examen.


### Reglas pedagógicas específicas de Matemáticas II
- Cada técnica debe tener cuatro niveles: reconocer estructura -> aplicar -> elegir técnica -> problema mixto.
- No enseñar recetas sin hipótesis (L'Hôpital, inversa, inflexión, etc.).
- Añadir "comprobación" al final de cada worked example: dominio, signo, sustitución, derivación inversa o interpretación geométrica según proceda.
- Representación de funciones debe ser módulo integrador de límites+derivadas, no repetición aislada de reglas.
- En geometría, exigir dibujo/esquema y traducción entre forma vectorial, paramétrica, implícita cuando corresponda.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `mat_probabilidad / 04_Tablas_de_contingencia_y_diagramas_de_árbol / mcq[0]` | Opción correcta calcula x=0,4 pero explanation termina x=0,2. | Unificar correct/why_correct/explanation desde una única solución canónica; x=0,4. | No hay dos resultados distintos en campos del mismo item. |
| P1 | `mat_derivadas / inflexión` | f"(x0)=0 presentada como condición necesaria universal. | Definir inflexión por cambio de concavidad. Usar f"=0 o no existencia como candidatos y comprobar cambio de signo/concavidad. | Contraejemplo o nota impide memorizar f"=0 como equivalencia. |
| P1 | `mat_limites / L'Hôpital` | Receta sin hipótesis. | Añadir recuadro de hipótesis y condición de forma indeterminada real. | No se aplica como identidad algebraica. |
| P2 | `mat_derivadas / tangente vertical` | f'(a)=±∞ tratado como derivada ordinaria. | Hablar de pendiente infinita/límite de derivada; la derivada real finita no existe. | Terminología consistente. |
| P2 | `mat_probabilidad / no equiprobable` | No equiprobable equivale a usar frecuencias. | Distinguir estimación empírica y modelo no equiprobable conocido a priori. | Ejemplos cubren ambas situaciones. |
| P2 | `mat_probabilidad / reemplazamiento` | Con reemplazo implica independencia por definición. | Decir que ocurre en el modelo estándar de extracciones idénticas con reemplazo; independencia es propiedad del modelo conjunto. | No se usa como equivalencia semántica. |
| P2 | `matrices/grafos` | (A^k)ij descrito como caminos simples. | Usar walks/recorridos de longitud k; aclarar que pueden repetirse vértices/aristas. | Terminología de grafos correcta. |


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

_No se detectaron incidencias estructurales automáticas en este curso. Esto no elimina los cambios semánticos del ledger._

Archivo con todas las filas exactas: `../qa/selectividad_matematicas_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_matematicas`.
2. Resolver el CSV `qa/selectividad_matematicas_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
