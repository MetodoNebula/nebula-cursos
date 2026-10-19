# Auditoría de reestructuración — Selectividad / PAU — Física

**Curso ID:** `selectividad_fisica`  
**Unidades actuales:** 8  
**Lecciones actuales:** 76  
**Palabras pedagógicas aproximadas:** 1,045,039  
**Mediana de palabras/hora declarada:** ~6,862  
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
| `ondas` | 12 | 166.360 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `optica` | 11 | 149.374 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `nuclear` | 10 | 127.701 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `mas` | 7 | 94.259 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `campo_gravitatorio` | 9 | 135.040 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `cuantica` | 6 | 85.328 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `relatividad` | 7 | 100.537 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |
| `electromagnetismo` | 14 | 186.440 | CONSERVAR como módulo canónico. aplicando atomización/correcciones indicadas. |


### Interpretación
- **CONSERVAR** no significa dejar igual: significa conservar el contenido como fuente, pero migrarlo al modelo canónico y a la plantilla atómica.
- **MOVER/DIVIDIR/CONVERTIR** debe mantener `derived_from` para trazabilidad.
- Los bancos de ejercicios no cuentan como lección pedagógica lineal.

---

## 3. Arquitectura objetivo del curso

1. **00 Foundations** — Vectores, trigonometría, despeje algebraico, notación científica, unidades SI, lectura de gráficas y conservación de energía. Solo aparece cuando el diagnóstico detecta carencias.
2. **01 Campo gravitatorio** — Kepler -> gravitación -> campo/potencial -> energía -> órbitas/satélites -> problemas mixtos.
3. **02 Movimiento armónico simple** — Oscilación general -> MAS ideal -> x/v/a -> energía -> resolución de condiciones iniciales -> péndulo/muelle dentro del modelo.
4. **03 Ondas y sonido** — Concepto de onda -> magnitudes -> ecuación -> fase -> superposición/interferencia -> estacionarias -> sonido/dB.
5. **04 Electromagnetismo** — Coulomb/campo -> potencial/energía -> corriente/circuitos si están en alcance -> magnetismo -> fuerza de Lorentz -> flujo/Faraday-Lenz -> aplicaciones.
6. **05 Óptica** — Propagación -> índice/Snell -> TIR -> óptica geométrica -> lentes/espejos -> instrumentos/problemas.
7. **06 Relatividad** — Postulados SR -> simultaneidad -> dilatación/contracción -> transformaciones/energía si están en alcance -> equivalencia local/GR al nivel del curso.
8. **07 Física cuántica** — Planck/fotón -> fotoeléctrico -> Bohr/espectros -> de Broglie -> incertidumbre y límites del modelo.
9. **08 Física nuclear** — Núcleo -> energía de enlace -> estabilidad -> desintegración -> actividad/semivida -> reacciones/fisión/fusión.
10. **09 PAU integrada** — Problemas mixtos, selección de estrategia, simulacros y análisis de errores.


### Reglas pedagógicas específicas de Física PAU
- Cada ley/fórmula debe mostrar **sistema, hipótesis, signos, unidades y límite de validez**.
- Toda lección procedimental termina con al menos un problema en el que el alumno deba **elegir la ley**, no se le diga cuál usar.
- Diagramas de cuerpo libre, campos, rayos y ondas son parte del razonamiento, no decoración.
- La capa Advanced prioriza contraejemplos y cambio de modelo, no matemáticas universitarias gratuitas.
- Las derivaciones largas solo se mantienen si ayudan a reconstruir una fórmula o son examinables; si no, van a Advanced/"por qué funciona".


---

## 4. Cambios semánticos/técnicos obligatorios

| Prioridad | Ruta/ámbito | Problema | Cambio obligatorio | Criterio de aceptación |
|---|---|---|---|---|
| P0 | `electromagnetismo / 12_El_flujo_magnético_y_qué_induce_corriente` | Inducción presentada como existente solo con movimiento relativo. | Reescribir objetivos, teoría, ejemplos, MCQ, flashcards y summary alrededor de dΦ_B/dt != 0. Presentar movimiento relativo como una de varias formas de variar el flujo. Incluir ejemplo de espira fija con B(t) o transformador. | Ninguna pieza afirma que el movimiento sea condición necesaria; todas las evaluaciones aceptan flujo variable sin movimiento. |
| P0 | `cuantica / 06_Indeterminación_y_la_nueva_mecánica_cuántica` | Criterio dimensional usado como condición suficiente para decidir pares conjugados, contradiciendo la propia teoría. | Usar dimensiones solo como filtro negativo. Para afirmar conjugación, limitarse a pares estudiados o explicar conceptualmente la relación canónica/conmutador. Propagar el cambio a objectives, worked examples, MCQ y summary. | No existe ninguna pregunta que acepte "mismas dimensiones de acción => conjugadas" como criterio suficiente. |
| P1 | `campo_gravitatorio / conservación de energía` | "El rozamiento siempre realiza trabajo negativo". | Acotar al modelo habitual de rozamiento cinético sobre superficie fija. Añadir contraejemplo breve (cinta transportadora) solo en Advanced/nota de alcance. | Toda aparición de "siempre" queda condicionada al modelo. |
| P2 | `campo_gravitatorio / Kepler` | Tercera ley expresada solo con r. | Usar T²/a³ como formulación general y aclarar que en órbita circular a=r. | Resumen y ejercicios distinguen órbita circular de elíptica. |
| P2 | `campo_gravitatorio / caída` | a=g sin explicitar caída libre. | Añadir "si la gravedad es la única fuerza relevante". | No se identifica g con aceleración neta cuando hay otras fuerzas. |
| P2 | `campo_gravitatorio / g máxima` | g máxima en superficie formulado universalmente. | Etiquetar como propiedad del modelo esférico ideal utilizado. | Claim marcado MODEL y no EXACT. |
| P2 | `mas / varias lecciones` | Propiedades del MAS ideal presentadas como propiedades de toda oscilación. | Introducir categoría oscilación y después MAS como modelo especial. Etiquetar independencia del periodo respecto a amplitud y envolvente exponencial con sus hipótesis. | Summary distingue oscilación general de MAS ideal. |
| P1 | `electromagnetismo / 06_El_campo_magnético_un_campo_sin_fuentes` | Negación global de potencial/energía potencial magnética. | Decir que no se usa un potencial escalar de posición análogo al eléctrico para una carga móvil. Añadir nota Advanced: potencial vector A y U=-mu·B para dipolos. | No aparece "no existe potencial magnético" de forma absoluta. |
| P1 | `electromagnetismo / dieléctricos` | Polarización descrita siempre en sentido contrario a E. | Separar vector polarización P (alineado con E en dieléctrico lineal ordinario) del campo de despolarización debido a cargas ligadas. | Diagramas y texto muestran correctamente P y campo de despolarización. |
| P2 | `electromagnetismo / solenoide` | Campo uniforme en todo el interior. | Cambiar a "aproximadamente uniforme lejos de extremos para solenoide largo". | Fórmula B=mu n I marcada APPROX/MODEL con condiciones. |
| P2 | `ondas / intensidad` | Relación intensidad-amplitud demasiado vaga. | Indicar I proporcional a A² bajo condiciones comparables. | Flashcard y MCQ no reducen la relación a mera correspondencia. |
| P2 | `ondas / decibelios` | "Los decibelios no se suman". | Explicar que los niveles en dB no se suman aritméticamente; se suman intensidades/potencias y se transforma. | Ejemplo de dos fuentes idénticas usa suma de intensidades. |
| P2 | `ondas / estacionarias` | Explicación débil de ausencia de transporte neto. | Explicar superposición de ondas viajeras opuestas y cancelación del flujo medio de energía. | Summary usa superposición, no "el nodo no puede hacer trabajo" como razón principal. |
| P2 | `ondas / tubos` | Nodos/antinodos sin indicar magnitud. | Especificar desplazamiento o presión en cada dibujo y regla. | Todos los esquemas etiquetan la magnitud. |
| P2 | `optica / varias lecciones` | Idealizaciones ópticas redactadas como universales. | Etiquetar n>=1, TIR perfecta y formación puntual de imagen como modelos de óptica geométrica/medios ordinarios/interfaz ideal. | Claims absolutos reciben etiqueta de alcance. |
| P1 | `relatividad / introducción a GR` | Motivación incorrecta: "como todos aceleran no existen sistemas inerciales y SR no sirve". | Reescribir: SR no incorpora gravitación como geometría dinámica; equivalencia local conduce a curvatura y mareas. SR sigue siendo válida localmente y puede describir observadores acelerados. | No se afirma que SR sea inútil por inexistencia de marcos inerciales. |
| P2 | `relatividad / equivalencia` | Falta "localmente". | Añadir localmente desde la primera definición y distinguir efectos de marea. | El principio de equivalencia nunca se formula globalmente. |
| P2 | `relatividad / tiempo propio` | Definición imprecisa. | Definir dos eventos sobre la misma línea de universo y reloj comóvil. | La definición no habla de "un evento en reposo". |
| P1 | `nuclear / energía de enlace` | Máximo exacto atribuido a Fe-56. | Hablar de región hierro-níquel; mencionar Ni-62 como referencia de mayor E/A y Fe-56 como muy cercano/relevante. | No se presenta Fe-56 como máximo exacto universal. |
| P1 | `nuclear / estabilidad` | Regla Z>83 inconsistente con estabilidad estricta. | Reformular regla práctica y tratar explícitamente Bi-209 si se habla de estabilidad estricta. | No hay contradicción entre tabla y regla verbal. |
| P2 | `cuantica / producción de pares` | Umbral 2mc² sin recoil. | Marcar 2mc² como umbral ideal y desprecio del retroceso nuclear a este nivel. | Claim marcado MODEL/APPROX. |
| P2 | `cuantica / de Broglie` | lambda=h/mv como fórmula fundamental. | Usar lambda=h/p; h/mv solo aproximación no relativista. | Formula canonical = h/p. |


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

- `selectividad_fisica__ondas / 05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json` — 13830 words / 1.5 h = 9220 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__ondas / 11_Ondas_estacionarias_la_onda_que_no_viaja.json` — 18306 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__optica / 03_El_ángulo_límite_y_la_reflexión_total.json` — 13725 words / 1.5 h = 9150 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__campo_gravitatorio / 02_La_ley_de_gravitación_universal.json` — 18070 words / 2 h = 9035 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__cuantica / 06_Indeterminación_y_la_nueva_mecánica_cuántica.json` — 14633 words / 1.5 h = 9755 words/h: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.
- `selectividad_fisica__electromagnetismo / 05_El_potencial_eléctrico_sumar_sin_vectores.json` — 20190 words: dividir en concepto/intuición, formalización, ejemplo, práctica y transferencia; si es Exercise Bank, convertir directamente en pool.

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
| `selectividad_fisica__ondas` | `05_Diferencia_de_fase_puntos_en_fase_y_en_oposición.json` | medium | `content_overload` | 13830 words / 1.5 h = 9220 words/h |
| `selectividad_fisica__ondas` | `11_Ondas_estacionarias_la_onda_que_no_viaja.json` | high | `very_long_lesson` | 18306 words |
| `selectividad_fisica__optica` | `03_El_ángulo_límite_y_la_reflexión_total.json` | medium | `content_overload` | 13725 words / 1.5 h = 9150 words/h |
| `selectividad_fisica__campo_gravitatorio` | `02_La_ley_de_gravitación_universal.json` | medium | `content_overload` | 18070 words / 2 h = 9035 words/h |
| `selectividad_fisica__campo_gravitatorio` | `02_La_ley_de_gravitación_universal.json` | high | `very_long_lesson` | 18070 words |
| `selectividad_fisica__cuantica` | `06_Indeterminación_y_la_nueva_mecánica_cuántica.json` | medium | `content_overload` | 14633 words / 1.5 h = 9755 words/h |
| `selectividad_fisica__electromagnetismo` | `05_El_potencial_eléctrico_sumar_sin_vectores.json` | high | `very_long_lesson` | 20190 words |


Archivo con todas las filas exactas: `../qa/selectividad_fisica_structural_issues.csv`.

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

1. Ejecutar `semantic_change_ledger.csv` filtrando `course=selectividad_fisica`.
2. Resolver el CSV `qa/selectividad_fisica_structural_issues.csv`.
3. Asignar canonical IDs y knowledge claims.
4. Aplicar la arquitectura de la sección 3.
5. Fragmentar/poolizar la sección 6.
6. Crear prerrequisitos/Foundations.
7. Regenerar summaries/flashcards/MCQ desde claims.
8. Etiquetar y redistribuir ejercicios.
9. Crear diagnósticos/checkpoints/exam mode.
10. Ejecutar QA y comparar cobertura antes/después para confirmar que no se perdió contenido curricular válido.
