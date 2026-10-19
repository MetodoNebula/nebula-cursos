# Auditoría de reestructuración — Selectividad / PAU — Química

**Curso ID:** `selectividad_quimica`  
**Unidades actuales:** 9  
**Lecciones actuales:** 127  
**Palabras pedagógicas aproximadas:** 777,156  
**Mediana de palabras/hora declarada:** ~3,767  
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
| `U08_Organica` | 27 | 170.562 | DIVIDIR en 2–3 módulos de navegación (estructura/nomenclatura. isomería. reactividad). |
| `U06_Acido_Base` | 15 | 89.082 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U09_Competencia` | 5 | 34.714 | DISTRIBUIR habilidades transversalmente + conservar módulo final integrador. |
| `U07_Electroquimica` | 14 | 90.940 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U02_Estructura_Atomica` | 12 | 71.923 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U05_Equilibrio` | 19 | 101.877 | DIVIDIR navegación en Cinética + Equilibrio; conservar canonical IDs/derived_from. |
| `U03_Enlace` | 14 | 95.948 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U01_Estequiometria` | 11 | 64.756 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |
| `U04_Termoquimica` | 10 | 57.354 | CONSERVAR orden lógico con microlecciones y rutas adaptativas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Formulación/nomenclatura imprescindible, mol, unidades, proporcionalidad, logaritmos para pH, cifras significativas y lectura de material/gráficas.
2. **01 Estequiometría** — Ecuaciones -> mol/masa -> gases/disoluciones -> limitante -> pureza/rendimiento -> mezcla/dilución -> problemas integrados.
3. **02 Estructura atómica** — Rutherford/Bohr/espectros -> cuantos/fotón -> números cuánticos -> orbitales -> configuración -> periodicidad.
4. **03 Enlace y estructura** — Lewis -> VSEPR -> polaridad -> fuerzas intermoleculares -> sólidos/propiedades -> comparación de modelos.
5. **04 Termoquímica** — Sistema/energía -> 1er principio -> entalpía -> Hess/formación/combustión -> entropía/Gibbs con hipótesis.
6. **05 Cinética** — Velocidad -> colisiones/Ea -> factores -> ley de velocidad al alcance del curso -> catalizadores.
7. **06 Equilibrio químico** — K/Q -> desplazamientos -> Le Châtelier -> solubilidad si aplica -> problemas.
8. **07 Ácido-base** — Teorías -> pH fuerte/débil -> Ka/Kb -> hidrólisis/buffers si están en alcance -> valoraciones/equivalencia.
9. **08 Electroquímica** — Números de oxidación -> ajuste -> pilas/potenciales -> espontaneidad -> electrólisis.
10. **09 Orgánica A: estructura y nomenclatura** — Hidrocarburos -> grupos funcionales -> isomería constitucional/estereoquímica según alcance.
11. **10 Orgánica B: reactividad** — Transformaciones y tipos de reacción por familias; separar reglas generales de casos de examen.
12. **11 Competencia experimental y PAU** — La competencia U09 se distribuye transversalmente y aquí se integra con datos, diseño experimental y simulacros.


### Reglas pedagógicas específicas de Química PAU
- Separar siempre **modelo microscópico**, **ecuación simbólica**, **magnitud macroscópica** y **procedimiento de cálculo**.
- En pH/equilibrio/termoquímica, las aproximaciones deben tener condiciones visibles antes de aplicarse.
- U09 Competencia no puede vivir solo al final: insertar mini-tareas de lectura de datos, material, seguridad y diseño experimental en cada módulo; mantener U09 como integración final.
- U05 Equilibrio (19 lecciones) debe dividirse al menos en **Cinética** y **Equilibrio** para reducir carga y mejorar dependencias.
- U08 Orgánica (27 lecciones) debe dividirse en estructura/nomenclatura, isomería y reactividad; no presentar 27 pasos como una única unidad de navegación.


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P1 | `U06_Acido_Base / H2SO4` | Aproximación 2 H+ por mol reaparece como regla exacta en summaries/flashcards. | Distinguir neutralización completa, cálculo riguroso de pH con Ka2 y convención/aproximación PAU cuando proceda. | Cada claim de H2SO4 lleva scope/assumption explícita. |
| P1 | `U06_Acido_Base / neutralización` | "Ácido + base -> sal + agua" como definición general. | Definir Brønsted como transferencia de protón; sal+agua como caso frecuente con OH-/óxidos. | NH3 funciona como contraejemplo conceptual. |
| P1 | `U06_Acido_Base / equivalencia` | "moles ácido = moles base" sin estequiometría. | Usar equivalentes o relación de coeficientes desde el principio. | Ejercicios 2:1 y polipróticos no inducen igualdad molar simple. |
| P1 | `U04_Termoquimica / estado estándar` | Estado estándar definido como 25 C y 1 atm. | Definir presión estándar moderna como 1 bar; 298.15 K como temperatura habitual de tablas. Si un examen usa 1 atm, etiquetarlo EXAM_CONVENTION. | Summary separa definición universal de convención de problema. |
| P2 | `U04_Termoquimica / Qp=ΔH` | Faltan hipótesis. | Añadir sistema cerrado, presión constante y trabajo pV como único trabajo relevante en el modelo escolar. | Fórmula incluye conditions[]. |
| P2 | `U04_Termoquimica / ΔH=ΔU+ΔngRT` | Faltan hipótesis de gas ideal. | Etiquetar gases ideales/modelo. | Formula scope explícito. |
| P2 | `U04_Termoquimica / T=ΔH/ΔS` | Temperatura umbral presentada exacta. | Marcar aproximación suponiendo ΔH y ΔS constantes con T. | No se etiqueta EXACT. |
| P1 | `U05_Equilibrio / K=k+/k-` | Derivación generalizada indebidamente. | Limitar a reacción reversible elemental con las leyes de velocidad mostradas. | No se usa como derivación general de cualquier K. |
| P2 | `U05_Equilibrio / Kc` | Unidades de Kc tratadas como universales. | Mantener formalismo escolar si se necesita, con nota Advanced de actividades y K termodinámica adimensional. | No crea contradicción con química posterior. |
| P1 | `U08_Organica / estereoquímica` | Criterio cis/trans de alquenos extendido a ciclos. | Separar E/Z de dobles enlaces y cis/trans de ciclos. | Ejercicios clasifican por mecanismo geométrico correcto. |
| P2 | `U08_Organica / enantiómeros` | "Mismas propiedades salvo rotación óptica" sin entorno. | Añadir "en entorno achiral" y nota sobre sistemas quirales. | Scope explícito. |
| P2 | `U08_Organica / halogenación` | "Producto único" ignora estereoisómeros. | Distinguir producto constitucional y posibles estereoisómeros; marcar estereoquímica fuera de alcance si procede. | No usa "único" sin definir el nivel de identidad. |
| P2 | `U08_Organica / CCl4` | Referencia puede parecer recomendación experimental actual. | Presentarlo como referencia histórica o sustituir por descripción de solvente inerte no nucleófilo, con nota de seguridad si se conserva. | No se recomienda manipulación actual sin contexto. |
| P2 | `U03_Enlace / orbital` | Orbital igualado a región de probabilidad. | Definir orbital como función de onda; \|psi\|² da densidad de probabilidad. Simplificación visual puede quedar como modelo. | Definición formal y visual no se confunden. |
| P2 | `U03_Enlace / puente de hidrógeno` | "Interacción intermolecular más intensa" universal. | Reformular como tendencia en especies comparables. | No aparece superlativo universal. |
| P2 | `U02_Estructura_Atomica / Madelung` | Regla tratada como orden exacto con solo Cr/Cu como excepciones. | Etiquetar como guía de llenado útil para el nivel y no ley universal. | Claim marcado MODEL/HEURISTIC. |
| P0 | `U09_Competencia / 04_Resolución... / worked_examples[0]` | Redondeo inconsistente: 30,0-27,6 se muestra como 2,44. | Conservar cifras internas y mostrar 27,56 -> 2,44, o usar 27,6 -> 2,4. Introducir regla de cifras de guarda y redondeo final. | Las operaciones visibles son aritméticamente consistentes. |


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

Archivo con todas las filas exactas: `../qa/selectividad_quimica_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_quimica`.
2. Resolver el CSV `qa/selectividad_quimica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
