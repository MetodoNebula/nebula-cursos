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

def mrightleft(cond):
    return BS + 'overset{' + cond + '}{' + BS + 'rightleftharpoons}'

# 1. worked_examples[0].solution
old = 'CH3COOH + CH3CH2OH ⇌(H2SO4)⇌ CH3COOCH2CH3 + H2O (acetato de etilo).'
new = '$' + BS + 'mathrm{CH_3COOH + CH_3CH_2OH ' + mrightleft('H_2SO_4') + ' CH_3COOCH_2CH_3 + H_2O}$ (acetato de etilo).'
data = apply(data, old, new, '1 worked_examples[0].solution')

# 2. worked_examples[1].solution
old = 'CH3CH2CH2COOH + CH3OH ⇌(H2SO4)⇌ CH3CH2CH2COOCH3 + H2O.'
new = '$' + BS + 'mathrm{CH_3CH_2CH_2COOH + CH_3OH ' + mrightleft('H_2SO_4') + ' CH_3CH_2CH_2COOCH_3 + H_2O}$.'
data = apply(data, old, new, '2 worked_examples[1].solution')

# 3. guided_exercises[0].full_solution (metanoato)
old = "liberando agua: HCOOH + CH3CH2CH2OH ⇌(H2SO4)⇌ HCOOCH2CH2CH3 + H2O. La parte"
new = ('liberando agua: $' + BS + 'mathrm{HCOOH + CH_3CH_2CH_2OH ' + mrightleft('H_2SO_4')
       + ' HCOOCH_2CH_2CH_3 + H_2O}$. La parte')
data = apply(data, old, new, '3 guided_exercises metanoato')

# 4. guided_exercises[1] or exercises hydrolysis
old = "de partida: CH3COOCH2CH3+H2O ⇌(H+)⇌ CH3COOH+CH3CH2OH. Es, literalmente"
new = ('de partida: $' + BS + 'mathrm{CH_3COOCH_2CH_3 + H_2O ' + mrightleft('H^+')
       + ' CH_3COOH + CH_3CH_2OH}$. Es, literalmente')
data = apply(data, old, new, '4 hydrolysis eq')

# 5. propan-2-ol / isopropilo esterification
old = "liberando agua: CH3CH2COOH+(CH3)2CHOH ⇌(H2SO4)⇌ CH3CH2COOCH(CH3)2+H2O. Contando átomos"
new = ('liberando agua: $' + BS + 'mathrm{CH_3CH_2COOH + (CH_3)_2CHOH ' + mrightleft('H_2SO_4')
       + ' CH_3CH_2COOCH(CH_3)_2 + H_2O}$. Contando átomos')
data = apply(data, old, new, '5 propanoico+isopropilo eq')

# 6. exam_questions[0].answer
old = "(a) CH3CH2CH2COOH+CH3OH ⇌(H2SO4)⇌ CH3CH2CH2COOCH3+H2O (butanoato de metilo). (b)"
new = ('(a) $' + BS + 'mathrm{CH_3CH_2CH_2COOH + CH_3OH ' + mrightleft('H_2SO_4')
       + ' CH_3CH_2CH_2COOCH_3 + H_2O}$ (butanoato de metilo). (b)')
data = apply(data, old, new, '6 exam_questions[0].answer')

# 7. exam_questions[1].full_solution (both ácido and básico)
old = "(a) En medio ácido: CH3CH2COOCH3+H2O ⇌(H+)⇌ CH3CH2COOH+CH3OH. En medio básico: CH3CH2COOCH3+NaOH→CH3CH2COONa+CH3OH. (b)"
new = ('(a) En medio ácido: $' + BS + 'mathrm{CH_3CH_2COOCH_3 + H_2O ' + mrightleft('H^+')
       + ' CH_3CH_2COOH + CH_3OH}$. En medio básico: $' + BS
       + 'mathrm{CH_3CH_2COOCH_3 + NaOH ' + BS + 'rightarrow CH_3CH_2COONa + CH_3OH}$. (b)')
data = apply(data, old, new, '7 exam_questions[1].full_solution')

# 8. flashcards general equation
old = "\"back\": \"R-COOH + HO-R' ⇌(H2SO4)⇌ R-COO-R' + H2O.\""
new = ('"back": "$' + BS + "mathrm{R{-}COOH + HO{-}R' " + mrightleft('H_2SO_4')
       + " R{-}COO{-}R' + H_2O}$.\"")
data = apply(data, old, new, '8 flashcards general eq')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
