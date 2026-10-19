PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

edits = []

edits.append(("A_keywords2",
r'''Fracción de la cantidad inicial que se ha disociado, $\\alpha=x/n_0$, entre 0 y 1.''',
r'''Fracción de reactivo disociada: (moles de reactivo disociados)/(moles iniciales) $=a\\,x/n_0$, para un reactivo de coeficiente $a$; si $a=1$, $\\alpha=x/n_0$. Entre 0 y 1.'''
))

edits.append(("B_FC3_back",
r'''$\\alpha=x/n_0$: misma variable que $x$, expresada como fracción del valor inicial, entre 0 y 1.''',
r'''$\\alpha=a\\,x/n_0$ (si el coeficiente del reactivo es $a=1$, $\\alpha=x/n_0$): misma información que $x$, expresada como fracción del valor inicial, entre 0 y 1.'''
))

edits.append(("C_FC4_back",
r'''Se usa $x$ cuando el dato que falta es una cantidad absoluta; se usa $\\alpha$ cuando el dato es (o se pide) un porcentaje de disociación. Son la misma variable en dos formas distintas.''',
r'''Se usa $x$ cuando el dato que falta es una cantidad absoluta; se usa $\\alpha$ cuando el dato es (o se pide) un porcentaje de disociación. Son la misma información en dos formas distintas, relacionadas por $\\alpha=a\\,x/n_0$ (coeficiente $a$ del reactivo; si $a=1$, $\\alpha=x/n_0$).'''
))

edits.append(("D_summary_keypoint1",
r'''$\\alpha=x/n_0$: misma variable, distinta forma de expresarla.''',
r'''$\\alpha=a\\,x/n_0$ (coeficiente $a$ del reactivo; si $a=1$, $\\alpha=x/n_0$): misma información, distinta forma de expresarla.'''
))

edits.append(("E_summary_formula0",
r'''"\\alpha=\\frac{x}{n_0}",''',
r'''"\\alpha=\\frac{a\\,x}{n_0}\\ \\text{(coef. }a\\text{ del reactivo; si }a=1,\\ \\alpha=x/n_0\\text{)}",'''
))

edits.append(("H6_exam_notes2",
r'''Si la ecuación no es 1:1 con coeficiente unitario para el reactivo (p. ej. $\\text{N}_2\\text{O}_4\\rightleftharpoons 2\\text{NO}_2$, o $2\\text{SO}_3\\rightleftharpoons 2\\text{SO}_2+\\text{O}_2$), no se puede usar $\\alpha=x/n_0$ directamente en la fila de productos sin multiplicar por el coeficiente correspondiente. Para el caso $\\text{N}_2\\text{O}_4\\rightleftharpoons 2\\text{NO}_2$: el cambio en $\\text{NO}_2$ es $+2x=2n_0\\alpha$, no $+n_0\\alpha$.''',
r'''Cada cambio en la tabla es coeficiente $\\times x$. Si el reactivo tiene coeficiente 1 ($\\text{N}_2\\text{O}_4\\rightleftharpoons 2\\text{NO}_2$), entonces $x=n_0\\alpha$ y el $\\text{NO}_2$ aumenta $2x=2n_0\\alpha$. Si el reactivo tiene coeficiente $a>1$ ($2\\text{SO}_3\\rightleftharpoons 2\\text{SO}_2+\\text{O}_2$), los moles de reactivo disociados son $n_0\\alpha=2x$, luego $x=n_0\\alpha/2$.'''
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
    print("ABORT - not all unique")
