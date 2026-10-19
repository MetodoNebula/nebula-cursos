PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U05_Equilibrio.json"
data = open(PATH, encoding="utf-8").read()

old = r'''"statement": "Para $PCl_5(g)\\rightleftharpoons PCl_3(g)+Cl_2(g)$, con $c_0=0{,}0500$ M y $K_c=1{,}80\\cdot10^{-3}$: (a) plantea y resuelve la ecuación de segundo grado completa (sin aproximar) para $x$, descartando la raíz sin sentido físico. (b) Verifica sustituyendo tu valor de $x$ de vuelta en la expresión de $K_c$. (c) Compara con el resultado aproximado del ejercicio guiado y confirma el error relativo.",
        "hints": [
          "Ordena $K_c(c_0-x)=x^2$ como $x^2+K_c\\,x-K_c c_0=0$ antes de aplicar la fórmula general.",
          "Las dos raíces de la cuadrática suman $-K_c$ y una de ellas es necesariamente negativa (producto de raíces $=-K_cc_0<0$): descártala sin calcularla explícitamente si no hace falta."
        ],
        "answer": "(a) $x=8{,}63\\cdot10^{-3}$ M (raíz positiva). (b) $K_c$ recalculado $=1{,}80\\cdot10^{-3}$, coincide con el dato. (c) Error relativo $\\approx9{,}9\\,\\%$ frente al valor aproximado.",
        "full_solution": "(a) $x^2+K_cx-K_cc_0=0$, con $K_c=1{,}80\\cdot10^{-3}$ y $c_0=0{,}0500$. Con la fórmula general, $x=8{,}63\\cdot10^{-3}$ M (la raíz negativa, del orden de $-0{,}0104$, se descarta por no tener sentido físico). (b) $[PCl_5]_{eq}=0{,}0414$ M; $[PCl_3]_{eq}=[Cl_2]_{eq}=0{,}00863$ M. $K_c=\\dfrac{0{,}00863^2}{0{,}0414}=1{,}80\\cdot10^{-3}$: coincide con el dato. (c) El valor aproximado del ejercicio guiado citado, $9{,}49\\cdot10^{-3}$ M, difiere del exacto en un $9{,}9\\,\\%$: por debajo del $10\\,\\%$ tolerado en algunos contextos, pero por encima del $1\\,\\%$ estricto.",
        "common_errors": [
          "Calcular explícitamente la raíz negativa como si fuera necesaria para la respuesta, en vez de descartarla directamente por el signo del producto de raíces.",
          "No verificar sustituyendo de vuelta."
        ],'''

n = data.count(old)
print("count:", n)

new = r'''"statement": "Para $PCl_5(g)\\rightleftharpoons PCl_3(g)+Cl_2(g)$, con $K_c=1{,}80\\cdot10^{-3}$, se introducen en el mismo recipiente $0{,}0500$ M de $PCl_5$ y, además, $0{,}0100$ M de $PCl_3$ ya presentes desde el principio (sin $Cl_2$ inicial). (a) Plantea la tabla ICE con este dato inicial distinto de cero y la ecuación de segundo grado completa para $x$ (aquí no es válido aproximar: compruébalo al final). (b) Resuélvela, descartando la raíz sin sentido físico. (c) Verifica sustituyendo tus concentraciones de equilibrio de vuelta en $K_c$.",
        "hints": [
          "La tabla ICE ahora es: $[PCl_5]=0{,}0500-x$; $[PCl_3]=0{,}0100+x$; $[Cl_2]=x$. Sustituye en $K_c=\\dfrac{(0{,}0100+x)\\,x}{0{,}0500-x}$ y ordena como ecuación de segundo grado: $x^2+0{,}0118\\,x-9{,}0\\cdot10^{-5}=0$.",
          "Si aun así aproximases $0{,}0500-x\\approx0{,}0500$, comprueba después que $x_{aprox}/c_0$ no queda por debajo del $5\\,\\%$: por eso aquí hay que resolver la cuadrática completa."
        ],
        "answer": "(a) $x^2+0{,}0118\\,x-9{,}0\\cdot10^{-5}=0$. (b) $x\\approx5{,}27\\cdot10^{-3}$ M (raíz positiva). (c) $[PCl_5]_{eq}=0{,}04473$ M, $[PCl_3]_{eq}=0{,}01527$ M, $[Cl_2]_{eq}=0{,}00527$ M; $K_c$ recalculado $=1{,}80\\cdot10^{-3}$, coincide con el dato.",
        "full_solution": "(a) Tabla ICE: $[PCl_5]=0{,}0500-x$; $[PCl_3]=0{,}0100+x$; $[Cl_2]=x$. Sustituyendo en $K_c=\\dfrac{(0{,}0100+x)\\,x}{0{,}0500-x}=1{,}80\\cdot10^{-3}$ y desarrollando: $0{,}0100x+x^2=9{,}0\\cdot10^{-5}-1{,}80\\cdot10^{-3}x$, es decir $x^2+0{,}0118\\,x-9{,}0\\cdot10^{-5}=0$. (b) Con la fórmula general, $x=\\dfrac{-0{,}0118\\pm\\sqrt{0{,}0118^2+4\\cdot9{,}0\\cdot10^{-5}}}{2}=\\dfrac{-0{,}0118\\pm\\sqrt{4{,}992\\cdot10^{-4}}}{2}=\\dfrac{-0{,}0118\\pm0{,}02234}{2}$. La raíz negativa ($\\approx-0{,}01707$ M) se descarta por no tener sentido físico; la raíz positiva es $x\\approx5{,}27\\cdot10^{-3}$ M. (c) $[PCl_5]_{eq}=0{,}0500-0{,}00527=0{,}04473$ M; $[PCl_3]_{eq}=0{,}0100+0{,}00527=0{,}01527$ M; $[Cl_2]_{eq}=0{,}00527$ M. Comprobando: $K_c=\\dfrac{0{,}01527\\times0{,}00527}{0{,}04473}=1{,}80\\cdot10^{-3}$, coincide con el dato. Nótese que $x/c_0=0{,}00527/0{,}0500\\approx10{,}5\\,\\%>5\\,\\%$: la aproximación habría sido claramente inválida, y además el propio $PCl_3$ inicial, comparable en magnitud a $x$, hace que no tenga sentido simplificarlo.",
        "common_errors": [
          "Olvidar que $[PCl_3]$ inicial no es cero y escribir la fila de equilibrio como $x$ en vez de $0{,}0100+x$.",
          "Aproximar $0{,}0500-x\\approx0{,}0500$ sin comprobar después que $x/c_0<5\\,\\%$."
        ],'''

if n == 1:
    data = data.replace(old, new, 1)
    open(PATH, "w", encoding="utf-8").write(data)
    print("WRITTEN")
else:
    print("ABORT - not unique, n=", n)
