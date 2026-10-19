# CHANGELOG.md — selectividad_matematicas_ccss (piloto v2)
## Correcciones del ledger (foco: probabilidad, inferencia, análisis)
**P1**
- mat_derivadas/inflexión: verificado ya resuelto — se define por cambio de concavidad y se marca f''=0 como necesario-no-suficiente, con contraejemplo x⁴.
- mat_limites/L'Hôpital: **no aplica** — L'Hôpital no forma parte del corpus de CCSS (no se inventa contenido; no-hallucination rule).
- mat_muestreo_inferencia/representatividad: añadido matiz — la aleatoriedad reduce el sesgo de selección y habilita la inferencia, pero no *garantiza* que una muestra concreta sea representativa; existen sesgos de marco/no respuesta/medición.
**P2**
- mat_derivadas/tangente vertical: aclarado que la pendiente «se va a infinito» y la derivada finita **no existe** (ya se trataba como límite del cociente, no como derivada ordinaria).
- mat_probabilidad/no equiprobable: distinguida la estimación empírica por frecuencias del modelo no equiprobable conocido a priori.
- mat_probabilidad/reemplazamiento: la independencia es propiedad del modelo (P(A∩B)=P(A)P(B)), no sinónimo automático de «con reemplazamiento».
- mat_muestreo/TCL n≥30: etiquetado como regla práctica (heurística), no frontera universal; exacto si la población ya es normal.
- mat_muestreo/suma normal: scope explícito — exacto para normales independientes, aproximado por TCL en otros casos.
- mat_muestreo/eficiencia: n/σ² y n/[p(1-p)] reetiquetados como precisión/información de esos estimadores, no definición general de eficiencia.
- contrastes/aceptar H0: terminología unificada a «región de no rechazo» (40 apariciones) y añadido que no rechazar H0 ≠ probar H0.

## Estructura
- Resueltas 10 referencias de objetivo colgantes (mat_representacion 08: LO-08-1→LO-09-1; 09: LO-09-1→LO-11-1).
- Reorden esencial-primero en 7 lecciones (ampliación agrupada al final con separador).
- schema_v2 aditivo (prefijo SELMATCCSS); rutas, checkpoints, diagnóstico y Exam Mode generados.
- 3 diagramas nuevos (árbol de probabilidad total, región factible de PL, intervalo de confianza).
