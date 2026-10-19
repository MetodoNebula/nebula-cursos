# -*- coding: utf-8 -*-
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''Si $C\\gg s'$ (aproximación habitual, que conviene comprobar al final), se simplifica a $K_{sp}\\approx s'\\,C$, de donde $s'\\approx\\dfrac{K_{sp}}{C}$: un valor mucho menor que la solubilidad $s=\\sqrt{K_{sp}}$ en agua pura.",'''

new = r'''Si $C\\gg s'$ (aproximación habitual, que conviene comprobar al final), se simplifica a $K_{sp}\\approx s'\\,C$, de donde $s'\\approx\\dfrac{K_{sp}}{C}$: un valor mucho menor que la solubilidad $s=\\sqrt{K_{sp}}$ en agua pura.\n\nPara una sal tipo $AB_2$, $A_xB_y(s)\\rightleftharpoons A^{2+}+2\\,B^-$, hay dos casos según cuál sea el ion común:\n- Si el ion común es el anión $B^-$ (concentración $C$): $K_{sp}=s'(C+2s')^2\\approx s'C^2$ (si $2s'\\ll C$), de donde $s'\\approx K_{sp}/C^2$.\n- Si el ion común es el catión $A^{2+}$ (concentración $C$): $K_{sp}=(C+s')(2s')^2\\approx4Cs'^2$ (si $s'\\ll C$), de donde $s'\\approx\\sqrt{K_{sp}/(4C)}$.\n\nEn ambos casos conviene comprobar al final que la aproximación usada ($2s'\\ll C$ o $s'\\ll C$) es razonable.",'''

n = data.count(old)
print("count:", n)
if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT")
