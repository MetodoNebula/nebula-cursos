import sys
sys.path.insert(0, "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/_audit_scratch/u05")
from apply_edits import apply

edits = []

edits.append(("H1_H8_challenge_statement",
"Para la reacción $2A(g)\\rightleftharpoons B(g)+C(g)$, la constante de presión vale $K_p=12{,}0$ a $T_1=300$ K y $K_p=48{,}0$ a $T_2=600$ K (ambos valores adimensionales, pues $\\Delta n=0$ para esta reacción). Calcula el cociente $K_c(T_2)/K_c(T_1)$ y deduce si la reacción es exotérmica o endotérmica.",
"Para la reacción $\\text{N}_2\\text{O}_4(g)\\rightleftharpoons2\\,\\text{NO}_2(g)$, la constante de presión vale $K_p=0{,}17\\,\\mathrm{atm}$ a $T_1=300$ K y $K_p=3{,}9\\,\\mathrm{atm}$ a $T_2=350$ K. Calcula el cociente $K_c(T_2)/K_c(T_1)$ y deduce si la reacción (de izquierda a derecha) es exotérmica o endotérmica."
))

edits.append(("H1_H8_challenge_hint",
"Escribe $K_c=K_p/(RT)^{\\Delta n}$ para cada temperatura y forma el cociente: varios factores se simplifican antes de sustituir ningún número.",
"Escribe $K_c=K_p/(RT)^{\\Delta n}$ (con $\\Delta n=1$) para cada temperatura y forma el cociente: el factor $R$ se cancela, quedando solo $K_p$ y $T$."
))

edits.append(("H1_H8_challenge_answer",
"$K_c(T_2)/K_c(T_1)=4{,}00$.",
"$K_c(T_2)/K_c(T_1)\\approx19{,}7$; como $K_c$ aumenta mucho al subir $T$, la reacción directa es **endotérmica**."
))

edits.append(("H1_H8_challenge_fullsol",
"$\\Delta n=(1+1)-2=0$, así que $K_c=K_p/(RT)^0=K_p$ en ambos casos. Por tanto $K_c(T_2)/K_c(T_1)=K_p(T_2)/K_p(T_1)=48{,}0/12{,}0=4{,}00$.",
"$\\Delta n=2-1=1$, así que $K_c=K_p/(RT)^{1}=K_p/(RT)$ en cada temperatura. Por tanto:\n\n$$\\frac{K_c(T_2)}{K_c(T_1)}=\\frac{K_p(T_2)/(RT_2)}{K_p(T_1)/(RT_1)}=\\frac{K_p(T_2)}{K_p(T_1)}\\cdot\\frac{T_1}{T_2}=\\frac{3{,}9}{0{,}17}\\cdot\\frac{300}{350}\\approx22{,}9\\times0{,}857\\approx19{,}7$$\n\nComo $K_c$ (y $K_p$) aumentan mucho al pasar de 300 a 350 K, el equilibrio se desplaza hacia los productos al calentar; según el principio de Le Châtelier (que se estudia más adelante en esta unidad), un aumento de temperatura favorece siempre el sentido endotérmico. Como aquí favorece la reacción directa, esta es **endotérmica** ($\\Delta H^\\circ>0$), lo que es coherente con que la disociación de $\\text{N}_2\\text{O}_4$ en $\\text{NO}_2$ requiera romper un enlace N–N."
))

edits.append(("H1_H8_challenge_commonerr",
"Calcular $(RT)^{\\Delta n}$ para cada temperatura sin darse cuenta de que $\\Delta n=0$ hace ese paso innecesario.",
"Olvidar el factor $T_1/T_2$ al formar el cociente $K_c(T_2)/K_c(T_1)$ a partir de $K_p(T_2)/K_p(T_1)$, o concluir 'endotérmica' sin justificarlo con el aumento de $K_c$ al subir $T$ (Le Châtelier)."
))

ok = apply(edits)
print("DONE", ok)
