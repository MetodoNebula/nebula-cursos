# -*- coding: utf-8 -*-
"""
Fase 5 — Modulo 00: Fundamentos (remediacion just-in-time), reutilizable.

Microlecciones NUEVAS, en el mismo formato plano que usa index.html (para
que se puedan ver con el mismo visor sin tocar el frontend) + schema_v2,
en un bundle nuevo: selectividad_fisica__fundamentos.json, unidad
"fundamentos" (unit_id). No sustituye ni reescribe nada de las 8 unidades
existentes: es contenido ADITIVO, pensado para remediacion just-in-time
(un alumno DESDE_CERO entra aqui solo si el diagnostico lo pide), tal como
exige el encargo ("Usa remediation just-in-time. No conviertas Selectividad
Fisica en un curso de matematicas basicas.") -> por eso son 6 microlecciones
cortas (15-20 min), no una unidad completa de matematicas.
"""
import json, os

BASE = os.path.expanduser("~/mnt/Nebula_Cursos_Web")
PILOT = os.path.join(BASE, "pilot/selectividad_fisica_v2")

def lesson(id_, title, objectives, theory_blocks, worked_example, exercises, mcq, summary, keywords, concept_tag):
    return {
        "id": id_,
        "title": title,
        "subject": "Física",
        "course_label": "Selectividad Física",
        "unit_id": "fundamentos",
        "estimated_length": "0,5 h",
        "estimated_difficulty": 1,
        "curriculum": {"framework": "Remediación transversal (prerrequisito de varias unidades)",
                       "codes": [], "status": "FOUNDATIONS", "track": None},
        "objectives": objectives,
        "prerequisites": [],
        "diagnostic_items": [{
            "id": f"DIAG-{id_}-00",
            "question": f"Autoevaluación rápida: ¿te sientes seguro con {title.lower()} sin mirar la teoría?",
            "expected_answer": "Si la respuesta es sí para los tres primeros ejercicios de esta lección sin mirar el worked example, puedes saltar directamente a la práctica.",
            "common_wrong_answers": [],
            "interpretation": "Este microtema es remediación just-in-time: solo se recomienda cuando el diagnóstico de la unidad principal (ver KNOWLEDGE_GRAPH.json) detecta una carencia aquí.",
        }],
        "theory_blocks": theory_blocks,
        "keywords": keywords,
        "worked_examples": [worked_example],
        "guided_exercises": [],
        "exercises": exercises,
        "exam_questions": [],
        "challenge_questions": [],
        "mcq": mcq,
        "flashcards": [],
        "misconceptions": [],
        "common_mistakes": [],
        "exam_notes": [],
        "summary": summary,
        "lang": "es",
        "foundations_concept_tag": concept_tag,
    }

def tb(id_, type_, title, scope, body, concept_ids):
    return {"id": id_, "type": type_, "title": title, "scope": scope, "body": body,
            "concept_ids": concept_ids, "objective_ids": [], "provenance": "foundations_module"}

LESSONS = []

LESSONS.append(lesson(
    "F01", "Vectores: componentes, módulo y suma",
    [{"id": "LO-F01-1", "statement": "Descomponer un vector en componentes x/y a partir de su módulo y ángulo, y recomponer módulo y ángulo a partir de las componentes.", "bloom": "apply", "concept_ids": ["C-FUND-VEC"], "scope": "CORE"},
     {"id": "LO-F01-2", "statement": "Sumar vectores por componentes, sin dibujar paralelogramos.", "bloom": "apply", "concept_ids": ["C-FUND-VEC"], "scope": "CORE"}],
    [tb("TH-F01-0","intuition","Por qué no basta un número","CORE",
        "Muchas magnitudes de Física (fuerza, velocidad, campo) tienen dirección, no solo valor. Un vector se representa mejor por sus **componentes** $(V_x, V_y)$ que por 'módulo y una flecha', porque las componentes se suman con una simple suma de números.",
        ["C-FUND-VEC"]),
     tb("TH-F01-1","formalisation","Componentes y recomposición","CORE",
        "Dado el módulo $V$ y el ángulo $\\theta$ medido desde el eje $x$: $V_x=V\\cos\\theta$, $V_y=V\\,\\mathrm{sen}\\,\\theta$. Al revés: $V=\\sqrt{V_x^2+V_y^2}$ y $\\theta=\\arctan(V_y/V_x)$, vigilando el cuadrante.",
        ["C-FUND-VEC"]),
     tb("TH-F01-2","worked_rule","Sumar por componentes","CORE",
        "Para sumar dos o más vectores: se descompone cada uno, se suman las $x$ entre sí y las $y$ entre sí, y solo al final se recompone el vector resultante. Nunca se suman módulos directamente salvo que los vectores sean paralelos.",
        ["C-FUND-VEC"])],
    {"id": "WE-F01-1", "statement": "Suma $\\vec A$ (módulo 5, a 0°) y $\\vec B$ (módulo 5, a 90°).",
     "knowns": ["$A=5$, $\\theta_A=0°$", "$B=5$, $\\theta_B=90°$"], "unknowns": ["$\\vec A+\\vec B$"],
     "reasoning": ["$A_x=5,\\ A_y=0$.", "$B_x=0,\\ B_y=5$.", "Suma: $(5,5)$.", "Módulo $\\sqrt{50}=7{,}07$; ángulo $45°$."],
     "solution": "$\\vec A+\\vec B$ tiene módulo $7{,}07$ a $45°$.",
     "interpretation": "Dos vectores iguales a 90° nunca suman el doble del módulo: suman $\\sqrt2$ veces, y la dirección resultante biseca el ángulo entre ellos.", "common_mistake": "Sumar los módulos (10) en vez de las componentes."},
    [{"id": "EX-F01-1", "type": "APPLY", "objective_ids": ["LO-F01-1"], "concept_ids": ["C-FUND-VEC"], "difficulty": 1,
      "statement": "Descompón un vector de módulo 10 a 30° sobre el eje x.",
      "hints": ["$\\cos30°=0{,}866$, $\\mathrm{sen}\\,30°=0{,}5$."], "answer": "$(8{,}66;\\ 5{,}0)$",
      "full_solution": "$V_x=10\\cos30°=8{,}66$; $V_y=10\\,\\mathrm{sen}\\,30°=5{,}0$.", "common_errors": ["Intercambiar seno y coseno."]}],
    [{"id": "MCQ-F01-1", "stem": "Dos vectores de módulo 3 y 4, perpendiculares entre sí. ¿Módulo de la suma?",
      "options": [{"key": "a", "text": "7"}, {"key": "b", "text": "5", }, {"key": "c", "text": "1"}, {"key": "d", "text": "12"}],
      "correct": "b", "explanation": "$\\sqrt{3^2+4^2}=5$ (es el 3-4-5 pitagórico). No se suman módulos directamente salvo vectores paralelos.",
      "difficulty": 1, "objective_id": "LO-F01-1", "concept_id": "C-FUND-VEC"}],
    {"big_idea": "Un vector se maneja mejor por componentes que por 'módulo y flecha'; sumar vectores es sumar componentes.",
     "key_points": ["$V_x=V\\cos\\theta$, $V_y=V\\,\\mathrm{sen}\\,\\theta$.", "Para sumar: primero componentes, después módulo y ángulo del resultado.", "Los módulos no se suman salvo que los vectores sean paralelos."],
     "formulas": ["V_x=V\\cos\\theta,\\quad V_y=V\\,\\mathrm{sen}\\,\\theta", "V=\\sqrt{V_x^2+V_y^2}"],
     "what_to_remember_if_nothing_else": "Para sumar vectores: descompone, suma componente a componente, recompone al final."},
    [{"term": "Componentes de un vector", "definition": "Las proyecciones del vector sobre cada eje; se suman independientemente de las de los demás ejes."}],
    "C-FUND-VEC",
))

LESSONS.append(lesson(
    "F02", "Trigonometría básica para Física",
    [{"id": "LO-F02-1", "statement": "Usar seno, coseno y tangente de un ángulo en un triángulo rectángulo para despejar catetos o hipotenusa.", "bloom": "apply", "concept_ids": ["C-FUND-TRIG"], "scope": "CORE"}],
    [tb("TH-F02-0","intuition","El triángulo que aparece en todas partes","CORE",
        "Óptica, ondas, campo gravitatorio... casi todos usan en algún momento un triángulo rectángulo con un ángulo conocido y un lado conocido.",
        ["C-FUND-TRIG"]),
     tb("TH-F02-1","formalisation","Las tres razones","CORE",
        "Con el ángulo $\\theta$: $\\mathrm{sen}\\,\\theta=\\dfrac{\\text{cateto opuesto}}{\\text{hipotenusa}}$, $\\cos\\theta=\\dfrac{\\text{cateto contiguo}}{\\text{hipotenusa}}$, $\\mathrm{tg}\\,\\theta=\\dfrac{\\text{opuesto}}{\\text{contiguo}}$.",
        ["C-FUND-TRIG"])],
    {"id": "WE-F02-1", "statement": "Un rayo incide con ángulo 40° sobre una superficie; calcula el seno y el coseno de ese ángulo.",
     "knowns": ["$\\theta=40°$"], "unknowns": ["$\\mathrm{sen}\\,40°,\\ \\cos40°$"],
     "reasoning": ["Calculadora en modo grados (no radianes).", "$\\mathrm{sen}\\,40°=0{,}643$.", "$\\cos40°=0{,}766$."],
     "solution": "$\\mathrm{sen}\\,40°=0{,}643$; $\\cos40°=0{,}766$.",
     "interpretation": "El error más caro en Selectividad no es de trigonometría: es dejar la calculadora en radianes.", "common_mistake": "Calcular en radianes en vez de grados."},
    [{"id": "EX-F02-1", "type": "APPLY", "objective_ids": ["LO-F02-1"], "concept_ids": ["C-FUND-TRIG"], "difficulty": 1,
      "statement": "Un triángulo rectángulo tiene hipotenusa 10 y un ángulo de 30°. Calcula el cateto opuesto.",
      "hints": ["opuesto = hipotenusa · sen(ángulo)."], "answer": "5", "full_solution": "$10\\cdot\\mathrm{sen}\\,30°=10\\cdot0{,}5=5$.",
      "common_errors": ["Usar el coseno en vez del seno."]}],
    [{"id": "MCQ-F02-1", "stem": "¿Cuánto vale sen(90°)?",
      "options": [{"key": "a", "text": "0"}, {"key": "b", "text": "1"}, {"key": "c", "text": "0,707"}, {"key": "d", "text": "indefinido"}],
      "correct": "b", "explanation": "sen(90°)=1: a 90° todo el lado es el 'opuesto', coincide con la hipotenusa.",
      "difficulty": 1, "objective_id": "LO-F02-1", "concept_id": "C-FUND-TRIG"}],
    {"big_idea": "Seno, coseno y tangente relacionan un ángulo con los lados de un triángulo rectángulo; la calculadora debe estar en grados salvo que el problema dé radianes.",
     "key_points": ["sen = opuesto/hipotenusa; cos = contiguo/hipotenusa; tg = opuesto/contiguo.", "Comprobar siempre el modo DEG/RAD de la calculadora."],
     "formulas": ["\\mathrm{sen}\\,\\theta=\\text{opuesto}/\\text{hipotenusa}", "\\cos\\theta=\\text{contiguo}/\\text{hipotenusa}"],
     "what_to_remember_if_nothing_else": "Comprueba el modo de la calculadora (grados) antes de nada."},
    [{"term": "Razón trigonométrica", "definition": "Cociente entre dos lados de un triángulo rectángulo asociado a un ángulo."}],
    "C-FUND-TRIG",
))

LESSONS.append(lesson(
    "F03", "Despeje algebraico y cambio de unidades",
    [{"id": "LO-F03-1", "statement": "Despejar una variable de una ecuación con varias magnitudes sin cambiar su significado físico.", "bloom": "apply", "concept_ids": ["C-FUND-ALG"], "scope": "CORE"}],
    [tb("TH-F03-0","formalisation","Despejar sin perder de vista las unidades","CORE",
        "Despejar es aplicar la misma operación a los dos lados de la igualdad. El resultado debe tener las unidades correctas: si no las tiene, hay un error antes del despeje, no en el despeje.",
        ["C-FUND-ALG"])],
    {"id": "WE-F03-1", "statement": "De $F=\\dfrac{Gm_1m_2}{r^2}$, despeja $r$.",
     "knowns": ["$F, G, m_1, m_2$"], "unknowns": ["$r$"],
     "reasoning": ["Multiplicar los dos lados por $r^2$: $Fr^2=Gm_1m_2$.", "Dividir entre $F$: $r^2=\\dfrac{Gm_1m_2}{F}$.", "Raíz cuadrada: $r=\\sqrt{\\dfrac{Gm_1m_2}{F}}$."],
     "solution": "$r=\\sqrt{\\dfrac{Gm_1m_2}{F}}$.",
     "interpretation": "Cuando la variable a despejar está al cuadrado en el denominador, hay que \"subirla\" antes de poder despejarla.", "common_mistake": "Olvidar la raíz cuadrada al final."},
    [{"id": "EX-F03-1", "type": "APPLY", "objective_ids": ["LO-F03-1"], "concept_ids": ["C-FUND-ALG"], "difficulty": 1,
      "statement": "De $v=\\omega R$, despeja $\\omega$.", "hints": ["Dividir ambos lados entre $R$."], "answer": "$\\omega=v/R$",
      "full_solution": "$\\omega=\\dfrac{v}{R}$.", "common_errors": ["Invertir la fracción."]}],
    [{"id": "MCQ-F03-1", "stem": "De $E=mc^2$, ¿cómo se despeja $m$?",
      "options": [{"key": "a", "text": "$m=E/c^2$"}, {"key": "b", "text": "$m=Ec^2$"}, {"key": "c", "text": "$m=E/c$"}, {"key": "d", "text": "$m=\\sqrt{E}/c$"}],
      "correct": "a", "explanation": "Dividiendo los dos lados entre $c^2$: $m=E/c^2$.",
      "difficulty": 1, "objective_id": "LO-F03-1", "concept_id": "C-FUND-ALG"}],
    {"big_idea": "Despejar es operar igual en los dos lados de la ecuación; el resultado final debe tener sentido dimensional.",
     "key_points": ["Operar siempre en los dos lados por igual.", "Comprobar las unidades del resultado final."],
     "formulas": [], "what_to_remember_if_nothing_else": "Después de despejar, comprueba las unidades: si no salen las esperadas, hay un error."},
    [{"term": "Despejar", "definition": "Aislar una variable en un lado de la ecuación aplicando la misma operación a ambos lados."}],
    "C-FUND-ALG",
))

LESSONS.append(lesson(
    "F04", "Notación científica y unidades del SI",
    [{"id": "LO-F04-1", "statement": "Convertir cantidades a notación científica y manejar las unidades básicas del SI.", "bloom": "apply", "concept_ids": ["C-FUND-SI"], "scope": "CORE"}],
    [tb("TH-F04-0","formalisation","Notación científica","CORE",
        "Un número en notación científica se escribe $a\\cdot10^n$ con $1\\le a<10$. Multiplicar/dividir potencias de 10 se hace sumando/restando exponentes.",
        ["C-FUND-SI"]),
     tb("TH-F04-1","formalisation","Las unidades del SI que aparecen siempre","CORE",
        "m (longitud), kg (masa), s (tiempo), A (corriente), K (temperatura). Todas las fórmulas de Selectividad Física están pensadas para sustituir datos ya en SI: antes de sustituir, convierte minutos a segundos, km a metros, gramos a kilogramos.",
        ["C-FUND-SI"])],
    {"id": "WE-F04-1", "statement": "Expresa 0,000025 km en notación científica y en metros.",
     "knowns": ["$0{,}000025$ km"], "unknowns": ["metros, notación científica"],
     "reasoning": ["$0{,}000025=2{,}5\\cdot10^{-5}$.", "1 km = 1000 m, luego en metros: $2{,}5\\cdot10^{-5}\\cdot10^3=2{,}5\\cdot10^{-2}$ m."],
     "solution": "$2{,}5\\cdot10^{-2}$ m.", "interpretation": "Cambiar de unidad es multiplicar por una potencia de 10; no cambia el número de cifras significativas.",
     "common_mistake": "Multiplicar por 1000 en el sentido equivocado."},
    [{"id": "EX-F04-1", "type": "APPLY", "objective_ids": ["LO-F04-1"], "concept_ids": ["C-FUND-SI"], "difficulty": 1,
      "statement": "Convierte 45 minutos a segundos.", "hints": ["1 min = 60 s."], "answer": "2700 s", "full_solution": "$45\\cdot60=2700$ s.",
      "common_errors": ["Dividir en vez de multiplicar."]}],
    [{"id": "MCQ-F04-1", "stem": "¿Cuál es la unidad SI de masa?",
      "options": [{"key": "a", "text": "gramo"}, {"key": "b", "text": "kilogramo"}, {"key": "c", "text": "libra"}, {"key": "d", "text": "tonelada"}],
      "correct": "b", "explanation": "El kilogramo es la unidad base de masa en el SI; el gramo es un submúltiplo.",
      "difficulty": 1, "objective_id": "LO-F04-1", "concept_id": "C-FUND-SI"}],
    {"big_idea": "Trabajar siempre en SI antes de sustituir en una fórmula evita el 90% de los errores de cálculo.",
     "key_points": ["$a\\cdot10^n$ con $1\\le a<10$.", "Convertir SIEMPRE a SI antes de sustituir en una fórmula."],
     "formulas": [], "what_to_remember_if_nothing_else": "Antes de sustituir: todo en SI."},
    [{"term": "Notación científica", "definition": "Forma $a\\cdot10^n$, con $1\\le a<10$, de escribir números muy grandes o muy pequeños."}],
    "C-FUND-SI",
))

LESSONS.append(lesson(
    "F05", "Lectura de gráficas en Física",
    [{"id": "LO-F05-1", "statement": "Extraer pendiente, área y valores concretos de una gráfica y relacionarlos con magnitudes físicas.", "bloom": "analyze", "concept_ids": ["C-FUND-GRAF"], "scope": "CORE"}],
    [tb("TH-F05-0","formalisation","Qué significa la pendiente y qué significa el área","CORE",
        "En una gráfica $y$ frente a $x$, la **pendiente** en un punto es la derivada ($dy/dx$) y el **área bajo la curva** entre dos valores de $x$ es la integral. Muchas magnitudes físicas son, literalmente, la pendiente o el área de otra.",
        ["C-FUND-GRAF"])],
    {"id": "WE-F05-1", "statement": "En una gráfica $v$ (m/s) frente a $t$ (s), la recta pasa por (0,0) y (4,20). ¿Qué representa la pendiente?",
     "knowns": ["puntos (0,0) y (4,20)"], "unknowns": ["significado físico de la pendiente"],
     "reasoning": ["Pendiente $=\\dfrac{20-0}{4-0}=5$.", "Si el eje y es velocidad y el eje x es tiempo, la pendiente es la aceleración."],
     "solution": "La pendiente vale 5 y representa una aceleración de 5 m/s².",
     "interpretation": "La misma gráfica, con otros ejes, cambia lo que \"es\" la pendiente: siempre hay que mirar qué hay en cada eje antes de interpretar.", "common_mistake": "Confundir la pendiente con el valor de $y$ en un punto."},
    [{"id": "EX-F05-1", "type": "APPLY", "objective_ids": ["LO-F05-1"], "concept_ids": ["C-FUND-GRAF"], "difficulty": 2,
      "statement": "Una gráfica $F$ (N) frente a $x$ (m) es una recta horizontal en $F=10$ N entre $x=0$ y $x=3$ m. ¿Qué representa el área bajo la curva?",
      "hints": ["Área de un rectángulo: base por altura."], "answer": "30 J (trabajo)", "full_solution": "Área $=10\\cdot3=30$; si el eje y es fuerza y el eje x es posición, el área es el trabajo: 30 J.",
      "common_errors": ["Dar solo el número sin la interpretación física."]}],
    [{"id": "MCQ-F05-1", "stem": "En una gráfica posición-tiempo, ¿qué representa la pendiente?",
      "options": [{"key": "a", "text": "La aceleración"}, {"key": "b", "text": "La velocidad"}, {"key": "c", "text": "La posición inicial"}, {"key": "d", "text": "El tiempo total"}],
      "correct": "b", "explanation": "La pendiente de x(t) es $dx/dt$, que es la velocidad.",
      "difficulty": 1, "objective_id": "LO-F05-1", "concept_id": "C-FUND-GRAF"}],
    {"big_idea": "En una gráfica física, la pendiente y el área casi siempre son otra magnitud física; hay que mirar qué hay en cada eje antes de interpretar el número.",
     "key_points": ["Pendiente = derivada = tasa de cambio.", "Área bajo la curva = integral = magnitud acumulada."],
     "formulas": [], "what_to_remember_if_nothing_else": "Antes de leer una gráfica, identifica qué magnitud hay en cada eje."},
    [{"term": "Pendiente", "definition": "Tasa de cambio de la variable del eje y respecto a la del eje x; en Física suele ser otra magnitud con significado propio."}],
    "C-FUND-GRAF",
))

LESSONS.append(lesson(
    "F06", "Conservación de la energía: el balance básico",
    [{"id": "LO-F06-1", "statement": "Plantear un balance de energía entre dos instantes, incluyendo el trabajo de fuerzas no conservativas cuando las haya.", "bloom": "apply", "concept_ids": ["C-FUND-ENERGIA"], "scope": "CORE"}],
    [tb("TH-F06-0","formalisation","El balance en una línea","CORE",
        "$E_{c,1}+E_{p,1}+W_{\\text{no conservativas}}=E_{c,2}+E_{p,2}$. Si no hay fuerzas disipativas (rozamiento, resistencia del aire) ni agentes externos, $W_{\\text{no conservativas}}=0$ y la energía mecánica se conserva: $E_{c,1}+E_{p,1}=E_{c,2}+E_{p,2}$.",
        ["C-FUND-ENERGIA"])],
    {"id": "WE-F06-1", "statement": "Un cuerpo de 2 kg cae en caída libre desde 10 m. ¿Con qué velocidad llega al suelo (sin rozamiento)?",
     "knowns": ["$m=2$ kg", "$h=10$ m", "$g=9{,}8$ m/s²"], "unknowns": ["$v$"],
     "reasoning": ["$E_{p,1}=mgh$, $E_{c,1}=0$.", "$E_{c,2}=\\tfrac12mv^2$, $E_{p,2}=0$.", "$mgh=\\tfrac12mv^2\\Rightarrow v=\\sqrt{2gh}$."],
     "solution": "$v=\\sqrt{2\\cdot9{,}8\\cdot10}=14{,}0$ m/s.", "interpretation": "La masa se cancela: todos los cuerpos en caída libre sin rozamiento llegan a la misma velocidad desde la misma altura.", "common_mistake": "Olvidar que la masa se cancela y dejarla en la fórmula final."},
    [{"id": "EX-F06-1", "type": "APPLY", "objective_ids": ["LO-F06-1"], "concept_ids": ["C-FUND-ENERGIA"], "difficulty": 2,
      "statement": "Un bloque de 1 kg desliza con rozamiento (W_roz=-5 J) desde 3 m de altura, en reposo. ¿Con qué velocidad llega abajo?",
      "hints": ["$E_{p,1}+W_{roz}=E_{c,2}$."], "answer": "$v\\approx6{,}4$ m/s",
      "full_solution": "$mgh+W_{roz}=\\tfrac12mv^2\\Rightarrow 1\\cdot9{,}8\\cdot3-5=\\tfrac12\\cdot1\\cdot v^2\\Rightarrow v=\\sqrt{2(29{,}4-5)}=6{,}97$ m/s.",
      "common_errors": ["Sumar el trabajo del rozamiento en vez de restarlo."]}],
    [{"id": "MCQ-F06-1", "stem": "¿Cuándo se conserva la energía mecánica de un sistema?",
      "options": [{"key": "a", "text": "Siempre"}, {"key": "b", "text": "Cuando no actúan fuerzas no conservativas (rozamiento, agentes externos)"}, {"key": "c", "text": "Solo en caída libre"}, {"key": "d", "text": "Nunca, siempre se pierde algo"}],
      "correct": "b", "explanation": "La energía mecánica se conserva solo si el trabajo de las fuerzas no conservativas es cero; en presencia de rozamiento, lo que se conserva es la energía TOTAL, no la mecánica.",
      "difficulty": 2, "objective_id": "LO-F06-1", "concept_id": "C-FUND-ENERGIA"}],
    {"big_idea": "El balance de energía entre dos instantes es la herramienta más usada de toda la Selectividad de Física; la condición para que la energía MECÁNICA se conserve es que no haya fuerzas no conservativas actuando.",
     "key_points": ["$E_{c,1}+E_{p,1}+W_{nc}=E_{c,2}+E_{p,2}$.", "La energía mecánica se conserva SOLO si $W_{nc}=0$."],
     "formulas": ["E_{c,1}+E_{p,1}+W_{nc}=E_{c,2}+E_{p,2}"],
     "what_to_remember_if_nothing_else": "Antes de igualar energías, pregúntate si hay rozamiento u otro agente externo."},
    [{"term": "Energía mecánica", "definition": "Suma de energía cinética y potencial; se conserva solo si no actúan fuerzas no conservativas."}],
    "C-FUND-ENERGIA",
))

bundle = {f"{l['id']}_{l['title'].split(':')[0].replace(' ','_')}.json": l for l in LESSONS}
# clean keys of accents-free safe names already mostly ascii; keep simple
out = {}
for l in LESSONS:
    safe_title = l["title"].split(":")[0].replace(" ", "_").replace(",", "")
    bkey = f"{l['id']}_{safe_title}.json"
    out[bkey] = l

fp = os.path.join(PILOT, "selectividad_fisica__fundamentos.json")
json.dump(out, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"Escrito {fp} con {len(out)} microlecciones:")
for k in out:
    print(" -", k)
