import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"24_Propiedades')
i1 = data.find('"25_', i0)
seg = data[i0:i1]

def rep(old, new, expect, label):
    global seg
    c = seg.count(old)
    if c != expect:
        print("MISMATCH", label, "expected", expect, "got", c)
        idx = seg.find(old[:50])
        print("near:", repr(seg[max(0,idx-20):idx+200]))
        sys.exit(1)
    seg = seg.replace(old, new)
    print("OK", label, c)

BS = chr(92)*2

# F9a: worked_examples[3].statement — LaTeX pKa
old = "El ácido acético tiene pKa≈4,8 y el etanol pKa≈16."
new = "El ácido acético tiene $pK_a" + BS + "approx4{,}8$ y el etanol $pK_a" + BS + "approx16$."
rep(old, new, 1, "F9a statement")

# F9b: worked_examples[3].reasoning[0]
old = "pKa=-log Ka, así que Ka=10^-pKa; el cociente de dos Ka es 10 elevado a la diferencia de los pKa, con el signo adecuado."
new = "$" + BS + "mathrm{p}K_a=-" + BS + "log K_a$, así que $K_a=10^{-" + BS + "mathrm{p}K_a}$; el cociente de dos $K_a$ es 10 elevado a la diferencia de los $pK_a$, con el signo adecuado."
rep(old, new, 1, "F9b reasoning0")

# F9c: worked_examples[3].reasoning[1]
old = "Ka(ácido)/Ka(etanol)=10^(16-4,8)=10^11,2."
new = "$K_a(" + BS + "text{ácido})/K_a(" + BS + "text{etanol})=10^{16-4{,}8}=10^{11{,}2}$."
rep(old, new, 1, "F9c reasoning1")

# F9d: flashcards[7].back
old = "Ka(A)/Ka(B) = 10^(pKa(B)-pKa(A)); nunca se divide directamente un pKa entre otro."
new = "$K_a(A)/K_a(B) = 10^{" + BS + "mathrm{p}K_a(B)-" + BS + "mathrm{p}K_a(A)}$; nunca se divide directamente un $pK_a$ entre otro."
rep(old, new, 1, "F9d flashcards7")

# F11: mcq[4].explanation — "de los cinco" -> "de los cuatro"
old = "El butano es el único de los cinco sin ningún átomo electronegativo"
new = "El butano es el único de los cuatro sin ningún átomo electronegativo"
rep(old, new, 1, "F11 mcq4")

# F13a: guided_exercises[1].hints[1]
old = "Para (b), cuenta los carbonos que no llevan ningún grupo -OH."
new = "Para (b), cuenta los carbonos de la cadena de cada compuesto."
rep(old, new, 1, "F13a hint")

# F13b: guided_exercises[1].common_errors[0]
old = "Razonar solo a partir de la masa molecular parecida y concluir que la solubilidad también debería ser parecida."
new = "Pensar que, al ser más pesado, el 1-hexanol debería ser igual o más soluble que el etano-1,2-diol, sin tener en cuenta el número de grupos -OH ni la longitud de la cadena apolar."
rep(old, new, 1, "F13b common_errors")

# F18a: exercises[1].statement
old = "con la misma cantidad de grupos -COOH pero más del doble de carbonos, solo se disuelve de forma limitada."
new = "con la misma cantidad de grupos -COOH pero el doble de carbonos (6 frente a 3), solo se disuelve de forma limitada."
rep(old, new, 1, "F18a statement")

# F18b: exercises[1].full_solution
old = "el ácido hexanoico tiene una cadena casi tres veces más larga (5 carbonos)"
new = "el ácido hexanoico tiene una cadena 2,5 veces más larga (5 carbonos frente a 2)"
rep(old, new, 1, "F18b full_solution")

# F19: mcq[0].options[0].why_wrong
old = "No basta con contener el átomo electronegativo: hace falta además que algún H esté unido directamente a él, como en un éter o una cetona, que tienen O pero no pueden donar."
new = "No basta con contener el átomo electronegativo: hace falta además que algún H esté unido directamente a él. Un éter o una cetona, por ejemplo, tienen O pero no pueden donar."
rep(old, new, 1, "F19 mcq0")

# F20: misconceptions[0].correct_model
old = "una diferencia de casi 87°C causada únicamente por que uno puede formar enlaces de hidrógeno (tiene H unido a O) y el otro no."
new = "una diferencia de casi 87°C debida, sobre todo, a que uno puede formar enlaces de hidrógeno (tiene H unido a O) y el otro no."
rep(old, new, 1, "F20 misconceptions0")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE E")
