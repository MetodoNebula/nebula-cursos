import json

path = 'bundles/selectividad_quimica__U08_Organica.json'
data = open(path, encoding='utf-8').read()
BS = chr(92) * 2

def apply(data, old, new, label):
    c = data.count(old)
    if c == 1:
        data = data.replace(old, new)
        print('OK', label)
    elif c == 0:
        print('NOT FOUND', label)
    else:
        print('MULTIPLE', c, label)
    return data

# Finding 3: statement name correction
old = 'partiendo de 1-bromoetano, que termine en etilmetilamina (CH3CH2-NH-CH3, una amina secundaria con un grupo etilo y un grupo metilo sobre el mismo nitrógeno)'
new = 'partiendo de bromoetano, que termine en N-metiletanamina (etilmetilamina; CH3CH2-NH-CH3, una amina secundaria con un grupo etilo y un grupo metilo sobre el mismo nitrógeno)'
data = apply(data, old, new, 'statement name/locant')

# Finding 1+2: fix balanced equations & unify answer/full_solution, correct IUPAC name
old_answer = 'Paso 1: CH3CH2Br + NH3(exceso) → CH3CH2NH2 + NH4Br (etilamina). Paso 2: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + CH3CH2NH₃⁺·Br⁻ (la base de la etilamina en exceso captura el HBr; etilmetilamina).'
new_answer = 'Paso 1: CH3CH2Br + 2 NH3(exceso) → CH3CH2NH2 + NH4Br (etanamina/etilamina). Paso 2: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + HBr (N-metiletanamina/etilmetilamina; el HBr es neutralizado por el exceso de NH3 o de etilamina presente).'
data = apply(data, old_answer, new_answer, 'challenge answer')

old_fs1 = 'con amoniaco en gran exceso para evitar sobresustitución: CH3CH2Br + NH3(exceso) → CH3CH2NH2 + NH4Br, que da etilamina.'
new_fs1 = 'con amoniaco en gran exceso para evitar sobresustitución: CH3CH2Br + 2 NH3(exceso) → CH3CH2NH2 + NH4Br, que da etanamina (etilamina).'
data = apply(data, old_fs1, new_fs1, 'challenge full_solution step1')

old_fs2 = 'desplazando el bromo: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + HBr. Aquí interesa justo lo contrario que en el paso 1'
new_fs2 = 'desplazando el bromo: CH3CH2NH2 + CH3Br → CH3CH2-NH-CH3 + HBr, formando N-metiletanamina (etilmetilamina). Aquí interesa justo lo contrario que en el paso 1'
data = apply(data, old_fs2, new_fs2, 'challenge full_solution step2 naming')

open(path, 'w', encoding='utf-8').write(data)
print('WRITTEN')
