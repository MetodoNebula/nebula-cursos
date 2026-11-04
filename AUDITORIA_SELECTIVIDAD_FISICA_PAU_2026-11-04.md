# Auditoría — Banco de ejercicios PAU · Curso `selectividad_fisica`
**Fecha:** 2026-11-04 · **Alcance:** las 9 lecciones nuevas "Ejercicios de selectividad (PAU)" (una por bloque)

## Resumen ejecutivo
- **425 ejercicios PAU** resueltos paso a paso (tras depurar duplicados), **38 figuras** TikZ validadas, repartidos en los 9 bloques.
- **Todo en español**; duplicados por idioma (valenciano/catalán) eliminados en la extracción.
- **MathJax:** 4402 campos renderizados en Chromium headless con la config exacta del proyecto → **0 `mjx-merror`, 0 errores de consola**.
- **Integridad:** cada bundle de física difiere del original SOLO en la lección nueva; los otros 8 cursos, intactos; catálogo regenerado con **0 avisos**.
- Copias de seguridad en `_pau_build_fisica/_backup_*` y `_backup_final_*`.

## 1) Auditoría numérica independiente (contenido)
10 revisores independientes (que no generaron el contenido) recomputaron **con Python** cada número de los 437 ejercicios iniciales. Resultado: **5 errores reales**, todos corregidos y reverificados:

| Ejercicio (bloque) | Error detectado | Corrección |
|---|---|---|
| EM · "campo nulo entre dos hilos (misma corriente)" | Afirmaba cancelación en toda la mediatriz | Reescrito: el campo se anula **solo en el punto medio** |
| NUC · patrón del kg (Pt-190) | λ con exponente erróneo (10⁻²³) | Corregido a **10⁻²⁰ s⁻¹** (la actividad ya era coherente) |
| NUC · radón-222 | Conversión de masa 10⁻⁶ pg | Corregido a **10⁻³ pg** |
| MAS/ÓPT · lámina de vidrio en agua | Enunciado ambiguo (medio superior) | Aclarado "**incide desde el aire**"; resultado 43,9° (coincide con la solución oficial de Murcia) |
| ÓPT · proyector | Frase rota "real (misma lado contrario)" | Redacción corregida |

También: corregida la etiqueta "serie de Balmer" (transición físicamente imposible en Balmer) y el signo intermedio de Δp en un problema de dinámica del protón. **Nota:** se había detectado y corregido antes una errata de la propia solución oficial (Madrid 2026, fotoeléctrico: daba 0,93 eV; correcto 0,07 eV).

Bloques `GRAV` (2ª mitad) y `ÓPT` (2ª mitad): **0 errores**. El resto, solo los listados.

## 2) Deduplicación
El examen **C. Valenciana Junio 2022** se había procesado dos veces (sus ficheros `-exam` y `-criterios` cayeron en lotes distintos) → 24 ejercicios = 12 únicos × 2. Se eliminó un gemelo de cada par (conservando el que lleva figura o datos completos). **12 duplicados retirados → 425 ejercicios finales.** No hay otros exámenes duplicados.

## 3) Figuras (38) — sin cuadros blancos ni solapes
Revisadas **una a una a resolución completa sobre el fondo real de la tarjeta**:
- **Cuadros blancos eliminados:** las 12 gráficas de ejes (fotoeléctrico, I-V, desintegración, ondas) tenían los recuadros de las etiquetas de los ejes en blanco puro; se recolorearon al color de la tarjeta (`#f6f8fb`) para que se fundan con el fondo. La curva I-V del fotoeléctrico se rediseñó con el eje Y a la izquierda, despejado de las curvas.
- **Solapes corregidos (11 figuras):** etiquetas "pendiente" que se montaban sobre las rectas, "T₁/₂(Ni)" sobre una curva, fuerzas apretadas en las puntas de flecha, rótulos sobre el campo de ×/⊙, el ángulo "63,4°" junto a "B", "F/O" pegados y "f_roz"/"v" sobre el rayado del suelo.
- Verificación final: **0 solapes texto-texto, 0 solapes texto-línea; todas las etiquetas legibles** en los 9 bloques.

## 4) Calidad pedagógica
- Formato de corrección PAU: **planteamiento simbólico → sustitución con unidades → resultado → interpretación**, con apartados **(a)/(b)/(c)** y bloques `$$…$$`.
- Las cuestiones teóricas (defecto de masa, Faraday-Lenz, reflexión total, etc.) **explican el concepto**, no solo aplican fórmulas (desarrollos de 500–1300 caracteres).
- Cada ejercicio incluye **2–3 "errores típicos"** que aportan valor didáctico.
- **Sin relleno:** todos son problemas reales de examen (Madrid, C. Valenciana, Andalucía, Cantabria, Murcia; 2007–2026), resueltos; no hay ejercicios inventados ni genéricos.
- Problemas con enunciado simbólico (p. ej. "determine la expresión de v") se resuelven correctamente en forma simbólica, como pide el examen.

## 5) Recuento final por bloque
| Bloque | Ejercicios | Figuras |
|---|---|---|
| Fundamentos | 1 | 0 |
| Campo gravitatorio | 81 | 6 |
| Vibraciones y ondas (MAS) | 5 | 1 |
| Ondas | 59 | 4 |
| Electromagnetismo | 107 | 9 |
| Óptica | 77 | 9 |
| Relatividad | 17 | 0 |
| Cuántica | 36 | 5 |
| Nuclear | 42 | 4 |
| **TOTAL** | **425** | **38** |

`selectividad_fisica`: 100 lecciones · 601 exam_questions en el curso (425 PAU + 176 previas).

## 6) Para publicar
En **localhost** se ve directamente desde los `bundles/` en claro. Para la web pública, ejecuta tu **`publicar.bat`** (cifra el contenido nuevo con `cifrar.js` y hace push), igual que con Química.
