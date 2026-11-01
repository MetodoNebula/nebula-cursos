# Auditoría cualitativa independiente — GCSE Chemistry

**Curso auditado:** `gcse_ciencias_chem`  
**Fecha:** 31 de octubre de 2026  
**Alcance:** auditoría de la versión presente en `bundles/gcse_ciencias_chem__*.json`. No se ha modificado ningún paquete, catálogo ni contenido docente.

## Dictamen ejecutivo

**Perspectiva docente: 8,2/10. Perspectiva del alumno: 7,9/10.** El curso tiene una arquitectura muy sólida: cada lección nuclear suele presentar objetivos, prerrequisitos, diagnóstico, secuencia explícita de teoría, ejemplos resueltos, práctica guiada, práctica independiente, preguntas de examen, recuperación y tratamiento de errores. Destacan la precisión de los títulos de bloques teóricos, el uso sistemático de contraejemplos y las transiciones desde el modelo particulado a la explicación causal.

El principal límite no es de cobertura sino de experiencia: las 13 lecciones denominadas *Exercise Bank* son bancos sin objetivo, activación de prerrequisitos, ejemplo o retroalimentación interna; son útiles como práctica acumulativa, pero no son lecciones autoexplicativas. La unidad de revisión recupera contenido valioso, aunque varias de sus lecciones sustituyen práctica guiada por lectura/flashcards. Se recomienda situar cada banco después de una pauta de selección, autocorrección y reenseñanza, y añadir una ruta de repaso diagnóstico antes del examen final.

## Rúbrica y evidencia revisada

Las dos notas no son una media de conteos. La perspectiva docente valora alineación, secuenciación, evaluabilidad, precisión disciplinar y posibilidades de intervención; la del alumno valora claridad, autonomía, carga cognitiva, práctica con feedback y legibilidad. En cada lección se han contrastado objetivos, prerrequisitos, ítems diagnósticos, bloques teóricos, ejemplos, ejercicios guiados e independientes, preguntas de examen, MCQ, flashcards, errores frecuentes, notas de examen y activos.

La progresión se juzga por dependencia conceptual entre bloques; la carga cognitiva por el número y novedad de ideas que se introducen a la vez, el andamiaje visible y la práctica inmediata. Una nota menor en un banco de ejercicios expresa ausencia de estructura pedagógica interna, no una valoración del valor de practicar.

### Revisión técnica y visual de figuras

Se localizaron 93 SVG incorporados al contenido. Los 93 son XML válido y los 93 declaran `viewBox`, anchura y altura, por lo que no hay evidencia estructural de SVG roto, viewport ausente o recorte inevitable. Se revisó además la coherencia de los activos con su bloque: partículas/estados, enlaces, cantidades, energía, reactividad, orgánica y análisis usan diagramas ligados a la explicación, no decoración aislada. Los lienzos tienen dimensiones diversas; los más anchos requieren prueba responsiva en móvil.

No fue posible abrir una superficie de navegador en esta ejecución para inspeccionar píxel a píxel el *layout* final, de modo que esta parte certifica integridad y riesgo bajo de recorte desde la fuente, **no** una garantía visual absoluta de ausencia de solapamientos CSS. Antes de publicar cambios de interfaz, conviene abrir al menos una figura ancha, una alta y una con etiquetas densas a 320 px, 768 px y escritorio; no es necesario modificar el curso para hacerlo.

## Evaluación bloque por bloque y lección por lección

### U00 — Foundations

**Bloque: Docente 8,5 / Alumno 8,2.** El orden átomos → tabla → fórmulas → ecuaciones → conservación → mol establece los prerrequisitos correctos para cantidad de sustancia. El salto al mol llega pronto, pero se amortigua con ejemplos y práctica. Seguridad se sitúa como fundamento transversal aunque pedagógicamente convendría enlazarla de nuevo antes de las prácticas posteriores.

- **L00-01 — Atoms, elements and compounds — the basics. Docente 8,5 / Alumno 8,5.** Empieza con modelos y distinciones esenciales, incluye tres ejercicios guiados y seis de práctica; los cuatro diagramas sostienen la lectura de partículas. Faltan diagnóstico y prerrequisitos explícitos, razonable sólo por ser la puerta de entrada.
- **L00-02 — Reading the periodic table. Docente 8,5 / Alumno 8,2.** Dos diagnósticos detectan lectura de la tabla antes de grupos, períodos y masa/número atómico; la secuencia alivia confusiones habituales. Requiere verificar que el alumno domine la notación antes de usarla en enlaces.
- **L00-03 — Chemical formulas and equations. Docente 8,4 / Alumno 8,1.** Va de leer fórmula a ecuación y conteo de átomos con práctica guiada abundante; buena preparación para conservación. La densidad de símbolos puede cargar a alumnado con álgebra débil, aunque los ejemplos la mitigan.
- **L00-04 — Balancing chemical equations. Docente 8,6 / Alumno 8,2.** Explicita conservación y ofrece un método paso a paso más un ejemplo Fe/O2/Fe2O3; excelente puente entre comprensión y algoritmo. La práctica debe exigirse sin mirar el procedimiento para comprobar transferencia.
- **L00-05 — The mole concept — an introduction. Docente 8,1 / Alumno 7,7.** Tiene diagnóstico, tres ejemplos y la fórmula masa/moles, pero introduce una abstracción de alta carga antes de la unidad cuantitativa. Es un anticipo útil si se trata como familiarización, no como dominio definitivo.
- **L00-06 — Laboratory equipment and safety. Docente 8,3 / Alumno 8,3.** Elige material por función y conecta peligro con precaución, con diagramas y práctica suficiente. Ganaría transferencia si cada unidad experimental remitiera de manera visible a esta lección.

### U01 — States of Matter

**Bloque: Docente 8,8 / Alumno 8,6.** Progresión modélica muy limpia: propiedades observables, cambios de estado, curvas, presión/volumen y difusión. Los diagnósticos y los diagramas permiten que el alumno conecte macro y micro; la curva de calentamiento exige sostener simultáneamente energía, temperatura y estado.

- **CHEM-U01-L01 — A particle model for solids, liquids and gases. Docente 9,0 / Alumno 8,8.** Diferencia observación y modelo, mantiene el tamaño de partícula y explica compresibilidad; los prerrequisitos y diagnósticos están bien focalizados. La advertencia sobre lo que el diagrama no afirma reduce una fuente importante de ideas erróneas.
- **CHEM-U01-L02 — Why substances change state. Docente 8,8 / Alumno 8,6.** Los cinco cambios, evaporación frente a ebullición y conservación de identidad se encadenan de forma explícita. Cuatro ejemplos dan anclaje, aunque el vocabulario múltiple merece recuperación espaciada.
- **CHEM-U01-L03 — What heating and cooling curves mean. Docente 8,9 / Alumno 8,3.** Lectura por tramos, explicación de meseta y reversibilidad forman una secuencia excelente; tres preguntas de examen miden aplicación. Es cognitivamente densa por coordinar gráfica, energía y partículas: conviene pausa de comprobación entre tramos.
- **CHEM-U01-L04 — Gas volume, temperature and pressure. Docente 8,7 / Alumno 8,4.** Separa con acierto recipiente flexible, rígido y compresión antes de recurrir a colisiones. Cinco bloques y seis prácticas son ricos, pero cuatro objetivos aumentan la carga; la lección requiere ritmo lento.
- **CHEM-U01-L05 — Diffusion and molecular mass. Docente 8,8 / Alumno 8,5.** Distingue movimiento aleatorio de difusión neta y controla la variable “condiciones comparables”. Los ejemplos y práctica guiada hacen visible una inferencia que suele memorizarse sin entender.
- **CHEM-U01-L06 — Exercise Bank. Docente 6,2 / Alumno 5,8.** Nueve ejercicios aportan práctica acumulativa, pero no objetivos, diagnóstico, andamiaje, ejemplo ni feedback visible. Debe presentarse como evaluación/formación dirigida por el profesor, no como aprendizaje autónomo.

### U02 — Atoms, Elements and Bonding

**Bloque: Docente 8,7 / Alumno 8,2.** La unidad avanza de clasificación de materia a estructura atómica, enlace y propiedades, y compara finalmente las estructuras. La progresión es rigurosa; el coste es una elevada densidad de representaciones (símbolos, electrones, diagramas y redes) que demanda comprobaciones frecuentes.

- **CHEM-U02-L01 — Elements, compounds and mixtures. Docente 8,7 / Alumno 8,5.** La pregunta clasificatoria, las definiciones y la separación sin romper enlaces dan un criterio operativo excelente. Los diagramas y seis ejercicios sostienen la transición desde U00.
- **CHEM-U02-L02 — Atomic structure, electrons and isotopes. Docente 8,8 / Alumno 8,1.** Protones/neutrones/electrones, capas e isótopo/ion están bien descompuestos y cuentan con cinco ejemplos. Tres prerrequisitos y cuatro objetivos señalan carga alta: se necesita dominio de cada representación antes de continuar.
- **CHEM-U02-L03 — Ionic bonding and lattice properties. Docente 9,0 / Alumno 8,3.** Va de transferencia electrónica a punto-cruz, red gigante y conductividad según estado; evita tratar un compuesto iónico como una pareja aislada. Seis bloques y tres diagnósticos justifican un ritmo guiado.
- **CHEM-U02-L04 — Covalent molecules and their properties. Docente 8,8 / Alumno 8,2.** Distingue enlaces intra-moleculares y fuerzas entre moléculas, con dobles/triples enlaces y contraejemplos. El alumno necesita comparar de inmediato con iónico para no reducir “covalente” a un dibujo.
- **CHEM-U02-L05 — Giant covalent structures. Docente 8,7 / Alumno 8,4.** Diamond/graphite enlazan estructura, fuerza y uso, con la precisión “débil entre capas, no dentro”. La comparación reduce una concepción errónea muy frecuente.
- **CHEM-U02-L06 — Metallic bonding and structure comparisons. Docente 8,5 / Alumno 8,2.** La comparación de cuatro estructuras y el modelo de electrones deslocalizados producen una buena síntesis. Haría falta una tarea final que fuerce a elegir el modelo adecuado sin pistas.
- **CHEM-U02-L07 — Exercise Bank. Docente 6,2 / Alumno 5,7.** Trece ejercicios son valiosos para consolidar, pero el banco no ofrece explicación, diagnóstico ni secuencia de dificultad. Alto riesgo de practicar errores de enlace si se usa sin corrección.

### U03 — Formulas and Amounts

**Bloque: Docente 8,5 / Alumno 7,8.** Es la progresión cuantitativa más exigente: representación → masas relativas → mol → concentración/volumen → reactivo limitante. La construcción es correcta y muy evaluable, pero conviene que las lecciones de dificultad 3 incluyan recuperación breve de unidades y proporciones antes de los problemas integrados.

- **CHEM-U03-L01 — Formulas and balanced equations. Docente 8,8 / Alumno 8,0.** Siete bloques cubren fórmula, coeficiente/subíndice, balanceo e introducen fórmula iónica; cinco ejemplos ayudan. Su amplitud convierte la lección en un posible cuello de botella: comprobar cada subdestreza por separado.
- **CHEM-U03-L02 — Relative masses and direct proportions. Docente 8,6 / Alumno 7,9.** Relaciona Ar, Mr y ratios desde ecuaciones equilibradas sin presentar el cálculo como magia. La extensión de isótopos es conceptualmente útil, pero debe marcarse como ampliación para no desviar el foco de la proporción.
- **CHEM-U03-L03 — The mole connects mass and particles. Docente 8,6 / Alumno 7,8.** La entidad se nombra explícitamente y n=m/M se trabaja con cuatro ejemplos, una fortaleza didáctica. El alumno puede confundir masa, cantidad y partículas; conviene verbalizar unidades en cada línea de trabajo.
- **CHEM-U03-L04 — Gas volume and concentration. Docente 8,5 / Alumno 7,9.** Distingue g/dm3, mol/dm3 y la conversión cm3/dm3 antes de V=n×24; muy buen control de unidades. Dos ideas cuantitativas en una sola lección reclaman práctica intercalada, no sólo seguida.
- **CHEM-U03-L05 — Limiting reactants and integrated stoichiometry. Docente 8,7 / Alumno 7,6.** El método de seis pasos y la normalización por coeficiente son sólidos y hay tres preguntas de examen. Integra demasiadas decisiones para un principiante; el docente debería fraccionar primero los casos de un solo paso.
- **CHEM-U03-L06 — Exercise Bank. Docente 6,3 / Alumno 5,6.** Dieciséis problemas ofrecen cantidad de práctica, pero sin pistas, criterio de entrada o solución escalonada. Debe acompañarse de clasificación por subhabilidad y corrección comentada.

### U04 — Electrochemistry

**Bloque: Docente 8,6 / Alumno 8,0.** La secuencia móvil de iones → productos → semiecuaciones/electrodos → célula de combustible es conceptualmente coherente y evita reglas aisladas. Requiere cuidar el cambio entre electrólisis y célula, donde signos y flujo de electrones confunden fácilmente.

- **CHEM-U04-L01 — Electrolysis needs mobile ions. Docente 8,8 / Alumno 8,2.** Parte de una observación de conducción, define electrodo/electrolito y corrige la idea de signo fijo. Los diagnósticos y cinco activos permiten construir explicación antes de memorizar términos.
- **CHEM-U04-L02 — Predicting electrode products. Docente 8,8 / Alumno 7,9.** Presenta primero el caso binario, luego agua y reglas acuosas; los ocho bloques y tres prácticas guiadas justifican el nivel 3. La gran cantidad de excepciones potenciales exige un árbol de decisión visible.
- **CHEM-U04-L03 — Charge transfer and copper electrodes. Docente 8,6 / Alumno 7,9.** Contrasta electrodos inertes y activos y vincula observaciones con semiecuaciones. Es una buena lección puente, aunque necesita repaso explícito de oxidación/reducción antes de las semiecuaciones.
- **CHEM-U04-L04 — Hydrogen-oxygen fuel cells. Docente 8,5 / Alumno 8,1.** Aclara que se alimenta la célula y compara beneficios/limitaciones sin simplificar la sostenibilidad. La conexión como inversa de electrólisis es potente si se comprueba que no se invierten indiscriminadamente los signos.
- **CHEM-U04-L05 — Exercise Bank. Docente 6,2 / Alumno 5,6.** Catorce ejercicios son apropiados para consolidar, pero son insuficientes como enseñanza de reglas de productos en electrodos. Requiere clave razonada y agrupación por fundido/acuoso.

### U05 — Chemical Energetics

**Bloque: Docente 8,7 / Alumno 8,2.** La unidad pasa de medición de entorno a perfil energético y cambios de enlace, un orden explicativo fuerte. Los ejemplos cotidianos anclan el fenómeno, mientras que ΔH y Ea demandan precisión de lenguaje, ejes y signos.

- **CHEM-U05-L01 — Thermal energy and reaction surroundings. Docente 8,8 / Alumno 8,4.** Define exotérmica/endotérmica por dirección y separa activación de balance global; cinco ejemplos y seguridad convierten una abstracción en experiencia medible. Muy buena base para el bloque siguiente.
- **CHEM-U05-L02 — Reaction pathways, ΔH and activation energy. Docente 8,9 / Alumno 8,1.** Construye diagrama y lee el eje, en vez de pedir solo reconocimiento; tres diagnósticos y preguntas de examen sostienen evaluación. La simultaneidad de ΔH, Ea, altura y signo hace imprescindible una mini-verificación gráfica.
- **CHEM-U05-L03 — Why bond changes can heat or cool. Docente 8,5 / Alumno 8,1.** El balance entre romper y formar enlaces se formula con precisión y la analogía no reemplaza la explicación. Cinco ejemplos favorecen cálculo/razonamiento, pero debe distinguirse energía de enlace de “energía contenida”.
- **CHEM-U05-L04 — Exercise Bank. Docente 6,0 / Alumno 5,5.** Sólo cuatro ejercicios y ningún andamiaje dejan poca evidencia de progresión o recuperación. Úsese como comprobación breve tras una sesión de práctica guiada adicional.

### U06 — Chemical Reactions

**Bloque: Docente 8,5 / Alumno 8,1.** Se inicia por evidencia y composición, continúa con medida de velocidad, la explica por colisiones y sitúa redox como transferencia. La cadena modelo–medida–explicación es correcta; velocidad y teoría de colisiones deben enseñarse como pareja cercana.

- **CHEM-U06-L01 — Recognising chemical change. Docente 8,5 / Alumno 8,3.** Define por composición y recuerda que la evidencia es una pista, no un veredicto; ese matiz es excelente. Cuatro ejemplos y seis prácticas permiten contrastar casos ambiguos.
- **CHEM-U06-L02 — Measuring rate and testing factors. Docente 8,7 / Alumno 8,0.** Distingue velocidad de total, usa pendiente y prueba justa. Reúne gráfica, cálculo y diseño experimental: conviene alternar una lectura de gráfico con una decisión de variable controlada.
- **CHEM-U06-L03 — Collision theory explains rate. Docente 8,6 / Alumno 8,0.** Cada factor se vincula a frecuencia/energía de colisión y el catalizador no se presenta como “más energía”. La transferencia mejora si el alumno redacta explicaciones completas, no sólo selecciona opciones.
- **CHEM-U06-L04 — Redox is paired oxidation and reduction. Docente 8,6 / Alumno 8,1.** Compara definiciones por oxígeno, electrones y número de oxidación, declarando cuándo cada una falla. Es buen diseño, aunque tres marcos en una sesión justifican recapitulación final comparativa.
- **CHEM-U06-L05 — Exercise Bank. Docente 6,1 / Alumno 5,7.** Seis ejercicios sin modelos ni feedback sirven de comprobación, no de recuperación de colisiones o redox. Acompañar de rúbrica de explicación causal.

### U07 — Acids, Bases and Salts

**Bloque: Docente 8,8 / Alumno 8,2.** La progresión va de carácter químico y neutralización a óxidos, sales solubles e insolubles. Es uno de los bloques mejor articulados para práctica de procedimiento; las lecciones de diez y siete bloques necesitan segmentación explícita.

- **CHEM-U07-L01 — Acids, bases, indicators and neutralisation. Docente 8,8 / Alumno 8,3.** Conecta observables, reacciones de ácido, base/álcali e indicador con neutralización. Cinco MCQ y ejemplos sostienen vocabulario que suele confundirse.
- **CHEM-U07-L02 — Acidic, basic and amphoteric oxides. Docente 8,7 / Alumno 8,0.** Siete bloques y activos contrastan categorías que no deben aprenderse como listas. La idea anfótera aumenta carga: pedir al alumno clasificar con evidencia y ecuación.
- **CHEM-U07-L03 — Making soluble salts. Docente 8,9 / Alumno 8,1.** Diez bloques, ejemplos y preguntas de examen hacen visible la elección de método según reactivo/producto. Es excelente como referencia procedimental, pero larga para una única sesión; pausar después de cada ruta de preparación.
- **CHEM-U07-L04 — Precipitating insoluble salts. Docente 8,7 / Alumno 8,1.** Continúa lógicamente desde solubilidad a precipitación y usa siete activos para sostener pasos y observación. Debe compararse inmediatamente con L03 para que el método no se convierta en receta desconectada.
- **CHEM-U07-L05 — Exercise Bank. Docente 6,2 / Alumno 5,7.** Doce ejercicios ofrecen cobertura, pero carecen de diagnóstico, ejemplos y secuencia de procedimiento. Necesita soluciones que nombren la decisión de método y no sólo el producto.

### U08 — The Periodic Table

**Bloque: Docente 8,5 / Alumno 8,2.** La organización periódica conduce a predicción en grupos I y VII y después a transitorios/gases nobles. Es una secuencia breve y coherente, aunque los patrones electrónicos deben reactivarse de U02 antes de pedir explicaciones de tendencia.

- **CHEM-U08-L01 — Why the table has groups and periods. Docente 8,5 / Alumno 8,3.** Recupera organización y la convierte en explicación de periodicidad, con práctica suficiente. El vínculo con configuración electrónica debe ser visible para evitar que grupo/período sean coordenadas sin significado.
- **CHEM-U08-L02 — Group I: properties and prediction. Docente 8,6 / Alumno 8,2.** Observación, tendencia y seguridad de demostración se combinan con cuidado. Separa propiedades y predicción de una reacción peligrosa, una buena decisión de formato.
- **CHEM-U08-L03 — Group VII: appearance, trend and displacement. Docente 8,7 / Alumno 8,0.** Distingue molécula/ion y enseña desplazamiento en tres representaciones, con examen integrado. El alumnado necesita tabla-resumen para no mezclar reactividad, color y estado.
- **CHEM-U08-L04 — Transition elements and noble gases. Docente 8,3 / Alumno 8,1.** Contrasta rasgos en vez de afirmar que todo metal es como sodio; la parte de capa completa es clara. La amplitud de “transición” conviene limitarla al nivel curricular para no introducir excepciones innecesarias.
- **CHEM-U08-L05 — Exercise Bank. Docente 6,1 / Alumno 5,8.** Siete ejercicios sin apoyo son una práctica útil pero poco diagnóstica. Ordenarlos por grupo y tipo de predicción reduciría ensayo/error.

### U09 — Metals

**Bloque: Docente 8,6 / Alumno 8,2.** Propiedades y usos llevan a aleaciones, reactividad, corrosión y extracción: la unidad une estructura, decisión de material y química industrial. El enlace con redox/electroquímica está presente pero debe hacerse explícito para maximizar transferencia.

- **CHEM-U09-L01 — Metal properties determine uses. Docente 8,5 / Alumno 8,3.** Enseña que un uso es un compromiso de propiedades y no una asociación de memoria. La comparación metal/no metal y seis prácticas sostienen decisiones justificadas.
- **CHEM-U09-L02 — Alloys improve useful properties. Docente 8,5 / Alumno 8,2.** El modelo de átomos de tamaño distinto explica dureza sin sacrificar precisión de “mezcla”. Buen uso de diagramas; pedir explicación de deformación consolidaría el mecanismo.
- **CHEM-U09-L03 — Reactivity and displacement. Docente 8,8 / Alumno 8,1.** Pasa de evidencia experimental a serie, ecuaciones, electrones y predicción; muy buena progresión. Seis bloques y tres representaciones implican carga elevada y merecen práctica discriminada antes de predecir.
- **CHEM-U09-L04 — Corrosion and protection. Docente 8,6 / Alumno 8,3.** La necesidad simultánea de agua y oxígeno y la distinción barrera/sacrificial están especialmente claras. Es una buena oportunidad para justificar, no enumerar, métodos de protección.
- **CHEM-U09-L05 — Extracting iron and aluminium. Docente 8,7 / Alumno 8,0.** Deriva método de la serie y separa funciones de carbono y caliza en el alto horno. Es exigente por encadenar redox, industria y ecuaciones; se beneficia de diagrama de flujo final.
- **CHEM-U09-L06 — Exercise Bank. Docente 6,2 / Alumno 5,8.** Diez ejercicios tienen valor acumulativo pero ningún apoyo interno. Añadir por fuera una guía “propiedad → mecanismo → uso” evitaría respuestas telegráficas.

### U10 — Environmental Chemistry

**Bloque: Docente 8,5 / Alumno 8,1.** El bloque conecta pruebas de agua, composición del aire, contaminantes, impacto y control. La relación causa–efecto–mitigación es una fortaleza; se debe proteger contra explicaciones moralizantes sin química causal.

- **CHEM-U10-L01 — Testing and treating water. Docente 8,7 / Alumno 8,3.** Diferencia presencia, pureza y seguridad y ordena el tratamiento por función. Es una precisión excelente para desmontar “puro = potable”.
- **CHEM-U10-L02 — Air composition and pollutant sources. Docente 8,5 / Alumno 8,2.** Presenta aire como mezcla, combustión y un mapa causal de fuentes. Los seis contaminantes demandan recuperación repetida para no convertirse en lista.
- **CHEM-U10-L03 — Pollutant effects and climate response. Docente 8,6 / Alumno 7,9.** Vincula cada contaminante a daño y estrategia concreta, y corrige la metáfora de reflexión. La carga verbal y de vocabulario es alta; requiere organizador gráfico de cuatro partes.
- **CHEM-U10-L04 — Acid rain and catalytic control. Docente 8,5 / Alumno 8,0.** Distingue retirar de convertir, y limita bien la afirmación “reducido, no eliminado”. La lección debe recuperar origen de SO2/NOx antes de hablar de control.
- **CHEM-U10-L05 — Exercise Bank. Docente 6,3 / Alumno 5,7.** Veinte ejercicios dan una buena muestra de examen, pero sin clasificación causal ni feedback. Es apto para evaluación una vez enseñado el mapa de contaminantes.

### U11 — Organic Chemistry

**Bloque: Docente 8,4 / Alumno 7,9.** Fórmulas/nombres → fracciones → alcanos → alquenos → etanol → polímeros es la progresión adecuada. Requiere repetición espaciada de representaciones y familias, pues los sufijos, enlaces y mecanismos se acumulan rápidamente.

- **CHEM-U11-L01 — Representing and naming carbon compounds. Docente 8,6 / Alumno 8,0.** El método de cuatro pasos y fórmulas desarrolladas hacen visible la relación estructura–nombre. La lección necesita práctica de ida y vuelta nombre↔estructura para comprobar dominio.
- **CHEM-U11-L02 — Fuels and petroleum fractions. Docente 8,4 / Alumno 8,1.** Conecta destilación fraccionada con rango de ebullición, longitud de cadena y uso. Buena claridad conceptual con carga moderada.
- **CHEM-U11-L03 — Alkanes and combustion. Docente 8,3 / Alumno 8,0.** Evita presentar “poco reactivo” como inerte y trabaja combustión completa. Con sólo un objetivo y tres bloques es clara, pero conviene enlazar con combustión incompleta de U10.
- **CHEM-U11-L04 — Alkenes, cracking and addition. Docente 8,5 / Alumno 7,9.** El doble enlace, bromine water, cracking y tres adiciones se organizan en progresión funcional. La distinción entre prueba, proceso y reacción exige alternar ejemplos, no sólo memorizar términos.
- **CHEM-U11-L05 — Ethanol as alcohol, solvent and fuel. Docente 8,3 / Alumno 8,0.** La estructura explica familia y usos sin sobreextender la relación “contiene oxígeno”. El alcance es manejable, pero debería compararse explícitamente con alcanos.
- **CHEM-U11-L06 — Addition polymers from alkenes. Docente 8,4 / Alumno 7,8.** Trabaja monómero↔polímero en ambas direcciones, lo que favorece transferencia. Tres bloques para una representación simbólica difícil dejan poco margen para diagnóstico individual.
- **CHEM-U11-L07 — Condensation polymers and nylon. Docente 8,5 / Alumno 7,7.** El contraste lateral con polímeros de adición y el enlace amida son rigurosos. Es alta carga para un único objetivo: necesita práctica de identificar enlace y unidad repetitiva antes de comparar mecanismos.
- **CHEM-U11-L08 — Exercise Bank. Docente 6,3 / Alumno 5,7.** Dieciséis ejercicios apoyan consolidación pero son poco accesibles sin clasificación por familia/reacción. Requiere soluciones estructurales, no sólo respuestas finales.

### U12 — Experimental Methods and Analysis

**Bloque: Docente 8,8 / Alumno 8,3.** Es una secuencia excepcionalmente funcional: lenguaje e instrumentos, titulación, cromatografía, selección de separación y análisis cualitativo. La dificultad aumenta de procedimiento a elección justificada; el riesgo es que tablas de pruebas se memoricen sin interpretar evidencia.

- **CHEM-U12-L01 — Measurement and solution language. Docente 8,8 / Alumno 8,4.** El instrumento se selecciona por magnitud y se distinguen solvente/soluto/solución, filtrado y etapas. Seis bloques conectan vocabulario con uso posterior y reducen errores de laboratorio.
- **CHEM-U12-L02 — Acid-base titration as measured neutralisation. Docente 8,7 / Alumno 8,2.** Las funciones de pipeta, bureta e indicador y el criterio de concordancia estructuran un procedimiento seguro. Las cuatro prácticas deben requerir lectura de menisco/volumen si se espera destreza práctica real.
- **CHEM-U12-L03 — Chromatography and Rf evidence. Docente 8,7 / Alumno 8,1.** Separación, montaje, evidencia de manchas y Rf se desarrollan en un orden correcto, incluyendo el límite “una mancha no prueba pureza”. Es buena educación en evidencia; la razón de distancias debe modelarse una vez con unidades.
- **CHEM-U12-L04 — Selecting separation and purity methods. Docente 8,9 / Alumno 8,0.** Diez bloques vinculan método con diferencia de propiedad, distinguen técnicas y tratan evidencia de pureza con prudencia. Es excelente pero muy extensa: dividir decisión de método y validación de pureza reduce sobrecarga.
- **CHEM-U12-L05 — Identifying anions and gases. Docente 8,8 / Alumno 8,2.** Presenta prueba cualitativa como cadena reactivo–condición–resultado y explica acidificación. La tabla debe convertirse en decisiones de evidencia para evitar recuerdo aislado de colores.
- **CHEM-U12-L06 — Cations, precipitates and flame tests. Docente 8,8 / Alumno 8,1.** Combina NaOH/NH3, estrategia para incógnita, evolución de precipitado y llama. Es sólido, aunque la densidad de observaciones recomienda práctica de casos incompletos y confirmación cruzada.
- **CHEM-U12-L07 — Exercise Bank. Docente 6,2 / Alumno 5,8.** Ocho ejercicios dan cierre, pero sin andamiaje para escoger prueba ni feedback de observaciones. Debe usarse después de la matriz de decisión de L05–L06.

### U13 — Revision and Exam Practice

**Bloque: Docente 7,8 / Alumno 7,3.** Ofrece recuperación cuantitativa, técnica de examen, errores comunes, glosario y preguntas. La cobertura es útil y explícita, pero el bloque no arranca con diagnóstico de lagunas ni ofrece una ruta adaptativa; varias lecciones privilegian lectura/flashcards frente a recuperación generativa con corrección.

- **CHEM-U13-L01 — Exercise Bank. Docente 6,4 / Alumno 5,8.** Quince preguntas de examen sirven para evidencia final, pero carecen de pauta de corrección, selección por tema y puente de reenseñanza. Es evaluación, no una lección independiente.
- **CHEM-U13-L02 — Revision: the quantitative chemistry toolkit. Docente 8,0 / Alumno 7,5.** Resume mol, concentración, gas y masas con tres ejemplos y tres ejercicios; es una recuperación pertinente. Sin guiado ni diagnóstico, los alumnos con lagunas pueden no detectar en qué paso fallan.
- **CHEM-U13-L03 — Revision: exam technique, command words and working. Docente 7,9 / Alumno 7,5.** Hace explícitos verbo de mando, trabajo mostrado, observación y extensión de respuesta. Faltan ejercicios de producción evaluada, por lo que el alumno puede reconocer una regla sin aplicarla bajo presión.
- **CHEM-U13-L04 — Revision: the most common mistakes across the course. Docente 7,8 / Alumno 7,2.** Doce concepciones erróneas y flashcards hacen visibles trampas transversales; el alcance es muy amplio para 0,75 h. Conviene transformar cada error en una pregunta de recuperación breve.
- **CHEM-U13-L05 — Revision: key terms glossary. Docente 7,4 / Alumno 7,0.** Las 52 flashcards y la organización por área lo convierten en buen recurso de consulta. Sin uso contextual ni práctica de definición aplicada, favorece reconocimiento antes que dominio examinable.

## Prioridades de mejora sin alterar el contenido auditado

1. Diseñar una capa de uso para cada *Exercise Bank*: criterio de entrada, agrupación por objetivo, solución razonada, umbral de autocorrección y acción de reenseñanza. Es la intervención de mayor impacto en autonomía.
2. Añadir al inicio de U13 un diagnóstico corto por dominios y una ruta “si fallas X, vuelve a Y”; así las preguntas de examen se convierten en revisión dirigida, no en una prueba ciega.
3. En las lecciones de alta densidad (U03-L01/L05, U04-L02, U07-L03, U12-L04–L06), introducir puntos de parada con una sola decisión comprobable antes de continuar al siguiente modelo o procedimiento.
4. Realizar una comprobación visual responsiva de figuras en el lector final a 320 px, 768 px y escritorio, sobre todo diagramas anchos y tablas/etiquetas densas. La fuente está estructuralmente sana, pero la interfaz es la última responsable de evitar solapamiento.

## Conclusión

El curso está listo para enseñanza guiada con una calidad pedagógica alta y una base especialmente fuerte de ejemplos, práctica y prevención de errores. Para aprendizaje autónomo y preparación final, el foco debe estar en convertir bancos y revisión en ciclos diagnósticos de práctica con feedback, y en completar la validación visual dentro de la interfaz final.
