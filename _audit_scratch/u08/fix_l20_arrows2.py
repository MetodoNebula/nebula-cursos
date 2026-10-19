path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2

def apply(data, old, new, label, expect=1):
    c = data.count(old)
    if c == expect:
        data = data.replace(old, new)
        print('OK', label, c)
    else:
        print('MISMATCH', label, 'expected', expect, 'got', c)
    return data

# objectives[0] statement
old = "Escribir la reacción de esterificación R-COOH + HO-R' ⇌ R-COO-R' + H2O, identificando el catalizador típico (ácido sulfúrico) y el subproducto"
new = ("Escribir la reacción de esterificación $" + BS + "mathrm{R{-}COOH + HO{-}R' " + BS
       + "rightleftharpoons R{-}COO{-}R' + H_2O}$, identificando el catalizador típico (ácido sulfúrico) y el subproducto")
data = apply(data, old, new, 'objectives[0]')

# guided_exercises propilo answer
old = "(a) HCOOH + CH3CH2CH2OH ⇌ HCOOCH2CH2CH3 + H2O. (b) Metanoato de propilo."
new = ("(a) $" + BS + "mathrm{HCOOH + CH_3CH_2CH_2OH " + BS
       + "rightleftharpoons HCOOCH_2CH_2CH_3 + H_2O}$. (b) Metanoato de propilo.")
data = apply(data, old, new, 'guided_exercises propilo answer')

# NaOH saponification side-note
old = 'reacciona de inmediato con el NaOH y se convierte en acetato de sodio: CH3COOCH2CH3+NaOH→CH3COONa+CH3CH2OH. Al no quedar'
new = ('reacciona de inmediato con el NaOH y se convierte en acetato de sodio: $' + BS
       + 'mathrm{CH_3COOCH_2CH_3 + NaOH ' + BS + 'rightarrow CH_3COONa + CH_3CH_2OH}$. Al no quedar')
data = apply(data, old, new, 'saponification side-note')

# exercises[2] isopropilo (finding 4/5 analog + 12 naming)
old = 'CH3CH2COOH + (CH3)2CHOH ⇌ CH3CH2COOCH(CH3)2 + H2O; propanoato de isopropilo.'
new = ('$' + BS + 'mathrm{CH_3CH_2COOH + (CH_3)_2CHOH ' + BS
       + 'rightleftharpoons CH_3CH_2COOCH(CH_3)_2 + H_2O}$; propanoato de propan-2-ilo (isopropilo).')
data = apply(data, old, new, 'exercises[2] isopropilo answer')

# mcq options A-D
old = '"text": "R-COOH + NaOH → R-COONa + H2O"'
new = '"text": "$' + BS + 'mathrm{R{-}COOH + NaOH ' + BS + 'rightarrow R{-}COONa + H_2O}$"'
data = apply(data, old, new, "mcq optA")

old = "\"text\": \"R-COOH + HO-R' ⇌ R-COO-R' + H2O\""
new = "\"text\": \"$" + BS + "mathrm{R{-}COOH + HO{-}R' " + BS + "rightleftharpoons R{-}COO{-}R' + H_2O}$\""
data = apply(data, old, new, "mcq optB")

old = '"text": "R-X + OH⁻ → R-OH + X⁻"'
new = '"text": "$' + BS + 'mathrm{R{-}X + OH^- ' + BS + 'rightarrow R{-}OH + X^-}$"'
data = apply(data, old, new, "mcq optC")

old = "\"text\": \"R-COO-R' + NaOH → R-COONa + HO-R'\""
new = "\"text\": \"$" + BS + "mathrm{R{-}COO{-}R' + NaOH " + BS + "rightarrow R{-}COONa + HO{-}R'}$\""
data = apply(data, old, new, "mcq optD")

# key_points
old = "Reacción: R-COOH+HO-R'⇌R-COO-R'+H2O, catalizada por ácido (p. ej. H2SO4)."
new = ("Reacción: $" + BS + "mathrm{R{-}COOH + HO{-}R' " + BS
       + "rightleftharpoons R{-}COO{-}R' + H_2O}$, catalizada por ácido (p. ej. H$_2$SO$_4$).")
data = apply(data, old, new, "key_points reaction")

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
