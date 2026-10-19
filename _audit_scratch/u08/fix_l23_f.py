import sys
PATH = "/sessions/rcw-015astzm9paxeees2msu1v35/mnt/Nebula_Cursos_Web/bundles/selectividad_quimica__U08_Organica.json"
with open(PATH, "r", encoding="utf-8") as f:
    data = f.read()

i0 = data.find('"23_Condiciones')
i1 = data.find('"24_', i0)
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

# F13: exercises[2] — concrete propeno instead of generic "Un alqueno"
old_stmt = "Un alqueno se trata, por separado, con: (i) H2 con catalizador de Pt; (ii) H2O en medio ácido fuerte. Ambos son adiciones, pero dan productos de familias distintas. Indica el producto de cada una y explica por qué hace falta un catalizador distinto en cada caso."
new_stmt = "El propeno (CH2=CH-CH3) se trata, por separado, con: (i) H2 con catalizador de Pt; (ii) H2O en medio ácido fuerte. Ambos son adiciones, pero dan productos de familias distintas. Indica el producto (fórmula y nombre) de cada una, aplicando Markovnikov donde corresponda, y explica por qué hace falta un catalizador distinto en cada caso."
rep(old_stmt, new_stmt, 1, "F13 statement")

old_ans = "(i) Alcano (hidrogenación catalítica). (ii) Alcohol (hidratación ácida)."
new_ans = "(i) Propano, CH3-CH2-CH3 (hidrogenación catalítica). (ii) Propan-2-ol, CH3-CH(OH)-CH3 (hidratación ácida, Markovnikov)."
rep(old_ans, new_ans, 1, "F13 answer")

old_fs = "(i) H2 con catalizador metálico (Pt, Pd o Ni) da un alcano: el doble enlace se satura con dos H. El catalizador es necesario porque el H2, por sí solo, apenas reacciona con el doble enlace a temperatura ambiente; el metal facilita la ruptura del enlace H-H. (ii) H2O en medio ácido fuerte da un alcohol (Markovnikov): se incorpora H a un carbono y OH al otro."
new_fs = "(i) H2 con catalizador metálico (Pt, Pd o Ni) da propano, CH3-CH2-CH3: el doble enlace se satura con dos H. El catalizador es necesario porque el H2, por sí solo, apenas reacciona con el doble enlace a temperatura ambiente; el metal facilita la ruptura del enlace H-H. (ii) H2O en medio ácido fuerte da propan-2-ol, CH3-CH(OH)-CH3 (Markovnikov): el OH se incorpora al carbono central, que es el más sustituido, y el H al carbono terminal."
rep(old_fs, new_fs, 1, "F13 full_solution")

# F14: worked_examples[1].solution — E/Z isomerism of but-2-ene
old = "El producto mayoritario es el but-2-eno: su doble enlace está entre los dos carbonos centrales, ambos más sustituidos que los extremos, frente al but-1-eno, minoritario."
new = "El producto mayoritario es el but-2-eno, principalmente como el isómero (E) (trans), más estable que el (Z) por el menor impedimento estérico entre los grupos metilo: su doble enlace está entre los dos carbonos centrales, ambos más sustituidos que los extremos, frente al but-1-eno, minoritario."
rep(old, new, 1, "F14 worked_examples[1]")

# F15: worked_examples[2].solution — IUPAC names + formulas
old = "(i) Predomina la sustitución (SN2: CH3-CH(OH)-CH2-CH3 + NaBr). (ii) Predomina la eliminación (E2: mezcla de but-1-eno y but-2-eno, con but-2-eno mayoritario por Saytzeff, + NaBr + H2O)."
new = "(i) Predomina la sustitución (SN2: CH3-CH(OH)-CH2-CH3, butan-2-ol, + NaBr). (ii) Predomina la eliminación (E2: mezcla de CH2=CH-CH2-CH3, but-1-eno, y CH3-CH=CH-CH3, but-2-eno, mayoritario por Saytzeff, + NaBr + H2O)."
rep(old, new, 1, "F15 worked_examples[2]")

data2 = data[:i0] + seg + data[i1:]
with open(PATH, "w", encoding="utf-8") as f:
    f.write(data2)
print("DONE F")
