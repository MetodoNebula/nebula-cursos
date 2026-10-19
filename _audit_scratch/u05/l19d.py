# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("H5_mcq4stem", r'''"stem": "¿Cuál de las siguientes es la razón termodinámica exacta (no aproximada) por la que un sólido puro no aparece en K?",''',
r'''"stem": "¿Cuál es la razón termodinámica por la que un sólido puro no aparece en K?",'''
))

edits.append(("H5_challenge_statement", r'''"statement": "Justifica, a partir de la idea de actividad termodinámica (actividad de un sólido o líquido puro = 1), por qué la regla «los sólidos y líquidos puros no aparecen en K» no es una simplificación aproximada, sino una consecuencia exacta de cómo se define rigurosamente la constante de equilibrio.",''',
r'''"statement": "(Ampliación, no exigible en PAU.) Justifica, a partir de la idea de actividad termodinámica (actividad de un sólido o líquido puro = 1 en su estado estándar), por qué la regla «los sólidos y líquidos puros no aparecen en K» no se basa en que su concentración sea pequeña o casi constante, sino en la propia definición de actividad de una fase pura.",'''
))

edits.append(("H5_challenge_answer", r'''"answer": "Porque la actividad de un sólido o líquido puro en su estado estándar es exactamente 1 por definición, así que ese factor desaparece de $K=\\prod a_i^{\\nu_i}$ sin ninguna aproximación.",''',
r'''"answer": "Porque la actividad de un sólido o líquido puro en su estado estándar es 1 por definición (y, a presiones ordinarias, prácticamente 1 sea cual sea la cantidad presente), así que ese factor desaparece de $K=\\prod a_i^{\\nu_i}$, no por ser «despreciable» sino por su propia definición.",'''
))

edits.append(("H5_challenge_fullsol", r'''"full_solution": "La constante de equilibrio termodinámicamente rigurosa se escribe como $K=\\prod_i a_i^{\\nu_i}$, donde $a_i$ es la actividad de cada especie. Para un gas ideal, $a_i\\approx P_i/P^\\circ$; para un soluto diluido, $a_i\\approx [i]/c^\\circ$; pero para un sólido o un líquido puro en su propio estado estándar, la actividad se define exactamente como $a_i=1$, independientemente de cuánta cantidad de esa sustancia haya presente (mientras siga siendo pura). Por tanto, el factor correspondiente a cada sólido o líquido puro en el producto $\\prod a_i^{\\nu_i}$ es $1^{\\nu_i}=1$, y desaparece sin aproximar nada: no es que su efecto sea «despreciable», es que, por la propia definición de actividad de una fase pura, su contribución es exactamente la unidad.",
        "common_errors": [
          "Explicar la regla como una aproximación («su concentración casi no cambia») en vez de como una consecuencia exacta de la definición de actividad de una fase pura."
        ],''',
r'''"full_solution": "La constante de equilibrio termodinámicamente rigurosa se escribe como $K=\\prod_i a_i^{\\nu_i}$, donde $a_i$ es la actividad de cada especie. Para un gas ideal, $a_i=P_i/P^\\circ$ (exacto); para un soluto diluido, $a_i\\approx[i]/c^\\circ$; y para un sólido o un líquido puro en su propio estado estándar, la actividad es $a_i=1$, y a presiones ordinarias sigue siendo prácticamente 1, independientemente de cuánta cantidad de esa sustancia haya presente (mientras siga siendo pura; a presiones muy altas hay una pequeña corrección, fuera del nivel de este curso). Por tanto, el factor correspondiente a cada sólido o líquido puro en el producto $\\prod a_i^{\\nu_i}$ es (prácticamente) $1^{\\nu_i}=1$, y desaparece de $K$: no es que su efecto sea «despreciable» por tener poca influencia, sino que, por la propia definición de actividad de una fase pura, su contribución es (prácticamente) la unidad, algo distinto a decir que su concentración es pequeña.",
        "common_errors": [
          "Explicar la regla como si la concentración del sólido o líquido puro fuera «pequeña» o «casi constante», en vez de apelar a la definición de actividad de una fase pura.",
          "Olvidar que, estrictamente, la actividad de una fase pura es exactamente 1 solo en su estado estándar (presión $P^\\circ$); a otras presiones es solo prácticamente 1, salvo a presiones muy altas."
        ],'''
))

results = []
ok_all = True
for label, old, new in edits:
    n = data.count(old)
    results.append((label, n))
    if n == 1:
        data = data.replace(old, new, 1)
    else:
        ok_all = False
for lb, cnt in results:
    print(lb, cnt)
if ok_all:
    open(PATH, "w", encoding="utf-8").write(data)
    print("ALL WRITTEN")
else:
    print("ABORT")
